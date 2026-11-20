"""Data-only locale extension, strict packaging and safe runtime fallback."""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vase_studio import language_packs, locale_catalog, studio_ui, plugin_main


def write_pack(folder: Path, code: str = "nl", **changes) -> Path:
    pack = {"schema_version": 1, "code": code, "native_name": 'Nederlands & "NL"',
            "direction": "ltr", "order": 7,
            "translations": {"Total Height": "Hoogte", "Preset Gallery": "Galerij",
                             "ui:sec_presets::Preset Gallery": "Modellenbibliotheek"}}
    pack.update(changes)
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / (code + ".json")
    target.write_text(json.dumps(pack, ensure_ascii=False), encoding="utf8", newline="\n")
    return target


def unused_fixture_code() -> str:
    available = locale_catalog.supported_languages()
    candidates = itertools.chain(("nl",), ("q" + "".join(letters) for letters in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3)))
    return next(code for code in candidates if not any(item == code or item.startswith(code + "-") for item in available))


class TestLanguagePacks(unittest.TestCase):
    def test_migration_preserves_all_previous_translation_bytes(self):
        proof = json.loads((ROOT / "tests/fixtures/multilingual_catalog_reference.json").read_text(encoding="utf8"))
        vocabulary = locale_catalog.locale_vocabulary()
        for code, expected in proof["locale_translation_sha256"].items():
            # New feature strings may be added while every published entry stays exact.
            baseline = {key: vocabulary[code][key] for key in proof["locale_translation_keys"]}
            digest = hashlib.sha256(json.dumps(baseline, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
            self.assertEqual(digest, expected, code)
        for code, messages in proof["ui"].items():
            for key, (english, translated) in messages.items():
                self.assertEqual(locale_catalog.UI_MESSAGES[key], english)
                self.assertEqual(vocabulary[code][english], translated, (code, key))

    def test_one_extra_file_drives_host_page_dock_and_safe_metadata(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary) / "locales"
            shutil.copytree(ROOT / "src/vase_studio/locales", folder)
            code = unused_fixture_code()
            write_pack(folder, code)
            with patch.object(language_packs, "__file__", str(Path(temporary) / "language_packs.py")):
                self.assertIn(code, locale_catalog.supported_languages())
                self.assertEqual(plugin_main._detect_language({"language": code + "_NL"}), code)
                for mode in ("page", "dock"):
                    html = studio_ui.get_studio_html(mode, {"lang": code + "-NL"})
                    self.assertIn(f'<html lang="{code}" dir="ltr"', html)
                    self.assertTrue(f'<option value="{code}">Nederlands &amp; &quot;NL&quot;</option>' in html)
                    self.assertIn('"Total Height":"Hoogte"', html)
                self.assertEqual(locale_catalog.translate_text("Unregistered text", code), "Unregistered text")
                self.assertEqual(locale_catalog.translate_text("Total Height", code + "-NL"), "Hoogte")
                # A regional file wins exactly, while a different region uses its base.
                write_pack(folder, code + "-nl", native_name="Nederlands (Nederland)", translations={"Total Height": "Totale hoogte"})
                self.assertEqual(locale_catalog.normalize_language(code.upper() + "_nl.UTF-8"), code + "-nl")
                self.assertEqual(locale_catalog.normalize_language(code + "-BE"), code)
                self.assertEqual(locale_catalog.translate_text("Total Height", code + "-nl"), "Totale hoogte")
                write_pack(folder, "ar", native_name="العربية", direction="rtl")
                self.assertIn('<html lang="ar" dir="rtl"', studio_ui.get_studio_html("page", {"lang": "ar"}))

    def test_runtime_skips_invalid_optional_files_but_strict_validation_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            write_pack(folder)
            bad = folder / "bad.json"
            for content in ("{broken", '{"schema_version":1,"schema_version":1}',
                            json.dumps({"schema_version": True, "code": "xx", "native_name": "X"}),
                            json.dumps({"schema_version": 1, "code": "xx", "native_name": "X", "translations": {"Width {mm}": "Breedte"}}),
                            json.dumps({"schema_version": 1, "code": "xx", "native_name": "X", "translations": {"Name": "<script>alert(1)</script>"}})):
                bad.write_text(content, encoding="utf8")
                packs, errors = language_packs.load_language_packs(folder, embedded={})
                self.assertIn("nl", packs)
                self.assertTrue(errors)
                with self.assertRaises(ValueError):
                    language_packs.load_language_packs(folder, embedded={}, strict=True)
            bad.unlink()
            duplicate = json.loads((folder / "nl.json").read_text())
            (folder / "duplicate.json").write_text(json.dumps(duplicate), encoding="utf8")
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                language_packs.load_language_packs(folder, embedded={}, strict=True)

    def test_embedded_duplicates_and_placeholder_mismatch_rejected(self):
        base = {"schema_version": 1, "code": "nl-NL", "native_name": "Nederlands", "translations": {}}
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                language_packs.load_language_packs(temporary, embedded={"a": base, "b": {**base, "code": "nl_nl"}}, strict=True)
        for changed in ({"code": True}, {"native_name": "Bad\nname"}, {"translations": {"": "empty"}},
                        {"translations": {"{n} objects": "Oggetti {other}"}}):
            with self.assertRaises(ValueError):
                language_packs.validate_language_pack({**base, **changed})

    def test_data_only_eighth_pack_is_in_both_standalones_and_wheel(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            outside = Path(temporary) / "outside"
            outside.mkdir()
            shutil.copytree(ROOT / "src", project / "src", ignore=shutil.ignore_patterns("__pycache__"))
            (project / "scripts").mkdir()
            shutil.copy2(ROOT / "scripts/build_and_install.py", project / "scripts/build_and_install.py")
            for filename in ("README.md", "LICENSE", "pyproject.toml"):
                shutil.copy2(ROOT / filename, project / filename)
            extra_code = unused_fixture_code()
            expected_count = len(locale_catalog.supported_languages()) + 1
            write_pack(project / "src/vase_studio/locales", extra_code)
            result = subprocess.run([sys.executable, "-B", "-W", "error", str(project / "scripts/build_and_install.py"), "--no-install"], cwd=outside, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            probe = r'''
import json,sys,types,zipfile
from pathlib import Path
artifact=Path(sys.argv[1]);code=sys.argv[3]
if artifact.suffix == '.whl':
 target=Path(sys.argv[2]);zipfile.ZipFile(artifact).extractall(target);sys.path.insert(0,str(target))
 from vase_studio import locale_catalog as adapter, studio_ui as ui, plugin_main as plugin
else:
 module=types.ModuleType('_data_only_bundle');module.__file__=str(artifact);sys.modules[module.__name__]=module
 exec(compile(artifact.read_text(encoding='utf8'),str(artifact),'exec'),module.__dict__)
 adapter=ui=module;plugin=module
assert code in adapter.supported_languages()
assert plugin._detect_language({'language':code+'_NL'}) == code
for mode in ('page','dock'):
 html=ui.get_studio_html(mode,{'lang':code+'-NL'})
 assert ('<html lang="'+code+'" dir="ltr"') in html
 assert ('<option value="'+code+'">') in html
 assert '"Total Height":"Hoogte"' in html
assert adapter.translate_text('Untranslated',code)=='Untranslated'
print(json.dumps({'artifact':artifact.name,'languages':len(adapter.supported_languages()),'ok':True}))
'''
            artifacts = sorted((project / "dist").iterdir())
            self.assertEqual(len(artifacts), 3)
            for index, artifact in enumerate(artifacts):
                child = subprocess.run([sys.executable, "-B", "-W", "error", "-c", probe, str(artifact), str(outside / ("wheel_" + str(index))), extra_code], cwd=outside, capture_output=True, text=True)
                self.assertEqual(child.returncode, 0, artifact.name + child.stdout + child.stderr)
                self.assertEqual(json.loads(child.stdout)["languages"], expected_count)
            # Strict errors are detected before replacing the existing distribution.
            before = {artifact.name: hashlib.sha256(artifact.read_bytes()).hexdigest() for artifact in artifacts}
            (project / "src/vase_studio/locales/bad.json").write_text("{bad", encoding="utf8")
            invalid = subprocess.run([sys.executable, "-B", "-W", "error", str(project / "scripts/build_and_install.py"), "--no-install"], cwd=outside, capture_output=True, text=True)
            self.assertNotEqual(invalid.returncode, 0)
            self.assertEqual(before, {artifact.name: hashlib.sha256(artifact.read_bytes()).hexdigest() for artifact in artifacts})


if __name__ == "__main__":
    unittest.main()
