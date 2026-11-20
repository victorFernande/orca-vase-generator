"""Seven offline locales, persistent host preference and lossless packaging contracts."""
from __future__ import annotations

import json
import hashlib
import re
import sys
import tempfile
import struct
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vase_studio.locale_catalog import SUPPORTED_LANGUAGES, locale_vocabulary, normalize_language, translate_text
from vase_studio.studio_ui import get_studio_html
from vase_studio import plugin_main
from vase_studio.presets_catalog import BUILTIN_PRESETS
from vase_studio.mesh_generator import generate_vase_mesh, generate_saucer_mesh


class TestMultilingual(unittest.TestCase):
    def test_all_published_manufacturing_arrays_remain_identical(self):
        reference = json.loads((ROOT / "tests/fixtures/published_1_1_1_mesh_digests.json").read_text(encoding="utf8"))
        by_id = {preset["id"]: preset for preset in BUILTIN_PRESETS}
        for item in reference["presets"]:
            for kind in ("vase", "saucer"):
                if kind not in item:
                    continue
                generator = generate_vase_mesh if kind == "vase" else generate_saucer_mesh
                mesh = generator(by_id[item["id"]]["params"])
                for name, expected in item[kind].items():
                    self.assertEqual(hashlib.sha256(getattr(mesh, name).tobytes()).hexdigest(), expected, (item["id"], kind, name))

    def test_importing_controller_never_requests_callback_only_storage(self):
        with patch.object(plugin_main, "_resolve_storage_dir", side_effect=AssertionError("Storage requested outside callback")):
            controller = plugin_main.VaseStudioController()
            self.assertIsNone(controller._manual_language)

    def test_locale_variants_and_fallback(self):
        for raw, expected in (("it_IT", "it"), ("es-MX", "es"), ("ja_JP.UTF-8", "ja"),
                              ("fr-FR", "fr"), ("de_DE", "de"), ("pt_BR", "pt"),
                              ("en-GB", "en"), ("ru_RU", "en"), (None, "pt")):
            self.assertEqual(normalize_language(raw), expected)
        self.assertEqual(plugin_main._detect_language({"language": "it_IT"}), "it")

    def test_all_existing_ui_sliders_presets_and_placeholders_covered(self):
        source = (ROOT / "src/vase_studio/studio_ui.py").read_text(encoding="utf8")
        start = source.index("    en: {", source.index("const I18N"))
        end = source.index("\n    }\n  };", start)
        labels = [json.loads(value) for value in re.findall(r': ("(?:[^"\\]|\\.)*")', source[start:end])]
        labels += re.findall(r'pt: "[^"\n]*", en: "([^"\n]*)"', source)
        for preset in BUILTIN_PRESETS:
            labels.extend((preset["title_en"], preset["description_en"]))
        for code, vocabulary in locale_vocabulary().items():
            for label in labels:
                self.assertIn(label, vocabulary, (code, label))
                self.assertEqual(sorted(re.findall(r"\{\w+\}", label)),
                                 sorted(re.findall(r"\{\w+\}", vocabulary[label])), (code, label))

    def test_page_dock_html_language_and_independent_selector(self):
        for mode in ("page", "dock"):
            for code in SUPPORTED_LANGUAGES:
                html = get_studio_html(mode, {"lang": code + "_XX"})
                self.assertIn(f'<html lang="{code}"', html)
                self.assertIn('id="lang-select"', html)
                for option in SUPPORTED_LANGUAGES:
                    self.assertIn(f'<option value="{option}">', html)
                self.assertNotIn("__VASE_LOCALE_VOCABULARY__", html)

    def test_saved_preference_wins_host_and_updates_both_live_views(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(plugin_main, "_resolve_storage_dir", return_value=Path(directory)):
            controller = plugin_main.VaseStudioController()
            page, dock = [], []
            # Register both views without asking geometry to run in a language-only test.
            controller._listeners["page"] = page.append
            controller._listeners["dock"] = dock.append
            original = controller.current_params
            controller.handle_message({"type": "set_language", "lang": "ja_JP"}, page.append)
            self.assertEqual(page[-1]["type"], "preferences_updated")
            self.assertEqual(page[-1]["lang"], "ja")
            self.assertEqual(dock[-1], page[-1])
            self.assertEqual(controller.current_params, original)
            self.assertEqual(controller.read_host_context()["lang"], "ja")
            restored = plugin_main.VaseStudioController()
            self.assertEqual(restored.read_host_context()["lang"], "ja")
            self.assertEqual(json.loads((Path(directory) / "ui_preferences.json").read_text()), {"language": "ja"})
            self.assertFalse((Path(directory) / "ui_preferences.tmp").exists())

    def test_corrupt_preferences_do_not_prevent_startup(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(plugin_main, "_resolve_storage_dir", return_value=Path(directory)):
            (Path(directory) / "ui_preferences.json").write_text("{broken", encoding="utf8")
            controller = plugin_main.VaseStudioController()
            self.assertIsNone(controller._manual_language)

    def test_late_request_does_not_overwrite_newer_saved_language(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(plugin_main, "_resolve_storage_dir", return_value=Path(directory)):
            controller = plugin_main.VaseStudioController()
            replies = []
            controller.handle_message({"type":"set_language","lang":"fr","mode":"page","request_id":2},replies.append)
            controller.handle_message({"type":"set_language","lang":"it","mode":"page","request_id":1},replies.append)
            self.assertEqual(controller.read_host_context()["lang"], "fr")
            self.assertEqual(json.loads((Path(directory) / "ui_preferences.json").read_text()), {"language":"fr"})
            self.assertEqual(replies[-1]["request_id"], 2)
            self.assertEqual(replies[-1]["language_revision"], 1)

    def test_actual_stl_3mf_exports_localize_messages_preserving_names_and_paths(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(plugin_main, "_resolve_storage_dir", return_value=Path(directory)):
            controller = plugin_main.VaseStudioController()
            params = controller.current_params
            params["name"] = "Custom Ω 日本語"
            expected_paths = {}
            for language in ("es", "it", "fr", "de", "ja"):
                controller.handle_message({"type": "set_language", "lang": language}, lambda _: None)
                for fmt in ("stl", "3mf"):
                    replies = []
                    controller.handle_message({"type": "export_file", "format": fmt, "params": params}, replies.append)
                    reply = next(item for item in replies if item["type"] == "action_result")
                    self.assertTrue(reply["ok"], reply)
                    exported = Path(reply["path"])
                    expected_paths.setdefault(fmt, exported)
                    self.assertEqual(exported, expected_paths[fmt])
                    self.assertEqual(reply["message"], translate_text("Exported successfully: {name}", language).replace("{name}", exported.name))
                    if fmt == "stl":
                        data = exported.read_bytes()
                        count = struct.unpack_from("<I", data, 80)[0]
                        self.assertGreater(count, 0)
                        self.assertEqual(len(data), 84 + 50 * count)
                    else:
                        with zipfile.ZipFile(exported) as archive:
                            model = archive.read("3D/3dmodel.model").decode("utf8")
                            self.assertIn("Custom Ω 日本語", model)
                self.assertEqual(controller.current_params["name"], params["name"])


if __name__ == "__main__":
    unittest.main()
