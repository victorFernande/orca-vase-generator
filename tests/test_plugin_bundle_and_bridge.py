"""Comprehensive verification of the installed PEP-723 single-file plugin, mock Orca v2.5.1 host,
WebGL2 HTML/JS syntax, JS-vs-Python mathematical surface parity, and full bridge message protocol.
"""

from __future__ import annotations

import sys

# CRITICAL: Never emit __pycache__ / .pyc next to the installed OrcaSlicer single-file plugin!
sys.dont_write_bytecode = True

import asyncio
import copy
import ctypes
import importlib.util
import json
import math
import re
import shutil
import struct
import subprocess
import tempfile
import threading
import time
import tomllib
import types
import unittest
import xml.etree.ElementTree as ET
import zipfile
import base64
import csv
import hashlib
import os
from pathlib import Path
from unittest import mock


def _resolve_orca_data_dir() -> Path:
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "").strip()
        return Path(appdata) / "OrcaSlicer" if appdata else Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    return (Path(xdg) if xdg else (Path.home() / ".config")) / "OrcaSlicer"


REPO_ROOT = Path(__file__).resolve().parent.parent
ORCA_DATA_DIR = _resolve_orca_data_dir()
ORCA_SITE_PACKAGES = ORCA_DATA_DIR / "python" / "packages" / f"cp{sys.version_info.major}{sys.version_info.minor}"
PROJECT_SRC = REPO_ROOT / "src"
for _p in (ORCA_SITE_PACKAGES, PROJECT_SRC):
    _ps = str(_p)
    if _ps not in sys.path:
        sys.path.insert(0, _ps)

import numpy as np

from vase_studio.mesh_generator import evaluate_radius_grid
from vase_studio.schema import DEFAULT_PARAMS, normalize_params

PYPROJECT_TOML = REPO_ROOT / "pyproject.toml"
BUILD_SCRIPT = REPO_ROOT / "scripts" / "build_and_install.py"
SRC_ICON_SVG = REPO_ROOT / "src" / "vase_studio" / "icon.svg"
DIST_BUNDLE = REPO_ROOT / "dist" / "orca_vase_generator.py"
DIST_ANY_BUNDLE = REPO_ROOT / "dist" / "orca_vase_generator_any.py"
DIST_WHEEL = REPO_ROOT / "dist" / "orca_vase_generator-1.3.3-py3-none-any.whl"
# Repository tests never inspect or replace the user's installed plugin.
# An explicit isolated install directory can be provided for installer verification.
INSTALLED_DIR = Path(os.environ.get("ORCA_VASE_TEST_INSTALL_DIR") or (REPO_ROOT / "test-output" / "isolated-install"))
INSTALLED_PLUGIN_PY = INSTALLED_DIR / "orca_vase_generator.py"
ALLOWED_INSTALLED_FILENAMES = {
    "orca_vase_generator.py",
    "icon.svg",
    ".install_state.json",
    "install_state.json",
}


def _unescape_strings_cstyle_orca(raw: str) -> tuple[bool, list[str]]:
    """Faithful Python implementation of `OrcaSlicer.dll`'s `unescape_strings_cstyle` (`0x41faf0`)."""
    if not isinstance(raw, str):
        return (False, [])
    if raw == "":
        return (True, [])
    n = len(raw)
    i = 0
    out: list[str] = []
    while i < n:
        if raw[i] != '"':
            return (False, [])
        i += 1
        chars: list[str] = []
        closed = False
        while i < n:
            ch = raw[i]
            i += 1
            if ch == '"':
                closed = True
                break
            if ch == "\\":
                if i >= n:
                    return (False, [])
                esc = raw[i]
                i += 1
                if esc == "\\":
                    chars.append("\\")
                elif esc == '"':
                    chars.append('"')
                elif esc == "r":
                    chars.append("\r")
                elif esc == "n":
                    chars.append("\n")
                else:
                    # Single unescaped backslashes drop '\' in C++ and corrupt Windows paths!
                    chars.append(esc)
            else:
                chars.append(ch)
        if not closed:
            return (False, [])
        out.append("".join(chars))
        if i == n:
            break
        if raw[i] != ";" or (i + 1) >= n:
            return (False, [])
        i += 1
    return (True, out)


def _inspect_binary_stl_open_mouth(stl_path: Path, height_mm: float) -> dict[str, int]:
    """Parse binary STL on disk and count top-center mouth-closing triangles & inward cavity triangles."""
    raw = stl_path.read_bytes()
    (tri_count,) = struct.unpack("<I", raw[80:84])
    if len(raw) != 84 + 50 * tri_count:
        raise ValueError(f"Invalid binary STL byte length {len(raw)} for {tri_count} triangles")
    stl_dtype = np.dtype(
        [
            ("normal", "<f4", (3,)),
            ("v0", "<f4", (3,)),
            ("v1", "<f4", (3,)),
            ("v2", "<f4", (3,)),
            ("attr", "<u2"),
        ]
    )
    rec = np.frombuffer(raw, dtype=stl_dtype, offset=84)
    tri_verts = np.stack([rec["v0"], rec["v1"], rec["v2"]], axis=1).astype(np.float64)
    normals = rec["normal"].astype(np.float64)

    vert_r = np.hypot(tri_verts[:, :, 0], tri_verts[:, :, 1])
    vert_z = tri_verts[:, :, 2]
    top_cap_tris = int(
        np.sum(np.any((vert_r < 1.0) & (np.abs(vert_z - float(height_mm)) < 0.5), axis=1))
    )

    centroids = tri_verts.mean(axis=1)
    r_c = np.hypot(centroids[:, 0], centroids[:, 1])
    upper_mask = (centroids[:, 2] > 0.40 * float(height_mm)) & (r_c > 1.0)
    radial_dot = np.zeros(len(rec), dtype=np.float64)
    radial_dot[upper_mask] = (
        normals[upper_mask, 0] * centroids[upper_mask, 0]
        + normals[upper_mask, 1] * centroids[upper_mask, 1]
    ) / r_c[upper_mask]
    inward_cavity_tris = int(np.sum(upper_mask & (radial_dot < -0.15)))
    return {
        "tri_count": int(tri_count),
        "top_center_cap_tris": top_cap_tris,
        "inward_cavity_tris": inward_cavity_tris,
    }


def _inspect_3mf_vase_open_mouth(mf_path: Path, height_mm: float) -> dict[str, int]:
    """Parse tallest mesh object inside a .3mf archive and verify open-mouth hollow topology."""
    best_stats: dict[str, int] | None = None
    best_z_span = -1.0
    with zipfile.ZipFile(mf_path, "r") as zf:
        for member in zf.namelist():
            if not member.endswith(".model"):
                continue
            root = ET.fromstring(zf.read(member))
            for elem in root.iter():
                tag = elem.tag.split("}", 1)[1] if "}" in elem.tag else elem.tag
                if tag != "mesh":
                    continue
                v_list = []
                t_list = []
                for child in elem:
                    ctag = child.tag.split("}", 1)[1] if "}" in child.tag else child.tag
                    if ctag == "vertices":
                        for v in child:
                            v_list.append(
                                [float(v.attrib["x"]), float(v.attrib["y"]), float(v.attrib["z"])]
                            )
                    elif ctag == "triangles":
                        for t in child:
                            t_list.append(
                                [int(t.attrib["v1"]), int(t.attrib["v2"]), int(t.attrib["v3"])]
                            )
                if not v_list or not t_list:
                    continue
                verts = np.asarray(v_list, dtype=np.float64)
                tris = np.asarray(t_list, dtype=np.int64)
                z_span = float(verts[:, 2].max() - verts[:, 2].min())
                if z_span > best_z_span:
                    best_z_span = z_span
                    tri_verts = verts[tris]
                    v0, v1, v2 = tri_verts[:, 0], tri_verts[:, 1], tri_verts[:, 2]
                    cross = np.cross(v1 - v0, v2 - v0)
                    areas2 = np.maximum(np.linalg.norm(cross, axis=1, keepdims=True), 1e-12)
                    normals = cross / areas2
                    # Center XY in case vertices are offset
                    cx0 = 0.5 * float(verts[:, 0].min() + verts[:, 0].max())
                    cy0 = 0.5 * float(verts[:, 1].min() + verts[:, 1].max())
                    rel_tri = tri_verts.copy()
                    rel_tri[:, :, 0] -= cx0
                    rel_tri[:, :, 1] -= cy0
                    vert_r = np.hypot(rel_tri[:, :, 0], rel_tri[:, :, 1])
                    vert_z = rel_tri[:, :, 2] - float(verts[:, 2].min())
                    top_cap_tris = int(
                        np.sum(
                            np.any(
                                (vert_r < 1.0) & (np.abs(vert_z - float(height_mm)) < 0.5),
                                axis=1,
                            )
                        )
                    )
                    centroids = rel_tri.mean(axis=1)
                    centroids[:, 2] -= float(verts[:, 2].min())
                    r_c = np.hypot(centroids[:, 0], centroids[:, 1])
                    upper_mask = (centroids[:, 2] > 0.40 * float(height_mm)) & (r_c > 1.0)
                    radial_dot = np.zeros(len(tris), dtype=np.float64)
                    radial_dot[upper_mask] = (
                        normals[upper_mask, 0] * centroids[upper_mask, 0]
                        + normals[upper_mask, 1] * centroids[upper_mask, 1]
                    ) / r_c[upper_mask]
                    inward_cavity_tris = int(np.sum(upper_mask & (radial_dot < -0.15)))
                    best_stats = {
                        "tri_count": int(len(tris)),
                        "top_center_cap_tris": top_cap_tris,
                        "inward_cavity_tris": inward_cavity_tris,
                    }
    if best_stats is None:
        raise ValueError(f"No <mesh> found in 3MF archive {mf_path}")
    return best_stats


class MockOrcaHostHarness:
    """Faithful mock of OrcaSlicer 2.5.1 C++ pybind11 `orca` module hierarchy."""

    def __init__(self, storage_dir: Path) -> None:
        self.storage_dir = storage_dir
        self.main_thread_id = threading.get_ident()
        self.plugin_classes: list[type] = []
        self.registered_capabilities: list[type] = []
        self.requested_permissions: list[dict] = []
        self.posted_page_messages: list[dict] = []
        self.page_msg_event = threading.Event()
        self.dock_panels: list[object] = []
        self.windows: list[object] = []
        self.notifications: list[tuple] = []
        self.process_transactions: list[dict] = []
        self.tx_event = threading.Event()
        self._saved_configs: dict[str, str] = {}

        self.preset_values: dict[str, object] = {
            "printer_settings_id": "Anycubic Kobra X 0.4 nozzle",
            "filament_settings_id": ["Generic PLA @System"],
            "print_settings_id": "0.20mm Standard @Anycubic Kobra X",
            "printable_area": ["0x0", "220x0", "220x220", "0x220"],
            "printable_height": "250",
            "nozzle_diameter": ["0.4"],
            "layer_height": "0.2",
            "outer_wall_line_width": "0.42",
            "spiral_mode": "0",
            "wall_loops": "2",
            "bottom_shell_layers": "4",
            "top_shell_layers": "4",
            "sparse_infill_density": "15%",
        }

    def build_modules(self) -> dict[str, types.ModuleType]:
        harness = self

        orca_mod = types.ModuleType("orca")
        pages_mod = types.ModuleType("orca.pages")
        script_mod = types.ModuleType("orca.script")
        host_mod = types.ModuleType("orca.host")
        host_ui_mod = types.ModuleType("orca.host.ui")
        host_preset_mod = types.ModuleType("orca.host.preset")
        plugin_mod = types.ModuleType("orca.plugin")

        class PluginType:
            PrinterConnection = "PrinterConnection"
            Pages = "Pages"
            Analysis = "Analysis"
            Importer = "Importer"
            Exporter = "Exporter"
            Visualization = "Visualization"
            Script = "Script"
            SlicingPipeline = "SlicingPipeline"
            ResourceTexture = "ResourceTexture"
            Unknown = "Unknown"

        class PluginResult:
            Success = "Success"
            Skipped = "Skipped"
            RecoverableError = "RecoverableError"
            FatalError = "FatalError"

        class LifecycleEvent:
            NewProject = "NewProject"
            ProjectOpened = "ProjectOpened"
            ProjectBeforeSave = "ProjectBeforeSave"
            ProjectAfterSave = "ProjectAfterSave"
            ProjectClosed = "ProjectClosed"
            ProjectDirtyChanged = "ProjectDirtyChanged"
            SliceStarted = "SliceStarted"
            SliceGeometryFinished = "SliceGeometryFinished"
            GCodeExportStarted = "GCodeExportStarted"
            GCodeExportFinished = "GCodeExportFinished"
            SlicingJobComplete = "SlicingJobComplete"
            ObjectAdded = "ObjectAdded"
            ObjectDeleted = "ObjectDeleted"
            ObjectTransformed = "ObjectTransformed"
            ObjectChanged = "ObjectChanged"
            ObjectRenamed = "ObjectRenamed"
            PlateCreated = "PlateCreated"
            PlateDeleted = "PlateDeleted"
            PlateSelected = "PlateSelected"
            PlateRenamed = "PlateRenamed"
            PresetSelected = "PresetSelected"
            PresetSaved = "PresetSaved"

        class LifecycleEvtCode:
            Ok = 0
            Warn = 1
            Error = 2

        class ExecutionResult:
            def __init__(
                self,
                status: str = PluginResult.Success,
                message: str = "",
                data: str = "",
            ) -> None:
                self.status = status
                self.message = message
                self.data = data

            @staticmethod
            def success(message: str = "", data: str = "") -> ExecutionResult:
                return ExecutionResult(PluginResult.Success, message, data)

            @staticmethod
            def skipped(message: str = "") -> ExecutionResult:
                return ExecutionResult(PluginResult.Skipped, message, "")

            @staticmethod
            def failure(
                status: str = PluginResult.RecoverableError,
                message: str = "",
                data: str = "",
            ) -> ExecutionResult:
                return ExecutionResult(status, message, data)

        class OrcaBase:
            def __init__(self) -> None:
                pass

            def register_capabilities(self) -> None:
                pass

        def plugin_decorator(cls: type) -> type:
            harness.plugin_classes.append(cls)
            return cls

        def register_capability(cap_cls: type) -> None:
            harness.registered_capabilities.append(cap_cls)

        def request_permissions(**kwargs: object) -> None:
            harness.requested_permissions.append(dict(kwargs))

        class PythonPluginBase:
            def get_name(self) -> str:
                raise NotImplementedError

            def get_type(self) -> str:
                return PluginType.Unknown

            def on_load(self) -> None:
                pass

            def on_unload(self) -> None:
                pass

            def on_cancelled(self) -> None:
                pass

            def on_lifecycle_event(self, event: object, ctx: object = None) -> None:
                pass

            def has_config_ui(self) -> bool:
                return False

            def get_config_ui(self) -> str:
                return ""

            def get_default_config(self) -> dict:
                return {}

            def get_config(self) -> str:
                return harness._saved_configs.get(self.__class__.__name__, "{}")

            def get_config_version(self) -> str:
                return "1.0"

            def save_config(self, config_json: str) -> bool:
                harness._saved_configs[self.__class__.__name__] = str(config_json)
                return True

        class PagesPluginCapabilityBase(PythonPluginBase):
            def get_type(self) -> str:
                return PluginType.Pages

            def get_ui(self) -> str:
                raise NotImplementedError

            def get_icon(self) -> str:
                return ""

            def on_message(self, data: object) -> None:
                pass

            def post_message(self, data: object) -> None:
                # OrcaSlicer serializes payload to JSON for window.orca.onMessage
                serialized = json.loads(json.dumps(data))
                harness.posted_page_messages.append(serialized)
                harness.page_msg_event.set()

        class ScriptPluginCapabilityBase(PythonPluginBase):
            def get_type(self) -> str:
                return PluginType.Script

            def execute(self) -> object:
                raise NotImplementedError

        # Read-only Plater & Model matching OrcaSlicer.dll v2.5.1 (strictly NO load_file / add_object!)
        class ReadOnlyModel:
            id = 1
            object_count = 0
            max_z = 0.0
            material_count = 1
            current_plate_index = 0
            designer = ""
            design_id = ""

            def objects(self) -> list:
                return []

            def object(self, idx: int) -> None:
                return None

        class ReadOnlyPlater:
            model = ReadOnlyModel()
            is_project_dirty = False
            is_presets_dirty = False
            inside_snapshot_capture = False
            project_path = ""

            def export_3mf_copy(self, path: str) -> None:
                Path(path).write_bytes(b"")

        class MockPresetBundle:
            def current_print_preset(self) -> str:
                return str(harness.preset_values.get("print_settings_id", "0.20mm Standard"))

            def current_printer_preset(self) -> str:
                return str(harness.preset_values.get("printer_settings_id", "Default Printer"))

            def current_filament_presets(self) -> list[str]:
                fils = harness.preset_values.get("filament_settings_id", ["Generic PLA @System"])
                return list(fils) if isinstance(fils, (list, tuple)) else [str(fils)]

            def full_config_keys(self) -> list[str]:
                return list(harness.preset_values.keys())

            def full_config_value(self, key: str) -> object:
                val = harness.preset_values.get(key, "")
                return val[0] if isinstance(val, list) and len(val) == 1 else val

            def config_value(self, key: str) -> object:
                return self.full_config_value(key)

        class MockPresetUpdateResult:
            def __init__(self, ok: bool = True, message: str = "") -> None:
                self.ok = ok
                self.success = ok
                self.message = message

            def __bool__(self) -> bool:
                return self.ok

        class MockPresetTransaction:
            def __init__(self, preset_name: str, thread_id: int) -> None:
                self.preset_name = preset_name
                self.thread_id = thread_id
                self.updates: dict[str, str] = {}
                self.committed = False

            def set(self, key: str, value: str) -> MockPresetTransaction:
                self.updates[str(key)] = str(value)
                return self

            def commit(self) -> MockPresetUpdateResult:
                self.committed = True
                for k, v in self.updates.items():
                    harness.preset_values[k] = v
                harness.process_transactions.append(
                    {
                        "preset_name": self.preset_name,
                        "thread_id": self.thread_id,
                        "on_ui_thread": (self.thread_id == harness.main_thread_id),
                        "updates": dict(self.updates),
                    }
                )
                harness.tx_event.set()
                return MockPresetUpdateResult(True)

            def __enter__(self) -> MockPresetTransaction:
                return self

            def __exit__(self, exc_type: object, exc: object, tb: object) -> bool:
                if exc_type is None and not self.committed:
                    self.commit()
                return False

        class MockPresetEditor:
            def update(self, key: str, value: str) -> MockPresetUpdateResult:
                tid = threading.get_ident()
                harness.preset_values[str(key)] = str(value)
                harness.process_transactions.append(
                    {
                        "preset_name": "",
                        "thread_id": tid,
                        "on_ui_thread": (tid == harness.main_thread_id),
                        "updates": {str(key): str(value)},
                    }
                )
                harness.tx_event.set()
                return MockPresetUpdateResult(True)

            def begin_update(self, preset_name: str = "") -> MockPresetTransaction:
                return MockPresetTransaction(preset_name, threading.get_ident())

        class MockDockPanel:
            def __init__(
                self,
                html: str,
                title: str = "OrcaSlicer",
                width: int = 400,
                height: int = 720,
                on_message: object = None,
                on_close: object = None,
                dock: str = "right",
            ) -> None:
                self.html = html
                self.title = title
                self.width = width
                self.height = height
                self.on_message = on_message
                self.on_close = on_close
                self.dock = dock
                self._open = True
                self.posted: list[object] = []

            def post(self, data: object) -> None:
                self.posted.append(json.loads(json.dumps(data)))

            def post_message(self, data: object) -> None:
                self.post(data)

            def show(self) -> None:
                self._open = True

            def hide(self) -> None:
                self._open = False

            def close(self) -> None:
                self._open = False
                if callable(self.on_close):
                    self.on_close()

            def is_open(self) -> bool:
                return self._open

        def create_dock_panel(
            html: str,
            title: str = "OrcaSlicer",
            width: int = 400,
            height: int = 720,
            on_message: object = None,
            on_close: object = None,
            dock: str = "right",
        ) -> MockDockPanel:
            panel = MockDockPanel(html, title, width, height, on_message, on_close, dock)
            harness.dock_panels.append(panel)
            return panel

        def create_window(
            html: str,
            title: str = "OrcaSlicer",
            width: int = 900,
            height: int = 720,
            on_message: object = None,
            on_close: object = None,
            style: int = 0,
            on_submit: object = None,
        ) -> MockDockPanel:
            win = MockDockPanel(html, title, width, height, on_message, on_close, "window")
            harness.windows.append(win)
            return win

        class NotificationLevel:
            ProgressBarNotificationLevel = "ProgressBarNotificationLevel"
            HintNotificationLevel = "HintNotificationLevel"
            RegularNotificationLevel = "RegularNotificationLevel"
            PrintInfoNotificationLevel = "PrintInfoNotificationLevel"
            PrintInfoShortNotificationLevel = "PrintInfoShortNotificationLevel"
            ImportantNotificationLevel = "ImportantNotificationLevel"
            WarningNotificationLevel = "WarningNotificationLevel"
            SeriousWarningNotificationLevel = "SeriousWarningNotificationLevel"
            ErrorNotificationLevel = "ErrorNotificationLevel"

        def push_notification(
            notification_level: object,
            text: str,
            hyper_text: str = "",
            on_click: object = None,
        ) -> None:
            harness.notifications.append(
                (notification_level, str(text), str(hyper_text), on_click)
            )

        def ui_message(
            text: str,
            title: str = "OrcaSlicer",
            buttons: str = "ok",
            icon: str = "info",
        ) -> str:
            return "ok"

        def storage_fn() -> str:
            harness.storage_dir.mkdir(parents=True, exist_ok=True)
            return str(harness.storage_dir)

        plugin_mod.storage = storage_fn

        host_ui_mod.NotificationLevel = NotificationLevel
        host_ui_mod.create_dock_panel = create_dock_panel
        host_ui_mod.create_window = create_window
        host_ui_mod.push_notification = push_notification
        host_ui_mod.message = ui_message
        host_ui_mod.WINDOW_MODELESS = 0

        host_preset_mod.process = MockPresetEditor()
        host_preset_mod.printer = MockPresetEditor()
        host_preset_mod.filament = MockPresetEditor()

        host_mod.plater = lambda: ReadOnlyPlater()
        host_mod.model = lambda: ReadOnlyModel()
        host_mod.preset_bundle = lambda: MockPresetBundle()
        host_mod.preset = host_preset_mod
        host_mod.ui = host_ui_mod
        host_mod.plugin = plugin_mod
        host_mod.app_language = lambda: "pt_BR"
        host_mod.app_info = lambda: {
            "version": "2.5.1",
            "orca_version": "2.5.1",
            "language": "pt_BR",
            "theme": "dark",
        }
        host_mod.gl_info = lambda: {"version": "4.6.0", "renderer": "MockGPU"}
        host_mod.selected_printer = lambda: None

        pages_mod.PagesPluginCapabilityBase = PagesPluginCapabilityBase
        script_mod.ScriptPluginCapabilityBase = ScriptPluginCapabilityBase

        orca_mod.base = OrcaBase
        orca_mod.plugin = plugin_decorator
        orca_mod.register_capability = register_capability
        orca_mod.request_permissions = request_permissions
        orca_mod.PythonPluginBase = PythonPluginBase
        orca_mod.PluginType = PluginType
        orca_mod.PluginResult = PluginResult
        orca_mod.LifecycleEvent = LifecycleEvent
        orca_mod.LifecycleEvtCode = LifecycleEvtCode
        orca_mod.ExecutionResult = ExecutionResult
        orca_mod.pages = pages_mod
        orca_mod.script = script_mod
        orca_mod.host = host_mod
        orca_mod.plugin_storage = plugin_mod

        return {
            "orca": orca_mod,
            "orca.pages": pages_mod,
            "orca.script": script_mod,
            "orca.host": host_mod,
            "orca.host.ui": host_ui_mod,
            "orca.host.preset": host_preset_mod,
            "orca.plugin": plugin_mod,
        }


def _extract_pep723_block(source: str) -> dict:
    """Extract and parse PEP 723 `# /// script ... # ///` block via stdlib tomllib."""
    match = re.search(
        r"(?m)^# /// script[ \t]*\r?\n((?:^#(?: .*|[ \t]*)\r?\n)+)^# ///[ \t]*$",
        source,
    )
    if not match:
        raise ValueError("Missing valid PEP 723 `# /// script ... # ///` metadata block")
    lines = []
    for raw_line in match.group(1).splitlines():
        if raw_line.startswith("# "):
            lines.append(raw_line[2:])
        elif raw_line.startswith("#"):
            lines.append(raw_line[1:])
    return tomllib.loads("\n".join(lines))


def _extract_script_blocks(html: str) -> list[str]:
    return re.findall(r"<script\b[^>]*>(.*?)</script>", html, flags=re.DOTALL | re.IGNORECASE)


class TestPluginBundleAndBridge(unittest.TestCase):
    """End-to-end verification of installed plugin layout, bridge capabilities, UI JS, and math parity."""

    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory(prefix="orca_vase_qa_plugin_")
        self.tmp_path = Path(self._tmpdir.name)
        self.harness = MockOrcaHostHarness(self.tmp_path / "plugin_storage")
        self._mock_mods = self.harness.build_modules()
        self._saved_sys_mods = {k: sys.modules.get(k) for k in self._mock_mods}
        sys.modules.update(self._mock_mods)

    def tearDown(self) -> None:
        for k, orig in self._saved_sys_mods.items():
            if orig is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = orig
        sys.modules.pop("_qa_loaded_orca_vase_generator", None)
        self._tmpdir.cleanup()

    def _active_bundle_path(self) -> Path:
        if INSTALLED_PLUGIN_PY.is_file():
            return INSTALLED_PLUGIN_PY
        return DIST_BUNDLE

    def _load_installed_bundle(self) -> types.ModuleType:
        bundle_path = self._active_bundle_path()
        self.assertTrue(
            bundle_path.is_file(),
            f"Plugin bundle missing at {bundle_path}",
        )
        # Read source and exec into module so Python NEVER writes __pycache__ next to bundle
        source = bundle_path.read_text(encoding="utf-8")
        mod = types.ModuleType("_qa_loaded_orca_vase_generator")
        mod.__file__ = str(bundle_path)
        code = compile(source, str(bundle_path), "exec")
        exec(code, mod.__dict__)
        sys.modules["_qa_loaded_orca_vase_generator"] = mod
        return mod

    def _assert_installed_dir_obeys_loader_rules(self, target_dir: Path | None = None) -> None:
        inst_dir = target_dir if target_dir is not None else INSTALLED_DIR
        self.assertTrue(
            inst_dir.is_dir(),
            f"Installed plugin directory does not exist: {inst_dir}",
        )
        all_entries = list(inst_dir.rglob("*"))
        all_files = [p for p in all_entries if p.is_file()]
        all_dirs = [p for p in all_entries if p.is_dir()]

        py_files = [p for p in all_files if p.suffix.lower() == ".py"]
        whl_files = [p for p in all_files if p.suffix.lower() == ".whl"]
        pyc_files = [p for p in all_files if p.suffix.lower() in (".pyc", ".pyo")]
        pycache_dirs = [p for p in all_dirs if p.name == "__pycache__"]

        self.assertEqual(
            len(py_files),
            1,
            f"OrcaSlicer.dll requires STRICTLY ONE .py file in {inst_dir}, found: {py_files}",
        )
        self.assertEqual(py_files[0].name, "orca_vase_generator.py")
        self.assertEqual(len(whl_files), 0, f"Forbidden .whl files in plugin folder: {whl_files}")
        self.assertEqual(len(pyc_files), 0, f"Forbidden .pyc files in plugin folder: {pyc_files}")
        self.assertEqual(
            len(pycache_dirs),
            0,
            f"Forbidden __pycache__ directories in plugin folder: {pycache_dirs}",
        )
        unexpected_files = [
            p.relative_to(inst_dir).as_posix()
            for p in all_files
            if p.parent != inst_dir or p.name not in ALLOWED_INSTALLED_FILENAMES
        ]
        self.assertEqual(
            unexpected_files,
            [],
            f"Unexpected files in {inst_dir} (allowed: {sorted(ALLOWED_INSTALLED_FILENAMES)}): {unexpected_files}",
        )

    def test_01_installed_plugin_layout_and_pep723_toml(self) -> None:
        self.assertTrue(DIST_BUNDLE.is_file(), f"Dist bundle missing at {DIST_BUNDLE}")
        self.assertTrue(DIST_ANY_BUNDLE.is_file(), f"OrcaCloud _any bundle missing at {DIST_ANY_BUNDLE}")

        dist_src = DIST_BUNDLE.read_text(encoding="utf-8")
        dist_any_src = DIST_ANY_BUNDLE.read_text(encoding="utf-8")
        self.assertEqual(
            dist_any_src,
            dist_src,
            "dist/orca_vase_generator_any.py must match dist/orca_vase_generator.py byte-for-byte",
        )

        # Validate source icon.svg (64x64)
        self.assertTrue(SRC_ICON_SVG.is_file(), f"Expected source icon.svg at {SRC_ICON_SVG}")
        src_svg_root = ET.fromstring(SRC_ICON_SVG.read_text(encoding="utf-8"))
        self.assertTrue(src_svg_root.tag.endswith("svg"))
        self.assertEqual(src_svg_root.attrib.get("width"), "64")
        self.assertEqual(src_svg_root.attrib.get("height"), "64")

        # When locally installed (i.e. without `--no-install`), verify strict OrcaSlicer dir invariants
        if INSTALLED_DIR.is_dir():
            self._assert_installed_dir_obeys_loader_rules(INSTALLED_DIR)
            installed_src = INSTALLED_PLUGIN_PY.read_text(encoding="utf-8")
            self.assertEqual(
                installed_src,
                dist_src,
                "Installed orca_vase_generator.py differs from dist/orca_vase_generator.py",
            )
            icon_path = INSTALLED_DIR / "icon.svg"
            self.assertTrue(icon_path.is_file(), f"Expected icon.svg in {INSTALLED_DIR}")
            svg_root = ET.fromstring(icon_path.read_text(encoding="utf-8"))
            self.assertTrue(svg_root.tag.endswith("svg"))
            self.assertEqual(svg_root.attrib.get("width"), "64")
            self.assertEqual(svg_root.attrib.get("height"), "64")

        # Parse PEP 723 TOML block via stdlib tomllib
        meta = _extract_pep723_block(dist_src)
        self.assertIn("requires-python", meta)
        self.assertIn("dependencies", meta)
        self.assertIsInstance(meta["dependencies"], list)
        self.assertTrue(
            any("numpy" in dep.lower() for dep in meta["dependencies"]),
            f"PEP 723 dependencies must declare numpy: {meta['dependencies']}",
        )

        plugin_meta = meta.get("tool", {}).get("orcaslicer", {}).get("plugin", {})
        self.assertEqual(plugin_meta.get("id"), "orca-vase-studio")
        self.assertTrue(bool(plugin_meta.get("name")), "Missing [tool.orcaslicer.plugin].name")
        self.assertNotIn(";", plugin_meta["name"])
        self.assertEqual(
            plugin_meta.get("version"),
            "1.3.3",
            f"Expected [tool.orcaslicer.plugin].version == '1.3.3', got {plugin_meta.get('version')!r}",
        )
        self.assertTrue(bool(plugin_meta.get("description")), "Missing [tool.orcaslicer.plugin].description")
        self.assertTrue(bool(plugin_meta.get("author")), "Missing [tool.orcaslicer.plugin].author")

        if PYPROJECT_TOML.is_file():
            pyproj = tomllib.loads(PYPROJECT_TOML.read_text(encoding="utf-8"))
            self.assertEqual(
                pyproj.get("project", {}).get("version"),
                "1.3.3",
                "pyproject.toml [project].version must be '1.3.3'",
            )
            self.assertEqual(
                pyproj.get("tool", {}).get("orcaslicer", {}).get("plugin", {}).get("version"),
                "1.3.3",
                "pyproject.toml [tool.orcaslicer.plugin].version must be '1.3.3'",
            )

    def test_02_plugin_registration_permissions_and_capabilities(self) -> None:
        self._load_installed_bundle()

        self.assertEqual(
            len(self.harness.plugin_classes),
            1,
            f"Entry module must have strictly 1 @orca.plugin class, got {self.harness.plugin_classes}",
        )
        plugin_cls = self.harness.plugin_classes[0]
        self.assertTrue(issubclass(plugin_cls, self._mock_mods["orca"].base))

        plugin_inst = plugin_cls()
        plugin_inst.register_capabilities()

        # Verify permissions requested
        self.assertGreaterEqual(
            len(self.harness.requested_permissions),
            1,
            "register_capabilities() must call orca.request_permissions(...)",
        )
        merged_perms: dict[str, object] = {}
        for perm in self.harness.requested_permissions:
            merged_perms.update(perm)
        self.assertTrue(
            bool(merged_perms.get("threading")),
            f"threading=True permission required for live preset updates: {merged_perms}",
        )
        self.assertFalse(
            bool(merged_perms.get("process")),
            f"Phase 2 must NOT request `process` permission (WM_COPYDATA is in-process): {merged_perms}",
        )

        fs_rw = [str(p).replace("\\", "/").lower() for p in merged_perms.get("fs_readwrite", [])]
        fs_r = [str(p).replace("\\", "/").lower() for p in merged_perms.get("fs_read", [])]
        self.assertTrue(
            any("plugin_data/orca_vase_generator" in p for p in fs_rw),
            f"fs_readwrite must include plugin_data\\orca_vase_generator: {merged_perms.get('fs_readwrite')}",
        )
        self.assertTrue(
            any("plugin_data/orca_vase_generator" in p for p in fs_r),
            f"fs_read must include plugin_data\\orca_vase_generator: {merged_perms.get('fs_read')}",
        )

        # Verify both Pages and Script capabilities registered
        orca_pages_base = self._mock_mods["orca.pages"].PagesPluginCapabilityBase
        orca_script_base = self._mock_mods["orca.script"].ScriptPluginCapabilityBase

        page_caps = [c for c in self.harness.registered_capabilities if issubclass(c, orca_pages_base)]
        script_caps = [c for c in self.harness.registered_capabilities if issubclass(c, orca_script_base)]
        self.assertEqual(len(page_caps), 1, f"Expected 1 Pages capability, got {page_caps}")
        self.assertGreaterEqual(len(script_caps), 1, f"Expected >=1 Script capability, got {script_caps}")

        page_inst = page_caps[0]()
        page_inst.on_load()
        page_name = page_inst.get_name()
        self.assertIsInstance(page_name, str)
        self.assertTrue(bool(page_name.strip()))
        self.assertNotIn(";", page_name)

        # Verify standalone single-file `get_icon()` auto-materialization when `icon.svg` is NOT next to `__file__`
        mod = sys.modules["_qa_loaded_orca_vase_generator"]
        self.assertTrue(hasattr(mod, "ICON_SVG_CONTENT"))
        empty_py_dir = self.tmp_path / "sideload_single_file"
        empty_py_dir.mkdir(parents=True, exist_ok=True)
        with (
            mock.patch.dict(mod.__dict__, {"__file__": str(empty_py_dir / "orca_vase_generator.py")}),
            mock.patch.object(mod, "_default_installed_plugin_dir", return_value=empty_py_dir),
        ):
            materialized_icon = page_inst.get_icon()
            self.assertTrue(bool(materialized_icon), "Standalone single-file get_icon() returned empty path")
            mat_path = Path(materialized_icon)
            self.assertTrue(mat_path.is_file(), f"Auto-materialized icon missing at {mat_path}")
            self.assertEqual(mat_path.parent.resolve(), self.harness.storage_dir.resolve())
            mat_svg = ET.fromstring(mat_path.read_text(encoding="utf-8"))
            self.assertTrue(mat_svg.tag.endswith("svg"))
            self.assertEqual(mat_svg.attrib.get("width"), "64")

        script_inst = script_caps[0]()
        script_inst.on_load()
        script_name = script_inst.get_name()
        self.assertIsInstance(script_name, str)
        self.assertTrue(bool(script_name.strip()))
        self.assertNotIn(";", script_name)

        exec_res = script_inst.execute()
        if asyncio.iscoroutine(exec_res):
            exec_res = asyncio.run(exec_res)
        self.assertIsNotNone(exec_res)

    def test_03_get_ui_page_and_dock_offline_and_node_js_syntax(self) -> None:
        mod = self._load_installed_bundle()
        plugin_inst = self.harness.plugin_classes[0]()
        plugin_inst.register_capabilities()

        orca_pages_base = self._mock_mods["orca.pages"].PagesPluginCapabilityBase
        page_cls = [c for c in self.harness.registered_capabilities if issubclass(c, orca_pages_base)][0]
        page_inst = page_cls()
        page_inst.on_load()

        html_page = page_inst.get_ui()
        if hasattr(mod, "get_studio_html"):
            html_dock = mod.get_studio_html(mode="dock")
        else:
            orca_script_base = self._mock_mods["orca.script"].ScriptPluginCapabilityBase
            script_cls = [c for c in self.harness.registered_capabilities if issubclass(c, orca_script_base)][0]
            s_inst = script_cls()
            res = s_inst.execute()
            if asyncio.iscoroutine(res):
                asyncio.run(res)
            html_dock = self.harness.dock_panels[0].html if self.harness.dock_panels else html_page

        for mode_name, html in (("page", html_page), ("dock", html_dock)):
            with self.subTest(mode=mode_name):
                self.assertIsInstance(html, str)
                self.assertGreater(len(html), 10000, f"{mode_name} HTML unexpectedly tiny")
                self.assertIn("<html", html.lower())

                # Zero external CDN scripts / stylesheets
                ext_scripts = re.findall(
                    r"<script\b[^>]+src=[\"']https?://[^\"']+[\"']",
                    html,
                    flags=re.IGNORECASE,
                )
                ext_links = re.findall(
                    r"<link\b[^>]+href=[\"']https?://[^\"']+[\"']",
                    html,
                    flags=re.IGNORECASE,
                )
                self.assertEqual(ext_scripts, [], f"{mode_name} HTML contains external CDN script")
                self.assertEqual(ext_links, [], f"{mode_name} HTML contains external CDN link")

                # Structural checks for WebGL2, Orca bridge, bilingual UI
                self.assertIn("webgl2", html.lower())
                self.assertIn("postMessage", html)
                self.assertIn("onMessage", html)

                # Phase 2 UI & Visualization Mode checks:
                # 1) Raio-X mode & WebGL X-Ray shader uniform/blending
                self.assertIn("raio-x", html.lower(), f"{mode_name} HTML missing Raio-X mode")
                self.assertIsNotNone(
                    re.search(r"u_xray|xraymode", html, flags=re.IGNORECASE),
                    f"{mode_name} HTML missing X-Ray WebGL shader uniform/mode",
                )
                # 2) Horizontal Z slice mode (Fatia Horizontal Z / u_clipMode)
                self.assertIsNotNone(
                    re.search(r"fatia|z[-_]?slice|u_clipmode", html, flags=re.IGNORECASE),
                    f"{mode_name} HTML missing horizontal Z slice mode",
                )
                # 3) #vp-caliper-canvas CAD overlay
                self.assertIn(
                    "vp-caliper-canvas",
                    html,
                    f"{mode_name} HTML missing #vp-caliper-canvas CAD overlay",
                )
                # 4) max: 25 wall thickness slider & stl_always_open_hollow toggle
                self.assertIsNotNone(
                    re.search(
                        r"wall_thickness_mm[\s\S]{0,250}?(?:max\s*[:=]\s*[\"']?25(?:\.0)?[\"']?)"
                        r"|(?:max\s*[:=]\s*[\"']?25(?:\.0)?[\"']?)[\s\S]{0,250}?wall_thickness_mm",
                        html,
                        flags=re.IGNORECASE,
                    ),
                    f"{mode_name} HTML missing max=25 wall_thickness_mm slider definition",
                )
                self.assertIn(
                    "stl_always_open_hollow",
                    html,
                    f"{mode_name} HTML missing stl_always_open_hollow option",
                )

                scripts = _extract_script_blocks(html)
                self.assertGreaterEqual(len(scripts), 1, f"No <script> block in {mode_name} HTML")

                node_bin = shutil.which("node")
                if node_bin:
                    for s_idx, js_code in enumerate(scripts):
                        js_file = self.tmp_path / f"ui_{mode_name}_{s_idx}.js"
                        js_file.write_text(js_code, encoding="utf-8")
                        proc = subprocess.run(
                            [node_bin, "--check", str(js_file)],
                            capture_output=True,
                            text=True,
                            encoding="utf-8",
                            timeout=15,
                        )
                        self.assertEqual(
                            proc.returncode,
                            0,
                            f"JS syntax error in {mode_name} script[{s_idx}]:\n{proc.stderr}",
                        )

    def test_04_js_vs_python_surface_radius_parity(self) -> None:
        """Cross-check client-side WebGL2 JS surface math against Python `evaluate_radius_grid`."""
        mod = self._load_installed_bundle()
        html = (
            mod.get_studio_html(mode="page")
            if hasattr(mod, "get_studio_html")
            else ""
        )
        if not html:
            plugin_inst = self.harness.plugin_classes[0]()
            plugin_inst.register_capabilities()
            orca_pages_base = self._mock_mods["orca.pages"].PagesPluginCapabilityBase
            page_cls = [c for c in self.harness.registered_capabilities if issubclass(c, orca_pages_base)][0]
            html = page_cls().get_ui()

        scripts = _extract_script_blocks(html)
        main_js = max(scripts, key=len)

        # Discover all top-level/IIFE function names in the script so we can export them safely in Node
        fn_names = sorted(
            set(
                re.findall(
                    r"\bfunction\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*\(",
                    main_js,
                )
                + re.findall(
                    r"\b(?:const|let|var)\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*(?:function|\([^)]*\)\s*=>|[A-Za-z_$][A-Za-z0-9_$]*\s*=>)",
                    main_js,
                )
            )
        )
        export_entries = ", ".join(
            f"{name}: (typeof {name} !== 'undefined' ? {name} : undefined)"
            for name in fn_names
        )
        export_stmt = f"\nglobalThis.__qaFns = Object.assign(globalThis.__qaFns || {{}}, {{{export_entries}}});\n"

        # Inject export right before closing IIFE if wrapped in IIFE, AND at end of script
        iife_close = re.search(r"\}\s*\)\s*\([^)]*\)\s*;?\s*$", main_js)
        if iife_close:
            instrumented_js = (
                main_js[: iife_close.start()]
                + export_stmt
                + main_js[iife_close.start() :]
                + export_stmt
            )
        else:
            instrumented_js = main_js + export_stmt

        test_cases = [
            ("default_waves", normalize_params(DEFAULT_PARAMS)),
            (
                "ribbed_hex_twist",
                normalize_params(
                    {
                        "height_mm": 150.0,
                        "polygon_sides": 6,
                        "polygon_roundness": 0.30,
                        "global_twist_deg": 60.0,
                        "textures": {
                            "ribbed": {
                                "enabled": True,
                                "depth_mm": 2.8,
                                "count": 24,
                                "duty_cycle": 0.50,
                                "sharpness": 0.40,
                                "twist_deg": 45.0,
                                "phase_deg": 15.0,
                            },
                            "waves": {"enabled": False},
                        },
                    }
                ),
            ),
            (
                "origami_diamonds",
                normalize_params(
                    {
                        "height_mm": 140.0,
                        "textures": {
                            "waves": {"enabled": False},
                            "origami": {
                                "enabled": True,
                                "depth_mm": 3.0,
                                "cells_around": 12,
                                "cells_vertical": 8,
                                "crease_sharpness": 0.75,
                                "stagger": 0.50,
                            },
                        },
                    }
                ),
            ),
            (
                "cellular_coral",
                normalize_params(
                    {
                        "height_mm": 155.0,
                        "textures": {
                            "waves": {"enabled": False},
                            "cellular": {
                                "enabled": True,
                                "depth_mm": 2.4,
                                "scale_angular": 8,
                                "scale_vertical_mm": 22.0,
                                "ridge_mode": True,
                                "octaves": 2,
                                "seed": 42,
                            },
                        },
                    }
                ),
            ),
        ]

        from vase_studio.geometric_patterns import GEOMETRIC_PATTERNS
        for pattern in GEOMETRIC_PATTERNS:
            test_cases.append(("geometric_" + pattern, normalize_params({
                "global_twist_deg": 53.0,
                "textures": {"geometric": {"enabled": True, "pattern": pattern,
                    "twist_deg": -137, "phase_deg": 29, "strength_bottom": 0.2,
                    "strength_middle": 1.7, "strength_top": 0.6},
                    "ribbed": {"enabled": True}}})))

        n_z = 9
        n_theta = 8
        py_payload = []
        for label, p in test_cases:
            z_vals, theta_vals, radii_grid = evaluate_radius_grid(p, n_z=n_z, n_theta=n_theta)
            py_payload.append(
                {
                    "label": label,
                    "params": p,
                    "z_vals": [float(x) for x in z_vals],
                    "theta_vals": [float(x) for x in theta_vals],
                    "py_radii": [[float(v) for v in row] for row in radii_grid],
                }
            )

        probe_params = normalize_params(
            {
                "height_mm": 160.0,
                "base_diameter_mm": 76.0,
                "belly_diameter_mm": 110.0,
                "belly_height_ratio": 0.34,
                "waist_diameter_mm": 68.0,
                "waist_height_ratio": 0.68,
                "neck_diameter_mm": 82.0,
                "lip_flare_mm": 4.0,
                "polygon_sides": 0,
                "use_custom_profile": False,
                "textures": {
                    "ribbed": {"enabled": False},
                    "waves": {"enabled": False},
                    "origami": {"enabled": False},
                    "cellular": {"enabled": False},
                },
            }
        )

        node_harness = r"""
const fs = require('fs');

// Minimal headless browser + WebGL2 + Canvas2D shim so Studio UI boots cleanly in Node
const noop = () => {};
const makeGlStub = () => new Proxy({
  ARRAY_BUFFER: 0x8892,
  ELEMENT_ARRAY_BUFFER: 0x8893,
  STATIC_DRAW: 0x88E4,
  DYNAMIC_DRAW: 0x88E8,
  TRIANGLES: 4,
  LINES: 1,
  LINE_LOOP: 2,
  LINE_STRIP: 3,
  FLOAT: 0x1406,
  UNSIGNED_INT: 0x1405,
  UNSIGNED_SHORT: 0x1403,
  VERTEX_SHADER: 0x8B31,
  FRAGMENT_SHADER: 0x8B30,
  COMPILE_STATUS: 0x8B81,
  LINK_STATUS: 0x8B82,
  DEPTH_TEST: 0x0B71,
  CULL_FACE: 0x0B44,
  FRONT: 0x0404,
  BACK: 0x0405,
  BLEND: 0x0BE2,
  SRC_ALPHA: 0x0302,
  ONE_MINUS_SRC_ALPHA: 0x0303,
  ONE: 1,
  ZERO: 0,
  LEQUAL: 0x0203,
  LESS: 0x0201,
  COLOR_BUFFER_BIT: 0x4000,
  DEPTH_BUFFER_BIT: 0x0100,
  createShader: () => ({}),
  getShaderParameter: () => true,
  getShaderInfoLog: () => '',
  createProgram: () => ({}),
  getProgramParameter: () => true,
  getProgramInfoLog: () => '',
  createBuffer: () => ({}),
  createVertexArray: () => ({}),
  getUniformLocation: () => ({}),
  getAttribLocation: () => 0,
  getExtension: () => ({}),
  canvas: { width: 800, height: 600, clientWidth: 800, clientHeight: 600 },
}, {
  get(target, prop) {
    if (prop in target) return target[prop];
    return noop;
  }
});

const make2dStub = () => new Proxy({
  canvas: { width: 800, height: 600, clientWidth: 800, clientHeight: 600 },
  measureText: () => ({ width: 20 }),
  createLinearGradient: () => ({ addColorStop: noop }),
  createRadialGradient: () => ({ addColorStop: noop }),
}, {
  get(target, prop) {
    if (prop in target) return target[prop];
    return noop;
  }
});

const makeEl = (tag = 'div') => {
  const el = {
    tagName: String(tag).toUpperCase(),
    style: {},
    dataset: {},
    classList: { add: noop, remove: noop, toggle: noop, contains: () => false },
    children: [],
    options: [],
    parentElement: null,
    parentNode: null,
    nextElementSibling: null,
    previousElementSibling: null,
    value: '0',
    checked: false,
    disabled: false,
    textContent: '',
    innerHTML: '',
    width: 800,
    height: 600,
    clientWidth: 800,
    clientHeight: 600,
    offsetWidth: 800,
    offsetHeight: 600,
    addEventListener: noop,
    removeEventListener: noop,
    appendChild(c) { if (c) { c.parentElement = this; c.parentNode = this; } this.children.push(c); return c; },
    insertBefore(c) { if (c) { c.parentElement = this; c.parentNode = this; } this.children.push(c); return c; },
    removeChild: noop,
    remove: noop,
    closest: () => null,
    matches: () => false,
    focus: noop,
    blur: noop,
    click: noop,
    setAttribute: noop,
    getAttribute: () => null,
    hasAttribute: () => false,
    getBoundingClientRect: () => ({ left: 0, top: 0, width: 800, height: 600, right: 800, bottom: 600 }),
    querySelector: () => makeEl('div'),
    querySelectorAll: () => [],
    getContext(kind) {
      if (String(kind).includes('webgl')) return makeGlStub();
      return make2dStub();
    },
    setPointerCapture: noop,
    releasePointerCapture: noop,
  };
  return el;
};

globalThis.window = globalThis;
globalThis.self = globalThis;
globalThis.devicePixelRatio = 1;
globalThis.requestAnimationFrame = () => 1;
globalThis.cancelAnimationFrame = noop;
globalThis.ResizeObserver = class { observe() {} unobserve() {} disconnect() {} };
globalThis.MutationObserver = class { observe() {} disconnect() {} };
globalThis.localStorage = { getItem: () => null, setItem: noop, removeItem: noop };
globalThis.navigator = { language: 'pt-BR', userAgent: 'NodeQA', clipboard: { writeText: async () => {} } };
globalThis.document = {
  documentElement: makeEl('html'),
  body: makeEl('body'),
  head: makeEl('head'),
  getElementById: (id) => makeEl('canvas'),
  querySelector: () => makeEl('div'),
  querySelectorAll: () => [],
  createElement: (tag) => makeEl(tag),
  createElementNS: (_ns, tag) => makeEl(tag),
  addEventListener: noop,
  removeEventListener: noop,
};
globalThis.orca = {
  postMessage: noop,
  onMessage: (cb) => { globalThis.__orcaOnMsg = cb; },
};

const uiCode = fs.readFileSync(process.argv[2], 'utf8');
const payload = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
eval(uiCode);

const fns = globalThis.__qaFns || {};
const probe = payload.probe;

// Auto-detect either a grid evaluator (params, nZ, nTheta) or point evaluator
let evaluator = null;

for (const [name, fn] of Object.entries(fns)) {
  if (typeof fn !== 'function') continue;

  // Try grid signatures: fn(params, nZ, nTheta)
  try {
    const g = fn(probe, 11, 8);
    if (g) {
      const arr = g.radii || g.grid || g;
      if (Array.isArray(arr) || ArrayBuffer.isView(arr)) {
        const r0 = Array.isArray(arr[0]) ? arr[0][0] : arr[0];
        const midIdx = Array.isArray(arr[0]) ? arr[4][0] : arr[4 * 8];
        if (Math.abs(r0 - 38.0) < 0.25 && midIdx > 48.0 && midIdx < 56.0) {
          evaluator = {
            kind: 'grid',
            name,
            evalCase(tc) {
              const res = fn(tc.params, tc.z_vals.length, tc.theta_vals.length);
              const data = res.radii || res.grid || res;
              const out = [];
              for (let i = 0; i < tc.z_vals.length; i++) {
                const row = [];
                for (let j = 0; j < tc.theta_vals.length; j++) {
                  row.push(Array.isArray(data[i]) ? Number(data[i][j]) : Number(data[i * tc.theta_vals.length + j]));
                }
                out.push(row);
              }
              return out;
            }
          };
          break;
        }
      }
    }
  } catch (_) {}

  // Try point signatures returning scalar outer radius (38.0 at z=0, ~55.0 at z=54.4)
  const callPatterns = [
    ['(p, z, th)', (p, z, zN, th) => fn(p, z, th)],
    ['(z, th, p)', (p, z, zN, th) => fn(z, th, p)],
    ['(p, zNorm, th)', (p, z, zN, th) => fn(p, zN, th)],
    ['(zNorm, th, p)', (p, z, zN, th) => fn(zN, th, p)],
  ];
  for (const [sig, caller] of callPatterns) {
    try {
      const v0 = caller(probe, 0.0, 0.0, 0.5);
      const vBelly = caller(probe, 0.34 * 160.0, 0.34, 0.5);
      const vTop = caller(probe, 160.0, 1.0, 0.5);
      if (
        typeof v0 === 'number' && Number.isFinite(v0) &&
        typeof vBelly === 'number' && Number.isFinite(vBelly) &&
        Math.abs(v0 - 38.0) < 0.25 &&
        Math.abs(vBelly - 55.0) < 0.5 &&
        Math.abs(vTop - 45.0) < 0.5
      ) {
        // Confirm it also responds to waves texture!
        const probeWave = JSON.parse(JSON.stringify(probe));
        probeWave.textures.waves.enabled = true;
        probeWave.textures.waves.depth_mm = 4.0;
        const vw = caller(probeWave, 80.0, 0.5, 0.7);
        const vp = caller(probe, 80.0, 0.5, 0.7);
        if (Math.abs(vw - vp) > 0.05) {
          evaluator = {
            kind: 'point:' + sig,
            name,
            evalCase(tc) {
              const H = tc.params.height_mm;
              return tc.z_vals.map((z) => {
                const zN = H > 0 ? z / H : 0;
                return tc.theta_vals.map((th) => Number(caller(tc.params, z, zN, th)));
              });
            }
          };
          break;
        }
      }
    } catch (_) {}
  }
  if (evaluator) break;
}

if (!evaluator) {
  console.log(JSON.stringify({ ok: false, fnNames: Object.keys(fns) }));
  process.exit(0);
}

const results = payload.cases.map((tc) => ({
  label: tc.label,
  js_radii: evaluator.evalCase(tc),
}));
console.log(JSON.stringify({ ok: true, evaluator: evaluator.name + ' [' + evaluator.kind + ']', results }));
"""
        ui_js_path = self.tmp_path / "instrumented_studio_ui.js"
        payload_path = self.tmp_path / "parity_payload.json"
        runner_path = self.tmp_path / "parity_runner.js"

        ui_js_path.write_text(instrumented_js, encoding="utf-8")
        payload_path.write_text(
            json.dumps({"probe": probe_params, "cases": py_payload}),
            encoding="utf-8",
        )
        runner_path.write_text(node_harness, encoding="utf-8")

        node_bin = shutil.which("node")
        if not node_bin:
            for tc_py in py_payload:
                arr_py = np.array(tc_py["py_radii"], dtype=np.float64)
                self.assertEqual(arr_py.shape, (n_z, n_theta))
                self.assertTrue(np.all(np.isfinite(arr_py)))
            return

        proc = subprocess.run(
            [node_bin, str(runner_path), str(ui_js_path), str(payload_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=20,
        )
        self.assertEqual(
            proc.returncode,
            0,
            f"Node parity runner crashed:\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}",
        )
        out = json.loads(proc.stdout.strip().splitlines()[-1])
        self.assertTrue(
            out.get("ok"),
            f"Could not locate matching JS surface radius evaluator among functions: {out.get('fnNames')}",
        )

        for tc_py, tc_js in zip(py_payload, out["results"]):
            label = tc_py["label"]
            arr_py = np.array(tc_py["py_radii"], dtype=np.float64)
            arr_js = np.array(tc_js["js_radii"], dtype=np.float64)
            self.assertEqual(arr_py.shape, arr_js.shape)
            self.assertTrue(np.all(np.isfinite(arr_js)), f"JS produced NaN/Inf in {label}")
            max_diff = float(np.max(np.abs(arr_py - arr_js)))
            self.assertLess(
                max_diff,
                1e-12,
                f"JS vs Python radius mismatch on '{label}': max |r_js - r_py| = {max_diff:.3e} mm",
            )

    def test_05_all_bridge_on_message_commands(self) -> None:
        mod = self._load_installed_bundle()
        plugin_inst = self.harness.plugin_classes[0]()
        plugin_inst.register_capabilities()

        self.assertTrue(
            hasattr(mod, "_dispatch_copydata_to_hwnd"),
            "Bundle must expose `_dispatch_copydata_to_hwnd` for in-process WM_COPYDATA dispatch",
        )
        self.assertTrue(
            hasattr(mod, "_find_orca_mainframe_hwnd"),
            "Bundle must expose `_find_orca_mainframe_hwnd` for MainFrame HWND lookup",
        )
        self.assertTrue(
            hasattr(mod, "_format_other_instance_payload"),
            "Bundle must expose `_format_other_instance_payload` for C-escaped WM_COPYDATA formatting",
        )

        orca_pages_base = self._mock_mods["orca.pages"].PagesPluginCapabilityBase
        page_cls = [c for c in self.harness.registered_capabilities if issubclass(c, orca_pages_base)][0]
        page = page_cls()
        page.on_load()

        def send_and_collect(payload: dict | str, expected_types: set[str], timeout: float = 5.0) -> list[dict]:
            start_idx = len(self.harness.posted_page_messages)
            page.on_message(payload)
            deadline = time.monotonic() + timeout
            while time.monotonic() < deadline:
                batch = self.harness.posted_page_messages[start_idx:]
                seen = {m.get("type") for m in batch if isinstance(m, dict)}
                if expected_types.issubset(seen):
                    return batch
                time.sleep(0.03)
            return self.harness.posted_page_messages[start_idx:]

        # 1. `ready` (passed as raw JSON string matching C++ (self, str) binding!)
        ready_msgs = send_and_collect(
            json.dumps({"type": "ready", "mode": "page"}),
            {"init_state", "analysis_result"},
        )
        init_msg = [m for m in ready_msgs if m.get("type") == "init_state"][0]
        self.assertIn(init_msg.get("lang"), mod.supported_languages())
        self.assertIn(init_msg.get("theme"), ("dark", "light"))
        self.assertEqual(len(init_msg.get("builtin_presets", [])), 12)
        self.assertIsInstance(init_msg.get("params"), dict)
        self.assertEqual(init_msg["params"].get("print_mode"), "shelled_hollow")
        self.assertIs(init_msg["params"].get("stl_always_open_hollow"), True)
        self.assertTrue(bool(init_msg.get("export_dir")))

        init_analysis = [m for m in ready_msgs if m.get("type") == "analysis_result"][0]
        self.assertIn("max_overhang_deg", init_analysis["report"])

        # 2. `analyze` (passed as dict)
        spiral_params = normalize_params(
            {
                "name": "Bridge QA Vase",
                "height_mm": 135.0,
                "resolution_angular": 72,
                "resolution_vertical": 60,
                "print_mode": "spiral_vase",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "auto_configure_slicer": True,
                "spiral_bottom_layers": 5,
                "spiral_line_width_mm": 0.65,
            }
        )
        an_msgs = send_and_collect(
            {"type": "analyze", "params": spiral_params},
            {"analysis_result"},
        )
        an_rep = [m for m in an_msgs if m.get("type") == "analysis_result"][0]["report"]
        self.assertAlmostEqual(an_rep["dimensions_mm"][2], 135.0, delta=1.0)

        # 3. `randomize`
        rnd_msgs = send_and_collect(
            json.dumps({"type": "randomize", "seed": 77, "params": spiral_params}),
            {"params_updated"},
        )
        rnd_msg = [m for m in rnd_msgs if m.get("type") == "params_updated"][0]
        self.assertEqual(rnd_msg.get("source"), "randomize")
        self.assertIsInstance(rnd_msg.get("params"), dict)

        # 4. `preset_save` & 5. `preset_delete`
        save_msgs = send_and_collect(
            json.dumps({"type": "preset_save", "name": "Preset Bridge QA", "params": spiral_params}),
            {"presets_updated"},
        )
        saved_list = [m for m in save_msgs if m.get("type") == "presets_updated"][0]["user_presets"]
        self.assertEqual(len(saved_list), 1)
        saved_id = saved_list[0]["id"]

        del_msgs = send_and_collect(
            json.dumps({"type": "preset_delete", "id": saved_id}),
            {"presets_updated"},
        )
        after_del = [m for m in del_msgs if m.get("type") == "presets_updated"][0]["user_presets"]
        self.assertEqual(len(after_del), 0)

        # 6a. `export_file(format="stl")` with `print_mode="spiral_vase"` + `stl_always_open_hollow=True`
        #     MUST export an open-mouthed hollow .STL!
        exp_stl_msgs = send_and_collect(
            json.dumps(
                {
                    "type": "export_file",
                    "format": "stl",
                    "params": spiral_params,
                    "include_saucer": False,
                    "filename": "qa_bridge_open_spiral_guard.stl",
                }
            ),
            {"action_result"},
        )
        stl_res = [m for m in exp_stl_msgs if m.get("type") == "action_result"][0]
        self.assertTrue(stl_res.get("ok"), f"STL export_file failed: {stl_res}")
        self.assertEqual(stl_res.get("action"), "export_file")
        stl_paths = stl_res.get("paths") or ([stl_res["path"]] if "path" in stl_res else [])
        self.assertGreaterEqual(len(stl_paths), 1)
        stl_file_path = Path(stl_paths[0])
        self.assertTrue(stl_file_path.is_file())
        stl_guard_stats = _inspect_binary_stl_open_mouth(stl_file_path, 135.0)
        self.assertEqual(
            stl_guard_stats["top_center_cap_tris"],
            0,
            "export_file(format='stl') with print_mode='spiral_vase' + stl_always_open_hollow=True closed the mouth!",
        )
        self.assertGreater(
            stl_guard_stats["inward_cavity_tris"],
            0,
            "export_file(format='stl') with stl_always_open_hollow=True lacked an inner hollow cavity!",
        )

        # 6b. `export_file(format="stl", include_saucer=True)` with `print_mode="spiral_vase"` and
        #     `stl_always_open_hollow=False` MUST still generate an open-mouthed hollow vase!
        spiral_optout_params = copy.deepcopy(spiral_params)
        spiral_optout_params["stl_always_open_hollow"] = False
        exp_saucer_stl_msgs = send_and_collect(
            json.dumps(
                {
                    "type": "export_file",
                    "format": "stl",
                    "params": spiral_optout_params,
                    "include_saucer": True,
                    "filename": "qa_bridge_saucer_combo.stl",
                }
            ),
            {"action_result"},
        )
        saucer_stl_res = [m for m in exp_saucer_stl_msgs if m.get("type") == "action_result"][0]
        self.assertTrue(saucer_stl_res.get("ok"), f"STL+saucer export_file failed: {saucer_stl_res}")
        saucer_stl_paths = saucer_stl_res.get("paths", [])
        self.assertEqual(len(saucer_stl_paths), 2)
        combo_stl_stats = _inspect_binary_stl_open_mouth(Path(saucer_stl_paths[0]), 135.0)
        self.assertEqual(
            combo_stl_stats["top_center_cap_tris"],
            0,
            "include_saucer=True with print_mode='spiral_vase' generated a closed-mouth STL!",
        )
        self.assertGreater(combo_stl_stats["inward_cavity_tris"], 0)

        # 6c. `export_file(format="3mf", include_saucer=True)` with `print_mode="spiral_vase"`
        #     MUST force shelled_hollow BEFORE generate_vase_mesh AND set spiral_mode == "0"!
        exp_3mf_msgs = send_and_collect(
            json.dumps(
                {
                    "type": "export_file",
                    "format": "3mf",
                    "params": spiral_params,
                    "include_saucer": True,
                    "filename": "qa_bridge_export.3mf",
                }
            ),
            {"action_result"},
        )
        mf_res = [m for m in exp_3mf_msgs if m.get("type") == "action_result"][0]
        self.assertTrue(mf_res.get("ok"), f"3MF export_file failed: {mf_res}")
        mf_paths = mf_res.get("paths") or ([mf_res["path"]] if "path" in mf_res else [])
        self.assertGreaterEqual(len(mf_paths), 1)
        mf_file = Path(mf_paths[0])
        self.assertTrue(zipfile.is_zipfile(mf_file))
        mf_vase_stats = _inspect_3mf_vase_open_mouth(mf_file, 135.0)
        self.assertEqual(
            mf_vase_stats["top_center_cap_tris"],
            0,
            "3MF export with include_saucer=True + spiral_vase generated a closed-top solid block!",
        )
        self.assertGreater(mf_vase_stats["inward_cavity_tris"], 0)
        with zipfile.ZipFile(mf_file, "r") as zf:
            mf_proj = json.loads(zf.read("Metadata/project_settings.config").decode("utf-8"))
            self.assertEqual(mf_proj.get("spiral_mode"), "0")

        # 7a. `send_to_plater` in default `shelled_hollow` mode -> ZERO subprocess.Popen,
        #     background-thread WM_COPYDATA dispatch, exact C-escaped payload, & background preset tx!
        hollow_params = normalize_params(
            {
                "name": "Bridge Hollow Plater",
                "height_mm": 135.0,
                "resolution_angular": 72,
                "resolution_vertical": 60,
                "print_mode": "shelled_hollow",
                "wall_thickness_mm": 2.52,
                "bottom_thickness_mm": 3.2,
                "auto_configure_slicer": True,
            }
        )
        self.harness.process_transactions.clear()
        self.harness.tx_event.clear()
        copydata_calls: list[dict] = []
        copydata_ev = threading.Event()

        def _spy_dispatch_copydata(hwnd: int, payload_str: str, *args: object, **kwargs: object) -> tuple[bool, str]:
            tid = threading.get_ident()
            copydata_calls.append(
                {
                    "hwnd": hwnd,
                    "payload_str": payload_str,
                    "thread_id": tid,
                    "on_ui_thread": (tid == self.harness.main_thread_id),
                }
            )
            copydata_ev.set()
            return (True, "mock_copydata_ok")

        with (
            mock.patch("subprocess.Popen") as mock_popen,
            mock.patch.object(mod, "_find_orca_mainframe_hwnd", return_value=0x002468AC),
            mock.patch.object(mod, "_dispatch_copydata_to_hwnd", side_effect=_spy_dispatch_copydata),
        ):
            plater_hollow_msgs = send_and_collect(
                json.dumps(
                    {
                        "type": "send_to_plater",
                        "params": hollow_params,
                        "include_saucer": False,
                    }
                ),
                {"action_result"},
                timeout=8.0,
            )
            plater_hollow_res = [m for m in plater_hollow_msgs if m.get("type") == "action_result"][0]
            self.assertTrue(plater_hollow_res.get("ok"), f"send_to_plater (hollow) failed: {plater_hollow_res}")
            self.assertEqual(plater_hollow_res.get("action"), "send_to_plater")

            self.assertTrue(copydata_ev.wait(timeout=4.0), "_dispatch_copydata_to_hwnd was not invoked!")
            self.assertTrue(self.harness.tx_event.wait(timeout=4.0), "Background preset update did not run!")
            self.assertEqual(
                mock_popen.call_count,
                0,
                f"CRITICAL: send_to_plater must call ZERO subprocess.Popen, got {mock_popen.call_count}!",
            )

        self.assertEqual(len(copydata_calls), 1)
        cd_call = copydata_calls[0]
        self.assertFalse(
            cd_call["on_ui_thread"],
            "CRITICAL: _dispatch_copydata_to_hwnd must run on a background thread, NOT the UI thread!",
        )
        self.assertEqual(cd_call["hwnd"], 0x002468AC)
        raw_payload = cd_call["payload_str"]
        self.assertFalse(raw_payload.endswith(";"), f"WM_COPYDATA payload must have NO trailing ';': {raw_payload!r}")
        ok_parse, parsed_args = _unescape_strings_cstyle_orca(raw_payload)
        self.assertTrue(ok_parse, f"OrcaSlicer unescape_strings_cstyle rejected payload: {raw_payload!r}")
        self.assertEqual(len(parsed_args), 2, f"Expected [argv0, stl_path], got: {parsed_args}")
        self.assertEqual(parsed_args[0], "orca-slicer.exe")
        self.assertTrue(Path(parsed_args[1]).is_file(), f"STL path in WM_COPYDATA missing on disk: {parsed_args[1]}")
        self.assertEqual(
            Path(parsed_args[1]).resolve(),
            Path(plater_hollow_res["paths"][0]).resolve(),
        )
        hollow_plater_stats = _inspect_binary_stl_open_mouth(Path(parsed_args[1]), 135.0)
        self.assertEqual(hollow_plater_stats["top_center_cap_tris"], 0)
        self.assertGreater(hollow_plater_stats["inward_cavity_tris"], 0)

        merged_hollow_tx: dict[str, str] = {}
        for tx in self.harness.process_transactions:
            self.assertFalse(tx["on_ui_thread"])
            merged_hollow_tx.update(tx["updates"])
        self.assertEqual(merged_hollow_tx.get("spiral_mode"), "0")
        self.assertIn("wall_loops", merged_hollow_tx)
        self.assertGreaterEqual(int(merged_hollow_tx["wall_loops"]), 3)
        self.assertIn("bottom_shell_layers", merged_hollow_tx)
        self.assertGreaterEqual(int(merged_hollow_tx["bottom_shell_layers"]), 8)

        # 7b. `send_to_plater` in `spiral_vase` single-object mode -> ZERO subprocess.Popen,
        #     WM_COPYDATA on background thread, and spiral_mode=="1" preset update!
        self.harness.process_transactions.clear()
        self.harness.tx_event.clear()
        copydata_calls.clear()
        copydata_ev.clear()

        with (
            mock.patch("subprocess.Popen") as mock_popen_sp,
            mock.patch.object(mod, "_find_orca_mainframe_hwnd", return_value=0x002468AC),
            mock.patch.object(mod, "_dispatch_copydata_to_hwnd", side_effect=_spy_dispatch_copydata),
        ):
            plater_msgs = send_and_collect(
                json.dumps(
                    {
                        "type": "send_to_plater",
                        "params": spiral_params,
                        "include_saucer": False,
                    }
                ),
                {"action_result"},
                timeout=8.0,
            )
            plater_res = [m for m in plater_msgs if m.get("type") == "action_result"][0]
            self.assertTrue(plater_res.get("ok"), f"send_to_plater (spiral) failed: {plater_res}")
            self.assertTrue(copydata_ev.wait(timeout=4.0))
            self.assertTrue(self.harness.tx_event.wait(timeout=4.0))
            self.assertEqual(mock_popen_sp.call_count, 0)

        self.assertEqual(len(copydata_calls), 1)
        self.assertFalse(copydata_calls[0]["on_ui_thread"])
        ok_sp, sp_args = _unescape_strings_cstyle_orca(copydata_calls[0]["payload_str"])
        self.assertTrue(ok_sp)
        self.assertEqual(sp_args[0], "orca-slicer.exe")
        self.assertEqual(Path(sp_args[1]).resolve(), Path(plater_res["paths"][0]).resolve())

        merged_tx: dict[str, str] = {}
        for tx in self.harness.process_transactions:
            self.assertFalse(
                tx["on_ui_thread"],
                "CRITICAL DEADLOCK BUG: preset.process update called synchronously on UI thread!",
            )
            merged_tx.update(tx["updates"])

        self.assertEqual(merged_tx.get("spiral_mode"), "1")
        self.assertEqual(merged_tx.get("wall_loops"), "1")
        self.assertEqual(merged_tx.get("top_shell_layers"), "0")
        self.assertEqual(merged_tx.get("sparse_infill_density"), "0%")
        self.assertEqual(merged_tx.get("bottom_shell_layers"), "5")

        # 8. `send_to_plater` with `include_saucer=True` in spiral_vase mode ->
        #    MUST generate an open-mouthed hollow vase STL, send BOTH paths via WM_COPYDATA,
        #    call ZERO subprocess.Popen, and set spiral_mode == "0"!
        self.harness.process_transactions.clear()
        self.harness.tx_event.clear()
        copydata_calls.clear()
        copydata_ev.clear()

        with (
            mock.patch("subprocess.Popen") as mock_popen2,
            mock.patch.object(mod, "_find_orca_mainframe_hwnd", return_value=0x002468AC),
            mock.patch.object(mod, "_dispatch_copydata_to_hwnd", side_effect=_spy_dispatch_copydata),
        ):
            saucer_msgs = send_and_collect(
                json.dumps(
                    {
                        "type": "send_to_plater",
                        "params": spiral_params,
                        "include_saucer": True,
                    }
                ),
                {"action_result"},
                timeout=8.0,
            )
            saucer_res = [m for m in saucer_msgs if m.get("type") == "action_result"][0]
            self.assertTrue(saucer_res.get("ok"), f"send_to_plater+saucer failed: {saucer_res}")
            self.assertTrue(copydata_ev.wait(timeout=4.0))
            self.assertTrue(self.harness.tx_event.wait(timeout=4.0))
            self.assertEqual(mock_popen2.call_count, 0)

        self.assertEqual(len(copydata_calls), 1)
        self.assertFalse(copydata_calls[0]["on_ui_thread"])
        self.assertFalse(copydata_calls[0]["payload_str"].endswith(";"))
        ok_sc, sc_args = _unescape_strings_cstyle_orca(copydata_calls[0]["payload_str"])
        self.assertTrue(ok_sc)
        self.assertEqual(len(sc_args), 3)
        self.assertEqual(sc_args[0], "orca-slicer.exe")
        self.assertEqual(Path(sc_args[1]).resolve(), Path(saucer_res["paths"][0]).resolve())
        self.assertEqual(Path(sc_args[2]).resolve(), Path(saucer_res["paths"][1]).resolve())
        self.assertTrue(Path(sc_args[1]).is_file())
        self.assertTrue(Path(sc_args[2]).is_file())

        saucer_vase_stl_stats = _inspect_binary_stl_open_mouth(Path(sc_args[1]), 135.0)
        self.assertEqual(
            saucer_vase_stl_stats["top_center_cap_tris"],
            0,
            "send_to_plater(include_saucer=True, print_mode='spiral_vase') sent a closed-mouth vase STL!",
        )
        self.assertGreater(saucer_vase_stl_stats["inward_cavity_tris"], 0)

        merged_saucer_tx: dict[str, str] = {}
        for tx in self.harness.process_transactions:
            self.assertFalse(tx["on_ui_thread"])
            merged_saucer_tx.update(tx["updates"])
        self.assertEqual(
            merged_saucer_tx.get("spiral_mode"),
            "0",
            "Two objects (vase + saucer) on one plate must set spiral_mode == '0'",
        )

        # 9. `open_exports_folder` (mock os.startfile so Explorer window does not open)
        with mock.patch("os.startfile", create=True):
            page.on_message(json.dumps({"type": "open_exports_folder"}))

    def test_06_dock_panel_bridge_and_isolated_audit_load(self) -> None:
        """Verify Dock capability message roundtrip and standalone load without `src/` on sys.path."""
        self._load_installed_bundle()
        plugin_inst = self.harness.plugin_classes[0]()
        plugin_inst.register_capabilities()

        orca_script_base = self._mock_mods["orca.script"].ScriptPluginCapabilityBase
        dock_cls = [c for c in self.harness.registered_capabilities if issubclass(c, orca_script_base)][0]
        dock_cap = dock_cls()
        dock_cap.on_load()
        res = dock_cap.execute()
        if asyncio.iscoroutine(res):
            asyncio.run(res)

        self.assertEqual(len(self.harness.dock_panels), 1)
        panel = self.harness.dock_panels[0]
        self.assertEqual(panel.dock, "right")
        self.assertTrue(callable(panel.on_message))

        panel.on_message({"type": "ready", "mode": "dock"})
        posted_types = {m.get("type") for m in panel.posted if isinstance(m, dict)}
        self.assertIn("init_state", posted_types)
        self.assertIn("analysis_result", posted_types)

        # Subprocess isolation check: load bundle WITHOUT project `src/` on sys.path
        # and with PEP 578 audit hook blocking `OrcaSlicer.conf`.
        if INSTALLED_PLUGIN_PY.is_file():
            isolated_bundle_py = INSTALLED_PLUGIN_PY
        else:
            isolated_dir = self.tmp_path / "isolated_bundle_only"
            isolated_dir.mkdir(parents=True, exist_ok=True)
            isolated_bundle_py = isolated_dir / "orca_vase_generator.py"
            shutil.copyfile(DIST_BUNDLE, isolated_bundle_py)

        clean_env = dict(os.environ)
        clean_env.pop("PYTHONPATH", None)

        isolated_code = (
            "import os, sys, importlib.util\n"
            f"if os.path.isdir({str(ORCA_SITE_PACKAGES)!r}):\n"
            f"    sys.path.insert(0, {str(ORCA_SITE_PACKAGES)!r})\n"
            "assert all('orca-vase-generator' not in p.lower() for p in sys.path)\n"
            "def _hook(ev, args):\n"
            "    if ev == 'open' and args and 'orcaslicer.conf' in str(args[0]).lower():\n"
            "        raise PermissionError('[AUDIT] Denied filename: OrcaSlicer.conf')\n"
            "sys.addaudithook(_hook)\n"
            f"p = {str(isolated_bundle_py)!r}\n"
            "spec = importlib.util.spec_from_file_location('orca_vase_isolated', p)\n"
            "mod = importlib.util.module_from_spec(spec)\n"
            "sys.modules[spec.name] = mod\n"
            "spec.loader.exec_module(mod)\n"
            "m = mod.generate_vase_mesh(mod.normalize_params({'resolution_angular': 64, 'resolution_vertical': 60}))\n"
            "assert m.volume_cm3 > 0\n"
            "print('ISOLATED_OK')\n"
        )
        proc = subprocess.run(
            [sys.executable, "-B", "-c", isolated_code],
            cwd=str(self.tmp_path),
            env=clean_env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=20,
        )
        self.assertEqual(proc.returncode, 0, f"Isolated bundle load failed:\n{proc.stderr}")
        self.assertIn("ISOLATED_OK", proc.stdout)

    def test_07_wm_copydata_binary_struct_and_unescape_cstyle(self) -> None:
        """Directly verify C-escaped formatter, unescape_strings_cstyle edge cases, and Win64 COPYDATASTRUCT memory."""
        mod = self._load_installed_bundle()

        # 1. Verify our faithful OrcaSlicer `unescape_strings_cstyle` parser catches invalid formats
        ok_trail, _ = _unescape_strings_cstyle_orca('"orca-slicer.exe";"C:\\\\test.stl";')
        self.assertFalse(ok_trail, "Trailing ';' must be rejected by unescape_strings_cstyle")
        ok_unq, _ = _unescape_strings_cstyle_orca('orca-slicer.exe;"C:\\\\test.stl"')
        self.assertFalse(ok_unq, "Unquoted token must be rejected by unescape_strings_cstyle")
        ok_raw_bs, bad_args = _unescape_strings_cstyle_orca('"orca-slicer.exe";"C:\\Users\\vaso.stl"')
        self.assertTrue(ok_raw_bs)
        self.assertNotEqual(bad_args[1], r"C:\Users\vaso.stl", "Single unescaped backslashes corrupt paths")

        # 2. Verify `_format_other_instance_payload` roundtrips tricky paths cleanly
        #    (including spaces, semicolons ';', parens, and PT-BR diacritics)
        f1 = self.tmp_path / "Vaso (Ondas); Ção 01.stl"
        f2 = self.tmp_path / "Prato Coletor 01.stl"
        f1.write_bytes(b"stl1")
        f2.write_bytes(b"stl2")

        formatted = mod._format_other_instance_payload([f1, f2])
        self.assertFalse(formatted.endswith(";"))
        ok_fmt, out_tokens = _unescape_strings_cstyle_orca(formatted)
        self.assertTrue(ok_fmt, f"_format_other_instance_payload produced invalid C-escaped string: {formatted!r}")
        self.assertEqual(
            out_tokens,
            ["orca-slicer.exe", str(f1.resolve()), str(f2.resolve())],
        )

        # 3. Verify `_find_orca_mainframe_hwnd` returns None cleanly for non-existent PID
        self.assertIsNone(mod._find_orca_mainframe_hwnd(target_pid=999_999_999))

        # 4. Verify `_dispatch_copydata_to_hwnd` constructs exact COPYDATASTRUCT (dwData=1, WCHAR + NUL)
        class _QaCopyDataStruct(ctypes.Structure):
            _fields_ = [
                ("dwData", ctypes.c_size_t),
                ("cbData", ctypes.c_uint32),
                ("lpData", ctypes.c_void_p),
            ]

        captured_msgs: list[dict] = []

        def _fake_send_msg_timeout(
            hwnd: object,
            msg: int,
            wparam: int,
            lparam: object,
            flags: int,
            timeout_ms: int,
            lpdw_res: object = None,
        ) -> int:
            if hasattr(lparam, "_obj"):
                addr = ctypes.addressof(lparam._obj)
            elif isinstance(lparam, int):
                addr = lparam
            else:
                addr = int(ctypes.cast(lparam, ctypes.c_void_p).value or 0)
            cds = _QaCopyDataStruct.from_address(addr)
            raw_bytes = ctypes.string_at(cds.lpData, cds.cbData)
            hwnd_val = hwnd.value if hasattr(hwnd, "value") else int(hwnd)
            captured_msgs.append(
                {
                    "hwnd": hwnd_val,
                    "msg": int(msg),
                    "dwData": int(cds.dwData),
                    "cbData": int(cds.cbData),
                    "raw_bytes": raw_bytes,
                    "timeout_ms": int(timeout_ms),
                }
            )
            if lpdw_res is not None:
                if hasattr(lpdw_res, "_obj"):
                    lpdw_res._obj.value = 1
                elif hasattr(lpdw_res, "contents"):
                    lpdw_res.contents.value = 1
            return 1

        mock_send_msg = mock.MagicMock(side_effect=_fake_send_msg_timeout)
        fake_windll = types.SimpleNamespace(
            user32=types.SimpleNamespace(SendMessageTimeoutW=mock_send_msg),
            kernel32=types.SimpleNamespace(GetLastError=lambda: 0),
        )
        with (
            mock.patch.object(sys, "platform", "win32"),
            mock.patch.object(ctypes, "windll", fake_windll, create=True),
        ):
            ok_disp, _ = mod._dispatch_copydata_to_hwnd(0x00ABCDEF, formatted, timeout_ms=3500)

        wchar_sz = ctypes.sizeof(ctypes.c_wchar)
        wchar_enc = "utf-16-le" if wchar_sz == 2 else "utf-32-le"
        self.assertTrue(ok_disp)
        self.assertEqual(len(captured_msgs), 1)
        cap = captured_msgs[0]
        self.assertEqual(cap["hwnd"], 0x00ABCDEF)
        self.assertEqual(cap["msg"], 0x004A)  # WM_COPYDATA
        self.assertEqual(cap["dwData"], 1)    # MainFrame::MSWWindowProc requires dwData == 1
        self.assertEqual(cap["cbData"], (len(formatted) + 1) * wchar_sz)
        self.assertEqual(cap["raw_bytes"][-wchar_sz:], b"\x00" * wchar_sz)
        decoded_wstr = cap["raw_bytes"][:-wchar_sz].decode(wchar_enc)
        self.assertEqual(decoded_wstr, formatted)

    def test_08_live_printer_sync_line_width_pct_circular_beds_and_zero_sovol(self) -> None:
        """Verify v1.3.3 community readiness: zero 'Sovol' strings, %/0 line-width parsing,
        circular/large/small printable_area sync, C++ PresetCollection.edited_preset properties,
        sync_printer -> printer_updated + analysis_result, on_lifecycle_event, and JS dynamic slider max.
        """
        # 1. Zero hardcoded "Sovol" or "SV06" strings in src/, dist/, scripts/, or installed bundle
        repo_root = REPO_ROOT
        scan_targets = [
            *sorted((repo_root / "src").rglob("*.py")),
            DIST_BUNDLE,
            DIST_ANY_BUNDLE,
            repo_root / "scripts" / "build_and_install.py",
        ]
        if INSTALLED_PLUGIN_PY.is_file():
            scan_targets.append(INSTALLED_PLUGIN_PY)
        for path in scan_targets:
            txt = path.read_text(encoding="utf-8")
            self.assertIsNone(
                re.search(r"sovol|sv06", txt, flags=re.IGNORECASE),
                f"Forbidden hardcoded 'Sovol'/'SV06' string found in {path}!",
            )

        mod = self._load_installed_bundle()
        plugin_inst = self.harness.plugin_classes[0]()
        plugin_inst.register_capabilities()

        # 2. Direct unit verification of _parse_line_width (% strings, "0", fallback_raw, arrays)
        self.assertAlmostEqual(mod._parse_line_width("105%", 0.4), 0.42, places=3)
        self.assertAlmostEqual(mod._parse_line_width("110%", 0.4), 0.44, places=3)
        self.assertAlmostEqual(mod._parse_line_width(["120%"], 0.6), 0.72, places=3)
        self.assertAlmostEqual(mod._parse_line_width("0", 0.4), 0.42, places=3)
        self.assertAlmostEqual(mod._parse_line_width("0", 0.6), 0.63, places=3)
        self.assertAlmostEqual(mod._parse_line_width("0%", 0.8), 0.84, places=3)
        self.assertAlmostEqual(mod._parse_line_width("0", 0.4, fallback_raw="115%"), 0.46, places=3)
        self.assertAlmostEqual(mod._parse_line_width("0.48", 0.4), 0.48, places=3)

        # 3. Direct unit verification of _parse_bed_geometry (rectangular, circular >6 verts, Point objects)
        rect_420 = mod._parse_bed_geometry(["0x0", "420x0", "420x420", "0x420"])
        self.assertEqual(rect_420["bed_x"], 420.0)
        self.assertEqual(rect_420["bed_y"], 420.0)
        self.assertEqual(rect_420["bed_shape"], "rectangular")

        rect_180 = mod._parse_bed_geometry("0x0,180x0,180x180,0x180")
        self.assertEqual(rect_180["bed_x"], 180.0)
        self.assertEqual(rect_180["bed_y"], 180.0)
        self.assertEqual(rect_180["bed_shape"], "rectangular")

        # 35-gon (odd vertex count!) circular delta bed of Ø300mm centered at (0, 0)
        delta_pts = [
            f"{150.0 * math.cos(2.0 * math.pi * k / 35):.4f}x{150.0 * math.sin(2.0 * math.pi * k / 35):.4f}"
            for k in range(35)
        ]
        circ_300 = mod._parse_bed_geometry(delta_pts)
        self.assertEqual(circ_300["bed_shape"], "circular")
        self.assertAlmostEqual(circ_300["bed_x"], 300.0, places=2)
        self.assertAlmostEqual(circ_300["bed_y"], 300.0, places=2)
        self.assertAlmostEqual(circ_300["bed_center"][0], 0.0, places=1)
        self.assertAlmostEqual(circ_300["bed_center"][1], 0.0, places=1)

        # Pointf-like objects exposing .x and .y properties (matching orca.host.Point in OrcaSlicer.dll)
        pt_cls = lambda x, y: types.SimpleNamespace(x=x, y=y)
        pt_geom = mod._parse_bed_geometry([pt_cls(0, 0), pt_cls(350, 0), pt_cls(350, 350), pt_cls(0, 350)])
        self.assertEqual(pt_geom["bed_x"], 350.0)
        self.assertEqual(pt_geom["bed_y"], 350.0)
        self.assertEqual(pt_geom["bed_shape"], "rectangular")

        # 4. Live bridge `sync_printer` -> `printer_updated` + `analysis_result` & `on_lifecycle_event`
        orca_pages_base = self._mock_mods["orca.pages"].PagesPluginCapabilityBase
        page_cls = [c for c in self.harness.registered_capabilities if issubclass(c, orca_pages_base)][0]
        page = page_cls()
        page.on_load()

        # Switch mock host to Large-Format Elegoo Neptune 4 Max (420x420x480, 0.6 nozzle, "110%" line width)
        self.harness.preset_values.update(
            {
                "printer_settings_id": "Elegoo Neptune 4 Max 0.6 nozzle",
                "print_settings_id": "0.28mm Draft @Neptune4Max",
                "printable_area": ["0x0", "420x0", "420x420", "0x420"],
                "printable_height": "480",
                "nozzle_diameter": ["0.6"],
                "layer_height": "0.28",
                "outer_wall_line_width": "110%",
            }
        )
        tall_vase = normalize_params(
            {
                "name": "Tall Amphora 440",
                "height_mm": 440.0,
                "base_diameter_mm": 210.0,
                "belly_diameter_mm": 340.0,
                "waist_diameter_mm": 240.0,
                "neck_diameter_mm": 260.0,
                "resolution_angular": 64,
                "resolution_vertical": 60,
            }
        )
        idx0 = len(self.harness.posted_page_messages)
        page.on_message(json.dumps({"type": "sync_printer", "params": tall_vase}))
        batch_420 = self.harness.posted_page_messages[idx0:]
        upd_420 = [m for m in batch_420 if m.get("type") == "printer_updated"][0]
        an_420 = [m for m in batch_420 if m.get("type") == "analysis_result"][0]
        self.assertEqual(upd_420["printer"]["name"], "Elegoo Neptune 4 Max 0.6 nozzle")
        self.assertEqual(upd_420["printer"]["bed_x"], 420.0)
        self.assertEqual(upd_420["printer"]["bed_y"], 420.0)
        self.assertEqual(upd_420["printer"]["max_z"], 480.0)
        self.assertAlmostEqual(upd_420["printer"]["nozzle_mm"], 0.6, places=3)
        self.assertAlmostEqual(upd_420["printer"]["line_width_mm"], 0.66, places=3)
        self.assertTrue(an_420["report"]["fits_bed"])
        self.assertTrue(an_420["report"]["fits_height"])

        # Switch mock host to Small Prusa MINI+ (180x180x180, 0.4 nozzle, "0" outer_wall_line_width -> 0.42mm)
        # AND trigger via C++ `on_lifecycle_event(LifecycleEvent.PresetSelected)`!
        self.harness.preset_values.update(
            {
                "printer_settings_id": "Original Prusa MINI+ Input Shaper 0.4 nozzle",
                "print_settings_id": "0.20mm SPEED @MINI",
                "printable_area": ["0x0", "180x0", "180x180", "0x180"],
                "printable_height": "180",
                "nozzle_diameter": ["0.4"],
                "layer_height": "0.20",
                "outer_wall_line_width": "0",
            }
        )
        idx1 = len(self.harness.posted_page_messages)
        lifecycle_ev = self._mock_mods["orca"].LifecycleEvent.PresetSelected
        page.on_lifecycle_event(lifecycle_ev, None)
        batch_180 = self.harness.posted_page_messages[idx1:]
        upd_180 = [m for m in batch_180 if m.get("type") == "printer_updated"][0]
        an_180 = [m for m in batch_180 if m.get("type") == "analysis_result"][0]
        self.assertEqual(upd_180["printer"]["name"], "Original Prusa MINI+ Input Shaper 0.4 nozzle")
        self.assertEqual(upd_180["printer"]["bed_x"], 180.0)
        self.assertEqual(upd_180["printer"]["max_z"], 180.0)
        self.assertAlmostEqual(upd_180["printer"]["line_width_mm"], 0.42, places=3)
        # Tall 440x340mm vase exceeds 180x180x180 MINI+ volume!
        self.assertFalse(an_180["report"]["fits_bed"])
        self.assertFalse(an_180["report"]["fits_height"])

        # Verify pybind11 property-style `PresetBundle.printers.edited_preset` (non-callable properties!)
        delta_36 = [
            [round(150.0 * math.cos(2.0 * math.pi * k / 36), 3), round(150.0 * math.sin(2.0 * math.pi * k / 36), 3)]
            for k in range(36)
        ]
        prop_printer_preset = types.SimpleNamespace(
            name="FLSun V400 0.4 nozzle",
            config_value=lambda key: {
                "printable_area": delta_36,
                "printable_height": 410.0,
                "nozzle_diameter": [0.4],
            }.get(key),
        )
        prop_process_preset = types.SimpleNamespace(
            name="0.20mm High-Speed @FLSun",
            config_value=lambda key: {
                "layer_height": 0.20,
                "outer_wall_line_width": "105%",
            }.get(key),
        )
        prop_bundle = types.SimpleNamespace(
            printers=types.SimpleNamespace(edited_preset=prop_printer_preset),
            prints=types.SimpleNamespace(edited_preset=prop_process_preset),
            current_printer_preset=prop_printer_preset,
            current_process_preset=prop_process_preset,
            current_filament_preset_names=["FLSun High-Speed PLA"],
            full_config_value=lambda key: None,
        )
        with mock.patch.object(self._mock_mods["orca.host"], "preset_bundle", return_value=prop_bundle):
            idx2 = len(self.harness.posted_page_messages)
            page.on_message({"type": "sync_printer"})
            upd_delta = [m for m in self.harness.posted_page_messages[idx2:] if m.get("type") == "printer_updated"][0]
            self.assertEqual(upd_delta["printer"]["name"], "FLSun V400 0.4 nozzle")
            self.assertEqual(upd_delta["printer"]["bed_shape"], "circular")
            self.assertEqual(upd_delta["printer"]["bed_x"], 300.0)
            self.assertEqual(upd_delta["printer"]["bed_y"], 300.0)
            self.assertEqual(upd_delta["printer"]["max_z"], 410.0)
            self.assertAlmostEqual(upd_delta["printer"]["line_width_mm"], 0.42, places=3)

        # 5. Headless Node.js check of Studio UI:
        #    - Non-clipping #printer-pill CSS (.printer-pill-specs has flex-shrink: 0; .printer-pill-name has ellipsis)
        #    - Dynamic slider max sync on `printer_updated` (420x420x480 -> height max 480, diam max 416; 180x180x180 -> height max 180, diam max 176)
        #    - Automatic `sync_printer` postMessage on `visibilitychange`, `focus`, and `#printer-pill` click
        #    - 1-click `fitParamsToActivePrinter()` clamping tall/wide vase into 180x180x180 build volume
        html_ui = page.get_ui()
        self.assertIn('id="printer-pill-name"', html_ui)
        self.assertIn('id="printer-pill-specs"', html_ui)
        self.assertIn('id="printer-pill-sync"', html_ui)
        self.assertRegex(html_ui, r"\.printer-pill-specs\s*\{[^}]*flex-shrink:\s*0")
        self.assertRegex(html_ui, r"\.printer-pill-name\s*\{[^}]*text-overflow:\s*ellipsis")

        main_js = max(_extract_script_blocks(html_ui), key=len)
        ui_js_path = self.tmp_path / "studio_ui_printer_sync.js"
        ui_js_path.write_text(main_js, encoding="utf-8")

        node_sync_script = r"""
const fs = require('fs');
const noop = () => {};
const posted = [];
const docListeners = {};
const winListeners = {};
const elCache = {};

const makeGlStub = () => new Proxy({
  ARRAY_BUFFER: 0x8892, ELEMENT_ARRAY_BUFFER: 0x8893, STATIC_DRAW: 0x88E4, DYNAMIC_DRAW: 0x88E8,
  TRIANGLES: 4, LINES: 1, FLOAT: 0x1406, UNSIGNED_INT: 0x1405, UNSIGNED_SHORT: 0x1403,
  VERTEX_SHADER: 0x8B31, FRAGMENT_SHADER: 0x8B30, COMPILE_STATUS: 0x8B81, LINK_STATUS: 0x8B82,
  DEPTH_TEST: 0x0B71, CULL_FACE: 0x0B44, FRONT: 0x0404, BACK: 0x0405, BLEND: 0x0BE2,
  SRC_ALPHA: 0x0302, ONE_MINUS_SRC_ALPHA: 0x0303, COLOR_BUFFER_BIT: 0x4000, DEPTH_BUFFER_BIT: 0x0100,
  createShader: () => ({}), getShaderParameter: () => true, getShaderInfoLog: () => '',
  createProgram: () => ({}), getProgramParameter: () => true, getProgramInfoLog: () => '',
  createBuffer: () => ({}), getUniformLocation: () => ({}), getAttribLocation: () => 0,
  getExtension: () => ({}),
  canvas: { width: 800, height: 600, clientWidth: 800, clientHeight: 600 }
}, { get(t, p) { return p in t ? t[p] : noop; } });

const make2dStub = () => new Proxy({
  canvas: { width: 300, height: 220, clientWidth: 300, clientHeight: 220 },
  measureText: () => ({ width: 24 })
}, { get(t, p) { return p in t ? t[p] : noop; } });

const makeEl = (tag = 'div', id = '') => {
  const listeners = {};
  let inner = '';
  const el = {
    id, tagName: String(tag).toUpperCase(), style: {}, dataset: {},
    classList: { add: noop, remove: noop, toggle: noop, contains: () => false },
    children: [], value: '0', min: '0', max: '100', step: '1', checked: false, disabled: false,
    textContent: '', title: '', clientWidth: 800, clientHeight: 600, width: 800, height: 600,
    get innerHTML() { return inner; },
    set innerHTML(v) {
      inner = String(v);
      this._rangeChild = makeEl('input');
      this._numChild = makeEl('input');
      this._lblChild = makeEl('span');
    },
    addEventListener(ev, fn) { (listeners[ev] = listeners[ev] || []).push(fn); },
    dispatch(ev, arg = {}) { (listeners[ev] || []).forEach(fn => fn(arg)); },
    querySelector(sel) {
      if (sel.includes('range')) return this._rangeChild || (this._rangeChild = makeEl('input'));
      if (sel.includes('number')) return this._numChild || (this._numChild = makeEl('input'));
      if (sel.includes('data-spec-label')) return this._lblChild || (this._lblChild = makeEl('span'));
      return makeEl('div');
    },
    querySelectorAll: () => [],
    appendChild(c) { this.children.push(c); return c; },
    setAttribute: noop, getAttribute: () => null,
    getBoundingClientRect: () => ({ left: 0, top: 0, width: 300, height: 220 }),
    getContext: (k) => String(k).includes('webgl') ? makeGlStub() : make2dStub()
  };
  return el;
};

const sliderHosts = {};
globalThis.window = globalThis;
globalThis.addEventListener = (ev, fn) => { (winListeners[ev] = winListeners[ev] || []).push(fn); };
globalThis.devicePixelRatio = 1;
globalThis.requestAnimationFrame = () => 1;
globalThis.cancelAnimationFrame = noop;
globalThis.ResizeObserver = class { constructor(cb) { this.cb = cb; } observe() {} disconnect() {} };
globalThis.document = {
  visibilityState: 'visible',
  documentElement: makeEl('html'),
  body: makeEl('body'),
  getElementById(id) { return elCache[id] || (elCache[id] = makeEl('div', id)); },
  querySelector(sel) {
    const m = sel.match(/\[data-slider="([^"]+)"\]/);
    if (m) return sliderHosts[m[1]] || (sliderHosts[m[1]] = makeEl('div', m[1]));
    if (sel === '.studio-shell') return elCache['__shell'] || (elCache['__shell'] = makeEl('div', '__shell'));
    return makeEl('div');
  },
  querySelectorAll: () => [],
  createElement: (t) => makeEl(t),
  addEventListener(ev, fn) { (docListeners[ev] = docListeners[ev] || []).push(fn); }
};
globalThis.orca = {
  postMessage(msg) { posted.push(msg); },
  onMessage(cb) { globalThis.__onHostMsg = cb; }
};

eval(fs.readFileSync(process.argv[2], 'utf8'));
const api = globalThis.VaseStudioMath;

// 1) Simulate incoming 420x420x480 printer_updated
api.handleHostMessage({
  type: 'printer_updated',
  printer: { name: 'Elegoo Neptune 4 Max 0.6', bed_x: 420, bed_y: 420, bed_shape: 'rectangular', max_z: 480, nozzle_mm: 0.6, layer_height_mm: 0.28, line_width_mm: 0.66 }
});
const max420H = Number(api.sliderRefs['height_mm'].rangeEl.max);
const max420D = Number(api.sliderRefs['belly_diameter_mm'].rangeEl.max);

// Set a tall 450mm x 360mm vase on the 420x420x480 printer
api.state.params = api.normalizeParams({ height_mm: 450, belly_diameter_mm: 360, base_diameter_mm: 220, waist_diameter_mm: 260, neck_diameter_mm: 280 });
api.buildFullStudioGeometry(api.state.params, true);
const fits420 = api.state.clientMetrics.fitsBed && api.state.clientMetrics.fitsHeight;

// 2) Switch to small 180x180x180 printer -> slider max updates to 180 / 176, vase flagged out-of-bounds, then fitParamsToActivePrinter clamps cleanly!
api.handleHostMessage({
  type: 'printer_updated',
  printer: { name: 'Prusa MINI+ 0.4', bed_x: 180, bed_y: 180, bed_shape: 'rectangular', max_z: 180, nozzle_mm: 0.4, layer_height_mm: 0.2, line_width_mm: 0.42 }
});
const max180H = Number(api.sliderRefs['height_mm'].rangeEl.max);
const max180D = Number(api.sliderRefs['belly_diameter_mm'].rangeEl.max);
const fits180Before = api.state.clientMetrics.fitsBed && api.state.clientMetrics.fitsHeight;

api.fitParamsToActivePrinter();
const fits180After = api.state.clientMetrics.fitsBed && api.state.clientMetrics.fitsHeight;

// 3) Trigger pill click & focus/visibilitychange -> verify `sync_printer` messages emitted
const beforeSyncCount = posted.filter(m => m.type === 'sync_printer').length;
elCache['printer-pill'].dispatch('click');
const afterClickSyncCount = posted.filter(m => m.type === 'sync_printer').length;

console.log(JSON.stringify({
  max420H, max420D, fits420,
  max180H, max180D, fits180Before, fits180After,
  fittedHeight: api.state.params.height_mm,
  pillName: elCache['printer-pill-name'].textContent,
  pillSpecs: elCache['printer-pill-specs'].textContent,
  syncTriggeredByClick: afterClickSyncCount > beforeSyncCount
}));
"""
        runner_js = self.tmp_path / "run_printer_sync_check.js"
        runner_js.write_text(node_sync_script, encoding="utf-8")
        node_bin = shutil.which("node")
        if node_bin:
            proc = subprocess.run(
                [node_bin, str(runner_js), str(ui_js_path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=15,
            )
            self.assertEqual(proc.returncode, 0, f"Node printer sync runner failed:\n{proc.stderr}")
            js_res = json.loads(proc.stdout.strip().splitlines()[-1])
            self.assertEqual(js_res["max420H"], 480)
            self.assertEqual(js_res["max420D"], 416)
            self.assertTrue(js_res["fits420"])
            self.assertEqual(js_res["max180H"], 180)
            self.assertEqual(js_res["max180D"], 176)
            self.assertFalse(js_res["fits180Before"])
            self.assertTrue(js_res["fits180After"])
            self.assertLessEqual(js_res["fittedHeight"], 180)
            self.assertEqual(js_res["pillName"], "Prusa MINI+ 0.4")
            self.assertIn("180×180×180 mm", js_res["pillSpecs"])
            self.assertIn("0.4mm", js_res["pillSpecs"])
            self.assertTrue(js_res["syncTriggeredByClick"])

    def test_09_official_wiki_compliance_matrix_checks(self) -> None:
        """Audit strict compliance with the official OrcaSlicer Plugin Development Wiki:
        - Zero hardcoded user/machine paths anywhere in src/, dist/, scripts/, or tests/
        - Cross-platform data_dir() resolution (win32, darwin, linux + XDG_CONFIG_HOME)
        - Non-Win32 (darwin/linux) graceful fallbacks without ctypes.windll crashes
        - Callback-only orca.host.plugin.storage() rule during register_capabilities()
        - Official orca.host.ui.push_notification(NotificationLevel, text) signature
        - Official orca.host.app_language() fallback
        - PythonPluginBase capability configuration (get_default_config / get_config / save_config / on_unload)
        - PEP 427 .whl community distribution wheel validation & @orca.plugin capture
        - Automatic --orca-bg CSS variable theme detection in WebView2 / WebKit
        """
        # 1. Zero hardcoded developer username anywhere in src/, dist/, scripts/, tests/, pyproject.toml
        forbidden_user = "victor" + "f"
        check_files = [
            PYPROJECT_TOML,
            DIST_BUNDLE,
            DIST_ANY_BUNDLE,
            *sorted((REPO_ROOT / "src").rglob("*.py")),
            *sorted((REPO_ROOT / "scripts").rglob("*.py")),
            *sorted((REPO_ROOT / "tests").rglob("*.py")),
        ]
        if INSTALLED_PLUGIN_PY.is_file():
            check_files.append(INSTALLED_PLUGIN_PY)
        for fpath in check_files:
            content = fpath.read_text(encoding="utf-8")
            # Public author attribution is allowed; actual private home paths are not.
            normalized = content.lower().replace("\\", "/")
            self.assertNotRegex(
                normalized,
                r"[a-z]:/+users/+" + forbidden_user + r"(?:/|$)",
                f"Forbidden hardcoded user path found in {fpath}!",
            )

        mod = self._load_installed_bundle()

        # 2. Verify register_capabilities() does NOT call orca.host.plugin.storage() outside callbacks
        def _forbid_storage_during_discovery() -> str:
            raise AssertionError("plugin.storage() must NOT be called inside register_capabilities()!")

        with mock.patch.object(self._mock_mods["orca.plugin"], "storage", side_effect=_forbid_storage_during_discovery):
            plugin_inst = self.harness.plugin_classes[0]()
            plugin_inst.register_capabilities()

        # 3. Cross-platform _orca_data_dir() & non-Win32 safety (macOS darwin + Linux)
        with (
            mock.patch.dict(mod.__dict__, {"__file__": str(DIST_BUNDLE)}),
            mock.patch.object(sys, "platform", "darwin"),
            mock.patch.dict(os.environ, {"APPDATA": ""}, clear=False),
        ):
            mac_dir = mod._orca_data_dir()
            self.assertEqual(
                mac_dir.parts[-3:],
                ("Library", "Application Support", "OrcaSlicer"),
                f"Expected macOS Application Support/OrcaSlicer path, got {mac_dir}",
            )
            self.assertIsNone(mod._find_orca_mainframe_hwnd())
            ok_mac, msg_mac = mod._dispatch_copydata_to_hwnd(12345, '"orca-slicer.exe";"test.stl"')
            self.assertFalse(ok_mac)
            self.assertIn("win32", msg_mac.lower())

        custom_xdg = str(self.tmp_path / "xdg_cfg")
        with (
            mock.patch.dict(mod.__dict__, {"__file__": str(DIST_BUNDLE)}),
            mock.patch.object(sys, "platform", "linux"),
            mock.patch.dict(os.environ, {"APPDATA": "", "XDG_CONFIG_HOME": custom_xdg}, clear=False),
        ):
            lin_xdg = mod._orca_data_dir()
            self.assertEqual(lin_xdg, Path(custom_xdg) / "OrcaSlicer")

        with (
            mock.patch.dict(mod.__dict__, {"__file__": str(DIST_BUNDLE)}),
            mock.patch.object(sys, "platform", "linux"),
            mock.patch.dict(os.environ, {"APPDATA": "", "XDG_CONFIG_HOME": ""}, clear=False),
        ):
            lin_def = mod._orca_data_dir()
            self.assertEqual(lin_def.parts[-2:], (".config", "OrcaSlicer"))

        # 4. Official `orca.host.app_language()` fallback when `app_info()` omits `"language"`
        with (
            mock.patch.object(self._mock_mods["orca.host"], "app_info", return_value={"version": "2.5.1"}),
            mock.patch.object(self._mock_mods["orca.host"], "app_language", return_value="en_US"),
        ):
            ctx_en = mod._SHARED_CONTROLLER.read_host_context()
            self.assertEqual(ctx_en["lang"], mod.normalize_language("en_US"))
            self.assertFalse(ctx_en["theme_explicit"])

        # 5. Official `orca.host.ui.push_notification(NotificationLevel, text)` 2-arg signature
        self.harness.notifications.clear()
        mod._SHARED_CONTROLLER._notify_host_toast("Teste de notificacao oficial")
        self.assertEqual(len(self.harness.notifications), 1)
        notif_lvl, notif_txt, _, _ = self.harness.notifications[0]
        self.assertEqual(
            notif_lvl,
            self._mock_mods["orca.host.ui"].NotificationLevel.RegularNotificationLevel,
        )
        self.assertEqual(notif_txt, "Teste de notificacao oficial")

        # 6. Capability configuration (`get_default_config`, `save_config`, `get_config`, `on_unload`)
        page_cap = mod.VaseStudioPageCapability()
        dock_cap = mod.VaseStudioDockCapability()
        page_def = page_cap.get_default_config()
        dock_def = dock_cap.get_default_config()
        self.assertIsInstance(page_def, dict)
        self.assertIsInstance(dock_def, dict)
        self.assertEqual(dock_def.get("dock"), "right")

        self.assertTrue(
            dock_cap.save_config(json.dumps({"dock": "left", "width": 460, "height": 820}))
        )
        self.harness.dock_panels.clear()
        dock_cap.on_unload()
        exec_res = dock_cap.execute()
        self.assertEqual(
            exec_res.status,
            self._mock_mods["orca"].PluginResult.Success,
        )
        self.assertEqual(len(self.harness.dock_panels), 1)
        created_panel = self.harness.dock_panels[0]
        self.assertEqual(created_panel.dock, "left")
        self.assertEqual(created_panel.width, 460)
        self.assertEqual(created_panel.height, 820)
        dock_cap.on_unload()
        self.assertIsNone(mod.VaseStudioDockCapability._active_panel)

        # 7. Verify community `.whl` in `dist/` passes OrcaSlicer C++ wheel rules + RECORD SHA-256
        self.assertTrue(DIST_WHEEL.is_file(), f"Expected community wheel at {DIST_WHEEL}")
        with zipfile.ZipFile(DIST_WHEEL, "r") as zf:
            members = set(zf.namelist())
            dist_infos = {m.split("/", 1)[0] for m in members if ".dist-info/" in m}
            self.assertEqual(len(dist_infos), 1)
            di = next(iter(dist_infos))
            meta_txt = zf.read(f"{di}/METADATA").decode("utf-8")
            wheel_txt = zf.read(f"{di}/WHEEL").decode("utf-8")
            top_txt = zf.read(f"{di}/top_level.txt").decode("utf-8").strip()
            rec_txt = zf.read(f"{di}/RECORD").decode("utf-8")

            self.assertIn("Name: Orca Vase Studio", meta_txt)
            self.assertIn("Version: 1.3.3", meta_txt)
            self.assertIn("Author: Orca Vase Studio", meta_txt)
            self.assertIn("Requires-Dist: numpy>=1.26", meta_txt)
            self.assertIn("Import-Name: vase_studio", meta_txt)
            self.assertIn("Wheel-Version: 1.0", wheel_txt)
            self.assertIn("Tag: py3-none-any", wheel_txt)
            self.assertEqual(top_txt, "vase_studio")
            self.assertIn("vase_studio/icon.svg", members)

            rows = list(csv.reader(rec_txt.splitlines()))
            self.assertGreaterEqual(len(rows), 8)
            for arc_name, hash_spec, size_spec in rows:
                if arc_name == f"{di}/RECORD":
                    self.assertEqual(hash_spec, "")
                    continue
                payload = zf.read(arc_name)
                self.assertEqual(len(payload), int(size_spec))
                expected_b64 = base64.urlsafe_b64encode(hashlib.sha256(payload).digest()).rstrip(b"=").decode("ascii")
                self.assertEqual(hash_spec, f"sha256={expected_b64}")

        # 8. Verify WebView `--orca-bg` injected theme auto-detection via Node
        html_ui = page_cap.get_ui()
        self.assertIn("var(--orca-font", html_ui)
        main_js = max(_extract_script_blocks(html_ui), key=len)
        ui_js_path = self.tmp_path / "studio_ui_theme_audit.js"
        ui_js_path.write_text(main_js, encoding="utf-8")
        theme_probe_js = r"""
const fs = require('fs');
const noop = () => {};
let currentOrcaBg = '#f7f9fc';
const makeGlStub = () => new Proxy({ canvas: { width: 800, height: 600, clientWidth: 800, clientHeight: 600 }, createShader: () => ({}), getShaderParameter: () => true, createProgram: () => ({}), getProgramParameter: () => true, createBuffer: () => ({}), getUniformLocation: () => ({}), getAttribLocation: () => 0 }, { get(t, p) { return p in t ? t[p] : noop; } });
const make2dStub = () => new Proxy({ canvas: { width: 300, height: 220 }, measureText: () => ({ width: 20 }) }, { get(t, p) { return p in t ? t[p] : noop; } });
const makeEl = (tag = 'div') => ({ tagName: tag.toUpperCase(), style: {}, dataset: {}, classList: { add: noop, remove: noop, toggle: noop, contains: () => false }, children: [], value: '0', min: '0', max: '100', step: '1', addEventListener: noop, querySelector: () => makeEl('input'), querySelectorAll: () => [], appendChild(c) { return c; }, setAttribute(k, v) { this[k] = v; }, getAttribute(k) { return this[k] || null; }, getBoundingClientRect: () => ({ left: 0, top: 0, width: 300, height: 220 }), getContext: (k) => String(k).includes('webgl') ? makeGlStub() : make2dStub() });
globalThis.window = globalThis;
globalThis.addEventListener = noop;
globalThis.getComputedStyle = () => ({ getPropertyValue: (prop) => prop === '--orca-bg' ? currentOrcaBg : '' });
globalThis.requestAnimationFrame = () => 1;
globalThis.cancelAnimationFrame = noop;
globalThis.ResizeObserver = class { observe() {} disconnect() {} };
globalThis.document = { visibilityState: 'visible', documentElement: makeEl('html'), body: makeEl('body'), getElementById: () => makeEl('div'), querySelector: () => makeEl('div'), querySelectorAll: () => [], createElement: () => makeEl('div'), addEventListener: noop };
globalThis.orca = { postMessage: noop, onMessage: noop };
eval(fs.readFileSync(process.argv[2], 'utf8'));
const api = globalThis.VaseStudioMath;
const bootLight = api.state.theme;
currentOrcaBg = 'rgb(22, 24, 28)';
api.handleHostMessage({ type: 'init_state', lang: 'en', theme: 'light', theme_explicit: false, printer: { name: 'P1S', bed_x: 256, bed_y: 256, max_z: 256, nozzle_mm: 0.4, layer_height_mm: 0.2, line_width_mm: 0.42 } });
const switchedDark = api.state.theme;
console.log(JSON.stringify({ bootLight, switchedDark }));
"""
        probe_runner = self.tmp_path / "run_theme_probe.js"
        probe_runner.write_text(theme_probe_js, encoding="utf-8")
        node_bin = shutil.which("node")
        if node_bin:
            proc = subprocess.run(
                [node_bin, str(probe_runner), str(ui_js_path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=15,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            theme_out = json.loads(proc.stdout.strip().splitlines()[-1])
            self.assertEqual(theme_out["bootLight"], "light")
            self.assertEqual(theme_out["switchedDark"], "dark")

    def test_99_installed_plugin_dir_remains_pristine_after_tests(self) -> None:
        # Always verify `install_plugin()` enforces OrcaSlicer directory invariants in an isolated temp dir
        spec = importlib.util.spec_from_file_location("_qa_vase_build_script", str(BUILD_SCRIPT))
        assert spec is not None and spec.loader is not None
        build_mod = importlib.util.module_from_spec(spec)
        sys.modules["_qa_vase_build_script"] = build_mod
        try:
            spec.loader.exec_module(build_mod)
            temp_install_dir = self.tmp_path / "orca_plugins" / "orca_vase_generator"
            with mock.patch.object(build_mod, "get_install_dir", return_value=temp_install_dir):
                installed_out = build_mod.install_plugin(DIST_BUNDLE)
            self.assertEqual(installed_out, temp_install_dir)
            self._assert_installed_dir_obeys_loader_rules(temp_install_dir)
        finally:
            sys.modules.pop("_qa_vase_build_script", None)

        if INSTALLED_DIR.is_dir():
            self._assert_installed_dir_obeys_loader_rules(INSTALLED_DIR)


if __name__ == "__main__":
    unittest.main(verbosity=2)
