"""Discover data-only offline language packs in source, wheels and standalone bundles.

This module is self-contained so future Studio plugins can use the same format
without importing another plugin. Catalogs never contain executable code.
"""
from __future__ import annotations

import base64
import json
from pathlib import Path
import re
import zlib

_BUNDLED_LANGUAGE_PACKS = {}  # Replaced with compressed JSON by the standalone builder.
_PACK_CODE = re.compile(r"^[a-z]{2,8}(?:-[a-z0-9]{1,8})*$")
_PACK_PLACEHOLDER = re.compile(r"\{[A-Za-z_]\w*\}")
_PACK_HTML_TAG = re.compile(r"<\s*/?\s*[A-Za-z][^>]*>")
_PACK_MAX_BYTES = 2 * 1024 * 1024


def canonical_language_code(value: object) -> str:
    """BCP-47-style matching, accepting the host's underscore and encoding suffix."""
    return str(value or "").strip().lower().replace("_", "-").split(".", 1)[0].split("@", 1)[0]


def validate_language_pack(raw: object, filename: str = "catalog.json") -> dict:
    if not isinstance(raw, dict) or type(raw.get("schema_version")) is not int or raw["schema_version"] != 1:
        raise ValueError("Language pack requires schema_version 1: " + filename)
    if not isinstance(raw.get("code"), str):
        raise ValueError("Language code must be text: " + filename)
    code = canonical_language_code(raw["code"])
    if not _PACK_CODE.fullmatch(code):
        raise ValueError("Invalid language code: " + filename)
    name = raw.get("native_name")
    if (not isinstance(name, str) or not 1 <= len(name.strip()) <= 80
            or _PACK_HTML_TAG.search(name) or any(ord(char) < 32 for char in name)):
        raise ValueError("Invalid native language name: " + filename)
    direction = raw.get("direction", "ltr")
    if direction not in ("ltr", "rtl"):
        raise ValueError("Invalid text direction: " + filename)
    order = raw.get("order", 1000)
    if not isinstance(order, int) or isinstance(order, bool):
        raise ValueError("Invalid language order: " + filename)
    translations = raw.get("translations", {})
    if not isinstance(translations, dict):
        raise ValueError("Translations must be an object: " + filename)
    checked = {}
    for english, translated in translations.items():
        if not isinstance(english, str) or not english.strip() or not isinstance(translated, str) or not translated.strip():
            raise ValueError("Translations must contain nonempty text: " + filename)
        if _PACK_HTML_TAG.search(translated):
            raise ValueError("Translations are plain text, not HTML: " + filename)
        if sorted(_PACK_PLACEHOLDER.findall(english)) != sorted(_PACK_PLACEHOLDER.findall(translated)):
            raise ValueError("Translation placeholders differ: " + filename)
        checked[english] = translated
    return {"schema_version": 1, "code": code, "native_name": name.strip(),
            "direction": direction, "order": order, "translations": checked}


def _language_json_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON object key: " + str(key))
        result[key] = value
    return result


def read_language_pack_files(folder: Path, strict: bool = False) -> tuple[dict, list[str]]:
    """Read only immediate JSON files; invalid optional packs cannot disable the UI."""
    found, errors = {}, []
    if not folder.is_dir():
        return found, errors
    for path in sorted(folder.glob("*.json")):
        try:
            path.resolve().relative_to(folder.resolve())
            if path.stat().st_size > _PACK_MAX_BYTES:
                raise ValueError("Language pack exceeds size limit: " + path.name)
            raw = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_language_json_object)
            pack = validate_language_pack(raw, path.name)
            if pack["code"] in found:
                raise ValueError("Duplicate language code: " + path.name)
            found[pack["code"]] = pack
        except (OSError, ValueError, TypeError, UnicodeError) as exc:
            if strict:
                raise ValueError("Invalid language pack " + path.name + ": " + str(exc)) from exc
            errors.append(path.name + ": " + type(exc).__name__)
    return found, errors


def load_language_packs(folder: str | Path | None = None, *, embedded: dict | None = None,
                        strict: bool = False) -> tuple[dict, tuple[str, ...]]:
    """Bundle data first, then optional local JSON overrides, sorted by metadata."""
    packs, errors = {}, []
    for filename, raw in (embedded if embedded is not None else _BUNDLED_LANGUAGE_PACKS).items():
        try:
            pack = validate_language_pack(raw, str(filename))
            if pack["code"] in packs:
                raise ValueError("Duplicate embedded language code: " + str(filename))
            packs[pack["code"]] = pack
        except (ValueError, TypeError) as exc:
            if strict:
                raise
            errors.append(str(filename) + ": " + type(exc).__name__)
    directory = Path(folder) if folder is not None else Path(__file__).resolve().parent / "locales"
    files, issues = read_language_pack_files(directory, strict=strict)
    errors.extend(issues)
    for code, pack in files.items():
        if code in packs:
            pack = {**pack, "translations": {**packs[code]["translations"], **pack["translations"]}}
        packs[code] = pack
    packs.setdefault("en", {"schema_version": 1, "code": "en", "native_name": "English",
                            "direction": "ltr", "order": 1, "translations": {}})
    return dict(sorted(packs.items(), key=lambda item: (item[1]["order"], item[0]))), tuple(errors)


def resolve_language(value: object, available: object, default: str = "pt") -> str:
    code = canonical_language_code(value)
    if not code:
        return default if default in available else "en"
    candidate = code
    while candidate:
        if candidate in available:
            return candidate
        candidate = candidate.rsplit("-", 1)[0] if "-" in candidate else ""
    return "en"


def language_pack_payload(packs: dict) -> list[dict]:
    """Metadata is used by the UI directly; there is no second locale allowlist."""
    return [{"code": code, "native_name": pack["native_name"], "direction": pack["direction"]}
            for code, pack in packs.items()]
