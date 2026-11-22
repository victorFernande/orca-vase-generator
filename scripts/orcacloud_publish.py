"""Publish verified GitHub release assets using OrcaCloud's GitHub OIDC API.

MIT License; Copyright (c) 2026 Victor Fernandes.
Only the publisher job runs this entry point; tests never contact either service.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import tomllib
import urllib.error
import urllib.request
import uuid

API = "https://api.orcaslicer.com/api/v1/plugin-publish/releases"
RECEIPT = "orcacloud-publish.json"
SEMVER = re.compile(r"v?(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?\Z")


def gh(*args: str):
    return subprocess.run(["gh", *args], check=True, text=True, capture_output=True).stdout


def metadata(tag: str, body: str) -> dict:
    if not SEMVER.fullmatch(tag):
        raise ValueError("Expected a semantic release tag, such as v1.4.1")
    return {"version": tag.removeprefix("v"), "changelog": body[:4000]}


def multipart(meta: dict, filename: str, content: bytes) -> tuple[str, bytes]:
    """Encode JSON literally, including curl-form metacharacters and Unicode."""
    boundary = "OrcaCloud" + uuid.uuid4().hex
    prefix = (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"metadata\"\r\n"
        "Content-Type: application/json; charset=utf-8\r\n\r\n"
        + json.dumps(meta, ensure_ascii=False)
        + f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"files\"; filename=\"{filename}\"\r\n"
        "Content-Type: text/x-python\r\n\r\n"
    ).encode("utf8")
    return boundary, prefix + content + f"\r\n--{boundary}--\r\n".encode("ascii")


def verify_asset(asset: dict, path: Path, meta: dict, plugin_id: str) -> str:
    if path.name != asset["name"] or not path.name.endswith("_any.py"):
        raise ValueError("Expected the universal _any.py release asset")
    content = path.read_bytes()
    digest = "sha256:" + hashlib.sha256(content).hexdigest()
    if digest != asset.get("digest"):
        raise ValueError("Downloaded release asset failed SHA-256 verification")
    text = content.decode("utf8")
    block = text.split("# /// script\n", 1)[1].split("# ///", 1)[0]
    pep = tomllib.loads("\n".join(line.removeprefix("# ").removeprefix("#") for line in block.splitlines()))
    plugin = pep["tool"]["orcaslicer"]["plugin"]
    if plugin["version"] != meta["version"] or plugin["id"] != plugin_id:
        raise ValueError("Release tag, package version or plugin identity does not match")
    return digest


def ci_approved(runs: list[dict], sha: str) -> bool:
    return any(r.get("head_sha") == sha and r.get("event") == "push"
               and r.get("status") == "completed" and r.get("conclusion") == "success" for r in runs)


def receipt_matches(receipt: dict, repo: str, meta: dict, digest: str, cloud_id: str) -> bool:
    return (receipt.get("repository") == repo and receipt.get("version") == meta["version"]
            and receipt.get("sha256") == digest and receipt.get("plugin_id") == cloud_id)


def request_json(request: urllib.request.Request, expected_status: int = 200) -> dict:
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            if response.status != expected_status:
                raise RuntimeError(f"Expected HTTP {expected_status}, received {response.status}")
            return json.load(response)
    except urllib.error.HTTPError as error:
        details = error.read().decode("utf8", errors="replace")[:2000]
        raise RuntimeError(f"HTTP {error.code}: {details}") from None


def announce(message: str):
    print(message)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf8") as stream:
            stream.write(message + "\n")


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("Publication must run inside GitHub Actions")
    repo, tag = os.environ["GITHUB_REPOSITORY"], os.environ["RELEASE_TAG"]
    filename, plugin_id, cloud_id = (os.environ[k] for k in ("PLUGIN_FILE", "PLUGIN_ID", "CLOUD_PLUGIN_ID"))
    if Path(filename).name != filename or not filename.endswith("_any.py"):
        raise ValueError("Invalid publisher asset filename")
    metadata(tag, "")  # Validate before using the tag in a command or API path.
    release = json.loads(gh("release", "view", tag, "--repo", repo, "--json", "tagName,isDraft,body,assets"))
    if release["tagName"] != tag:
        raise ValueError("GitHub returned a different release")
    if release["isDraft"]:
        announce(f"{tag}: draft release; publication will wait for release.published.")
        return
    meta = metadata(tag, release.get("body") or "")
    sha = json.loads(gh("api", f"repos/{repo}/commits/{tag}"))["sha"]
    runs = json.loads(gh("api", f"repos/{repo}/actions/workflows/ci.yml/runs?head_sha={sha}&per_page=100"))["workflow_runs"]
    if not ci_approved(runs, sha):
        announce(f"{tag}: waiting for successful CI on the released commit; workflow_run will retry.")
        return
    assets = [a for a in release["assets"] if a["name"] == filename]
    if len(assets) != 1:
        raise ValueError("Release must contain exactly one universal plugin asset")
    with tempfile.TemporaryDirectory(prefix="orcacloud-publish-") as temporary:
        folder = Path(temporary)
        gh("release", "download", tag, "--repo", repo, "--pattern", filename, "--dir", temporary)
        package = folder / filename
        digest = verify_asset(assets[0], package, meta, plugin_id)
        if any(a["name"] == RECEIPT for a in release["assets"]):
            gh("release", "download", tag, "--repo", repo, "--pattern", RECEIPT, "--dir", temporary)
            receipt = json.loads((folder / RECEIPT).read_text(encoding="utf8"))
            if receipt_matches(receipt, repo, meta, digest, cloud_id):
                announce(f"{tag}: already published with the same package; verified receipt, no upload repeated.")
                return
        oidc_url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"] + "&audience=orcacloud"
        token = request_json(urllib.request.Request(oidc_url, headers={
            "Authorization": "Bearer " + os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"]}))["value"]
        boundary, payload = multipart(meta, filename, package.read_bytes())
        result = request_json(urllib.request.Request(API, data=payload, method="POST", headers={
            "Authorization": "Bearer " + token, "Content-Type": "multipart/form-data; boundary=" + boundary}), expected_status=201)
        if result.get("id") != cloud_id or result.get("version") != meta["version"]:
            raise ValueError("OrcaCloud did not confirm the expected plugin and version")
        receipt = {"repository": repo, "version": meta["version"], "sha256": digest,
                   "plugin_id": cloud_id, "source_commit": sha,
                   "run_url": f"https://github.com/{repo}/actions/runs/{os.environ['GITHUB_RUN_ID']}"}
        (folder / RECEIPT).write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf8")
        gh("release", "upload", tag, str(folder / RECEIPT), "--repo", repo, "--clobber")
        announce(f"Published {meta['version']} to OrcaCloud, plugin {cloud_id}. Release package SHA-256 verified.")


if __name__ == "__main__":
    main()
