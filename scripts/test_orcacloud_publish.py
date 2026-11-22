"""Offline publisher regressions: no credentials, uploads, or external services."""
import hashlib
import io
import json
from email import policy
from email.parser import BytesParser
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import orcacloud_publish as publisher
from orcacloud_publish import ci_approved, metadata, multipart, receipt_matches, verify_asset


class PublisherTests(unittest.TestCase):
    def test_unicode_and_curl_form_metacharacters_survive_the_real_multipart_parser(self):
        body = 'Português 日本語; type=text/plain; filename=x; @file, "aspas"\n' * 150
        meta = metadata("v1.4.1", body)
        boundary, encoded = multipart(meta, "plugin_any.py", b"# plugin\n")
        message = BytesParser(policy=policy.default).parsebytes(
            f"Content-Type: multipart/form-data; boundary={boundary}\r\nMIME-Version: 1.0\r\n\r\n".encode() + encoded)
        parts = list(message.iter_parts())
        self.assertEqual(len(parts), 2)
        self.assertEqual(json.loads(parts[0].get_content()), meta)
        self.assertEqual(meta["changelog"], body[:4000])
        self.assertEqual(parts[1].get_payload(decode=True), b"# plugin\n")
        self.assertEqual(parts[1].get_filename(), "plugin_any.py")

    def test_only_successful_push_ci_on_the_exact_release_commit_authorizes_publication(self):
        run = {"head_sha": "abc", "event": "push", "status": "completed", "conclusion": "success"}
        self.assertTrue(ci_approved([run], "abc"))
        for key, value in (("head_sha", "other"), ("event", "pull_request"),
                           ("status", "in_progress"), ("conclusion", "failure")):
            self.assertFalse(ci_approved([{**run, key: value}], "abc"))
        self.assertFalse(ci_approved([], "abc"))

    def test_tag_validation_blocks_command_options_and_api_path_injection(self):
        for tag in ("--repo", "main", "v1.2.3/../../main", "v1.2.3\n", "v01.2.3"):
            with self.assertRaises(ValueError):
                metadata(tag, "notes")
        self.assertEqual(metadata("v1.4.1", "notes")["version"], "1.4.1")

    def test_release_bytes_version_and_identity_must_match_before_upload(self):
        content = b'# /// script\n# [tool.orcaslicer.plugin]\n# version = "1.4.1"\n# id = "test-plugin"\n# ///\n'
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "test_any.py"
            path.write_bytes(content)
            digest = "sha256:" + hashlib.sha256(content).hexdigest()
            asset = {"name": path.name, "digest": digest}
            self.assertEqual(verify_asset(asset, path, metadata("v1.4.1", ""), "test-plugin"), digest)
            for meta, identity, bad_asset in ((metadata("v1.4.2", ""), "test-plugin", asset),
                                              (metadata("v1.4.1", ""), "other-plugin", asset),
                                              (metadata("v1.4.1", ""), "test-plugin", {**asset, "digest": "bad"})):
                with self.assertRaises(ValueError):
                    verify_asset(bad_asset, path, meta, identity)

    def test_receipt_never_skips_another_plugin_version_or_package(self):
        receipt = {"repository": "owner/repo", "version": "1.4.1", "sha256": "sha256:abc", "plugin_id": "cloud-id"}
        self.assertTrue(receipt_matches(receipt, "owner/repo", metadata("v1.4.1", ""), "sha256:abc", "cloud-id"))
        for key in receipt:
            with self.subTest(key=key):
                self.assertFalse(receipt_matches({**receipt, key: "other"}, "owner/repo", metadata("v1.4.1", ""), "sha256:abc", "cloud-id"))

    def test_legacy_name_only_manifest_requires_the_explicit_expected_name(self):
        content = b'# /// script\n# [tool.orcaslicer.plugin]\n# version = "1.4.1"\n# name = "Orca Gear Studio"\n# ///\n'
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "gear_any.py"
            path.write_bytes(content)
            asset = {"name": path.name, "digest": "sha256:" + hashlib.sha256(content).hexdigest()}
            self.assertEqual(verify_asset(asset, path, metadata("v1.4.1", ""), "gear-id", "Orca Gear Studio"), asset["digest"])
            for name in (None, "Another plugin"):
                with self.assertRaises(ValueError):
                    verify_asset(asset, path, metadata("v1.4.1", ""), "gear-id", name)

    def test_incomplete_ci_never_requests_credentials_or_downloads_a_package(self):
        env = {"GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": "release", "CI_WAIT_SECONDS": "0", "GITHUB_REPOSITORY": "owner/repo", "RELEASE_TAG": "v1.4.1",
               "PLUGIN_FILE": "test_any.py", "PLUGIN_ID": "test-plugin", "CLOUD_PLUGIN_ID": "cloud-id"}
        replies = [json.dumps({"tagName": "v1.4.1", "isDraft": False, "body": "notes", "assets": []}),
                   json.dumps({"sha": "abc"}), json.dumps({"workflow_runs": []})]
        with patch.dict(publisher.os.environ, env, clear=True), patch.object(publisher, "gh", side_effect=replies) as cli, \
             patch.object(publisher, "request_json") as network, patch.object(publisher, "announce"):
            with self.assertRaisesRegex(RuntimeError, 'No successful CI'):
                publisher.main()
            self.assertEqual(cli.call_count, 3)
            network.assert_not_called()

    def test_confirmed_upload_writes_a_receipt_and_a_replay_never_uploads_again(self):
        env = {"GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": "release", "GITHUB_REPOSITORY": "owner/repo", "RELEASE_TAG": "v1.4.1",
               "PLUGIN_FILE": "test_any.py", "PLUGIN_ID": "test-plugin", "CLOUD_PLUGIN_ID": "cloud-id",
               "ACTIONS_ID_TOKEN_REQUEST_URL": "https://example.invalid/?request=1",
               "ACTIONS_ID_TOKEN_REQUEST_TOKEN": "test-placeholder", "GITHUB_RUN_ID": "123"}
        content = b'# /// script\n# [tool.orcaslicer.plugin]\n# version = "1.4.1"\n# id = "test-plugin"\n# ///\n'
        digest = "sha256:" + hashlib.sha256(content).hexdigest()
        release = {"tagName": "v1.4.1", "isDraft": False, "body": "Unicode 日本語; filename=x", "assets": [
            {"name": "test_any.py", "digest": digest}]}
        receipt = {}
        release_views = 0

        def cli(*args):
            nonlocal release_views
            if args[:2] == ("release", "view"):
                release_views += 1
                if release_views == 1:
                    # The CI attachment job has not finished at release.published.
                    return json.dumps({**release, "assets": []})
                return json.dumps(release)
            if args[0] == "api":
                return json.dumps({"workflow_runs": [{"head_sha": "abc", "head_branch": "v1.4.1", "event": "push", "status": "completed", "conclusion": "success"}]}
                                  if "workflow" in args[1] else {"sha": "abc"})
            if args[:2] == ("release", "download"):
                folder = Path(args[args.index("--dir") + 1])
                name = args[args.index("--pattern") + 1]
                (folder / name).write_bytes(content if name == "test_any.py" else json.dumps(receipt).encode())
            if args[:2] == ("release", "upload"):
                receipt.update(json.loads(Path(args[3]).read_text(encoding="utf8")))
            return ""

        with patch.dict(publisher.os.environ, env, clear=True), patch.object(publisher, "gh", side_effect=cli), \
             patch.object(publisher, "request_json", return_value={"value": "test-placeholder"}) as network, \
             patch.object(publisher, "upload", return_value={"id": "cloud-id", "version": "1.4.1"}) as remote_upload, \
             patch.object(publisher, "announce"):
            publisher.main()
            self.assertEqual(network.call_count, 1)
            self.assertEqual(remote_upload.call_count, 1)
            self.assertEqual(receipt["sha256"], digest)
            release["assets"].append({"name": publisher.RECEIPT})
            network.reset_mock()
            remote_upload.reset_mock()
            publisher.main()
            network.assert_not_called()
            remote_upload.assert_not_called()

    def test_http_failure_never_exposes_a_reflected_credential(self):
        request = publisher.urllib.request.Request("https://example.invalid", headers={"Authorization": "Bearer test-placeholder"})
        error = publisher.urllib.error.HTTPError(request.full_url, 401, "rejected", {}, io.BytesIO(b'Bearer test-placeholder'))
        with patch.object(publisher.urllib.request, "urlopen", side_effect=error):
            with self.assertRaisesRegex(RuntimeError, r"HTTP 401: \[redacted\]") as caught:
                publisher.request_json(request)
            self.assertNotIn("test-placeholder", str(caught.exception))

    def test_publication_requires_http_created_not_merely_a_json_response(self):
        response = io.BytesIO(b'{"id":"cloud-id","version":"1.4.1"}')
        response.status = 200
        with patch.object(publisher.urllib.request, "urlopen", return_value=response):
            with self.assertRaisesRegex(RuntimeError, 'Expected HTTP 201'):
                publisher.request_json(publisher.urllib.request.Request("https://example.invalid"), expected_status=201)

    def test_documented_transport_keeps_credentials_out_of_arguments_and_disk(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            package = folder / "test_any.py"
            package.write_bytes(b"# public package")

            def curl(command, **options):
                self.assertNotIn("test-placeholder", " ".join(command))
                self.assertIn('Authorization: Bearer test-placeholder', options["input"])
                self.assertEqual(command[command.index("--config") + 1], "-")
                self.assertNotIn(b"test-placeholder", (folder / "multipart.bin").read_bytes())
                (folder / "response.json").write_text('{"id":"cloud-id","version":"1.4.1"}', encoding="utf8")
                return publisher.subprocess.CompletedProcess(command, 0, "201", "")

            with patch.object(publisher.subprocess, "run", side_effect=curl):
                result = publisher.upload(metadata("v1.4.1", "日本語; filename=x"), package, "test-placeholder", folder)
                self.assertEqual(result["version"], "1.4.1")

    def test_release_context_is_required_before_accessing_services(self):
        with patch.dict(publisher.os.environ, {"GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": "workflow_dispatch"}, clear=True), \
             patch.object(publisher, "gh") as cli, patch.object(publisher, "request_json") as network:
            with self.assertRaisesRegex(RuntimeError, 'release-triggered'):
                publisher.main()
            cli.assert_not_called()
            network.assert_not_called()

    def test_release_job_waits_for_running_ci_without_replacing_its_oidc_context(self):
        pending = {"head_sha": "abc", "head_branch": "v1.4.1", "event": "push", "status": "in_progress", "conclusion": None}
        success = {**pending, "status": "completed", "conclusion": "success"}
        main_success = {**success, "head_branch": "main"}
        with patch.object(publisher, "gh", side_effect=[json.dumps({"workflow_runs": [main_success, pending]}), json.dumps({"workflow_runs": [success]})]), \
             patch.object(publisher.time, "sleep") as sleep:
            publisher.wait_for_ci("owner/repo", "abc", "v1.4.1", timeout=10, interval=0)
            self.assertEqual(sleep.call_count, 1)


if __name__ == "__main__":
    unittest.main()
