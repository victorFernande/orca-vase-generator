#!/usr/bin/env python3
"""Single-file PEP 723 bundler, PEP 427 wheel builder, and local installer for Orca Vase Studio.

Compiles all modules under `src/vase_studio/` into:
1. Self-contained single-file OrcaSlicer 2.5.1+ plugin (`dist/orca_vase_generator.py` + `dist/orca_vase_generator_any.py`)
2. Pure-Python community/OrcaCloud wheel (`dist/orca_vase_generator-<ver>-py3-none-any.whl`)
and deploys ONLY `orca_vase_generator.py` + `icon.svg` into `<data_dir>/orca_plugins/orca_vase_generator/`
(unless `--no-install` is passed for CI/CD).
"""

from __future__ import annotations

import ast
import base64
import csv
import hashlib
import io
import os
import re
import shutil
import sys
import tempfile
import tokenize
import tomllib
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PKG_DIR = PROJECT_ROOT / "src" / "vase_studio"
DIST_DIR = PROJECT_ROOT / "dist"
DIST_BUNDLE_PATH = DIST_DIR / "orca_vase_generator.py"
DIST_ANY_BUNDLE_PATH = DIST_DIR / "orca_vase_generator_any.py"
ICON_SRC_PATH = SRC_PKG_DIR / "icon.svg"

MODULE_ORDER: list[str] = [
    "schema.py",
    "mesh_generator.py",
    "printability.py",
    "exporters.py",
    "presets_catalog.py",
    "studio_ui.py",
    "plugin_main.py",
]

DEFAULT_PLUGIN_VERSION = "1.1.1"
PLUGIN_VERSION = os.environ.get("ORCA_PLUGIN_VERSION", "").strip().lstrip("v") or DEFAULT_PLUGIN_VERSION

PEP723_HEADER = f"""\
# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-vase-studio"
# name = "Orca Vase Studio"
# description = "Parametric 3D Vase & Planter Studio with X-Ray Wall Calipers & 1-Click Plater | Estudio 3D de Vasos e Cachepos"
# author = "Orca Vase Studio"
# version = "{PLUGIN_VERSION}"
# ///
"""

DIST_WHEEL_PATH = DIST_DIR / f"orca_vase_generator-{PLUGIN_VERSION}-py3-none-any.whl"
PRESERVED_SIDE_FILES: frozenset[str] = frozenset(
    {
        "orca_vase_generator.py",
        "icon.svg",
        ".install_state.json",
        "install_state.json",
    }
)


def get_orca_data_dir() -> Path:
    """Resolve OrcaSlicer's `data_dir()` across Windows, macOS, and Linux."""
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "").strip()
        if appdata:
            return Path(appdata) / "OrcaSlicer"
        return Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    xdg_cfg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    if xdg_cfg:
        return Path(xdg_cfg) / "OrcaSlicer"
    return Path.home() / ".config" / "OrcaSlicer"


def get_install_dir() -> Path:
    return get_orca_data_dir() / "orca_plugins" / "orca_vase_generator"


def extract_pep723_toml(source: str) -> dict:
    """Parse and validate PEP 723 `# /// script ... # ///` block using stdlib `tomllib`."""
    in_block = False
    toml_lines: list[str] = []
    for line in source.splitlines():
        stripped = line.strip()
        if not in_block:
            if stripped == "# /// script":
                in_block = True
            continue
        if stripped == "# ///":
            break
        if line.startswith("# "):
            toml_lines.append(line[2:])
        elif line.startswith("#"):
            toml_lines.append(line[1:])
        else:
            raise ValueError(f"Invalid non-comment line inside PEP 723 header: {line!r}")
    else:
        raise ValueError("Missing closing `# ///` for PEP 723 script block.")

    return tomllib.loads("\n".join(toml_lines))


def _collect_top_level_private_defs(tree: ast.Module) -> tuple[set[str], set[str]]:
    """Return `(private_top_defs, class_attr_names)` for collision analysis."""
    privates: set[str] = set()
    class_attrs: set[str] = set()

    def _record_target(target: ast.AST) -> None:
        if isinstance(target, ast.Name):
            nm = target.id
            if nm.startswith("_") and not (nm.startswith("__") and nm.endswith("__")):
                privates.add(nm)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                _record_target(elt)

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            nm = node.name
            if nm.startswith("_") and not (nm.startswith("__") and nm.endswith("__")):
                privates.add(nm)
            if isinstance(node, ast.ClassDef):
                for sub in node.body:
                    if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        class_attrs.add(sub.name)
                    elif isinstance(sub, ast.Assign):
                        for t in sub.targets:
                            if isinstance(t, ast.Name):
                                class_attrs.add(t.id)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                _record_target(t)
        elif isinstance(node, ast.AnnAssign) and node.target is not None:
            _record_target(node.target)

    return privates, class_attrs


def _rename_colliding_privates(source: str, mod_stem: str, to_rename: set[str]) -> str:
    """Token-safely prefix colliding module-private helper names without touching strings/JS."""
    if not to_rename:
        return source

    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    rewritten: list[tokenize.TokenInfo] = []
    prev_significant_str = ""

    for tok in tokens:
        if tok.type == tokenize.NAME and tok.string in to_rename and prev_significant_str != ".":
            tok = tok._replace(string=f"_{mod_stem}{tok.string}")
        rewritten.append(tok)
        if tok.type not in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT, tokenize.COMMENT):
            prev_significant_str = tok.string

    return tokenize.untokenize(rewritten)


def _strip_internal_imports(source: str) -> tuple[str, set[str]]:
    """Strip `from __future__` and intra-package `vase_studio` imports via AST line spans."""
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    future_features: set[str] = set()

    # Collect AST import nodes (innermost/bottom-up by line number)
    replacements: list[tuple[int, int, str]] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            mod_name = node.module or ""
            is_future = node.level == 0 and mod_name == "__future__"
            is_internal = node.level >= 1 or mod_name == "vase_studio" or mod_name.startswith("vase_studio.")

            if not (is_future or is_internal):
                continue

            start_line = node.lineno
            end_line = node.end_lineno or node.lineno
            first_line = lines[start_line - 1]
            indent_match = re.match(r"^[ \t]*", first_line)
            indent = indent_match.group(0) if indent_match else ""

            if is_future:
                for alias in node.names:
                    future_features.add(alias.name)
                repl = f"{indent}pass  # [bundled] hoisted __future__ import\n"
                replacements.append((start_line, end_line, repl))
                continue

            # Intra-package import
            stmts: list[str] = []
            if node.level >= 1 and not mod_name:
                # `from . import schema, mesh_generator as mg`
                stmts.append(f"{indent}import sys as _orca_bundle_sys\n")
                for alias in node.names:
                    bound_name = alias.asname or alias.name
                    stmts.append(f"{indent}{bound_name} = _orca_bundle_sys.modules[__name__]\n")
            else:
                # `from .schema import DEFAULT_PARAMS, normalize_params as norm`
                for alias in node.names:
                    if alias.name == "*":
                        continue
                    if alias.asname and alias.asname != alias.name:
                        stmts.append(f"{indent}{alias.asname} = {alias.name}\n")
                if not stmts:
                    stmts.append(f"{indent}pass  # [bundled] resolved intra-package import\n")

            replacements.append((start_line, end_line, "".join(stmts)))

        elif isinstance(node, ast.Import):
            internal_aliases = [
                a for a in node.names if a.name == "vase_studio" or a.name.startswith("vase_studio.")
            ]
            if not internal_aliases:
                continue
            start_line = node.lineno
            end_line = node.end_lineno or node.lineno
            first_line = lines[start_line - 1]
            indent_match = re.match(r"^[ \t]*", first_line)
            indent = indent_match.group(0) if indent_match else ""

            stmts = [f"{indent}import sys as _orca_bundle_sys\n"]
            for alias in node.names:
                if alias.name == "vase_studio" or alias.name.startswith("vase_studio."):
                    bound = alias.asname or alias.name.split(".")[0]
                    stmts.append(f"{indent}{bound} = _orca_bundle_sys.modules[__name__]\n")
                else:
                    as_part = f" as {alias.asname}" if alias.asname else ""
                    stmts.append(f"{indent}import {alias.name}{as_part}\n")
            replacements.append((start_line, end_line, "".join(stmts)))

    # Deduplicate overlapping spans and apply from bottom to top
    replacements.sort(key=lambda item: (item[0], -item[1]), reverse=True)
    applied_ranges: list[tuple[int, int]] = []
    for start_line, end_line, repl_text in replacements:
        if any(not (end_line < s or start_line > e) for s, e in applied_ranges):
            continue
        lines[start_line - 1 : end_line] = [repl_text]
        applied_ranges.append((start_line, end_line))

    return "".join(lines), future_features


def build_bundle() -> Path:
    """Compile all `src/vase_studio/*.py` modules into `dist/orca_vase_generator.py`."""
    missing = [m for m in MODULE_ORDER if not (SRC_PKG_DIR / m).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing required source module(s) in {SRC_PKG_DIR}: {missing}")

    raw_sources: dict[str, str] = {}
    private_defs_by_mod: dict[str, set[str]] = {}
    class_attrs_by_mod: dict[str, set[str]] = {}
    def_counts: dict[str, int] = {}

    for mod_file in MODULE_ORDER:
        src = (SRC_PKG_DIR / mod_file).read_text(encoding="utf-8")
        raw_sources[mod_file] = src
        tree = ast.parse(src, filename=mod_file)
        privs, cls_attrs = _collect_top_level_private_defs(tree)
        private_defs_by_mod[mod_file] = privs
        class_attrs_by_mod[mod_file] = cls_attrs
        for nm in privs:
            def_counts[nm] = def_counts.get(nm, 0) + 1

    colliding_privates = {nm for nm, count in def_counts.items() if count > 1}

    all_future_features: set[str] = {"annotations"}
    sections: list[str] = []

    for mod_file in MODULE_ORDER:
        mod_stem = Path(mod_file).stem
        src = raw_sources[mod_file]
        rename_set = (private_defs_by_mod[mod_file] & colliding_privates) - class_attrs_by_mod[mod_file]
        if rename_set:
            src = _rename_colliding_privates(src, mod_stem, rename_set)

        transformed, fut = _strip_internal_imports(src)
        all_future_features.update(fut)

        banner = (
            f"\n# {'=' * 75}\n"
            f"# MODULE: vase_studio.{mod_stem}\n"
            f"# {'=' * 75}\n\n"
        )
        sections.append(banner + transformed.rstrip() + "\n")

    future_stmt = f"from __future__ import {', '.join(sorted(all_future_features))}\n"
    module_bootstrap = (
        "import sys as _orca_init_sys\n"
        "import types as _orca_init_types\n"
        "if __name__ not in _orca_init_sys.modules:\n"
        "    _orca_init_sys.modules[__name__] = _orca_init_types.ModuleType(__name__)\n"
    )
    bundled_code = (
        PEP723_HEADER
        + "\n"
        + future_stmt
        + "\n"
        + module_bootstrap
        + "".join(sections)
    )

    # Validate PEP 723 TOML & Python compilation before writing
    meta = extract_pep723_toml(bundled_code)
    plugin_meta = meta.get("tool", {}).get("orcaslicer", {}).get("plugin", {})
    if plugin_meta.get("id") != "orca-vase-studio":
        raise RuntimeError("PEP 723 header is missing [tool.orcaslicer.plugin].id == 'orca-vase-studio'")
    if not plugin_meta.get("name"):
        raise RuntimeError("PEP 723 header is missing [tool.orcaslicer.plugin].name")
    if not meta.get("dependencies"):
        raise RuntimeError("PEP 723 header is missing dependencies")

    if ICON_SRC_PATH.is_file():
        icon_disk = ICON_SRC_PATH.read_text(encoding="utf-8").strip()
        if icon_disk not in raw_sources["plugin_main.py"]:
            raise RuntimeError("Embedded ICON_SVG_CONTENT in plugin_main.py is out of sync with src/vase_studio/icon.svg")

    compile(bundled_code, str(DIST_BUNDLE_PATH), "exec")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    with open(DIST_BUNDLE_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(bundled_code)
    with open(DIST_ANY_BUNDLE_PATH, "w", encoding="utf-8", newline="\n") as fh_any:
        fh_any.write(bundled_code)

    return DIST_BUNDLE_PATH


def _record_digest_and_size(data: bytes) -> tuple[str, str]:
    digest = hashlib.sha256(data).digest()
    b64 = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return f"sha256={b64}", str(len(data))


def build_wheel() -> Path:
    """Build pure-Python PEP 427 wheel (`dist/orca_vase_generator-<ver>-py3-none-any.whl`)
    satisfying `OrcaSlicer.dll` `read_wheel_plugin_metadata` (`METADATA`, `WHEEL`, `RECORD`,
    `top_level.txt`, `Import-Name: vase_studio`, and bundled `vase_studio/icon.svg`).
    """
    pyproj = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    proj_tbl = pyproj.get("project", {})
    plugin_tbl = pyproj.get("tool", {}).get("orcaslicer", {}).get("plugin", {})

    display_name = str(plugin_tbl.get("name") or "Orca Vase Studio").strip()
    version = PLUGIN_VERSION
    whl_path = DIST_DIR / f"orca_vase_generator-{version}-py3-none-any.whl"
    summary = str(plugin_tbl.get("description") or proj_tbl.get("description") or "").strip()
    author = str(plugin_tbl.get("author") or "Orca Vase Studio").strip()
    req_py = str(proj_tbl.get("requires-python") or ">=3.12").strip()
    deps = list(proj_tbl.get("dependencies") or ["numpy>=1.26"])

    readme_path = PROJECT_ROOT / "README.md"
    readme_body = readme_path.read_text(encoding="utf-8").strip() if readme_path.is_file() else summary

    dist_info_dir = f"orca_vase_generator-{version}.dist-info"
    pkg_files = ["__init__.py", *MODULE_ORDER, "icon.svg"]
    missing = [f for f in pkg_files if not (SRC_PKG_DIR / f).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing package file(s) in {SRC_PKG_DIR} for wheel build: {missing}")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for stale_whl in DIST_DIR.glob("*.whl"):
        if stale_whl != whl_path:
            stale_whl.unlink()

    entries: list[tuple[str, bytes]] = []
    for rel_name in pkg_files:
        raw_bytes = (SRC_PKG_DIR / rel_name).read_bytes().replace(b"\r\n", b"\n")
        entries.append((f"vase_studio/{rel_name}", raw_bytes))

    meta_lines = [
        "Metadata-Version: 2.1",
        f"Name: {display_name}",
        f"Version: {version}",
        f"Summary: {summary}",
        f"Author: {author}",
        "License: MIT",
        f"Requires-Python: {req_py}",
        *[f"Requires-Dist: {dep}" for dep in deps],
        "Import-Name: vase_studio",
        "Description-Content-Type: text/markdown",
        "",
        readme_body,
        "",
    ]
    metadata_bytes = "\n".join(meta_lines).encode("utf-8")
    wheel_bytes = (
        "Wheel-Version: 1.0\n"
        f"Generator: orca-vase-studio-builder ({version})\n"
        "Root-Is-Purelib: true\n"
        "Tag: py3-none-any\n"
    ).encode("utf-8")
    top_level_bytes = b"vase_studio\n"

    if (PROJECT_ROOT / "LICENSE").is_file():
        entries.append((f"{dist_info_dir}/LICENSE", (PROJECT_ROOT / "LICENSE").read_bytes().replace(b"\r\n", b"\n")))
    entries.append((f"{dist_info_dir}/METADATA", metadata_bytes))
    entries.append((f"{dist_info_dir}/WHEEL", wheel_bytes))
    entries.append((f"{dist_info_dir}/top_level.txt", top_level_bytes))

    rec_buf = io.StringIO()
    writer = csv.writer(rec_buf, lineterminator="\n")
    for arc_path, payload in entries:
        digest_str, size_str = _record_digest_and_size(payload)
        writer.writerow([arc_path, digest_str, size_str])
    writer.writerow([f"{dist_info_dir}/RECORD", "", ""])
    entries.append((f"{dist_info_dir}/RECORD", rec_buf.getvalue().encode("utf-8")))

    fixed_dt = (2026, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(whl_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for arc_path, payload in entries:
            zi = zipfile.ZipInfo(arc_path, date_time=fixed_dt)
            zi.external_attr = 0o644 << 16
            zi.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(zi, payload)

    return whl_path


def install_plugin(bundle_path: Path) -> Path:
    """Install `orca_vase_generator.py` and `icon.svg` into OrcaSlicer's `orca_plugins`,
    preserving OrcaSlicer's `.install_state.json` / `install_state.json` untouched.
    """
    install_dir = get_install_dir()
    install_dir.mkdir(parents=True, exist_ok=True)

    # Remove any stale .py, .pyc, .pyo, .whl files or __pycache__ directories while
    # strictly preserving `.install_state.json` / `install_state.json` and `icon.svg`.
    for item in list(install_dir.iterdir()):
        if item.name in PRESERVED_SIDE_FILES:
            continue
        if item.is_dir() and item.name == "__pycache__":
            shutil.rmtree(item, ignore_errors=True)
        elif item.is_file() and item.suffix.lower() in {".py", ".pyc", ".pyo", ".whl"}:
            item.unlink()

    for cache_dir in list(install_dir.rglob("__pycache__")):
        shutil.rmtree(cache_dir, ignore_errors=True)

    dest_py = install_dir / "orca_vase_generator.py"
    shutil.copyfile(bundle_path, dest_py)

    if ICON_SRC_PATH.is_file():
        shutil.copyfile(ICON_SRC_PATH, install_dir / "icon.svg")

    # Enforce strict OrcaSlicer.dll v2.5.1 directory invariants
    py_files = list(install_dir.glob("*.py"))
    whl_files = list(install_dir.glob("*.whl"))
    pyc_files = [*install_dir.rglob("*.pyc"), *install_dir.rglob("*.pyo")]
    pycache_dirs = list(install_dir.rglob("__pycache__"))

    if len(py_files) != 1 or py_files[0].name != "orca_vase_generator.py":
        raise RuntimeError(f"Expected strictly 1 .py file in {install_dir}, found: {py_files}")
    if whl_files:
        raise RuntimeError(f"Found forbidden .whl file(s) in {install_dir}: {whl_files}")
    if pyc_files:
        raise RuntimeError(f"Found forbidden bytecode file(s) in {install_dir}: {pyc_files}")
    if pycache_dirs:
        raise RuntimeError(f"Found forbidden __pycache__ in {install_dir}: {pycache_dirs}")

    return install_dir


def verify_bundle_smoke(bundle_path: Path) -> None:
    """Load the generated bundle from `dist/` with a mock `orca` host to verify registration & UI."""
    import importlib.util

    meta = extract_pep723_toml(bundle_path.read_text(encoding="utf-8"))
    plugin_meta = meta.get("tool", {}).get("orcaslicer", {}).get("plugin", {})
    if plugin_meta.get("version") != PLUGIN_VERSION:
        raise RuntimeError(
            f"Expected PEP 723 plugin version {PLUGIN_VERSION!r}, got {plugin_meta.get('version')!r}"
        )

    # Ensure OrcaSlicer's shared cp3xx packages folder is on sys.path (where numpy lives!)
    cp_pkgs = get_orca_data_dir() / "python" / "packages" / f"cp{sys.version_info.major}{sys.version_info.minor}"
    if cp_pkgs.is_dir() and str(cp_pkgs) not in sys.path:
        sys.path.insert(0, str(cp_pkgs))

    sys.dont_write_bytecode = True

    with tempfile.TemporaryDirectory(prefix="orca_vase_smoke_") as tmp_dir:
        standalone_dir = Path(tmp_dir) / "standalone_only_py"
        standalone_dir.mkdir(parents=True, exist_ok=True)
        standalone_py = standalone_dir / "orca_vase_generator.py"
        shutil.copyfile(bundle_path, standalone_py)

        storage_only_dir = Path(tmp_dir) / "plugin_storage"
        storage_only_dir.mkdir(parents=True, exist_ok=True)

        spec = importlib.util.spec_from_file_location("orca_vase_generator_smoke", str(standalone_py))
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Could not create module spec for {standalone_py}")

        mod = importlib.util.module_from_spec(spec)
        sys.modules["orca_vase_generator_smoke"] = mod
        try:
            spec.loader.exec_module(mod)

            plugin_instance = mod.OrcaVaseStudioPlugin()
            plugin_instance.register_capabilities()

            perms = getattr(mod.orca, "_requested_permissions", {})
            assert "process" not in perms, f"Unexpected process permission requested: {perms}"
            assert bool(perms.get("threading")), f"Missing threading=True permission: {perms}"

            sample_stl = Path(tmp_dir) / "vaso_smoke.stl"
            sample_stl.write_bytes(b"smoke")
            payload = mod._format_other_instance_payload([sample_stl])
            assert payload.startswith('"orca-slicer.exe";'), f"Bad WM_COPYDATA prefix: {payload!r}"
            assert not payload.endswith(";"), f"Forbidden trailing semicolon in payload: {payload!r}"

            page_cap = mod.VaseStudioPageCapability()
            dock_cap = mod.VaseStudioDockCapability()
            assert page_cap.get_name() == "Gerador de Vasos"
            assert dock_cap.get_name() == "Orca Vase Studio - Painel Lateral"

            # Direct temporary storage during smoke check (and verify standalone icon auto-materialization!)
            mod.orca.host.plugin.storage = lambda: str(storage_only_dir)
            orig_inst_dir_fn = mod._default_installed_plugin_dir
            mod._default_installed_plugin_dir = lambda: standalone_dir
            try:
                auto_icon = page_cap.get_icon()
                assert auto_icon and Path(auto_icon).is_file(), f"Standalone get_icon() failed: {auto_icon!r}"
                assert Path(auto_icon).parent == storage_only_dir, (
                    f"Expected icon auto-materialized into storage {storage_only_dir}, got {auto_icon}"
                )
            finally:
                mod._default_installed_plugin_dir = orig_inst_dir_fn

            html_page = page_cap.get_ui()
            html_dock = dock_cap.get_ui()
            assert "<html" in html_page.lower() and len(html_page) > 1000
            assert "<html" in html_dock.lower() and len(html_dock) > 1000

            outbox: list[dict] = []
            page_cap.post_message = lambda payload_msg: outbox.append(payload_msg)  # type: ignore[method-assign]
            page_cap.on_message('{"type": "ready", "mode": "page"}')
            assert len(outbox) >= 2
            assert outbox[0]["type"] == "init_state"
            assert outbox[1]["type"] == "analysis_result"
        finally:
            sys.modules.pop("orca_vase_generator_smoke", None)


def verify_wheel_smoke(wheel_path: Path) -> None:
    """Validate `.whl` archive structure against `OrcaSlicer.dll` `read_wheel_plugin_metadata`
    and verify importing `vase_studio` from the wheel triggers `@orca.plugin` capture.
    """
    with zipfile.ZipFile(wheel_path, "r") as zf:
        names = zf.namelist()
        dist_infos = sorted({n.split("/", 1)[0] for n in names if ".dist-info/" in n})
        if len(dist_infos) != 1:
            raise RuntimeError(f"Expected strictly 1 .dist-info directory in {wheel_path}, got {dist_infos}")
        di = dist_infos[0]
        for req_member in (f"{di}/METADATA", f"{di}/WHEEL", f"{di}/RECORD", f"{di}/top_level.txt", "vase_studio/icon.svg"):
            if req_member not in names:
                raise RuntimeError(f"Wheel missing required member {req_member!r}")
        meta_txt = zf.read(f"{di}/METADATA").decode("utf-8")
        wheel_txt = zf.read(f"{di}/WHEEL").decode("utf-8")
        rec_txt = zf.read(f"{di}/RECORD").decode("utf-8").strip()
        assert "Name: Orca Vase Studio" in meta_txt
        assert f"Version: {PLUGIN_VERSION}" in meta_txt
        assert "Requires-Dist: numpy" in meta_txt
        assert "Import-Name: vase_studio" in meta_txt
        assert "Wheel-Version:" in wheel_txt and "-none-any" in wheel_txt
        assert bool(rec_txt), "Wheel RECORD must be non-empty"

    with tempfile.TemporaryDirectory(prefix="orca_vase_whl_smoke_") as tmp_dir:
        extract_root = Path(tmp_dir) / "extracted_whl"
        with zipfile.ZipFile(wheel_path, "r") as zf:
            zf.extractall(extract_root)

        saved_mods = {k: v for k, v in sys.modules.items() if k == "vase_studio" or k.startswith("vase_studio.")}
        for k in list(saved_mods):
            sys.modules.pop(k, None)
        sys.path.insert(0, str(extract_root))
        try:
            import importlib

            pkg = importlib.import_module("vase_studio")
            assert hasattr(pkg, "OrcaVaseStudioPlugin"), "vase_studio wheel package did not expose OrcaVaseStudioPlugin"
            inst = pkg.OrcaVaseStudioPlugin()
            inst.register_capabilities()
            icon_file = pkg.VaseStudioPageCapability().get_icon()
            assert icon_file and Path(icon_file).is_file(), f"Wheel get_icon() failed: {icon_file!r}"
        finally:
            if str(extract_root) in sys.path:
                sys.path.remove(str(extract_root))
            for k in [m for m in sys.modules if m == "vase_studio" or m.startswith("vase_studio.")]:
                sys.modules.pop(k, None)
            sys.modules.update(saved_mods)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    skip_install = "--no-install" in args

    print("[1/4] Bundling src/vase_studio/*.py -> dist/orca_vase_generator.py (+ _any.py) ...")
    bundle_path = build_bundle()
    size_kb = bundle_path.stat().st_size / 1024.0
    print(f"      Built {bundle_path} ({size_kb:.1f} KB)")

    print("[2/4] Building pure-Python community wheel -> dist/*.whl ...")
    wheel_path = build_wheel()
    whl_kb = wheel_path.stat().st_size / 1024.0
    print(f"      Built {wheel_path} ({whl_kb:.1f} KB)")

    print("[3/4] Running smoke verification on dist/orca_vase_generator.py and dist/*.whl ...")
    verify_bundle_smoke(bundle_path)
    verify_wheel_smoke(wheel_path)
    print("      Smoke check passed (PEP 723 .py, PEP 427 .whl, @orca.plugin, Page + Dock UI, bridge).")

    if skip_install:
        print("[4/4] Skipping local OrcaSlicer install (--no-install).")
    else:
        print("[4/4] Installing into OrcaSlicer local plugins directory ...")
        install_dir = install_plugin(bundle_path)
        installed_entries = sorted(p.name for p in install_dir.iterdir())
        print(f"      Installed to: {install_dir}")
        print(f"      Directory contents: {installed_entries}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
