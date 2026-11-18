# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-vase-studio"
# name = "Orca Vase Studio"
# description = "Parametric 3D Vase & Planter Studio with X-Ray Wall Calipers & 1-Click Plater | Estudio 3D de Vasos e Cachepos"
# author = "Orca Vase Studio"
# version = "1.1.1"
# ///

from __future__ import annotations

import sys as _orca_init_sys
import types as _orca_init_types
if __name__ not in _orca_init_sys.modules:
    _orca_init_sys.modules[__name__] = _orca_init_types.ModuleType(__name__)

# ===========================================================================
# MODULE: vase_studio.schema
# ===========================================================================

"""Unified parameter schema and validation for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import copy
import math
from typing import Any

SCHEMA_VERSION = "1.0"

DEFAULT_PARAMS: dict[str, Any] = {
    "name": "Ondas Organicas",
    "height_mm": 160.0,              # [30.0, 500.0]
    "base_diameter_mm": 76.0,        # [20.0, 450.0]
    "belly_diameter_mm": 110.0,      # [20.0, 450.0]
    "belly_height_ratio": 0.34,      # [0.08, 0.85]
    "waist_diameter_mm": 68.0,       # [16.0, 450.0]
    "waist_height_ratio": 0.68,      # [0.15, 0.92]
    "neck_diameter_mm": 82.0,        # [16.0, 450.0]
    "lip_flare_mm": 4.0,             # [-15.0, 25.0] extra radius added smoothly over top 8% (z_norm 0.92..1.0)
    "lip_bevel_mm": 1.0,             # [0.0, 4.0] subtle top rim rounding/bevel
    "polygon_sides": 0,              # 0 = smooth circle; 3..24 = polygonal cross-section
    "polygon_roundness": 0.35,       # [0.0, 1.0] blends polygon radius toward circle (1.0 = pure circle)
    "use_custom_profile": False,     # bool: when True, base silhouette comes from profile_points instead of base/belly/waist/neck
    "profile_points": [              # list of [z_norm (0..1), radius_mm (8..225)], >= 2 points, endpoints clamped to z=0.0 and z=1.0
        [0.0, 38.0],
        [0.34, 55.0],
        [0.68, 34.0],
        [0.92, 41.0],
        [1.0, 45.0],
    ],
    "resolution_angular": 240,       # [64, 360]
    "resolution_vertical": 220,      # [60, 400]

    # Global texture envelope & helical twist
    "bottom_fade_mm": 8.0,           # [0.0, 60.0] smoothstep 0->1 from z=0 to z=bottom_fade_mm (flat bed adhesion!)
    "top_fade_mm": 6.0,              # [0.0, 60.0] smoothstep 1->0 from z=(H - top_fade_mm) to z=H
    "global_twist_deg": 0.0,         # [-720.0, 720.0]

    # Combinable Surface Texture Layers (summed radial displacement in mm)
    "textures": {
        "ribbed": {
            "enabled": False,
            "depth_mm": 2.6,         # [-15.0, 15.0]
            "count": 32,             # [3, 180] circumferential rib count (density)
            "duty_cycle": 0.50,      # [0.10, 0.90] width of rib vs flat spacing gap
            "sharpness": 0.35,       # [0.0, 1.0] 0=smooth cosine, 0.5=rounded flute, 1.0=sharp triangular/chiseled
            "twist_deg": 60.0,       # [-720.0, 720.0]
            "phase_deg": 0.0,        # [0.0, 360.0]
        },
        "waves": {
            "enabled": True,
            "depth_mm": 3.0,         # [-15.0, 15.0]
            "vertical_wavelength_mm": 26.0,  # [4.0, 120.0] vertical wave spacing in mm
            "angular_lobes": 6,      # [0, 48] circumferential wave count
            "interference_mix": 0.45,  # [0.0, 1.0] mix of counter-helical wave creating organic woven/ripple pockets
            "wave_skew": 0.0,        # [-0.8, 0.8]
            "phase_deg": 0.0,        # [0.0, 360.0]
        },
        "origami": {
            "enabled": False,
            "depth_mm": 3.2,         # [-15.0, 15.0]
            "cells_around": 12,      # [3, 60] horizontal diamond density
            "cells_vertical": 8,     # [2, 50] vertical diamond tiers
            "crease_sharpness": 0.75,  # [0.0, 1.0]
            "stagger": 0.50,         # [0.0, 1.0]
        },
        "cellular": {
            "enabled": False,
            "depth_mm": 2.4,         # [-12.0, 12.0]
            "scale_angular": 8,      # [2, 40] cells around circumference
            "scale_vertical_mm": 22.0,  # [5.0, 100.0] vertical cell spacing in mm
            "ridge_mode": True,      # bool: True = ridged coral/stone veins, False = smooth organic billows
            "octaves": 2,            # [1, 4]
            "seed": 42,              # [1, 99999]
        },
    },

    # Printability & Wall Structure
    "print_mode": "shelled_hollow",  # "shelled_hollow" | "spiral_vase"
    "stl_always_open_hollow": True,  # keep open mouth when exporting .stl even if spiral_vase is selected
    "auto_configure_slicer": True,
    "spiral_line_width_mm": 0.65,    # [0.40, 1.20]
    "spiral_bottom_layers": 5,       # [2, 15]
    "spiral_smooth": True,
    "wall_thickness_mm": 2.4,        # [0.8, 25.0] used when print_mode == "shelled_hollow"
    "bottom_thickness_mm": 3.2,      # [1.0, 25.0] used when print_mode == "shelled_hollow"
    "auto_clamp_overhang": False,
    "max_safe_overhang_deg": 48.0,   # [35.0, 65.0]

    # Gardening: Drainage & Matching Saucer
    "drainage": {
        "enabled": False,
        "hole_count": 4,             # [1, 9]
        "hole_diameter_mm": 8.0,     # [3.0, 20.0]
        "ring_radius_ratio": 0.48,   # [0.0, 0.68]
    },
    "saucer": {
        "clearance_mm": 8.0,         # [3.0, 25.0]
        "rim_height_mm": 22.0,       # [10.0, 60.0]
        "wall_thickness_mm": 2.4,    # [1.2, 5.0]
        "floor_thickness_mm": 2.6,   # [1.2, 6.0]
        "inner_ribs_height_mm": 2.0, # [0.0, 6.0] raised drainage ribs inside saucer floor
        "match_vase_texture": True,
    },
}


def _to_float(val: Any, default: float, lo: float, hi: float) -> float:
    if isinstance(val, bool):
        return default
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f):
        return default
    return max(lo, min(hi, f))


def _to_int(val: Any, default: int, lo: int, hi: int) -> int:
    if isinstance(val, bool):
        return default
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f):
        return default
    i = int(round(f))
    return max(lo, min(hi, i))


def _to_bool(val: Any, default: bool) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        if math.isfinite(val):
            return bool(val)
        return default
    if isinstance(val, str):
        s = val.strip().lower()
        if s in ("true", "1", "yes", "on"):
            return True
        if s in ("false", "0", "no", "off", ""):
            return False
    return default


def _normalize_profile_points(raw_pts: Any) -> list[list[float]]:
    default_pts = copy.deepcopy(DEFAULT_PARAMS["profile_points"])
    if not isinstance(raw_pts, (list, tuple)) or len(raw_pts) < 2:
        return default_pts

    parsed: list[list[float]] = []
    for item in raw_pts:
        z_raw: Any = None
        r_raw: Any = None
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            z_raw, r_raw = item[0], item[1]
        elif isinstance(item, dict):
            z_raw = item.get("z", item.get("z_norm"))
            r_raw = item.get("r", item.get("radius_mm", item.get("radius")))
        else:
            continue

        z_val = _to_float(z_raw, -1.0, 0.0, 1.0)
        r_val = _to_float(r_raw, -1.0, 8.0, 225.0)
        if z_raw is None or r_raw is None:
            continue
        try:
            zf = float(z_raw)
            rf = float(r_raw)
            if not (math.isfinite(zf) and math.isfinite(rf)):
                continue
        except (TypeError, ValueError):
            continue
        parsed.append([max(0.0, min(1.0, zf)), max(8.0, min(225.0, rf))])

    if len(parsed) < 2:
        return default_pts

    parsed.sort(key=lambda p: p[0])
    parsed[0][0] = 0.0
    parsed[-1][0] = 1.0

    # Deduplicate near-identical z_norm knots so PCHIP never divides by zero
    cleaned: list[list[float]] = [parsed[0]]
    for pt in parsed[1:]:
        if pt[0] - cleaned[-1][0] < 1e-4:
            if pt[0] >= 1.0:
                cleaned[-1] = [1.0, pt[1]]
            else:
                cleaned[-1][1] = 0.5 * (cleaned[-1][1] + pt[1])
        else:
            cleaned.append(pt)

    if len(cleaned) < 2:
        return default_pts
    cleaned[0][0] = 0.0
    cleaned[-1][0] = 1.0
    return cleaned


def _deep_merge_dict(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    for k, v in override.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            _deep_merge_dict(base[k], v)
        elif k in base:
            base[k] = v
    return base


def normalize_params(raw: dict[str, Any] | None) -> dict[str, Any]:
    """Deep-copy DEFAULT_PARAMS, merge raw recursively, coerce types, and clamp bounds."""
    out = copy.deepcopy(DEFAULT_PARAMS)
    if isinstance(raw, dict):
        _deep_merge_dict(out, raw)

    # Top-level string & mode fields
    raw_name = out.get("name")
    if isinstance(raw_name, str) and raw_name.strip():
        out["name"] = raw_name.strip()[:120]
    else:
        out["name"] = DEFAULT_PARAMS["name"]

    d = DEFAULT_PARAMS
    out["height_mm"] = _to_float(out["height_mm"], d["height_mm"], 30.0, 500.0)
    out["base_diameter_mm"] = _to_float(out["base_diameter_mm"], d["base_diameter_mm"], 20.0, 450.0)
    out["belly_diameter_mm"] = _to_float(out["belly_diameter_mm"], d["belly_diameter_mm"], 20.0, 450.0)
    out["belly_height_ratio"] = _to_float(out["belly_height_ratio"], d["belly_height_ratio"], 0.08, 0.85)
    out["waist_diameter_mm"] = _to_float(out["waist_diameter_mm"], d["waist_diameter_mm"], 16.0, 450.0)
    out["waist_height_ratio"] = _to_float(out["waist_height_ratio"], d["waist_height_ratio"], 0.15, 0.92)
    out["neck_diameter_mm"] = _to_float(out["neck_diameter_mm"], d["neck_diameter_mm"], 16.0, 450.0)
    out["lip_flare_mm"] = _to_float(out["lip_flare_mm"], d["lip_flare_mm"], -15.0, 25.0)
    out["lip_bevel_mm"] = _to_float(out["lip_bevel_mm"], d["lip_bevel_mm"], 0.0, 4.0)

    poly_sides = _to_int(out["polygon_sides"], d["polygon_sides"], 0, 24)
    out["polygon_sides"] = 0 if poly_sides < 3 else poly_sides
    out["polygon_roundness"] = _to_float(out["polygon_roundness"], d["polygon_roundness"], 0.0, 1.0)

    out["use_custom_profile"] = _to_bool(out["use_custom_profile"], d["use_custom_profile"])
    out["profile_points"] = _normalize_profile_points(out.get("profile_points"))

    out["resolution_angular"] = _to_int(out["resolution_angular"], d["resolution_angular"], 64, 360)
    out["resolution_vertical"] = _to_int(out["resolution_vertical"], d["resolution_vertical"], 60, 400)

    out["bottom_fade_mm"] = _to_float(out["bottom_fade_mm"], d["bottom_fade_mm"], 0.0, 60.0)
    out["top_fade_mm"] = _to_float(out["top_fade_mm"], d["top_fade_mm"], 0.0, 60.0)
    out["global_twist_deg"] = _to_float(out["global_twist_deg"], d["global_twist_deg"], -720.0, 720.0)

    # Textures
    tex = out["textures"]
    dt = d["textures"]

    rib = tex["ribbed"]
    d_rib = dt["ribbed"]
    rib["enabled"] = _to_bool(rib["enabled"], d_rib["enabled"])
    rib["depth_mm"] = _to_float(rib["depth_mm"], d_rib["depth_mm"], -15.0, 15.0)
    rib["count"] = _to_int(rib["count"], d_rib["count"], 3, 180)
    rib["duty_cycle"] = _to_float(rib["duty_cycle"], d_rib["duty_cycle"], 0.10, 0.90)
    rib["sharpness"] = _to_float(rib["sharpness"], d_rib["sharpness"], 0.0, 1.0)
    rib["twist_deg"] = _to_float(rib["twist_deg"], d_rib["twist_deg"], -720.0, 720.0)
    rib["phase_deg"] = _to_float(rib["phase_deg"], d_rib["phase_deg"], 0.0, 360.0)

    wav = tex["waves"]
    d_wav = dt["waves"]
    wav["enabled"] = _to_bool(wav["enabled"], d_wav["enabled"])
    wav["depth_mm"] = _to_float(wav["depth_mm"], d_wav["depth_mm"], -15.0, 15.0)
    wav["vertical_wavelength_mm"] = _to_float(wav["vertical_wavelength_mm"], d_wav["vertical_wavelength_mm"], 4.0, 120.0)
    wav["angular_lobes"] = _to_int(wav["angular_lobes"], d_wav["angular_lobes"], 0, 48)
    wav["interference_mix"] = _to_float(wav["interference_mix"], d_wav["interference_mix"], 0.0, 1.0)
    wav["wave_skew"] = _to_float(wav["wave_skew"], d_wav["wave_skew"], -0.8, 0.8)
    wav["phase_deg"] = _to_float(wav["phase_deg"], d_wav["phase_deg"], 0.0, 360.0)

    ori = tex["origami"]
    d_ori = dt["origami"]
    ori["enabled"] = _to_bool(ori["enabled"], d_ori["enabled"])
    ori["depth_mm"] = _to_float(ori["depth_mm"], d_ori["depth_mm"], -15.0, 15.0)
    ori["cells_around"] = _to_int(ori["cells_around"], d_ori["cells_around"], 3, 60)
    ori["cells_vertical"] = _to_int(ori["cells_vertical"], d_ori["cells_vertical"], 2, 50)
    ori["crease_sharpness"] = _to_float(ori["crease_sharpness"], d_ori["crease_sharpness"], 0.0, 1.0)
    ori["stagger"] = _to_float(ori["stagger"], d_ori["stagger"], 0.0, 1.0)

    cel = tex["cellular"]
    d_cel = dt["cellular"]
    cel["enabled"] = _to_bool(cel["enabled"], d_cel["enabled"])
    cel["depth_mm"] = _to_float(cel["depth_mm"], d_cel["depth_mm"], -12.0, 12.0)
    cel["scale_angular"] = _to_int(cel["scale_angular"], d_cel["scale_angular"], 2, 40)
    cel["scale_vertical_mm"] = _to_float(cel["scale_vertical_mm"], d_cel["scale_vertical_mm"], 5.0, 100.0)
    cel["ridge_mode"] = _to_bool(cel["ridge_mode"], d_cel["ridge_mode"])
    cel["octaves"] = _to_int(cel["octaves"], d_cel["octaves"], 1, 4)
    cel["seed"] = _to_int(cel["seed"], d_cel["seed"], 1, 99999)

    # Printability & Wall Structure
    pm = str(out.get("print_mode", d["print_mode"])).strip().lower()
    out["print_mode"] = pm if pm in ("spiral_vase", "shelled_hollow") else d["print_mode"]
    out["stl_always_open_hollow"] = _to_bool(out["stl_always_open_hollow"], d["stl_always_open_hollow"])
    out["auto_configure_slicer"] = _to_bool(out["auto_configure_slicer"], d["auto_configure_slicer"])
    out["spiral_line_width_mm"] = _to_float(out["spiral_line_width_mm"], d["spiral_line_width_mm"], 0.40, 1.20)
    out["spiral_bottom_layers"] = _to_int(out["spiral_bottom_layers"], d["spiral_bottom_layers"], 2, 15)
    out["spiral_smooth"] = _to_bool(out["spiral_smooth"], d["spiral_smooth"])
    out["wall_thickness_mm"] = _to_float(out["wall_thickness_mm"], d["wall_thickness_mm"], 0.8, 25.0)
    out["bottom_thickness_mm"] = _to_float(out["bottom_thickness_mm"], d["bottom_thickness_mm"], 1.0, 25.0)
    out["auto_clamp_overhang"] = _to_bool(out["auto_clamp_overhang"], d["auto_clamp_overhang"])
    out["max_safe_overhang_deg"] = _to_float(out["max_safe_overhang_deg"], d["max_safe_overhang_deg"], 35.0, 65.0)

    # Drainage
    dr = out["drainage"]
    d_dr = d["drainage"]
    dr["enabled"] = _to_bool(dr["enabled"], d_dr["enabled"])
    dr["hole_count"] = _to_int(dr["hole_count"], d_dr["hole_count"], 1, 9)
    dr["hole_diameter_mm"] = _to_float(dr["hole_diameter_mm"], d_dr["hole_diameter_mm"], 3.0, 20.0)
    dr["ring_radius_ratio"] = _to_float(dr["ring_radius_ratio"], d_dr["ring_radius_ratio"], 0.0, 0.68)

    # Saucer
    sc = out["saucer"]
    d_sc = d["saucer"]
    sc["clearance_mm"] = _to_float(sc["clearance_mm"], d_sc["clearance_mm"], 3.0, 25.0)
    sc["rim_height_mm"] = _to_float(sc["rim_height_mm"], d_sc["rim_height_mm"], 10.0, 60.0)
    sc["wall_thickness_mm"] = _to_float(sc["wall_thickness_mm"], d_sc["wall_thickness_mm"], 1.2, 5.0)
    sc["floor_thickness_mm"] = _to_float(sc["floor_thickness_mm"], d_sc["floor_thickness_mm"], 1.2, 6.0)
    sc["inner_ribs_height_mm"] = _to_float(sc["inner_ribs_height_mm"], d_sc["inner_ribs_height_mm"], 0.0, 6.0)
    sc["match_vase_texture"] = _to_bool(sc["match_vase_texture"], d_sc["match_vase_texture"])

    return out

# ===========================================================================
# MODULE: vase_studio.mesh_generator
# ===========================================================================

"""Parametric 3D vase and saucer manifold mesh generator for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

from dataclasses import dataclass
import math
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import os as _os
    from pathlib import Path as _Path
    import sys as _sys

    if _sys.platform == "win32":
        _appdata = _os.environ.get("APPDATA", "").strip()
        _orca_base = _Path(_appdata) / "OrcaSlicer" if _appdata else _Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    elif _sys.platform == "darwin":
        _orca_base = _Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    else:
        _xdg = _os.environ.get("XDG_CONFIG_HOME", "").strip()
        _orca_base = (_Path(_xdg) if _xdg else (_Path.home() / ".config")) / "OrcaSlicer"

    _orca_pkg_dir = str(_orca_base / "python" / "packages" / f"cp{_sys.version_info.major}{_sys.version_info.minor}")
    if _orca_pkg_dir not in _sys.path:
        _sys.path.insert(0, _orca_pkg_dir)
    import numpy as np

pass  # [bundled] resolved intra-package import


@dataclass
class MeshData:
    vertices: np.ndarray      # float32, shape (V, 3), min Z == 0.0, centered at X=0, Y=0
    triangles: np.ndarray     # int32, shape (F, 3), outward CCW winding (right-hand rule)
    face_normals: np.ndarray  # float32, shape (F, 3), unit normals
    bounds_mm: dict[str, list[float]]  # {"min": [x,y,z], "max": [x,y,z], "size": [dx,dy,dz]}
    volume_cm3: float


# ---------------------------------------------------------------------------
# Section 2: Shared Mathematical Surface Evaluation (Python <-> WebGL2 Parity)
# ---------------------------------------------------------------------------

def _smoothstep(edge0: float, edge1: float, x: np.ndarray) -> np.ndarray:
    span = edge1 - edge0
    if span <= 1e-9:
        return np.where(x > edge0, 1.0, 0.0)
    u = np.clip((x - edge0) / span, 0.0, 1.0)
    return u * u * (3.0 - 2.0 * u)


def _prepare_knots(params: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    if params["use_custom_profile"]:
        raw = [[float(p[0]), float(p[1])] for p in params["profile_points"]]
    else:
        r_base = 0.5 * float(params["base_diameter_mm"])
        r_belly = 0.5 * float(params["belly_diameter_mm"])
        r_waist = 0.5 * float(params["waist_diameter_mm"])
        r_neck = 0.5 * float(params["neck_diameter_mm"])
        r_lip = max(4.0, r_neck + float(params["lip_flare_mm"]))
        raw = [
            [0.0, r_base],
            [float(params["belly_height_ratio"]), r_belly],
            [float(params["waist_height_ratio"]), r_waist],
            [0.92, r_neck],
            [1.0, r_lip],
        ]

    raw.sort(key=lambda pair: pair[0])
    raw[0][0] = 0.0
    raw[-1][0] = 1.0

    # Ensure strictly increasing z_norm knots so PCHIP never divides by zero
    dedup: list[list[float]] = [raw[0]]
    for z_k, r_k in raw[1:]:
        if z_k - dedup[-1][0] < 1e-4:
            if z_k >= 1.0:
                dedup[-1] = [1.0, r_k]
            else:
                dedup[-1][1] = 0.5 * (dedup[-1][1] + r_k)
        else:
            dedup.append([z_k, r_k])

    if len(dedup) < 2:
        dedup = [[0.0, raw[0][1]], [1.0, raw[-1][1]]]

    xs = np.array([p[0] for p in dedup], dtype=np.float64)
    ys = np.array([p[1] for p in dedup], dtype=np.float64)
    return xs, ys


def _pchip_interpolate(xs: np.ndarray, ys: np.ndarray, x_eval: np.ndarray) -> np.ndarray:
    """Monotone Piecewise Cubic Hermite Interpolating Polynomial (Fritsch-Carlson / PCHIP)."""
    m = len(xs)
    if m == 2:
        t = np.clip((x_eval - xs[0]) / max(xs[1] - xs[0], 1e-9), 0.0, 1.0)
        return ys[0] + t * (ys[1] - ys[0])

    h = np.diff(xs)
    delta = np.diff(ys) / h
    d = np.zeros(m, dtype=np.float64)

    # Interior slopes: weighted harmonic mean when adjacent secants share sign
    for k in range(1, m - 1):
        if delta[k - 1] * delta[k] > 0.0:
            w1 = 2.0 * h[k] + h[k - 1]
            w2 = h[k] + 2.0 * h[k - 1]
            d[k] = (w1 + w2) / (w1 / delta[k - 1] + w2 / delta[k])
        else:
            d[k] = 0.0

    # Shape-preserving endpoint slopes
    d0 = ((2.0 * h[0] + h[1]) * delta[0] - h[0] * delta[1]) / (h[0] + h[1])
    if d0 * delta[0] <= 0.0:
        d0 = 0.0
    elif (delta[0] * delta[1] <= 0.0) and (abs(d0) > abs(3.0 * delta[0])):
        d0 = 3.0 * delta[0]
    d[0] = d0

    dn = ((2.0 * h[-1] + h[-2]) * delta[-1] - h[-1] * delta[-2]) / (h[-1] + h[-2])
    if dn * delta[-1] <= 0.0:
        dn = 0.0
    elif (delta[-1] * delta[-2] <= 0.0) and (abs(dn) > abs(3.0 * delta[-1])):
        dn = 3.0 * delta[-1]
    d[-1] = dn

    x_clamped = np.clip(x_eval, xs[0], xs[-1])
    idx = np.searchsorted(xs, x_clamped, side="right") - 1
    idx = np.clip(idx, 0, m - 2)

    hk = h[idx]
    t = (x_clamped - xs[idx]) / hk
    t2 = t * t
    t3 = t2 * t

    h00 = 2.0 * t3 - 3.0 * t2 + 1.0
    h10 = t3 - 2.0 * t2 + t
    h01 = -2.0 * t3 + 3.0 * t2
    h11 = t3 - t2

    return h00 * ys[idx] + h10 * hk * d[idx] + h01 * ys[idx + 1] + h11 * hk * d[idx + 1]


def _hash3_u32(ix: np.ndarray, iy: np.ndarray, iz: np.ndarray, seed: int) -> np.ndarray:
    """Deterministic 32-bit integer hash matching JS Math.imul bit-for-bit."""
    ux = ix.astype(np.int64).astype(np.uint32)
    uy = iy.astype(np.int64).astype(np.uint32)
    uz = iz.astype(np.int64).astype(np.uint32)
    us = np.uint32(int(seed) & 0xFFFFFFFF)

    with np.errstate(over="ignore"):
        h = (
            ux * np.uint32(374761393)
            + uy * np.uint32(668265263)
            + uz * np.uint32(1274126177)
            + us * np.uint32(1597334677)
        )
        h = h ^ (h >> np.uint32(13))
        h = h * np.uint32(1274126177)
        h = h ^ (h >> np.uint32(16))

    return h.astype(np.float64) / 4294967295.0


def _value_noise_3d(cx: np.ndarray, cy: np.ndarray, cz: np.ndarray, octaves: int, seed: int) -> np.ndarray:
    total = np.zeros_like(cx, dtype=np.float64)
    amp_sum = 0.0
    freq = 1.0
    amp = 1.0

    for oct_idx in range(max(1, int(octaves))):
        x = cx * freq
        y = cy * freq
        z = cz * freq

        ix0 = np.floor(x).astype(np.int64)
        iy0 = np.floor(y).astype(np.int64)
        iz0 = np.floor(z).astype(np.int64)

        fx = x - ix0
        fy = y - iy0
        fz = z - iz0

        ux = fx * fx * (3.0 - 2.0 * fx)
        uy = fy * fy * (3.0 - 2.0 * fy)
        uz = fz * fz * (3.0 - 2.0 * fz)

        s_oct = int(seed)
        c000 = _hash3_u32(ix0, iy0, iz0, s_oct)
        c100 = _hash3_u32(ix0 + 1, iy0, iz0, s_oct)
        c010 = _hash3_u32(ix0, iy0 + 1, iz0, s_oct)
        c110 = _hash3_u32(ix0 + 1, iy0 + 1, iz0, s_oct)
        c001 = _hash3_u32(ix0, iy0, iz0 + 1, s_oct)
        c101 = _hash3_u32(ix0 + 1, iy0, iz0 + 1, s_oct)
        c011 = _hash3_u32(ix0, iy0 + 1, iz0 + 1, s_oct)
        c111 = _hash3_u32(ix0 + 1, iy0 + 1, iz0 + 1, s_oct)

        nx00 = c000 + ux * (c100 - c000)
        nx10 = c010 + ux * (c110 - c010)
        nx01 = c001 + ux * (c101 - c001)
        nx11 = c011 + ux * (c111 - c011)

        nxy0 = nx00 + uy * (nx10 - nx00)
        nxy1 = nx01 + uy * (nx11 - nx01)

        n_val = nxy0 + uz * (nxy1 - nxy0)
        total += amp * n_val
        amp_sum += amp
        freq *= 2.0
        amp *= 0.5

    return total / max(amp_sum, 1e-9)


def _compute_texture_displacement(
    z_grid: np.ndarray,
    z_norm_grid: np.ndarray,
    theta_grid: np.ndarray,
    theta_g: np.ndarray,
    textures: dict[str, Any],
    global_twist_rad: float,
) -> np.ndarray:
    dr = np.zeros_like(theta_g, dtype=np.float64)

    rib = textures["ribbed"]
    if rib["enabled"] and abs(rib["depth_mm"]) > 1e-9:
        count = float(rib["count"])
        duty = float(rib["duty_cycle"])
        sharp = float(rib["sharpness"])
        twist_rad = math.radians(float(rib["twist_deg"]))
        phase_rad = math.radians(float(rib["phase_deg"]))

        phi = np.mod((theta_grid + twist_rad * z_norm_grid + phase_rad) * count / (2.0 * math.pi), 1.0)
        u = np.abs(phi - 0.5) * 2.0
        t = np.clip(u / max(duty, 1e-6), 0.0, 1.0)
        w_smooth = 0.5 * (1.0 + np.cos(math.pi * t))
        w_sharp = 1.0 - t
        shape = (1.0 - sharp) * w_smooth + sharp * w_sharp
        dr += float(rib["depth_mm"]) * shape

    wav = textures["waves"]
    if wav["enabled"] and abs(wav["depth_mm"]) > 1e-9:
        wl = max(float(wav["vertical_wavelength_mm"]), 1.0)
        lobes = float(wav["angular_lobes"])
        mix = float(wav["interference_mix"])
        skew = float(wav["wave_skew"])
        phase_rad = math.radians(float(wav["phase_deg"]))

        kz = (2.0 * math.pi * z_grid / wl) + phase_rad
        ka = lobes * theta_grid + global_twist_rad * z_norm_grid
        w1 = np.sin(kz + ka + skew * np.sin(kz))
        w2 = np.sin(kz - ka)
        dr += float(wav["depth_mm"]) * ((1.0 - 0.5 * mix) * w1 + 0.5 * mix * w2)

    ori = textures["origami"]
    if ori["enabled"] and abs(ori["depth_mm"]) > 1e-9:
        c_around = float(ori["cells_around"])
        c_vert = float(ori["cells_vertical"])
        crease = float(ori["crease_sharpness"])
        stagger = float(ori["stagger"])

        v = z_norm_grid * c_vert
        tier = np.floor(v)
        fv = v - tier
        u = (theta_grid / (2.0 * math.pi)) * c_around + tier * stagger
        fu = u - np.floor(u)

        diamond = 1.0 - (np.abs(2.0 * fu - 1.0) + np.abs(2.0 * fv - 1.0))
        soft = np.sin(math.pi * (fu - 0.5)) * np.sin(math.pi * (fv - 0.5))
        val = crease * diamond + (1.0 - crease) * soft
        dr += float(ori["depth_mm"]) * val

    cel = textures["cellular"]
    if cel["enabled"] and abs(cel["depth_mm"]) > 1e-9:
        s_ang = float(cel["scale_angular"])
        s_vert = max(float(cel["scale_vertical_mm"]), 1.0)
        octaves = int(cel["octaves"])
        seed = int(cel["seed"])
        ridge = bool(cel["ridge_mode"])

        cyl_scale = s_ang / (2.0 * math.pi) * 4.0
        cx = np.cos(theta_g) * cyl_scale
        cy = np.sin(theta_g) * cyl_scale
        cz = z_grid / s_vert

        n = _value_noise_3d(cx, cy, cz, octaves, seed)
        val = (1.0 - 2.0 * np.abs(n - 0.5)) if ridge else (2.0 * (n - 0.5))
        dr += float(cel["depth_mm"]) * val

    return dr


def evaluate_radius_grid(
    params: dict[str, Any],
    n_z: int | None = None,
    n_theta: int | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate outer vase surface radius grid (z_vals, theta_vals, radii_grid)."""
    p = normalize_params(params)
    nz = max(2, int(n_z)) if n_z is not None else int(p["resolution_vertical"])
    nt = max(3, int(n_theta)) if n_theta is not None else int(p["resolution_angular"])

    height_mm = float(p["height_mm"])
    z_vals = np.linspace(0.0, height_mm, nz, dtype=np.float64)
    z_norm = z_vals / height_mm
    theta_vals = np.linspace(0.0, 2.0 * math.pi, nt, endpoint=False, dtype=np.float64)

    # 1. Base silhouette R_base(z_norm) via monotone PCHIP
    knot_x, knot_r = _prepare_knots(p)
    r_base_1d = _pchip_interpolate(knot_x, knot_r, z_norm)

    z_grid = z_vals[:, None]
    z_norm_grid = z_norm[:, None]
    theta_grid = theta_vals[None, :]

    global_twist_rad = math.radians(float(p["global_twist_deg"]))
    theta_g = theta_grid + global_twist_rad * z_norm_grid

    # 2. Polygonal cross-section factor
    n_sides = int(p["polygon_sides"])
    if n_sides >= 3:
        alpha = math.pi / float(n_sides)
        two_alpha = 2.0 * alpha
        sector = np.mod(np.mod(theta_g, two_alpha) + two_alpha, two_alpha) - alpha
        poly_scale = math.cos(alpha) / np.cos(sector)
        roundness = float(p["polygon_roundness"])
        r_prof = r_base_1d[:, None] * ((1.0 - roundness) * poly_scale + roundness * 1.0)
    else:
        r_prof = np.broadcast_to(r_base_1d[:, None], (nz, nt)).copy()

    # 3. Vertical texture fade envelope E(z) (forced 0.0 at z == 0 for flat bed contact)
    bfade = float(p["bottom_fade_mm"])
    tfade = float(p["top_fade_mm"])
    if bfade <= 0.01:
        e_bot = np.where(z_vals > 1e-9, 1.0, 0.0)
    else:
        e_bot = _smoothstep(0.0, bfade, z_vals)
        e_bot[0] = 0.0

    if tfade <= 0.01:
        e_top = np.ones_like(z_vals)
    else:
        e_top = _smoothstep(0.0, tfade, height_mm - z_vals)

    env = (e_bot * e_top)[:, None]

    # 4. Combinable surface textures
    dr = _compute_texture_displacement(
        z_grid=z_grid,
        z_norm_grid=z_norm_grid,
        theta_grid=theta_grid,
        theta_g=theta_g,
        textures=p["textures"],
        global_twist_rad=global_twist_rad,
    )

    radii = np.maximum(6.0, r_prof + env * dr)

    # 5. Optional overhang slope clamping (2-pass 1D Lipschitz projection)
    if p["auto_clamp_overhang"] and nz >= 2:
        dz = height_mm / float(nz - 1)
        max_dr = dz * math.tan(math.radians(float(p["max_safe_overhang_deg"])))
        for i in range(nz - 1):
            radii[i + 1] = np.clip(radii[i + 1], radii[i] - max_dr, radii[i] + max_dr)
        for i in range(nz - 2, -1, -1):
            radii[i] = np.clip(radii[i], radii[i + 1] - max_dr, radii[i + 1] + max_dr)
        radii = np.maximum(6.0, radii)

    return z_vals, theta_vals, radii


# ---------------------------------------------------------------------------
# Watertight 2-Manifold Mesh Construction Primitives
# ---------------------------------------------------------------------------

class _MeshBuilder:
    """Collects indexed vertices and CCW outward-facing triangles."""

    def __init__(self) -> None:
        self._verts_chunks: list[np.ndarray] = []
        self._tris_chunks: list[np.ndarray] = []
        self._v_count: int = 0

    @property
    def vertex_count(self) -> int:
        return self._v_count

    def add_vertices(self, pts: np.ndarray) -> np.ndarray:
        arr = np.asarray(pts, dtype=np.float64)
        if arr.ndim == 1:
            arr = arr[None, :]
        n = arr.shape[0]
        start = self._v_count
        self._verts_chunks.append(arr)
        self._v_count += n
        return np.arange(start, start + n, dtype=np.int32)

    def add_vertex(self, x: float, y: float, z: float) -> int:
        idx = self._v_count
        self._verts_chunks.append(np.array([[x, y, z]], dtype=np.float64))
        self._v_count += 1
        return idx

    def add_polar_ring(self, radii: np.ndarray | float, thetas: np.ndarray, z: float | np.ndarray) -> np.ndarray:
        r_arr = np.broadcast_to(np.asarray(radii, dtype=np.float64), thetas.shape)
        z_arr = np.broadcast_to(np.asarray(z, dtype=np.float64), thetas.shape)
        pts = np.column_stack((r_arr * np.cos(thetas), r_arr * np.sin(thetas), z_arr))
        return self.add_vertices(pts)

    def add_circle_ring(self, cx: float, cy: float, radius: float, z: float, count: int) -> np.ndarray:
        phis = np.linspace(0.0, 2.0 * math.pi, count, endpoint=False, dtype=np.float64)
        pts = np.column_stack((cx + radius * np.cos(phis), cy + radius * np.sin(phis), np.full(count, z, dtype=np.float64)))
        return self.add_vertices(pts)

    def add_triangles(self, tris: np.ndarray) -> None:
        arr = np.asarray(tris, dtype=np.int32)
        if arr.size > 0:
            self._tris_chunks.append(arr.reshape(-1, 3))

    def add_quad_strip(self, ring_a: np.ndarray, ring_b: np.ndarray, reverse: bool = False) -> None:
        """Connect two equal-length closed CCW rings.

        With reverse=False, normal is (+dz * r_hat - dr * z_hat):
        - upward outer wall (dz > 0) -> outward (+r_hat)
        - inward top rim (dr < 0) -> upward (+z_hat)
        - downward inner cavity wall (dz < 0) -> inward (-r_hat)
        """
        a0 = ring_a
        a1 = np.roll(ring_a, -1)
        b0 = ring_b
        b1 = np.roll(ring_b, -1)
        if not reverse:
            t1 = np.column_stack((a0, a1, b1))
            t2 = np.column_stack((a0, b1, b0))
        else:
            t1 = np.column_stack((a0, b1, a1))
            t2 = np.column_stack((a0, b0, b1))
        self.add_triangles(np.vstack((t1, t2)))

    def add_tube_grid(self, rings: list[np.ndarray], reverse: bool = False) -> None:
        """Vectorized quad-strip across an ordered sequence of equal-length rings."""
        arr = np.asarray(rings, dtype=np.int32)  # (S, M)
        a0 = arr[:-1, :]
        a1 = np.roll(a0, -1, axis=1)
        b0 = arr[1:, :]
        b1 = np.roll(b0, -1, axis=1)
        if not reverse:
            t1 = np.stack((a0, a1, b1), axis=-1).reshape(-1, 3)
            t2 = np.stack((a0, b1, b0), axis=-1).reshape(-1, 3)
        else:
            t1 = np.stack((a0, b1, a1), axis=-1).reshape(-1, 3)
            t2 = np.stack((a0, b0, b1), axis=-1).reshape(-1, 3)
        self.add_triangles(np.vstack((t1, t2)))

    def add_disk_fan(self, center_idx: int, ring: np.ndarray, normal_up: bool = True) -> None:
        m = len(ring)
        c = np.full(m, center_idx, dtype=np.int32)
        r0 = ring
        r1 = np.roll(ring, -1)
        if normal_up:
            tris = np.column_stack((c, r0, r1))
        else:
            tris = np.column_stack((c, r1, r0))
        self.add_triangles(tris)

    def get_vertices_array(self) -> np.ndarray:
        if not self._verts_chunks:
            return np.zeros((0, 3), dtype=np.float64)
        return np.vstack(self._verts_chunks)

    def build(self) -> MeshData:
        verts64 = self.get_vertices_array()
        tris = np.vstack(self._tris_chunks).astype(np.int32) if self._tris_chunks else np.zeros((0, 3), dtype=np.int32)

        # Anchor min Z cleanly at exact 0.0 in float32
        z_min = float(verts64[:, 2].min()) if len(verts64) else 0.0
        verts64[:, 2] -= z_min
        verts64[np.abs(verts64[:, 2]) < 1e-7, 2] = 0.0

        verts32 = verts64.astype(np.float32)
        if len(verts32):
            z_min32 = float(verts32[:, 2].min())
            if z_min32 != 0.0:
                verts32[:, 2] -= np.float32(z_min32)
            verts32[np.abs(verts32[:, 2]) < 1e-7, 2] = np.float32(0.0)

        # Compute exact face normals & signed volume from float32 vertex positions
        v0 = verts32[tris[:, 0]].astype(np.float64)
        v1 = verts32[tris[:, 1]].astype(np.float64)
        v2 = verts32[tris[:, 2]].astype(np.float64)

        cross = np.cross(v1 - v0, v2 - v0)
        norms = np.linalg.norm(cross, axis=1, keepdims=True)
        face_normals = (cross / np.maximum(norms, 1e-30)).astype(np.float32)

        signed_vol_mm3 = float(np.sum(np.einsum("ij,ij->i", v0, cross)) / 6.0)
        volume_cm3 = signed_vol_mm3 / 1000.0

        vmin = verts32.min(axis=0)
        vmax = verts32.max(axis=0)
        vsize = vmax - vmin
        bounds_mm = {
            "min": [float(vmin[0]), float(vmin[1]), float(vmin[2])],
            "max": [float(vmax[0]), float(vmax[1]), float(vmax[2])],
            "size": [float(vsize[0]), float(vsize[1]), float(vsize[2])],
        }

        return MeshData(
            vertices=verts32,
            triangles=tris,
            face_normals=face_normals,
            bounds_mm=bounds_mm,
            volume_cm3=float(volume_cm3),
        )


def _bridge_closed_loops_up(
    verts_xy: np.ndarray,
    loop_in: list[int] | np.ndarray,
    loop_out: list[int] | np.ndarray,
    center_xy: tuple[float, float],
) -> np.ndarray:
    """Triangulate the annular region between two star-shaped closed CCW loops (normal +Z).

    Guarantees:
    - Outer loop edges emitted once as (O_q, O_{q+1})
    - Inner loop edges emitted once as (I_{p+1}, I_p)
    - Every internal spoke emitted once forward and once backward (strict 2-manifold)
    """
    lin = [int(i) for i in loop_in]
    lout = [int(i) for i in loop_out]
    m1 = len(lin)
    m2 = len(lout)
    cx, cy = center_xy

    ang_in: list[float] = []
    for p, idx in enumerate(lin):
        a = math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        if p > 0:
            while a <= ang_in[-1]:
                a += 2.0 * math.pi
        ang_in.append(a)
    ang_in.append(ang_in[0] + 2.0 * math.pi)

    raw_out = [
        math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        for idx in lout
    ]
    best_s = min(
        range(m2),
        key=lambda s: abs(((raw_out[s] - ang_in[0] + math.pi) % (2.0 * math.pi)) - math.pi),
    )
    lout = lout[best_s:] + lout[:best_s]

    a0 = math.atan2(float(verts_xy[lout[0], 1]) - cy, float(verts_xy[lout[0], 0]) - cx)
    while a0 - ang_in[0] > math.pi:
        a0 -= 2.0 * math.pi
    while ang_in[0] - a0 > math.pi:
        a0 += 2.0 * math.pi

    ang_out: list[float] = [a0]
    for q in range(1, m2):
        idx = lout[q]
        a = math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        while a <= ang_out[-1]:
            a += 2.0 * math.pi
        ang_out.append(a)
    ang_out.append(ang_out[0] + 2.0 * math.pi)

    tris: list[tuple[int, int, int]] = []
    p = 0
    q = 0

    while p < m1 or q < m2:
        if p == m1:
            advance_out = True
        elif q == m2:
            advance_out = False
        else:
            skew_if_in = abs(ang_in[p + 1] - ang_out[q])
            skew_if_out = abs(ang_out[q + 1] - ang_in[p])
            advance_out = skew_if_out < skew_if_in

        if advance_out:
            tris.append((lin[p % m1], lout[q % m2], lout[(q + 1) % m2]))
            q += 1
        else:
            tris.append((lin[p % m1], lout[q % m2], lin[(p + 1) % m1]))
            p += 1

    return np.array(tris, dtype=np.int32)


def _drainage_zone_radii(r_avail: float) -> tuple[float, float]:
    """Return (r_collar, r_guard) strictly inside r_avail with guaranteed manifold margins."""
    r_av = max(2.2, float(r_avail))
    safe_margin = max(0.35, 0.10 * r_av)
    r_usable = max(1.2, r_av - safe_margin)
    r_guard = min(r_av - 0.15, max(r_usable + 0.10, r_av - 0.50 * safe_margin))
    r_collar = 0.92 * r_usable
    return r_collar, r_guard


def _compute_drainage_layout(
    drainage_cfg: dict[str, Any],
    r_avail: float,
) -> list[tuple[float, float, float]]:
    """Compute safe non-overlapping (cx, cy, r_hole) list for 1..9 holes inside r_avail."""
    k = int(drainage_cfg["hole_count"])
    req_r = 0.5 * float(drainage_cfg["hole_diameter_mm"])
    req_ratio = float(drainage_cfg["ring_radius_ratio"])
    r_collar, _ = _drainage_zone_radii(r_avail)

    if k <= 1:
        max_safe_r = 0.68 * r_collar
        r_h = max(0.20, min(req_r, max_safe_r))
        return [(0.0, 0.0, min(r_h, max_safe_r))]

    if k == 2:
        eff_ratio = req_ratio if req_ratio >= 0.15 else 0.45
        r_ring = min(max(0.36 * r_collar, eff_ratio * r_avail), 0.68 * r_collar)
        max_safe_r = 0.60 * min(r_ring, r_collar - r_ring)
        r_h = max(0.18, min(req_r, max_safe_r))
        r_h = min(r_h, max_safe_r)
        return [(r_ring, 0.0, r_h), (-r_ring, 0.0, r_h)]

    eff_ratio = req_ratio if req_ratio >= 0.15 else 0.48
    r_ring = min(max(0.42 * r_collar, eff_ratio * r_avail), 0.72 * r_collar)
    dpsi = math.pi / float(k)
    r_hub = 0.32 * r_ring
    max_safe_r = 0.60 * min(r_ring * math.sin(dpsi), r_ring - r_hub, r_collar - r_ring)
    r_h = max(0.18, min(req_r, max_safe_r))
    r_h = min(r_h, max_safe_r)

    holes: list[tuple[float, float, float]] = []
    for c in range(k):
        psi = 2.0 * math.pi * float(c) / float(k)
        holes.append((r_ring * math.cos(psi), r_ring * math.sin(psi), r_h))
    return holes


def _add_planar_disk_with_holes(
    mb: _MeshBuilder,
    outer_ring: np.ndarray,
    z_plane: float,
    holes: list[tuple[float, float, float]],
    r_avail: float,
    normal_up: bool,
    m_hole: int = 32,
) -> list[np.ndarray]:
    """Triangulate a planar disk bounded by outer_ring with 0..9 circular holes.

    Uses a radial polar guard ring + strictly convex sector decomposition + loop bridging
    so zero triangles can flip or degenerate even on sharp polygonal/textured profiles
    or 25 mm walls with 9 holes, and every shared edge is traversed once in each direction.
    """
    k = len(holes)
    if k == 0:
        c_idx = mb.add_vertex(0.0, 0.0, z_plane)
        mb.add_disk_fan(c_idx, outer_ring, normal_up=normal_up)
        return []

    r_collar, r_guard = _drainage_zone_radii(r_avail)

    # Project outer_ring radially onto a pure circular guard_ring at r_guard < r_avail
    verts_init = mb.get_vertices_array()
    outer_xy = verts_init[outer_ring, :2]
    outer_norms = np.maximum(np.hypot(outer_xy[:, 0], outer_xy[:, 1]), 1e-9)
    guard_pts = np.column_stack((
        (r_guard / outer_norms) * outer_xy[:, 0],
        (r_guard / outer_norms) * outer_xy[:, 1],
        np.full(len(outer_ring), z_plane, dtype=np.float64),
    ))
    guard_ring = mb.add_vertices(guard_pts)

    o0 = np.asarray(outer_ring, dtype=np.int32)
    o1 = np.roll(o0, -1)
    g0 = guard_ring
    g1 = np.roll(g0, -1)

    hole_rings: list[np.ndarray] = [
        mb.add_circle_ring(cx, cy, rh, z_plane, m_hole)
        for (cx, cy, rh) in holes
    ]

    tris_list: list[np.ndarray] = [
        np.vstack((
            np.column_stack((o0, o1, g1)),
            np.column_stack((o0, g1, g0)),
        ))
    ]

    if k == 1:
        verts_xy = mb.get_vertices_array()[:, :2]
        cx, cy, _ = holes[0]
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[0], guard_ring, (cx, cy)))

    elif k == 2:
        m_semi = 24
        n_diam = 16
        bot_pole = mb.add_vertex(0.0, -r_collar, z_plane)
        top_pole = mb.add_vertex(0.0, r_collar, z_plane)

        right_angs = np.linspace(-0.5 * math.pi, 0.5 * math.pi, m_semi + 1, dtype=np.float64)[1:-1]
        right_semi = mb.add_vertices(
            np.column_stack((r_collar * np.cos(right_angs), r_collar * np.sin(right_angs), np.full(len(right_angs), z_plane)))
        )

        left_angs = np.linspace(0.5 * math.pi, 1.5 * math.pi, m_semi + 1, dtype=np.float64)[1:-1]
        left_semi = mb.add_vertices(
            np.column_stack((r_collar * np.cos(left_angs), r_collar * np.sin(left_angs), np.full(len(left_angs), z_plane)))
        )

        diam_ys = np.linspace(-r_collar, r_collar, n_diam + 1, dtype=np.float64)[1:-1]
        diam_mid = mb.add_vertices(
            np.column_stack((np.zeros(len(diam_ys)), diam_ys, np.full(len(diam_ys), z_plane)))
        )

        # Right half-disk CCW around (+r_ring, 0)
        cell_0 = [bot_pole, *right_semi.tolist(), top_pole, *diam_mid[::-1].tolist()]
        # Left half-disk CCW around (-r_ring, 0)
        cell_1 = [top_pole, *left_semi.tolist(), bot_pole, *diam_mid.tolist()]
        # Full collar loop CCW around (0, 0)
        collar_ring = [bot_pole, *right_semi.tolist(), top_pole, *left_semi.tolist()]

        verts_xy = mb.get_vertices_array()[:, :2]
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[0], cell_0, (holes[0][0], holes[0][1])))
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[1], cell_1, (holes[1][0], holes[1][1])))
        tris_list.append(_bridge_closed_loops_up(verts_xy, collar_ring, guard_ring, (0.0, 0.0)))

    else:
        r_ring = math.hypot(holes[0][0], holes[0][1])
        dpsi = math.pi / float(k)
        r_hub = 0.32 * r_ring

        n_spoke = 14
        n_chord = 6
        m_arc = max(12, int(round(64.0 / float(k))))

        spoke_angs = [2.0 * math.pi * float(c) / float(k) - dpsi for c in range(k)]
        spoke_radii = np.linspace(r_hub, r_collar, n_spoke + 1, dtype=np.float64)

        spokes: list[np.ndarray] = []
        for ang in spoke_angs:
            pts = np.column_stack((
                spoke_radii * math.cos(ang),
                spoke_radii * math.sin(ang),
                np.full(len(spoke_radii), z_plane),
            ))
            spokes.append(mb.add_vertices(pts))

        verts_so_far = mb.get_vertices_array()
        chord_interiors: list[np.ndarray] = []
        arc_interiors: list[np.ndarray] = []
        t_chord = np.linspace(0.0, 1.0, n_chord + 1, dtype=np.float64)[1:-1][:, None]
        for c in range(k):
            c_next = (c + 1) % k
            u0 = verts_so_far[spokes[c][0]]
            u1 = verts_so_far[spokes[c_next][0]]
            c_pts = u0[None, :] + t_chord * (u1 - u0)[None, :]
            c_pts[:, 2] = z_plane
            chord_interiors.append(mb.add_vertices(c_pts))

            ang0 = spoke_angs[c]
            ang1 = ang0 + 2.0 * dpsi
            a_pts = np.linspace(ang0, ang1, m_arc + 1, dtype=np.float64)[1:-1]
            arc_interiors.append(
                mb.add_vertices(
                    np.column_stack((r_collar * np.cos(a_pts), r_collar * np.sin(a_pts), np.full(len(a_pts), z_plane)))
                )
            )

        # Center hub k-gon fan (+Z first; flipped at end if not normal_up)
        hub_center = mb.add_vertex(0.0, 0.0, z_plane)
        hub_loop: list[int] = []
        for c in range(k):
            hub_loop.append(int(spokes[c][0]))
            hub_loop.extend(chord_interiors[c].tolist())
        hc = np.full(len(hub_loop), hub_center, dtype=np.int32)
        hr0 = np.array(hub_loop, dtype=np.int32)
        hr1 = np.roll(hr0, -1)
        tris_list.append(np.column_stack((hc, hr0, hr1)))

        collar_ring = []
        for c in range(k):
            collar_ring.append(int(spokes[c][-1]))
            collar_ring.extend(arc_interiors[c].tolist())

        verts_xy = mb.get_vertices_array()[:, :2]
        for c in range(k):
            c_next = (c + 1) % k
            cell_loop: list[int] = [
                *spokes[c][:-1].tolist(),              # U_c .. before W_c (outward)
                int(spokes[c][-1]),                    # W_c
                *arc_interiors[c].tolist(),            # collar arc CCW
                *spokes[c_next][::-1][:-1].tolist(),   # W_{c+1} .. before U_{c+1} (inward)
                int(spokes[c_next][0]),                # U_{c+1}
                *chord_interiors[c][::-1].tolist(),    # inner chord back toward U_c
            ]
            tris_list.append(
                _bridge_closed_loops_up(verts_xy, hole_rings[c], cell_loop, (holes[c][0], holes[c][1]))
            )

        tris_list.append(_bridge_closed_loops_up(verts_xy, collar_ring, guard_ring, (0.0, 0.0)))

    all_tris = np.vstack(tris_list)
    if not normal_up:
        all_tris = all_tris[:, [0, 2, 1]]
    mb.add_triangles(all_tris)
    return hole_rings


# ---------------------------------------------------------------------------
# Public Mesh Generators (Section 3)
# ---------------------------------------------------------------------------

def generate_vase_mesh(params: dict[str, Any], layer_height_mm: float = 0.2) -> MeshData:
    """Generate a 100% closed, watertight 2-manifold vase mesh for spiral_vase or shelled_hollow."""
    p = normalize_params(params)
    lh = max(0.05, min(1.0, float(layer_height_mm)))
    z_vals, theta_vals, radii_grid = evaluate_radius_grid(p)
    nz, _ = radii_grid.shape
    height_mm = float(p["height_mm"])

    mb = _MeshBuilder()
    drain_cfg = p["drainage"]
    drain_enabled = bool(drain_cfg["enabled"])

    if p["print_mode"] == "spiral_vase":
        # Outer wall rings from Z = 0 to Z = height_mm
        outer_rings: list[np.ndarray] = [
            mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i]))
            for i in range(nz)
        ]
        mb.add_tube_grid(outer_rings, reverse=False)

        # Top solid cap at Z = height_mm (+Z normal)
        top_center = mb.add_vertex(0.0, 0.0, height_mm)
        mb.add_disk_fan(top_center, outer_rings[-1], normal_up=True)

        # Bottom cap at Z = 0.0 (-Z normal), with optional blind drainage cavities
        if not drain_enabled:
            bot_center = mb.add_vertex(0.0, 0.0, 0.0)
            mb.add_disk_fan(bot_center, outer_rings[0], normal_up=False)
        else:
            z_cap = min(
                float(p["spiral_bottom_layers"]) * lh + 0.30,
                0.34 * height_mm,
            )
            z_cap = max(0.45, z_cap)
            sub_cap_mask = z_vals <= (z_cap + 1e-3)
            r_avail = float(radii_grid[sub_cap_mask].min()) if np.any(sub_cap_mask) else float(radii_grid[0].min())
            holes = _compute_drainage_layout(drain_cfg, r_avail)
            bot_hole_rings = _add_planar_disk_with_holes(
                mb=mb,
                outer_ring=outer_rings[0],
                z_plane=0.0,
                holes=holes,
                r_avail=r_avail,
                normal_up=False,
            )
            m_hole = len(bot_hole_rings[0])
            for idx_h, (cx, cy, rh) in enumerate(holes):
                top_hole_ring = mb.add_circle_ring(cx, cy, rh, z_cap, m_hole)
                # Tunnel wall facing inward into blind cavity (reverse=True)
                mb.add_quad_strip(bot_hole_rings[idx_h], top_hole_ring, reverse=True)
                # Blind cavity ceiling facing -Z into cavity
                roof_center = mb.add_vertex(cx, cy, z_cap)
                mb.add_disk_fan(roof_center, top_hole_ring, normal_up=False)

        return mb.build()

    # Mode 2: shelled_hollow (true thick-walled hollow shell with optional lip bevel & through-drainage)
    wall_t = float(p["wall_thickness_mm"])
    effective_bottom = min(float(p["bottom_thickness_mm"]), height_mm * 0.65)
    z_floor = max(1.0, effective_bottom)

    if nz >= 5:
        r_for_slope = (
            0.25 * np.vstack((radii_grid[0:1], radii_grid[:-1]))
            + 0.50 * radii_grid
            + 0.25 * np.vstack((radii_grid[1:], radii_grid[-1:]))
        )
    else:
        r_for_slope = radii_grid
    slope_z = np.gradient(r_for_slope, z_vals, axis=0)
    slope_z = np.clip(slope_z, -1.75, 1.75)
    extra_radial = np.minimum(wall_t * (np.sqrt(1.0 + slope_z * slope_z) - 1.0), 8.0)
    radial_wall = wall_t + extra_radial

    # Smooth C1 clamp above min_inner_r = 3.0 mm so narrow waists with 25 mm walls never invert or crease
    min_inner_r = 3.0
    min_wall_gap = min(0.65, 0.80 * wall_t)
    delta_in = (radii_grid - radial_wall) - min_inner_r
    inner_grid = min_inner_r + 0.5 * (delta_in + np.sqrt(delta_in * delta_in + 0.16))
    inner_grid = np.minimum(inner_grid, radii_grid - min_wall_gap)
    inner_grid = np.maximum(min_inner_r, inner_grid)

    if p["auto_clamp_overhang"] and nz >= 2:
        dz = height_mm / float(nz - 1)
        max_dr = dz * math.tan(math.radians(float(p["max_safe_overhang_deg"])))
        for i in range(nz - 1):
            inner_grid[i + 1] = np.clip(inner_grid[i + 1], inner_grid[i] - max_dr, inner_grid[i] + max_dr)
        for i in range(nz - 2, -1, -1):
            inner_grid[i] = np.clip(inner_grid[i], inner_grid[i + 1] - max_dr, inner_grid[i + 1] + max_dr)
        inner_grid = np.minimum(inner_grid, radii_grid - min_wall_gap)
        inner_grid = np.maximum(min_inner_r, inner_grid)

    # Determine safe lip bevel radius
    top_wall_span = float(np.min(radii_grid[-1] - inner_grid[-1]))
    bevel = min(
        float(p["lip_bevel_mm"]),
        0.42 * max(0.0, top_wall_span),
        0.15 * (height_mm - z_floor),
    )

    profile_rings: list[np.ndarray] = []

    if bevel > 0.08:
        z_lip_base = height_mm - bevel
        # Outer wall up to z_lip_base (keep >= 0.05 mm Z margin so adjacent rings never quantize-collapse)
        outer_mask = z_vals < (z_lip_base - 0.05)
        for i in np.nonzero(outer_mask)[0]:
            profile_rings.append(mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i])))

        # Interpolate outer & inner radii cleanly at z_lip_base
        r_out_lip = np.array([np.interp(z_lip_base, z_vals, radii_grid[:, j]) for j in range(len(theta_vals))])
        r_in_lip = np.array([np.interp(z_lip_base, z_vals, inner_grid[:, j]) for j in range(len(theta_vals))])
        r_in_lip = np.minimum(r_in_lip, r_out_lip - min_wall_gap)
        r_in_lip = np.maximum(min_inner_r, r_in_lip)

        r_mid = 0.5 * (r_out_lip + r_in_lip)
        half_w = 0.5 * (r_out_lip - r_in_lip)

        # Semicircular lip arch peaking at exact Z = height_mm (gamma = pi/2)
        for gamma in (0.0, 0.25 * math.pi, 0.5 * math.pi, 0.75 * math.pi, math.pi):
            z_a = height_mm if abs(gamma - 0.5 * math.pi) < 1e-9 else (z_lip_base + bevel * math.sin(gamma))
            r_a = r_mid + half_w * math.cos(gamma)
            profile_rings.append(mb.add_polar_ring(r_a, theta_vals, z_a))

        z_inner_top = z_lip_base
    else:
        for i in range(nz):
            profile_rings.append(mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i])))
        profile_rings.append(mb.add_polar_ring(inner_grid[-1], theta_vals, height_mm))
        z_inner_top = height_mm

    # Inner cavity wall descending from below z_inner_top down to z_floor
    inner_mask = (z_vals < z_inner_top - 0.05) & (z_vals > z_floor + 0.05)
    for i in np.nonzero(inner_mask)[0][::-1]:
        profile_rings.append(mb.add_polar_ring(inner_grid[i], theta_vals, float(z_vals[i])))

    r_in_floor = np.array([np.interp(z_floor, z_vals, inner_grid[:, j]) for j in range(len(theta_vals))])
    r_in_floor = np.maximum(min_inner_r, r_in_floor)
    profile_rings.append(mb.add_polar_ring(r_in_floor, theta_vals, z_floor))

    # Connect continuous meridian revolution (outer wall -> lip -> inner cavity wall)
    mb.add_tube_grid(profile_rings, reverse=False)

    outer_bot_ring = profile_rings[0]
    inner_floor_ring = profile_rings[-1]

    if not drain_enabled:
        bot_center = mb.add_vertex(0.0, 0.0, 0.0)
        mb.add_disk_fan(bot_center, outer_bot_ring, normal_up=False)

        floor_center = mb.add_vertex(0.0, 0.0, z_floor)
        mb.add_disk_fan(floor_center, inner_floor_ring, normal_up=True)
    else:
        sub_floor_mask = z_vals <= (z_floor + 1e-3)
        min_outer_below_floor = (
            float(radii_grid[sub_floor_mask].min())
            if np.any(sub_floor_mask)
            else float(radii_grid[0].min())
        )
        r_avail = max(min_inner_r, float(min(min_outer_below_floor - min_wall_gap, r_in_floor.min())))
        holes = _compute_drainage_layout(drain_cfg, r_avail)

        bot_hole_rings = _add_planar_disk_with_holes(
            mb=mb,
            outer_ring=outer_bot_ring,
            z_plane=0.0,
            holes=holes,
            r_avail=r_avail,
            normal_up=False,
        )
        top_hole_rings = _add_planar_disk_with_holes(
            mb=mb,
            outer_ring=inner_floor_ring,
            z_plane=z_floor,
            holes=holes,
            r_avail=r_avail,
            normal_up=True,
        )
        for idx_h in range(len(holes)):
            mb.add_quad_strip(bot_hole_rings[idx_h], top_hole_rings[idx_h], reverse=True)

    return mb.build()


def generate_saucer_mesh(params: dict[str, Any]) -> MeshData:
    """Generate a watertight 2-manifold matching plant saucer tray centered at (0, 0), min(Z) == 0.0."""
    p = normalize_params(params)
    sc = p["saucer"]

    nt = max(96, min(240, int(p["resolution_angular"])))
    theta_vals = np.linspace(0.0, 2.0 * math.pi, nt, endpoint=False, dtype=np.float64)

    # Account for custom profile or polygonal vase base radius so the vase always fits comfortably
    _, _, vase_base_radii = evaluate_radius_grid(p, n_z=12, n_theta=nt)
    vase_foot_radius = max(0.5 * float(p["base_diameter_mm"]), float(vase_base_radii[0].max()))

    r_saucer_inner = vase_foot_radius + float(sc["clearance_mm"])
    rim_h = float(sc["rim_height_mm"])
    wall_t = float(sc["wall_thickness_mm"])
    floor_t = min(float(sc["floor_thickness_mm"]), rim_h - 3.0)
    floor_t = max(1.2, floor_t)
    ribs_h = min(float(sc["inner_ribs_height_mm"]), 0.45 * (rim_h - floor_t))
    ribs_h = max(0.0, ribs_h)

    flare_tan = math.tan(math.radians(12.0))
    n_wall = 28
    z_out = np.linspace(0.0, rim_h, n_wall, dtype=np.float64)
    z_out_norm = z_out / max(rim_h, 1.0)

    r_out_base = (r_saucer_inner + wall_t) + z_out * flare_tan
    r_out_grid = np.broadcast_to(r_out_base[:, None], (n_wall, nt)).copy()

    # Optional matching outer vase texture with clean bed/rim fade
    if sc["match_vase_texture"]:
        e_bot = _smoothstep(0.0, min(3.5, 0.25 * rim_h), z_out)
        e_bot[0] = 0.0
        e_top = _smoothstep(0.0, min(3.0, 0.22 * rim_h), rim_h - z_out)
        env = (e_bot * e_top)[:, None]

        twist_rad = math.radians(float(p["global_twist_deg"])) * 0.25
        theta_g = theta_vals[None, :] + twist_rad * z_out_norm[:, None]
        dr_tex = _compute_texture_displacement(
            z_grid=z_out[:, None],
            z_norm_grid=z_out_norm[:, None],
            theta_grid=theta_vals[None, :],
            theta_g=theta_g,
            textures=p["textures"],
            global_twist_rad=twist_rad,
        )
        max_tex = 0.45 * wall_t
        r_out_grid += env * np.clip(0.40 * dr_tex, -max_tex, max_tex)

    mb = _MeshBuilder()
    rings: list[np.ndarray] = []

    # 1. Outer flared wall from Z = 0 up to Z = rim_h - bevel
    lip_r = 0.5 * wall_t
    z_arch_base = max(floor_t + 1.0, rim_h - lip_r)
    for i in range(n_wall):
        if z_out[i] < z_arch_base - 1e-4:
            rings.append(mb.add_polar_ring(r_out_grid[i], theta_vals, float(z_out[i])))

    # 2. Smooth rounded top rim peaking at exact Z = rim_h
    r_outer_top = np.array([np.interp(z_arch_base, z_out, r_out_grid[:, j]) for j in range(nt)])
    r_inner_top = np.full(nt, r_saucer_inner + (z_arch_base - floor_t) * flare_tan, dtype=np.float64)
    r_inner_top = np.minimum(r_inner_top, r_outer_top - 0.6)

    r_mid = 0.5 * (r_outer_top + r_inner_top)
    half_w = 0.5 * (r_outer_top - r_inner_top)
    arch_h = rim_h - z_arch_base
    for gamma in (0.0, 0.25 * math.pi, 0.5 * math.pi, 0.75 * math.pi, math.pi):
        z_a = rim_h if abs(gamma - 0.5 * math.pi) < 1e-9 else (z_arch_base + arch_h * math.sin(gamma))
        r_a = r_mid + half_w * math.cos(gamma)
        rings.append(mb.add_polar_ring(r_a, theta_vals, z_a))

    # 3. Inner flared wall descending to inner floor edge (r_saucer_inner, floor_t)
    n_in_wall = 16
    z_in = np.linspace(z_arch_base, floor_t, n_in_wall, dtype=np.float64)[1:]
    for zv in z_in:
        r_v = r_saucer_inner + (zv - floor_t) * flare_tan
        rings.append(mb.add_polar_ring(r_v, theta_vals, float(zv)))

    # 4. Inner floor radial rings with raised drainage ribs so the pot sits above water
    n_floor_rings = 22
    r_floor_vals = np.linspace(r_saucer_inner, 0.06 * r_saucer_inner, n_floor_rings, dtype=np.float64)[1:]
    n_ribs = 8
    rib_ang_profile = np.maximum(0.0, np.cos(float(n_ribs) * theta_vals)) ** 2

    for rv in r_floor_vals:
        if ribs_h > 1e-4:
            u_rad = np.clip((rv - 0.16 * r_saucer_inner) / max(0.70 * r_saucer_inner, 1e-6), 0.0, 1.0)
            rib_env = math.sin(math.pi * float(u_rad)) ** 2
            z_ring = floor_t + ribs_h * rib_env * rib_ang_profile
        else:
            z_ring = floor_t
        rings.append(mb.add_polar_ring(rv, theta_vals, z_ring))

    mb.add_tube_grid(rings, reverse=False)

    # Bottom flat cap at Z = 0 (-Z normal) & inner floor center fan (+Z normal)
    bot_center = mb.add_vertex(0.0, 0.0, 0.0)
    mb.add_disk_fan(bot_center, rings[0], normal_up=False)

    top_center = mb.add_vertex(0.0, 0.0, floor_t)
    mb.add_disk_fan(top_center, rings[-1], normal_up=True)

    return mb.build()

# ===========================================================================
# MODULE: vase_studio.printability
# ===========================================================================

"""Printability, overhang, bed-fit, and filament weight analysis for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import math
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import os as _os
    from pathlib import Path as _Path
    import sys as _sys

    if _sys.platform == "win32":
        _appdata = _os.environ.get("APPDATA", "").strip()
        _orca_base = _Path(_appdata) / "OrcaSlicer" if _appdata else _Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    elif _sys.platform == "darwin":
        _orca_base = _Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    else:
        _xdg = _os.environ.get("XDG_CONFIG_HOME", "").strip()
        _orca_base = (_Path(_xdg) if _xdg else (_Path.home() / ".config")) / "OrcaSlicer"

    _orca_pkg_dir = str(_orca_base / "python" / "packages" / f"cp{_sys.version_info.major}{_sys.version_info.minor}")
    if _orca_pkg_dir not in _sys.path:
        _sys.path.insert(0, _orca_pkg_dir)
    import numpy as np

pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import

PLA_DENSITY_G_CM3 = 1.24


def _ctx_float(ctx: dict[str, Any], key: str, default: float, lo: float, hi: float) -> float:
    val = ctx.get(key, default)
    if isinstance(val, (list, tuple)) and len(val) > 0:
        val = val[0]
    if isinstance(val, str):
        val = val.strip().rstrip("%mM ").strip()
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f) or f <= 0.0:
        return default
    return max(lo, min(hi, f))


def analyze_printability(
    mesh: MeshData,
    params: dict[str, Any],
    host_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Analyze a generated mesh for overhangs, bed bounds, spiral vase gap risk, and PLA usage."""
    p = normalize_params(params)
    ctx = host_context if isinstance(host_context, dict) else {}

    bed_x = _ctx_float(ctx, "bed_x", 220.0, 50.0, 2000.0)
    bed_y = _ctx_float(ctx, "bed_y", 220.0, 50.0, 2000.0)
    max_z = _ctx_float(ctx, "max_z", 250.0, 50.0, 2000.0)
    nozzle_mm = _ctx_float(ctx, "nozzle_mm", 0.4, 0.15, 2.0)
    layer_h = _ctx_float(ctx, "layer_height_mm", 0.2, 0.04, 1.2)
    line_w = _ctx_float(ctx, "line_width_mm", 0.42, 0.15, 2.5)

    verts = np.asarray(mesh.vertices, dtype=np.float64)
    tris = np.asarray(mesh.triangles, dtype=np.int32)
    normals = np.asarray(mesh.face_normals, dtype=np.float64)
    tri_count = int(len(tris))

    size = mesh.bounds_mm.get("size", [0.0, 0.0, 0.0])
    dx = round(float(size[0]), 2)
    dy = round(float(size[1]), 2)
    dz = round(float(size[2]), 2)

    bed_shape = str(ctx.get("bed_shape") or "rectangular").strip().lower()
    if bed_shape == "circular":
        bed_diam = min(bed_x, bed_y)
        verts_xy_r = float(np.max(np.hypot(verts[:, 0], verts[:, 1]))) if len(verts) > 0 else 0.5 * max(dx, dy)
        fits_bed = bool(2.0 * verts_xy_r <= bed_diam + 1e-3 and max(dx, dy) <= bed_diam + 1e-3)
    else:
        fits_bed = bool(dx <= bed_x + 1e-3 and dy <= bed_y + 1e-3)
    fits_height = bool(dz <= max_z + 1e-3)

    if tri_count == 0 or len(verts) == 0:
        return {
            "max_overhang_deg": 0.0,
            "warning_faces_pct": 0.0,
            "critical_faces_pct": 0.0,
            "fits_bed": fits_bed,
            "fits_height": fits_height,
            "spiral_gap_risk": False,
            "estimated_weight_g": 0.0,
            "estimated_volume_cm3": 0.0,
            "dimensions_mm": [dx, dy, dz],
            "triangle_count": 0,
            "warnings": [],
        }

    v0 = verts[tris[:, 0]]
    v1 = verts[tris[:, 1]]
    v2 = verts[tris[:, 2]]
    face_areas = 0.5 * np.linalg.norm(np.cross(v1 - v0, v2 - v0), axis=1)

    face_z_max = np.maximum(np.maximum(v0[:, 2], v1[:, 2]), v2[:, 2])
    face_z_min = np.minimum(np.minimum(v0[:, 2], v1[:, 2]), v2[:, 2])
    nz = normals[:, 2]

    # Exclude flat bottom faces resting on bed Z == 0
    non_bed_mask = face_z_max > 1e-3

    # In spiral_vase mode, top cap and blind-drainage internal roof are unprinted slicing caps
    is_spiral = p["print_mode"] == "spiral_vase"
    if is_spiral:
        top_cap_mask = (face_z_min >= dz - 1e-2) & (nz > 0.999)
        eval_mask = non_bed_mask & (~top_cap_mask)
        if p["drainage"]["enabled"]:
            z_blind_cap = min(float(p["spiral_bottom_layers"]) * layer_h + 0.30, 0.34 * float(p["height_mm"]))
            blind_roof_mask = (face_z_max <= z_blind_cap + 0.08) & (nz < -0.999)
            eval_mask = eval_mask & (~blind_roof_mask)
    else:
        eval_mask = non_bed_mask

    downward_mask = eval_mask & (nz < -1e-4)
    overhang_deg = np.zeros(tri_count, dtype=np.float64)
    if np.any(downward_mask):
        overhang_deg[downward_mask] = np.degrees(np.arcsin(np.clip(-nz[downward_mask], 0.0, 1.0)))

    # Robust 99.8th area-weighted percentile avoids single microscopic facet spikes while catching real slopes;
    # still report true max on clean surfaces
    eval_areas = face_areas[eval_mask]
    total_eval_area = float(np.sum(eval_areas)) if eval_areas.size > 0 else 0.0

    max_overhang_deg = round(float(np.max(overhang_deg)), 1) if np.any(downward_mask) else 0.0
    if total_eval_area > 1e-6:
        warn_area = float(np.sum(face_areas[eval_mask & (overhang_deg > 45.0)]))
        crit_area = float(np.sum(face_areas[eval_mask & (overhang_deg > 55.0)]))
        warning_faces_pct = round(100.0 * warn_area / total_eval_area, 2)
        critical_faces_pct = round(100.0 * crit_area / total_eval_area, 2)
    else:
        warning_faces_pct = 0.0
        critical_faces_pct = 0.0

    # Spiral vase gap risk & realistic filament usage estimate
    eff_spiral_lw = float(p["spiral_line_width_mm"]) if p["auto_configure_slicer"] else line_w
    if is_spiral:
        horiz_step_mm = layer_h * math.tan(math.radians(min(max_overhang_deg, 84.0)))
        spiral_gap_risk = bool(
            (horiz_step_mm > 0.68 * eff_spiral_lw and warning_faces_pct > 0.25)
            or critical_faces_pct > 0.5
            or max_overhang_deg > 55.0
        )
        # Estimate actual printed shell volume (1 outer wall + bottom solid layers)
        bed_area_mm2 = float(np.sum(face_areas[~non_bed_mask]))
        wall_area_mm2 = total_eval_area
        bottom_h_mm = float(p["spiral_bottom_layers"]) * layer_h
        printed_vol_mm3 = wall_area_mm2 * eff_spiral_lw + bed_area_mm2 * bottom_h_mm
        est_vol_cm3 = max(0.5, min(float(mesh.volume_cm3), printed_vol_mm3 / 1000.0))
    else:
        spiral_gap_risk = False
        est_vol_cm3 = max(0.5, float(mesh.volume_cm3))

    est_vol_cm3 = round(est_vol_cm3, 2)
    est_weight_g = round(est_vol_cm3 * PLA_DENSITY_G_CM3, 1)

    warnings: list[dict[str, str]] = []

    if not fits_bed:
        warnings.append({
            "code": "BED_OVERFLOW",
            "pt": f"Dimensoes XY ({dx:.1f} x {dy:.1f} mm) excedem a mesa ({bed_x:.0f} x {bed_y:.0f} mm).",
            "en": f"XY dimensions ({dx:.1f} x {dy:.1f} mm) exceed build plate ({bed_x:.0f} x {bed_y:.0f} mm).",
        })

    if not fits_height:
        warnings.append({
            "code": "HEIGHT_OVERFLOW",
            "pt": f"Altura ({dz:.1f} mm) excede o limite Z da impressora ({max_z:.0f} mm).",
            "en": f"Height ({dz:.1f} mm) exceeds printer Z limit ({max_z:.0f} mm).",
        })

    if critical_faces_pct > 0.5 or max_overhang_deg > 55.0:
        warnings.append({
            "code": "CRITICAL_OVERHANG",
            "pt": (
                f"Overhang critico de {max_overhang_deg:.1f}° ({critical_faces_pct:.1f}% da parede > 55°). "
                "Ative 'Limitar Overhang Automaticamente' ou reduza a profundidade das texturas."
            ),
            "en": (
                f"Critical overhang of {max_overhang_deg:.1f}° ({critical_faces_pct:.1f}% of wall > 55°). "
                "Enable 'Auto-Clamp Overhang' or reduce texture depth."
            ),
        })
    elif warning_faces_pct > 1.0 or max_overhang_deg > 45.0:
        warnings.append({
            "code": "MODERATE_OVERHANG",
            "pt": f"Overhang moderado de {max_overhang_deg:.1f}° ({warning_faces_pct:.1f}% > 45°). Use boa ventilacao de camada.",
            "en": f"Moderate overhang of {max_overhang_deg:.1f}° ({warning_faces_pct:.1f}% > 45°). Ensure strong part cooling.",
        })

    if spiral_gap_risk:
        warnings.append({
            "code": "SPIRAL_GAP_RISK",
            "pt": (
                f"Risco de frestas no Modo Vaso Espiral (passo lateral > largura de linha {eff_spiral_lw:.2f} mm). "
                "Aumente a largura da parede espiral, reduza altura de camada ou mude para Parede Dupla."
            ),
            "en": (
                f"Gap risk in Spiral Vase mode (stepover exceeds {eff_spiral_lw:.2f} mm line width). "
                "Increase spiral line width, lower layer height, or switch to Shelled Hollow mode."
            ),
        })

    if is_spiral and eff_spiral_lw > 2.0 * nozzle_mm + 1e-4:
        warnings.append({
            "code": "LINE_WIDTH_HIGH",
            "pt": f"Largura espiral ({eff_spiral_lw:.2f} mm) acima de 2x o bico ({nozzle_mm:.2f} mm).",
            "en": f"Spiral line width ({eff_spiral_lw:.2f} mm) exceeds 2x nozzle diameter ({nozzle_mm:.2f} mm).",
        })

    if (not is_spiral) and float(p["wall_thickness_mm"]) < 2.0 * line_w - 1e-4:
        warnings.append({
            "code": "THIN_SHELL_WALL",
            "pt": f"Espessura da parede ({p['wall_thickness_mm']:.2f} mm) muito fina para perimetros duplos ({2.0 * line_w:.2f} mm).",
            "en": f"Wall thickness ({p['wall_thickness_mm']:.2f} mm) is thin for dual perimeters ({2.0 * line_w:.2f} mm).",
        })

    min_foot = max(1.0, min(dx, dy))
    if dz / min_foot > 3.2:
        warnings.append({
            "code": "TALL_SLENDER_RATIO",
            "pt": "Proporcao alta e estreita — considere adicionar Brim no OrcaSlicer para aderencia extra.",
            "en": "Tall slender aspect ratio — consider enabling a Brim in OrcaSlicer for extra bed adhesion.",
        })

    return {
        "max_overhang_deg": max_overhang_deg,
        "warning_faces_pct": warning_faces_pct,
        "critical_faces_pct": critical_faces_pct,
        "fits_bed": fits_bed,
        "fits_height": fits_height,
        "spiral_gap_risk": spiral_gap_risk,
        "estimated_weight_g": est_weight_g,
        "estimated_volume_cm3": est_vol_cm3,
        "dimensions_mm": [dx, dy, dz],
        "triangle_count": tri_count,
        "warnings": warnings,
    }

# ===========================================================================
# MODULE: vase_studio.exporters
# ===========================================================================

"""Binary STL and OrcaSlicer 2.5.1 3MF project exporters for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import datetime as _dt
import json
import math
import struct
import uuid
import zipfile
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape as _xml_escape

import numpy as np

_STL_RECORD_DTYPE = np.dtype(
    [
        ("normal", "<f4", (3,)),
        ("v0", "<f4", (3,)),
        ("v1", "<f4", (3,)),
        ("v2", "<f4", (3,)),
        ("attr", "<u2"),
    ]
)

_CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="config" ContentType="text/xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="json" ContentType="application/json"/>
</Types>
"""

_RELS_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>
"""


def _extract_mesh_arrays(mesh: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract validated (vertices, triangles, face_normals) arrays from duck-typed MeshData."""
    vertices = np.asarray(mesh.vertices, dtype=np.float32)
    if vertices.ndim != 2 or vertices.shape[1] != 3:
        raise ValueError(f"Expected vertices shape (V, 3), got {vertices.shape!r}")
    vertices = np.nan_to_num(vertices, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float32, copy=False)

    triangles = np.asarray(mesh.triangles, dtype=np.int32)
    if triangles.size == 0:
        triangles = np.zeros((0, 3), dtype=np.int32)
    elif triangles.ndim != 2 or triangles.shape[1] != 3:
        raise ValueError(f"Expected triangles shape (F, 3), got {triangles.shape!r}")

    num_tris = triangles.shape[0]
    raw_normals = getattr(mesh, "face_normals", None)
    if (
        raw_normals is not None
        and np.asarray(raw_normals).shape == (num_tris, 3)
        and np.all(np.isfinite(raw_normals))
    ):
        normals = np.asarray(raw_normals, dtype=np.float32)
    elif num_tris > 0:
        tris_xyz = vertices[triangles]
        e1 = tris_xyz[:, 1, :] - tris_xyz[:, 0, :]
        e2 = tris_xyz[:, 2, :] - tris_xyz[:, 0, :]
        cross = np.cross(e1, e2)
        lengths = np.linalg.norm(cross, axis=1, keepdims=True)
        safe_lengths = np.where(lengths > 1e-12, lengths, 1.0)
        normals = (cross / safe_lengths).astype(np.float32)
        normals = np.where(lengths > 1e-12, normals, np.array([[0.0, 0.0, 1.0]], dtype=np.float32))
    else:
        normals = np.zeros((0, 3), dtype=np.float32)

    return vertices, triangles, normals


def _mesh_xy_extents(mesh: Any, vertices: np.ndarray | None = None) -> tuple[float, float]:
    """Return (width_x_mm, depth_y_mm) of a mesh from bounds_mm or vertices."""
    bounds = getattr(mesh, "bounds_mm", None)
    if isinstance(bounds, dict):
        size = bounds.get("size")
        if isinstance(size, (list, tuple)) and len(size) >= 2:
            return max(float(size[0]), 1.0), max(float(size[1]), 1.0)
        bmin = bounds.get("min")
        bmax = bounds.get("max")
        if isinstance(bmin, (list, tuple)) and isinstance(bmax, (list, tuple)) and len(bmin) >= 2 and len(bmax) >= 2:
            return max(float(bmax[0]) - float(bmin[0]), 1.0), max(float(bmax[1]) - float(bmin[1]), 1.0)
    verts = vertices if vertices is not None else np.asarray(mesh.vertices, dtype=np.float32)
    if verts.shape[0] == 0:
        return 10.0, 10.0
    dx = float(np.max(verts[:, 0]) - np.min(verts[:, 0]))
    dy = float(np.max(verts[:, 1]) - np.min(verts[:, 1]))
    return max(dx, 1.0), max(dy, 1.0)


def _resolve_bed_dimensions(host_config: dict | None) -> tuple[float, float]:
    """Extract (bed_x, bed_y) in mm from host_config with 220x220 fallback."""
    bed_x = 220.0
    bed_y = 220.0
    if isinstance(host_config, dict):
        if "bed_x" in host_config:
            try:
                bed_x = max(float(host_config["bed_x"]), 60.0)
            except (TypeError, ValueError):
                pass
        if "bed_y" in host_config:
            try:
                bed_y = max(float(host_config["bed_y"]), 60.0)
            except (TypeError, ValueError):
                pass
        printer = host_config.get("printer")
        if isinstance(printer, dict):
            if "bed_x" in printer and "bed_x" not in host_config:
                try:
                    bed_x = max(float(printer["bed_x"]), 60.0)
                except (TypeError, ValueError):
                    pass
            if "bed_y" in printer and "bed_y" not in host_config:
                try:
                    bed_y = max(float(printer["bed_y"]), 60.0)
                except (TypeError, ValueError):
                    pass
    return bed_x, bed_y


def _positions_overlap(
    positions: list[tuple[float, float, float]],
    extents: list[tuple[float, float]],
    min_clearance_mm: float = 3.0,
) -> bool:
    """Return True if any two items overlap on the XY build plate."""
    n = len(positions)
    for i in range(n):
        xi, yi, _ = positions[i]
        wxi, wyi = extents[i]
        for j in range(i + 1, n):
            xj, yj, _ = positions[j]
            wxj, wyj = extents[j]
            overlap_x = abs(xi - xj) < (0.5 * (wxi + wxj) + min_clearance_mm)
            overlap_y = abs(yi - yj) < (0.5 * (wyi + wyj) + min_clearance_mm)
            if overlap_x and overlap_y:
                return True
    return False


def _arrange_items_on_bed(
    extents: list[tuple[float, float]],
    z_offsets: list[float],
    bed_x: float,
    bed_y: float,
    gap_mm: float = 10.0,
) -> list[tuple[float, float, float]]:
    """Arrange 1 or more items cleanly around the bed center without XY overlap."""
    cx = bed_x * 0.5
    cy = bed_y * 0.5
    count = len(extents)
    if count == 0:
        return []
    if count == 1:
        return [(cx, cy, z_offsets[0])]

    if count == 2:
        (w0, d0), (w1, d1) = extents
        total_w = w0 + gap_mm + w1
        if total_w <= bed_x - 8.0:
            left_edge = cx - 0.5 * total_w
            x0 = left_edge + 0.5 * w0
            x1 = left_edge + w0 + gap_mm + 0.5 * w1
            return [(x0, cy, z_offsets[0]), (x1, cy, z_offsets[1])]

        # Place along the bed diagonal when side-by-side exceeds X width
        r0 = 0.5 * max(w0, d0)
        r1 = 0.5 * max(w1, d1)
        diag_sep = r0 + r1 + gap_mm
        step = diag_sep / math.sqrt(2.0)
        half_step = 0.5 * step
        x0 = max(r0 + 2.0, cx - half_step)
        y0 = max(r0 + 2.0, cy - half_step)
        x1 = min(bed_x - r1 - 2.0, cx + half_step)
        y1 = min(bed_y - r1 - 2.0, cy + half_step)
        if math.hypot(x1 - x0, y1 - y0) >= (r0 + r1 + 2.0):
            return [(x0, y0, z_offsets[0]), (x1, y1, z_offsets[1])]
        # If combined radii exceed diagonal bed size, still place cleanly separated
        return [(cx - half_step, cy - half_step, z_offsets[0]), (cx + half_step, cy + half_step, z_offsets[1])]

    # General grid/row layout for 3+ items
    total_w = sum(w for w, _ in extents) + gap_mm * (count - 1)
    cursor_x = cx - 0.5 * total_w
    placed: list[tuple[float, float, float]] = []
    for idx, (w, _) in enumerate(extents):
        px = cursor_x + 0.5 * w
        placed.append((px, cy, z_offsets[idx]))
        cursor_x += w + gap_mm
    return placed


def _build_project_settings_dict(params: dict | None, host_config: dict | None) -> dict[str, Any]:
    """Merge host project settings with print-mode overrides for OrcaSlicer 2.5.1."""
    merged: dict[str, Any] = {}
    if isinstance(host_config, dict):
        raw_ps = host_config.get("project_settings")
        if isinstance(raw_ps, dict):
            merged.update(raw_ps)

    p = params if isinstance(params, dict) else {}
    print_mode = str(p.get("print_mode", "spiral_vase")).strip().lower()

    if print_mode == "shelled_hollow":
        wall_thickness = max(0.8, float(p.get("wall_thickness_mm", 2.2)))
        bottom_thickness = max(1.0, float(p.get("bottom_thickness_mm", 3.2)))
        merged["spiral_mode"] = "0"
        merged["spiral_mode_smooth"] = "0"
        if str(merged.get("wall_loops", "")).strip() in ("", "0", "1"):
            merged["wall_loops"] = str(max(2, min(6, int(round(wall_thickness / 0.84)))))
        if str(merged.get("top_shell_layers", "")).strip() in ("", "0"):
            merged["top_shell_layers"] = "4"
        if str(merged.get("bottom_shell_layers", "")).strip() in ("", "0"):
            merged["bottom_shell_layers"] = str(max(3, int(round(bottom_thickness / 0.20))))
        if str(merged.get("sparse_infill_density", "")).strip() in ("", "0", "0%"):
            merged["sparse_infill_density"] = "15%"
    else:
        spiral_smooth = bool(p.get("spiral_smooth", True))
        spiral_bottom_layers = max(2, min(20, int(round(float(p.get("spiral_bottom_layers", 5))))))
        spiral_line_width = max(0.30, min(1.50, float(p.get("spiral_line_width_mm", 0.65))))
        merged["spiral_mode"] = "1"
        merged["spiral_mode_smooth"] = "1" if spiral_smooth else "0"
        merged["wall_loops"] = "1"
        merged["top_shell_layers"] = "0"
        merged["sparse_infill_density"] = "0%"
        merged["bottom_shell_layers"] = str(spiral_bottom_layers)
        merged["outer_wall_line_width"] = f"{spiral_line_width:.2f}"

    return merged


def write_binary_stl(path: str | Path, mesh: Any, header_name: str = "OrcaVaseStudio") -> Path:
    """Write a duck-typed MeshData object to a standard little-endian binary STL file.

    Binary layout: 80-byte ASCII header + uint32 triangle count + F * 50-byte facet records.
    """
    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    vertices, triangles, normals = _extract_mesh_arrays(mesh)
    num_triangles = int(triangles.shape[0])

    clean_header = str(header_name or "OrcaVaseStudio").strip() or "OrcaVaseStudio"
    if clean_header.lower().startswith("solid"):
        clean_header = f"Orca_{clean_header}"
    header_text = f"{clean_header} - Orca Vase Studio Binary STL"
    header_bytes = header_text.encode("ascii", errors="replace")[:80].ljust(80, b"\x00")

    records = np.zeros(num_triangles, dtype=_STL_RECORD_DTYPE)
    if num_triangles > 0:
        tris_xyz = vertices[triangles]
        records["normal"] = normals.astype("<f4", copy=False)
        records["v0"] = tris_xyz[:, 0, :].astype("<f4", copy=False)
        records["v1"] = tris_xyz[:, 1, :].astype("<f4", copy=False)
        records["v2"] = tris_xyz[:, 2, :].astype("<f4", copy=False)
        records["attr"] = 0

    with open(out_path, "wb") as fh:
        fh.write(header_bytes)
        fh.write(struct.pack("<I", num_triangles))
        if num_triangles > 0:
            fh.write(records.tobytes())

    return out_path


def write_orca_3mf(
    path: str | Path,
    items: list[tuple[str, Any, tuple[float, float, float]]],
    params: dict,
    host_config: dict | None = None,
) -> Path:
    """Write an OrcaSlicer 2.5.1 compatible .3mf project archive with meshes and slicer settings."""
    if not items:
        raise ValueError("write_orca_3mf requires at least one item in 'items'.")

    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    bed_x, bed_y = _resolve_bed_dimensions(host_config)
    cx, cy = bed_x * 0.5, bed_y * 0.5

    parsed_items: list[tuple[str, np.ndarray, np.ndarray, tuple[float, float]]] = []
    raw_positions: list[tuple[float, float, float] | None] = []
    z_offsets: list[float] = []

    for idx, entry in enumerate(items):
        if len(entry) == 2:
            raw_name, mesh = entry  # type: ignore[misc]
            raw_pos = None
        elif len(entry) >= 3:
            raw_name, mesh, raw_pos = entry[0], entry[1], entry[2]
        else:
            raise ValueError(f"Invalid item tuple at index {idx}: {entry!r}")

        item_name = str(raw_name or f"Object_{idx + 1}").strip() or f"Object_{idx + 1}"
        vertices, triangles, _ = _extract_mesh_arrays(mesh)
        ext = _mesh_xy_extents(mesh, vertices)
        parsed_items.append((item_name, vertices, triangles, ext))

        if raw_pos is None:
            raw_positions.append(None)
            z_offsets.append(0.0)
        else:
            px, py, pz = float(raw_pos[0]), float(raw_pos[1]), float(raw_pos[2])
            raw_positions.append((px, py, pz))
            z_offsets.append(pz)

    extents_list = [it[3] for it in parsed_items]
    if any(pos is None for pos in raw_positions):
        if len(parsed_items) == 1:
            final_positions = [(cx, cy, z_offsets[0])]
        else:
            final_positions = _arrange_items_on_bed(extents_list, z_offsets, bed_x, bed_y, gap_mm=10.0)
    else:
        concrete_positions = [pos for pos in raw_positions if pos is not None]
        if len(concrete_positions) >= 2 and _positions_overlap(concrete_positions, extents_list, min_clearance_mm=3.0):
            final_positions = _arrange_items_on_bed(extents_list, z_offsets, bed_x, bed_y, gap_mm=10.0)
        else:
            final_positions = concrete_positions

    title = str((params or {}).get("name") or parsed_items[0][0] or "Orca Vase Studio").strip()
    escaped_title = _xml_escape(title, {'"': "&quot;"})
    today_iso = _dt.date.today().isoformat()
    ns_seed = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    build_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-build-{title}"))

    object_blocks: list[str] = []
    build_items_xml: list[str] = []
    model_settings_objects: list[str] = []
    model_settings_instances: list[str] = []
    model_settings_assemble: list[str] = []

    for idx, (item_name, vertices, triangles, _) in enumerate(parsed_items):
        obj_id = idx + 1
        tx, ty, tz = final_positions[idx]
        esc_name = _xml_escape(item_name, {'"': "&quot;"})
        obj_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-obj-{obj_id}-{item_name}"))
        item_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-item-{obj_id}-{item_name}"))

        verts_py = vertices.tolist()
        tris_py = triangles.tolist()

        vertex_lines = "\n".join(
            f'     <vertex x="{vx:.5f}" y="{vy:.5f}" z="{vz:.5f}"/>'
            for vx, vy, vz in verts_py
        )
        triangle_lines = "\n".join(
            f'     <triangle v1="{v1}" v2="{v2}" v3="{v3}"/>'
            for v1, v2, v3 in tris_py
        )

        object_blocks.append(
            f'  <object id="{obj_id}" p:UUID="{obj_uuid}" name="{esc_name}" type="model">\n'
            f"   <mesh>\n"
            f"    <vertices>\n"
            f"{vertex_lines}\n"
            f"    </vertices>\n"
            f"    <triangles>\n"
            f"{triangle_lines}\n"
            f"    </triangles>\n"
            f"   </mesh>\n"
            f"  </object>"
        )

        transform_3x4 = f"1 0 0 0 1 0 0 0 1 {tx:.4f} {ty:.4f} {tz:.4f}"
        build_items_xml.append(
            f'  <item objectid="{obj_id}" p:UUID="{item_uuid}" transform="{transform_3x4}" printable="1"/>'
        )

        model_settings_objects.append(
            f'  <object id="{obj_id}">\n'
            f'    <metadata key="name" value="{esc_name}"/>\n'
            f'    <metadata key="extruder" value="1"/>\n'
            f'    <part id="1" subtype="normal_part">\n'
            f'      <metadata key="name" value="{esc_name}"/>\n'
            f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
            f'      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
            f"    </part>\n"
            f"  </object>"
        )
        model_settings_instances.append(
            f"    <model_instance>\n"
            f'      <metadata key="object_id" value="{obj_id}"/>\n'
            f'      <metadata key="instance_id" value="0"/>\n'
            f'      <metadata key="identify_id" value="{100 + obj_id}"/>\n'
            f"    </model_instance>"
        )
        model_settings_assemble.append(
            f'    <assemble_item object_id="{obj_id}" instance_id="0" transform="{transform_3x4}" offset="0 0 0"/>'
        )

    model_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<model unit="millimeter" xml:lang="en-US" '
        'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
        'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021" '
        'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" '
        'requiredextensions="p">\n'
        ' <metadata name="Application">OrcaSlicer-2.5.1</metadata>\n'
        ' <metadata name="OrcaSlicer">2.5.1</metadata>\n'
        ' <metadata name="BambuStudio:3mfVersion">1</metadata>\n'
        f' <metadata name="Title">{escaped_title}</metadata>\n'
        f' <metadata name="CreationDate">{today_iso}</metadata>\n'
        " <resources>\n"
        + "\n".join(object_blocks)
        + "\n </resources>\n"
        + f' <build p:UUID="{build_uuid}">\n'
        + "\n".join(build_items_xml)
        + "\n </build>\n"
        "</model>\n"
    )

    model_settings_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<config>\n"
        + "\n".join(model_settings_objects)
        + "\n  <plate>\n"
        '    <metadata key="plater_id" value="1"/>\n'
        '    <metadata key="plater_name" value=""/>\n'
        '    <metadata key="locked" value="false"/>\n'
        + "\n".join(model_settings_instances)
        + "\n  </plate>\n"
        "  <assemble>\n"
        + "\n".join(model_settings_assemble)
        + "\n  </assemble>\n"
        "</config>\n"
    )

    project_settings = _build_project_settings_dict(params, host_config)
    project_settings_json = json.dumps(project_settings, indent=2, ensure_ascii=False)

    with zipfile.ZipFile(out_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        zf.writestr("[Content_Types].xml", _CONTENT_TYPES_XML)
        zf.writestr("_rels/.rels", _RELS_XML)
        zf.writestr("3D/3dmodel.model", model_xml)
        zf.writestr("Metadata/model_settings.config", model_settings_xml)
        zf.writestr("Metadata/project_settings.config", project_settings_json)

    return out_path

# ===========================================================================
# MODULE: vase_studio.presets_catalog
# ===========================================================================

"""Curated built-in presets catalog, user preset storage, and smart printable randomizer."""

pass  # [bundled] hoisted __future__ import

import copy
import datetime as _dt
import json
import math
import random
import re
import uuid
from pathlib import Path
from typing import Any

_PRESETS_FALLBACK_DEFAULT_PARAMS: dict[str, Any] = {
    "name": "Ondas Organicas",
    "height_mm": 160.0,
    "base_diameter_mm": 76.0,
    "belly_diameter_mm": 110.0,
    "belly_height_ratio": 0.34,
    "waist_diameter_mm": 68.0,
    "waist_height_ratio": 0.68,
    "neck_diameter_mm": 82.0,
    "lip_flare_mm": 4.0,
    "lip_bevel_mm": 1.0,
    "polygon_sides": 0,
    "polygon_roundness": 0.35,
    "use_custom_profile": False,
    "profile_points": [
        [0.0, 38.0],
        [0.34, 55.0],
        [0.68, 34.0],
        [0.92, 41.0],
        [1.0, 45.0],
    ],
    "resolution_angular": 240,
    "resolution_vertical": 220,
    "bottom_fade_mm": 8.0,
    "top_fade_mm": 6.0,
    "global_twist_deg": 0.0,
    "textures": {
        "ribbed": {
            "enabled": False,
            "depth_mm": 2.6,
            "count": 32,
            "duty_cycle": 0.50,
            "sharpness": 0.35,
            "twist_deg": 60.0,
            "phase_deg": 0.0,
        },
        "waves": {
            "enabled": True,
            "depth_mm": 3.0,
            "vertical_wavelength_mm": 26.0,
            "angular_lobes": 6,
            "interference_mix": 0.45,
            "wave_skew": 0.0,
            "phase_deg": 0.0,
        },
        "origami": {
            "enabled": False,
            "depth_mm": 3.2,
            "cells_around": 12,
            "cells_vertical": 8,
            "crease_sharpness": 0.75,
            "stagger": 0.50,
        },
        "cellular": {
            "enabled": False,
            "depth_mm": 2.4,
            "scale_angular": 8,
            "scale_vertical_mm": 22.0,
            "ridge_mode": True,
            "octaves": 2,
            "seed": 42,
        },
    },
    "print_mode": "shelled_hollow",
    "stl_always_open_hollow": True,
    "auto_configure_slicer": True,
    "spiral_line_width_mm": 0.65,
    "spiral_bottom_layers": 5,
    "spiral_smooth": True,
    "wall_thickness_mm": 2.4,
    "bottom_thickness_mm": 3.2,
    "auto_clamp_overhang": False,
    "max_safe_overhang_deg": 48.0,
    "drainage": {
        "enabled": False,
        "hole_count": 4,
        "hole_diameter_mm": 8.0,
        "ring_radius_ratio": 0.48,
    },
    "saucer": {
        "clearance_mm": 8.0,
        "rim_height_mm": 22.0,
        "wall_thickness_mm": 2.4,
        "floor_thickness_mm": 2.6,
        "inner_ribs_height_mm": 2.0,
        "match_vase_texture": True,
    },
}


def _presets_clamp_float(val: Any, lo: float, hi: float, default: float) -> float:
    try:
        num = float(val)
        if not math.isfinite(num):
            return default
        return max(lo, min(hi, num))
    except (TypeError, ValueError):
        return default


def _presets_clamp_int(val: Any, lo: int, hi: int, default: int) -> int:
    try:
        num = int(round(float(val)))
        return max(lo, min(hi, num))
    except (TypeError, ValueError):
        return default


def _presets_to_bool(val: Any, default: bool) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val) if math.isfinite(val) else default
    if isinstance(val, str):
        s = val.strip().lower()
        if s in ("true", "1", "yes", "on"):
            return True
        if s in ("false", "0", "no", "off", ""):
            return False
    return default


def _presets_deep_merge(dst: dict[str, Any], src: dict[str, Any]) -> None:
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            _presets_deep_merge(dst[k], v)
        else:
            dst[k] = copy.deepcopy(v)


def _presets_fallback_normalize(raw: dict | None = None) -> dict[str, Any]:
    out = copy.deepcopy(_PRESETS_FALLBACK_DEFAULT_PARAMS)
    if isinstance(raw, dict):
        _presets_deep_merge(out, raw)

    out["name"] = str(out.get("name") or "Ondas Organicas").strip()[:100] or "Ondas Organicas"
    out["height_mm"] = _presets_clamp_float(out.get("height_mm"), 30.0, 500.0, 160.0)
    out["base_diameter_mm"] = _presets_clamp_float(out.get("base_diameter_mm"), 20.0, 450.0, 76.0)
    out["belly_diameter_mm"] = _presets_clamp_float(out.get("belly_diameter_mm"), 20.0, 450.0, 110.0)
    out["belly_height_ratio"] = _presets_clamp_float(out.get("belly_height_ratio"), 0.08, 0.85, 0.34)
    out["waist_diameter_mm"] = _presets_clamp_float(out.get("waist_diameter_mm"), 16.0, 450.0, 68.0)
    out["waist_height_ratio"] = _presets_clamp_float(out.get("waist_height_ratio"), 0.15, 0.92, 0.68)
    out["neck_diameter_mm"] = _presets_clamp_float(out.get("neck_diameter_mm"), 16.0, 450.0, 82.0)
    out["lip_flare_mm"] = _presets_clamp_float(out.get("lip_flare_mm"), -15.0, 25.0, 4.0)
    out["lip_bevel_mm"] = _presets_clamp_float(out.get("lip_bevel_mm"), 0.0, 4.0, 1.0)

    poly = _presets_clamp_int(out.get("polygon_sides"), 0, 24, 0)
    out["polygon_sides"] = 0 if poly < 3 else poly
    out["polygon_roundness"] = _presets_clamp_float(out.get("polygon_roundness"), 0.0, 1.0, 0.35)
    out["use_custom_profile"] = bool(out.get("use_custom_profile", False))

    pts_raw = out.get("profile_points")
    pts: list[list[float]] = []
    if isinstance(pts_raw, list):
        for item in pts_raw:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                zn = _presets_clamp_float(item[0], 0.0, 1.0, 0.0)
                rm = _presets_clamp_float(item[1], 8.0, 225.0, 38.0)
                pts.append([zn, rm])
    if len(pts) < 2:
        pts = copy.deepcopy(_PRESETS_FALLBACK_DEFAULT_PARAMS["profile_points"])
    pts.sort(key=lambda pair: pair[0])
    pts[0][0] = 0.0
    pts[-1][0] = 1.0
    out["profile_points"] = pts

    out["resolution_angular"] = _presets_clamp_int(out.get("resolution_angular"), 64, 360, 240)
    out["resolution_vertical"] = _presets_clamp_int(out.get("resolution_vertical"), 60, 400, 220)
    out["bottom_fade_mm"] = _presets_clamp_float(out.get("bottom_fade_mm"), 0.0, 60.0, 8.0)
    out["top_fade_mm"] = _presets_clamp_float(out.get("top_fade_mm"), 0.0, 60.0, 6.0)
    out["global_twist_deg"] = _presets_clamp_float(out.get("global_twist_deg"), -720.0, 720.0, 0.0)

    tex = out["textures"]
    rib = tex["ribbed"]
    rib["enabled"] = bool(rib.get("enabled", False))
    rib["depth_mm"] = _presets_clamp_float(rib.get("depth_mm"), -15.0, 15.0, 2.6)
    rib["count"] = _presets_clamp_int(rib.get("count"), 3, 180, 32)
    rib["duty_cycle"] = _presets_clamp_float(rib.get("duty_cycle"), 0.10, 0.90, 0.50)
    rib["sharpness"] = _presets_clamp_float(rib.get("sharpness"), 0.0, 1.0, 0.35)
    rib["twist_deg"] = _presets_clamp_float(rib.get("twist_deg"), -720.0, 720.0, 60.0)
    rib["phase_deg"] = _presets_clamp_float(rib.get("phase_deg"), 0.0, 360.0, 0.0)

    wav = tex["waves"]
    wav["enabled"] = bool(wav.get("enabled", True))
    wav["depth_mm"] = _presets_clamp_float(wav.get("depth_mm"), -15.0, 15.0, 3.0)
    wav["vertical_wavelength_mm"] = _presets_clamp_float(wav.get("vertical_wavelength_mm"), 4.0, 120.0, 26.0)
    wav["angular_lobes"] = _presets_clamp_int(wav.get("angular_lobes"), 0, 48, 6)
    wav["interference_mix"] = _presets_clamp_float(wav.get("interference_mix"), 0.0, 1.0, 0.45)
    wav["wave_skew"] = _presets_clamp_float(wav.get("wave_skew"), -0.8, 0.8, 0.0)
    wav["phase_deg"] = _presets_clamp_float(wav.get("phase_deg"), 0.0, 360.0, 0.0)

    ori = tex["origami"]
    ori["enabled"] = bool(ori.get("enabled", False))
    ori["depth_mm"] = _presets_clamp_float(ori.get("depth_mm"), -15.0, 15.0, 3.2)
    ori["cells_around"] = _presets_clamp_int(ori.get("cells_around"), 3, 60, 12)
    ori["cells_vertical"] = _presets_clamp_int(ori.get("cells_vertical"), 2, 50, 8)
    ori["crease_sharpness"] = _presets_clamp_float(ori.get("crease_sharpness"), 0.0, 1.0, 0.75)
    ori["stagger"] = _presets_clamp_float(ori.get("stagger"), 0.0, 1.0, 0.50)

    cel = tex["cellular"]
    cel["enabled"] = bool(cel.get("enabled", False))
    cel["depth_mm"] = _presets_clamp_float(cel.get("depth_mm"), -12.0, 12.0, 2.4)
    cel["scale_angular"] = _presets_clamp_int(cel.get("scale_angular"), 2, 40, 8)
    cel["scale_vertical_mm"] = _presets_clamp_float(cel.get("scale_vertical_mm"), 5.0, 100.0, 22.0)
    cel["ridge_mode"] = bool(cel.get("ridge_mode", True))
    cel["octaves"] = _presets_clamp_int(cel.get("octaves"), 1, 4, 2)
    cel["seed"] = _presets_clamp_int(cel.get("seed"), 1, 99999, 42)

    pm = str(out.get("print_mode", "shelled_hollow")).strip().lower()
    out["print_mode"] = pm if pm in ("spiral_vase", "shelled_hollow") else "shelled_hollow"
    out["stl_always_open_hollow"] = _presets_to_bool(out.get("stl_always_open_hollow"), True)
    out["auto_configure_slicer"] = _presets_to_bool(out.get("auto_configure_slicer"), True)
    out["spiral_line_width_mm"] = _presets_clamp_float(out.get("spiral_line_width_mm"), 0.40, 1.20, 0.65)
    out["spiral_bottom_layers"] = _presets_clamp_int(out.get("spiral_bottom_layers"), 2, 15, 5)
    out["spiral_smooth"] = _presets_to_bool(out.get("spiral_smooth"), True)
    out["wall_thickness_mm"] = _presets_clamp_float(out.get("wall_thickness_mm"), 0.8, 25.0, 2.4)
    out["bottom_thickness_mm"] = _presets_clamp_float(out.get("bottom_thickness_mm"), 1.0, 25.0, 3.2)
    out["auto_clamp_overhang"] = _presets_to_bool(out.get("auto_clamp_overhang"), False)
    out["max_safe_overhang_deg"] = _presets_clamp_float(out.get("max_safe_overhang_deg"), 35.0, 65.0, 48.0)

    drn = out["drainage"]
    drn["enabled"] = bool(drn.get("enabled", False))
    drn["hole_count"] = _presets_clamp_int(drn.get("hole_count"), 1, 9, 4)
    drn["hole_diameter_mm"] = _presets_clamp_float(drn.get("hole_diameter_mm"), 3.0, 20.0, 8.0)
    drn["ring_radius_ratio"] = _presets_clamp_float(drn.get("ring_radius_ratio"), 0.0, 0.68, 0.48)

    scr = out["saucer"]
    scr["clearance_mm"] = _presets_clamp_float(scr.get("clearance_mm"), 3.0, 25.0, 8.0)
    scr["rim_height_mm"] = _presets_clamp_float(scr.get("rim_height_mm"), 10.0, 60.0, 22.0)
    scr["wall_thickness_mm"] = _presets_clamp_float(scr.get("wall_thickness_mm"), 1.2, 5.0, 2.4)
    scr["floor_thickness_mm"] = _presets_clamp_float(scr.get("floor_thickness_mm"), 1.2, 6.0, 2.6)
    scr["inner_ribs_height_mm"] = _presets_clamp_float(scr.get("inner_ribs_height_mm"), 0.0, 6.0, 2.0)
    scr["match_vase_texture"] = bool(scr.get("match_vase_texture", True))

    return out


try:
    pass  # [bundled] resolved intra-package import

    pass
except (ImportError, KeyError, ValueError):
    pass

if "DEFAULT_PARAMS" not in globals() or "normalize_params" not in globals():
    DEFAULT_PARAMS = _PRESETS_FALLBACK_DEFAULT_PARAMS
    normalize_params = _presets_fallback_normalize


_USER_PRESETS_FILENAME = "user_presets.json"


def _make_preset_params(overrides: dict[str, Any]) -> dict[str, Any]:
    """Build a clean preset parameter dictionary starting with all textures disabled unless specified."""
    base = copy.deepcopy(DEFAULT_PARAMS)
    for t_cfg in base["textures"].values():
        t_cfg["enabled"] = False
    _presets_deep_merge(base, overrides)
    return normalize_params(base)


BUILTIN_PRESETS: list[dict[str, Any]] = [
    {
        "id": "ondas_organicas",
        "title_pt": "Ondas Orgânicas",
        "title_en": "Organic Waves",
        "category": "organic",
        "description_pt": "Ondulações contra-helicoidais fluidas inspiradas em dunas e correntes marinhas.",
        "description_en": "Flowing counter-helical ripples inspired by coastal dunes and ocean currents.",
        "params": _make_preset_params(
            {
                "name": "Ondas Orgânicas",
                "height_mm": 165.0,
                "base_diameter_mm": 76.0,
                "belly_diameter_mm": 112.0,
                "belly_height_ratio": 0.34,
                "waist_diameter_mm": 68.0,
                "waist_height_ratio": 0.68,
                "neck_diameter_mm": 82.0,
                "lip_flare_mm": 4.0,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 7.0,
                "global_twist_deg": 40.0,
                "textures": {
                    "waves": {
                        "enabled": True,
                        "depth_mm": 3.0,
                        "vertical_wavelength_mm": 26.0,
                        "angular_lobes": 6,
                        "interference_mix": 0.45,
                        "wave_skew": 0.15,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "colunas_caneladas",
        "title_pt": "Colunas Caneladas",
        "title_en": "Architectural Fluted",
        "category": "architectural",
        "description_pt": "Caneluras verticais clássicas com espaçamento arquitetônico limpo e sombra marcada.",
        "description_en": "Crisp vertical architectural flutes with balanced flat fillets and clean shadow lines.",
        "params": _make_preset_params(
            {
                "name": "Colunas Caneladas",
                "height_mm": 190.0,
                "base_diameter_mm": 84.0,
                "belly_diameter_mm": 102.0,
                "belly_height_ratio": 0.40,
                "waist_diameter_mm": 88.0,
                "waist_height_ratio": 0.76,
                "neck_diameter_mm": 90.0,
                "lip_flare_mm": 3.0,
                "bottom_fade_mm": 9.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 0.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 2.5,
                        "count": 36,
                        "duty_cycle": 0.58,
                        "sharpness": 0.35,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.8,
                "bottom_thickness_mm": 3.6,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "helice_escultural",
        "title_pt": "Hélice Escultural",
        "title_en": "Twisted Helix",
        "category": "sculptural",
        "description_pt": "Lâminas helicoidais contínuas combinadas com seção octogonal suavizada.",
        "description_en": "Sweeping helical fins paired with a softened octagonal cross-section.",
        "params": _make_preset_params(
            {
                "name": "Hélice Escultural",
                "height_mm": 185.0,
                "base_diameter_mm": 78.0,
                "belly_diameter_mm": 108.0,
                "belly_height_ratio": 0.36,
                "waist_diameter_mm": 72.0,
                "waist_height_ratio": 0.72,
                "neck_diameter_mm": 80.0,
                "lip_flare_mm": 3.5,
                "polygon_sides": 8,
                "polygon_roundness": 0.55,
                "bottom_fade_mm": 12.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 180.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 2.4,
                        "count": 16,
                        "duty_cycle": 0.65,
                        "sharpness": 0.55,
                        "twist_deg": 180.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "spiral_line_width_mm": 0.68,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "origami_yoshimura",
        "title_pt": "Origami Yoshimura",
        "title_en": "Yoshimura Origami Diamond",
        "category": "geometric",
        "description_pt": "Dobragem geométrica em diamantes alternados estilo Yoshimura com vincos precisos.",
        "description_en": "Authentic staggered diamond origami facets with crisp Yoshimura paper creases.",
        "params": _make_preset_params(
            {
                "name": "Origami Yoshimura",
                "height_mm": 160.0,
                "base_diameter_mm": 82.0,
                "belly_diameter_mm": 104.0,
                "belly_height_ratio": 0.42,
                "waist_diameter_mm": 86.0,
                "waist_height_ratio": 0.76,
                "neck_diameter_mm": 84.0,
                "lip_flare_mm": 1.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 15.0,
                "textures": {
                    "origami": {
                        "enabled": True,
                        "depth_mm": 3.2,
                        "cells_around": 12,
                        "cells_vertical": 9,
                        "crease_sharpness": 0.82,
                        "stagger": 0.50,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.0,
                "bottom_thickness_mm": 3.0,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "recife_celular",
        "title_pt": "Recife Celular",
        "title_en": "Cellular Coral",
        "category": "organic",
        "description_pt": "Veios orgânicos tridimensionais inspirados em corais marinhos e rocha vulcânica.",
        "description_en": "Three-dimensional ridged veins inspired by reef coral and carved volcanic stone.",
        "params": _make_preset_params(
            {
                "name": "Recife Celular",
                "height_mm": 150.0,
                "base_diameter_mm": 80.0,
                "belly_diameter_mm": 118.0,
                "belly_height_ratio": 0.38,
                "waist_diameter_mm": 76.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 70.0,
                "lip_flare_mm": 2.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 24.0,
                "textures": {
                    "cellular": {
                        "enabled": True,
                        "depth_mm": 2.8,
                        "scale_angular": 9,
                        "scale_vertical_mm": 20.0,
                        "ridge_mode": True,
                        "octaves": 3,
                        "seed": 108,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.6,
                "bottom_thickness_mm": 3.4,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "tulipa_minimalista",
        "title_pt": "Tulipa Minimalista",
        "title_en": "Minimalist Tulip",
        "category": "minimal",
        "description_pt": "Silhueta escandinava pura e serena com lábio suavemente aberto e parede espessa.",
        "description_en": "Pure Scandinavian silhouette with a serene waist and gently flared tulip rim.",
        "params": _make_preset_params(
            {
                "name": "Tulipa Minimalista",
                "height_mm": 175.0,
                "base_diameter_mm": 70.0,
                "belly_diameter_mm": 106.0,
                "belly_height_ratio": 0.28,
                "waist_diameter_mm": 58.0,
                "waist_height_ratio": 0.72,
                "neck_diameter_mm": 66.0,
                "lip_flare_mm": 6.0,
                "lip_bevel_mm": 1.4,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.6,
                "bottom_thickness_mm": 3.4,
                "spiral_line_width_mm": 0.75,
                "spiral_bottom_layers": 6,
            }
        ),
    },
    {
        "id": "cachepo_botanico",
        "title_pt": "Cachepô Botânico + Pratinho",
        "title_en": "Botanical Planter + Saucer",
        "category": "garden",
        "description_pt": "Vaso estrutural oco com parede dupla, furos de drenagem reais e pratinho coletor.",
        "description_en": "Sturdy shelled hollow planter with real drainage tunnels and matching drip saucer.",
        "params": _make_preset_params(
            {
                "name": "Cachepô Botânico",
                "height_mm": 125.0,
                "base_diameter_mm": 112.0,
                "belly_diameter_mm": 132.0,
                "belly_height_ratio": 0.45,
                "waist_diameter_mm": 136.0,
                "waist_height_ratio": 0.78,
                "neck_diameter_mm": 138.0,
                "lip_flare_mm": 2.0,
                "lip_bevel_mm": 1.4,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.8,
                        "count": 42,
                        "duty_cycle": 0.62,
                        "sharpness": 0.25,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 3.2,
                "bottom_thickness_mm": 3.8,
                "drainage": {
                    "enabled": True,
                    "hole_count": 4,
                    "hole_diameter_mm": 8.0,
                    "ring_radius_ratio": 0.46,
                },
                "saucer": {
                    "clearance_mm": 8.0,
                    "rim_height_mm": 22.0,
                    "wall_thickness_mm": 2.4,
                    "floor_thickness_mm": 2.6,
                    "inner_ribs_height_mm": 2.0,
                    "match_vase_texture": True,
                },
            }
        ),
    },
    {
        "id": "ampulheta_hibrida",
        "title_pt": "Ampulheta Ondas & Frisos",
        "title_en": "Hourglass Wave-Ribbed Hybrid",
        "category": "sculptural",
        "description_pt": "Curva ampulheta de duplo bojo combinando micro-frisos torcidos sobre ondas suaves.",
        "description_en": "Dual-belly hourglass profile layering fine twisted ribs over gentle harmonic waves.",
        "params": _make_preset_params(
            {
                "name": "Ampulheta Ondas & Frisos",
                "height_mm": 175.0,
                "base_diameter_mm": 88.0,
                "belly_diameter_mm": 116.0,
                "belly_height_ratio": 0.24,
                "waist_diameter_mm": 68.0,
                "waist_height_ratio": 0.52,
                "neck_diameter_mm": 84.0,
                "lip_flare_mm": 4.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 44.0],
                    [0.24, 58.0],
                    [0.52, 34.0],
                    [0.80, 51.0],
                    [0.93, 42.0],
                    [1.0, 46.0],
                ],
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 7.0,
                "global_twist_deg": 35.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.6,
                        "count": 44,
                        "duty_cycle": 0.55,
                        "sharpness": 0.40,
                        "twist_deg": 45.0,
                        "phase_deg": 0.0,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 2.1,
                        "vertical_wavelength_mm": 32.0,
                        "angular_lobes": 5,
                        "interference_mix": 0.50,
                        "wave_skew": 0.0,
                        "phase_deg": 0.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
            }
        ),
    },
    {
        "id": "cristal_lowpoly",
        "title_pt": "Cristal Facetado Low-Poly",
        "title_en": "Low-Poly Geometric Crystal",
        "category": "geometric",
        "description_pt": "Prisma heptagonal lapidado com facetas angulares que capturam reflexos de seda.",
        "description_en": "Gem-cut heptagonal crystal facets designed to showcase silk and dual-color filaments.",
        "params": _make_preset_params(
            {
                "name": "Cristal Facetado Low-Poly",
                "height_mm": 168.0,
                "base_diameter_mm": 74.0,
                "belly_diameter_mm": 114.0,
                "belly_height_ratio": 0.38,
                "waist_diameter_mm": 78.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 68.0,
                "lip_flare_mm": 1.0,
                "polygon_sides": 7,
                "polygon_roundness": 0.08,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "global_twist_deg": 90.0,
                "textures": {
                    "origami": {
                        "enabled": True,
                        "depth_mm": 2.5,
                        "cells_around": 7,
                        "cells_vertical": 5,
                        "crease_sharpness": 0.92,
                        "stagger": 0.50,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.2,
                "bottom_thickness_mm": 3.0,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "zen_martelado",
        "title_pt": "Cerâmica Zen Martelada",
        "title_en": "Hammered Zen Ceramic",
        "category": "organic",
        "description_pt": "Vaso wabi-sabi de parede espessa com relevo martelado suave ideal para PLA fosco.",
        "description_en": "Thick-walled wabi-sabi vessel with soft hammered dimples tailored for matte filaments.",
        "params": _make_preset_params(
            {
                "name": "Cerâmica Zen Martelada",
                "height_mm": 138.0,
                "base_diameter_mm": 82.0,
                "belly_diameter_mm": 122.0,
                "belly_height_ratio": 0.36,
                "waist_diameter_mm": 92.0,
                "waist_height_ratio": 0.75,
                "neck_diameter_mm": 76.0,
                "lip_flare_mm": 1.5,
                "lip_bevel_mm": 1.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "textures": {
                    "cellular": {
                        "enabled": True,
                        "depth_mm": 2.0,
                        "scale_angular": 12,
                        "scale_vertical_mm": 16.0,
                        "ridge_mode": False,
                        "octaves": 2,
                        "seed": 77,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 0.9,
                        "vertical_wavelength_mm": 38.0,
                        "angular_lobes": 3,
                        "interference_mix": 0.70,
                        "wave_skew": 0.0,
                        "phase_deg": 30.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 4.0,
                "bottom_thickness_mm": 4.4,
            }
        ),
    },
    {
        "id": "lanterna_plissada",
        "title_pt": "Lanterna Plissada",
        "title_en": "Pleated Paper Lantern",
        "category": "architectural",
        "description_pt": "Pregas sanfonadas agudas com anéis horizontais sutis inspiradas em lanternas chochin.",
        "description_en": "Sharp accordion pleats crossed by subtle horizontal rings inspired by chochin lanterns.",
        "params": _make_preset_params(
            {
                "name": "Lanterna Plissada",
                "height_mm": 155.0,
                "base_diameter_mm": 78.0,
                "belly_diameter_mm": 124.0,
                "belly_height_ratio": 0.48,
                "waist_diameter_mm": 102.0,
                "waist_height_ratio": 0.80,
                "neck_diameter_mm": 78.0,
                "lip_flare_mm": 2.0,
                "bottom_fade_mm": 9.0,
                "top_fade_mm": 7.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 3.2,
                        "count": 48,
                        "duty_cycle": 0.86,
                        "sharpness": 0.88,
                        "twist_deg": 18.0,
                        "phase_deg": 0.0,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 1.1,
                        "vertical_wavelength_mm": 18.0,
                        "angular_lobes": 0,
                        "interference_mix": 0.0,
                        "wave_skew": 0.0,
                        "phase_deg": 0.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 1.8,
                "bottom_thickness_mm": 2.8,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "anfora_mediterranea",
        "title_pt": "Ânfora Mediterrânea",
        "title_en": "Mediterranean Amphora",
        "category": "classic",
        "description_pt": "Proporções greco-romanas esbeltas com pedestal suave, ombros largos e estrias finas.",
        "description_en": "Classical Greco-Roman proportions with a tapered foot, broad shoulder, and fine lathe ribs.",
        "params": _make_preset_params(
            {
                "name": "Ânfora Mediterrânea",
                "height_mm": 195.0,
                "base_diameter_mm": 72.0,
                "belly_diameter_mm": 120.0,
                "belly_height_ratio": 0.46,
                "waist_diameter_mm": 62.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 60.0,
                "lip_flare_mm": 7.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 36.0],
                    [0.12, 33.0],
                    [0.46, 60.0],
                    [0.74, 31.0],
                    [0.90, 30.0],
                    [0.96, 36.5],
                    [1.0, 40.0],
                ],
                "bottom_fade_mm": 28.0,
                "top_fade_mm": 24.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.2,
                        "count": 60,
                        "duty_cycle": 0.50,
                        "sharpness": 0.20,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 3.0,
                "bottom_thickness_mm": 3.8,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
]


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return slug[:32] or "preset"


def _user_presets_path(storage_dir: str | Path) -> Path:
    return Path(storage_dir) / _USER_PRESETS_FILENAME


def _sanitize_user_preset_entry(entry: dict[str, Any]) -> dict[str, Any] | None:
    if not isinstance(entry, dict):
        return None
    raw_params = entry.get("params")
    if not isinstance(raw_params, dict):
        return None
    name = str(entry.get("name") or entry.get("title_pt") or raw_params.get("name") or "Meu Vaso").strip()[:80]
    if not name:
        name = "Meu Vaso"
    preset_id = str(entry.get("id") or "").strip() or f"user_{_slugify(name)}_{uuid.uuid4().hex[:6]}"
    norm_params = normalize_params(raw_params)
    norm_params["name"] = name
    now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()
    return {
        "id": preset_id,
        "name": name,
        "title_pt": str(entry.get("title_pt") or name),
        "title_en": str(entry.get("title_en") or name),
        "category": "user",
        "description_pt": str(entry.get("description_pt") or "Preset salvo pelo usuário"),
        "description_en": str(entry.get("description_en") or "User-saved custom preset"),
        "created_at": str(entry.get("created_at") or now_iso),
        "updated_at": str(entry.get("updated_at") or now_iso),
        "params": norm_params,
    }


def _write_user_presets_file(storage_dir: str | Path, presets: list[dict[str, Any]]) -> None:
    folder = Path(storage_dir)
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)
    target = folder / _USER_PRESETS_FILENAME
    payload = {"version": "1.0", "presets": presets}
    with open(target, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)


def load_user_presets(storage_dir: str | Path) -> list[dict[str, Any]]:
    """Load and validate user-saved presets from storage_dir/user_presets.json."""
    target = _user_presets_path(storage_dir)
    if not target.is_file():
        return []
    try:
        with open(target, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return []

    raw_list = raw.get("presets") if isinstance(raw, dict) else raw
    if not isinstance(raw_list, list):
        return []

    cleaned: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for item in raw_list:
        sanitized = _sanitize_user_preset_entry(item)
        if sanitized is not None and sanitized["id"] not in seen_ids:
            seen_ids.add(sanitized["id"])
            cleaned.append(sanitized)
    return cleaned


def save_user_preset(
    storage_dir: str | Path,
    name: str,
    params: dict[str, Any],
    preset_id: str | None = None,
) -> list[dict[str, Any]]:
    """Save or update a user preset in storage_dir and return the updated list."""
    existing = load_user_presets(storage_dir)
    clean_name = str(name or "").strip()[:80]
    if not clean_name:
        clean_name = str((params or {}).get("name") or "Meu Vaso").strip()[:80] or "Meu Vaso"

    norm_params = normalize_params(params if isinstance(params, dict) else {})
    norm_params["name"] = clean_name
    now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()

    target_id = str(preset_id).strip() if preset_id else ""
    updated = False
    if target_id:
        for idx, item in enumerate(existing):
            if item.get("id") == target_id:
                existing[idx] = {
                    **item,
                    "id": target_id,
                    "name": clean_name,
                    "title_pt": clean_name,
                    "title_en": clean_name,
                    "updated_at": now_iso,
                    "params": norm_params,
                }
                updated = True
                break

    if not updated:
        if not target_id:
            target_id = f"user_{_slugify(clean_name)}_{uuid.uuid4().hex[:8]}"
        existing.append(
            {
                "id": target_id,
                "name": clean_name,
                "title_pt": clean_name,
                "title_en": clean_name,
                "category": "user",
                "description_pt": "Preset salvo pelo usuário",
                "description_en": "User-saved custom preset",
                "created_at": now_iso,
                "updated_at": now_iso,
                "params": norm_params,
            }
        )

    _write_user_presets_file(storage_dir, existing)
    return existing


def delete_user_preset(storage_dir: str | Path, preset_id: str) -> list[dict[str, Any]]:
    """Delete a user preset by preset_id and return the remaining presets list."""
    target_id = str(preset_id or "").strip()
    existing = load_user_presets(storage_dir)
    remaining = [item for item in existing if item.get("id") != target_id]
    if len(remaining) != len(existing) or _user_presets_path(storage_dir).is_file():
        _write_user_presets_file(storage_dir, remaining)
    return remaining


def generate_random_printable_params(
    seed: int | None = None,
    current_params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Generate a cohesive, aesthetically balanced, FDM-printable random vase parameter dict."""
    actual_seed = int(seed) if seed is not None else random.SystemRandom().randint(1, 99999)
    rng = random.Random(actual_seed)

    base_state = normalize_params(current_params) if isinstance(current_params, dict) else copy.deepcopy(DEFAULT_PARAMS)
    params = copy.deepcopy(DEFAULT_PARAMS)
    params["print_mode"] = "shelled_hollow"
    params["stl_always_open_hollow"] = True

    rand_wall_mm = round(rng.uniform(1.8, 4.0), 1)
    rand_bottom_mm = round(max(2.6, rand_wall_mm + rng.uniform(0.6, 1.2)), 1)
    params["wall_thickness_mm"] = rand_wall_mm
    params["bottom_thickness_mm"] = rand_bottom_mm

    # Preserve print mode, slicer settings, and drainage/saucer preferences if current_params was supplied
    if isinstance(current_params, dict):
        for keep_key in (
            "print_mode",
            "stl_always_open_hollow",
            "auto_configure_slicer",
            "spiral_line_width_mm",
            "spiral_bottom_layers",
            "spiral_smooth",
            "wall_thickness_mm",
            "bottom_thickness_mm",
            "drainage",
            "saucer",
            "resolution_angular",
            "resolution_vertical",
        ):
            params[keep_key] = copy.deepcopy(base_state[keep_key])

    params["use_custom_profile"] = False
    height_mm = round(rng.uniform(115.0, 215.0), 1)
    min_stable_base = max(64.0, round(0.40 * height_mm, 1))
    base_diam = round(rng.uniform(min_stable_base, min(126.0, min_stable_base + 38.0)), 1)
    base_r = 0.5 * base_diam

    belly_ratio = round(rng.uniform(0.26, 0.48), 2)
    waist_ratio = round(rng.uniform(belly_ratio + 0.22, 0.82), 2)

    # Bound radial slope dR/dz <= tan(30 deg) (~0.577) so base curve + texture stays well below 45 deg overhang
    max_slope = 0.52
    dz_belly = belly_ratio * height_mm
    max_delta_belly = min(28.0, dz_belly * max_slope)
    belly_r = max(28.0, min(88.0, base_r + rng.uniform(-0.35 * max_delta_belly, max_delta_belly)))

    dz_waist = (waist_ratio - belly_ratio) * height_mm
    max_delta_waist = min(26.0, dz_waist * max_slope)
    waist_r = max(24.0, min(82.0, belly_r + rng.uniform(-max_delta_waist, 0.40 * max_delta_waist)))

    dz_neck = (0.92 - waist_ratio) * height_mm
    max_delta_neck = min(18.0, dz_neck * max_slope)
    neck_r = max(24.0, min(84.0, waist_r + rng.uniform(-0.45 * max_delta_neck, max_delta_neck)))

    dz_lip = 0.08 * height_mm
    max_lip_flare = min(7.0, dz_lip * 0.46)
    lip_flare = round(rng.uniform(-1.5, max_lip_flare), 1)

    params["height_mm"] = height_mm
    params["base_diameter_mm"] = round(base_r * 2.0, 1)
    params["belly_diameter_mm"] = round(belly_r * 2.0, 1)
    params["belly_height_ratio"] = belly_ratio
    params["waist_diameter_mm"] = round(waist_r * 2.0, 1)
    params["waist_height_ratio"] = waist_ratio
    params["neck_diameter_mm"] = round(neck_r * 2.0, 1)
    params["lip_flare_mm"] = lip_flare
    params["lip_bevel_mm"] = round(rng.uniform(0.6, 1.8), 1)

    # Sync profile_points with the generated 5-knot silhouette for seamless switching to custom curve editor
    params["profile_points"] = [
        [0.0, round(base_r, 2)],
        [belly_ratio, round(belly_r, 2)],
        [waist_ratio, round(waist_r, 2)],
        [0.92, round(neck_r, 2)],
        [1.0, round(max(12.0, neck_r + lip_flare), 2)],
    ]

    poly_choices = [0, 0, 0, 0, 5, 6, 7, 8, 9, 10, 12]
    poly_sides = rng.choice(poly_choices)
    params["polygon_sides"] = poly_sides
    params["polygon_roundness"] = round(rng.uniform(0.18, 0.72), 2)
    params["bottom_fade_mm"] = round(rng.uniform(8.0, 16.0), 1)
    params["top_fade_mm"] = round(rng.uniform(6.0, 13.0), 1)
    params["global_twist_deg"] = round(rng.choice([-1, 1]) * rng.choice([0.0, 30.0, 60.0, 90.0, 135.0, 180.0, 240.0]), 1)
    params["auto_clamp_overhang"] = True
    params["max_safe_overhang_deg"] = 46.0

    for t_cfg in params["textures"].values():
        t_cfg["enabled"] = False

    archetypes = [
        ("Ondas Harmônicas", ["waves"]),
        ("Coluna Canelada", ["ribbed"]),
        ("Cristal Origami", ["origami"]),
        ("Coral Orgânico", ["cellular"]),
        ("Trama Ondas & Frisos", ["waves", "ribbed"]),
        ("Cerâmica Texturizada", ["cellular", "waves"]),
    ]
    archetype_label, active_layers = rng.choice(archetypes)
    depth_scale = 0.72 if len(active_layers) > 1 else 1.0

    if "ribbed" in active_layers:
        rib = params["textures"]["ribbed"]
        rib["enabled"] = True
        rib["depth_mm"] = round(rng.uniform(1.5, 3.2) * depth_scale, 2)
        rib["count"] = rng.choice([14, 18, 24, 30, 36, 42, 48, 56])
        rib["duty_cycle"] = round(rng.uniform(0.38, 0.78), 2)
        rib["sharpness"] = round(rng.uniform(0.15, 0.75), 2)
        rib["twist_deg"] = round(rng.choice([-180.0, -90.0, -45.0, 0.0, 0.0, 45.0, 90.0, 180.0]), 1)
        rib["phase_deg"] = round(rng.uniform(0.0, 180.0), 1)

    if "waves" in active_layers:
        wav = params["textures"]["waves"]
        wav["enabled"] = True
        wav["depth_mm"] = round(rng.uniform(1.6, 3.3) * depth_scale, 2)
        wav["vertical_wavelength_mm"] = round(rng.uniform(18.0, 44.0), 1)
        wav["angular_lobes"] = rng.choice([0, 3, 4, 5, 6, 7, 8, 10])
        wav["interference_mix"] = round(rng.uniform(0.0, 0.75), 2)
        wav["wave_skew"] = round(rng.uniform(-0.35, 0.35), 2)
        wav["phase_deg"] = round(rng.uniform(0.0, 360.0), 1)

    if "origami" in active_layers:
        ori = params["textures"]["origami"]
        ori["enabled"] = True
        ori["depth_mm"] = round(rng.uniform(2.0, 3.4) * depth_scale, 2)
        ori["cells_around"] = poly_sides if poly_sides >= 5 else rng.choice([8, 10, 12, 14, 16])
        ori["cells_vertical"] = rng.randint(5, 11)
        ori["crease_sharpness"] = round(rng.uniform(0.55, 0.90), 2)
        ori["stagger"] = rng.choice([0.0, 0.5, 0.5, 0.5])

    if "cellular" in active_layers:
        cel = params["textures"]["cellular"]
        cel["enabled"] = True
        cel["depth_mm"] = round(rng.uniform(1.6, 2.9) * depth_scale, 2)
        cel["scale_angular"] = rng.randint(6, 15)
        cel["scale_vertical_mm"] = round(rng.uniform(15.0, 30.0), 1)
        cel["ridge_mode"] = rng.choice([True, False])
        cel["octaves"] = rng.choice([2, 3])
        cel["seed"] = rng.randint(1, 99999)

    params["name"] = f"{archetype_label} #{actual_seed % 10000:04d}"
    return normalize_params(params)

# ===========================================================================
# MODULE: vase_studio.studio_ui
# ===========================================================================

"""Self-contained offline HTML5 + CSS3 + WebGL2 + 2D Curve Studio UI for Orca Vase Studio.

Generates the interactive 3D & 2D parametric vase design studio for both:
- `mode="page"`: Wide 3-column studio tab inside OrcaSlicer (`PagesPluginCapabilityBase`)
- `mode="dock"`: Compact tabbed side-docked panel beside OrcaSlicer's 3D Plater (`UiDockPanel`)

Zero external CDN scripts, stylesheets, or web fonts are referenced so WebView2 runs 100% offline
without network permission prompts.
"""

pass  # [bundled] hoisted __future__ import

import copy
import json
from typing import Any

if "DEFAULT_PARAMS" not in globals():
    try:
        pass  # [bundled] resolved intra-package import
    except Exception:
        DEFAULT_PARAMS = None  # type: ignore[assignment]

if "BUILTIN_PRESETS" not in globals():
    try:
        pass  # [bundled] resolved intra-package import
    except Exception:
        BUILTIN_PRESETS = None  # type: ignore[assignment]

__all__ = ["get_studio_html"]


def _studio_ui_safe_json(payload: dict[str, Any]) -> str:
    """Serialize payload into script-safe JSON (escaping `</` and line separators)."""
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return (
        raw.replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


_STUDIO_UI_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="__INITIAL_LANG__" data-theme="__INITIAL_THEME__">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Orca Vase Studio</title>
<style>
:root,
[data-theme="dark"] {
  --bg-app: #16181c;
  --bg-panel: #1e2026;
  --bg-card: #252830;
  --bg-card-hover: #2c303a;
  --bg-input: #17191e;
  --bg-viewport-top: #232730;
  --bg-viewport-bot: #121418;
  --bg-hud: rgba(24, 27, 33, 0.86);
  --border-subtle: #313640;
  --border-strong: #414856;
  --text-main: #eef2f6;
  --text-muted: #9aa3b2;
  --text-dim: #6e7787;
  --orca-accent: #00a896;
  --orca-accent-hover: #00bfa5;
  --orca-accent-soft: rgba(0, 191, 165, 0.15);
  --orca-accent-border: rgba(0, 191, 165, 0.48);
  --status-ok: #00c853;
  --status-warn: #ffb300;
  --status-crit: #ff5252;
  --shadow-soft: 0 8px 24px rgba(0, 0, 0, 0.35);
  --radius-sm: 6px;
  --radius-md: 9px;
  --radius-lg: 12px;
  --font-sans: var(--orca-font, "Segoe UI", -apple-system, BlinkMacSystemFont, Roboto, Ubuntu, sans-serif);
  --font-mono: "Cascadia Code", Consolas, "SFMono-Regular", monospace;
}

[data-theme="light"] {
  --bg-app: #eef2f6;
  --bg-panel: #ffffff;
  --bg-card: #f5f7fa;
  --bg-card-hover: #eaeff5;
  --bg-input: #ffffff;
  --bg-viewport-top: #dde4ec;
  --bg-viewport-bot: #c7d1dc;
  --bg-hud: rgba(255, 255, 255, 0.90);
  --border-subtle: #d5dce4;
  --border-strong: #b8c3cf;
  --text-main: #1c222b;
  --text-muted: #556070;
  --text-dim: #7b8696;
  --orca-accent: #00897b;
  --orca-accent-hover: #00796b;
  --orca-accent-soft: rgba(0, 137, 123, 0.12);
  --orca-accent-border: rgba(0, 137, 123, 0.45);
  --status-ok: #1b9e4b;
  --status-warn: #d98200;
  --status-crit: #d93025;
  --shadow-soft: 0 8px 24px rgba(15, 25, 40, 0.10);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--bg-app);
  color: var(--text-main);
  font-family: var(--font-sans);
  font-size: 12.5px;
  line-height: 1.4;
  user-select: none;
  -webkit-font-smoothing: antialiased;
}

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: 99px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--orca-accent);
}

button, input, select {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
}

.studio-shell {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}

/* Header Bar */
.studio-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 7px 12px;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
  z-index: 20;
}

.brand-group {
  display: flex;
  align-items: center;
  gap: 9px;
  min-width: 0;
  flex: 1 1 auto;
}

.brand-logo {
  width: 26px;
  height: 26px;
  border-radius: 7px;
  background: linear-gradient(135deg, #00bfa5 0%, #00796b 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(0, 191, 165, 0.30);
}

.brand-titles {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.brand-name-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.brand-title {
  font-weight: 700;
  font-size: 13.5px;
  letter-spacing: 0.2px;
  white-space: nowrap;
}

.vase-name-input {
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 3px 8px;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-main);
  width: 165px;
  transition: border-color 0.15s;
}
.vase-name-input:focus {
  outline: none;
  border-color: var(--orca-accent);
}

.printer-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 11px;
  border-radius: 99px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  font-size: 11px;
  white-space: nowrap;
  max-width: min(560px, 56vw);
  min-width: 0;
  flex: 0 1 auto;
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s, color 0.15s;
}
.printer-pill:hover {
  border-color: var(--orca-accent-border);
  background: var(--bg-card-hover);
  color: var(--text-main);
}
.printer-pill:active {
  transform: translateY(1px);
}

.printer-pill-text {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-width: 0;
  overflow: hidden;
}

.printer-pill-name {
  min-width: 0;
  max-width: 260px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 600;
  color: var(--text-main);
}

.printer-pill-specs {
  flex-shrink: 0;
  white-space: nowrap;
  color: var(--text-muted);
  font-family: var(--font-mono);
  font-size: 10.6px;
}

.printer-pill-sync {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 11.5px;
  line-height: 1;
  color: var(--orca-accent-hover);
  margin-left: 1px;
  transition: transform 0.38s ease;
}
[data-theme="light"] .printer-pill-sync {
  color: var(--orca-accent);
}
.printer-pill.syncing .printer-pill-sync {
  transform: rotate(360deg);
}

.printer-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--orca-accent-hover);
  flex-shrink: 0;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-shrink: 0;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  padding: 5px 10px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-card);
  color: var(--text-main);
  font-weight: 600;
  font-size: 11.5px;
  cursor: pointer;
  transition: background 0.14s, border-color 0.14s, transform 0.08s;
  white-space: nowrap;
}
.btn:hover:not(:disabled) {
  background: var(--bg-card-hover);
  border-color: var(--border-strong);
}
.btn:active:not(:disabled) {
  transform: translateY(1px);
}
.btn:disabled {
  opacity: 0.42;
  cursor: not-allowed;
}

.btn-icon {
  padding: 5px 7px;
}

.btn-accent {
  background: linear-gradient(135deg, var(--orca-accent) 0%, #00897b 100%);
  border-color: transparent;
  color: #ffffff;
}
.btn-accent:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--orca-accent-hover) 0%, var(--orca-accent) 100%);
  border-color: transparent;
}

.btn-soft {
  background: var(--orca-accent-soft);
  border-color: var(--orca-accent-border);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .btn-soft {
  color: var(--orca-accent);
}
.btn-soft:hover:not(:disabled) {
  background: var(--orca-accent);
  color: #ffffff;
}

/* Main Workspace Grid */
.studio-workspace {
  flex: 1;
  min-height: 0;
  display: grid;
  grid-template-columns: 332px minmax(340px, 1fr) 364px;
  overflow: hidden;
}

.col-panel {
  display: flex;
  flex-direction: column;
  min-height: 0;
  background: var(--bg-panel);
  overflow: hidden;
}
.col-left {
  border-right: 1px solid var(--border-subtle);
}
.col-right {
  border-left: 1px solid var(--border-subtle);
}

.col-scroll {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Dock Mode Navigation Tabs (hidden in wide page mode) */
.dock-tabs {
  display: none;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border-subtle);
  padding: 4px 6px;
  gap: 4px;
  flex-shrink: 0;
}

.dock-tab-btn {
  flex: 1;
  padding: 6px 4px;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: all 0.14s;
}
.dock-tab-btn:hover {
  color: var(--text-main);
  background: var(--bg-card);
}
.dock-tab-btn.active {
  background: var(--orca-accent-soft);
  border-color: var(--orca-accent-border);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .dock-tab-btn.active {
  color: var(--orca-accent);
}

/* Cards & Sections */
.studio-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
}

.card-title {
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.55px;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-badge {
  font-size: 10px;
  font-weight: 600;
  padding: 1px 6px;
  border-radius: 99px;
  background: var(--orca-accent-soft);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .card-badge {
  color: var(--orca-accent);
}

/* Presets Grid */
.preset-filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.filter-chip {
  padding: 3px 7px;
  font-size: 10.5px;
  font-weight: 600;
  border-radius: 99px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-input);
  color: var(--text-muted);
  cursor: pointer;
}
.filter-chip.active {
  background: var(--orca-accent);
  border-color: var(--orca-accent);
  color: #ffffff;
}

.presets-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 6px;
  max-height: 205px;
  overflow-y: auto;
  padding-right: 2px;
}

.preset-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 6px 7px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-panel);
  cursor: pointer;
  transition: border-color 0.14s, background 0.14s;
  text-align: left;
}
.preset-card:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-strong);
}
.preset-card.active {
  border-color: var(--orca-accent-hover);
  background: var(--orca-accent-soft);
}

.preset-thumb {
  width: 30px;
  height: 36px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.preset-meta {
  min-width: 0;
  flex: 1;
}

.preset-name {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-main);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.preset-sub {
  font-size: 9.8px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.preset-del-btn {
  position: absolute;
  top: 3px;
  right: 3px;
  width: 17px;
  height: 17px;
  border-radius: 4px;
  border: none;
  background: rgba(255, 82, 82, 0.16);
  color: var(--status-crit);
  font-size: 11px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
.preset-del-btn:hover {
  background: var(--status-crit);
  color: #ffffff;
}

.save-preset-bar {
  display: none;
  gap: 5px;
  align-items: center;
  padding-top: 4px;
  border-top: 1px dashed var(--border-subtle);
}
.save-preset-bar.open {
  display: flex;
}
.save-preset-input {
  flex: 1;
  min-width: 0;
  background: var(--bg-input);
  border: 1px solid var(--orca-accent-border);
  border-radius: var(--radius-sm);
  padding: 4px 7px;
  font-size: 11.5px;
}

/* Segmented Mode Switch */
.seg-group {
  display: flex;
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 2px;
  gap: 2px;
}

.seg-btn {
  flex: 1;
  padding: 5px 6px;
  border: none;
  border-radius: 4px;
  background: transparent;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.14s;
}
.seg-btn.active {
  background: var(--orca-accent);
  color: #ffffff;
}

/* 2D Curve Canvas Box */
.curve-editor-wrap {
  position: relative;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-input);
  overflow: hidden;
}

#curve-canvas {
  display: block;
  width: 100%;
  height: 220px;
  cursor: crosshair;
  touch-action: none;
}

.curve-overlay-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 8px;
  background: var(--bg-panel);
  border-top: 1px solid var(--border-subtle);
  font-size: 10.5px;
  color: var(--text-muted);
}

.curve-coord-readout {
  font-family: var(--font-mono);
  font-size: 10.5px;
  color: var(--orca-accent-hover);
}
[data-theme="light"] .curve-coord-readout {
  color: var(--orca-accent);
}

.curve-hint {
  font-size: 10.2px;
  color: var(--text-dim);
}

/* Slider Controls */
.ctrl-row {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.ctrl-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
}

.ctrl-label {
  font-size: 11.3px;
  color: var(--text-muted);
  font-weight: 500;
}

.ctrl-val-wrap {
  display: flex;
  align-items: center;
  gap: 3px;
}

.ctrl-num {
  width: 58px;
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: 4px;
  padding: 2px 5px;
  text-align: right;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-main);
}
.ctrl-num:focus {
  outline: none;
  border-color: var(--orca-accent);
}

.ctrl-unit {
  font-size: 10px;
  color: var(--text-dim);
  min-width: 18px;
}

input[type="range"].orca-slider {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 5px;
  border-radius: 99px;
  background: var(--border-strong);
  outline: none;
  cursor: pointer;
}
input[type="range"].orca-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 13px;
  height: 13px;
  border-radius: 50%;
  background: var(--orca-accent-hover);
  border: 2px solid #ffffff;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.4);
  cursor: grab;
  transition: transform 0.1s;
}
input[type="range"].orca-slider::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

/* Toggle Switch */
.switch-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 34px;
  height: 18px;
  flex-shrink: 0;
}
.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}
.toggle-track {
  position: absolute;
  inset: 0;
  background: var(--border-strong);
  border-radius: 99px;
  cursor: pointer;
  transition: background 0.18s;
}
.toggle-track::before {
  content: "";
  position: absolute;
  width: 14px;
  height: 14px;
  left: 2px;
  top: 2px;
  border-radius: 50%;
  background: #ffffff;
  transition: transform 0.18s;
}
.toggle-switch input:checked + .toggle-track {
  background: var(--orca-accent);
}
.toggle-switch input:checked + .toggle-track::before {
  transform: translateX(16px);
}

/* Texture Accordion Layer Cards */
.tex-card {
  background: var(--bg-panel);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  overflow: hidden;
  transition: border-color 0.15s;
}
.tex-card.enabled {
  border-color: var(--orca-accent-border);
}

.tex-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 7px 9px;
  background: var(--bg-card);
  cursor: pointer;
}
.tex-card.enabled .tex-head {
  background: var(--orca-accent-soft);
}

.tex-title-wrap {
  display: flex;
  align-items: center;
  gap: 7px;
  font-weight: 600;
  font-size: 12px;
}

.tex-chevron {
  font-size: 10px;
  color: var(--text-muted);
  transition: transform 0.15s;
}
.tex-card.expanded .tex-chevron {
  transform: rotate(90deg);
}

.tex-body {
  display: none;
  padding: 8px 9px 10px;
  border-top: 1px solid var(--border-subtle);
  flex-direction: column;
  gap: 7px;
}
.tex-card.expanded .tex-body {
  display: flex;
}

/* Center 3D Viewport */
.viewport-col {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  min-height: 0;
  background: radial-gradient(circle at 50% 32%, var(--bg-viewport-top) 0%, var(--bg-viewport-bot) 100%);
  overflow: hidden;
}

#gl-canvas {
  width: 100%;
  height: 100%;
  display: block;
  touch-action: none;
  cursor: grab;
}
#gl-canvas:active {
  cursor: grabbing;
}

#vp-caliper-canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
  pointer-events: none;
  z-index: 5;
}

/* Wall Thickness Quick Presets & Perimeter Hint */
.wall-preset-row {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-top: 1px;
}

.wall-chip {
  flex: 1;
  min-width: 48px;
  padding: 3px 5px;
  border-radius: 5px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-input);
  color: var(--text-muted);
  font-family: var(--font-mono);
  font-size: 10.2px;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: all 0.14s;
}
.wall-chip:hover {
  color: var(--text-main);
  border-color: var(--border-strong);
  background: var(--bg-card-hover);
}
.wall-chip.active {
  background: var(--orca-accent-soft);
  border-color: var(--orca-accent-hover);
  color: var(--orca-accent-hover);
}
[data-theme="light"] .wall-chip.active {
  color: var(--orca-accent);
  border-color: var(--orca-accent);
}

.wall-perim-hint {
  font-size: 10.4px;
  color: var(--orca-accent-hover);
  font-family: var(--font-mono);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  padding: 3px 7px;
  border-radius: 5px;
  background: var(--orca-accent-soft);
  border: 1px solid var(--orca-accent-border);
}
[data-theme="light"] .wall-perim-hint {
  color: var(--orca-accent);
}

/* Floating Viewport Overlays */
.vp-toolbar-left {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 5px;
  max-width: calc(100% - 252px);
  z-index: 10;
}

.vp-glass {
  background: var(--bg-hud);
  backdrop-filter: blur(8px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-soft);
}

.vp-select {
  background: var(--bg-hud);
  color: var(--text-main);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 5px 8px;
  font-size: 11.5px;
  font-weight: 600;
  cursor: pointer;
}

.vp-chip {
  padding: 5px 8px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: var(--bg-hud);
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.vp-chip:hover {
  color: var(--text-main);
  border-color: var(--border-strong);
}
.vp-chip.active {
  background: var(--orca-accent);
  border-color: var(--orca-accent);
  color: #ffffff;
}
.vp-chip-xray {
  border-color: var(--orca-accent-border);
  color: var(--text-main);
}
.vp-chip-xray.active {
  background: linear-gradient(135deg, #00bfa5 0%, #ff8f00 130%);
  border-color: transparent;
  color: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 191, 165, 0.35);
}

.spiral-mode-banner {
  display: none;
  position: absolute;
  top: 48px;
  left: 10px;
  max-width: calc(100% - 256px);
  padding: 5px 10px;
  font-size: 10.6px;
  font-weight: 600;
  line-height: 1.3;
  z-index: 12;
  border-left: 3px solid var(--orca-accent-hover);
  color: var(--text-main);
  pointer-events: none;
}
.spiral-mode-banner.visible {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.spiral-mode-banner.warn {
  border-left-color: var(--status-warn);
  background: rgba(45, 34, 14, 0.90);
}
[data-theme="light"] .spiral-mode-banner.warn {
  background: rgba(255, 245, 224, 0.94);
}

.vp-cam-bar {
  position: absolute;
  bottom: 56px;
  left: 10px;
  display: flex;
  gap: 4px;
  z-index: 10;
}

.vp-cut-bar {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 6px 10px;
  z-index: 10;
}

.vp-cut-modes {
  display: inline-flex;
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 2px;
  gap: 2px;
  flex-shrink: 0;
}

.vp-cut-mode-btn {
  padding: 3px 7px;
  border: none;
  border-radius: 4px;
  background: transparent;
  color: var(--text-muted);
  font-size: 10.5px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.14s;
}
.vp-cut-mode-btn:hover {
  color: var(--text-main);
}
.vp-cut-mode-btn.active {
  background: var(--orca-accent);
  color: #ffffff;
}

.vp-cut-label {
  font-size: 11px;
  font-weight: 600;
  white-space: nowrap;
  color: var(--text-muted);
}

/* Printability HUD */
.vp-hud-right {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 236px;
  padding: 9px 11px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  z-index: 10;
}

.hud-title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 10.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-muted);
}

.hud-status-pill {
  padding: 1px 7px;
  border-radius: 99px;
  font-size: 10px;
  font-weight: 700;
}
.hud-status-pill.ok {
  background: rgba(0, 200, 83, 0.18);
  color: var(--status-ok);
}
.hud-status-pill.warn {
  background: rgba(255, 179, 0, 0.20);
  color: var(--status-warn);
}
.hud-status-pill.crit {
  background: rgba(255, 82, 82, 0.22);
  color: var(--status-crit);
}

.hud-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px 8px;
}

.hud-metric {
  display: flex;
  flex-direction: column;
}
.hud-metric-k {
  font-size: 9.8px;
  color: var(--text-dim);
}
.hud-metric-v {
  font-family: var(--font-mono);
  font-size: 11.2px;
  font-weight: 600;
  color: var(--text-main);
}

.hud-warnings {
  display: flex;
  flex-direction: column;
  gap: 3px;
  max-height: 92px;
  overflow-y: auto;
}

.hud-warn-item {
  font-size: 10.2px;
  padding: 3px 6px;
  border-radius: 4px;
  background: rgba(255, 179, 0, 0.13);
  border-left: 2px solid var(--status-warn);
  color: var(--text-main);
}
.hud-warn-item.crit {
  background: rgba(255, 82, 82, 0.15);
  border-left-color: var(--status-crit);
}

.heatmap-legend {
  display: none;
  align-items: center;
  gap: 6px;
  font-size: 10px;
  padding-top: 4px;
  border-top: 1px solid var(--border-subtle);
  color: var(--text-muted);
}
.heatmap-legend.visible {
  display: flex;
}
.legend-swatch {
  width: 9px;
  height: 9px;
  border-radius: 2px;
  display: inline-block;
}

.bed-alert-banner {
  display: none;
  position: absolute;
  top: 52px;
  left: 50%;
  transform: translateX(-50%);
  padding: 6px 12px 6px 14px;
  border-radius: 99px;
  background: rgba(213, 0, 0, 0.90);
  color: #ffffff;
  font-weight: 700;
  font-size: 11.5px;
  box-shadow: 0 4px 16px rgba(213, 0, 0, 0.45);
  z-index: 15;
  pointer-events: auto;
  white-space: nowrap;
}
.bed-alert-banner.visible {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.bed-fit-btn {
  padding: 2px 9px;
  border-radius: 99px;
  border: 1px solid rgba(255, 255, 255, 0.65);
  background: rgba(255, 255, 255, 0.18);
  color: #ffffff;
  font-size: 10.5px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.14s;
}
.bed-fit-btn:hover {
  background: rgba(255, 255, 255, 0.32);
}

/* Right Action Footer */
.action-footer {
  padding: 10px;
  background: var(--bg-panel);
  border-top: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  gap: 7px;
  flex-shrink: 0;
}

.btn-hero {
  width: 100%;
  padding: 10px 14px;
  font-size: 13px;
  font-weight: 700;
  border-radius: var(--radius-md);
  background: linear-gradient(135deg, #00bfa5 0%, #00897b 100%);
  color: #ffffff;
  border: none;
  box-shadow: 0 4px 14px rgba(0, 191, 165, 0.32);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: filter 0.15s, transform 0.08s;
}
.btn-hero:hover:not(:disabled) {
  filter: brightness(1.07);
}
.btn-hero:active:not(:disabled) {
  transform: translateY(1px);
}
.btn-hero:disabled {
  opacity: 0.55;
  cursor: wait;
}

.export-btn-row {
  display: grid;
  grid-template-columns: 1fr 1fr auto;
  gap: 6px;
}

.helper-note {
  font-size: 10.5px;
  color: var(--text-muted);
  background: var(--bg-input);
  border-left: 2px solid var(--orca-accent);
  padding: 5px 7px;
  border-radius: 0 4px 4px 0;
}

.helper-note.warn {
  border-left-color: var(--status-warn);
  background: rgba(255, 179, 0, 0.10);
}

/* Toast Notification */
.toast-banner {
  position: fixed;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  opacity: 0;
  pointer-events: none;
  padding: 8px 16px;
  border-radius: var(--radius-md);
  background: var(--bg-card);
  border: 1px solid var(--orca-accent);
  color: var(--text-main);
  font-size: 12px;
  font-weight: 600;
  box-shadow: var(--shadow-soft);
  transition: opacity 0.2s, transform 0.2s;
  z-index: 999;
  max-width: 90vw;
}
.toast-banner.visible {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
.toast-banner.error {
  border-color: var(--status-crit);
}

/* ============================================================================
   COMPACT SIDE-DOCK MODE (`data-mode="dock"` or narrow viewports <= 960px)
   ============================================================================ */
body[data-mode="dock"] .printer-pill,
body[data-mode="dock"] .brand-title {
  display: none;
}

body[data-mode="dock"] .vase-name-input {
  width: 118px;
}

body[data-mode="dock"] .studio-workspace {
  display: flex;
  flex-direction: column;
}

body[data-mode="dock"] .viewport-col {
  order: -1;
  height: 245px;
  flex-shrink: 0;
  border-bottom: 1px solid var(--border-subtle);
}

body[data-mode="dock"] .vp-hud-right {
  width: 172px;
  padding: 5px 7px;
  gap: 3px;
}
body[data-mode="dock"] .hud-warnings,
body[data-mode="dock"] .spiral-mode-banner {
  display: none;
}
body[data-mode="dock"] .vp-cam-bar {
  display: none;
}
body[data-mode="dock"] .vp-cut-bar {
  padding: 4px 6px;
  bottom: 6px;
  gap: 4px;
}
body[data-mode="dock"] .vp-cut-mode-btn {
  padding: 2px 5px;
  font-size: 9.8px;
}

body[data-mode="dock"] .dock-tabs {
  display: flex;
  order: 0;
}

body[data-mode="dock"] .col-left,
body[data-mode="dock"] .col-right {
  border: none;
  flex: 1;
  min-height: 0;
}

body[data-mode="dock"] .col-right .action-footer {
  display: none;
}

.dock-global-footer {
  display: none;
}
body[data-mode="dock"] .dock-global-footer {
  display: flex;
}

body[data-mode="dock"][data-dock-tab="shape"] .col-right {
  display: none;
}
body[data-mode="dock"][data-dock-tab="shape"] #card-presets {
  display: none;
}

body[data-mode="dock"][data-dock-tab="presets"] .col-right {
  display: none;
}
body[data-mode="dock"][data-dock-tab="presets"] #card-silhouette,
body[data-mode="dock"][data-dock-tab="presets"] #card-resolution {
  display: none;
}
body[data-mode="dock"][data-dock-tab="presets"] .presets-grid {
  max-height: none;
}

body[data-mode="dock"][data-dock-tab="textures"] .col-left {
  display: none;
}
body[data-mode="dock"][data-dock-tab="textures"] #card-print-mode,
body[data-mode="dock"][data-dock-tab="textures"] #card-gardening {
  display: none;
}

body[data-mode="dock"][data-dock-tab="print"] .col-left {
  display: none;
}
body[data-mode="dock"][data-dock-tab="print"] #card-envelope,
body[data-mode="dock"][data-dock-tab="print"] #card-textures {
  display: none;
}

@media (max-width: 960px) {
  .printer-pill {
    display: none;
  }
  .studio-workspace {
    grid-template-columns: 280px minmax(260px, 1fr) 300px;
  }
}
</style>
</head>
<body data-mode="__INITIAL_MODE__" data-dock-tab="shape">
<div class="studio-shell">
  <!-- TOP HEADER -->
  <header class="studio-header">
    <div class="brand-group">
      <div class="brand-logo" title="Orca Vase Studio">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M8 3h8l-1.5 4.5c2.5 2.5 3.5 5.5 2.5 9.5-.7 2.5-2.3 4-5 4s-4.3-1.5-5-4c-1-4 0-7 2.5-9.5L8 3z"/>
          <path d="M6.5 13.5c3.5-1.8 7.5 1.8 11 0"/>
        </svg>
      </div>
      <div class="brand-titles">
        <div class="brand-name-row">
          <span class="brand-title">Orca Vase Studio</span>
          <input id="inp-vase-name" class="vase-name-input" type="text" maxlength="80" value="Ondas Organicas" aria-label="Design Name" />
        </div>
      </div>
      <button id="printer-pill" type="button" class="printer-pill" title="Clique para sincronizar impressora ativa do OrcaSlicer">
        <span class="printer-dot"></span>
        <span id="printer-pill-text" class="printer-pill-text">
          <span id="printer-pill-name" class="printer-pill-name">Generic 3D Printer</span>
          <span id="printer-pill-specs" class="printer-pill-specs">· 220×220×250 mm · 0.4mm</span>
        </span>
        <span id="printer-pill-sync" class="printer-pill-sync" aria-hidden="true">↻</span>
      </button>
    </div>

    <div class="header-actions">
      <button id="btn-undo" class="btn btn-icon" title="Undo (Ctrl+Z)" disabled>↶</button>
      <button id="btn-redo" class="btn btn-icon" title="Redo (Ctrl+Y)" disabled>↷</button>
      <button id="btn-randomize" class="btn btn-soft">
        <span>🎲</span>
        <span data-i18n="btn_surprise">Surpreenda-me</span>
      </button>
      <button id="btn-reset" class="btn btn-icon" title="Reset">↺</button>
      <button id="btn-lang" class="btn btn-icon" title="Português / English">PT</button>
      <button id="btn-theme" class="btn btn-icon" title="Dark / Light">☾</button>
    </div>
  </header>

  <!-- DOCK MODE TABS -->
  <nav class="dock-tabs" aria-label="Studio Sections">
    <button class="dock-tab-btn active" data-tab="shape" data-i18n="tab_shape">Forma</button>
    <button class="dock-tab-btn" data-tab="textures" data-i18n="tab_textures">Texturas</button>
    <button class="dock-tab-btn" data-tab="print" data-i18n="tab_print">Impressão</button>
    <button class="dock-tab-btn" data-tab="presets" data-i18n="tab_presets">Presets</button>
  </nav>

  <!-- MAIN 3-COLUMN WORKSPACE -->
  <main class="studio-workspace">
    <!-- LEFT COLUMN: PRESETS + SILHOUETTE + 2D CURVE EDITOR -->
    <section class="col-panel col-left">
      <div class="col-scroll">
        <!-- Presets Gallery Card -->
        <div id="card-presets" class="studio-card">
          <div class="card-head">
            <span class="card-title" data-i18n="sec_presets">Galeria de Modelos</span>
            <button id="btn-toggle-save-preset" class="btn btn-soft" style="padding:2px 8px;font-size:10.5px;" data-i18n="btn_save_preset">+ Salvar</button>
          </div>
          <div id="save-preset-bar" class="save-preset-bar">
            <input id="inp-save-preset-name" class="save-preset-input" type="text" maxlength="64" placeholder="Nome do preset..." />
            <button id="btn-confirm-save-preset" class="btn btn-accent" style="padding:4px 8px;" data-i18n="btn_ok">Salvar</button>
          </div>
          <div id="preset-filters" class="preset-filter-row">
            <button class="filter-chip active" data-cat="all" data-i18n="cat_all">Todos</button>
            <button class="filter-chip" data-cat="organic" data-i18n="cat_organic">Orgânicos</button>
            <button class="filter-chip" data-cat="geometric" data-i18n="cat_geometric">Geométricos</button>
            <button class="filter-chip" data-cat="planter" data-i18n="cat_planter">Cachepôs</button>
            <button class="filter-chip" data-cat="user" data-i18n="cat_user">Meus</button>
          </div>
          <div id="presets-grid" class="presets-grid"></div>
        </div>

        <!-- Base Silhouette & Interactive 2D Curve Editor -->
        <div id="card-silhouette" class="studio-card">
          <div class="card-head">
            <span class="card-title" data-i18n="sec_silhouette">Silhueta & Curva 2D</span>
            <span id="poly-badge" class="card-badge">Circular</span>
          </div>

          <div class="seg-group">
            <button id="btn-prof-sliders" class="seg-btn active" data-i18n="mode_sliders">Sliders</button>
            <button id="btn-prof-curve" class="seg-btn" data-i18n="mode_curve">Curva Livre 2D</button>
          </div>

          <div class="curve-editor-wrap">
            <canvas id="curve-canvas" width="300" height="220"></canvas>
            <div class="curve-overlay-bar">
              <span id="curve-coord-readout" class="curve-coord-readout">Z 0.0 · Ø 76.0 mm</span>
              <button id="btn-sliders-to-curve" class="btn" style="padding:2px 6px;font-size:10px;" data-i18n="btn_to_curve">Sliders → Curva</button>
            </div>
          </div>
          <div id="curve-hint" class="curve-hint" data-i18n="hint_curve_sliders">Arraste os pontos na silhueta ou ajuste os controles abaixo.</div>

          <div id="sliders-silhouette-group" style="display:flex;flex-direction:column;gap:7px;">
            <div data-slider="height_mm"></div>
            <div id="parametric-diameters-box" style="display:flex;flex-direction:column;gap:7px;">
              <div data-slider="base_diameter_mm"></div>
              <div data-slider="belly_diameter_mm"></div>
              <div data-slider="belly_height_ratio"></div>
              <div data-slider="waist_diameter_mm"></div>
              <div data-slider="waist_height_ratio"></div>
              <div data-slider="neck_diameter_mm"></div>
              <div data-slider="lip_flare_mm"></div>
            </div>
            <div data-slider="lip_bevel_mm"></div>
            <div data-slider="polygon_sides"></div>
            <div data-slider="polygon_roundness"></div>
          </div>
        </div>

        <!-- Mesh Resolution Card -->
        <div id="card-resolution" class="studio-card">
          <div class="card-head">
            <span class="card-title" data-i18n="sec_resolution">Resolução da Malha</span>
          </div>
          <div data-slider="resolution_angular"></div>
          <div data-slider="resolution_vertical"></div>
        </div>
      </div>
    </section>

    <!-- CENTER COLUMN: INTERACTIVE 3D WEBGL2 VIEWPORT -->
    <section class="viewport-col">
      <canvas id="gl-canvas"></canvas>
      <canvas id="vp-caliper-canvas"></canvas>

      <!-- Top-Left Material & View Controls -->
      <div class="vp-toolbar-left">
        <select id="sel-material" class="vp-select" aria-label="Material">
          <option value="emerald_silk" data-i18n="mat_emerald">Seda Esmeralda Orca</option>
          <option value="terracotta" data-i18n="mat_terracotta">Cerâmica Terracota</option>
          <option value="matte_ceramic" data-i18n="mat_white">Porcelana Branca Mate</option>
          <option value="copper_bronze" data-i18n="mat_copper">Bronze Cobre Escovado</option>
          <option value="xray" data-i18n="mat_xray">🔬 Raio-X / Parede (Translúcido)</option>
          <option value="heatmap" data-i18n="mat_heatmap">Mapa de Overhang (°)</option>
        </select>
        <button id="btn-vp-xray" class="vp-chip vp-chip-xray" data-i18n="vp_xray">🔬 Raio-X / Parede</button>
        <button id="btn-vp-calipers" class="vp-chip" data-i18n="vp_calipers">📏 Cotas mm</button>
        <button id="btn-vp-heatmap" class="vp-chip" data-i18n="vp_heatmap">🔥 Overhang</button>
        <button id="btn-vp-wire" class="vp-chip" data-i18n="vp_wire">⌗ Malha</button>
        <button id="btn-vp-saucer" class="vp-chip" data-i18n="vp_saucer">🍽 Pratinho</button>
        <button id="btn-vp-saucer-layout" class="vp-chip" style="display:none;" data-i18n="vp_layout_nested">Encaixado</button>
        <button id="btn-vp-spin" class="vp-chip" title="Auto-Rotate">⟳</button>
      </div>

      <!-- Honest Spiral Mode Viewport Info Badge -->
      <div id="spiral-mode-banner" class="spiral-mode-banner vp-glass">
        <span id="spiral-banner-icon">🌀</span>
        <span id="spiral-banner-text">Modo Espiral: malha base p/ .3MF · .STL protegido c/ Boca Aberta</span>
      </div>

      <!-- Out-of-bed live warning -->
      <div id="bed-alert-banner" class="bed-alert-banner">
        <span>⚠</span>
        <span id="bed-alert-text">Dimensões excedem o volume da impressora!</span>
        <button id="btn-fit-to-printer" type="button" class="bed-fit-btn" data-i18n="btn_fit_printer">Ajustar à Mesa</button>
      </div>

      <!-- Top-Right Live Printability & Dimensions HUD -->
      <aside id="vp-hud-right" class="vp-hud-right vp-glass">
        <div class="hud-title-row">
          <span data-i18n="hud_title">Printabilidade</span>
          <span id="hud-status-pill" class="hud-status-pill ok">OK</span>
        </div>
        <div class="hud-grid">
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_wall_floor">Parede / Fundo</span>
            <span id="hud-wall-floor" class="hud-metric-v">2.4 / 3.2 mm</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_mouth_hole">Ø Furo Boca</span>
            <span id="hud-mouth-hole" class="hud-metric-v">Ø 85.2 mm</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_dims">Dimensões (mm)</span>
            <span id="hud-dims" class="hud-metric-v">116×116×160</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_overhang">Overhang Máx</span>
            <span id="hud-overhang" class="hud-metric-v">28.4°</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_weight">Filamento Est.</span>
            <span id="hud-weight" class="hud-metric-v">~48 g</span>
          </div>
          <div class="hud-metric">
            <span class="hud-metric-k" data-i18n="hud_Tris">Triângulos</span>
            <span id="hud-tris" class="hud-metric-v">105k</span>
          </div>
        </div>
        <div id="xray-legend" class="heatmap-legend">
          <span><i class="legend-swatch" style="background:#0fd6c2"></i><span data-i18n="leg_outer">Externa</span></span>
          <span><i class="legend-swatch" style="background:#ff8c38"></i><span data-i18n="leg_inner">Cavidade &amp; Fundo</span></span>
        </div>
        <div id="heatmap-legend" class="heatmap-legend">
          <span><i class="legend-swatch" style="background:#00c853"></i>≤45°</span>
          <span><i class="legend-swatch" style="background:#ffb300"></i>45–55°</span>
          <span><i class="legend-swatch" style="background:#ff3d00"></i>&gt;55°</span>
        </div>
        <div id="hud-warnings" class="hud-warnings"></div>
      </aside>

      <!-- Camera Preset Pills -->
      <div class="vp-cam-bar">
        <button class="vp-chip" data-cam="iso">Iso</button>
        <button class="vp-chip" data-cam="front" data-i18n="cam_front">Frente</button>
        <button class="vp-chip" data-cam="top" data-i18n="cam_top">Topo</button>
        <button class="vp-chip" data-cam="bottom" data-i18n="cam_bottom">Base</button>
        <button class="vp-chip" data-cam="fit" data-i18n="cam_fit">Enquadrar</button>
      </div>

      <!-- Bottom Dual Section Inspector Slider (Vertical Profile Y + Horizontal Plan Slice Z) -->
      <div class="vp-cut-bar vp-glass">
        <div class="vp-cut-modes" role="group" aria-label="Section Cut Mode">
          <button id="btn-cut-mode-y" class="vp-cut-mode-btn active" data-i18n="vp_cut_y">✂ Corte Vertical (Perfil Y)</button>
          <button id="btn-cut-mode-z" class="vp-cut-mode-btn" data-i18n="vp_cut_z">💿 Fatia Horizontal Z (Planta 5%–100%)</button>
        </div>
        <input id="inp-cross-cut" class="orca-slider" type="range" min="0" max="100" step="1" value="0" />
        <span id="lbl-cross-cut" class="ctrl-num" style="width:62px;text-align:center;">Off</span>
        <button id="btn-cut-half" class="btn" style="padding:3px 7px;font-size:10.5px;">50%</button>
        <button id="btn-cut-off" class="btn" style="padding:3px 7px;font-size:10.5px;">Off</button>
      </div>
    </section>

    <!-- RIGHT COLUMN: WALL & OPENING (TOP) + TEXTURE LAYERS + ENVELOPE + GARDENING + ACTIONS -->
    <section class="col-panel col-right">
      <div class="col-scroll">
        <!-- 1. Wall Thickness & Mouth Opening (Elevated to Top of Right Column!) -->
        <div id="card-print-mode" class="studio-card" style="border-color:var(--orca-accent-border);">
          <div class="card-head">
            <span class="card-title" data-i18n="sec_print_mode">Parede &amp; Abertura (mm)</span>
            <span id="wall-mode-badge" class="card-badge">Oco · 2.4 mm</span>
          </div>

          <div class="seg-group">
            <button id="btn-mode-hollow" class="seg-btn active" data-i18n="mode_hollow">Vaso Oco Real (Parede em mm)</button>
            <button id="btn-mode-spiral" class="seg-btn" data-i18n="mode_spiral">Modo Espiral (1 Linha)</button>
          </div>

          <div id="box-hollow-opts" style="display:flex;flex-direction:column;gap:7px;">
            <div data-slider="wall_thickness_mm"></div>
            <div id="wall-preset-chips" class="wall-preset-row">
              <button type="button" class="wall-chip" data-wall-preset="1.2">1.2 mm</button>
              <button type="button" class="wall-chip active" data-wall-preset="2.4">2.4 mm</button>
              <button type="button" class="wall-chip" data-wall-preset="4.0">4.0 mm</button>
              <button type="button" class="wall-chip" data-wall-preset="8.0">8.0 mm</button>
              <button type="button" class="wall-chip" data-wall-preset="15.0">15.0 mm</button>
            </div>
            <div id="wall-perim-hint" class="wall-perim-hint">≈ 6 voltas de 0.42 mm</div>
            <div data-slider="bottom_thickness_mm"></div>
          </div>

          <div id="box-spiral-opts" style="display:none;flex-direction:column;gap:7px;">
            <div id="spiral-mode-note" class="helper-note warn" data-i18n="note_spiral_honest">
              O Modo Espiral gera um bloco base cujo topo é removido pelo fatiador (.3MF). Para exportar .STL sempre aberto, mantenha a proteção abaixo ativa!
            </div>
            <div data-slider="spiral_line_width_mm"></div>
            <div data-slider="spiral_bottom_layers"></div>
            <div id="spiral-floor-hint" class="wall-perim-hint">≈ 1.0 mm de fundo sólido</div>
            <div class="switch-row">
              <span class="ctrl-label" data-i18n="lbl_spiral_smooth">Suavizar Costura Espiral XY</span>
              <label class="toggle-switch">
                <input id="chk-spiral-smooth" type="checkbox" checked />
                <span class="toggle-track"></span>
              </label>
            </div>
          </div>

          <div style="border-top:1px solid var(--border-subtle);padding-top:7px;display:flex;flex-direction:column;gap:6px;">
            <div class="switch-row">
              <span class="ctrl-label" data-i18n="lbl_stl_open_hollow">Manter boca aberta ao exportar .STL</span>
              <label class="toggle-switch">
                <input id="chk-stl-open-hollow" type="checkbox" checked />
                <span class="toggle-track"></span>
              </label>
            </div>
            <div class="switch-row">
              <span class="ctrl-label" data-i18n="lbl_auto_slicer">Auto-ajustar OrcaSlicer ao enviar</span>
              <label class="toggle-switch">
                <input id="chk-auto-slicer" type="checkbox" checked />
                <span class="toggle-track"></span>
              </label>
            </div>
            <div class="switch-row">
              <span class="ctrl-label" data-i18n="lbl_clamp_overhang">Limitar Overhang Automaticamente</span>
              <label class="toggle-switch">
                <input id="chk-clamp-overhang" type="checkbox" />
                <span class="toggle-track"></span>
              </label>
            </div>
            <div data-slider="max_safe_overhang_deg"></div>
          </div>
        </div>

        <!-- 2. Combinable Surface Textures -->
        <div id="card-textures" class="studio-card">
          <div class="card-head">
            <span class="card-title" data-i18n="sec_textures">Texturas Combináveis</span>
            <span id="active-tex-badge" class="card-badge">1 ativa</span>
          </div>

          <!-- 1. Ribbed / Canelado (collapsed by default so Wall + Textures fit above the fold) -->
          <div class="tex-card" data-tex-card="ribbed">
            <div class="tex-head" data-tex-toggle-expand="ribbed">
              <div class="tex-title-wrap">
                <span class="tex-chevron">▶</span>
                <span data-i18n="tex_ribbed">Canelado / Frisos</span>
              </div>
              <label class="toggle-switch" onclick="event.stopPropagation()">
                <input id="chk-tex-ribbed" type="checkbox" />
                <span class="toggle-track"></span>
              </label>
            </div>
            <div class="tex-body">
              <div data-slider="textures.ribbed.depth_mm"></div>
              <div data-slider="textures.ribbed.count"></div>
              <div data-slider="textures.ribbed.duty_cycle"></div>
              <div data-slider="textures.ribbed.sharpness"></div>
              <div data-slider="textures.ribbed.twist_deg"></div>
              <div data-slider="textures.ribbed.phase_deg"></div>
            </div>
          </div>

          <!-- 2. Organic Waves / Ondas -->
          <div class="tex-card enabled expanded" data-tex-card="waves">
            <div class="tex-head" data-tex-toggle-expand="waves">
              <div class="tex-title-wrap">
                <span class="tex-chevron">▶</span>
                <span data-i18n="tex_waves">Ondas Orgânicas</span>
              </div>
              <label class="toggle-switch" onclick="event.stopPropagation()">
                <input id="chk-tex-waves" type="checkbox" checked />
                <span class="toggle-track"></span>
              </label>
            </div>
            <div class="tex-body">
              <div data-slider="textures.waves.depth_mm"></div>
              <div data-slider="textures.waves.vertical_wavelength_mm"></div>
              <div data-slider="textures.waves.angular_lobes"></div>
              <div data-slider="textures.waves.interference_mix"></div>
              <div data-slider="textures.waves.wave_skew"></div>
              <div data-slider="textures.waves.phase_deg"></div>
            </div>
          </div>

          <!-- 3. Origami / Yoshimura -->
          <div class="tex-card" data-tex-card="origami">
            <div class="tex-head" data-tex-toggle-expand="origami">
              <div class="tex-title-wrap">
                <span class="tex-chevron">▶</span>
                <span data-i18n="tex_origami">Origami Diamante</span>
              </div>
              <label class="toggle-switch" onclick="event.stopPropagation()">
                <input id="chk-tex-origami" type="checkbox" />
                <span class="toggle-track"></span>
              </label>
            </div>
            <div class="tex-body">
              <div data-slider="textures.origami.depth_mm"></div>
              <div data-slider="textures.origami.cells_around"></div>
              <div data-slider="textures.origami.cells_vertical"></div>
              <div data-slider="textures.origami.crease_sharpness"></div>
              <div data-slider="textures.origami.stagger"></div>
            </div>
          </div>

          <!-- 4. Cellular / Coral -->
          <div class="tex-card" data-tex-card="cellular">
            <div class="tex-head" data-tex-toggle-expand="cellular">
              <div class="tex-title-wrap">
                <span class="tex-chevron">▶</span>
                <span data-i18n="tex_cellular">Celular / Coral 3D</span>
              </div>
              <label class="toggle-switch" onclick="event.stopPropagation()">
                <input id="chk-tex-cellular" type="checkbox" />
                <span class="toggle-track"></span>
              </label>
            </div>
            <div class="tex-body">
              <div data-slider="textures.cellular.depth_mm"></div>
              <div data-slider="textures.cellular.scale_angular"></div>
              <div data-slider="textures.cellular.scale_vertical_mm"></div>
              <div class="switch-row">
                <span class="ctrl-label" data-i18n="lbl_ridge_mode">Veios em Crista (Coral)</span>
                <label class="toggle-switch">
                  <input id="chk-cel-ridge" type="checkbox" checked />
                  <span class="toggle-track"></span>
                </label>
              </div>
              <div data-slider="textures.cellular.octaves"></div>
              <div style="display:flex;align-items:flex-end;gap:6px;">
                <div style="flex:1;" data-slider="textures.cellular.seed"></div>
                <button id="btn-reseed" class="btn btn-icon" title="New Seed">🎲</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Global Envelope & Twist -->
        <div id="card-envelope" class="studio-card">
          <div class="card-head">
            <span class="card-title" data-i18n="sec_envelope">Envelope &amp; Torção Global</span>
          </div>
          <div data-slider="bottom_fade_mm"></div>
          <div data-slider="top_fade_mm"></div>
          <div data-slider="global_twist_deg"></div>
        </div>

        <!-- Gardening: Drainage & Saucer -->
        <div id="card-gardening" class="studio-card">
          <div class="card-head">
            <span class="card-title" data-i18n="sec_gardening">Jardinagem: Drenagem & Prato</span>
          </div>

          <div class="switch-row">
            <span class="ctrl-label" data-i18n="lbl_drainage">Furos de Drenagem na Base</span>
            <label class="toggle-switch">
              <input id="chk-drainage" type="checkbox" />
              <span class="toggle-track"></span>
            </label>
          </div>

          <div id="box-drainage-opts" style="display:none;flex-direction:column;gap:7px;">
            <div id="drainage-mode-note" class="helper-note" data-i18n="note_drainage_spiral">
              Cavidades cegas nas camadas sólidas da base: furos reais sem quebrar o contorno único do Modo Espiral!
            </div>
            <div data-slider="drainage.hole_count"></div>
            <div data-slider="drainage.hole_diameter_mm"></div>
            <div data-slider="drainage.ring_radius_ratio"></div>
          </div>

          <div style="border-top:1px solid var(--border-subtle);padding-top:7px;display:flex;flex-direction:column;gap:7px;">
            <div class="switch-row">
              <span class="ctrl-label" data-i18n="lbl_include_saucer">Incluir Pratinho Coordenado</span>
              <label class="toggle-switch">
                <input id="chk-include-saucer" type="checkbox" />
                <span class="toggle-track"></span>
              </label>
            </div>

            <div id="box-saucer-opts" style="display:none;flex-direction:column;gap:7px;">
              <div id="saucer-spiral-warn" class="helper-note warn" style="display:none;" data-i18n="warn_saucer_spiral">
                Vaso + Prato juntos na mesa desativam o Modo Espiral global (use Parede Oca ou envie separados).
              </div>
              <div data-slider="saucer.clearance_mm"></div>
              <div data-slider="saucer.rim_height_mm"></div>
              <div data-slider="saucer.wall_thickness_mm"></div>
              <div data-slider="saucer.floor_thickness_mm"></div>
              <div data-slider="saucer.inner_ribs_height_mm"></div>
              <div class="switch-row">
                <span class="ctrl-label" data-i18n="lbl_saucer_tex">Repetir Textura do Vaso no Prato</span>
                <label class="toggle-switch">
                  <input id="chk-saucer-tex" type="checkbox" checked />
                  <span class="toggle-track"></span>
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Wide Mode Sticky Action Footer -->
      <footer class="action-footer">
        <button class="btn-hero" data-action="send_to_plater">
          <span>🚀</span>
          <span data-i18n="btn_send_plater">Enviar para a Mesa do OrcaSlicer</span>
        </button>
        <div class="export-btn-row">
          <button class="btn" data-action="export_3mf">💾 <span data-i18n="btn_exp_3mf">Exportar .3MF</span></button>
          <button class="btn" data-action="export_stl">📐 <span data-i18n="btn_exp_stl">Exportar .STL</span></button>
          <button class="btn btn-icon" data-action="open_folder" title="Open Exports Folder">📂</button>
        </div>
      </footer>
    </section>
  </main>

  <!-- Compact Dock Mode Sticky Footer -->
  <footer class="action-footer dock-global-footer">
    <button class="btn-hero" data-action="send_to_plater" style="padding:8px 10px;font-size:12px;">
      <span>🚀</span>
      <span data-i18n="btn_send_plater">Enviar para a Mesa do OrcaSlicer</span>
    </button>
    <div class="export-btn-row">
      <button class="btn" data-action="export_3mf">💾 .3MF</button>
      <button class="btn" data-action="export_stl">📐 .STL</button>
      <button class="btn btn-icon" data-action="open_folder" title="Open Exports Folder">📂</button>
    </div>
  </footer>
</div>

<div id="toast-banner" class="toast-banner" role="status" aria-live="polite"></div>

<script>
(function () {
  "use strict";

  const BOOT_PAYLOAD = __ORCA_VASE_STUDIO_BOOT_JSON__;

  // ==========================================================================
  // 1. Canonical Parameter Schema & Normalization (100% Parity with schema.py)
  // ==========================================================================
  const JS_DEFAULT_PARAMS = {
    name: "Ondas Organicas",
    height_mm: 160.0,
    base_diameter_mm: 76.0,
    belly_diameter_mm: 110.0,
    belly_height_ratio: 0.34,
    waist_diameter_mm: 68.0,
    waist_height_ratio: 0.68,
    neck_diameter_mm: 82.0,
    lip_flare_mm: 4.0,
    lip_bevel_mm: 1.0,
    polygon_sides: 0,
    polygon_roundness: 0.35,
    use_custom_profile: false,
    profile_points: [
      [0.0, 38.0],
      [0.34, 55.0],
      [0.68, 34.0],
      [0.92, 41.0],
      [1.0, 45.0]
    ],
    resolution_angular: 240,
    resolution_vertical: 220,
    bottom_fade_mm: 8.0,
    top_fade_mm: 6.0,
    global_twist_deg: 0.0,
    textures: {
      ribbed: {
        enabled: false,
        depth_mm: 2.6,
        count: 32,
        duty_cycle: 0.50,
        sharpness: 0.35,
        twist_deg: 60.0,
        phase_deg: 0.0
      },
      waves: {
        enabled: true,
        depth_mm: 3.0,
        vertical_wavelength_mm: 26.0,
        angular_lobes: 6,
        interference_mix: 0.45,
        wave_skew: 0.0,
        phase_deg: 0.0
      },
      origami: {
        enabled: false,
        depth_mm: 3.2,
        cells_around: 12,
        cells_vertical: 8,
        crease_sharpness: 0.75,
        stagger: 0.50
      },
      cellular: {
        enabled: false,
        depth_mm: 2.4,
        scale_angular: 8,
        scale_vertical_mm: 22.0,
        ridge_mode: true,
        octaves: 2,
        seed: 42
      }
    },
    print_mode: "shelled_hollow",
    stl_always_open_hollow: true,
    auto_configure_slicer: true,
    spiral_line_width_mm: 0.65,
    spiral_bottom_layers: 5,
    spiral_smooth: true,
    wall_thickness_mm: 2.4,
    bottom_thickness_mm: 3.2,
    auto_clamp_overhang: false,
    max_safe_overhang_deg: 48.0,
    drainage: {
      enabled: false,
      hole_count: 4,
      hole_diameter_mm: 8.0,
      ring_radius_ratio: 0.48
    },
    saucer: {
      clearance_mm: 8.0,
      rim_height_mm: 22.0,
      wall_thickness_mm: 2.4,
      floor_thickness_mm: 2.6,
      inner_ribs_height_mm: 2.0,
      match_vase_texture: true
    }
  };

  function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
  }

  function clampFloat(val, defVal, lo, hi) {
    if (typeof val === "boolean" || val === null || val === undefined || val === "") return defVal;
    const f = Number(val);
    if (!Number.isFinite(f)) return defVal;
    return Math.max(lo, Math.min(hi, f));
  }

  function clampInt(val, defVal, lo, hi) {
    if (typeof val === "boolean" || val === null || val === undefined || val === "") return defVal;
    const f = Number(val);
    if (!Number.isFinite(f)) return defVal;
    return Math.max(lo, Math.min(hi, Math.round(f)));
  }

  function toBool(val, defVal) {
    if (typeof val === "boolean") return val;
    if (typeof val === "number") return Number.isFinite(val) ? Boolean(val) : defVal;
    if (typeof val === "string") {
      const s = val.trim().toLowerCase();
      if (s === "true" || s === "1" || s === "yes" || s === "on") return true;
      if (s === "false" || s === "0" || s === "no" || s === "off" || s === "") return false;
    }
    return defVal;
  }

  function normalizeProfilePoints(rawPts) {
    const fallback = deepClone(JS_DEFAULT_PARAMS.profile_points);
    if (!Array.isArray(rawPts) || rawPts.length < 2) return fallback;
    const parsed = [];
    for (let i = 0; i < rawPts.length; i++) {
      const item = rawPts[i];
      let zRaw = null;
      let rRaw = null;
      if (Array.isArray(item) && item.length >= 2) {
        zRaw = item[0];
        rRaw = item[1];
      } else if (item && typeof item === "object") {
        zRaw = item.z !== undefined ? item.z : item.z_norm;
        rRaw = item.r !== undefined ? item.r : (item.radius_mm !== undefined ? item.radius_mm : item.radius);
      }
      const zf = Number(zRaw);
      const rf = Number(rRaw);
      if (!Number.isFinite(zf) || !Number.isFinite(rf)) continue;
      parsed.push([Math.max(0.0, Math.min(1.0, zf)), Math.max(8.0, Math.min(225.0, rf))]);
    }
    if (parsed.length < 2) return fallback;
    parsed.sort(function (a, b) { return a[0] - b[0]; });
    parsed[0][0] = 0.0;
    parsed[parsed.length - 1][0] = 1.0;

    const cleaned = [[parsed[0][0], parsed[0][1]]];
    for (let i = 1; i < parsed.length; i++) {
      const pt = parsed[i];
      const last = cleaned[cleaned.length - 1];
      if (pt[0] - last[0] < 1e-4) {
        if (pt[0] >= 1.0) {
          cleaned[cleaned.length - 1] = [1.0, pt[1]];
        } else {
          last[1] = 0.5 * (last[1] + pt[1]);
        }
      } else {
        cleaned.push([pt[0], pt[1]]);
      }
    }
    if (cleaned.length < 2) return fallback;
    cleaned[0][0] = 0.0;
    cleaned[cleaned.length - 1][0] = 1.0;
    return cleaned;
  }

  function normalizeParams(raw) {
    const src = (raw && typeof raw === "object") ? raw : {};
    const texSrc = (src.textures && typeof src.textures === "object") ? src.textures : {};
    const ribSrc = (texSrc.ribbed && typeof texSrc.ribbed === "object") ? texSrc.ribbed : {};
    const wavSrc = (texSrc.waves && typeof texSrc.waves === "object") ? texSrc.waves : {};
    const oriSrc = (texSrc.origami && typeof texSrc.origami === "object") ? texSrc.origami : {};
    const celSrc = (texSrc.cellular && typeof texSrc.cellular === "object") ? texSrc.cellular : {};
    const drnSrc = (src.drainage && typeof src.drainage === "object") ? src.drainage : {};
    const sauSrc = (src.saucer && typeof src.saucer === "object") ? src.saucer : {};

    let polySides = clampInt(src.polygon_sides, 0, 0, 24);
    if (polySides > 0 && polySides < 3) polySides = 3;

    const pmRaw = String(src.print_mode !== undefined ? src.print_mode : "shelled_hollow").trim().toLowerCase();
    const printMode = pmRaw === "spiral_vase" ? "spiral_vase" : "shelled_hollow";

    const cleanName = String(src.name !== undefined ? src.name : JS_DEFAULT_PARAMS.name).trim().slice(0, 80) || "Ondas Organicas";

    return {
      name: cleanName,
      height_mm: clampFloat(src.height_mm, 160.0, 30.0, 500.0),
      base_diameter_mm: clampFloat(src.base_diameter_mm, 76.0, 20.0, 450.0),
      belly_diameter_mm: clampFloat(src.belly_diameter_mm, 110.0, 20.0, 450.0),
      belly_height_ratio: clampFloat(src.belly_height_ratio, 0.34, 0.08, 0.85),
      waist_diameter_mm: clampFloat(src.waist_diameter_mm, 68.0, 16.0, 450.0),
      waist_height_ratio: clampFloat(src.waist_height_ratio, 0.68, 0.15, 0.92),
      neck_diameter_mm: clampFloat(src.neck_diameter_mm, 82.0, 16.0, 450.0),
      lip_flare_mm: clampFloat(src.lip_flare_mm, 4.0, -15.0, 25.0),
      lip_bevel_mm: clampFloat(src.lip_bevel_mm, 1.0, 0.0, 4.0),
      polygon_sides: polySides,
      polygon_roundness: clampFloat(src.polygon_roundness, 0.35, 0.0, 1.0),
      use_custom_profile: toBool(src.use_custom_profile, false),
      profile_points: normalizeProfilePoints(src.profile_points),
      resolution_angular: clampInt(src.resolution_angular, 240, 64, 360),
      resolution_vertical: clampInt(src.resolution_vertical, 220, 60, 400),
      bottom_fade_mm: clampFloat(src.bottom_fade_mm, 8.0, 0.0, 60.0),
      top_fade_mm: clampFloat(src.top_fade_mm, 6.0, 0.0, 60.0),
      global_twist_deg: clampFloat(src.global_twist_deg, 0.0, -720.0, 720.0),
      textures: {
        ribbed: {
          enabled: toBool(ribSrc.enabled, false),
          depth_mm: clampFloat(ribSrc.depth_mm, 2.6, -15.0, 15.0),
          count: clampInt(ribSrc.count, 32, 3, 180),
          duty_cycle: clampFloat(ribSrc.duty_cycle, 0.50, 0.10, 0.90),
          sharpness: clampFloat(ribSrc.sharpness, 0.35, 0.0, 1.0),
          twist_deg: clampFloat(ribSrc.twist_deg, 60.0, -720.0, 720.0),
          phase_deg: clampFloat(ribSrc.phase_deg, 0.0, 0.0, 360.0)
        },
        waves: {
          enabled: toBool(wavSrc.enabled, true),
          depth_mm: clampFloat(wavSrc.depth_mm, 3.0, -15.0, 15.0),
          vertical_wavelength_mm: clampFloat(wavSrc.vertical_wavelength_mm, 26.0, 4.0, 120.0),
          angular_lobes: clampInt(wavSrc.angular_lobes, 6, 0, 48),
          interference_mix: clampFloat(wavSrc.interference_mix, 0.45, 0.0, 1.0),
          wave_skew: clampFloat(wavSrc.wave_skew, 0.0, -0.8, 0.8),
          phase_deg: clampFloat(wavSrc.phase_deg, 0.0, 0.0, 360.0)
        },
        origami: {
          enabled: toBool(oriSrc.enabled, false),
          depth_mm: clampFloat(oriSrc.depth_mm, 3.2, -15.0, 15.0),
          cells_around: clampInt(oriSrc.cells_around, 12, 3, 60),
          cells_vertical: clampInt(oriSrc.cells_vertical, 8, 2, 50),
          crease_sharpness: clampFloat(oriSrc.crease_sharpness, 0.75, 0.0, 1.0),
          stagger: clampFloat(oriSrc.stagger, 0.50, 0.0, 1.0)
        },
        cellular: {
          enabled: toBool(celSrc.enabled, false),
          depth_mm: clampFloat(celSrc.depth_mm, 2.4, -12.0, 12.0),
          scale_angular: clampInt(celSrc.scale_angular, 8, 2, 40),
          scale_vertical_mm: clampFloat(celSrc.scale_vertical_mm, 22.0, 5.0, 100.0),
          ridge_mode: toBool(celSrc.ridge_mode, true),
          octaves: clampInt(celSrc.octaves, 2, 1, 4),
          seed: clampInt(celSrc.seed, 42, 1, 99999)
        }
      },
      print_mode: printMode,
      stl_always_open_hollow: toBool(src.stl_always_open_hollow, true),
      auto_configure_slicer: toBool(src.auto_configure_slicer, true),
      spiral_line_width_mm: clampFloat(src.spiral_line_width_mm, 0.65, 0.40, 1.20),
      spiral_bottom_layers: clampInt(src.spiral_bottom_layers, 5, 2, 15),
      spiral_smooth: toBool(src.spiral_smooth, true),
      wall_thickness_mm: clampFloat(src.wall_thickness_mm, 2.4, 0.8, 25.0),
      bottom_thickness_mm: clampFloat(src.bottom_thickness_mm, 3.2, 1.0, 25.0),
      auto_clamp_overhang: toBool(src.auto_clamp_overhang, false),
      max_safe_overhang_deg: clampFloat(src.max_safe_overhang_deg, 48.0, 35.0, 65.0),
      drainage: {
        enabled: toBool(drnSrc.enabled, false),
        hole_count: clampInt(drnSrc.hole_count, 4, 1, 9),
        hole_diameter_mm: clampFloat(drnSrc.hole_diameter_mm, 8.0, 3.0, 20.0),
        ring_radius_ratio: clampFloat(drnSrc.ring_radius_ratio, 0.48, 0.0, 0.68)
      },
      saucer: {
        clearance_mm: clampFloat(sauSrc.clearance_mm, 8.0, 3.0, 25.0),
        rim_height_mm: clampFloat(sauSrc.rim_height_mm, 22.0, 10.0, 60.0),
        wall_thickness_mm: clampFloat(sauSrc.wall_thickness_mm, 2.4, 1.2, 5.0),
        floor_thickness_mm: clampFloat(sauSrc.floor_thickness_mm, 2.6, 1.2, 6.0),
        inner_ribs_height_mm: clampFloat(sauSrc.inner_ribs_height_mm, 2.0, 0.0, 6.0),
        match_vase_texture: toBool(sauSrc.match_vase_texture, true)
      }
    };
  }

  // ==========================================================================
  // 2. Shared Mathematical Surface Engine (Exact Bit-for-Bit Parity with Python)
  // ==========================================================================
  const DEG2RAD = Math.PI / 180.0;
  const TWO_PI = 2.0 * Math.PI;

  function posMod(a, m) {
    return ((a % m) + m) % m;
  }

  function smoothstepScalar(edge0, edge1, x) {
    const span = edge1 - edge0;
    if (span <= 1e-9) return x > edge0 ? 1.0 : 0.0;
    const u = Math.max(0.0, Math.min(1.0, (x - edge0) / span));
    return u * u * (3.0 - 2.0 * u);
  }

  function prepareSilhouetteKnots(p) {
    let raw;
    if (p.use_custom_profile) {
      raw = p.profile_points.map(function (pt) { return [Number(pt[0]), Number(pt[1])]; });
    } else {
      const rBase = 0.5 * Number(p.base_diameter_mm);
      const rBelly = 0.5 * Number(p.belly_diameter_mm);
      const rWaist = 0.5 * Number(p.waist_diameter_mm);
      const rNeck = 0.5 * Number(p.neck_diameter_mm);
      const rLip = Math.max(4.0, rNeck + Number(p.lip_flare_mm));
      raw = [
        [0.0, rBase],
        [Number(p.belly_height_ratio), rBelly],
        [Number(p.waist_height_ratio), rWaist],
        [0.92, rNeck],
        [1.0, rLip]
      ];
    }

    raw.sort(function (a, b) { return a[0] - b[0]; });
    raw[0][0] = 0.0;
    raw[raw.length - 1][0] = 1.0;

    const dedup = [[raw[0][0], raw[0][1]]];
    for (let i = 1; i < raw.length; i++) {
      const zK = raw[i][0];
      const rK = raw[i][1];
      const last = dedup[dedup.length - 1];
      if (zK - last[0] < 1e-4) {
        if (zK >= 1.0) {
          dedup[dedup.length - 1] = [1.0, rK];
        } else {
          last[1] = 0.5 * (last[1] + rK);
        }
      } else {
        dedup.push([zK, rK]);
      }
    }
    if (dedup.length < 2) {
      return { xs: [0.0, 1.0], ys: [raw[0][1], raw[raw.length - 1][1]] };
    }
    return {
      xs: dedup.map(function (k) { return k[0]; }),
      ys: dedup.map(function (k) { return k[1]; })
    };
  }

  function buildPchipSpline(xs, ys) {
    const m = xs.length;
    if (m === 2) {
      return { xs: xs, ys: ys, h: [xs[1] - xs[0]], d: [0, 0], linear: true };
    }
    const h = new Float64Array(m - 1);
    const delta = new Float64Array(m - 1);
    for (let k = 0; k < m - 1; k++) {
      h[k] = xs[k + 1] - xs[k];
      delta[k] = (ys[k + 1] - ys[k]) / h[k];
    }
    const d = new Float64Array(m);
    for (let k = 1; k < m - 1; k++) {
      if (delta[k - 1] * delta[k] > 0.0) {
        const w1 = 2.0 * h[k] + h[k - 1];
        const w2 = h[k] + 2.0 * h[k - 1];
        d[k] = (w1 + w2) / (w1 / delta[k - 1] + w2 / delta[k]);
      } else {
        d[k] = 0.0;
      }
    }

    let d0 = ((2.0 * h[0] + h[1]) * delta[0] - h[0] * delta[1]) / (h[0] + h[1]);
    if (d0 * delta[0] <= 0.0) {
      d0 = 0.0;
    } else if (delta[0] * delta[1] <= 0.0 && Math.abs(d0) > Math.abs(3.0 * delta[0])) {
      d0 = 3.0 * delta[0];
    }
    d[0] = d0;

    const n1 = m - 1;
    let dn = ((2.0 * h[n1 - 1] + h[n1 - 2]) * delta[n1 - 1] - h[n1 - 1] * delta[n1 - 2]) / (h[n1 - 1] + h[n1 - 2]);
    if (dn * delta[n1 - 1] <= 0.0) {
      dn = 0.0;
    } else if (delta[n1 - 1] * delta[n1 - 2] <= 0.0 && Math.abs(dn) > Math.abs(3.0 * delta[n1 - 1])) {
      dn = 3.0 * delta[n1 - 1];
    }
    d[n1] = dn;

    return { xs: xs, ys: ys, h: h, d: d, linear: false };
  }

  function evalPchipScalar(spline, xVal) {
    const xs = spline.xs;
    const ys = spline.ys;
    const m = xs.length;
    if (spline.linear || m === 2) {
      const tLin = Math.max(0.0, Math.min(1.0, (xVal - xs[0]) / Math.max(xs[1] - xs[0], 1e-9)));
      return ys[0] + tLin * (ys[1] - ys[0]);
    }
    const xClamped = Math.max(xs[0], Math.min(xs[m - 1], xVal));
    let idx = m - 2;
    for (let k = 0; k < m - 1; k++) {
      if (xClamped < xs[k + 1]) {
        idx = k;
        break;
      }
    }
    const hk = spline.h[idx];
    const t = (xClamped - xs[idx]) / hk;
    const t2 = t * t;
    const t3 = t2 * t;
    const h00 = 2.0 * t3 - 3.0 * t2 + 1.0;
    const h10 = t3 - 2.0 * t2 + t;
    const h01 = -2.0 * t3 + 3.0 * t2;
    const h11 = t3 - t2;
    return h00 * ys[idx] + h10 * hk * spline.d[idx] + h01 * ys[idx + 1] + h11 * hk * spline.d[idx + 1];
  }

  function hash3U32(ix, iy, iz, seed) {
    let h = (
      Math.imul(ix | 0, 374761393) +
      Math.imul(iy | 0, 668265263) +
      Math.imul(iz | 0, 1274126177) +
      Math.imul(seed | 0, 1597334677)
    ) >>> 0;
    h = (h ^ (h >>> 13)) >>> 0;
    h = Math.imul(h, 1274126177) >>> 0;
    h = (h ^ (h >>> 16)) >>> 0;
    return h / 4294967295.0;
  }

  function valueNoise3DScalar(cx, cy, cz, octaves, seed) {
    let total = 0.0;
    let ampSum = 0.0;
    let freq = 1.0;
    let amp = 1.0;
    const nOct = Math.max(1, octaves | 0);
    const baseSeed = seed | 0;

    for (let octIdx = 0; octIdx < nOct; octIdx++) {
      const x = cx * freq;
      const y = cy * freq;
      const z = cz * freq;

      const ix0 = Math.floor(x);
      const iy0 = Math.floor(y);
      const iz0 = Math.floor(z);

      const fx = x - ix0;
      const fy = y - iy0;
      const fz = z - iz0;

      const ux = fx * fx * (3.0 - 2.0 * fx);
      const uy = fy * fy * (3.0 - 2.0 * fy);
      const uz = fz * fz * (3.0 - 2.0 * fz);

      const sOct = baseSeed;
      const c000 = hash3U32(ix0, iy0, iz0, sOct);
      const c100 = hash3U32(ix0 + 1, iy0, iz0, sOct);
      const c010 = hash3U32(ix0, iy0 + 1, iz0, sOct);
      const c110 = hash3U32(ix0 + 1, iy0 + 1, iz0, sOct);
      const c001 = hash3U32(ix0, iy0, iz0 + 1, sOct);
      const c101 = hash3U32(ix0 + 1, iy0, iz0 + 1, sOct);
      const c011 = hash3U32(ix0, iy0 + 1, iz0 + 1, sOct);
      const c111 = hash3U32(ix0 + 1, iy0 + 1, iz0 + 1, sOct);

      const nx00 = c000 + ux * (c100 - c000);
      const nx10 = c010 + ux * (c110 - c010);
      const nx01 = c001 + ux * (c101 - c001);
      const nx11 = c011 + ux * (c111 - c011);

      const nxy0 = nx00 + uy * (nx10 - nx00);
      const nxy1 = nx01 + uy * (nx11 - nx01);

      const nVal = nxy0 + uz * (nxy1 - nxy0);
      total += amp * nVal;
      ampSum += amp;
      freq *= 2.0;
      amp *= 0.5;
    }

    return total / Math.max(ampSum, 1e-9);
  }

  function computeTextureDisplacementScalar(z, zNorm, theta, thetaG, textures, globalTwistRad) {
    let dr = 0.0;

    const rib = textures.ribbed;
    if (rib.enabled && Math.abs(rib.depth_mm) > 1e-9) {
      const count = Number(rib.count);
      const duty = Math.max(Number(rib.duty_cycle), 1e-6);
      const sharp = Number(rib.sharpness);
      const twistRad = Number(rib.twist_deg) * DEG2RAD;
      const phaseRad = Number(rib.phase_deg) * DEG2RAD;

      const phi = posMod((theta + twistRad * zNorm + phaseRad) * count / TWO_PI, 1.0);
      const u = Math.abs(phi - 0.5) * 2.0;
      const t = Math.max(0.0, Math.min(1.0, u / duty));
      const wSmooth = 0.5 * (1.0 + Math.cos(Math.PI * t));
      const wSharp = 1.0 - t;
      const shape = (1.0 - sharp) * wSmooth + sharp * wSharp;
      dr += Number(rib.depth_mm) * shape;
    }

    const wav = textures.waves;
    if (wav.enabled && Math.abs(wav.depth_mm) > 1e-9) {
      const wl = Math.max(Number(wav.vertical_wavelength_mm), 1.0);
      const lobes = Number(wav.angular_lobes);
      const mix = Number(wav.interference_mix);
      const skew = Number(wav.wave_skew);
      const phaseRad = Number(wav.phase_deg) * DEG2RAD;

      const kz = (TWO_PI * z / wl) + phaseRad;
      const ka = lobes * theta + globalTwistRad * zNorm;
      const w1 = Math.sin(kz + ka + skew * Math.sin(kz));
      const w2 = Math.sin(kz - ka);
      dr += Number(wav.depth_mm) * ((1.0 - 0.5 * mix) * w1 + 0.5 * mix * w2);
    }

    const ori = textures.origami;
    if (ori.enabled && Math.abs(ori.depth_mm) > 1e-9) {
      const cAround = Number(ori.cells_around);
      const cVert = Number(ori.cells_vertical);
      const crease = Number(ori.crease_sharpness);
      const stagger = Number(ori.stagger);

      const v = zNorm * cVert;
      const tier = Math.floor(v);
      const fv = v - tier;
      const u = (theta / TWO_PI) * cAround + tier * stagger;
      const fu = u - Math.floor(u);

      const diamond = 1.0 - (Math.abs(2.0 * fu - 1.0) + Math.abs(2.0 * fv - 1.0));
      const soft = Math.sin(Math.PI * (fu - 0.5)) * Math.sin(Math.PI * (fv - 0.5));
      const val = crease * diamond + (1.0 - crease) * soft;
      dr += Number(ori.depth_mm) * val;
    }

    const cel = textures.cellular;
    if (cel.enabled && Math.abs(cel.depth_mm) > 1e-9) {
      const sAng = Number(cel.scale_angular);
      const sVert = Math.max(Number(cel.scale_vertical_mm), 1.0);
      const octaves = cel.octaves | 0;
      const seed = cel.seed | 0;
      const ridge = Boolean(cel.ridge_mode);

      const cylScale = sAng / TWO_PI * 4.0;
      const cx = Math.cos(thetaG) * cylScale;
      const cy = Math.sin(thetaG) * cylScale;
      const cz = z / sVert;

      const n = valueNoise3DScalar(cx, cy, cz, octaves, seed);
      const val = ridge ? (1.0 - 2.0 * Math.abs(n - 0.5)) : (2.0 * (n - 0.5));
      dr += Number(cel.depth_mm) * val;
    }

    return dr;
  }

  function evaluateRadiusGrid(rawParams, nZ, nTheta) {
    const p = normalizeParams(rawParams);
    const nz = (nZ !== undefined && nZ !== null) ? Math.max(2, nZ | 0) : (p.resolution_vertical | 0);
    const nt = (nTheta !== undefined && nTheta !== null) ? Math.max(3, nTheta | 0) : (p.resolution_angular | 0);

    const heightMm = Number(p.height_mm);
    const zVals = new Array(nz);
    const zNorms = new Array(nz);
    const zStep = nz > 1 ? (heightMm / (nz - 1)) : 0.0;
    for (let i = 0; i < nz; i++) {
      const zv = (nz > 1 && i === nz - 1) ? heightMm : (i * zStep);
      zVals[i] = zv;
      zNorms[i] = heightMm > 1e-9 ? (zv / heightMm) : 0.0;
    }

    const thetaVals = new Array(nt);
    const thStep = TWO_PI / nt;
    for (let j = 0; j < nt; j++) {
      thetaVals[j] = j * thStep;
    }

    const knots = prepareSilhouetteKnots(p);
    const spline = buildPchipSpline(knots.xs, knots.ys);
    const rBase1D = new Float64Array(nz);
    for (let i = 0; i < nz; i++) {
      rBase1D[i] = evalPchipScalar(spline, zNorms[i]);
    }

    const globalTwistRad = Number(p.global_twist_deg) * DEG2RAD;
    const nSides = p.polygon_sides | 0;
    const hasPoly = nSides >= 3;
    const alpha = hasPoly ? (Math.PI / nSides) : 0.0;
    const twoAlpha = 2.0 * alpha;
    const roundness = Number(p.polygon_roundness);

    const bfade = Number(p.bottom_fade_mm);
    const tfade = Number(p.top_fade_mm);

    const radii = new Array(nz);
    for (let i = 0; i < nz; i++) {
      const z = zVals[i];
      const zn = zNorms[i];

      let eBot;
      if (bfade <= 0.01) {
        eBot = z > 1e-9 ? 1.0 : 0.0;
      } else {
        eBot = i === 0 ? 0.0 : smoothstepScalar(0.0, bfade, z);
      }
      const eTop = tfade <= 0.01 ? 1.0 : smoothstepScalar(0.0, tfade, heightMm - z);
      const env = eBot * eTop;

      const row = new Array(nt);
      const rBase = rBase1D[i];

      for (let j = 0; j < nt; j++) {
        const theta = thetaVals[j];
        const thetaG = theta + globalTwistRad * zn;

        let rProf = rBase;
        if (hasPoly) {
          const sector = posMod(thetaG, twoAlpha) - alpha;
          const polyScale = Math.cos(alpha) / Math.cos(sector);
          rProf = rBase * ((1.0 - roundness) * polyScale + roundness);
        }

        let dr = 0.0;
        if (env > 1e-9) {
          dr = computeTextureDisplacementScalar(z, zn, theta, thetaG, p.textures, globalTwistRad);
        }
        row[j] = Math.max(6.0, rProf + env * dr);
      }
      radii[i] = row;
    }

    if (p.auto_clamp_overhang && nz >= 2) {
      const dz = heightMm / (nz - 1);
      const maxDr = dz * Math.tan(Number(p.max_safe_overhang_deg) * DEG2RAD);
      for (let i = 0; i < nz - 1; i++) {
        const cur = radii[i];
        const nxt = radii[i + 1];
        for (let j = 0; j < nt; j++) {
          const lo = cur[j] - maxDr;
          const hi = cur[j] + maxDr;
          if (nxt[j] < lo) nxt[j] = lo;
          else if (nxt[j] > hi) nxt[j] = hi;
        }
      }
      for (let i = nz - 2; i >= 0; i--) {
        const cur = radii[i];
        const nxt = radii[i + 1];
        for (let j = 0; j < nt; j++) {
          const lo = nxt[j] - maxDr;
          const hi = nxt[j] + maxDr;
          if (cur[j] < lo) cur[j] = lo;
          else if (cur[j] > hi) cur[j] = hi;
          if (cur[j] < 6.0) cur[j] = 6.0;
        }
      }
      for (let j = 0; j < nt; j++) {
        if (radii[nz - 1][j] < 6.0) radii[nz - 1][j] = 6.0;
      }
    }

    return {
      z_vals: zVals,
      theta_vals: thetaVals,
      radii: radii,
      r_base: rBase1D
    };
  }

  function evaluateSurfaceRadius(rawParams, z, theta) {
    const p = normalizeParams(rawParams);
    const heightMm = Number(p.height_mm);
    const zClamped = Math.max(0.0, Math.min(heightMm, Number(z)));
    const zn = heightMm > 1e-9 ? zClamped / heightMm : 0.0;

    const knots = prepareSilhouetteKnots(p);
    const spline = buildPchipSpline(knots.xs, knots.ys);
    const rBase = evalPchipScalar(spline, zn);

    const globalTwistRad = Number(p.global_twist_deg) * DEG2RAD;
    const thetaG = theta + globalTwistRad * zn;

    let rProf = rBase;
    const nSides = p.polygon_sides | 0;
    if (nSides >= 3) {
      const alpha = Math.PI / nSides;
      const sector = posMod(thetaG, 2.0 * alpha) - alpha;
      const polyScale = Math.cos(alpha) / Math.cos(sector);
      rProf = rBase * ((1.0 - p.polygon_roundness) * polyScale + p.polygon_roundness);
    }

    const bfade = Number(p.bottom_fade_mm);
    const tfade = Number(p.top_fade_mm);
    const eBot = zClamped <= 1e-9 ? 0.0 : (bfade <= 0.01 ? 1.0 : smoothstepScalar(0.0, bfade, zClamped));
    const eTop = tfade <= 0.01 ? 1.0 : smoothstepScalar(0.0, tfade, heightMm - zClamped);
    const env = eBot * eTop;

    const dr = env > 1e-9 ? computeTextureDisplacementScalar(zClamped, zn, theta, thetaG, p.textures, globalTwistRad) : 0.0;
    return Math.max(6.0, rProf + env * dr);
  }

  globalThis.evaluateRadiusGrid = evaluateRadiusGrid;
  globalThis.evaluateSurfaceRadius = evaluateSurfaceRadius;
  globalThis.normalizeParams = normalizeParams;
  globalThis.VaseStudioMath = {
    normalizeParams: normalizeParams,
    evaluateRadiusGrid: evaluateRadiusGrid,
    evaluateSurfaceRadius: evaluateSurfaceRadius,
    hash3U32: hash3U32,
    valueNoise3DScalar: valueNoise3DScalar
  };

  // ==========================================================================
  // 3. Translations (PT-BR & EN) & Slider Metadata
  // ==========================================================================
  const I18N = {
    pt: {
      btn_surprise: "Surpreenda-me",
      tab_shape: "Forma",
      tab_textures: "Texturas",
      tab_print: "Impressão",
      tab_presets: "Presets",
      sec_presets: "Galeria de Modelos",
      btn_save_preset: "+ Salvar",
      btn_ok: "Salvar",
      cat_all: "Todos",
      cat_organic: "Orgânicos",
      cat_geometric: "Geométricos",
      cat_planter: "Cachepôs",
      cat_user: "Meus",
      sec_silhouette: "Silhueta & Curva 2D",
      mode_sliders: "Sliders",
      mode_curve: "Curva Livre 2D",
      btn_to_curve: "Sliders → Curva",
      hint_curve_sliders: "Arraste as alças na silhueta 2D ou ajuste os controles abaixo.",
      hint_curve_free: "Arraste pontos · Clique na curva p/ adicionar · Duplo-clique/botão direito p/ remover.",
      sec_resolution: "Resolução da Malha",
      mat_emerald: "Seda Esmeralda Orca",
      mat_terracotta: "Cerâmica Terracota",
      mat_white: "Porcelana Branca Mate",
      mat_copper: "Bronze Cobre Escovado",
      mat_xray: "🔬 Raio-X / Parede (Translúcido)",
      mat_heatmap: "Mapa de Overhang (°)",
      vp_xray: "🔬 Raio-X / Parede",
      vp_calipers: "📏 Cotas mm",
      vp_heatmap: "🔥 Overhang",
      vp_wire: "⌗ Malha",
      vp_saucer: "🍽 Pratinho",
      vp_layout_nested: "Encaixado",
      vp_layout_side: "Lado a Lado",
      hud_title: "Printabilidade",
      hud_wall_floor: "Parede / Fundo",
      hud_mouth_hole: "Ø Furo Boca",
      hud_dims: "Dimensões (mm)",
      hud_overhang: "Overhang Máx",
      hud_weight: "Filamento Est.",
      hud_Tris: "Triângulos",
      leg_outer: "Externa",
      leg_inner: "Cavidade & Fundo",
      cam_front: "Frente",
      cam_top: "Topo",
      cam_bottom: "Base",
      cam_fit: "Enquadrar",
      vp_cut: "✂ Corte Transversal",
      vp_cut_y: "✂ Corte Vertical (Perfil Y)",
      vp_cut_z: "💿 Fatia Horizontal Z (Planta 5%–100%)",
      sec_envelope: "Envelope & Torção Global",
      sec_textures: "Texturas Combináveis",
      tex_ribbed: "Canelado / Frisos",
      tex_waves: "Ondas Orgânicas",
      tex_origami: "Origami Diamante",
      tex_cellular: "Celular / Coral 3D",
      lbl_ridge_mode: "Veios em Crista (Coral)",
      sec_print_mode: "Parede & Abertura (mm)",
      mode_hollow: "Vaso Oco Real (Parede em mm)",
      mode_spiral: "Modo Espiral (1 Linha)",
      lbl_stl_open_hollow: "Manter boca aberta ao exportar .STL",
      note_spiral_honest: "O Modo Espiral gera um bloco base cujo topo é removido pelo fatiador (.3MF). Para exportar .STL sempre aberto, mantenha a proteção abaixo ativa!",
      banner_spiral_safe: "Modo Espiral: malha base p/ .3MF (fatiador remove o topo) · .STL protegido c/ Boca Aberta",
      banner_spiral_closed: "Atenção: Bloco Espiral maciço — o .STL sairá com o topo FECHADO para fatiamento Espiral!",
      perim_hint_fmt: "≈ {n} voltas de {lw} mm · Furo Ø {id} mm",
      spiral_floor_fmt: "≈ {mm} mm de fundo ({n} cam.) · Bico {noz}mm (ideal {wmin}–{wmax} mm)",
      wall_badge_hollow: "Oco · {w} mm",
      wall_badge_spiral: "Espiral · {w} mm",
      cal_ext: "Ø Externo: {v} mm",
      cal_hole: "Ø Furo: {v} mm",
      cal_wall: "Parede: {v} mm",
      cal_wall_range: "Parede: {v} mm ({min}–{max} mm)",
      cal_floor: "Fundo: {v} mm",
      cal_z_slice: "💿 Fatia Z = {z} mm ({pct}%)",
      lbl_2d_wall: "Parede {v} mm",
      lbl_2d_floor: "Fundo {v} mm",
      lbl_2d_hole: "Ø Furo {v} mm",
      lbl_2d_spiral_cap: "Tampa Espiral (.3MF)",
      lbl_auto_slicer: "Auto-ajustar OrcaSlicer ao enviar",
      lbl_spiral_smooth: "Suavizar Costura Espiral XY",
      lbl_clamp_overhang: "Limitar Overhang Automaticamente",
      sec_gardening: "Jardinagem: Drenagem & Prato",
      lbl_drainage: "Furos de Drenagem na Base",
      note_drainage_spiral: "Cavidades cegas nas camadas sólidas da base: furos reais sem quebrar o contorno único do Modo Espiral!",
      note_drainage_hollow: "Túneis cilíndricos atravessando o fundo oco da peça com malha 2-manifold estanque.",
      lbl_include_saucer: "Incluir Pratinho Coordenado",
      warn_saucer_spiral: "Vaso + Prato juntos convertem automaticamente para Vaso Oco Aberto na mesa/exportação.",
      lbl_saucer_tex: "Repetir Textura do Vaso no Prato",
      btn_send_plater: "Enviar para a Mesa do OrcaSlicer",
      btn_exp_3mf: "Exportar .3MF",
      btn_exp_stl: "Exportar .STL",
      poly_circle: "Circular",
      poly_sides_fmt: "{n} Lados",
      active_tex_fmt: "{n} ativa(s)",
      bed_exceeded: "Excede o volume da impressora ({bx}×{by}×{bz} mm)!",
      btn_fit_printer: "Ajustar à Mesa",
      printer_sync_tip: "Clique para sincronizar impressora ativa do OrcaSlicer",
      toast_printer_synced: "Impressora ativa sincronizada: {name} ({dims})",
      toast_fitted_printer: "Dimensões ajustadas ao volume de {name}!",
      status_ok: "ÓTIMO",
      status_warn: "ATENÇÃO",
      status_crit: "CRÍTICO",
      toast_randomized: "Novo vaso imprimível gerado!",
      toast_preset_saved: "Preset salvo com sucesso!",
      toast_converted_curve: "Convertido para Curva Livre PCHIP!"
    },
    en: {
      btn_surprise: "Surprise Me",
      tab_shape: "Shape",
      tab_textures: "Textures",
      tab_print: "Wall & Print",
      tab_presets: "Presets",
      sec_presets: "Preset Gallery",
      btn_save_preset: "+ Save",
      btn_ok: "Save",
      cat_all: "All",
      cat_organic: "Organic",
      cat_geometric: "Geometric",
      cat_planter: "Planters",
      cat_user: "Saved",
      sec_silhouette: "Silhouette & 2D Curve",
      mode_sliders: "Sliders",
      mode_curve: "Freeform 2D Curve",
      btn_to_curve: "Sliders → Curve",
      hint_curve_sliders: "Drag handles directly on the 2D silhouette or fine-tune sliders below.",
      hint_curve_free: "Drag knots · Click curve to add knot · Double-click/right-click interior knot to remove.",
      sec_resolution: "Mesh Resolution",
      mat_emerald: "Orca Emerald Silk",
      mat_terracotta: "Terracotta Clay",
      mat_white: "Matte White Ceramic",
      mat_copper: "Copper Bronze",
      mat_xray: "🔬 X-Ray / Wall (Translucent)",
      mat_heatmap: "Overhang Heatmap (°)",
      vp_xray: "🔬 X-Ray / Wall",
      vp_calipers: "📏 mm Calipers",
      vp_heatmap: "🔥 Overhang",
      vp_wire: "⌗ Wireframe",
      vp_saucer: "🍽 Saucer",
      vp_layout_nested: "Nested",
      vp_layout_side: "Side-by-Side",
      hud_title: "Printability",
      hud_wall_floor: "Wall / Floor",
      hud_mouth_hole: "Ø Mouth Bore",
      hud_dims: "Dimensions (mm)",
      hud_overhang: "Max Overhang",
      hud_weight: "Est. Filament",
      hud_Tris: "Triangles",
      leg_outer: "Outer Wall",
      leg_inner: "Cavity & Floor",
      cam_front: "Front",
      cam_top: "Top",
      cam_bottom: "Bottom",
      cam_fit: "Fit View",
      vp_cut: "✂ Cross-Section Cut",
      vp_cut_y: "✂ Vertical Cut (Profile Y)",
      vp_cut_z: "💿 Horizontal Z Slice (Plan 5%–100%)",
      sec_envelope: "Envelope & Global Twist",
      sec_textures: "Combinable Textures",
      tex_ribbed: "Ribbed / Fluted",
      tex_waves: "Organic Waves",
      tex_origami: "Origami Diamond",
      tex_cellular: "Cellular / Coral 3D",
      lbl_ridge_mode: "Ridged Coral Veins",
      sec_print_mode: "Wall & Opening (mm)",
      mode_hollow: "True Hollow Vase (mm Wall)",
      mode_spiral: "Spiral Mode (1 Line)",
      lbl_stl_open_hollow: "Always keep open mouth on .STL export",
      note_spiral_honest: "Spiral Mode builds a solid base block whose top is removed by the slicer (.3MF). Keep the toggle below checked so .STL exports stay open!",
      banner_spiral_safe: "Spiral Mode: solid base block for .3MF (slicer removes top) · .STL protected w/ Open Mouth",
      banner_spiral_closed: "Warning: Solid Spiral Block — .STL will export CLOSED at top for Spiral Slicing!",
      perim_hint_fmt: "≈ {n} loops of {lw} mm · Bore Ø {id} mm",
      spiral_floor_fmt: "≈ {mm} mm floor ({n} lay.) · Nozzle {noz}mm (ideal {wmin}–{wmax} mm)",
      wall_badge_hollow: "Hollow · {w} mm",
      wall_badge_spiral: "Spiral · {w} mm",
      cal_ext: "Ø Outer: {v} mm",
      cal_hole: "Ø Bore: {v} mm",
      cal_wall: "Wall: {v} mm",
      cal_wall_range: "Wall: {v} mm ({min}–{max} mm)",
      cal_floor: "Bottom: {v} mm",
      cal_z_slice: "💿 Z Slice = {z} mm ({pct}%)",
      lbl_2d_wall: "Wall {v} mm",
      lbl_2d_floor: "Bottom {v} mm",
      lbl_2d_hole: "Ø Bore {v} mm",
      lbl_2d_spiral_cap: "Spiral Cap (.3MF)",
      lbl_auto_slicer: "Auto-configure OrcaSlicer on send",
      lbl_spiral_smooth: "Smooth Spiral XY Seam",
      lbl_clamp_overhang: "Auto-Clamp Overhang Slope",
      sec_gardening: "Gardening: Drainage & Saucer",
      lbl_drainage: "Bottom Drainage Holes",
      note_drainage_spiral: "Smart blind cavities through solid bottom layers: real drainage holes without breaking single-contour Spiral Vase!",
      note_drainage_hollow: "Watertight cylindrical drainage tunnels straight through the hollow pot floor.",
      lbl_include_saucer: "Include Matching Saucer",
      warn_saucer_spiral: "Vase + Saucer together automatically switch to Open Hollow Mesh on send/export.",
      lbl_saucer_tex: "Match Vase Texture on Saucer",
      btn_send_plater: "Send to OrcaSlicer Plater",
      btn_exp_3mf: "Export .3MF",
      btn_exp_stl: "Export .STL",
      poly_circle: "Smooth Circle",
      poly_sides_fmt: "{n}-Gon",
      active_tex_fmt: "{n} active",
      bed_exceeded: "Exceeds printer build volume ({bx}×{by}×{bz} mm)!",
      btn_fit_printer: "Fit to Printer",
      printer_sync_tip: "Click to sync active OrcaSlicer printer",
      toast_printer_synced: "Synced active printer: {name} ({dims})",
      toast_fitted_printer: "Dimensions fitted to {name} build volume!",
      status_ok: "PRINTABLE",
      status_warn: "WARNING",
      status_crit: "CRITICAL",
      toast_randomized: "Generated printable vase design!",
      toast_preset_saved: "Preset saved!",
      toast_converted_curve: "Converted sliders to PCHIP Freeform Curve!"
    }
  };

  const SLIDER_SPECS = [
    { path: "height_mm", min: 30, max: 500, step: 1, unit: "mm", pt: "Altura Total", en: "Total Height" },
    { path: "base_diameter_mm", min: 20, max: 450, step: 1, unit: "mm", pt: "Diâmetro da Base", en: "Base Diameter" },
    { path: "belly_diameter_mm", min: 20, max: 450, step: 1, unit: "mm", pt: "Diâmetro do Bojo", en: "Belly Diameter" },
    { path: "belly_height_ratio", min: 0.08, max: 0.85, step: 0.01, unit: "h", pt: "Altura do Bojo", en: "Belly Height Ratio" },
    { path: "waist_diameter_mm", min: 16, max: 450, step: 1, unit: "mm", pt: "Diâmetro da Cintura", en: "Waist Diameter" },
    { path: "waist_height_ratio", min: 0.15, max: 0.92, step: 0.01, unit: "h", pt: "Altura da Cintura", en: "Waist Height Ratio" },
    { path: "neck_diameter_mm", min: 16, max: 450, step: 1, unit: "mm", pt: "Diâmetro do Pescoço", en: "Neck Diameter" },
    { path: "lip_flare_mm", min: -15, max: 25, step: 0.5, unit: "mm", pt: "Abertura da Borda", en: "Top Lip Flare" },
    { path: "lip_bevel_mm", min: 0, max: 4, step: 0.2, unit: "mm", pt: "Chanfro/Borda", en: "Top Rim Bevel" },
    { path: "polygon_sides", min: 0, max: 24, step: 1, unit: "n", pt: "Lados do Polígono (0=Circ)", en: "Polygon Sides (0=Circle)" },
    { path: "polygon_roundness", min: 0, max: 1, step: 0.02, unit: "", pt: "Suavidade dos Cantos", en: "Polygon Roundness" },
    { path: "resolution_angular", min: 64, max: 360, step: 8, unit: "seg", pt: "Resolução Angular", en: "Angular Resolution" },
    { path: "resolution_vertical", min: 60, max: 400, step: 10, unit: "cam", pt: "Resolução Vertical", en: "Vertical Resolution" },

    { path: "bottom_fade_mm", min: 0, max: 60, step: 1, unit: "mm", pt: "Suavização na Base", en: "Bottom Texture Fade" },
    { path: "top_fade_mm", min: 0, max: 60, step: 1, unit: "mm", pt: "Suavização no Topo", en: "Top Texture Fade" },
    { path: "global_twist_deg", min: -720, max: 720, step: 5, unit: "°", pt: "Torção Helicoidal", en: "Global Helical Twist" },

    { path: "textures.ribbed.depth_mm", min: -15, max: 15, step: 0.2, unit: "mm", pt: "Profundidade do Friso", en: "Rib Depth" },
    { path: "textures.ribbed.count", min: 3, max: 180, step: 1, unit: "un", pt: "Quantidade (Densidade)", en: "Rib Count (Density)" },
    { path: "textures.ribbed.duty_cycle", min: 0.10, max: 0.90, step: 0.02, unit: "", pt: "Largura vs Espaçamento", en: "Rib Width / Duty Cycle" },
    { path: "textures.ribbed.sharpness", min: 0, max: 1, step: 0.02, unit: "", pt: "Nitidez da Crista", en: "Crest Sharpness" },
    { path: "textures.ribbed.twist_deg", min: -720, max: 720, step: 5, unit: "°", pt: "Torção dos Frisos", en: "Rib Helical Twist" },
    { path: "textures.ribbed.phase_deg", min: 0, max: 360, step: 5, unit: "°", pt: "Fase Angular", en: "Angular Phase" },

    { path: "textures.waves.depth_mm", min: -15, max: 15, step: 0.2, unit: "mm", pt: "Amplitude da Onda", en: "Wave Depth" },
    { path: "textures.waves.vertical_wavelength_mm", min: 4, max: 120, step: 1, unit: "mm", pt: "Comprimento Vertical", en: "Vertical Wavelength" },
    { path: "textures.waves.angular_lobes", min: 0, max: 48, step: 1, unit: "un", pt: "Lóbulos na Volta", en: "Angular Lobes" },
    { path: "textures.waves.interference_mix", min: 0, max: 1, step: 0.02, unit: "", pt: "Interferência Cruzada", en: "Counter-Wave Mix" },
    { path: "textures.waves.wave_skew", min: -0.8, max: 0.8, step: 0.05, unit: "", pt: "Assimetria da Onda", en: "Wave Skew" },
    { path: "textures.waves.phase_deg", min: 0, max: 360, step: 5, unit: "°", pt: "Fase da Onda", en: "Wave Phase" },

    { path: "textures.origami.depth_mm", min: -15, max: 15, step: 0.2, unit: "mm", pt: "Relevo dos Diamantes", en: "Facet Depth" },
    { path: "textures.origami.cells_around", min: 3, max: 60, step: 1, unit: "un", pt: "Células Horizontais", en: "Cells Around" },
    { path: "textures.origami.cells_vertical", min: 2, max: 50, step: 1, unit: "un", pt: "Andares Verticais", en: "Vertical Tiers" },
    { path: "textures.origami.crease_sharpness", min: 0, max: 1, step: 0.02, unit: "", pt: "Vincos Dobrados", en: "Crease Sharpness" },
    { path: "textures.origami.stagger", min: 0, max: 1, step: 0.05, unit: "", pt: "Deslocamento (Stagger)", en: "Row Stagger" },

    { path: "textures.cellular.depth_mm", min: -12, max: 12, step: 0.2, unit: "mm", pt: "Relevo Celular", en: "Cellular Depth" },
    { path: "textures.cellular.scale_angular", min: 2, max: 40, step: 1, unit: "un", pt: "Células na Volta", en: "Angular Cell Scale" },
    { path: "textures.cellular.scale_vertical_mm", min: 5, max: 100, step: 1, unit: "mm", pt: "Escala Vertical", en: "Vertical Cell Size" },
    { path: "textures.cellular.octaves", min: 1, max: 4, step: 1, unit: "oct", pt: "Detalhe (Oitavas)", en: "Detail Octaves" },
    { path: "textures.cellular.seed", min: 1, max: 99999, step: 1, unit: "#", pt: "Semente (Seed)", en: "Pattern Seed" },

    { path: "spiral_line_width_mm", min: 0.40, max: 1.20, step: 0.02, unit: "mm", pt: "Largura de Linha Espiral", en: "Spiral Line Width" },
    { path: "spiral_bottom_layers", min: 2, max: 15, step: 1, unit: "cam", pt: "Camadas Sólidas de Base", en: "Bottom Solid Layers" },
    { path: "wall_thickness_mm", min: 0.8, max: 25, step: 0.1, unit: "mm", pt: "Espessura da Parede", en: "Wall Thickness" },
    { path: "bottom_thickness_mm", min: 1.0, max: 25, step: 0.2, unit: "mm", pt: "Espessura do Fundo", en: "Bottom Floor Thickness" },
    { path: "max_safe_overhang_deg", min: 35, max: 65, step: 1, unit: "°", pt: "Limite de Overhang", en: "Max Safe Overhang" },

    { path: "drainage.hole_count", min: 1, max: 9, step: 1, unit: "un", pt: "Número de Furos", en: "Drainage Hole Count" },
    { path: "drainage.hole_diameter_mm", min: 3, max: 20, step: 0.5, unit: "mm", pt: "Diâmetro do Furo", en: "Hole Diameter" },
    { path: "drainage.ring_radius_ratio", min: 0, max: 0.68, step: 0.02, unit: "r", pt: "Raio do Anel (0=Centro)", en: "Ring Radius Ratio" },

    { path: "saucer.clearance_mm", min: 3, max: 25, step: 0.5, unit: "mm", pt: "Folga Interna do Prato", en: "Saucer Inner Clearance" },
    { path: "saucer.rim_height_mm", min: 10, max: 60, step: 1, unit: "mm", pt: "Altura da Borda", en: "Saucer Rim Height" },
    { path: "saucer.wall_thickness_mm", min: 1.2, max: 5.0, step: 0.2, unit: "mm", pt: "Parede do Prato", en: "Saucer Wall Thickness" },
    { path: "saucer.floor_thickness_mm", min: 1.2, max: 6.0, step: 0.2, unit: "mm", pt: "Fundo do Prato", en: "Saucer Floor Thickness" },
    { path: "saucer.inner_ribs_height_mm", min: 0, max: 6.0, step: 0.2, unit: "mm", pt: "Frisos Internos de Escoamento", en: "Inner Drainage Ribs" }
  ];

  // ==========================================================================
  // 4. Studio Application State & Undo/Redo Stack
  // ==========================================================================
  const initCtx = (BOOT_PAYLOAD && BOOT_PAYLOAD.initial_context) ? BOOT_PAYLOAD.initial_context : {};
  const state = {
    mode: BOOT_PAYLOAD.mode === "dock" ? "dock" : "page",
    lang: initCtx.lang === "en" ? "en" : "pt",
    theme: initCtx.theme === "light" ? "light" : "dark",
    printer: Object.assign(
      {
        name: "Generic 3D Printer",
        bed_x: 220.0,
        bed_y: 220.0,
        bed_shape: "rectangular",
        max_z: 250.0,
        nozzle_mm: 0.4,
        layer_height_mm: 0.2,
        line_width_mm: 0.42
      },
      initCtx.printer || {}
    ),
    builtinPresets: Array.isArray(initCtx.builtin_presets) && initCtx.builtin_presets.length
      ? initCtx.builtin_presets
      : (Array.isArray(BOOT_PAYLOAD.fallback_presets) ? BOOT_PAYLOAD.fallback_presets : []),
    userPresets: Array.isArray(initCtx.user_presets) ? initCtx.user_presets : [],
    presetFilter: "all",
    activePresetId: "ondas_organicas",
    params: normalizeParams(initCtx.params || BOOT_PAYLOAD.fallback_params || JS_DEFAULT_PARAMS),
    includeSaucer: false,
    saucerLayout: "nested", // "nested" | "side"
    material: "emerald_silk",
    prevSolidMaterial: "emerald_silk",
    xrayMode: false,
    caliperOverride: null, // null = auto (on when xray or section cut active), true = forced on, false = forced off
    wireframe: false,
    autoSpin: false,
    cutAxis: "y", // "y" = Vertical Profile Y, "z" = Horizontal Plan Slice Z
    crossCutPct: 0, // 0..100 for Vertical Y Cut (0 = Off)
    zSlicePct: 100, // 5..100 for Horizontal Z Slice (100 = Off / Full Height)
    lastGeoData: null,
    lastFrameCamera: null,
    isInteracting: false,
    busyAction: false,
    hostReport: null,
    clientMetrics: {
      dims: [110, 110, 160],
      maxOverhang: 0,
      warnPct: 0,
      critPct: 0,
      tris: 0,
      weightG: 0,
      fitsBed: true,
      fitsHeight: true,
      wallMm: 2.4,
      floorMm: 3.2,
      wallMinMm: 2.4,
      wallMaxMm: 2.4,
      mouthOuterDiam: 90.0,
      mouthInnerDiam: 85.2,
      hasActiveTexture: true
    },
    undoStack: [],
    redoStack: []
  };

  function isSectionCutActive() {
    return state.cutAxis === "z" ? (state.zSlicePct < 100) : (state.crossCutPct > 0);
  }

  function isCalipersActive() {
    if (state.caliperOverride !== null) return Boolean(state.caliperOverride);
    return Boolean(state.xrayMode || isSectionCutActive());
  }

  function tr(key) {
    const dict = I18N[state.lang] || I18N.pt;
    return dict[key] !== undefined ? dict[key] : key;
  }

  function getByPath(obj, path) {
    const parts = path.split(".");
    let cur = obj;
    for (let i = 0; i < parts.length; i++) {
      if (cur == null) return undefined;
      cur = cur[parts[i]];
    }
    return cur;
  }

  function setByPath(obj, path, val) {
    const parts = path.split(".");
    let cur = obj;
    for (let i = 0; i < parts.length - 1; i++) {
      if (cur[parts[i]] == null || typeof cur[parts[i]] !== "object") {
        cur[parts[i]] = {};
      }
      cur = cur[parts[i]];
    }
    cur[parts[parts.length - 1]] = val;
  }

  let dragSnapshot = null;
  function beginUndoGesture() {
    if (!dragSnapshot) {
      dragSnapshot = deepClone(state.params);
    }
  }

  function commitUndoGesture() {
    if (!dragSnapshot) return;
    if (JSON.stringify(dragSnapshot) !== JSON.stringify(state.params)) {
      state.undoStack.push(dragSnapshot);
      if (state.undoStack.length > 50) state.undoStack.shift();
      state.redoStack.length = 0;
      updateUndoButtons();
    }
    dragSnapshot = null;
  }

  function pushUndoSnapshot(beforeParams) {
    state.undoStack.push(deepClone(beforeParams));
    if (state.undoStack.length > 50) state.undoStack.shift();
    state.redoStack.length = 0;
    updateUndoButtons();
  }

  function performUndo() {
    if (!state.undoStack.length) return;
    state.redoStack.push(deepClone(state.params));
    state.params = normalizeParams(state.undoStack.pop());
    updateUndoButtons();
    syncControlsFromState();
    rebuildScene(false);
    scheduleHostAnalyze();
  }

  function performRedo() {
    if (!state.redoStack.length) return;
    state.undoStack.push(deepClone(state.params));
    state.params = normalizeParams(state.redoStack.pop());
    updateUndoButtons();
    syncControlsFromState();
    rebuildScene(false);
    scheduleHostAnalyze();
  }

  // ==========================================================================
  // 5. OrcaSlicer WebView2 Bridge (`window.orca.postMessage` / `onMessage`)
  // ==========================================================================
  let bridgeReadySent = false;
  let analyzeTimer = null;
  let lastPrinterSyncMs = 0;
  let pendingManualPrinterSync = false;
  let syncSpinTimer = null;

  function hasOrcaBridge() {
    return typeof window !== "undefined" && window.orca && typeof window.orca.postMessage === "function";
  }

  function sendToHost(payload) {
    if (hasOrcaBridge()) {
      try {
        window.orca.postMessage(payload);
        return true;
      } catch (err) {
        console.error("Orca bridge postMessage error:", err);
      }
    }
    return false;
  }

  function getPrinterSignature(pr) {
    if (!pr || typeof pr !== "object") return "";
    return [
      String(pr.name || ""),
      Number(pr.bed_x || 220).toFixed(2),
      Number(pr.bed_y || 220).toFixed(2),
      String(pr.bed_shape || "rectangular"),
      Number(pr.max_z || 250).toFixed(2),
      Number(pr.nozzle_mm || 0.4).toFixed(3),
      Number(pr.layer_height_mm || 0.2).toFixed(3),
      Number(pr.line_width_mm || 0.42).toFixed(3)
    ].join("|");
  }

  function getDynamicPrinterLimits() {
    const bx = Math.max(60.0, Number(state.printer.bed_x) || 220.0);
    const by = Math.max(60.0, Number(state.printer.bed_y) || 220.0);
    const mz = Math.max(50.0, Number(state.printer.max_z) || 250.0);
    const minBedXY = Math.min(bx, by);
    const maxHeight = Math.max(50, Math.min(500, Math.floor(mz)));
    const maxDiam = Math.max(40, Math.min(450, Math.floor(minBedXY - 4)));
    return {
      bedX: bx,
      bedY: by,
      minBedXY: minBedXY,
      maxZ: mz,
      maxHeight: maxHeight,
      maxDiam: maxDiam,
      maxCurveR: Math.max(20.0, Math.min(225.0, 0.5 * maxDiam))
    };
  }

  function requestPrinterSync(manualClick, minCooldownMs) {
    if (!manualClick && (state.isInteracting || state.busyAction)) return false;
    const now = Date.now();
    const cooldown = typeof minCooldownMs === "number" ? minCooldownMs : 250;
    if (!manualClick && (now - lastPrinterSyncMs) < cooldown) return false;
    lastPrinterSyncMs = now;
    if (manualClick) {
      pendingManualPrinterSync = true;
      const pill = document.getElementById("printer-pill");
      if (pill) {
        pill.classList.add("syncing");
        if (syncSpinTimer) clearTimeout(syncSpinTimer);
        syncSpinTimer = setTimeout(function () {
          pill.classList.remove("syncing");
        }, 420);
      }
    }
    return sendToHost({
      type: "sync_printer",
      params: deepClone(state.params)
    });
  }

  function scheduleHostAnalyze() {
    if (analyzeTimer) clearTimeout(analyzeTimer);
    analyzeTimer = setTimeout(function () {
      sendToHost({
        type: "analyze",
        params: deepClone(state.params)
      });
    }, 200);
  }

  function applyIncomingPrinter(printerPayload, announceIfChanged, forceAnnounce) {
    if (!printerPayload || typeof printerPayload !== "object") return false;
    const prevSig = getPrinterSignature(state.printer);
    state.printer = Object.assign({}, state.printer, printerPayload);
    const nextSig = getPrinterSignature(state.printer);
    const changed = prevSig !== nextSig;

    syncDynamicPrinterBounds();
    updatePrinterPillUI();
    rebuildBedGeometry();
    rebuildScene(false);

    if ((announceIfChanged && changed) || forceAnnounce) {
      const pr = state.printer;
      const isCirc = String(pr.bed_shape || "").toLowerCase() === "circular";
      const dimsLabel = (isCirc
        ? ("Ø" + Math.round(pr.bed_x || 220) + "×" + Math.round(pr.max_z || 250))
        : (Math.round(pr.bed_x || 220) + "×" + Math.round(pr.bed_y || 220) + "×" + Math.round(pr.max_z || 250))
      ) + " mm · " + Number(pr.nozzle_mm || 0.4).toFixed(1) + "mm";
      showToast(
        tr("toast_printer_synced")
          .replace("{name}", String(pr.name || "Printer"))
          .replace("{dims}", dimsLabel),
        false
      );
    }
    return changed;
  }

  function detectInjectedOrcaTheme() {
    if (typeof window === "undefined" || typeof window.getComputedStyle !== "function") return null;
    if (typeof document === "undefined" || !document.documentElement) return null;
    try {
      const style = window.getComputedStyle(document.documentElement);
      if (!style || typeof style.getPropertyValue !== "function") return null;
      const raw = String(style.getPropertyValue("--orca-bg") || "").trim();
      if (!raw) return null;
      let r = NaN, g = NaN, b = NaN;
      if (raw[0] === "#") {
        const hex = raw.slice(1).trim();
        if (hex.length === 3) {
          r = parseInt(hex[0] + hex[0], 16);
          g = parseInt(hex[1] + hex[1], 16);
          b = parseInt(hex[2] + hex[2], 16);
        } else if (hex.length >= 6) {
          r = parseInt(hex.slice(0, 2), 16);
          g = parseInt(hex.slice(2, 4), 16);
          b = parseInt(hex.slice(4, 6), 16);
        }
      } else {
        const m = raw.match(/rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)/i);
        if (m) {
          r = parseFloat(m[1]);
          g = parseFloat(m[2]);
          b = parseFloat(m[3]);
        }
      }
      if (!Number.isFinite(r) || !Number.isFinite(g) || !Number.isFinite(b)) return null;
      const lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0;
      return lum > 0.52 ? "light" : "dark";
    } catch (_) {
      return null;
    }
  }

  function handleHostMessage(rawData) {
    let msg = rawData;
    if (typeof rawData === "string") {
      try {
        msg = JSON.parse(rawData);
      } catch (_) {
        return;
      }
    }
    if (!msg || typeof msg !== "object") return;

    if (msg.type === "init_state") {
      if (msg.lang === "en" || msg.lang === "pt") state.lang = msg.lang;
      if (!state.userOverrodeTheme) {
        const cssTheme = msg.theme_explicit === false ? detectInjectedOrcaTheme() : null;
        if (cssTheme === "light" || cssTheme === "dark") {
          state.theme = cssTheme;
        } else if (msg.theme === "light" || msg.theme === "dark") {
          state.theme = msg.theme;
        }
      }
      if (msg.printer && typeof msg.printer === "object") {
        state.printer = Object.assign({}, state.printer, msg.printer);
      }
      if (Array.isArray(msg.builtin_presets) && msg.builtin_presets.length) {
        state.builtinPresets = msg.builtin_presets;
      }
      if (Array.isArray(msg.user_presets)) {
        state.userPresets = msg.user_presets;
      }
      if (msg.params && typeof msg.params === "object") {
        state.params = normalizeParams(msg.params);
      }
      lastPrinterSyncMs = Date.now();
      syncDynamicPrinterBounds();
      applyThemeAndLanguage();
      renderPresetsGrid();
      syncControlsFromState();
      rebuildBedGeometry();
      rebuildScene(false);
      fitCameraToVase();
      return;
    }

    if (msg.type === "printer_updated" && msg.printer && typeof msg.printer === "object") {
      const wasManual = pendingManualPrinterSync;
      pendingManualPrinterSync = false;
      let langOrThemeChanged = false;
      if ((msg.lang === "en" || msg.lang === "pt") && msg.lang !== state.lang) {
        state.lang = msg.lang;
        langOrThemeChanged = true;
      }
      if (!state.userOverrodeTheme) {
        const cssTheme = msg.theme_explicit === false ? detectInjectedOrcaTheme() : null;
        const resolvedTheme = (cssTheme === "light" || cssTheme === "dark") ? cssTheme : msg.theme;
        if ((resolvedTheme === "light" || resolvedTheme === "dark") && resolvedTheme !== state.theme) {
          state.theme = resolvedTheme;
          langOrThemeChanged = true;
        }
      }
      if (langOrThemeChanged) {
        applyThemeAndLanguage();
      }
      applyIncomingPrinter(msg.printer, true, wasManual);
      return;
    }

    if (msg.type === "analysis_result" && msg.report) {
      state.hostReport = msg.report;
      updatePrintabilityHud();
      return;
    }

    if (msg.type === "params_updated" && msg.params) {
      pushUndoSnapshot(state.params);
      state.params = normalizeParams(msg.params);
      syncControlsFromState();
      rebuildScene(false);
      scheduleHostAnalyze();
      showToast(tr("toast_randomized"), false);
      return;
    }

    if (msg.type === "presets_updated" && Array.isArray(msg.user_presets)) {
      state.userPresets = msg.user_presets;
      renderPresetsGrid();
      return;
    }

    if (msg.type === "action_result") {
      setActionButtonsBusy(false);
      if (msg.report) {
        state.hostReport = msg.report;
        updatePrintabilityHud();
      }
      if (msg.message) {
        showToast(msg.message, !msg.ok);
      }
      return;
    }
  }

  function connectOrcaBridge() {
    if (typeof window === "undefined") return;
    const tryBind = function () {
      if (window.orca && typeof window.orca.onMessage === "function" && !bridgeReadySent) {
        bridgeReadySent = true;
        window.orca.onMessage(handleHostMessage);
        sendToHost({ type: "ready", mode: state.mode });
      }
    };
    tryBind();
    if (!bridgeReadySent) {
      setTimeout(tryBind, 80);
      setTimeout(tryBind, 300);
    }
  }

  // ==========================================================================
  // 6. Client-Side 3D Mesh Builder (Vase + Drainage + Saucer + Bed Grid)
  // ==========================================================================
  function createChunkCollector() {
    const pos = [];
    const nrm = [];
    const ovh = [];
    const part = []; // 0.0 = vase, 1.0 = saucer
    const role = []; // 0.0 = outer wall/base, 1.0 = inner cavity/floor/drainage, 2.0 = top lip/cut cap
    const idx = [];
    const wire = [];

    return {
      pos: pos,
      nrm: nrm,
      ovh: ovh,
      part: part,
      role: role,
      idx: idx,
      wire: wire,
      vCount: 0,
      addVertex: function (x, y, z, nx, ny, nz, overhangDeg, partId, surfaceRole) {
        const id = this.vCount++;
        pos.push(x, y, z);
        nrm.push(nx, ny, nz);
        ovh.push(overhangDeg);
        part.push(partId);
        role.push(surfaceRole !== undefined ? surfaceRole : 0.0);
        return id;
      },
      addTri: function (a, b, c) {
        idx.push(a, b, c);
      },
      addWireSeg: function (x1, y1, z1, x2, y2, z2) {
        wire.push(x1, y1, z1, x2, y2, z2);
      }
    };
  }

  function raySectorDistance(hx, hy, dirX, dirY, halfAngle, outerRadius) {
    const b = 2.0 * (hx * dirX + hy * dirY);
    const c = hx * hx + hy * hy - outerRadius * outerRadius;
    const disc = Math.max(0.0, b * b - 4.0 * c);
    let bestT = 0.5 * (-b + Math.sqrt(disc));

    if (halfAngle < Math.PI - 1e-4) {
      const angles = [halfAngle, -halfAngle];
      for (let k = 0; k < 2; k++) {
        const ang = angles[k];
        const rx = Math.cos(ang);
        const ry = Math.sin(ang);
        const det = dirX * ry - dirY * rx;
        if (Math.abs(det) > 1e-8) {
          const tRay = (ry * (-hx) - rx * (-hy)) / det;
          const sRay = (dirX * (-hy) - dirY * (-hx)) / det;
          if (tRay > 1e-5 && sRay >= -1e-5 && tRay < bestT) {
            bestT = tRay;
          }
        }
      }
    }
    return Math.max(bestT, 0.1);
  }

  function appendPerforatedDiskAndTunnels(collector, outerR, zBot, zTop, capTopHoles, holeCount, holeDiam, ringRatio, partId) {
    const holeSegs = 20;
    const centered = (holeCount === 1 && ringRatio < 0.06) || ringRatio < 0.02;
    const nHoles = centered ? 1 : Math.max(1, holeCount | 0);
    const maxAllowedHr = centered
      ? Math.max(0.8, outerR * 0.42)
      : Math.max(0.8, Math.min(outerR * 0.28, outerR * ringRatio * Math.sin(Math.PI / Math.max(nHoles, 2)) * 0.76));
    const hr = Math.max(0.4, Math.min(0.5 * holeDiam, maxAllowedHr));
    const hDist = centered ? 0.0 : Math.max(hr + 0.8, Math.min(Math.max(hr + 0.8, outerR - hr - 0.9), outerR * ringRatio));
    const halfSector = Math.PI / nHoles;

    for (let k = 0; k < nHoles; k++) {
      const rot = (TWO_PI * k) / nHoles;
      const cosR = Math.cos(rot);
      const sinR = Math.sin(rot);

      const botInner = [];
      const botOuter = [];
      const topInner = [];
      const topOuter = [];

      for (let s = 0; s < holeSegs; s++) {
        const aLocal = (TWO_PI * s) / holeSegs;
        const dx = Math.cos(aLocal);
        const dy = Math.sin(aLocal);
        const dOut = raySectorDistance(hDist, 0.0, dx, dy, halfSector, outerR);

        const lxIn = hDist + hr * dx;
        const lyIn = hr * dy;
        const lxOut = hDist + dOut * dx;
        const lyOut = dOut * dy;

        const wxIn = lxIn * cosR - lyIn * sinR;
        const wyIn = lxIn * sinR + lyIn * cosR;
        const wxOut = lxOut * cosR - lyOut * sinR;
        const wyOut = lxOut * sinR + lyOut * cosR;

        botInner.push(collector.addVertex(wxIn, wyIn, zBot, 0, 0, -1, 0, partId, 0.0));
        botOuter.push(collector.addVertex(wxOut, wyOut, zBot, 0, 0, -1, 0, partId, 0.0));

        if (!capTopHoles) {
          topInner.push(collector.addVertex(wxIn, wyIn, zTop, 0, 0, 1, 0, partId, 1.0));
          topOuter.push(collector.addVertex(wxOut, wyOut, zTop, 0, 0, 1, 0, partId, 1.0));
        }

        // Tunnel cylinder vertices (role = 1.0 so drainage glow in X-Ray mode!)
        const nwx = -(dx * cosR - dy * sinR);
        const nwy = -(dx * sinR + dy * cosR);
        collector.addVertex(wxIn, wyIn, zBot, nwx, nwy, 0, 0, partId, 1.0);
        collector.addVertex(wxIn, wyIn, zTop, nwx, nwy, 0, 0, partId, 1.0);
      }

      const tunnelBase = collector.vCount - 2 * holeSegs;
      for (let s = 0; s < holeSegs; s++) {
        const sn = (s + 1) % holeSegs;
        collector.addTri(botInner[s], botOuter[sn], botOuter[s]);
        collector.addTri(botInner[s], botInner[sn], botOuter[sn]);

        if (!capTopHoles) {
          collector.addTri(topInner[s], topOuter[s], topOuter[sn]);
          collector.addTri(topInner[s], topOuter[sn], topInner[sn]);
        }

        const tb0 = tunnelBase + 2 * s;
        const tt0 = tb0 + 1;
        const tb1 = tunnelBase + 2 * sn;
        const tt1 = tb1 + 1;
        collector.addTri(tb0, tt0, tt1);
        collector.addTri(tb0, tt1, tb1);
      }

      if (capTopHoles) {
        const cwx = hDist * cosR;
        const cwy = hDist * sinR;
        const capCenter = collector.addVertex(cwx, cwy, zTop, 0, 0, -1, 0, partId, 1.0);
        const capRing = [];
        for (let s = 0; s < holeSegs; s++) {
          const aLocal = (TWO_PI * s) / holeSegs;
          const lxIn = hDist + hr * Math.cos(aLocal);
          const lyIn = hr * Math.sin(aLocal);
          capRing.push(collector.addVertex(lxIn * cosR - lyIn * sinR, lxIn * sinR + lyIn * cosR, zTop, 0, 0, -1, 0, partId, 1.0));
        }
        for (let s = 0; s < holeSegs; s++) {
          const sn = (s + 1) % holeSegs;
          collector.addTri(capCenter, capRing[sn], capRing[s]);
        }
      }
    }

    if (capTopHoles) {
      const fc = collector.addVertex(0, 0, zTop, 0, 0, 1, 0, partId, 1.0);
      const fr = [];
      const segs = 48;
      for (let s = 0; s < segs; s++) {
        const a = (TWO_PI * s) / segs;
        fr.push(collector.addVertex(outerR * Math.cos(a), outerR * Math.sin(a), zTop, 0, 0, 1, 0, partId, 1.0));
      }
      for (let s = 0; s < segs; s++) {
        collector.addTri(fc, fr[s], fr[(s + 1) % segs]);
      }
    }
  }

  function interpColumnAtZ(zVals, grid2D, colIdx, zTarget) {
    const nz = zVals.length;
    if (zTarget <= zVals[0]) return grid2D[0][colIdx];
    if (zTarget >= zVals[nz - 1]) return grid2D[nz - 1][colIdx];
    let lo = 0;
    let hi = nz - 1;
    while (hi - lo > 1) {
      const mid = (lo + hi) >> 1;
      if (zVals[mid] <= zTarget) lo = mid;
      else hi = mid;
    }
    const span = Math.max(1e-9, zVals[hi] - zVals[lo]);
    const t = (zTarget - zVals[lo]) / span;
    return grid2D[lo][colIdx] + t * (grid2D[hi][colIdx] - grid2D[lo][colIdx]);
  }

  function checkAnyTextureActive(p) {
    const t = p.textures;
    return Boolean(
      (t.ribbed.enabled && Math.abs(t.ribbed.depth_mm) > 0.05) ||
      (t.waves.enabled && Math.abs(t.waves.depth_mm) > 0.05) ||
      (t.origami.enabled && Math.abs(t.origami.depth_mm) > 0.05) ||
      (t.cellular.enabled && Math.abs(t.cellular.depth_mm) > 0.05)
    );
  }

  function buildFullStudioGeometry(p, fastInteractive) {
    const collector = createChunkCollector();
    const targetNz = fastInteractive ? Math.min(p.resolution_vertical, 128) : Math.min(p.resolution_vertical, 220);
    const targetNt = fastInteractive ? Math.min(p.resolution_angular, 144) : Math.min(p.resolution_angular, 240);

    const grid = evaluateRadiusGrid(p, targetNz, targetNt);
    const zVals = grid.z_vals;
    const thVals = grid.theta_vals;
    const radii = grid.radii;
    const nz = zVals.length;
    const nt = thVals.length;
    const heightMm = p.height_mm;

    const isHollow = p.print_mode === "shelled_hollow";
    const layerH = Math.max(0.08, Number(state.printer.layer_height_mm) || 0.2);
    const visWallMm = isHollow ? p.wall_thickness_mm : p.spiral_line_width_mm;
    const floorZ = isHollow
      ? Math.max(1.0, Math.min(heightMm * 0.65, p.bottom_thickness_mm))
      : Math.max(0.45, Math.min(heightMm * 0.34, p.spiral_bottom_layers * layerH + 0.30));

    const vaseOffsetX = (state.includeSaucer && state.saucerLayout === "side") ? -(0.32 * p.belly_diameter_mm + 16.0) : 0.0;
    const vaseLiftZ = (state.includeSaucer && state.saucerLayout === "nested")
      ? (p.saucer.floor_thickness_mm + p.saucer.inner_ribs_height_mm)
      : 0.0;

    const cosT = new Float64Array(nt);
    const sinT = new Float64Array(nt);
    for (let j = 0; j < nt; j++) {
      cosT[j] = Math.cos(thVals[j]);
      sinT[j] = Math.sin(thVals[j]);
    }

    // Precompute exact inner cavity radius grid matching mesh_generator.py (up to 25.0 mm walls!)
    const minBoreR = isHollow ? 3.0 : 2.5;
    const minSkinMm = isHollow ? 0.55 : 0.40;
    const innerGrid = new Array(nz);
    const slopeGrid = new Array(nz);
    for (let i = 0; i < nz; i++) {
      const iPrev = Math.max(0, i - 1);
      const iNext = Math.min(nz - 1, i + 1);
      const dzSpan = Math.max(1e-5, zVals[iNext] - zVals[iPrev]);
      const inRow = new Float64Array(nt);
      const slRow = new Float64Array(nt);
      for (let j = 0; j < nt; j++) {
        const rOut = radii[i][j];
        const rawSlope = (radii[iNext][j] - radii[iPrev][j]) / dzSpan;
        const slopeZ = Math.max(-3.0, Math.min(3.0, rawSlope));
        let rIn = rOut - visWallMm * Math.sqrt(1.0 + slopeZ * slopeZ);
        rIn = Math.min(rIn, rOut - minSkinMm);
        rIn = Math.max(minBoreR, rIn);
        inRow[j] = rIn;
        slRow[j] = slopeZ;
      }
      innerGrid[i] = inRow;
      slopeGrid[i] = slRow;
    }

    let minX = Infinity, maxX = -Infinity;
    let minY = Infinity, maxY = -Infinity;
    let maxOverhang = 0.0;
    let warnCount = 0;
    let critCount = 0;
    let totalOuterSamples = 0;
    let approxAreaMm2 = 0.0;

    // 1. Outer Vase Wall (role = 0.0)
    const outerGridIds = new Array(nz);
    const dTheta = TWO_PI / nt;
    for (let i = 0; i < nz; i++) {
      const rowIds = new Int32Array(nt);
      const z = zVals[i];
      const iPrev = Math.max(0, i - 1);
      const iNext = Math.min(nz - 1, i + 1);
      const dzSpan = Math.max(1e-5, zVals[iNext] - zVals[iPrev]);

      for (let j = 0; j < nt; j++) {
        const r = radii[i][j];
        const jPrev = (j + nt - 1) % nt;
        const jNext = (j + 1) % nt;

        const drDz = (radii[iNext][j] - radii[iPrev][j]) / dzSpan;
        const drDth = (radii[i][jNext] - radii[i][jPrev]) / (2.0 * dTheta);

        let nx = r * cosT[j] + drDth * sinT[j];
        let ny = r * sinT[j] - drDth * cosT[j];
        let nzVal = -r * drDz;
        const nLen = Math.hypot(nx, ny, nzVal) || 1.0;
        nx /= nLen;
        ny /= nLen;
        nzVal /= nLen;

        let ovhDeg = 0.0;
        if (i > 0 && nzVal < -1e-4) {
          ovhDeg = Math.asin(Math.max(0.0, Math.min(1.0, -nzVal))) / DEG2RAD;
          if (ovhDeg > maxOverhang) maxOverhang = ovhDeg;
          if (ovhDeg > 45.0) warnCount++;
          if (ovhDeg > 55.0) critCount++;
        }
        if (i > 0) totalOuterSamples++;

        const wx = r * cosT[j] + vaseOffsetX;
        const wy = r * sinT[j];
        const wz = z + vaseLiftZ;

        if (wx - vaseOffsetX < minX) minX = wx - vaseOffsetX;
        if (wx - vaseOffsetX > maxX) maxX = wx - vaseOffsetX;
        if (wy < minY) minY = wy;
        if (wy > maxY) maxY = wy;

        if (i < nz - 1) {
          const dzStep = zVals[i + 1] - z;
          approxAreaMm2 += r * dTheta * Math.hypot(dzStep, radii[i + 1][j] - r);
        }

        rowIds[j] = collector.addVertex(wx, wy, wz, nx, ny, nzVal, ovhDeg, 0.0, 0.0);
      }
      outerGridIds[i] = rowIds;
    }

    for (let i = 0; i < nz - 1; i++) {
      const r0 = outerGridIds[i];
      const r1 = outerGridIds[i + 1];
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        collector.addTri(r0[j], r0[jn], r1[jn]);
        collector.addTri(r0[j], r1[jn], r1[j]);
      }
    }

    // Wireframe isolines
    const wireStepI = Math.max(1, Math.floor(nz / 28));
    const wireStepJ = Math.max(1, Math.floor(nt / 32));
    for (let i = 0; i < nz; i += wireStepI) {
      const z = zVals[i] + vaseLiftZ;
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        collector.addWireSeg(
          radii[i][j] * cosT[j] + vaseOffsetX, radii[i][j] * sinT[j], z,
          radii[i][jn] * cosT[jn] + vaseOffsetX, radii[i][jn] * sinT[jn], z
        );
      }
    }
    for (let j = 0; j < nt; j += wireStepJ) {
      for (let i = 0; i < nz - 1; i += 2) {
        const i2 = Math.min(nz - 1, i + 2);
        collector.addWireSeg(
          radii[i][j] * cosT[j] + vaseOffsetX, radii[i][j] * sinT[j], zVals[i] + vaseLiftZ,
          radii[i2][j] * cosT[j] + vaseOffsetX, radii[i2][j] * sinT[j], zVals[i2] + vaseLiftZ
        );
      }
    }

    // 2. Inner Cavity Wall (role = 1.0) & Top Rim Bevel (role = 2.0)
    const rInFloor = new Float64Array(nt);
    for (let j = 0; j < nt; j++) {
      rInFloor[j] = Math.max(minBoreR, interpColumnAtZ(zVals, innerGrid, j, floorZ));
    }

    let floorIdxStart = 1;
    while (floorIdxStart < nz - 1 && zVals[floorIdxStart] <= floorZ + 1e-3) floorIdxStart++;

    const innerRings = [];
    // Exact floor ring at Z = floorZ
    const floorWallRing = new Int32Array(nt);
    for (let j = 0; j < nt; j++) {
      const sl0 = slopeGrid[Math.min(nz - 1, floorIdxStart)][j];
      let nx = -cosT[j], ny = -sinT[j], nzVal = sl0;
      const nl = Math.hypot(nx, ny, nzVal) || 1.0;
      floorWallRing[j] = collector.addVertex(
        rInFloor[j] * cosT[j] + vaseOffsetX,
        rInFloor[j] * sinT[j],
        floorZ + vaseLiftZ,
        nx / nl, ny / nl, nzVal / nl,
        0.0, 0.0, 1.0
      );
    }
    innerRings.push(floorWallRing);

    for (let i = floorIdxStart; i < nz; i++) {
      const z = zVals[i];
      const ring = new Int32Array(nt);
      for (let j = 0; j < nt; j++) {
        const rIn = innerGrid[i][j];
        const slopeZ = slopeGrid[i][j];
        let nx = -cosT[j];
        let ny = -sinT[j];
        let nzVal = slopeZ;
        const nLen = Math.hypot(nx, ny, nzVal) || 1.0;
        nx /= nLen;
        ny /= nLen;
        nzVal /= nLen;

        const ovhIn = (isHollow && nzVal < -1e-4)
          ? (Math.asin(Math.max(0.0, Math.min(1.0, -nzVal))) / DEG2RAD)
          : 0.0;

        ring[j] = collector.addVertex(
          rIn * cosT[j] + vaseOffsetX,
          rIn * sinT[j],
          z + vaseLiftZ,
          nx, ny, nzVal,
          ovhIn,
          0.0,
          1.0
        );
      }
      innerRings.push(ring);
    }

    for (let k = 0; k < innerRings.length - 1; k++) {
      const r0 = innerRings[k];
      const r1 = innerRings[k + 1];
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        collector.addTri(r0[j], r1[jn], r0[jn]);
        collector.addTri(r0[j], r1[j], r1[jn]);
      }
    }

    // Top Lip Annular Rim (role = 2.0)
    const topOuterRim = new Int32Array(nt);
    const topInnerRim = new Int32Array(nt);
    let minTopWallSpan = Infinity;
    for (let j = 0; j < nt; j++) {
      const sp = radii[nz - 1][j] - innerGrid[nz - 1][j];
      if (sp < minTopWallSpan) minTopWallSpan = sp;
    }
    const bevelLift = isHollow
      ? Math.min(p.lip_bevel_mm * 0.35, 0.42 * Math.max(0.0, minTopWallSpan), 1.4)
      : 0.05;
    const midTopRim = new Int32Array(nt);
    for (let j = 0; j < nt; j++) {
      const rOut = radii[nz - 1][j];
      const rIn = innerGrid[nz - 1][j];
      const rMid = 0.5 * (rOut + rIn);
      topOuterRim[j] = collector.addVertex(rOut * cosT[j] + vaseOffsetX, rOut * sinT[j], heightMm + vaseLiftZ, 0.35 * cosT[j], 0.35 * sinT[j], 0.94, 0, 0.0, 2.0);
      midTopRim[j] = collector.addVertex(rMid * cosT[j] + vaseOffsetX, rMid * sinT[j], heightMm + bevelLift + vaseLiftZ, 0, 0, 1, 0, 0.0, 2.0);
      topInnerRim[j] = collector.addVertex(rIn * cosT[j] + vaseOffsetX, rIn * sinT[j], heightMm + vaseLiftZ, -0.35 * cosT[j], -0.35 * sinT[j], 0.94, 0, 0.0, 2.0);
    }
    for (let j = 0; j < nt; j++) {
      const jn = (j + 1) % nt;
      collector.addTri(topOuterRim[j], topOuterRim[jn], midTopRim[jn]);
      collector.addTri(topOuterRim[j], midTopRim[jn], midTopRim[j]);
      collector.addTri(midTopRim[j], midTopRim[jn], topInnerRim[jn]);
      collector.addTri(midTopRim[j], topInnerRim[jn], topInnerRim[j]);
    }

    // 3. Bottom Base (role = 0.0) & Inner Floor / Drainage (role = 1.0)
    const minBaseOuterR = Math.min.apply(null, radii[0]);
    const minFloorInnerR = Math.max(2.5, Math.min(minBaseOuterR - minSkinMm, Math.min.apply(null, rInFloor)));

    if (p.drainage.enabled) {
      const vStart = collector.vCount;
      appendPerforatedDiskAndTunnels(
        collector,
        minFloorInnerR,
        vaseLiftZ,
        floorZ + vaseLiftZ,
        !isHollow,
        p.drainage.hole_count,
        p.drainage.hole_diameter_mm,
        p.drainage.ring_radius_ratio,
        0.0
      );
      if (Math.abs(vaseOffsetX) > 1e-5) {
        for (let vi = vStart; vi < collector.vCount; vi++) {
          collector.pos[3 * vi] += vaseOffsetX;
        }
      }
      // Annular rim on Z=0 between minFloorInnerR and actual outer polygon/circle radii[0]
      const botInnerRing = new Int32Array(nt);
      const botOuterRing = new Int32Array(nt);
      for (let j = 0; j < nt; j++) {
        botInnerRing[j] = collector.addVertex(minFloorInnerR * cosT[j] + vaseOffsetX, minFloorInnerR * sinT[j], vaseLiftZ, 0, 0, -1, 0, 0.0, 0.0);
        botOuterRing[j] = collector.addVertex(radii[0][j] * cosT[j] + vaseOffsetX, radii[0][j] * sinT[j], vaseLiftZ, 0, 0, -1, 0, 0.0, 0.0);
      }
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        collector.addTri(botInnerRing[j], botOuterRing[jn], botOuterRing[j]);
        collector.addTri(botInnerRing[j], botInnerRing[jn], botOuterRing[jn]);
      }
      // Annular rim on Z=floorZ between minFloorInnerR and actual rInFloor[j]
      const flrInnerRing = new Int32Array(nt);
      const flrOuterRing = new Int32Array(nt);
      for (let j = 0; j < nt; j++) {
        flrInnerRing[j] = collector.addVertex(minFloorInnerR * cosT[j] + vaseOffsetX, minFloorInnerR * sinT[j], floorZ + vaseLiftZ, 0, 0, 1, 0, 0.0, 1.0);
        flrOuterRing[j] = collector.addVertex(rInFloor[j] * cosT[j] + vaseOffsetX, rInFloor[j] * sinT[j], floorZ + vaseLiftZ, 0, 0, 1, 0, 0.0, 1.0);
      }
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        collector.addTri(flrInnerRing[j], flrOuterRing[j], flrOuterRing[jn]);
        collector.addTri(flrInnerRing[j], flrOuterRing[jn], flrInnerRing[jn]);
      }
    } else {
      const botCenter = collector.addVertex(vaseOffsetX, 0, vaseLiftZ, 0, 0, -1, 0, 0.0, 0.0);
      const flrCenter = collector.addVertex(vaseOffsetX, 0, floorZ + vaseLiftZ, 0, 0, 1, 0, 0.0, 1.0);
      const botRing = new Int32Array(nt);
      const flrRing = new Int32Array(nt);
      for (let j = 0; j < nt; j++) {
        botRing[j] = collector.addVertex(radii[0][j] * cosT[j] + vaseOffsetX, radii[0][j] * sinT[j], vaseLiftZ, 0, 0, -1, 0, 0.0, 0.0);
        flrRing[j] = collector.addVertex(rInFloor[j] * cosT[j] + vaseOffsetX, rInFloor[j] * sinT[j], floorZ + vaseLiftZ, 0, 0, 1, 0, 0.0, 1.0);
      }
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        collector.addTri(botCenter, botRing[jn], botRing[j]);
        collector.addTri(flrCenter, flrRing[j], flrRing[jn]);
      }
    }

    // 3B. Honest Spiral Mode Holographic Top-Cap Disk Indicator at Z = height_mm!
    const spiralCapCollector = createChunkCollector();
    if (!isHollow) {
      const capZ = heightMm + vaseLiftZ + 0.04;
      const capCenter = spiralCapCollector.addVertex(vaseOffsetX, 0, capZ, 0, 0, 1, 0, 0.0, 2.0);
      const capRing = new Int32Array(nt);
      for (let j = 0; j < nt; j++) {
        const rCap = innerGrid[nz - 1][j];
        capRing[j] = spiralCapCollector.addVertex(rCap * cosT[j] + vaseOffsetX, rCap * sinT[j], capZ, 0, 0, 1, 0, 0.0, 2.0);
      }
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        spiralCapCollector.addTri(capCenter, capRing[j], capRing[jn]);
      }
    }

    // 4. Optional Matching 3D Saucer Mesh
    let totalSpanX = maxX - minX;
    let totalSpanY = maxY - minY;

    if (state.includeSaucer) {
      const s = p.saucer;
      const baseMaxR = Math.max.apply(null, radii[0]);
      const rSaucerInner = baseMaxR + s.clearance_mm;
      const flareTan = Math.tan(12.0 * DEG2RAD);
      const sNz = 18;
      const sNt = Math.min(nt, 120);
      const saucerOffsetX = state.saucerLayout === "side"
        ? (vaseOffsetX + (maxX - minX) * 0.5 + rSaucerInner + s.wall_thickness_mm + s.rim_height_mm * flareTan + 12.0)
        : 0.0;

      const sOuterRings = [];
      const sInnerRings = [];
      const globalTwistRad = Number(p.global_twist_deg) * DEG2RAD;

      for (let i = 0; i < sNz; i++) {
        const t = i / (sNz - 1);
        const zOut = t * s.rim_height_mm;
        const zIn = s.floor_thickness_mm + t * (s.rim_height_mm - s.floor_thickness_mm);
        const rIn = rSaucerInner + zOut * flareTan;
        const rOutBase = rIn + s.wall_thickness_mm;

        const oRing = new Int32Array(sNt);
        const iRing = new Int32Array(sNt);
        const texEnv = Math.sin(Math.PI * t);

        for (let j = 0; j < sNt; j++) {
          const th = (TWO_PI * j) / sNt;
          const c = Math.cos(th);
          const sn = Math.sin(th);
          let texDr = 0.0;
          if (s.match_vase_texture && texEnv > 1e-4) {
            texDr = 0.45 * texEnv * computeTextureDisplacementScalar(zOut, t, th, th + globalTwistRad * t, p.textures, globalTwistRad);
          }
          const rOut = Math.max(rIn + 1.0, rOutBase + texDr);
          oRing[j] = collector.addVertex(rOut * c + saucerOffsetX, rOut * sn, zOut, c, sn, -flareTan * 0.6, 12.0, 1.0, 0.0);
          iRing[j] = collector.addVertex(rIn * c + saucerOffsetX, rIn * sn, zIn, -c, -sn, flareTan * 0.6, 0.0, 1.0, 1.0);
        }
        sOuterRings.push(oRing);
        sInnerRings.push(iRing);
      }

      for (let i = 0; i < sNz - 1; i++) {
        for (let j = 0; j < sNt; j++) {
          const jn = (j + 1) % sNt;
          collector.addTri(sOuterRings[i][j], sOuterRings[i][jn], sOuterRings[i + 1][jn]);
          collector.addTri(sOuterRings[i][j], sOuterRings[i + 1][jn], sOuterRings[i + 1][j]);
          collector.addTri(sInnerRings[i][j], sInnerRings[i + 1][jn], sInnerRings[i][jn]);
          collector.addTri(sInnerRings[i][j], sInnerRings[i + 1][j], sInnerRings[i + 1][jn]);
        }
      }

      const sBotCenter = collector.addVertex(saucerOffsetX, 0, 0, 0, 0, -1, 0, 1.0, 0.0);
      const sFlrCenter = collector.addVertex(saucerOffsetX, 0, s.floor_thickness_mm, 0, 0, 1, 0, 1.0, 1.0);
      const sFlrMidRing = new Int32Array(sNt);
      for (let j = 0; j < sNt; j++) {
        const th = (TWO_PI * j) / sNt;
        const ribWave = s.inner_ribs_height_mm * Math.pow(0.5 * (1.0 + Math.cos(8.0 * th)), 2.0);
        const rMid = 0.62 * rSaucerInner;
        sFlrMidRing[j] = collector.addVertex(rMid * Math.cos(th) + saucerOffsetX, rMid * Math.sin(th), s.floor_thickness_mm + ribWave, 0, 0, 1, 0, 1.0, 1.0);
      }

      for (let j = 0; j < sNt; j++) {
        const jn = (j + 1) % sNt;
        collector.addTri(sOuterRings[sNz - 1][j], sOuterRings[sNz - 1][jn], sInnerRings[sNz - 1][jn]);
        collector.addTri(sOuterRings[sNz - 1][j], sInnerRings[sNz - 1][jn], sInnerRings[sNz - 1][j]);
        collector.addTri(sBotCenter, sOuterRings[0][jn], sOuterRings[0][j]);
        collector.addTri(sFlrCenter, sFlrMidRing[j], sFlrMidRing[jn]);
        collector.addTri(sFlrMidRing[j], sInnerRings[0][j], sInnerRings[0][jn]);
        collector.addTri(sFlrMidRing[j], sInnerRings[0][jn], sFlrMidRing[jn]);
      }

      const saucerOuterMax = rSaucerInner + s.wall_thickness_mm + s.rim_height_mm * flareTan;
      if (state.saucerLayout === "side") {
        totalSpanX = (saucerOffsetX + saucerOuterMax) - (vaseOffsetX + minX);
        totalSpanY = Math.max(totalSpanY, 2.0 * saucerOuterMax);
      } else {
        totalSpanX = Math.max(totalSpanX, 2.0 * saucerOuterMax);
        totalSpanY = Math.max(totalSpanY, 2.0 * saucerOuterMax);
      }
    }

    // Mouth & wall thickness metrics across cavity height
    let sumMouthOutR = 0.0;
    let sumMouthInR = 0.0;
    for (let j = 0; j < nt; j++) {
      sumMouthOutR += radii[nz - 1][j];
      sumMouthInR += innerGrid[nz - 1][j];
    }
    const mouthOuterDiam = 2.0 * (sumMouthOutR / nt);
    const mouthInnerDiam = 2.0 * (sumMouthInR / nt);

    let wallMinMm = Infinity;
    let wallMaxMm = 0.0;
    for (let i = floorIdxStart; i < nz; i++) {
      for (let j = 0; j < nt; j++) {
        const wSpan = radii[i][j] - innerGrid[i][j];
        if (wSpan < wallMinMm) wallMinMm = wSpan;
        if (wSpan > wallMaxMm) wallMaxMm = wSpan;
      }
    }
    if (!Number.isFinite(wallMinMm)) {
      wallMinMm = visWallMm;
      wallMaxMm = visWallMm;
    }

    const hasActiveTexture = checkAnyTextureActive(p);

    // Client-side printability metrics
    const dx = maxX - minX;
    const dy = maxY - minY;
    const dz = heightMm;
    const baseAreaMm2 = Math.PI * minBaseOuterR * minBaseOuterR;
    const shellVolCm3 = (approxAreaMm2 * visWallMm + baseAreaMm2 * floorZ) / 1000.0;
    const estWeightG = shellVolCm3 * 1.24;
    const fullResolutionTris = (isHollow ? 4 : 2) * p.resolution_angular * p.resolution_vertical;

    const isCircBed = String(state.printer.bed_shape || "").toLowerCase() === "circular";
    const bedLimitXY = Math.min(Number(state.printer.bed_x) || 220, Number(state.printer.bed_y) || 220);
    const fitsBed = isCircBed
      ? (Math.max(totalSpanX, totalSpanY) <= bedLimitXY + 1e-3)
      : (totalSpanX <= (Number(state.printer.bed_x) || 220) + 1e-3 && totalSpanY <= (Number(state.printer.bed_y) || 220) + 1e-3);
    const fitsHeight = dz <= (Number(state.printer.max_z) || 250) + 1e-3;

    state.clientMetrics = {
      dims: [dx, dy, dz],
      maxOverhang: maxOverhang,
      warnPct: totalOuterSamples > 0 ? (100.0 * warnCount / totalOuterSamples) : 0,
      critPct: totalOuterSamples > 0 ? (100.0 * critCount / totalOuterSamples) : 0,
      tris: fullResolutionTris,
      weightG: estWeightG,
      fitsBed: fitsBed,
      fitsHeight: fitsHeight,
      wallMm: visWallMm,
      floorMm: floorZ,
      wallMinMm: wallMinMm,
      wallMaxMm: wallMaxMm,
      mouthOuterDiam: mouthOuterDiam,
      mouthInnerDiam: mouthInnerDiam,
      hasActiveTexture: hasActiveTexture
    };

    state.lastGeoData = {
      zVals: zVals,
      thVals: thVals,
      cosT: cosT,
      sinT: sinT,
      radii: radii,
      innerGrid: innerGrid,
      rInFloor: rInFloor,
      floorZ: floorZ,
      heightMm: heightMm,
      visWallMm: visWallMm,
      vaseOffsetX: vaseOffsetX,
      vaseLiftZ: vaseLiftZ,
      isHollow: isHollow,
      hasActiveTexture: hasActiveTexture
    };

    return {
      positions: new Float32Array(collector.pos),
      normals: new Float32Array(collector.nrm),
      overhangs: new Float32Array(collector.ovh),
      parts: new Float32Array(collector.part),
      roles: new Float32Array(collector.role),
      indices: new Uint32Array(collector.idx),
      wirePositions: new Float32Array(collector.wire),
      spiralCapPositions: new Float32Array(spiralCapCollector.pos),
      spiralCapNormals: new Float32Array(spiralCapCollector.nrm),
      spiralCapOverhangs: new Float32Array(spiralCapCollector.ovh),
      spiralCapParts: new Float32Array(spiralCapCollector.part),
      spiralCapRoles: new Float32Array(spiralCapCollector.role),
      spiralCapIndices: new Uint32Array(spiralCapCollector.idx),
      grid: grid
    };
  }

  function sampleGeoAtHeight(zLocalMm) {
    const gd = state.lastGeoData;
    if (!gd) return null;
    const nt = gd.thVals.length;
    const zClamped = Math.max(0.0, Math.min(gd.heightMm, zLocalMm));
    const rOutArr = new Float64Array(nt);
    const rInArr = new Float64Array(nt);
    let sumOut = 0.0;
    let sumIn = 0.0;
    let wMin = Infinity;
    let wMax = 0.0;
    const inSolidFloor = zClamped < gd.floorZ - 1e-4;

    for (let j = 0; j < nt; j++) {
      const ro = interpColumnAtZ(gd.zVals, gd.radii, j, zClamped);
      const ri = inSolidFloor ? 0.0 : interpColumnAtZ(gd.zVals, gd.innerGrid, j, zClamped);
      rOutArr[j] = ro;
      rInArr[j] = ri;
      sumOut += ro;
      sumIn += ri;
      const w = ro - ri;
      if (w < wMin) wMin = w;
      if (w > wMax) wMax = w;
    }

    return {
      zLocal: zClamped,
      zWorld: zClamped + gd.vaseLiftZ,
      inSolidFloor: inSolidFloor,
      rOut: rOutArr,
      rIn: rInArr,
      dOutMean: 2.0 * (sumOut / nt),
      dInMean: inSolidFloor ? 0.0 : 2.0 * (sumIn / nt),
      wMean: (sumOut - sumIn) / nt,
      wMin: wMin,
      wMax: wMax
    };
  }

  function buildHorizontalZSliceCap() {
    const gd = state.lastGeoData;
    if (!gd || state.cutAxis !== "z" || state.zSlicePct >= 100) return null;
    const zLocal = gd.heightMm * (state.zSlicePct / 100.0);
    const sl = sampleGeoAtHeight(zLocal);
    if (!sl) return null;

    const nt = gd.thVals.length;
    const col = createChunkCollector();
    const zCap = sl.zWorld;

    if (sl.inSolidFloor) {
      const cIdx = col.addVertex(gd.vaseOffsetX, 0.0, zCap, 0, 0, 1, 0, 0.0, 2.0);
      const oRing = new Int32Array(nt);
      for (let j = 0; j < nt; j++) {
        oRing[j] = col.addVertex(
          sl.rOut[j] * gd.cosT[j] + gd.vaseOffsetX,
          sl.rOut[j] * gd.sinT[j],
          zCap, 0, 0, 1, 0, 0.0, 2.0
        );
      }
      for (let j = 0; j < nt; j++) {
        col.addTri(cIdx, oRing[j], oRing[(j + 1) % nt]);
      }
    } else {
      const oRing = new Int32Array(nt);
      const iRing = new Int32Array(nt);
      for (let j = 0; j < nt; j++) {
        oRing[j] = col.addVertex(
          sl.rOut[j] * gd.cosT[j] + gd.vaseOffsetX,
          sl.rOut[j] * gd.sinT[j],
          zCap, 0, 0, 1, 0, 0.0, 2.0
        );
        iRing[j] = col.addVertex(
          sl.rIn[j] * gd.cosT[j] + gd.vaseOffsetX,
          sl.rIn[j] * gd.sinT[j],
          zCap, 0, 0, 1, 0, 0.0, 2.0
        );
      }
      for (let j = 0; j < nt; j++) {
        const jn = (j + 1) % nt;
        col.addTri(iRing[j], oRing[j], oRing[jn]);
        col.addTri(iRing[j], oRing[jn], iRing[jn]);
      }
    }

    return {
      positions: new Float32Array(col.pos),
      normals: new Float32Array(col.nrm),
      overhangs: new Float32Array(col.ovh),
      parts: new Float32Array(col.part),
      roles: new Float32Array(col.role),
      indices: new Uint32Array(col.idx)
    };
  }

  // ==========================================================================
  // 7. WebGL2 3D Viewport Engine (X-Ray Two-Pass + Dual Section + Calipers)
  // ==========================================================================
  let gl = null;
  let isWebGL2 = false;
  let meshProg = null;
  let lineProg = null;
  let meshBuffers = null;
  let spiralCapBuffers = null;
  let spiralCapIndexCount = 0;
  let spiralCapIndexType = 0;
  let sectionCapBuffers = null;
  let sectionCapIndexCount = 0;
  let sectionCapIndexType = 0;
  let wireBuffer = null;
  let wireVertCount = 0;
  let bedBuffer = null;
  let bedVertCount = 0;
  let indexCount = 0;
  let indexType = 0;

  const camera = {
    yaw: -0.68,
    pitch: 0.36,
    distance: 330.0,
    target: [0.0, 0.0, 80.0]
  };

  function mat4Identity() {
    const m = new Float32Array(16);
    m[0] = 1; m[5] = 1; m[10] = 1; m[15] = 1;
    return m;
  }

  function mat4Multiply(a, b) {
    const out = new Float32Array(16);
    for (let col = 0; col < 4; col++) {
      const b0 = b[col * 4], b1 = b[col * 4 + 1], b2 = b[col * 4 + 2], b3 = b[col * 4 + 3];
      out[col * 4]     = a[0] * b0 + a[4] * b1 + a[8]  * b2 + a[12] * b3;
      out[col * 4 + 1] = a[1] * b0 + a[5] * b1 + a[9]  * b2 + a[13] * b3;
      out[col * 4 + 2] = a[2] * b0 + a[6] * b1 + a[10] * b2 + a[14] * b3;
      out[col * 4 + 3] = a[3] * b0 + a[7] * b1 + a[11] * b2 + a[15] * b3;
    }
    return out;
  }

  function mat4Perspective(fovyRad, aspect, near, far) {
    const f = 1.0 / Math.tan(0.5 * fovyRad);
    const nf = 1.0 / (near - far);
    const out = new Float32Array(16);
    out[0] = f / Math.max(aspect, 0.05);
    out[5] = f;
    out[10] = (far + near) * nf;
    out[11] = -1.0;
    out[14] = (2.0 * far * near) * nf;
    return out;
  }

  function mat4LookAtZUp(eye, center) {
    let fx = center[0] - eye[0];
    let fy = center[1] - eye[1];
    let fz = center[2] - eye[2];
    const fl = Math.hypot(fx, fy, fz) || 1.0;
    fx /= fl; fy /= fl; fz /= fl;

    let upX = 0.0, upY = 0.0, upZ = 1.0;
    if (Math.abs(fz) > 0.999) {
      upY = 1.0; upZ = 0.0;
    }

    let sx = fy * upZ - fz * upY;
    let sy = fz * upX - fx * upZ;
    let sz = fx * upY - fy * upX;
    const sl = Math.hypot(sx, sy, sz) || 1.0;
    sx /= sl; sy /= sl; sz /= sl;

    const ux = sy * fz - sz * fy;
    const uy = sz * fx - sx * fz;
    const uz = sx * fy - sy * fx;

    const out = mat4Identity();
    out[0] = sx;  out[4] = sy;  out[8]  = sz;  out[12] = -(sx * eye[0] + sy * eye[1] + sz * eye[2]);
    out[1] = ux;  out[5] = uy;  out[9]  = uz;  out[13] = -(ux * eye[0] + uy * eye[1] + uz * eye[2]);
    out[2] = -fx; out[6] = -fy; out[10] = -fz; out[14] = (fx * eye[0] + fy * eye[1] + fz * eye[2]);
    out[3] = 0;   out[7] = 0;   out[11] = 0;   out[15] = 1;
    return out;
  }

  function compileProgram(glCtx, vsSrc, fsSrc) {
    const vs = glCtx.createShader(glCtx.VERTEX_SHADER);
    glCtx.shaderSource(vs, vsSrc);
    glCtx.compileShader(vs);
    if (!glCtx.getShaderParameter(vs, glCtx.COMPILE_STATUS)) {
      console.error("VS error:", glCtx.getShaderInfoLog(vs));
      return null;
    }
    const fs = glCtx.createShader(glCtx.FRAGMENT_SHADER);
    glCtx.shaderSource(fs, fsSrc);
    glCtx.compileShader(fs);
    if (!glCtx.getShaderParameter(fs, glCtx.COMPILE_STATUS)) {
      console.error("FS error:", glCtx.getShaderInfoLog(fs));
      return null;
    }
    const prog = glCtx.createProgram();
    glCtx.attachShader(prog, vs);
    glCtx.attachShader(prog, fs);
    glCtx.linkProgram(prog);
    if (!glCtx.getProgramParameter(prog, glCtx.LINK_STATUS)) {
      console.error("Link error:", glCtx.getProgramInfoLog(prog));
      return null;
    }
    return prog;
  }

  function createMeshBufferSet(glCtx) {
    return {
      pos: glCtx.createBuffer(),
      nrm: glCtx.createBuffer(),
      ovh: glCtx.createBuffer(),
      part: glCtx.createBuffer(),
      role: glCtx.createBuffer(),
      idx: glCtx.createBuffer()
    };
  }

  function initWebGLViewport() {
    const canvas = document.getElementById("gl-canvas");
    if (!canvas || !canvas.getContext) return;

    gl = canvas.getContext("webgl2", { antialias: true, alpha: false, depth: true });
    if (gl) {
      isWebGL2 = true;
    } else {
      gl = canvas.getContext("webgl", { antialias: true, alpha: false, depth: true });
      isWebGL2 = false;
      if (gl) gl.getExtension("OES_element_index_uint");
    }
    if (!gl) return;

    const vsMesh300 = `#version 300 es
      precision highp float;
      in vec3 a_pos;
      in vec3 a_nrm;
      in float a_ovh;
      in float a_part;
      in float a_role;
      uniform mat4 u_mvp;
      out vec3 v_pos;
      out vec3 v_nrm;
      out float v_ovh;
      out float v_part;
      out float v_surfaceRole;
      void main() {
        v_pos = a_pos;
        v_nrm = a_nrm;
        v_ovh = a_ovh;
        v_part = a_part;
        v_surfaceRole = a_role;
        gl_Position = u_mvp * vec4(a_pos, 1.0);
      }
    `;

    const fsMesh300 = `#version 300 es
      precision highp float;
      in vec3 v_pos;
      in vec3 v_nrm;
      in float v_ovh;
      in float v_part;
      in float v_surfaceRole;
      uniform vec3 u_eye;
      uniform vec3 u_baseColor;
      uniform vec3 u_saucerColor;
      uniform float u_roughness;
      uniform float u_metallic;
      uniform float u_heatmap;
      uniform float u_xrayMode;
      uniform float u_clipMode;
      uniform float u_clipVal;
      uniform float u_passMode;
      uniform float u_lightTheme;
      out vec4 outColor;

      vec3 heatmapColor(float deg) {
        vec3 safeA = vec3(0.02, 0.76, 0.45);
        vec3 safeB = vec3(0.18, 0.85, 0.42);
        vec3 warn  = vec3(1.00, 0.68, 0.02);
        vec3 crit  = vec3(0.98, 0.20, 0.16);
        if (deg <= 42.0) return mix(safeA, safeB, clamp(deg / 42.0, 0.0, 1.0));
        if (deg <= 46.0) return mix(safeB, warn, (deg - 42.0) / 4.0);
        if (deg <= 55.0) return mix(warn, crit, (deg - 46.0) / 9.0);
        return crit;
      }

      void main() {
        float clipRim = 0.0;
        if (u_clipMode > 0.5 && u_passMode < 0.5) {
          float dist = (u_clipMode < 1.5) ? (v_pos.y - u_clipVal) : (u_clipVal - v_pos.z);
          if (dist < 0.0) {
            discard;
          }
          if (dist < 1.45) {
            clipRim = 1.0 - (dist / 1.45);
          }
        } else if (u_clipMode > 0.5 && u_clipMode < 1.5 && u_passMode > 1.5) {
          if (v_pos.y < u_clipVal) discard;
        }

        // Special Pass 1: Solid Horizontal Z-Slice CAD Cross-Section Cap
        if (u_passMode > 0.5 && u_passMode < 1.5) {
          float hatch = sin((v_pos.x + v_pos.y) * 2.35);
          vec3 capA = vec3(1.00, 0.76, 0.20);
          vec3 capB = vec3(0.08, 0.92, 0.80);
          vec3 cCol = mix(capA, capB, hatch > 0.25 ? 0.65 : 0.12);
          outColor = vec4(cCol, u_xrayMode > 0.5 ? 0.90 : 1.0);
          return;
        }

        // Special Pass 2: Holographic Spiral Mode Top-Cap Indicator Disk
        if (u_passMode > 1.5) {
          float r = length(v_pos.xy);
          float rings = 0.5 + 0.5 * sin(r * 1.45);
          float diag = step(0.35, fract((v_pos.x - v_pos.y) * 0.14));
          vec3 holoCol = mix(vec3(1.00, 0.68, 0.18), vec3(0.10, 0.92, 0.82), rings * 0.65);
          float alpha = 0.18 + 0.20 * diag * rings;
          outColor = vec4(holoCol, alpha);
          return;
        }

        vec3 N = normalize(v_nrm);
        bool backFace = !gl_FrontFacing;
        if (backFace) N = -N;

        vec3 V = normalize(u_eye - v_pos);
        vec3 L1 = normalize(vec3(-0.52, -0.64, 0.56));
        vec3 L2 = normalize(vec3(0.68, -0.25, 0.42));
        vec3 L3 = normalize(vec3(0.05, 0.82, 0.35));
        float diff1 = max(dot(N, L1), 0.0);
        float diff2 = max(dot(N, L2), 0.0);
        float diff3 = max(dot(N, L3), 0.0);

        // Two-Pass Translucent X-Ray / Wall Caliper Shader
        if (u_xrayMode > 0.5) {
          float ndv = abs(dot(N, V));
          float fresnel = pow(1.0 - clamp(ndv, 0.0, 1.0), 2.15);
          vec3 Hx = normalize(L1 + V);
          float specX = pow(max(dot(N, Hx), 0.0), 54.0) * 0.45;

          vec3 xCol;
          float xAlpha;
          if (v_surfaceRole > 0.5 && v_surfaceRole < 1.5) {
            // Inner cavity wall, inner floor, and drainage holes -> warm glowing amber/coral!
            bool isFloorPlane = abs(N.z) > 0.68;
            vec3 innerBase = isFloorPlane ? vec3(1.00, 0.43, 0.18) : vec3(1.00, 0.58, 0.22);
            if (u_lightTheme > 0.5) innerBase *= 0.88;
            xCol = innerBase * (0.48 + 0.55 * diff1 + 0.25 * diff2)
                 + vec3(1.00, 0.84, 0.46) * (fresnel * 0.65 + specX * 0.5);
            xAlpha = isFloorPlane ? (0.52 + 0.28 * fresnel) : (0.35 + 0.42 * fresnel);
          } else if (v_surfaceRole >= 1.5) {
            // Top mouth lip / rim -> crisp luminous cyan-gold ring
            xCol = vec3(0.28, 0.96, 0.86) * (0.58 + 0.42 * diff1) + vec3(0.85) * specX;
            xAlpha = 0.62 + 0.28 * fresnel;
          } else {
            // Outer wall -> smoky emerald/cyan glass with Fresnel rim glow
            vec3 glassBase = (u_lightTheme > 0.5) ? vec3(0.00, 0.56, 0.52) : vec3(0.05, 0.82, 0.74);
            if (v_part > 0.5) glassBase = (u_lightTheme > 0.5) ? vec3(0.22, 0.42, 0.46) : vec3(0.18, 0.55, 0.58);
            xCol = glassBase * (0.40 + 0.52 * diff1 + 0.22 * diff2)
                 + vec3(0.46, 0.98, 0.92) * (fresnel * 0.78)
                 + vec3(1.0) * specX;
            xAlpha = 0.15 + 0.48 * fresnel + specX * 0.28;
          }

          if (backFace) xAlpha *= 0.76;
          if (clipRim > 0.01) {
            xCol = mix(xCol, vec3(1.00, 0.82, 0.24), clipRim * 0.88);
            xAlpha = max(xAlpha, 0.94 * clipRim);
          }
          outColor = vec4(clamp(xCol, 0.0, 1.0), clamp(xAlpha, 0.08, 0.95));
          return;
        }

        // Standard Opaque PBR-Lite Studio Shading
        vec3 albedo = v_part > 0.5 ? u_saucerColor : u_baseColor;
        if (u_heatmap > 0.5) {
          albedo = heatmapColor(v_ovh);
        } else if (u_clipMode > 0.5 && v_surfaceRole > 0.5 && v_surfaceRole < 1.5) {
          albedo = mix(albedo, vec3(0.98, 0.58, 0.24), 0.42);
        } else if (backFace && u_clipMode > 0.5) {
          albedo = mix(albedo, vec3(1.0, 0.72, 0.28), 0.45);
        }

        float layerWave = 0.985 + 0.015 * sin(v_pos.z * 31.4159);
        albedo *= layerWave;

        vec3 H1 = normalize(L1 + V);
        float shininess = mix(96.0, 14.0, u_roughness);
        float spec1 = pow(max(dot(N, H1), 0.0), shininess) * mix(0.28, 0.85, 1.0 - u_roughness);

        float hemi = 0.5 + 0.5 * N.z;
        vec3 ambient = mix(vec3(0.14, 0.16, 0.20), vec3(0.34, 0.37, 0.42), hemi);
        float rim = pow(1.0 - max(dot(N, V), 0.0), 3.2) * 0.22;

        vec3 specTint = mix(vec3(1.0), albedo, u_metallic);
        vec3 color = albedo * (ambient + 0.78 * diff1 + 0.32 * diff2 + 0.22 * diff3)
                   + specTint * spec1
                   + vec3(0.55, 0.85, 0.80) * rim;

        if (clipRim > 0.01) {
          color = mix(color, vec3(1.00, 0.80, 0.22), clipRim * 0.85);
        }

        color = pow(clamp(color, 0.0, 1.0), vec3(0.92));
        outColor = vec4(color, 1.0);
      }
    `;

    const vsLine300 = `#version 300 es
      precision highp float;
      in vec3 a_pos;
      uniform mat4 u_mvp;
      void main() {
        gl_Position = u_mvp * vec4(a_pos, 1.0);
      }
    `;

    const fsLine300 = `#version 300 es
      precision highp float;
      uniform vec4 u_color;
      out vec4 outColor;
      void main() {
        outColor = u_color;
      }
    `;

    const vsMesh100 = `
      precision highp float;
      attribute vec3 a_pos;
      attribute vec3 a_nrm;
      attribute float a_ovh;
      attribute float a_part;
      attribute float a_role;
      uniform mat4 u_mvp;
      varying vec3 v_pos;
      varying vec3 v_nrm;
      varying float v_ovh;
      varying float v_part;
      varying float v_surfaceRole;
      void main() {
        v_pos = a_pos;
        v_nrm = a_nrm;
        v_ovh = a_ovh;
        v_part = a_part;
        v_surfaceRole = a_role;
        gl_Position = u_mvp * vec4(a_pos, 1.0);
      }
    `;

    const fsMesh100 = `
      precision highp float;
      varying vec3 v_pos;
      varying vec3 v_nrm;
      varying float v_ovh;
      varying float v_part;
      varying float v_surfaceRole;
      uniform vec3 u_eye;
      uniform vec3 u_baseColor;
      uniform vec3 u_saucerColor;
      uniform float u_roughness;
      uniform float u_metallic;
      uniform float u_heatmap;
      uniform float u_xrayMode;
      uniform float u_clipMode;
      uniform float u_clipVal;
      uniform float u_passMode;
      uniform float u_lightTheme;
      vec3 heatmapColor(float deg) {
        if (deg <= 45.0) return vec3(0.08, 0.80, 0.44);
        if (deg <= 55.0) return vec3(1.00, 0.68, 0.02);
        return vec3(0.98, 0.20, 0.16);
      }
      void main() {
        float clipRim = 0.0;
        if (u_clipMode > 0.5 && u_passMode < 0.5) {
          float dist = (u_clipMode < 1.5) ? (v_pos.y - u_clipVal) : (u_clipVal - v_pos.z);
          if (dist < 0.0) discard;
          if (dist < 1.45) clipRim = 1.0 - (dist / 1.45);
        }
        if (u_passMode > 0.5 && u_passMode < 1.5) {
          gl_FragColor = vec4(0.98, 0.78, 0.24, 0.92);
          return;
        }
        if (u_passMode > 1.5) {
          gl_FragColor = vec4(0.20, 0.88, 0.78, 0.28);
          return;
        }
        vec3 N = normalize(v_nrm);
        if (!gl_FrontFacing) N = -N;
        vec3 V = normalize(u_eye - v_pos);
        if (u_xrayMode > 0.5) {
          float fresnel = pow(1.0 - clamp(abs(dot(N, V)), 0.0, 1.0), 2.0);
          vec3 col = (v_surfaceRole > 0.5 && v_surfaceRole < 1.5)
            ? vec3(1.0, 0.55, 0.20)
            : vec3(0.06, 0.82, 0.74);
          float a = (v_surfaceRole > 0.5 && v_surfaceRole < 1.5) ? (0.42 + 0.35 * fresnel) : (0.18 + 0.45 * fresnel);
          if (clipRim > 0.01) { col = vec3(1.0, 0.82, 0.24); a = max(a, 0.92 * clipRim); }
          gl_FragColor = vec4(col, a);
          return;
        }
        vec3 albedo = u_heatmap > 0.5 ? heatmapColor(v_ovh) : (v_part > 0.5 ? u_saucerColor : u_baseColor);
        vec3 L1 = normalize(vec3(-0.52, -0.64, 0.56));
        float diff = max(dot(N, L1), 0.0);
        vec3 H = normalize(L1 + V);
        float spec = pow(max(dot(N, H), 0.0), 42.0) * 0.35;
        vec3 outC = albedo * (0.32 + 0.75 * diff) + vec3(spec);
        if (clipRim > 0.01) outC = mix(outC, vec3(1.0, 0.80, 0.22), clipRim * 0.85);
        gl_FragColor = vec4(outC, 1.0);
      }
    `;

    const vsLine100 = `
      precision highp float;
      attribute vec3 a_pos;
      uniform mat4 u_mvp;
      void main() { gl_Position = u_mvp * vec4(a_pos, 1.0); }
    `;

    const fsLine100 = `
      precision highp float;
      uniform vec4 u_color;
      void main() { gl_FragColor = u_color; }
    `;

    meshProg = compileProgram(gl, isWebGL2 ? vsMesh300 : vsMesh100, isWebGL2 ? fsMesh300 : fsMesh100);
    lineProg = compileProgram(gl, isWebGL2 ? vsLine300 : vsLine100, isWebGL2 ? fsLine300 : fsLine100);

    meshBuffers = createMeshBufferSet(gl);
    spiralCapBuffers = createMeshBufferSet(gl);
    sectionCapBuffers = createMeshBufferSet(gl);
    wireBuffer = gl.createBuffer();
    bedBuffer = gl.createBuffer();

    rebuildBedGeometry();
    bindViewportEvents(canvas);
  }

  function rebuildBedGeometry() {
    if (!gl || !bedBuffer) return;
    const bx = Math.max(80, Number(state.printer.bed_x) || 220);
    const by = Math.max(80, Number(state.printer.bed_y) || 220);
    const hx = 0.5 * bx;
    const hy = 0.5 * by;
    const isCircular = String(state.printer.bed_shape || "").toLowerCase() === "circular";
    const verts = [];

    const step = bx > 320 || by > 320 ? 30 : 20;
    if (isCircular) {
      const rBed = Math.min(hx, hy);
      const rSq = rBed * rBed;
      for (let x = -Math.floor(rBed / step) * step; x <= rBed + 0.01; x += step) {
        const spanY = Math.sqrt(Math.max(0.0, rSq - x * x));
        if (spanY > 1.0) verts.push(x, -spanY, -0.08, x, spanY, -0.08);
      }
      for (let y = -Math.floor(rBed / step) * step; y <= rBed + 0.01; y += step) {
        const spanX = Math.sqrt(Math.max(0.0, rSq - y * y));
        if (spanX > 1.0) verts.push(-spanX, y, -0.08, spanX, y, -0.08);
      }
      const ringSegs = 72;
      for (let s = 0; s < ringSegs; s++) {
        const a0 = (TWO_PI * s) / ringSegs;
        const a1 = (TWO_PI * (s + 1)) / ringSegs;
        verts.push(
          rBed * Math.cos(a0), rBed * Math.sin(a0), 0.02,
          rBed * Math.cos(a1), rBed * Math.sin(a1), 0.02
        );
      }
      verts.push(-16, -rBed - 4, 0.02, 16, -rBed - 4, 0.02);
    } else {
      for (let x = -Math.floor(hx / step) * step; x <= hx + 0.01; x += step) {
        verts.push(x, -hy, -0.08, x, hy, -0.08);
      }
      for (let y = -Math.floor(hy / step) * step; y <= hy + 0.01; y += step) {
        verts.push(-hx, y, -0.08, hx, y, -0.08);
      }
      verts.push(
        -hx, -hy, 0.02, hx, -hy, 0.02,
        hx, -hy, 0.02, hx, hy, 0.02,
        hx, hy, 0.02, -hx, hy, 0.02,
        -hx, hy, 0.02, -hx, -hy, 0.02
      );
      verts.push(-18, -hy - 4, 0.02, 18, -hy - 4, 0.02);
    }

    const arr = new Float32Array(verts);
    bedVertCount = arr.length / 3;
    gl.bindBuffer(gl.ARRAY_BUFFER, bedBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, arr, gl.STATIC_DRAW);
  }

  function uploadBufferSet(bufSet, positions, normals, overhangs, parts, roles, indices, drawUsage) {
    gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.pos);
    gl.bufferData(gl.ARRAY_BUFFER, positions, drawUsage);

    gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.nrm);
    gl.bufferData(gl.ARRAY_BUFFER, normals, drawUsage);

    gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.ovh);
    gl.bufferData(gl.ARRAY_BUFFER, overhangs, drawUsage);

    gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.part);
    gl.bufferData(gl.ARRAY_BUFFER, parts, drawUsage);

    gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.role);
    gl.bufferData(gl.ARRAY_BUFFER, roles, drawUsage);

    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, bufSet.idx);
    let idxType;
    if (isWebGL2 || positions.length / 3 > 65530) {
      gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, drawUsage);
      idxType = gl.UNSIGNED_INT;
    } else {
      gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), drawUsage);
      idxType = gl.UNSIGNED_SHORT;
    }
    return { count: indices.length, type: idxType };
  }

  function updateSectionCapGPU() {
    if (!gl || !sectionCapBuffers) return;
    const capGeo = buildHorizontalZSliceCap();
    if (!capGeo || capGeo.indices.length === 0) {
      sectionCapIndexCount = 0;
      return;
    }
    const meta = uploadBufferSet(
      sectionCapBuffers,
      capGeo.positions,
      capGeo.normals,
      capGeo.overhangs,
      capGeo.parts,
      capGeo.roles,
      capGeo.indices,
      gl.DYNAMIC_DRAW
    );
    sectionCapIndexCount = meta.count;
    sectionCapIndexType = meta.type;
  }

  function uploadMeshToGPU(geo) {
    if (!gl || !meshBuffers) return;
    const drawUsage = state.isInteracting ? gl.DYNAMIC_DRAW : gl.STATIC_DRAW;

    const mainMeta = uploadBufferSet(
      meshBuffers,
      geo.positions,
      geo.normals,
      geo.overhangs,
      geo.parts,
      geo.roles,
      geo.indices,
      drawUsage
    );
    indexCount = mainMeta.count;
    indexType = mainMeta.type;

    if (geo.spiralCapIndices && geo.spiralCapIndices.length > 0 && spiralCapBuffers) {
      const spMeta = uploadBufferSet(
        spiralCapBuffers,
        geo.spiralCapPositions,
        geo.spiralCapNormals,
        geo.spiralCapOverhangs,
        geo.spiralCapParts,
        geo.spiralCapRoles,
        geo.spiralCapIndices,
        drawUsage
      );
      spiralCapIndexCount = spMeta.count;
      spiralCapIndexType = spMeta.type;
    } else {
      spiralCapIndexCount = 0;
    }

    updateSectionCapGPU();

    gl.bindBuffer(gl.ARRAY_BUFFER, wireBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, geo.wirePositions, drawUsage);
    wireVertCount = geo.wirePositions.length / 3;
  }

  function bindMeshBufferAttribs(bufSet) {
    const locPos = gl.getAttribLocation(meshProg, "a_pos");
    const locNrm = gl.getAttribLocation(meshProg, "a_nrm");
    const locOvh = gl.getAttribLocation(meshProg, "a_ovh");
    const locPart = gl.getAttribLocation(meshProg, "a_part");
    const locRole = gl.getAttribLocation(meshProg, "a_role");

    if (locPos >= 0) {
      gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.pos);
      gl.enableVertexAttribArray(locPos);
      gl.vertexAttribPointer(locPos, 3, gl.FLOAT, false, 0, 0);
    }
    if (locNrm >= 0) {
      gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.nrm);
      gl.enableVertexAttribArray(locNrm);
      gl.vertexAttribPointer(locNrm, 3, gl.FLOAT, false, 0, 0);
    }
    if (locOvh >= 0) {
      gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.ovh);
      gl.enableVertexAttribArray(locOvh);
      gl.vertexAttribPointer(locOvh, 1, gl.FLOAT, false, 0, 0);
    }
    if (locPart >= 0) {
      gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.part);
      gl.enableVertexAttribArray(locPart);
      gl.vertexAttribPointer(locPart, 1, gl.FLOAT, false, 0, 0);
    }
    if (locRole >= 0) {
      gl.bindBuffer(gl.ARRAY_BUFFER, bufSet.role);
      gl.enableVertexAttribArray(locRole);
      gl.vertexAttribPointer(locRole, 1, gl.FLOAT, false, 0, 0);
    }
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, bufSet.idx);
  }

  const MATERIAL_PRESETS = {
    emerald_silk:  { base: [0.02, 0.72, 0.63], saucer: [0.14, 0.24, 0.25], rough: 0.22, metal: 0.30 },
    terracotta:    { base: [0.79, 0.40, 0.28], saucer: [0.68, 0.34, 0.24], rough: 0.78, metal: 0.02 },
    matte_ceramic: { base: [0.91, 0.90, 0.87], saucer: [0.80, 0.78, 0.74], rough: 0.66, metal: 0.02 },
    copper_bronze: { base: [0.76, 0.48, 0.31], saucer: [0.36, 0.25, 0.20], rough: 0.26, metal: 0.72 },
    xray:          { base: [0.04, 0.80, 0.72], saucer: [0.16, 0.48, 0.52], rough: 0.18, metal: 0.15 },
    heatmap:       { base: [0.05, 0.76, 0.45], saucer: [0.05, 0.76, 0.45], rough: 0.55, metal: 0.05 }
  };

  function getActiveClipUniforms() {
    if (state.cutAxis === "z") {
      if (state.zSlicePct >= 100) return { mode: 0.0, val: 0.0 };
      const liftZ = state.lastGeoData ? state.lastGeoData.vaseLiftZ : 0.0;
      const zVal = state.params.height_mm * (state.zSlicePct / 100.0) + liftZ;
      return { mode: 2.0, val: zVal };
    }
    if (state.crossCutPct <= 0) return { mode: 0.0, val: 0.0 };
    const maxRad = Math.max(state.params.belly_diameter_mm, state.params.base_diameter_mm, state.params.neck_diameter_mm) * 0.60 + 18.0;
    const clipY = maxRad * (1.0 - 2.0 * (state.crossCutPct / 100.0));
    return { mode: 1.0, val: clipY };
  }

  function renderWebGLFrame() {
    if (!gl || !meshProg || !lineProg) return;
    const canvas = gl.canvas;
    const cssW = Math.max(1, canvas.clientWidth || 640);
    const cssH = Math.max(1, canvas.clientHeight || 480);
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const w = Math.max(1, Math.floor(cssW * dpr));
    const h = Math.max(1, Math.floor(cssH * dpr));
    if (canvas.width !== w || canvas.height !== h) {
      canvas.width = w;
      canvas.height = h;
    }

    gl.viewport(0, 0, w, h);
    gl.depthMask(true);
    gl.enable(gl.DEPTH_TEST);
    gl.disable(gl.CULL_FACE);
    gl.disable(gl.BLEND);

    if (state.theme === "light") {
      gl.clearColor(0.84, 0.88, 0.92, 1.0);
    } else {
      gl.clearColor(0.095, 0.11, 0.138, 1.0);
    }
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    const cosP = Math.cos(camera.pitch);
    const eye = [
      camera.target[0] + camera.distance * cosP * Math.cos(camera.yaw),
      camera.target[1] + camera.distance * cosP * Math.sin(camera.yaw),
      camera.target[2] + camera.distance * Math.sin(camera.pitch)
    ];

    const proj = mat4Perspective(38.0 * DEG2RAD, w / h, 4.0, 4200.0);
    const view = mat4LookAtZUp(eye, camera.target);
    const mvp = mat4Multiply(proj, view);

    const clipInfo = getActiveClipUniforms();
    state.lastFrameCamera = { mvp: mvp, eye: eye, cssW: cssW, cssH: cssH, clipInfo: clipInfo };

    // 1. Draw Opaque/Alpha Printer Bed Grid First (writes depth before X-Ray pass!)
    if (bedVertCount > 0) {
      gl.useProgram(lineProg);
      gl.uniformMatrix4fv(gl.getUniformLocation(lineProg, "u_mvp"), false, mvp);
      const outOfBounds = !(state.clientMetrics.fitsBed && state.clientMetrics.fitsHeight);
      if (outOfBounds) {
        gl.uniform4f(gl.getUniformLocation(lineProg, "u_color"), 0.98, 0.25, 0.25, 0.85);
      } else if (state.theme === "light") {
        gl.uniform4f(gl.getUniformLocation(lineProg, "u_color"), 0.35, 0.45, 0.52, 0.45);
      } else {
        gl.uniform4f(gl.getUniformLocation(lineProg, "u_color"), 0.0, 0.72, 0.62, 0.34);
      }
      const locLinePos = gl.getAttribLocation(lineProg, "a_pos");
      gl.bindBuffer(gl.ARRAY_BUFFER, bedBuffer);
      gl.enableVertexAttribArray(locLinePos);
      gl.vertexAttribPointer(locLinePos, 3, gl.FLOAT, false, 0, 0);
      gl.drawArrays(gl.LINES, 0, bedVertCount);
    }

    // 2. Draw 3D Vase (+ Saucer) Mesh
    if (indexCount > 0) {
      gl.useProgram(meshProg);
      gl.uniformMatrix4fv(gl.getUniformLocation(meshProg, "u_mvp"), false, mvp);
      gl.uniform3fv(gl.getUniformLocation(meshProg, "u_eye"), eye);

      const matKey = state.xrayMode ? "xray" : state.material;
      const mat = MATERIAL_PRESETS[matKey] || MATERIAL_PRESETS.emerald_silk;
      gl.uniform3fv(gl.getUniformLocation(meshProg, "u_baseColor"), mat.base);
      gl.uniform3fv(gl.getUniformLocation(meshProg, "u_saucerColor"), mat.saucer);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_roughness"), mat.rough);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_metallic"), mat.metal);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_heatmap"), (!state.xrayMode && state.material === "heatmap") ? 1.0 : 0.0);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_xrayMode"), state.xrayMode ? 1.0 : 0.0);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_clipMode"), clipInfo.mode);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_clipVal"), clipInfo.val);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_passMode"), 0.0);
      gl.uniform1f(gl.getUniformLocation(meshProg, "u_lightTheme"), state.theme === "light" ? 1.0 : 0.0);

      bindMeshBufferAttribs(meshBuffers);

      if (state.xrayMode) {
        // Two-pass alpha-blended X-Ray mode (back faces then front faces, depthMask=false)
        gl.enable(gl.BLEND);
        gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
        gl.depthMask(false);
        gl.enable(gl.CULL_FACE);

        gl.cullFace(gl.FRONT);
        gl.drawElements(gl.TRIANGLES, indexCount, indexType, 0);

        gl.cullFace(gl.BACK);
        gl.drawElements(gl.TRIANGLES, indexCount, indexType, 0);

        gl.disable(gl.CULL_FACE);

        if (sectionCapIndexCount > 0 && state.cutAxis === "z" && state.zSlicePct < 100) {
          gl.uniform1f(gl.getUniformLocation(meshProg, "u_passMode"), 1.0);
          bindMeshBufferAttribs(sectionCapBuffers);
          gl.drawElements(gl.TRIANGLES, sectionCapIndexCount, sectionCapIndexType, 0);
        }

        gl.depthMask(true);
        gl.disable(gl.BLEND);
      } else {
        // Standard Opaque Mode
        gl.disable(gl.BLEND);
        gl.depthMask(true);
        gl.disable(gl.CULL_FACE);
        gl.drawElements(gl.TRIANGLES, indexCount, indexType, 0);

        // Solid CAD Hatched Horizontal Z-Slice Cap Ring
        if (sectionCapIndexCount > 0 && state.cutAxis === "z" && state.zSlicePct < 100) {
          gl.uniform1f(gl.getUniformLocation(meshProg, "u_passMode"), 1.0);
          bindMeshBufferAttribs(sectionCapBuffers);
          gl.drawElements(gl.TRIANGLES, sectionCapIndexCount, sectionCapIndexType, 0);
        }

        // Honest Spiral Mode Semi-Transparent Holographic Top-Cap Disk Indicator
        if (
          state.params.print_mode === "spiral_vase" &&
          spiralCapIndexCount > 0 &&
          !(state.cutAxis === "z" && state.zSlicePct < 100)
        ) {
          gl.enable(gl.BLEND);
          gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
          gl.depthMask(false);
          gl.uniform1f(gl.getUniformLocation(meshProg, "u_passMode"), 2.0);
          bindMeshBufferAttribs(spiralCapBuffers);
          gl.drawElements(gl.TRIANGLES, spiralCapIndexCount, spiralCapIndexType, 0);
          gl.depthMask(true);
          gl.disable(gl.BLEND);
        }
      }
    }

    // 3. Optional Wireframe Overlay
    if (state.wireframe && wireVertCount > 0 && !isSectionCutActive()) {
      gl.useProgram(lineProg);
      gl.uniformMatrix4fv(gl.getUniformLocation(lineProg, "u_mvp"), false, mvp);
      gl.enable(gl.BLEND);
      gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
      gl.uniform4f(
        gl.getUniformLocation(lineProg, "u_color"),
        state.xrayMode ? 0.35 : 0.0,
        state.xrayMode ? 0.98 : 0.0,
        state.xrayMode ? 0.90 : 0.0,
        state.xrayMode ? 0.22 : 0.32
      );
      const locLinePos = gl.getAttribLocation(lineProg, "a_pos");
      gl.bindBuffer(gl.ARRAY_BUFFER, wireBuffer);
      gl.enableVertexAttribArray(locLinePos);
      gl.vertexAttribPointer(locLinePos, 3, gl.FLOAT, false, 0, 0);
      gl.drawArrays(gl.LINES, 0, wireVertCount);
      gl.disable(gl.BLEND);
    }

    // 4. Live 3D -> 2D CAD Caliper Overlay (#vp-caliper-canvas)
    renderCaliperOverlay();
  }

  // ==========================================================================
  // 7B. Live 3D -> 2D CAD Caliper `mm` Overlay (`#vp-caliper-canvas`)
  // ==========================================================================
  function projectWorldToScreen(wx, wy, wz, mvp, cssW, cssH) {
    const cx = mvp[0] * wx + mvp[4] * wy + mvp[8]  * wz + mvp[12];
    const cy = mvp[1] * wx + mvp[5] * wy + mvp[9]  * wz + mvp[13];
    const cz = mvp[2] * wx + mvp[6] * wy + mvp[10] * wz + mvp[14];
    const cw = mvp[3] * wx + mvp[7] * wy + mvp[11] * wz + mvp[15];
    if (cw <= 0.1) return null;
    const ndcX = cx / cw;
    const ndcY = cy / cw;
    return {
      x: (ndcX * 0.5 + 0.5) * cssW,
      y: (0.5 - ndcY * 0.5) * cssH,
      ndcZ: cz / cw
    };
  }

  function drawCadArrowHead(ctx, tipX, tipY, dirX, dirY, len) {
    const nx = -dirY;
    const ny = dirX;
    const w = len * 0.44;
    ctx.beginPath();
    ctx.moveTo(tipX, tipY);
    ctx.lineTo(tipX - dirX * len + nx * w, tipY - dirY * len + ny * w);
    ctx.lineTo(tipX - dirX * len - nx * w, tipY - dirY * len - ny * w);
    ctx.closePath();
    ctx.fill();
  }

  function drawCadDoubleArrow(ctx, x1, y1, x2, y2, color, dashed) {
    const dx = x2 - x1;
    const dy = y2 - y1;
    const dist = Math.hypot(dx, dy);
    if (dist < 4.0) return;
    const ux = dx / dist;
    const uy = dy / dist;
    const arrowLen = Math.min(7.5, dist * 0.28);

    ctx.save();
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = 1.65;
    if (dashed) ctx.setLineDash([4, 3]);
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.setLineDash([]);
    drawCadArrowHead(ctx, x1, y1, -ux, -uy, arrowLen);
    drawCadArrowHead(ctx, x2, y2, ux, uy, arrowLen);
    ctx.restore();
  }

  function drawCadPill(ctx, cx, cy, text, borderColor, cssW, cssH, placedBoxes) {
    ctx.save();
    ctx.font = "700 10.8px 'Cascadia Code', Consolas, 'Segoe UI', monospace";
    const padX = 7;
    const boxH = 20;
    const tw = ctx.measureText(text).width;
    const boxW = tw + padX * 2;

    let x = Math.max(10, Math.min(cssW - boxW - 10, cx - boxW * 0.5));
    let y = Math.max(44, Math.min(cssH - boxH - 46, cy - boxH * 0.5));

    // Gentle vertical collision avoidance so pills never overlap each other
    if (Array.isArray(placedBoxes)) {
      for (let pass = 0; pass < 4; pass++) {
        let hit = false;
        for (let k = 0; k < placedBoxes.length; k++) {
          const b = placedBoxes[k];
          const overlapX = x < b.x + b.w + 4 && x + boxW + 4 > b.x;
          const overlapY = y < b.y + b.h + 3 && y + boxH + 3 > b.y;
          if (overlapX && overlapY) {
            y = (y >= b.y) ? Math.min(cssH - boxH - 46, b.y + b.h + 4) : Math.max(44, b.y - boxH - 4);
            hit = true;
          }
        }
        if (!hit) break;
      }
      placedBoxes.push({ x: x, y: y, w: boxW, h: boxH });
    }

    const r = 5;
    ctx.beginPath();
    if (typeof ctx.roundRect === "function") {
      ctx.roundRect(x, y, boxW, boxH, r);
    } else {
      ctx.rect(x, y, boxW, boxH);
    }
    ctx.fillStyle = state.theme === "light" ? "rgba(250, 252, 255, 0.94)" : "rgba(15, 18, 24, 0.90)";
    ctx.fill();
    ctx.lineWidth = 1.4;
    ctx.strokeStyle = borderColor;
    ctx.stroke();

    ctx.fillStyle = state.theme === "light" ? "#141a22" : "#f3f7fb";
    ctx.textBaseline = "middle";
    ctx.fillText(text, x + padX, y + boxH * 0.5 + 0.5);
    ctx.restore();
    return { cx: x + boxW * 0.5, cy: y + boxH * 0.5 };
  }

  function renderCaliperOverlay() {
    const calCanvas = document.getElementById("vp-caliper-canvas");
    if (!calCanvas || !calCanvas.getContext) return;
    const ctx = calCanvas.getContext("2d");
    if (!ctx) return;

    const camFrame = state.lastFrameCamera;
    const cssW = camFrame ? camFrame.cssW : (calCanvas.clientWidth || 640);
    const cssH = camFrame ? camFrame.cssH : (calCanvas.clientHeight || 480);
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const pw = Math.max(1, Math.floor(cssW * dpr));
    const ph = Math.max(1, Math.floor(cssH * dpr));
    if (calCanvas.width !== pw || calCanvas.height !== ph) {
      calCanvas.width = pw;
      calCanvas.height = ph;
    }

    ctx.save();
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, cssW, cssH);

    if (!isCalipersActive() || !state.lastGeoData || !camFrame) {
      ctx.restore();
      return;
    }

    const gd = state.lastGeoData;
    const mvp = camFrame.mvp;
    const nt = gd.thVals.length;
    const placedBoxes = [];

    const isZSlice = state.cutAxis === "z" && state.zSlicePct < 100;
    const zInspect = isZSlice ? (gd.heightMm * (state.zSlicePct / 100.0)) : gd.heightMm;
    const sl = sampleGeoAtHeight(zInspect);
    if (!sl) {
      ctx.restore();
      return;
    }

    // Choose measurement axis perpendicular to camera view ray (or on cut plane when Vertical Y cut is active!)
    let measureAng = camera.yaw + Math.PI * 0.5;
    if (state.cutAxis === "y" && state.crossCutPct > 0) {
      measureAng = 0.0; // X-axis lies right along the Y cross-section plane!
    }
    const angRight = posMod(measureAng, TWO_PI);
    const angLeft = posMod(measureAng + Math.PI, TWO_PI);
    const jRight = Math.round((angRight / TWO_PI) * nt) % nt;
    const jLeft = Math.round((angLeft / TWO_PI) * nt) % nt;

    let yPlaneShift = 0.0;
    if (state.cutAxis === "y" && state.crossCutPct > 0 && camFrame.clipInfo && camFrame.clipInfo.mode === 1.0) {
      yPlaneShift = Math.max(0.0, Math.min(sl.rOut[jRight] * 0.65, camFrame.clipInfo.val));
    }

    const pOutL = projectWorldToScreen(
      sl.rOut[jLeft] * Math.cos(angLeft) + gd.vaseOffsetX,
      sl.rOut[jLeft] * Math.sin(angLeft) + yPlaneShift,
      sl.zWorld, mvp, cssW, cssH
    );
    const pOutR = projectWorldToScreen(
      sl.rOut[jRight] * Math.cos(angRight) + gd.vaseOffsetX,
      sl.rOut[jRight] * Math.sin(angRight) + yPlaneShift,
      sl.zWorld, mvp, cssW, cssH
    );

    const colExt = state.theme === "light" ? "#00796b" : "#1de9b6";
    const colHole = state.theme === "light" ? "#d96b00" : "#ffab40";
    const colWall = state.theme === "light" ? "#00838f" : "#64ffda";
    const colFloor = state.theme === "light" ? "#c63f17" : "#ff7043";

    // Optional Z-Slice header pill when inspecting horizontal tomography slice
    if (isZSlice) {
      const zTxt = tr("cal_z_slice")
        .replace("{z}", zInspect.toFixed(1))
        .replace("{pct}", String(state.zSlicePct));
      drawCadPill(ctx, cssW * 0.5, 56, zTxt, colExt, cssW, cssH, placedBoxes);
    }

    // 1. Outer Diameter Caliper (extension lines above mouth / active Z slice)
    if (pOutL && pOutR) {
      const liftPx = 28;
      const yExtL = pOutL.y - liftPx;
      const yExtR = pOutR.y - liftPx;
      ctx.save();
      ctx.strokeStyle = colExt;
      ctx.globalAlpha = 0.65;
      ctx.lineWidth = 1.2;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(pOutL.x, pOutL.y); ctx.lineTo(pOutL.x, yExtL - 4);
      ctx.moveTo(pOutR.x, pOutR.y); ctx.lineTo(pOutR.x, yExtR - 4);
      ctx.stroke();
      ctx.restore();

      drawCadDoubleArrow(ctx, pOutL.x, yExtL, pOutR.x, yExtR, colExt, false);
      const extLabel = tr("cal_ext").replace("{v}", sl.dOutMean.toFixed(1));
      drawCadPill(ctx, 0.5 * (pOutL.x + pOutR.x), 0.5 * (yExtL + yExtR) - 13, extLabel, colExt, cssW, cssH, placedBoxes);
    }

    // 2. Inner Bore / Hole Diameter Caliper & 3. Wall Thickness Caliper
    if (!sl.inSolidFloor) {
      const pInL = projectWorldToScreen(
        sl.rIn[jLeft] * Math.cos(angLeft) + gd.vaseOffsetX,
        sl.rIn[jLeft] * Math.sin(angLeft) + yPlaneShift,
        sl.zWorld, mvp, cssW, cssH
      );
      const pInR = projectWorldToScreen(
        sl.rIn[jRight] * Math.cos(angRight) + gd.vaseOffsetX,
        sl.rIn[jRight] * Math.sin(angRight) + yPlaneShift,
        sl.zWorld, mvp, cssW, cssH
      );

      if (pInL && pInR) {
        drawCadDoubleArrow(ctx, pInL.x, pInL.y, pInR.x, pInR.y, colHole, true);
        const holeLabel = tr("cal_hole").replace("{v}", sl.dInMean.toFixed(1));
        drawCadPill(ctx, 0.5 * (pInL.x + pInR.x), 0.5 * (pInL.y + pInR.y) + 14, holeLabel, colHole, cssW, cssH, placedBoxes);
      }

      if (pInR && pOutR) {
        ctx.save();
        ctx.strokeStyle = colWall;
        ctx.fillStyle = colWall;
        ctx.lineWidth = 2.4;
        ctx.beginPath();
        ctx.moveTo(pInR.x, pInR.y);
        ctx.lineTo(pOutR.x, pOutR.y);
        ctx.stroke();

        // Crisp perpendicular end ticks on inner & outer wall surfaces
        ctx.lineWidth = 1.6;
        ctx.beginPath();
        ctx.moveTo(pInR.x, pInR.y - 6); ctx.lineTo(pInR.x, pInR.y + 6);
        ctx.moveTo(pOutR.x, pOutR.y - 6); ctx.lineTo(pOutR.x, pOutR.y + 6);
        ctx.stroke();

        const leadX = pOutR.x + 26;
        const leadY = pOutR.y + 18;
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.moveTo(0.5 * (pInR.x + pOutR.x), 0.5 * (pInR.y + pOutR.y));
        ctx.lineTo(leadX, leadY);
        ctx.stroke();
        ctx.restore();

        const cm = state.clientMetrics;
        const wMinDisp = isZSlice ? sl.wMin : cm.wallMinMm;
        const wMaxDisp = isZSlice ? sl.wMax : cm.wallMaxMm;
        const nomW = gd.visWallMm;
        let wallLabel;
        if ((gd.hasActiveTexture || (wMaxDisp - wMinDisp) >= 0.22) && Math.abs(wMaxDisp - wMinDisp) >= 0.08) {
          wallLabel = tr("cal_wall_range")
            .replace("{v}", nomW.toFixed(1))
            .replace("{min}", wMinDisp.toFixed(1))
            .replace("{max}", wMaxDisp.toFixed(1));
        } else {
          wallLabel = tr("cal_wall").replace("{v}", nomW.toFixed(1));
        }
        drawCadPill(ctx, leadX + 54, leadY + 4, wallLabel, colWall, cssW, cssH, placedBoxes);
      }
    }

    // 4. Bottom Floor Thickness Caliper (Z = 0 .. floorZ)
    const rBaseL = gd.radii[0][jLeft] * 0.55;
    const pFlrBot = projectWorldToScreen(
      rBaseL * Math.cos(angLeft) + gd.vaseOffsetX,
      rBaseL * Math.sin(angLeft) + yPlaneShift,
      gd.vaseLiftZ, mvp, cssW, cssH
    );
    const pFlrTop = projectWorldToScreen(
      rBaseL * Math.cos(angLeft) + gd.vaseOffsetX,
      rBaseL * Math.sin(angLeft) + yPlaneShift,
      gd.floorZ + gd.vaseLiftZ, mvp, cssW, cssH
    );

    if (pFlrBot && pFlrTop) {
      ctx.save();
      ctx.strokeStyle = colFloor;
      ctx.lineWidth = 2.4;
      ctx.beginPath();
      ctx.moveTo(pFlrBot.x, pFlrBot.y);
      ctx.lineTo(pFlrTop.x, pFlrTop.y);
      ctx.stroke();

      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(pFlrBot.x - 6, pFlrBot.y); ctx.lineTo(pFlrBot.x + 6, pFlrBot.y);
      ctx.moveTo(pFlrTop.x - 6, pFlrTop.y); ctx.lineTo(pFlrTop.x + 6, pFlrTop.y);
      ctx.stroke();

      const flLeadX = pFlrBot.x - 28;
      const flLeadY = 0.5 * (pFlrBot.y + pFlrTop.y) - 6;
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(0.5 * (pFlrBot.x + pFlrTop.x), 0.5 * (pFlrBot.y + pFlrTop.y));
      ctx.lineTo(flLeadX, flLeadY);
      ctx.stroke();
      ctx.restore();

      const floorLabel = tr("cal_floor").replace("{v}", gd.floorZ.toFixed(1));
      drawCadPill(ctx, flLeadX - 42, flLeadY, floorLabel, colFloor, cssW, cssH, placedBoxes);
    }

    ctx.restore();
  }

  let rafPending = false;
  function requestRender() {
    if (rafPending) return;
    rafPending = true;
    requestAnimationFrame(function () {
      rafPending = false;
      if (state.autoSpin) {
        camera.yaw += 0.008;
        requestRender();
      }
      renderWebGLFrame();
    });
  }

  function fitCameraToVase() {
    const h = state.params.height_mm;
    const maxD = Math.max(state.params.base_diameter_mm, state.params.belly_diameter_mm, state.params.neck_diameter_mm);
    camera.target = [0.0, 0.0, h * 0.46];
    camera.distance = Math.max(170.0, Math.max(h * 1.65, maxD * 2.25));
    requestRender();
  }

  function bindViewportEvents(canvas) {
    let dragging = false;
    let panMode = false;
    let lastX = 0;
    let lastY = 0;

    canvas.addEventListener("contextmenu", function (e) { e.preventDefault(); });

    canvas.addEventListener("pointerdown", function (e) {
      dragging = true;
      panMode = (e.button === 1 || e.button === 2 || e.shiftKey);
      lastX = e.clientX;
      lastY = e.clientY;
      canvas.setPointerCapture?.(e.pointerId);
    });

    canvas.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      const dx = e.clientX - lastX;
      const dy = e.clientY - lastY;
      lastX = e.clientX;
      lastY = e.clientY;

      if (panMode) {
        const panScale = camera.distance * 0.0014;
        const rightX = -Math.sin(camera.yaw);
        const rightY = Math.cos(camera.yaw);
        camera.target[0] -= dx * rightX * panScale;
        camera.target[1] -= dx * rightY * panScale;
        camera.target[2] += dy * panScale;
      } else {
        camera.yaw -= dx * 0.0085;
        camera.pitch = Math.max(-1.48, Math.min(1.48, camera.pitch + dy * 0.0075));
      }
      requestRender();
    });

    const endDrag = function (e) {
      dragging = false;
      canvas.releasePointerCapture?.(e.pointerId);
    };
    canvas.addEventListener("pointerup", endDrag);
    canvas.addEventListener("pointercancel", endDrag);

    canvas.addEventListener("wheel", function (e) {
      e.preventDefault();
      const factor = Math.exp(e.deltaY * 0.0011);
      camera.distance = Math.max(55.0, Math.min(1850.0, camera.distance * factor));
      requestRender();
    }, { passive: false });

    canvas.addEventListener("dblclick", fitCameraToVase);

    if (typeof ResizeObserver !== "undefined") {
      const ro = new ResizeObserver(function () {
        requestRender();
        draw2DCurveEditor();
      });
      ro.observe(canvas);
    }
  }

  // ==========================================================================
  // 8. Interactive 2D Silhouette Curve Editor (`#curve-canvas`)
  // ==========================================================================
  let activeKnotIdx = -1;
  let hoverKnotIdx = -1;

  function get2DCurveMapping(canvas) {
    const w = canvas.clientWidth || 300;
    const h = canvas.clientHeight || 220;
    const padL = 32, padR = 14, padT = 14, padB = 22;
    const plotW = Math.max(40, w - padL - padR);
    const plotH = Math.max(40, h - padT - padB);
    const centerX = padL + plotW * 0.5;
    const lim = getDynamicPrinterLimits();
    const bedHalf = 0.5 * lim.minBedXY;
    const maxR = Math.max(
      95.0,
      bedHalf * 1.06,
      state.params.belly_diameter_mm * 0.62,
      state.params.base_diameter_mm * 0.62,
      state.params.neck_diameter_mm * 0.62,
      115.0
    );
    const halfW = plotW * 0.46;

    return {
      w: w,
      h: h,
      padL: padL,
      padR: padR,
      padT: padT,
      padB: padB,
      plotW: plotW,
      plotH: plotH,
      centerX: centerX,
      maxR: maxR,
      rToXRight: function (r) { return centerX + (r / maxR) * halfW; },
      rToXLeft: function (r) { return centerX - (r / maxR) * halfW; },
      zNormToY: function (zn) { return padT + (1.0 - zn) * plotH; },
      xToR: function (x) { return Math.max(8.0, Math.min(lim.maxCurveR, ((x - centerX) / halfW) * maxR)); },
      yToZNorm: function (y) { return Math.max(0.0, Math.min(1.0, 1.0 - (y - padT) / plotH)); }
    };
  }

  function getInteractiveHandles() {
    const p = state.params;
    if (p.use_custom_profile) {
      return p.profile_points.map(function (pt, idx) {
        return { idx: idx, zNorm: pt[0], r: pt[1], kind: "custom" };
      });
    }
    const rNeck = 0.5 * p.neck_diameter_mm;
    return [
      { idx: 0, zNorm: 0.0, r: 0.5 * p.base_diameter_mm, kind: "base" },
      { idx: 1, zNorm: p.belly_height_ratio, r: 0.5 * p.belly_diameter_mm, kind: "belly" },
      { idx: 2, zNorm: p.waist_height_ratio, r: 0.5 * p.waist_diameter_mm, kind: "waist" },
      { idx: 3, zNorm: 0.92, r: rNeck, kind: "neck" },
      { idx: 4, zNorm: 1.0, r: Math.max(4.0, rNeck + p.lip_flare_mm), kind: "lip" }
    ];
  }

  function draw2DMiniBadge(ctx, cx, cy, text, borderCol, isLight) {
    ctx.save();
    ctx.font = "600 9.4px 'Cascadia Code', Consolas, 'Segoe UI', sans-serif";
    const tw = ctx.measureText(text).width;
    const bw = tw + 10;
    const bh = 15;
    const bx = cx - bw * 0.5;
    const by = cy - bh * 0.5;
    ctx.beginPath();
    if (typeof ctx.roundRect === "function") {
      ctx.roundRect(bx, by, bw, bh, 4);
    } else {
      ctx.rect(bx, by, bw, bh);
    }
    ctx.fillStyle = isLight ? "rgba(255, 255, 255, 0.92)" : "rgba(18, 21, 27, 0.88)";
    ctx.fill();
    ctx.lineWidth = 1.1;
    ctx.strokeStyle = borderCol;
    ctx.stroke();
    ctx.fillStyle = isLight ? "#1a222c" : "#eef4fa";
    ctx.textBaseline = "middle";
    ctx.fillText(text, bx + 5, cy + 0.5);
    ctx.restore();
  }

  function draw2DCurveEditor() {
    const canvas = document.getElementById("curve-canvas");
    if (!canvas || !canvas.getContext) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const map = get2DCurveMapping(canvas);
    const cw = Math.max(1, Math.floor(map.w * dpr));
    const ch = Math.max(1, Math.floor(map.h * dpr));
    if (canvas.width !== cw || canvas.height !== ch) {
      canvas.width = cw;
      canvas.height = ch;
    }

    ctx.save();
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, map.w, map.h);

    const isLight = state.theme === "light";
    const gridCol = isLight ? "rgba(80, 100, 120, 0.16)" : "rgba(255, 255, 255, 0.07)";
    const axisCol = isLight ? "rgba(0, 137, 123, 0.45)" : "rgba(0, 191, 165, 0.40)";
    const strokeCol = isLight ? "#00897b" : "#00bfa5";
    const innerStrokeCol = isLight ? "#c65314" : "#ff9e40";
    const cavityFillCol = isLight ? "rgba(0, 137, 123, 0.06)" : "rgba(0, 191, 165, 0.06)";
    const wallFillCol = isLight ? "rgba(0, 137, 123, 0.28)" : "rgba(0, 191, 165, 0.30)";
    const floorFillCol = isLight ? "rgba(217, 107, 0, 0.25)" : "rgba(255, 140, 56, 0.28)";
    const txtCol = isLight ? "#5a6677" : "#8691a2";

    // Grid lines
    ctx.strokeStyle = gridCol;
    ctx.lineWidth = 1;
    for (let i = 0; i <= 4; i++) {
      const y = map.padT + (i / 4) * map.plotH;
      ctx.beginPath();
      ctx.moveTo(map.padL, y);
      ctx.lineTo(map.w - map.padR, y);
      ctx.stroke();

      const zMm = Math.round(state.params.height_mm * (1 - i / 4));
      ctx.fillStyle = txtCol;
      ctx.font = "9.5px Segoe UI, sans-serif";
      ctx.fillText(String(zMm), 4, y + 3);
    }

    // Center symmetry axis
    ctx.save();
    ctx.strokeStyle = axisCol;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(map.centerX, map.padT);
    ctx.lineTo(map.centerX, map.h - map.padB);
    ctx.stroke();
    ctx.restore();

    // Max bed radius guide line
    const bedHalf = 0.5 * Math.min(state.printer.bed_x || 220, state.printer.bed_y || 220);
    if (bedHalf <= map.maxR) {
      const bxRight = map.rToXRight(bedHalf);
      ctx.save();
      ctx.strokeStyle = "rgba(255, 179, 0, 0.38)";
      ctx.setLineDash([2, 3]);
      ctx.beginPath();
      ctx.moveTo(bxRight, map.padT);
      ctx.lineTo(bxRight, map.h - map.padB);
      ctx.stroke();
      ctx.restore();
    }

    // Evaluate PCHIP silhouette & exact physical wall/floor band (ALWAYS shown!)
    const p = state.params;
    const isHollow = p.print_mode === "shelled_hollow";
    const layerH = Math.max(0.08, Number(state.printer.layer_height_mm) || 0.2);
    const visWall = isHollow ? p.wall_thickness_mm : p.spiral_line_width_mm;
    const floorMm = isHollow
      ? Math.max(1.0, Math.min(p.height_mm * 0.65, p.bottom_thickness_mm))
      : Math.max(0.45, Math.min(p.height_mm * 0.34, p.spiral_bottom_layers * layerH + 0.30));
    const floorZn = Math.min(0.68, floorMm / Math.max(1.0, p.height_mm));
    const minBore = isHollow ? 3.0 : 2.5;
    const minSkin = isHollow ? 0.55 : 0.40;

    const knots = prepareSilhouetteKnots(p);
    const spline = buildPchipSpline(knots.xs, knots.ys);
    const samples = 80;

    const evalInnerR = function (zn) {
      const rO = evalPchipScalar(spline, zn);
      const eps = 0.008;
      const z0 = Math.max(0.0, zn - eps);
      const z1 = Math.min(1.0, zn + eps);
      const dr = evalPchipScalar(spline, z1) - evalPchipScalar(spline, z0);
      const dz = Math.max(1e-4, (z1 - z0) * p.height_mm);
      const slp = Math.max(-3.0, Math.min(3.0, dr / dz));
      return Math.max(minBore, Math.min(rO - minSkin, rO - visWall * Math.sqrt(1.0 + slp * slp)));
    };

    // 1. Subtle recessed interior cavity fill
    ctx.beginPath();
    for (let i = 0; i <= samples; i++) {
      const zn = floorZn + (1.0 - floorZn) * (i / samples);
      const rIn = evalInnerR(zn);
      const x = map.rToXRight(rIn);
      const y = map.zNormToY(zn);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    for (let i = samples; i >= 0; i--) {
      const zn = floorZn + (1.0 - floorZn) * (i / samples);
      const rIn = evalInnerR(zn);
      ctx.lineTo(map.rToXLeft(rIn), map.zNormToY(zn));
    }
    ctx.closePath();
    ctx.fillStyle = cavityFillCol;
    ctx.fill();

    // 2. Shaded + 45-degree Hatched Solid Wall Band & Floor Slab
    ctx.save();
    ctx.beginPath();
    // Right outer contour bottom -> top
    for (let i = 0; i <= samples; i++) {
      const zn = i / samples;
      const r = evalPchipScalar(spline, zn);
      const x = map.rToXRight(r);
      const y = map.zNormToY(zn);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    // Right inner contour top -> floorZn
    for (let i = samples; i >= 0; i--) {
      const zn = floorZn + (1.0 - floorZn) * (i / samples);
      ctx.lineTo(map.rToXRight(evalInnerR(zn)), map.zNormToY(zn));
    }
    // Across inner floor right -> left, then left inner contour floorZn -> top
    for (let i = 0; i <= samples; i++) {
      const zn = floorZn + (1.0 - floorZn) * (i / samples);
      ctx.lineTo(map.rToXLeft(evalInnerR(zn)), map.zNormToY(zn));
    }
    // Left outer contour top -> bottom
    for (let i = samples; i >= 0; i--) {
      const zn = i / samples;
      ctx.lineTo(map.rToXLeft(evalPchipScalar(spline, zn)), map.zNormToY(zn));
    }
    ctx.closePath();
    ctx.fillStyle = wallFillCol;
    ctx.fill();

    // Clip to solid wall + floor polygon to render CAD hatch lines + warm floor slab tint
    ctx.clip();
    const yFloorPx = map.zNormToY(floorZn);
    const yBotPx = map.zNormToY(0.0);
    ctx.fillStyle = floorFillCol;
    ctx.fillRect(map.padL, yFloorPx, map.plotW, Math.max(2.0, yBotPx - yFloorPx));

    ctx.strokeStyle = isLight ? "rgba(0, 110, 98, 0.36)" : "rgba(120, 255, 232, 0.30)";
    ctx.lineWidth = 1.0;
    ctx.beginPath();
    for (let d = -map.h; d < map.w + map.h; d += 7) {
      ctx.moveTo(map.padL + d, map.padT);
      ctx.lineTo(map.padL + d - map.plotH, map.padT + map.plotH);
    }
    ctx.stroke();
    ctx.restore();

    // 3. Outer Silhouette Stroke
    ctx.beginPath();
    for (let i = 0; i <= samples; i++) {
      const zn = i / samples;
      const r = evalPchipScalar(spline, zn);
      const x = map.rToXRight(r);
      const y = map.zNormToY(zn);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.moveTo(map.rToXLeft(evalPchipScalar(spline, 0.0)), map.zNormToY(0.0));
    for (let i = 1; i <= samples; i++) {
      const zn = i / samples;
      ctx.lineTo(map.rToXLeft(evalPchipScalar(spline, zn)), map.zNormToY(zn));
    }
    ctx.moveTo(map.rToXLeft(evalPchipScalar(spline, 0.0)), map.zNormToY(0.0));
    ctx.lineTo(map.rToXRight(evalPchipScalar(spline, 0.0)), map.zNormToY(0.0));
    ctx.strokeStyle = strokeCol;
    ctx.lineWidth = 2.0;
    ctx.stroke();

    // 4. Inner Cavity & Floor Top Contour Stroke
    ctx.save();
    ctx.strokeStyle = innerStrokeCol;
    ctx.lineWidth = 1.35;
    ctx.beginPath();
    for (let i = samples; i >= 0; i--) {
      const zn = floorZn + (1.0 - floorZn) * (i / samples);
      const x = map.rToXRight(evalInnerR(zn));
      const y = map.zNormToY(zn);
      if (i === samples) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    for (let i = 0; i <= samples; i++) {
      const zn = floorZn + (1.0 - floorZn) * (i / samples);
      ctx.lineTo(map.rToXLeft(evalInnerR(zn)), map.zNormToY(zn));
    }
    ctx.stroke();
    ctx.restore();

    // Honest Spiral Mode dashed top-cap line on 2D silhouette
    if (!isHollow) {
      const rTopIn = evalInnerR(1.0);
      const yTop = map.zNormToY(1.0);
      ctx.save();
      ctx.strokeStyle = "#ffb300";
      ctx.lineWidth = 1.6;
      ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ctx.moveTo(map.rToXLeft(rTopIn), yTop);
      ctx.lineTo(map.rToXRight(rTopIn), yTop);
      ctx.stroke();
      ctx.restore();
    }

    // Active Horizontal Z-Slice indicator line on 2D curve
    if (state.cutAxis === "z" && state.zSlicePct < 100) {
      const ySlice = map.zNormToY(state.zSlicePct / 100.0);
      ctx.save();
      ctx.strokeStyle = "#ffca28";
      ctx.lineWidth = 1.4;
      ctx.setLineDash([5, 3]);
      ctx.beginPath();
      ctx.moveTo(map.padL + 2, ySlice);
      ctx.lineTo(map.w - map.padR - 2, ySlice);
      ctx.stroke();
      ctx.restore();
    }

    // 5. Crisp `mm` Callouts: Ø Furo, Parede, Fundo
    const rTopIn = evalInnerR(1.0);
    const yMouthCall = map.zNormToY(0.93);
    const xInL = map.rToXLeft(rTopIn);
    const xInR = map.rToXRight(rTopIn);
    if (xInR - xInL > 18) {
      ctx.save();
      ctx.strokeStyle = innerStrokeCol;
      ctx.lineWidth = 1.2;
      ctx.setLineDash([2, 2]);
      ctx.beginPath();
      ctx.moveTo(xInL, yMouthCall);
      ctx.lineTo(xInR, yMouthCall);
      ctx.stroke();
      ctx.restore();
    }
    const holeDiamMm = (state.clientMetrics && state.clientMetrics.mouthInnerDiam)
      ? state.clientMetrics.mouthInnerDiam
      : (2.0 * rTopIn);
    draw2DMiniBadge(
      ctx,
      map.centerX,
      Math.max(map.padT + 10, yMouthCall),
      tr("lbl_2d_hole").replace("{v}", holeDiamMm.toFixed(1)),
      innerStrokeCol,
      isLight
    );

    // Wall thickness callout on left side (zn = 0.50) so right-side handles stay clear
    const znMid = Math.max(floorZn + 0.12, 0.50);
    const xWallOutL = map.rToXLeft(evalPchipScalar(spline, znMid));
    const xWallInL = map.rToXLeft(evalInnerR(znMid));
    const yWallMid = map.zNormToY(znMid);
    ctx.save();
    ctx.strokeStyle = strokeCol;
    ctx.lineWidth = 2.0;
    ctx.beginPath();
    ctx.moveTo(xWallOutL, yWallMid);
    ctx.lineTo(xWallInL, yWallMid);
    ctx.stroke();
    ctx.restore();
    draw2DMiniBadge(
      ctx,
      Math.max(map.padL + 44, 0.5 * (xWallOutL + xWallInL)),
      yWallMid - 13,
      tr("lbl_2d_wall").replace("{v}", visWall.toFixed(isHollow ? 1 : 2)),
      strokeCol,
      isLight
    );

    // Floor slab callout near bottom center
    const yFlrTop = map.zNormToY(floorZn);
    const yFlrBot = map.zNormToY(0.0);
    draw2DMiniBadge(
      ctx,
      map.centerX,
      Math.min(map.h - 10, 0.5 * (yFlrTop + yFlrBot) - 7),
      tr("lbl_2d_floor").replace("{v}", floorMm.toFixed(1)),
      innerStrokeCol,
      isLight
    );

    // 6. Draw draggable handles on right-hand contour
    const handles = getInteractiveHandles();
    for (let i = 0; i < handles.length; i++) {
      const hdl = handles[i];
      const hx = map.rToXRight(hdl.r);
      const hy = map.zNormToY(hdl.zNorm);
      const isAct = (i === activeKnotIdx || i === hoverKnotIdx);

      ctx.beginPath();
      ctx.arc(hx, hy, isAct ? 6.2 : 4.8, 0, TWO_PI);
      ctx.fillStyle = isAct ? "#ffb300" : strokeCol;
      ctx.fill();
      ctx.lineWidth = 1.8;
      ctx.strokeStyle = "#ffffff";
      ctx.stroke();
    }

    ctx.restore();
  }

  function bind2DCurveEditor() {
    const canvas = document.getElementById("curve-canvas");
    if (!canvas) return;
    const readout = document.getElementById("curve-coord-readout");

    const eventCoords = function (e) {
      const rect = canvas.getBoundingClientRect();
      return { x: e.clientX - rect.left, y: e.clientY - rect.top };
    };

    const hitTestHandle = function (x, y) {
      const map = get2DCurveMapping(canvas);
      const handles = getInteractiveHandles();
      let best = -1;
      let bestDist = 13.0;
      for (let i = 0; i < handles.length; i++) {
        const hx = map.rToXRight(handles[i].r);
        const hy = map.zNormToY(handles[i].zNorm);
        const d = Math.hypot(x - hx, y - hy);
        if (d < bestDist) {
          bestDist = d;
          best = i;
        }
      }
      return best;
    };

    canvas.addEventListener("contextmenu", function (e) {
      e.preventDefault();
      if (!state.params.use_custom_profile) return;
      const pt = eventCoords(e);
      const idx = hitTestHandle(pt.x, pt.y);
      if (idx > 0 && idx < state.params.profile_points.length - 1 && state.params.profile_points.length > 2) {
        pushUndoSnapshot(state.params);
        state.params.profile_points.splice(idx, 1);
        state.params = normalizeParams(state.params);
        activeKnotIdx = -1;
        hoverKnotIdx = -1;
        rebuildScene(false);
        scheduleHostAnalyze();
      }
    });

    canvas.addEventListener("dblclick", function (e) {
      if (!state.params.use_custom_profile) return;
      const pt = eventCoords(e);
      const idx = hitTestHandle(pt.x, pt.y);
      if (idx > 0 && idx < state.params.profile_points.length - 1 && state.params.profile_points.length > 2) {
        pushUndoSnapshot(state.params);
        state.params.profile_points.splice(idx, 1);
        state.params = normalizeParams(state.params);
        activeKnotIdx = -1;
        hoverKnotIdx = -1;
        rebuildScene(false);
        scheduleHostAnalyze();
      }
    });

    canvas.addEventListener("pointerdown", function (e) {
      if (e.button === 2) return;
      const pt = eventCoords(e);
      const map = get2DCurveMapping(canvas);
      const hit = hitTestHandle(pt.x, pt.y);

      if (hit >= 0) {
        beginUndoGesture();
        activeKnotIdx = hit;
        state.isInteracting = true;
        canvas.setPointerCapture?.(e.pointerId);
        draw2DCurveEditor();
        return;
      }

      // In Freeform Curve mode, clicking on the right half adds a new PCHIP knot!
      if (state.params.use_custom_profile && pt.x >= map.centerX - 6 && state.params.profile_points.length < 18) {
        beginUndoGesture();
        const lim = getDynamicPrinterLimits();
        const zn = clampFloat(map.yToZNorm(pt.y), 0.5, 0.02, 0.98);
        const r = clampFloat(map.xToR(pt.x), 38.0, 8.0, lim.maxCurveR);
        const pts = state.params.profile_points.slice();
        pts.push([zn, r]);
        pts.sort(function (a, b) { return a[0] - b[0]; });
        state.params.profile_points = normalizeProfilePoints(pts);

        // Locate newly inserted knot
        let bestK = 1;
        let minDz = 999;
        for (let k = 1; k < state.params.profile_points.length - 1; k++) {
          const dz = Math.abs(state.params.profile_points[k][0] - zn);
          if (dz < minDz) { minDz = dz; bestK = k; }
        }
        activeKnotIdx = bestK;
        state.isInteracting = true;
        canvas.setPointerCapture?.(e.pointerId);
        rebuildScene(true);
      }
    });

    canvas.addEventListener("pointermove", function (e) {
      const pt = eventCoords(e);
      const map = get2DCurveMapping(canvas);
      const rCur = map.xToR(Math.max(map.centerX + 4, pt.x));
      const znCur = map.yToZNorm(pt.y);
      if (readout) {
        const zMm = (znCur * state.params.height_mm).toFixed(1);
        const dMm = (2.0 * rCur).toFixed(1);
        readout.textContent = "Z " + zMm + " · Ø " + dMm + " mm";
      }

      if (activeKnotIdx < 0) {
        const hIdx = hitTestHandle(pt.x, pt.y);
        if (hIdx !== hoverKnotIdx) {
          hoverKnotIdx = hIdx;
          draw2DCurveEditor();
        }
        return;
      }

      const lim = getDynamicPrinterLimits();
      if (state.params.use_custom_profile) {
        const pts = state.params.profile_points;
        const lastIdx = pts.length - 1;
        if (activeKnotIdx === 0) {
          pts[0][0] = 0.0;
          pts[0][1] = clampFloat(rCur, 38.0, 10.0, lim.maxCurveR);
        } else if (activeKnotIdx === lastIdx) {
          pts[lastIdx][0] = 1.0;
          pts[lastIdx][1] = clampFloat(rCur, 42.0, 8.0, lim.maxCurveR);
        } else if (activeKnotIdx > 0 && activeKnotIdx < lastIdx) {
          const zLo = pts[activeKnotIdx - 1][0] + 0.025;
          const zHi = pts[activeKnotIdx + 1][0] - 0.025;
          pts[activeKnotIdx][0] = Math.max(zLo, Math.min(zHi, znCur));
          pts[activeKnotIdx][1] = clampFloat(rCur, 40.0, 8.0, lim.maxCurveR);
        }
      } else {
        // Parametric handle drag updates sliders live!
        if (activeKnotIdx === 0) {
          state.params.base_diameter_mm = clampFloat(2.0 * rCur, 76.0, 20.0, lim.maxDiam);
        } else if (activeKnotIdx === 1) {
          state.params.belly_diameter_mm = clampFloat(2.0 * rCur, 110.0, 20.0, lim.maxDiam);
          state.params.belly_height_ratio = clampFloat(znCur, 0.34, 0.08, 0.85);
        } else if (activeKnotIdx === 2) {
          state.params.waist_diameter_mm = clampFloat(2.0 * rCur, 68.0, 16.0, lim.maxDiam);
          state.params.waist_height_ratio = clampFloat(znCur, 0.68, 0.15, 0.92);
        } else if (activeKnotIdx === 3) {
          state.params.neck_diameter_mm = clampFloat(2.0 * rCur, 82.0, 16.0, lim.maxDiam);
        } else if (activeKnotIdx === 4) {
          const flare = rCur - 0.5 * state.params.neck_diameter_mm;
          state.params.lip_flare_mm = clampFloat(flare, 4.0, -15.0, 25.0);
        }
        syncSlidersOnly();
      }
      rebuildScene(true);
    });

    const stopKnotDrag = function (e) {
      if (activeKnotIdx >= 0) {
        activeKnotIdx = -1;
        state.isInteracting = false;
        canvas.releasePointerCapture?.(e.pointerId);
        commitUndoGesture();
        rebuildScene(false);
        scheduleHostAnalyze();
      }
    };
    canvas.addEventListener("pointerup", stopKnotDrag);
    canvas.addEventListener("pointercancel", stopKnotDrag);
  }

  // ==========================================================================
  // 9. UI Controls Binding, Presets Gallery & Bilingual Updates
  // ==========================================================================
  const sliderRefs = {};

  function buildSliderWidgets() {
    for (let i = 0; i < SLIDER_SPECS.length; i++) {
      const spec = SLIDER_SPECS[i];
      const host = document.querySelector('[data-slider="' + spec.path + '"]');
      if (!host) continue;

      const decs = spec.step < 0.1 ? 2 : (spec.step < 1 ? 1 : 0);
      const initVal = getByPath(state.params, spec.path);

      host.className = "ctrl-row";
      host.innerHTML =
        '<div class="ctrl-top">' +
          '<span class="ctrl-label" data-spec-label="' + spec.path + '">' + (state.lang === "en" ? spec.en : spec.pt) + '</span>' +
          '<div class="ctrl-val-wrap">' +
            '<input class="ctrl-num" type="number" min="' + spec.min + '" max="' + spec.max + '" step="' + spec.step + '" value="' + Number(initVal).toFixed(decs) + '" />' +
            '<span class="ctrl-unit">' + spec.unit + '</span>' +
          '</div>' +
        '</div>' +
        '<input class="orca-slider" type="range" min="' + spec.min + '" max="' + spec.max + '" step="' + spec.step + '" value="' + initVal + '" />';

      const rangeEl = host.querySelector('input[type="range"]');
      const numEl = host.querySelector('input[type="number"]');
      const labelEl = host.querySelector("[data-spec-label]");

      sliderRefs[spec.path] = { spec: spec, rangeEl: rangeEl, numEl: numEl, labelEl: labelEl, decs: decs };

      if (rangeEl) {
        rangeEl.addEventListener("pointerdown", function () {
          beginUndoGesture();
          state.isInteracting = true;
        });

        rangeEl.addEventListener("input", function () {
          let v = Number(rangeEl.value);
          if (spec.path === "polygon_sides" && v > 0 && v < 3) v = 3;
          setByPath(state.params, spec.path, v);
          state.params = normalizeParams(state.params);
          const normV = getByPath(state.params, spec.path);
          if (numEl) numEl.value = Number(normV).toFixed(decs);
          updateDerivedBadges();
          rebuildScene(true);
        });

        const finishRange = function () {
          if (!state.isInteracting) return;
          state.isInteracting = false;
          commitUndoGesture();
          rebuildScene(false);
          scheduleHostAnalyze();
        };
        rangeEl.addEventListener("pointerup", finishRange);
        rangeEl.addEventListener("change", finishRange);
      }

      if (numEl) {
        numEl.addEventListener("change", function () {
          const before = deepClone(state.params);
          let v = Number(numEl.value);
          if (spec.path === "polygon_sides" && v > 0 && v < 3) v = 3;
          setByPath(state.params, spec.path, v);
          state.params = normalizeParams(state.params);
          const normV = getByPath(state.params, spec.path);
          numEl.value = Number(normV).toFixed(decs);
          if (rangeEl) rangeEl.value = String(normV);
          pushUndoSnapshot(before);
          updateDerivedBadges();
          rebuildScene(false);
          scheduleHostAnalyze();
        });
      }
    }
  }

  function syncDynamicPrinterBounds() {
    const lim = getDynamicPrinterLimits();
    const updateRefMax = function (path, newMax) {
      const ref = sliderRefs[path];
      if (!ref) return;
      ref.spec.max = newMax;
      if (ref.rangeEl) {
        ref.rangeEl.max = String(newMax);
        const curVal = getByPath(state.params, path);
        if (curVal !== undefined) {
          ref.rangeEl.value = String(Math.min(newMax, Number(curVal)));
        }
      }
      if (ref.numEl) {
        ref.numEl.max = String(newMax);
      }
    };

    updateRefMax("height_mm", lim.maxHeight);
    updateRefMax("base_diameter_mm", lim.maxDiam);
    updateRefMax("belly_diameter_mm", lim.maxDiam);
    updateRefMax("waist_diameter_mm", lim.maxDiam);
    updateRefMax("neck_diameter_mm", lim.maxDiam);
    return lim;
  }

  function fitParamsToActivePrinter() {
    const lim = getDynamicPrinterLimits();
    const before = deepClone(state.params);
    state.params.height_mm = Math.min(state.params.height_mm, lim.maxHeight);

    const curDx = state.clientMetrics && state.clientMetrics.dims ? state.clientMetrics.dims[0] : 0;
    const curDy = state.clientMetrics && state.clientMetrics.dims ? state.clientMetrics.dims[1] : 0;
    const maxActualSpan = Math.max(curDx, curDy, state.params.base_diameter_mm, state.params.belly_diameter_mm, state.params.neck_diameter_mm);
    const safeTargetSpan = Math.max(36.0, lim.minBedXY - 6.0);

    if (maxActualSpan > safeTargetSpan) {
      const ratio = safeTargetSpan / maxActualSpan;
      state.params.base_diameter_mm = Math.round(Math.max(20.0, Math.min(lim.maxDiam, state.params.base_diameter_mm * ratio)));
      state.params.belly_diameter_mm = Math.round(Math.max(20.0, Math.min(lim.maxDiam, state.params.belly_diameter_mm * ratio)));
      state.params.waist_diameter_mm = Math.round(Math.max(16.0, Math.min(lim.maxDiam, state.params.waist_diameter_mm * ratio)));
      state.params.neck_diameter_mm = Math.round(Math.max(16.0, Math.min(lim.maxDiam, state.params.neck_diameter_mm * ratio)));
      if (state.params.lip_flare_mm > 0) {
        state.params.lip_flare_mm = Number((state.params.lip_flare_mm * ratio).toFixed(1));
      }
      if (Array.isArray(state.params.profile_points)) {
        for (let i = 0; i < state.params.profile_points.length; i++) {
          state.params.profile_points[i][1] = Number(
            Math.max(8.0, Math.min(lim.maxCurveR, state.params.profile_points[i][1] * ratio)).toFixed(2)
          );
        }
      }
    } else {
      state.params.base_diameter_mm = Math.min(state.params.base_diameter_mm, lim.maxDiam);
      state.params.belly_diameter_mm = Math.min(state.params.belly_diameter_mm, lim.maxDiam);
      state.params.waist_diameter_mm = Math.min(state.params.waist_diameter_mm, lim.maxDiam);
      state.params.neck_diameter_mm = Math.min(state.params.neck_diameter_mm, lim.maxDiam);
    }

    state.params = normalizeParams(state.params);
    pushUndoSnapshot(before);
    syncControlsFromState();
    rebuildScene(false);
    fitCameraToVase();
    scheduleHostAnalyze();
    showToast(tr("toast_fitted_printer").replace("{name}", String(state.printer.name || "Printer")), false);
  }

  function syncSlidersOnly() {
    const paths = Object.keys(sliderRefs);
    for (let i = 0; i < paths.length; i++) {
      const ref = sliderRefs[paths[i]];
      const v = getByPath(state.params, paths[i]);
      if (v === undefined) continue;
      const maxAttr = ref.spec && typeof ref.spec.max === "number" ? ref.spec.max : Number(v);
      if (ref.rangeEl) ref.rangeEl.value = String(Math.min(maxAttr, Number(v)));
      if (ref.numEl) ref.numEl.value = Number(v).toFixed(ref.decs);
    }
  }

  function syncSectionCutControls() {
    const isZ = state.cutAxis === "z";
    const btnY = document.getElementById("btn-cut-mode-y");
    const btnZ = document.getElementById("btn-cut-mode-z");
    const inp = document.getElementById("inp-cross-cut");
    const lbl = document.getElementById("lbl-cross-cut");
    if (btnY) btnY.classList.toggle("active", !isZ);
    if (btnZ) btnZ.classList.toggle("active", isZ);
    if (inp) {
      inp.min = isZ ? "5" : "0";
      inp.max = "100";
      inp.value = String(isZ ? state.zSlicePct : state.crossCutPct);
    }
    if (lbl) {
      if (isZ) {
        if (state.zSlicePct >= 100) {
          lbl.textContent = "Off";
        } else {
          const zMm = Math.round(state.params.height_mm * (state.zSlicePct / 100.0));
          lbl.textContent = state.zSlicePct + "% (" + zMm + "mm)";
        }
      } else {
        lbl.textContent = state.crossCutPct === 0 ? "Off" : (state.crossCutPct + "%");
      }
    }
  }

  function updateDerivedBadges() {
    const polyBadge = document.getElementById("poly-badge");
    if (polyBadge) {
      const n = state.params.polygon_sides | 0;
      polyBadge.textContent = n < 3 ? tr("poly_circle") : tr("poly_sides_fmt").replace("{n}", String(n));
    }

    const activeTexBadge = document.getElementById("active-tex-badge");
    if (activeTexBadge) {
      let c = 0;
      const t = state.params.textures;
      if (t.ribbed.enabled) c++;
      if (t.waves.enabled) c++;
      if (t.origami.enabled) c++;
      if (t.cellular.enabled) c++;
      activeTexBadge.textContent = tr("active_tex_fmt").replace("{n}", String(c));
    }

    const texNames = ["ribbed", "waves", "origami", "cellular"];
    for (let i = 0; i < texNames.length; i++) {
      const k = texNames[i];
      const card = document.querySelector('[data-tex-card="' + k + '"]');
      if (card) card.classList.toggle("enabled", Boolean(state.params.textures[k].enabled));
    }

    const isSpiral = state.params.print_mode === "spiral_vase";
    const btnSpiral = document.getElementById("btn-mode-spiral");
    const btnHollow = document.getElementById("btn-mode-hollow");
    const boxSpiral = document.getElementById("box-spiral-opts");
    const boxHollow = document.getElementById("box-hollow-opts");
    if (btnSpiral) btnSpiral.classList.toggle("active", isSpiral);
    if (btnHollow) btnHollow.classList.toggle("active", !isSpiral);
    if (boxSpiral) boxSpiral.style.display = isSpiral ? "flex" : "none";
    if (boxHollow) boxHollow.style.display = isSpiral ? "none" : "flex";

    // Wall mode badge + 1-click preset chips + live nozzle perimeter hint
    const wallBadge = document.getElementById("wall-mode-badge");
    if (wallBadge) {
      wallBadge.textContent = isSpiral
        ? tr("wall_badge_spiral").replace("{w}", state.params.spiral_line_width_mm.toFixed(2))
        : tr("wall_badge_hollow").replace("{w}", state.params.wall_thickness_mm.toFixed(1));
    }

    const wallChips = document.querySelectorAll("[data-wall-preset]");
    for (let i = 0; i < wallChips.length; i++) {
      const wVal = Number(wallChips[i].getAttribute("data-wall-preset"));
      wallChips[i].classList.toggle("active", !isSpiral && Math.abs(state.params.wall_thickness_mm - wVal) < 0.05);
    }

    const perimHint = document.getElementById("wall-perim-hint");
    if (perimHint) {
      const lineW = Math.max(0.20, Number(state.printer.line_width_mm) || 0.42);
      const loops = Math.max(1, Math.round(state.params.wall_thickness_mm / lineW));
      const mouthIn = (state.clientMetrics && state.clientMetrics.mouthInnerDiam)
        ? state.clientMetrics.mouthInnerDiam
        : Math.max(6.0, state.params.neck_diameter_mm + 2.0 * state.params.lip_flare_mm - 2.0 * state.params.wall_thickness_mm);
      perimHint.textContent = tr("perim_hint_fmt")
        .replace("{n}", String(loops))
        .replace("{lw}", lineW.toFixed(2))
        .replace("{id}", mouthIn.toFixed(1));
    }

    const spFloorHint = document.getElementById("spiral-floor-hint");
    if (spFloorHint) {
      const lh = Math.max(0.08, Number(state.printer.layer_height_mm) || 0.20);
      const noz = Math.max(0.15, Number(state.printer.nozzle_mm) || 0.40);
      const spMm = (state.params.spiral_bottom_layers * lh).toFixed(1);
      const wMinRec = Math.max(0.40, noz * 1.25).toFixed(2);
      const wMaxRec = Math.min(1.20, Math.max(0.45, noz * 1.85)).toFixed(2);
      spFloorHint.textContent = tr("spiral_floor_fmt")
        .replace("{mm}", spMm)
        .replace("{n}", String(state.params.spiral_bottom_layers))
        .replace("{noz}", noz.toFixed(1))
        .replace("{wmin}", wMinRec)
        .replace("{wmax}", wMaxRec);
    }

    // Honest Spiral Mode Viewport Info Banner
    const spiralBanner = document.getElementById("spiral-mode-banner");
    const spiralBannerIcon = document.getElementById("spiral-banner-icon");
    const spiralBannerText = document.getElementById("spiral-banner-text");
    if (spiralBanner) {
      spiralBanner.classList.toggle("visible", isSpiral);
      const stlSafe = Boolean(state.params.stl_always_open_hollow);
      spiralBanner.classList.toggle("warn", isSpiral && !stlSafe);
      if (spiralBannerIcon) spiralBannerIcon.textContent = stlSafe ? "🌀" : "⚠";
      if (spiralBannerText) {
        spiralBannerText.textContent = stlSafe ? tr("banner_spiral_safe") : tr("banner_spiral_closed");
      }
    }

    // Viewport X-Ray, Caliper, Material & Heatmap states
    const xrayBtn = document.getElementById("btn-vp-xray");
    const xrayLeg = document.getElementById("xray-legend");
    const calBtn = document.getElementById("btn-vp-calipers");
    const hmBtn = document.getElementById("btn-vp-heatmap");
    const hmLeg = document.getElementById("heatmap-legend");
    const selMat = document.getElementById("sel-material");
    if (xrayBtn) xrayBtn.classList.toggle("active", Boolean(state.xrayMode));
    if (xrayLeg) xrayLeg.classList.toggle("visible", Boolean(state.xrayMode));
    if (calBtn) calBtn.classList.toggle("active", isCalipersActive());
    if (hmBtn) hmBtn.classList.toggle("active", !state.xrayMode && state.material === "heatmap");
    if (hmLeg) hmLeg.classList.toggle("visible", !state.xrayMode && state.material === "heatmap");
    if (selMat) selMat.value = state.xrayMode ? "xray" : state.material;

    syncSectionCutControls();

    const isCustom = Boolean(state.params.use_custom_profile);
    const btnProfSliders = document.getElementById("btn-prof-sliders");
    const btnProfCurve = document.getElementById("btn-prof-curve");
    const paramBox = document.getElementById("parametric-diameters-box");
    const curveHint = document.getElementById("curve-hint");
    if (btnProfSliders) btnProfSliders.classList.toggle("active", !isCustom);
    if (btnProfCurve) btnProfCurve.classList.toggle("active", isCustom);
    if (paramBox) paramBox.style.display = isCustom ? "none" : "flex";
    if (curveHint) curveHint.textContent = isCustom ? tr("hint_curve_free") : tr("hint_curve_sliders");

    const drnBox = document.getElementById("box-drainage-opts");
    const drnNote = document.getElementById("drainage-mode-note");
    if (drnBox) drnBox.style.display = state.params.drainage.enabled ? "flex" : "none";
    if (drnNote) drnNote.textContent = isSpiral ? tr("note_drainage_spiral") : tr("note_drainage_hollow");

    const sauBox = document.getElementById("box-saucer-opts");
    const sauWarn = document.getElementById("saucer-spiral-warn");
    const vpSaucer = document.getElementById("btn-vp-saucer");
    const vpSaucerLayout = document.getElementById("btn-vp-saucer-layout");
    if (sauBox) sauBox.style.display = state.includeSaucer ? "flex" : "none";
    if (sauWarn) sauWarn.style.display = (state.includeSaucer && isSpiral) ? "block" : "none";
    if (vpSaucer) vpSaucer.classList.toggle("active", state.includeSaucer);
    if (vpSaucerLayout) {
      vpSaucerLayout.style.display = state.includeSaucer ? "inline-flex" : "none";
      vpSaucerLayout.textContent = state.saucerLayout === "nested" ? tr("vp_layout_nested") : tr("vp_layout_side");
    }
  }

  function syncControlsFromState() {
    const nameEl = document.getElementById("inp-vase-name");
    if (nameEl) nameEl.value = state.params.name;

    syncSlidersOnly();

    const setChk = function (id, val) {
      const el = document.getElementById(id);
      if (el) el.checked = Boolean(val);
    };
    setChk("chk-tex-ribbed", state.params.textures.ribbed.enabled);
    setChk("chk-tex-waves", state.params.textures.waves.enabled);
    setChk("chk-tex-origami", state.params.textures.origami.enabled);
    setChk("chk-tex-cellular", state.params.textures.cellular.enabled);
    setChk("chk-cel-ridge", state.params.textures.cellular.ridge_mode);
    setChk("chk-stl-open-hollow", state.params.stl_always_open_hollow);
    setChk("chk-auto-slicer", state.params.auto_configure_slicer);
    setChk("chk-spiral-smooth", state.params.spiral_smooth);
    setChk("chk-clamp-overhang", state.params.auto_clamp_overhang);
    setChk("chk-drainage", state.params.drainage.enabled);
    setChk("chk-include-saucer", state.includeSaucer);
    setChk("chk-saucer-tex", state.params.saucer.match_vase_texture);

    updateDerivedBadges();
  }

  function makePresetMiniSvg(presetParams) {
    const p = normalizeParams(presetParams);
    const knots = prepareSilhouetteKnots(p);
    const spline = buildPchipSpline(knots.xs, knots.ys);
    const steps = 16;
    let rightPts = "";
    let leftPts = "";
    const maxR = 72.0;
    for (let i = 0; i <= steps; i++) {
      const zn = i / steps;
      const r = Math.min(maxR, evalPchipScalar(spline, zn));
      const xOff = (r / maxR) * 12.0;
      const y = (33.0 - zn * 30.0).toFixed(1);
      rightPts += (i === 0 ? "M " : " L ") + (15.0 + xOff).toFixed(1) + " " + y;
    }
    for (let i = steps; i >= 0; i--) {
      const zn = i / steps;
      const r = Math.min(maxR, evalPchipScalar(spline, zn));
      const xOff = (r / maxR) * 12.0;
      const y = (33.0 - zn * 30.0).toFixed(1);
      leftPts += " L " + (15.0 - xOff).toFixed(1) + " " + y;
    }
    return '<svg width="30" height="36" viewBox="0 0 30 36">' +
      '<path d="' + rightPts + leftPts + ' Z" fill="rgba(0,191,165,0.22)" stroke="#00bfa5" stroke-width="1.4"/>' +
      '</svg>';
  }

  function matchesPresetCategory(item, filterCat) {
    if (filterCat === "all") return true;
    const cat = String(item.category || "").toLowerCase();
    if (filterCat === "user") return Boolean(item._isUser);
    if (filterCat === "planter") return cat.includes("plant") || cat.includes("garden") || cat.includes("cachep") || Boolean(item.params && item.params.drainage && item.params.drainage.enabled);
    if (filterCat === "geometric") return cat.includes("geom") || cat.includes("origami") || cat.includes("arch") || cat.includes("cryst") || Boolean(item.params && item.params.polygon_sides >= 3);
    if (filterCat === "organic") return !cat.includes("geom") && !cat.includes("arch");
    return true;
  }

  function renderPresetsGrid() {
    const gridEl = document.getElementById("presets-grid");
    if (!gridEl) return;
    gridEl.innerHTML = "";

    const combined = [];
    for (let i = 0; i < state.userPresets.length; i++) {
      combined.push(Object.assign({}, state.userPresets[i], { _isUser: true }));
    }
    for (let i = 0; i < state.builtinPresets.length; i++) {
      combined.push(Object.assign({}, state.builtinPresets[i], { _isUser: false }));
    }

    for (let i = 0; i < combined.length; i++) {
      const item = combined[i];
      if (!matchesPresetCategory(item, state.presetFilter)) continue;

      const card = document.createElement("div");
      card.className = "preset-card" + (item.id === state.activePresetId ? " active" : "");

      const title = state.lang === "en"
        ? (item.title_en || item.name || item.title_pt || "Preset")
        : (item.title_pt || item.name || item.title_en || "Preset");
      const desc = state.lang === "en"
        ? (item.description_en || item.category || "")
        : (item.description_pt || item.category || "");

      card.innerHTML =
        '<div class="preset-thumb">' + makePresetMiniSvg(item.params || {}) + '</div>' +
        '<div class="preset-meta">' +
          '<div class="preset-name"></div>' +
          '<div class="preset-sub"></div>' +
        '</div>';

      const nmEl = card.querySelector(".preset-name");
      const sbEl = card.querySelector(".preset-sub");
      if (nmEl) nmEl.textContent = title;
      if (sbEl) sbEl.textContent = desc;

      if (item._isUser) {
        const delBtn = document.createElement("button");
        delBtn.className = "preset-del-btn";
        delBtn.textContent = "×";
        delBtn.title = "Delete";
        delBtn.addEventListener("click", function (ev) {
          ev.stopPropagation();
          if (!sendToHost({ type: "preset_delete", id: item.id })) {
            state.userPresets = state.userPresets.filter(function (u) { return u.id !== item.id; });
            renderPresetsGrid();
          }
        });
        card.appendChild(delBtn);
      }

      card.addEventListener("click", function () {
        pushUndoSnapshot(state.params);
        state.activePresetId = item.id;
        state.params = normalizeParams(item.params);
        if (title) state.params.name = title;
        // Auto-enable saucer preview if preset has drainage enabled (botanical planter preset!)
        if (state.params.drainage.enabled) {
          state.includeSaucer = true;
        }
        // Expand enabled texture cards automatically
        const texKeys = ["ribbed", "waves", "origami", "cellular"];
        for (let t = 0; t < texKeys.length; t++) {
          const tk = texKeys[t];
          const tc = document.querySelector('[data-tex-card="' + tk + '"]');
          if (tc && state.params.textures[tk].enabled) tc.classList.add("expanded");
        }
        renderPresetsGrid();
        syncControlsFromState();
        rebuildScene(false);
        scheduleHostAnalyze();
      });

      gridEl.appendChild(card);
    }
  }

  function updatePrintabilityHud() {
    const rep = state.hostReport;
    const cm = state.clientMetrics;

    const dims = (!state.isInteracting && rep && Array.isArray(rep.dimensions_mm)) ? rep.dimensions_mm : cm.dims;
    const maxOvh = (!state.isInteracting && rep && typeof rep.max_overhang_deg === "number") ? rep.max_overhang_deg : cm.maxOverhang;
    const weightG = (!state.isInteracting && rep && typeof rep.estimated_weight_g === "number") ? rep.estimated_weight_g : cm.weightG;
    const tris = (!state.isInteracting && rep && typeof rep.triangle_count === "number") ? rep.triangle_count : cm.tris;
    const fitsBed = cm.fitsBed && (state.isInteracting || !rep || rep.fits_bed !== false);
    const fitsHeight = cm.fitsHeight && (state.isInteracting || !rep || rep.fits_height !== false);

    const wallFloorEl = document.getElementById("hud-wall-floor");
    const mouthHoleEl = document.getElementById("hud-mouth-hole");
    const dimsEl = document.getElementById("hud-dims");
    const ovhEl = document.getElementById("hud-overhang");
    const wgtEl = document.getElementById("hud-weight");
    const triEl = document.getElementById("hud-tris");
    const pillEl = document.getElementById("hud-status-pill");
    const warnEl = document.getElementById("hud-warnings");
    const bedBanner = document.getElementById("bed-alert-banner");
    const bedText = document.getElementById("bed-alert-text");

    const isSpiral = state.params.print_mode === "spiral_vase";
    if (wallFloorEl) {
      const wStr = Number(cm.wallMm || 2.4).toFixed(isSpiral ? 2 : 1);
      const fStr = Number(cm.floorMm || 3.2).toFixed(1);
      wallFloorEl.textContent = wStr + " / " + fStr + " mm";
    }
    if (mouthHoleEl) {
      mouthHoleEl.textContent = "Ø " + Number(cm.mouthInnerDiam || 77.2).toFixed(1) + " mm";
      mouthHoleEl.style.color = (isSpiral && !state.params.stl_always_open_hollow)
        ? "var(--status-warn)"
        : "var(--orca-accent-hover)";
    }

    if (dimsEl) dimsEl.textContent = Math.round(dims[0]) + "×" + Math.round(dims[1]) + "×" + Math.round(dims[2]);
    if (ovhEl) {
      ovhEl.textContent = maxOvh.toFixed(1) + "°";
      ovhEl.style.color = maxOvh > 55 ? "var(--status-crit)" : (maxOvh > 45 ? "var(--status-warn)" : "var(--status-ok)");
    }
    if (wgtEl) wgtEl.textContent = "~" + Math.max(1, Math.round(weightG)) + " g";
    if (triEl) triEl.textContent = tris >= 1000 ? (tris / 1000).toFixed(0) + "k" : String(tris);

    const isCrit = !fitsBed || !fitsHeight || maxOvh > 55.0;
    const isWarn = !isCrit && (maxOvh > 45.0 || Boolean(rep && rep.spiral_gap_risk));

    if (pillEl) {
      pillEl.className = "hud-status-pill " + (isCrit ? "crit" : (isWarn ? "warn" : "ok"));
      pillEl.textContent = isCrit ? tr("status_crit") : (isWarn ? tr("status_warn") : tr("status_ok"));
    }

    if (bedBanner && bedText) {
      const out = !fitsBed || !fitsHeight;
      bedBanner.classList.toggle("visible", out);
      if (out) {
        bedText.textContent = tr("bed_exceeded")
          .replace("{bx}", String(Math.round(state.printer.bed_x)))
          .replace("{by}", String(Math.round(state.printer.bed_y)))
          .replace("{bz}", String(Math.round(state.printer.max_z)));
      }
    }

    if (warnEl) {
      warnEl.innerHTML = "";
      if (rep && Array.isArray(rep.warnings)) {
        for (let i = 0; i < rep.warnings.length; i++) {
          const w = rep.warnings[i];
          const div = document.createElement("div");
          const code = String(w.code || "").toLowerCase();
          div.className = "hud-warn-item" + (code.includes("crit") || code.includes("bed") || code.includes("height") ? " crit" : "");
          div.textContent = state.lang === "en" ? (w.en || w.pt || "") : (w.pt || w.en || "");
          warnEl.appendChild(div);
        }
      }
    }
  }

  function updatePrinterPillUI() {
    const pr = state.printer;
    const prName = String(pr.name || "Generic 3D Printer");
    const isCirc = String(pr.bed_shape || "").toLowerCase() === "circular";
    const dimsStr = isCirc
      ? ("Ø" + Math.round(pr.bed_x || 220) + "×" + Math.round(pr.max_z || 250) + " mm")
      : (Math.round(pr.bed_x || 220) + "×" + Math.round(pr.bed_y || 220) + "×" + Math.round(pr.max_z || 250) + " mm");
    const nozVal = Number(pr.nozzle_mm || 0.4);
    const nozDigits = Math.abs(nozVal * 10 - Math.round(nozVal * 10)) > 0.02 ? 2 : 1;
    const nozzleStr = nozVal.toFixed(nozDigits) + "mm";

    const pillEl = document.getElementById("printer-pill");
    const nameEl = document.getElementById("printer-pill-name");
    const specsEl = document.getElementById("printer-pill-specs");
    const textEl = document.getElementById("printer-pill-text");

    if (nameEl && specsEl) {
      nameEl.textContent = prName;
      specsEl.textContent = "· " + dimsStr + " · " + nozzleStr;
    } else if (textEl) {
      textEl.textContent = prName + " · " + dimsStr + " · " + nozzleStr;
    }

    if (pillEl) {
      const detailParts = [prName + " · " + dimsStr + " · " + nozzleStr];
      if (pr.process_name) detailParts.push(String(pr.process_name));
      if (pr.filament_name) detailParts.push(String(pr.filament_name));
      detailParts.push(
        "LH " + Number(pr.layer_height_mm || 0.2).toFixed(2) + "mm / LW " + Number(pr.line_width_mm || 0.42).toFixed(2) + "mm"
      );
      pillEl.title = detailParts.join(" | ") + " — " + tr("printer_sync_tip");
    }
  }

  function applyThemeAndLanguage() {
    document.documentElement.setAttribute("data-theme", state.theme);
    document.documentElement.setAttribute("lang", state.lang);
    if (document.body) {
      document.body.setAttribute("data-mode", state.mode);
    }

    const langBtn = document.getElementById("btn-lang");
    if (langBtn) langBtn.textContent = state.lang.toUpperCase();

    const themeBtn = document.getElementById("btn-theme");
    if (themeBtn) themeBtn.textContent = state.theme === "dark" ? "☾" : "☀";

    updatePrinterPillUI();

    const nodes = document.querySelectorAll("[data-i18n]");
    for (let i = 0; i < nodes.length; i++) {
      const k = nodes[i].getAttribute("data-i18n");
      if (k) nodes[i].textContent = tr(k);
    }

    const paths = Object.keys(sliderRefs);
    for (let i = 0; i < paths.length; i++) {
      const ref = sliderRefs[paths[i]];
      if (ref.labelEl) {
        ref.labelEl.textContent = state.lang === "en" ? ref.spec.en : ref.spec.pt;
      }
    }

    updateDerivedBadges();
    renderPresetsGrid();
    updatePrintabilityHud();
    draw2DCurveEditor();
    requestRender();
  }

  function rebuildScene(fastInteractive) {
    const geo = buildFullStudioGeometry(state.params, Boolean(fastInteractive));
    uploadMeshToGPU(geo);
    updateDerivedBadges();
    draw2DCurveEditor();
    updatePrintabilityHud();
    requestRender();
  }

  function updateUndoButtons() {
    const u = document.getElementById("btn-undo");
    const r = document.getElementById("btn-redo");
    if (u) u.disabled = state.undoStack.length === 0;
    if (r) r.disabled = state.redoStack.length === 0;
  }

  function setActionButtonsBusy(busy) {
    state.busyAction = busy;
    const btns = document.querySelectorAll("[data-action]");
    for (let i = 0; i < btns.length; i++) {
      btns[i].disabled = busy;
    }
  }

  let toastTimer = null;
  function showToast(text, isError) {
    const el = document.getElementById("toast-banner");
    if (!el) return;
    el.textContent = text;
    el.classList.toggle("error", Boolean(isError));
    el.classList.add("visible");
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      el.classList.remove("visible");
    }, 3600);
  }

  function localPrintableRandomize(seedNum) {
    let s = (seedNum || Date.now()) >>> 0;
    const rand = function () {
      s = (Math.imul(s ^ (s >>> 15), 2246822519) + 3266489917) >>> 0;
      return (s >>> 0) / 4294967295.0;
    };
    const rr = function (lo, hi) { return lo + rand() * (hi - lo); };
    const p = deepClone(state.params);
    p.use_custom_profile = false;
    p.print_mode = "shelled_hollow";
    p.stl_always_open_hollow = true;
    p.wall_thickness_mm = Number(rr(1.8, 4.0).toFixed(1));
    p.bottom_thickness_mm = Number(rr(2.8, 4.4).toFixed(1));
    p.height_mm = Math.round(rr(115, 215));
    p.base_diameter_mm = Math.round(rr(62, 102));
    p.belly_diameter_mm = Math.round(p.base_diameter_mm * rr(0.95, 1.48));
    p.belly_height_ratio = Number(rr(0.24, 0.48).toFixed(2));
    p.waist_diameter_mm = Math.round(p.belly_diameter_mm * rr(0.68, 0.92));
    p.waist_height_ratio = Number(rr(0.58, 0.80).toFixed(2));
    p.neck_diameter_mm = Math.round(p.waist_diameter_mm * rr(0.92, 1.24));
    p.lip_flare_mm = Number(rr(0, 7.5).toFixed(1));
    p.polygon_sides = rand() < 0.28 ? [5, 6, 7, 8, 10, 12][Math.floor(rand() * 6)] : 0;
    p.global_twist_deg = Math.round(rr(-140, 140) / 5) * 5;

    const pick = Math.floor(rand() * 4);
    p.textures.ribbed.enabled = (pick === 0 || rand() < 0.25);
    p.textures.waves.enabled = (pick === 1 || rand() < 0.25);
    p.textures.origami.enabled = (pick === 2);
    p.textures.cellular.enabled = (pick === 3);
    p.textures.ribbed.count = Math.round(rr(16, 64));
    p.textures.ribbed.depth_mm = Number(rr(1.6, 3.6).toFixed(1));
    p.textures.waves.depth_mm = Number(rr(1.8, 3.8).toFixed(1));
    p.textures.waves.angular_lobes = Math.round(rr(3, 12));
    p.textures.cellular.seed = Math.floor(rr(1, 99990));
    p.auto_clamp_overhang = true;
    return normalizeParams(p);
  }

  function convertSlidersToCurve() {
    const before = deepClone(state.params);
    const knots = prepareSilhouetteKnots(Object.assign({}, state.params, { use_custom_profile: false }));
    const pts = [];
    for (let i = 0; i < knots.xs.length; i++) {
      pts.push([Number(knots.xs[i].toFixed(3)), Number(knots.ys[i].toFixed(2))]);
    }
    state.params.profile_points = normalizeProfilePoints(pts);
    state.params.use_custom_profile = true;
    pushUndoSnapshot(before);
    syncControlsFromState();
    rebuildScene(false);
    scheduleHostAnalyze();
    showToast(tr("toast_converted_curve"), false);
  }

  function sanitizeExportStem(name) {
    const clean = String(name || "vaso").replace(/[^\w\-. ]+/g, "").trim().replace(/\s+/g, "_");
    return clean || "vaso";
  }

  // ==========================================================================
  // 10. Event Wiring & Boot
  // ==========================================================================
  function bindUIControls() {
    const on = function (id, evt, fn) {
      const el = document.getElementById(id);
      if (el) el.addEventListener(evt, fn);
    };

    on("inp-vase-name", "change", function (e) {
      state.params.name = String(e.target.value || "").trim().slice(0, 80) || "Vaso";
    });

    on("printer-pill", "click", function () {
      if (!requestPrinterSync(true, 0)) {
        updatePrinterPillUI();
        const pr = state.printer;
        const dimsLabel = Math.round(pr.bed_x || 220) + "×" + Math.round(pr.bed_y || 220) + "×" + Math.round(pr.max_z || 250) + " mm";
        showToast(tr("toast_printer_synced").replace("{name}", String(pr.name || "Printer")).replace("{dims}", dimsLabel), false);
      }
    });

    on("btn-fit-to-printer", "click", fitParamsToActivePrinter);

    // Zero-permission automatic active printer sync whenever returning to the plugin tab!
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "visible") {
        requestPrinterSync(false, 250);
      }
    });

    if (typeof window !== "undefined" && typeof window.addEventListener === "function") {
      window.addEventListener("focus", function () {
        requestPrinterSync(false, 250);
      });
    }

    const shellRoot = document.querySelector(".studio-shell") || document.body;
    if (shellRoot && typeof shellRoot.addEventListener === "function") {
      shellRoot.addEventListener("pointerenter", function () {
        requestPrinterSync(false, 1200);
      });
    }

    if (typeof ResizeObserver !== "undefined" && shellRoot) {
      let wasHiddenZero = false;
      const tabRo = new ResizeObserver(function (entries) {
        let w = shellRoot.clientWidth || 0;
        let h = shellRoot.clientHeight || 0;
        if (entries && entries.length && entries[0].contentRect) {
          w = entries[0].contentRect.width;
          h = entries[0].contentRect.height;
        }
        if (w <= 2 || h <= 2) {
          wasHiddenZero = true;
        } else if (wasHiddenZero) {
          wasHiddenZero = false;
          requestPrinterSync(false, 150);
        }
      });
      tabRo.observe(shellRoot);
    }

    on("btn-undo", "click", performUndo);
    on("btn-redo", "click", performRedo);

    on("btn-randomize", "click", function () {
      const seed = Math.floor(Math.random() * 99999) + 1;
      if (!sendToHost({ type: "randomize", seed: seed, params: deepClone(state.params) })) {
        pushUndoSnapshot(state.params);
        state.params = localPrintableRandomize(seed);
        syncControlsFromState();
        rebuildScene(false);
        showToast(tr("toast_randomized"), false);
      }
    });

    on("btn-reset", "click", function () {
      pushUndoSnapshot(state.params);
      state.params = normalizeParams(JS_DEFAULT_PARAMS);
      state.includeSaucer = false;
      state.xrayMode = false;
      state.caliperOverride = null;
      state.cutAxis = "y";
      state.crossCutPct = 0;
      state.zSlicePct = 100;
      syncControlsFromState();
      rebuildScene(false);
      fitCameraToVase();
      scheduleHostAnalyze();
    });

    on("btn-lang", "click", function () {
      state.lang = state.lang === "pt" ? "en" : "pt";
      applyThemeAndLanguage();
    });

    on("btn-theme", "click", function () {
      state.userOverrodeTheme = true;
      state.theme = state.theme === "dark" ? "light" : "dark";
      applyThemeAndLanguage();
    });

    // Dock Mode Tabs
    const tabBtns = document.querySelectorAll(".dock-tab-btn");
    for (let i = 0; i < tabBtns.length; i++) {
      tabBtns[i].addEventListener("click", function () {
        const tab = tabBtns[i].getAttribute("data-tab") || "shape";
        if (document.body) document.body.setAttribute("data-dock-tab", tab);
        for (let k = 0; k < tabBtns.length; k++) {
          tabBtns[k].classList.toggle("active", tabBtns[k] === tabBtns[i]);
        }
        draw2DCurveEditor();
        requestRender();
      });
    }

    // Preset save & filter chips
    on("btn-toggle-save-preset", "click", function () {
      const bar = document.getElementById("save-preset-bar");
      const inp = document.getElementById("inp-save-preset-name");
      if (bar) {
        const open = !bar.classList.contains("open");
        bar.classList.toggle("open", open);
        if (open && inp) {
          inp.value = state.params.name || "Meu Vaso";
          inp.focus?.();
        }
      }
    });

    on("btn-confirm-save-preset", "click", function () {
      const inp = document.getElementById("inp-save-preset-name");
      const bar = document.getElementById("save-preset-bar");
      const name = String(inp && inp.value ? inp.value : state.params.name || "Meu Vaso").trim() || "Meu Vaso";
      state.params.name = name;
      const nmMain = document.getElementById("inp-vase-name");
      if (nmMain) nmMain.value = name;
      if (!sendToHost({ type: "preset_save", name: name, params: deepClone(state.params) })) {
        state.userPresets.push({
          id: "local_" + Date.now(),
          name: name,
          title_pt: name,
          title_en: name,
          category: "user",
          params: deepClone(state.params)
        });
        renderPresetsGrid();
      }
      if (bar) bar.classList.remove("open");
      showToast(tr("toast_preset_saved"), false);
    });

    const filterChips = document.querySelectorAll("#preset-filters .filter-chip");
    for (let i = 0; i < filterChips.length; i++) {
      filterChips[i].addEventListener("click", function () {
        state.presetFilter = filterChips[i].getAttribute("data-cat") || "all";
        for (let k = 0; k < filterChips.length; k++) {
          filterChips[k].classList.toggle("active", filterChips[k] === filterChips[i]);
        }
        renderPresetsGrid();
      });
    }

    // Silhouette Mode Switch
    on("btn-prof-sliders", "click", function () {
      if (!state.params.use_custom_profile) return;
      pushUndoSnapshot(state.params);
      state.params.use_custom_profile = false;
      syncControlsFromState();
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    on("btn-prof-curve", "click", function () {
      if (state.params.use_custom_profile) return;
      pushUndoSnapshot(state.params);
      state.params.use_custom_profile = true;
      syncControlsFromState();
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    on("btn-sliders-to-curve", "click", convertSlidersToCurve);

    // Viewport Toolbar (Material + X-Ray / Parede + CAD mm Calipers + Overhang Heatmap)
    on("sel-material", "change", function (e) {
      const m = e.target.value;
      if (m === "xray") {
        state.xrayMode = true;
        if (state.caliperOverride === false) state.caliperOverride = null;
      } else {
        state.xrayMode = false;
        state.material = m;
        if (m !== "heatmap") state.prevSolidMaterial = m;
      }
      updateDerivedBadges();
      requestRender();
    });

    on("btn-vp-xray", "click", function () {
      state.xrayMode = !state.xrayMode;
      if (state.xrayMode && state.caliperOverride === false) {
        state.caliperOverride = null;
      }
      updateDerivedBadges();
      requestRender();
    });

    on("btn-vp-calipers", "click", function () {
      const cur = isCalipersActive();
      state.caliperOverride = !cur;
      updateDerivedBadges();
      requestRender();
    });

    on("btn-vp-heatmap", "click", function () {
      state.xrayMode = false;
      const next = state.material === "heatmap" ? (state.prevSolidMaterial || "emerald_silk") : "heatmap";
      state.material = next;
      updateDerivedBadges();
      requestRender();
    });

    on("btn-vp-wire", "click", function () {
      state.wireframe = !state.wireframe;
      const b = document.getElementById("btn-vp-wire");
      if (b) b.classList.toggle("active", state.wireframe);
      requestRender();
    });

    on("btn-vp-saucer", "click", function () {
      state.includeSaucer = !state.includeSaucer;
      syncControlsFromState();
      rebuildScene(false);
    });

    on("btn-vp-saucer-layout", "click", function () {
      state.saucerLayout = state.saucerLayout === "nested" ? "side" : "nested";
      updateDerivedBadges();
      rebuildScene(false);
    });

    on("btn-vp-spin", "click", function () {
      state.autoSpin = !state.autoSpin;
      const b = document.getElementById("btn-vp-spin");
      if (b) b.classList.toggle("active", state.autoSpin);
      if (state.autoSpin) requestRender();
    });

    // Camera Presets
    const camBtns = document.querySelectorAll("[data-cam]");
    for (let i = 0; i < camBtns.length; i++) {
      camBtns[i].addEventListener("click", function () {
        const kind = camBtns[i].getAttribute("data-cam");
        if (kind === "iso") { camera.yaw = -0.68; camera.pitch = 0.36; fitCameraToVase(); }
        else if (kind === "front") { camera.yaw = -Math.PI * 0.5; camera.pitch = 0.06; fitCameraToVase(); }
        else if (kind === "top") { camera.yaw = -Math.PI * 0.5; camera.pitch = 1.44; fitCameraToVase(); }
        else if (kind === "bottom") { camera.yaw = -Math.PI * 0.5; camera.pitch = -1.42; fitCameraToVase(); }
        else if (kind === "fit") { fitCameraToVase(); }
      });
    }

    // Dual Section Cut Inspector (Vertical Profile Y + Horizontal Plan Slice Z)
    on("btn-cut-mode-y", "click", function () {
      if (state.cutAxis === "y") return;
      state.cutAxis = "y";
      if (state.crossCutPct === 0 && state.zSlicePct < 100) {
        state.crossCutPct = 50;
      }
      updateSectionCapGPU();
      updateDerivedBadges();
      draw2DCurveEditor();
      requestRender();
    });

    on("btn-cut-mode-z", "click", function () {
      if (state.cutAxis === "z") return;
      state.cutAxis = "z";
      if (state.zSlicePct >= 100) {
        state.zSlicePct = state.crossCutPct > 0 ? clampInt(100 - state.crossCutPct, 50, 15, 85) : 60;
      }
      updateSectionCapGPU();
      updateDerivedBadges();
      draw2DCurveEditor();
      requestRender();
    });

    on("inp-cross-cut", "input", function (e) {
      if (state.cutAxis === "z") {
        state.zSlicePct = clampInt(e.target.value, 100, 5, 100);
        updateSectionCapGPU();
        draw2DCurveEditor();
      } else {
        state.crossCutPct = clampInt(e.target.value, 0, 0, 100);
      }
      updateDerivedBadges();
      requestRender();
    });

    on("btn-cut-half", "click", function () {
      if (state.cutAxis === "z") {
        state.zSlicePct = state.zSlicePct === 50 ? 100 : 50;
        updateSectionCapGPU();
        draw2DCurveEditor();
      } else {
        state.crossCutPct = state.crossCutPct === 50 ? 0 : 50;
      }
      updateDerivedBadges();
      requestRender();
    });

    on("btn-cut-off", "click", function () {
      state.crossCutPct = 0;
      state.zSlicePct = 100;
      updateSectionCapGPU();
      updateDerivedBadges();
      draw2DCurveEditor();
      requestRender();
    });

    // Texture Accordions & Enable Switches
    const expandHeads = document.querySelectorAll("[data-tex-toggle-expand]");
    for (let i = 0; i < expandHeads.length; i++) {
      expandHeads[i].addEventListener("click", function () {
        const key = expandHeads[i].getAttribute("data-tex-toggle-expand");
        const card = document.querySelector('[data-tex-card="' + key + '"]');
        if (card) card.classList.toggle("expanded");
      });
    }

    const bindTexChk = function (id, key) {
      on(id, "change", function (e) {
        pushUndoSnapshot(state.params);
        state.params.textures[key].enabled = Boolean(e.target.checked);
        const card = document.querySelector('[data-tex-card="' + key + '"]');
        if (card && e.target.checked) card.classList.add("expanded");
        updateDerivedBadges();
        rebuildScene(false);
        scheduleHostAnalyze();
      });
    };
    bindTexChk("chk-tex-ribbed", "ribbed");
    bindTexChk("chk-tex-waves", "waves");
    bindTexChk("chk-tex-origami", "origami");
    bindTexChk("chk-tex-cellular", "cellular");

    on("chk-cel-ridge", "change", function (e) {
      pushUndoSnapshot(state.params);
      state.params.textures.cellular.ridge_mode = Boolean(e.target.checked);
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    on("btn-reseed", "click", function () {
      pushUndoSnapshot(state.params);
      state.params.textures.cellular.seed = Math.floor(Math.random() * 99990) + 1;
      syncSlidersOnly();
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    // Print Mode, 1-Click Wall Presets, STL Open-Mouth Safety & Gardening Switches
    on("btn-mode-spiral", "click", function () {
      if (state.params.print_mode === "spiral_vase") return;
      pushUndoSnapshot(state.params);
      state.params.print_mode = "spiral_vase";
      updateDerivedBadges();
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    on("btn-mode-hollow", "click", function () {
      if (state.params.print_mode === "shelled_hollow") return;
      pushUndoSnapshot(state.params);
      state.params.print_mode = "shelled_hollow";
      updateDerivedBadges();
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    const wallPresetBtns = document.querySelectorAll("[data-wall-preset]");
    for (let i = 0; i < wallPresetBtns.length; i++) {
      wallPresetBtns[i].addEventListener("click", function () {
        const wVal = clampFloat(wallPresetBtns[i].getAttribute("data-wall-preset"), 2.4, 0.8, 25.0);
        pushUndoSnapshot(state.params);
        state.params.print_mode = "shelled_hollow";
        state.params.wall_thickness_mm = wVal;
        syncControlsFromState();
        rebuildScene(false);
        scheduleHostAnalyze();
      });
    }

    on("chk-stl-open-hollow", "change", function (e) {
      pushUndoSnapshot(state.params);
      state.params.stl_always_open_hollow = Boolean(e.target.checked);
      updateDerivedBadges();
      updatePrintabilityHud();
      requestRender();
    });

    on("chk-auto-slicer", "change", function (e) {
      state.params.auto_configure_slicer = Boolean(e.target.checked);
    });

    on("chk-spiral-smooth", "change", function (e) {
      state.params.spiral_smooth = Boolean(e.target.checked);
    });

    on("chk-clamp-overhang", "change", function (e) {
      pushUndoSnapshot(state.params);
      state.params.auto_clamp_overhang = Boolean(e.target.checked);
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    on("chk-drainage", "change", function (e) {
      pushUndoSnapshot(state.params);
      state.params.drainage.enabled = Boolean(e.target.checked);
      updateDerivedBadges();
      rebuildScene(false);
      scheduleHostAnalyze();
    });

    on("chk-include-saucer", "change", function (e) {
      state.includeSaucer = Boolean(e.target.checked);
      updateDerivedBadges();
      rebuildScene(false);
    });

    on("chk-saucer-tex", "change", function (e) {
      pushUndoSnapshot(state.params);
      state.params.saucer.match_vase_texture = Boolean(e.target.checked);
      rebuildScene(false);
    });

    // Primary Action & Export Buttons (Section 6 Bridge Protocol)
    const actionBtns = document.querySelectorAll("[data-action]");
    for (let i = 0; i < actionBtns.length; i++) {
      actionBtns[i].addEventListener("click", function () {
        const act = actionBtns[i].getAttribute("data-action");
        if (act === "send_to_plater") {
          setActionButtonsBusy(true);
          if (!sendToHost({
            type: "send_to_plater",
            params: deepClone(state.params),
            include_saucer: Boolean(state.includeSaucer)
          })) {
            setActionButtonsBusy(false);
            showToast("OrcaSlicer host bridge not connected (Standalone Preview).", true);
          }
        } else if (act === "export_3mf" || act === "export_stl") {
          const fmt = act === "export_3mf" ? "3mf" : "stl";
          const fname = sanitizeExportStem(state.params.name) + "." + fmt;
          setActionButtonsBusy(true);
          if (!sendToHost({
            type: "export_file",
            format: fmt,
            params: deepClone(state.params),
            include_saucer: Boolean(state.includeSaucer),
            filename: fname
          })) {
            setActionButtonsBusy(false);
            showToast("OrcaSlicer host bridge not connected (Standalone Preview).", true);
          }
        } else if (act === "open_folder") {
          sendToHost({ type: "open_exports_folder" });
        }
      });
    }

    // Global Keyboard Shortcuts: Ctrl+Z / Ctrl+Y / Ctrl+Shift+Z
    document.addEventListener("keydown", function (e) {
      const tag = (e.target && e.target.tagName) ? String(e.target.tagName).toUpperCase() : "";
      if (tag === "INPUT" || tag === "TEXTAREA") return;
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "z") {
        e.preventDefault();
        if (e.shiftKey) performRedo();
        else performUndo();
      } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "y") {
        e.preventDefault();
        performRedo();
      }
    });
  }

  Object.assign(globalThis.VaseStudioMath, {
    buildFullStudioGeometry: buildFullStudioGeometry,
    sampleGeoAtHeight: sampleGeoAtHeight,
    buildHorizontalZSliceCap: buildHorizontalZSliceCap,
    projectWorldToScreen: projectWorldToScreen,
    getDynamicPrinterLimits: getDynamicPrinterLimits,
    syncDynamicPrinterBounds: syncDynamicPrinterBounds,
    applyIncomingPrinter: applyIncomingPrinter,
    requestPrinterSync: requestPrinterSync,
    fitParamsToActivePrinter: fitParamsToActivePrinter,
    detectInjectedOrcaTheme: detectInjectedOrcaTheme,
    handleHostMessage: handleHostMessage,
    sliderRefs: sliderRefs,
    state: state
  });

  function bootStudioUI() {
    if (typeof document === "undefined" || !document.getElementById) return;
    const hostCssTheme = detectInjectedOrcaTheme();
    if (hostCssTheme === "light" || hostCssTheme === "dark") {
      state.theme = hostCssTheme;
    }
    buildSliderWidgets();
    syncDynamicPrinterBounds();
    initWebGLViewport();
    bind2DCurveEditor();
    bindUIControls();
    applyThemeAndLanguage();
    syncControlsFromState();
    rebuildScene(false);
    fitCameraToVase();
    connectOrcaBridge();
  }

  bootStudioUI();
})();
</script>
</body>
</html>
"""


def get_studio_html(mode: str = "page", initial_context: dict[str, Any] | None = None) -> str:
    """Return the complete 100% offline self-contained Studio HTML5/WebGL2 application.

    Args:
        mode: `"page"` for the wide 3-column OrcaSlicer tab, or `"dock"` for the
            compact right-side docked panel beside OrcaSlicer's 3D Plater.
        initial_context: Optional initial state dictionary (`lang`, `theme`,
            `printer`, `builtin_presets`, `user_presets`, `params`, `export_dir`).
    """
    norm_mode = "dock" if str(mode or "").strip().lower() == "dock" else "page"
    ctx: dict[str, Any] = copy.deepcopy(initial_context) if isinstance(initial_context, dict) else {}

    lang_raw = str(ctx.get("lang") or "pt").strip().lower()
    norm_lang = "en" if lang_raw.startswith("en") else "pt"

    theme_raw = str(ctx.get("theme") or "dark").strip().lower()
    norm_theme = "light" if theme_raw == "light" else "dark"

    fallback_params = copy.deepcopy(DEFAULT_PARAMS) if isinstance(DEFAULT_PARAMS, dict) else None
    fallback_presets = copy.deepcopy(BUILTIN_PRESETS) if isinstance(BUILTIN_PRESETS, list) else []

    boot_payload: dict[str, Any] = {
        "mode": norm_mode,
        "initial_context": ctx,
        "fallback_params": fallback_params,
        "fallback_presets": fallback_presets,
    }

    html = _STUDIO_UI_HTML_TEMPLATE
    html = html.replace("__INITIAL_LANG__", norm_lang)
    html = html.replace("__INITIAL_THEME__", norm_theme)
    html = html.replace("__INITIAL_MODE__", norm_mode)
    html = html.replace("__ORCA_VASE_STUDIO_BOOT_JSON__", _studio_ui_safe_json(boot_payload))
    return html

# ===========================================================================
# MODULE: vase_studio.plugin_main
# ===========================================================================

pass  # [bundled] hoisted __future__ import

from collections.abc import Sequence
import copy
import ctypes
import json
import locale
import math
import os
import re
import sys
import threading
import time
import types
from pathlib import Path
from typing import Any, Callable

# Intra-package imports (stripped cleanly when bundled into single-file PEP 723 script)
if "normalize_params" not in globals():
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import


# ---------------------------------------------------------------------------
# OrcaSlicer `orca` Native Binding Import (with standalone fallback stub)
# ---------------------------------------------------------------------------


def _build_fallback_orca_module() -> types.ModuleType:
    """Create a lightweight stand-in when imported outside OrcaSlicer."""
    mod = types.ModuleType("orca")
    mod._registered_capabilities = []
    mod._requested_permissions = {}
    mod._plugin_cls = None
    mod._saved_configs = {}

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

    class PythonPluginBase:
        def __init__(self) -> None:
            pass

        def get_name(self) -> str:
            return ""

        def get_type(self) -> str:
            return PluginType.Unknown

        def on_load(self) -> None:
            pass

        def on_unload(self) -> None:
            pass

        def on_cancelled(self) -> None:
            pass

        def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
            pass

        def has_config_ui(self) -> bool:
            return False

        def get_config_ui(self) -> str:
            return ""

        def get_default_config(self) -> dict[str, Any]:
            return {}

        def get_config(self) -> str:
            raw = mod._saved_configs.get(self.__class__.__name__)
            if raw is not None:
                return raw
            default_cfg = self.get_default_config()
            return json.dumps(default_cfg) if isinstance(default_cfg, dict) else "{}"

        def get_config_version(self) -> str:
            return "1.1.1"

        def save_config(self, config: str) -> bool:
            try:
                parsed = json.loads(config)
                if not isinstance(parsed, dict):
                    return False
            except Exception:
                return False
            mod._saved_configs[self.__class__.__name__] = str(config)
            return True

    class BasePlugin:
        def __init__(self) -> None:
            pass

        def register_capabilities(self) -> None:
            pass

    class PagesPluginCapabilityBase(PythonPluginBase):
        def get_type(self) -> str:
            return PluginType.Pages

        def get_ui(self) -> str:
            return ""

        def get_icon(self) -> str:
            return ""

        def on_message(self, data: Any) -> None:
            pass

        def post_message(self, data: Any) -> None:
            pass

    class ScriptPluginCapabilityBase(PythonPluginBase):
        def get_type(self) -> str:
            return PluginType.Script

        def execute(self) -> Any:
            return None

    class PluginResult:
        Success = 0
        Skipped = 1
        RecoverableError = 2
        FatalError = 3

    class ExecutionResult:
        def __init__(self, status: int = 0, message: str = "", data: str = "") -> None:
            self.status = status
            self.message = message
            self.data = data

        @classmethod
        def success(cls, message: str = "", data: str = "") -> "ExecutionResult":
            return cls(PluginResult.Success, message, data)

        @classmethod
        def skipped(cls, message: str = "") -> "ExecutionResult":
            return cls(PluginResult.Skipped, message, "")

        @classmethod
        def failure(cls, status: int, message: str, data: str = "") -> "ExecutionResult":
            return cls(status, message, data)

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

    def plugin_decorator(cls: type) -> type:
        mod._plugin_cls = cls
        return cls

    def register_capability(cap_cls: type) -> None:
        mod._registered_capabilities.append(cap_cls)

    def request_permissions(**kwargs: Any) -> None:
        mod._requested_permissions.update(kwargs)

    pages_mod = types.ModuleType("orca.pages")
    pages_mod.PagesPluginCapabilityBase = PagesPluginCapabilityBase

    script_mod = types.ModuleType("orca.script")
    script_mod.ScriptPluginCapabilityBase = ScriptPluginCapabilityBase

    plugin_sub = types.ModuleType("orca.host.plugin")
    plugin_sub.storage = lambda: str(Path(__file__).resolve().parent)

    host_mod = types.ModuleType("orca.host")
    host_mod.app_info = lambda: {"version": "2.5.1", "language": "pt_BR"}
    host_mod.app_language = lambda: "pt_BR"
    host_mod.preset_bundle = lambda: None
    host_mod.plater = lambda: None
    host_mod.model = lambda: None
    host_mod.selected_printer = lambda: None
    host_mod.plugin = plugin_sub
    host_mod.ui = types.SimpleNamespace(
        NotificationLevel=NotificationLevel,
        create_dock_panel=None,
        create_window=None,
        push_notification=None,
        message=None,
    )
    host_mod.preset = types.SimpleNamespace(
        process=None,
        printer=None,
        filament=None,
    )

    mod.base = BasePlugin
    mod.PythonPluginBase = PythonPluginBase
    mod.PluginType = PluginType
    mod.PluginResult = PluginResult
    mod.LifecycleEvent = LifecycleEvent
    mod.LifecycleEvtCode = LifecycleEvtCode
    mod.ExecutionResult = ExecutionResult
    mod.plugin = plugin_decorator
    mod.register_capability = register_capability
    mod.request_permissions = request_permissions
    mod.pages = pages_mod
    mod.script = script_mod
    mod.host = host_mod

    return mod


try:
    import orca  # type: ignore[import-not-found]
except ImportError:
    orca = _build_fallback_orca_module()


PLUGIN_SLUG = "orca_vase_generator"
WM_COPYDATA = 0x004A
SMTO_ABORTIFHUNG = 0x0002
ORCA_OTHER_INSTANCE_DWDATA = 1

ICON_SVG_CONTENT: str = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" fill="none">
  <defs>
    <linearGradient id="orcaBodyFill" x1="13" y1="10" x2="50" y2="55" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="46%" stop-color="#00BFA5"/>
      <stop offset="100%" stop-color="#00897B"/>
    </linearGradient>
    <linearGradient id="orcaBodyShade" x1="12" y1="32" x2="52" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.32"/>
      <stop offset="45%" stop-color="#00BFA5" stop-opacity="0.0"/>
      <stop offset="100%" stop-color="#004D40" stop-opacity="0.46"/>
    </linearGradient>
    <linearGradient id="orcaRimStroke" x1="14" y1="9" x2="50" y2="56" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="55%" stop-color="#00BFA5"/>
      <stop offset="100%" stop-color="#00897B"/>
    </linearGradient>
    <linearGradient id="orcaWaveLight" x1="16" y1="14" x2="46" y2="53" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#B2FFFC" stop-opacity="0.92"/>
      <stop offset="50%" stop-color="#00E5FF" stop-opacity="0.78"/>
      <stop offset="100%" stop-color="#00BFA5" stop-opacity="0.35"/>
    </linearGradient>
    <linearGradient id="orcaMouthWall" x1="18" y1="8" x2="46" y2="15" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFE082"/>
      <stop offset="52%" stop-color="#FFB74D"/>
      <stop offset="100%" stop-color="#F57C00"/>
    </linearGradient>
    <linearGradient id="orcaMouthCavity" x1="22" y1="9" x2="42" y2="15" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#6D3605"/>
      <stop offset="48%" stop-color="#B45309"/>
      <stop offset="85%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#FFB74D"/>
    </linearGradient>
    <clipPath id="orcaVaseClip">
      <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"/>
    </clipPath>
  </defs>

  <!-- Subtle CAD Plater Base Ring -->
  <ellipse cx="32" cy="54.2" rx="22.5" ry="5.6" stroke="#00BFA5" stroke-width="1.25" stroke-opacity="0.48"/>
  <path d="M13.5 54.2 H50.5 M21.0 50.0 L43.0 58.2 M43.0 50.0 L21.0 58.2" stroke="#00E5FF" stroke-width="0.75" stroke-opacity="0.26" stroke-linecap="round"/>

  <!-- Sculpted Organic-Wave Vase Silhouette -->
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"
        fill="url(#orcaBodyFill)"/>
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"
        fill="url(#orcaBodyShade)"/>

  <!-- Helical Spiral Wave Ribs (Clipped Inside Vase Body) -->
  <g clip-path="url(#orcaVaseClip)">
    <!-- Deep sculpted wave valleys -->
    <path d="M15.0 14.0 C13.5 24.5 21.5 34.0 26.5 44.5 C29.0 49.8 31.8 54.0 34.5 57.0"
          stroke="#00695C" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.45"/>
    <path d="M23.5 13.0 C21.0 23.5 30.5 33.5 36.0 44.5 C38.8 50.0 41.0 53.8 43.2 56.5"
          stroke="#00695C" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.48"/>
    <path d="M33.0 13.0 C31.0 23.5 40.0 33.0 45.5 43.8 C47.8 48.2 49.5 51.5 51.0 54.0"
          stroke="#004D40" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.50"/>

    <!-- Crisp specular spiral wave crests -->
    <path d="M17.2 14.0 C15.2 24.2 23.5 33.8 28.6 44.5 C31.2 49.8 33.8 53.8 36.2 56.8"
          stroke="url(#orcaWaveLight)" stroke-width="1.75" stroke-linecap="round"/>
    <path d="M25.8 13.2 C23.6 23.4 32.8 33.4 38.2 44.2 C40.8 49.5 42.8 53.2 44.8 55.8"
          stroke="url(#orcaWaveLight)" stroke-width="1.85" stroke-linecap="round"/>
    <path d="M35.2 13.5 C33.2 23.2 42.0 32.6 47.2 43.2 C49.2 47.4 50.6 50.5 52.0 53.0"
          stroke="#00E5FF" stroke-width="1.55" stroke-linecap="round" stroke-opacity="0.68"/>
    <path d="M12.2 28.0 C15.0 35.5 19.8 43.2 24.8 51.8 C26.2 54.2 27.6 55.6 29.0 56.8"
          stroke="#80FFEA" stroke-width="1.45" stroke-linecap="round" stroke-opacity="0.65"/>
  </g>

  <!-- Crisp Outer Silhouette Contour (Native Contrast on Light & Dark Tabs) -->
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5"
        stroke="url(#orcaRimStroke)" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Warm Amber-Gold Open Mouth Wall Rim & Hollow Interior -->
  <ellipse cx="32" cy="11.5" rx="13.5" ry="4.5" fill="url(#orcaMouthWall)" stroke="#FFB74D" stroke-width="1.1"/>
  <ellipse cx="32" cy="11.6" rx="10.1" ry="3.05" fill="url(#orcaMouthCavity)" stroke="#FFF3E0" stroke-width="0.65" stroke-opacity="0.65"/>
  <!-- Inner Cavity Spiral Depth Hint -->
  <path d="M25.5 10.2 C26.8 11.8 28.8 13.1 31.2 14.3 M32.8 9.0 C34.2 10.9 36.2 12.5 38.4 13.8"
        stroke="#FFE082" stroke-width="0.9" stroke-linecap="round" stroke-opacity="0.45"/>
</svg>
"""


# ---------------------------------------------------------------------------
# Environment, Host Inspection & In-Process Win32 `WM_COPYDATA` IPC Helpers
# ---------------------------------------------------------------------------


def _is_native_orca_host() -> bool:
    """Return True only when running inside the real C++ pybind11 OrcaSlicer host."""
    base_cls = getattr(orca, "base", None)
    return base_cls is not None and type(base_cls).__name__ == "pybind11_type"


def _is_mock_callable(obj: Any) -> bool:
    """Detect unittest.mock objects without importing unittest.mock eagerly."""
    cls_mod = getattr(type(obj), "__module__", "")
    return cls_mod.startswith("unittest.mock")


def _orca_os_default_data_dir() -> Path:
    """Resolve OrcaSlicer's default `data_dir()` across Windows, macOS, and Linux."""
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


def _orca_data_dir() -> Path:
    """Resolve OrcaSlicer's active `data_dir()`, honoring custom/portable `--datadir` or Flatpak
    installations whenever `__file__` resides inside an `orca_plugins` directory tree on the host OS.
    """
    platform_matches_host = (sys.platform == "win32") == (os.name == "nt")
    if platform_matches_host:
        try:
            here = Path(__file__).resolve()
            for parent in here.parents:
                if parent.name == "orca_plugins" and parent.parent != parent:
                    return parent.parent
        except Exception:
            pass
    return _orca_os_default_data_dir()


def _default_installed_plugin_dir() -> Path:
    return _orca_data_dir() / "orca_plugins" / PLUGIN_SLUG


def _default_plugin_data_dir() -> Path:
    return _orca_data_dir() / "orca_plugins" / "plugin_data" / PLUGIN_SLUG


def _resolve_storage_dir(*, in_callback: bool = True) -> Path:
    """Resolve current plugin storage folder safely (`orca.host.plugin.storage()` inside callbacks)."""
    # 1. Inside capability callbacks, query canonical `orca.host.plugin.storage()` first
    if in_callback:
        host_plugin = getattr(getattr(orca, "host", None), "plugin", None)
        top_plugin = getattr(orca, "plugin", None)
        holders = [host_plugin]
        if isinstance(top_plugin, types.ModuleType):
            holders.append(top_plugin)
        for holder in holders:
            storage_fn = getattr(holder, "storage", None)
            if callable(storage_fn):
                try:
                    raw = storage_fn()
                    if isinstance(raw, (str, os.PathLike)) and str(raw).strip():
                        return Path(raw)
                except Exception:
                    pass

    # 2. In native OrcaSlicer, prefer `plugin_data/orca_vase_generator`
    if _is_native_orca_host():
        data_dir = _default_plugin_data_dir()
        try:
            data_dir.mkdir(parents=True, exist_ok=True)
            return data_dir
        except Exception:
            pass

    # 3. Fallback to __file__ parent if available
    try:
        here = Path(__file__).resolve().parent
        if here.exists():
            return here
    except Exception:
        pass

    return _default_installed_plugin_dir()


def _format_other_instance_payload(file_paths: Sequence[str | Path]) -> str:
    """Format Win32 `WM_COPYDATA` payload matching `OrcaSlicer.dll` `unescape_strings_cstyle`.

    Produces `"orca-slicer.exe";"<resolved_path_1>";...` where every token escapes
    `\\` -> `\\\\`, `"` -> `\\"`, `\\r` -> `\\r`, `\\n` -> `\\n`, wrapped in double quotes and
    joined by `;` with NO trailing `;` (`OtherInstanceMessageHandler::handle_message` skips `args[0]`).
    """
    resolved_files = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved_files:
        raise ValueError("file_paths must contain at least one model path")

    tokens = ["orca-slicer.exe", *resolved_files]
    escaped: list[str] = []
    for tok in tokens:
        s = (
            tok.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\r", "\\r")
            .replace("\n", "\\n")
        )
        escaped.append(f'"{s}"')
    return ";".join(escaped)


def _find_orca_mainframe_hwnd(target_pid: int | None = None) -> int | None:
    """Locate OrcaSlicer's `MainFrame` `wxWindowNR` `HWND` in `target_pid` (`os.getpid()` by default).

    Prefers `wxWindowNR` windows marked with OrcaSlicer's `Instance_Hash_Minor` or
    `Instance_Hash_Major` properties, falling back to a visible top-level `wxWindowNR` of that PID.
    """
    if sys.platform != "win32":
        return None

    from ctypes import wintypes

    pid = int(target_pid) if target_pid is not None else os.getpid()
    user32 = ctypes.windll.user32

    WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    enum_windows = user32.EnumWindows
    if not _is_mock_callable(enum_windows):
        enum_windows.argtypes = [WNDENUMPROC, wintypes.LPARAM]
        enum_windows.restype = wintypes.BOOL

    get_pid = user32.GetWindowThreadProcessId
    if not _is_mock_callable(get_pid):
        get_pid.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
        get_pid.restype = wintypes.DWORD

    get_class = user32.GetClassNameW
    if not _is_mock_callable(get_class):
        get_class.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
        get_class.restype = ctypes.c_int

    get_prop = user32.GetPropW
    if not _is_mock_callable(get_prop):
        get_prop.argtypes = [wintypes.HWND, wintypes.LPCWSTR]
        get_prop.restype = wintypes.HANDLE

    is_visible = user32.IsWindowVisible
    if not _is_mock_callable(is_visible):
        is_visible.argtypes = [wintypes.HWND]
        is_visible.restype = wintypes.BOOL

    get_parent = user32.GetParent
    if not _is_mock_callable(get_parent):
        get_parent.argtypes = [wintypes.HWND]
        get_parent.restype = wintypes.HWND

    hash_visible: list[int] = []
    hash_any: list[int] = []
    fallback_visible: list[int] = []

    def _enum_cb(hwnd: int, _lparam: int) -> bool:
        if not hwnd:
            return True
        win_pid = wintypes.DWORD(0)
        get_pid(hwnd, ctypes.byref(win_pid))
        if int(win_pid.value) != pid:
            return True

        cls_buf = ctypes.create_unicode_buffer(64)
        cls_len = get_class(hwnd, cls_buf, 64)
        if cls_len <= 0 or cls_buf.value != "wxWindowNR":
            return True

        minor = get_prop(hwnd, "Instance_Hash_Minor")
        major = get_prop(hwnd, "Instance_Hash_Major")
        vis = bool(is_visible(hwnd))
        hwnd_int = int(hwnd)

        if bool(minor) or bool(major):
            if vis:
                hash_visible.append(hwnd_int)
            else:
                hash_any.append(hwnd_int)
        elif vis and not get_parent(hwnd):
            fallback_visible.append(hwnd_int)
        return True

    cb_ref = WNDENUMPROC(_enum_cb)
    enum_windows(cb_ref, 0)

    if hash_visible:
        return hash_visible[0]
    if hash_any:
        return hash_any[0]
    if fallback_visible:
        return fallback_visible[0]
    return None


class _COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_size_t),
        ("cbData", ctypes.c_uint32),
        ("lpData", ctypes.c_void_p),
    ]


def _dispatch_copydata_to_hwnd(
    hwnd: int,
    payload_str: str,
    timeout_ms: int = 5000,
) -> tuple[bool, str]:
    """Send UTF-16LE `WM_COPYDATA` (`dwData = 1`) to `hwnd` via `SendMessageTimeoutW` (`0x0002`)."""
    if not hwnd or int(hwnd) <= 0:
        return (False, "OrcaSlicer MainFrame HWND not found")
    if not payload_str:
        return (False, "Empty WM_COPYDATA payload")
    if sys.platform != "win32":
        return (False, "WM_COPYDATA requires win32")

    from ctypes import wintypes

    wchar_buf = ctypes.create_unicode_buffer(payload_str)
    cds = _COPYDATASTRUCT(
        dwData=ORCA_OTHER_INSTANCE_DWDATA,
        cbData=ctypes.sizeof(wchar_buf),
        lpData=ctypes.cast(wchar_buf, ctypes.c_void_p),
    )
    result = ctypes.c_size_t(0)

    user32 = ctypes.windll.user32
    send_msg = user32.SendMessageTimeoutW
    if not _is_mock_callable(send_msg):
        send_msg.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            ctypes.c_void_p,
            wintypes.UINT,
            wintypes.UINT,
            ctypes.POINTER(ctypes.c_size_t),
        ]
        send_msg.restype = ctypes.c_size_t

    ret = send_msg(
        int(hwnd),
        WM_COPYDATA,
        0,
        ctypes.byref(cds),
        SMTO_ABORTIFHUNG,
        max(100, int(timeout_ms)),
        ctypes.byref(result),
    )
    if not ret:
        err = ctypes.windll.kernel32.GetLastError()
        return (False, f"SendMessageTimeoutW failed (GetLastError={err})")
    return (True, "ok")


def _dispatch_non_win32_plater_open(file_paths: Sequence[str | Path]) -> tuple[bool, str]:
    """Graceful macOS / Linux Plater open fallback when running outside Win32 (`WM_COPYDATA`)."""
    resolved = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved:
        return (False, "No model files to open")
    if not _is_native_orca_host():
        return (False, f"WM_COPYDATA requires win32 (platform={sys.platform})")
    try:
        import subprocess

        if sys.platform == "darwin":
            subprocess.Popen(
                ["open", "-a", "OrcaSlicer", *resolved],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return (True, "darwin_open_ok")
        # Linux / POSIX: try sibling `orca-slicer` binary with `--single-instance`, else `xdg-open`
        exe_dir = Path(sys.executable).resolve().parent
        for cand_bin in (exe_dir / "orca-slicer", exe_dir.parent / "orca-slicer", exe_dir.parent / "bin" / "orca-slicer"):
            if cand_bin.is_file():
                subprocess.Popen(
                    [str(cand_bin), "--single-instance", *resolved],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                return (True, "linux_single_instance_ok")
        subprocess.Popen(
            ["xdg-open", resolved[0]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return (True, "xdg_open_ok")
    except Exception as exc:
        return (False, f"Non-win32 Plater open fallback skipped: {exc}")


def _slugify_filename(name: str, fallback: str = "vaso") -> str:
    cleaned = re.sub(r"[^\w\-. ]+", "", str(name or "").strip(), flags=re.ASCII)
    cleaned = re.sub(r"\s+", "_", cleaned).strip("._-")
    if not cleaned:
        return fallback
    return cleaned[:64]


def _extract_first_float(val: Any, default: float) -> float:
    if val is None:
        return default
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        f = float(val)
        return f if f == f else default
    if isinstance(val, (list, tuple)):
        for item in val:
            res = _extract_first_float(item, float("nan"))
            if res == res:
                return res
        return default
    s = str(val).strip()
    if not s:
        return default
    m = re.search(r"[-+]?\d*\.?\d+", s)
    if not m:
        return default
    try:
        return float(m.group(0))
    except ValueError:
        return default


def _parse_bed_geometry(
    raw: Any,
    default_x: float = 220.0,
    default_y: float = 220.0,
) -> dict[str, Any]:
    """Parse OrcaSlicer `printable_area` / `bed_shape` polygon into bed dimensions and shape.

    Supports:
    - `['0x0', '220x0', '220x220', '0x220']`
    - `'0x0,220x0,220x220,0x220'` or semicolon-separated strings
    - `[[0, 0], [220, 0], [220, 220], [0, 220]]` or numpy arrays
    - `orca.host.Point` / `Pointf` objects exposing `.x` / `.y` or dicts `{'x': ..., 'y': ...}`
    - Circular / delta beds with `> 6` polygon vertices around origin or bed center
    """
    fallback = {
        "bed_x": float(default_x),
        "bed_y": float(default_y),
        "bed_shape": "rectangular",
        "bed_center": [round(float(default_x) * 0.5, 2), round(float(default_y) * 0.5, 2)],
    }
    if raw is None:
        return fallback

    xs: list[float] = []
    ys: list[float] = []

    tokens: list[Any]
    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return fallback
        if s.startswith("["):
            try:
                parsed = json.loads(s)
                tokens = parsed if isinstance(parsed, list) else [s]
            except Exception:
                tokens = re.split(r"[;,]+", s)
        else:
            tokens = re.split(r"[;,]+", s)
    elif isinstance(raw, Sequence) and not isinstance(raw, (bytes, bytearray)):
        tokens = list(raw)
    elif hasattr(raw, "__iter__"):
        try:
            tokens = list(raw)
        except Exception:
            return fallback
    else:
        return fallback

    for tok in tokens:
        if tok is None:
            continue
        if isinstance(tok, str):
            m = re.search(r"([-+]?\d*\.?\d+)\s*[xX:,]\s*([-+]?\d*\.?\d+)", tok.strip())
            if m:
                try:
                    xs.append(float(m.group(1)))
                    ys.append(float(m.group(2)))
                except ValueError:
                    continue
        elif isinstance(tok, dict):
            if "x" in tok and "y" in tok:
                try:
                    xs.append(float(tok["x"]))
                    ys.append(float(tok["y"]))
                except (TypeError, ValueError):
                    continue
        elif hasattr(tok, "x") and hasattr(tok, "y"):
            try:
                xv = tok.x() if callable(tok.x) else tok.x
                yv = tok.y() if callable(tok.y) else tok.y
                xs.append(float(xv))
                ys.append(float(yv))
            except Exception:
                continue
        elif hasattr(tok, "__len__") and hasattr(tok, "__getitem__"):
            try:
                if len(tok) >= 2:
                    xs.append(float(tok[0]))
                    ys.append(float(tok[1]))
            except Exception:
                continue

    if len(xs) >= 2 and len(ys) >= 2:
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        dx = max_x - min_x
        dy = max_y - min_y
        cx = 0.5 * (min_x + max_x)
        cy = 0.5 * (min_y + max_y)

        if dx >= 30.0 and dy >= 30.0:
            if len(xs) > 6:
                mean_x = sum(xs) / len(xs)
                mean_y = sum(ys) / len(ys)
                best_cx, best_cy = cx, cy
                best_radii = [math.hypot(x - cx, y - cy) for x, y in zip(xs, ys)]
                mean_radii = [math.hypot(x - mean_x, y - mean_y) for x, y in zip(xs, ys)]
                if (max(mean_radii) - min(mean_radii)) < (max(best_radii) - min(best_radii)):
                    best_cx, best_cy = mean_x, mean_y
                    best_radii = mean_radii

                r_max = max(best_radii)
                r_min = min(best_radii)
                if r_max >= 15.0 and (r_max - r_min) / r_max <= 0.12:
                    r_avg = sum(best_radii) / len(best_radii)
                    diam = round(2.0 * r_avg, 2)
                    if abs(diam - round(diam)) < 0.08:
                        diam = float(round(diam))
                    return {
                        "bed_x": float(diam),
                        "bed_y": float(diam),
                        "bed_shape": "circular",
                        "bed_center": [round(best_cx, 2), round(best_cy, 2)],
                    }

            bx = round(dx, 2)
            by = round(dy, 2)
            return {
                "bed_x": float(bx),
                "bed_y": float(by),
                "bed_shape": "rectangular",
                "bed_center": [round(cx, 2), round(cy, 2)],
            }

    return fallback


def _parse_printable_area(raw: Any, default_x: float = 220.0, default_y: float = 220.0) -> tuple[float, float]:
    """Parse OrcaSlicer `printable_area` into `(bed_x_mm, bed_y_mm)`."""
    geom = _parse_bed_geometry(raw, default_x=default_x, default_y=default_y)
    return (float(geom["bed_x"]), float(geom["bed_y"]))


def _parse_line_width(raw: Any, nozzle_mm: float, fallback_raw: Any = None) -> float:
    """Parse OrcaSlicer line width (`'0.42'`, `'105%'`, `'0'`, `['110%']`) relative to `nozzle_mm`."""
    default_lw = round(max(0.15, min(3.0, float(nozzle_mm) * 1.05)), 3)

    def _parse_single(candidate: Any) -> float | None:
        if candidate is None or isinstance(candidate, bool):
            return None
        if isinstance(candidate, (list, tuple)):
            return _parse_single(candidate[0] if candidate else None)
        s = str(candidate).strip()
        if not s:
            return None
        if s.endswith("%"):
            pct = _extract_first_float(s[:-1], 0.0)
            if pct > 10.0:
                return round(max(0.15, min(3.0, float(nozzle_mm) * (pct / 100.0))), 3)
            return None
        val = _extract_first_float(s, 0.0)
        if val <= 0.05:
            return None
        return round(max(0.15, min(3.0, val)), 3)

    parsed = _parse_single(raw)
    if parsed is not None:
        return parsed
    if fallback_raw is not None:
        parsed_fb = _parse_single(fallback_raw)
        if parsed_fb is not None:
            return parsed_fb
    return default_lw


def _resolve_attr_or_call(obj: Any, attr_name: str) -> Any:
    """Read an attribute on a pybind11/mock object whether exposed as a property or 0-arg method."""
    if obj is None:
        return None
    try:
        val = getattr(obj, attr_name, None)
    except Exception:
        return None
    if val is None:
        return None
    if callable(val):
        try:
            return val()
        except Exception:
            return None
    return val


def _extract_preset_name(obj: Any, fallback: str = "") -> str:
    if obj is None:
        return fallback
    if isinstance(obj, str):
        return obj.strip() or fallback
    if isinstance(obj, (list, tuple)):
        for item in obj:
            got = _extract_preset_name(item, "")
            if got:
                return got
        return fallback
    if isinstance(obj, dict):
        for k in ("name", "preset_name", "printer_name", "id"):
            v = obj.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
        return fallback
    for attr in ("name", "preset_name", "selected_preset_name"):
        val = _resolve_attr_or_call(obj, attr)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return fallback


def _preset_get_value(preset_obj: Any, key: str) -> Any:
    """Read `config_value(key)` directly from an `orca.host.Preset` instance if available."""
    if preset_obj is None or isinstance(preset_obj, (str, bytes, dict, list, tuple)):
        return None
    for method_name in ("config_value", "full_config_value", "get"):
        fn = getattr(preset_obj, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "" and val != []:
                    return val
            except Exception:
                continue
    return None


def _bundle_get_value(bundle: Any, key: str, preset_obj: Any = None) -> Any:
    from_preset = _preset_get_value(preset_obj, key)
    if from_preset is not None:
        return from_preset
    if bundle is None:
        return None
    for method_name in ("full_config_value", "config_value", "get"):
        fn = getattr(bundle, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "" and val != []:
                    return val
            except Exception:
                continue
    return None


def _detect_language(app_info: dict[str, Any]) -> str:
    raw = str(app_info.get("language") or app_info.get("lang") or "").strip().lower()
    if raw.startswith("en"):
        return "en"
    if raw.startswith("pt"):
        return "pt"
    if raw:
        return "en" if not raw.startswith("pt") else "pt"
    try:
        loc = (locale.getlocale()[0] or "").lower()
        if loc.startswith("en"):
            return "en"
        if loc.startswith("pt"):
            return "pt"
    except Exception:
        pass
    return "pt"


def _detect_theme(app_info: dict[str, Any]) -> str:
    theme_raw = str(app_info.get("theme") or app_info.get("color_mode") or "").strip().lower()
    if theme_raw == "light":
        return "light"
    if theme_raw == "dark":
        return "dark"
    if app_info.get("dark_mode") is False:
        return "light"
    return "dark"


def _make_execution_result_success(message: str) -> Any:
    exec_cls = getattr(orca, "ExecutionResult", None)
    if exec_cls is not None:
        success_fn = getattr(exec_cls, "success", None)
        if callable(success_fn):
            try:
                return success_fn(message)
            except TypeError:
                return success_fn(message, "")
        try:
            ok_code = getattr(getattr(orca, "PluginResult", None), "Success", 0)
            return exec_cls(ok_code, message, "")
        except Exception:
            pass
    return {"status": "Success", "message": message}


# ---------------------------------------------------------------------------
# Shared Studio Session & Message Router
# ---------------------------------------------------------------------------


class VaseStudioController:
    """Coordinates live host reading, mesh generation, exports, and Plater IPC."""

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._current_params: dict[str, Any] = normalize_params(DEFAULT_PARAMS)
        self._listeners: list[Callable[[dict[str, Any]], None]] = []
        self._last_plater_worker: threading.Thread | None = None
        self._last_plater_outcome: dict[str, Any] = {}

    @property
    def current_params(self) -> dict[str, Any]:
        with self._lock:
            return copy.deepcopy(self._current_params)

    def set_current_params(self, raw: dict[str, Any] | None) -> dict[str, Any]:
        norm = normalize_params(raw)
        with self._lock:
            self._current_params = norm
            return copy.deepcopy(norm)

    def get_presets_dir(self) -> Path:
        base = _resolve_storage_dir()
        target = base / "presets"
        try:
            target.mkdir(parents=True, exist_ok=True)
            return target
        except Exception:
            return base

    def get_export_dir(self) -> Path:
        base = _resolve_storage_dir()
        target = base / "exports"
        try:
            target.mkdir(parents=True, exist_ok=True)
            return target
        except Exception:
            fallback = Path.home() / "Documents" / "OrcaVaseStudio"
            try:
                fallback.mkdir(parents=True, exist_ok=True)
                return fallback
            except Exception:
                return base

    def read_host_context(self) -> dict[str, Any]:
        """Defensively inspect `orca.host.app_info()`, `orca.host.app_language()`, and `orca.host.preset_bundle()`."""
        app_info: dict[str, Any] = {}
        host = getattr(orca, "host", None)
        if host is not None:
            app_info_fn = getattr(host, "app_info", None)
            if callable(app_info_fn):
                try:
                    info = app_info_fn()
                    if isinstance(info, dict):
                        app_info = dict(info)
                except Exception:
                    app_info = {}

            # Official Wiki API (`orca.host.app_language()` -> e.g. "en_US", "pt_BR")
            if not str(app_info.get("language") or app_info.get("lang") or "").strip():
                app_lang_fn = getattr(host, "app_language", None)
                if callable(app_lang_fn):
                    try:
                        lang_val = app_lang_fn()
                        if isinstance(lang_val, str) and lang_val.strip():
                            app_info["language"] = lang_val.strip()
                    except Exception:
                        pass

        lang = _detect_language(app_info)
        theme = _detect_theme(app_info)
        theme_explicit = any(k in app_info for k in ("theme", "color_mode", "dark_mode"))
        orca_version = str(app_info.get("version") or "2.5.1")

        bundle = _resolve_attr_or_call(host, "preset_bundle") if host is not None else None

        printer_name = ""
        process_name = "0.20mm Standard"
        filament_name = "Generic PLA"

        active_printer_preset: Any = None
        active_process_preset: Any = None

        if bundle is not None:
            # 1. Inspect `bundle.printers` (`PresetCollection` on OrcaSlicer.dll v2.5.1)
            printers_col = _resolve_attr_or_call(bundle, "printers")
            if printers_col is not None:
                for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                    cand = _resolve_attr_or_call(printers_col, attr)
                    if cand is not None:
                        if active_printer_preset is None:
                            active_printer_preset = cand
                        got = _extract_preset_name(cand, "")
                        if got:
                            printer_name = got
                            break
                if not printer_name:
                    for attr in ("selected_preset_name", "get_selected_preset_name"):
                        got = _extract_preset_name(_resolve_attr_or_call(printers_col, attr), "")
                        if got:
                            printer_name = got
                            break

            # 2. Inspect `bundle.current_printer_preset` (property or 0-arg method)
            cur_pr = _resolve_attr_or_call(bundle, "current_printer_preset")
            if cur_pr is not None:
                if active_printer_preset is None:
                    active_printer_preset = cur_pr
                if not printer_name:
                    printer_name = _extract_preset_name(cur_pr, "")

            # 3. Inspect `bundle.prints` (`PresetCollection`) & `current_process_preset` / `current_print_preset`
            prints_col = _resolve_attr_or_call(bundle, "prints")
            if prints_col is not None:
                for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                    cand = _resolve_attr_or_call(prints_col, attr)
                    if cand is not None:
                        if active_process_preset is None:
                            active_process_preset = cand
                        got = _extract_preset_name(cand, "")
                        if got:
                            process_name = got
                            break

            for m in ("current_process_preset", "current_print_preset"):
                cand = _resolve_attr_or_call(bundle, m)
                if cand is not None:
                    if active_process_preset is None:
                        active_process_preset = cand
                    got = _extract_preset_name(cand, "")
                    if got:
                        process_name = got
                        break

            # 4. Inspect filament presets (`current_filament_preset_names`, `current_filament_presets`, `filaments`)
            got_fil = ""
            for m in ("current_filament_preset_names", "current_filament_presets"):
                fils = _resolve_attr_or_call(bundle, m)
                if isinstance(fils, (list, tuple)) and fils:
                    got_fil = _extract_preset_name(fils[0], "")
                    if got_fil:
                        filament_name = got_fil
                        break
            if not got_fil:
                fil_col = _resolve_attr_or_call(bundle, "filaments")
                if fil_col is not None:
                    for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                        got_fil = _extract_preset_name(_resolve_attr_or_call(fil_col, attr), "")
                        if got_fil:
                            filament_name = got_fil
                            break

            # 5. Fallback preset IDs from resolved config keys
            if not printer_name:
                for key_id in ("printer_settings_id", "printer_model"):
                    p_id = _bundle_get_value(bundle, key_id, active_printer_preset)
                    got = _extract_preset_name(p_id, "")
                    if got:
                        printer_name = got
                        break

            if process_name == "0.20mm Standard":
                pr_id = _bundle_get_value(bundle, "print_settings_id", active_process_preset)
                got_pr = _extract_preset_name(pr_id, "")
                if got_pr:
                    process_name = got_pr

        # Optional fallback to `orca.host.selected_printer` if bundle had no printer name
        if not printer_name and host is not None:
            sel_pr = _resolve_attr_or_call(host, "selected_printer")
            printer_name = _extract_preset_name(sel_pr, "")

        if not printer_name:
            printer_name = "Default Printer"

        raw_area = _bundle_get_value(bundle, "printable_area", active_printer_preset)
        if raw_area is None or raw_area == "" or raw_area == []:
            raw_area = _bundle_get_value(bundle, "bed_shape", active_printer_preset)

        bed_geom = _parse_bed_geometry(raw_area, default_x=220.0, default_y=220.0)
        bed_x = float(bed_geom["bed_x"])
        bed_y = float(bed_geom["bed_y"])
        bed_shape = str(bed_geom["bed_shape"])
        bed_center = list(bed_geom["bed_center"])

        max_z = max(
            50.0,
            min(
                1000.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "printable_height", active_printer_preset),
                    250.0,
                ),
            ),
        )
        nozzle_mm = max(
            0.15,
            min(
                2.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "nozzle_diameter", active_printer_preset),
                    0.4,
                ),
            ),
        )
        layer_height_mm = max(
            0.04,
            min(
                1.2,
                _extract_first_float(
                    _bundle_get_value(bundle, "layer_height", active_process_preset),
                    0.2,
                ),
            ),
        )
        line_width_mm = _parse_line_width(
            _bundle_get_value(bundle, "outer_wall_line_width", active_process_preset),
            nozzle_mm=nozzle_mm,
            fallback_raw=_bundle_get_value(bundle, "line_width", active_process_preset),
        )
        top_shell_layers = int(
            round(
                _extract_first_float(
                    _bundle_get_value(bundle, "top_shell_layers", active_process_preset),
                    4.0,
                )
            )
        )
        raw_infill = _bundle_get_value(bundle, "sparse_infill_density", active_process_preset)
        if isinstance(raw_infill, (list, tuple)):
            raw_infill = raw_infill[0] if raw_infill else "15%"
        sparse_infill_density = str(raw_infill if raw_infill is not None else "15%").strip() or "15%"

        return {
            "lang": lang,
            "theme": theme,
            "theme_explicit": theme_explicit,
            "orca_version": orca_version,
            "printer_name": printer_name,
            "process_name": process_name,
            "filament_name": filament_name,
            "bed_x": float(bed_x),
            "bed_y": float(bed_y),
            "bed_shape": bed_shape,
            "bed_center": bed_center,
            "max_z": float(max_z),
            "nozzle_mm": float(nozzle_mm),
            "layer_height_mm": float(layer_height_mm),
            "line_width_mm": float(line_width_mm),
            "top_shell_layers": top_shell_layers,
            "sparse_infill_density": sparse_infill_density,
        }

    def read_full_host_config_snapshot(self, host_ctx: dict[str, Any] | None = None) -> dict[str, Any]:
        """Collect full resolved `project_settings` snapshot from `preset_bundle()` for `.3mf` export."""
        ctx = dict(host_ctx) if host_ctx is not None else self.read_host_context()
        project_settings: dict[str, Any] = {}

        host = getattr(orca, "host", None)
        bundle = None
        if host is not None:
            bundle_fn = getattr(host, "preset_bundle", None)
            if callable(bundle_fn):
                try:
                    bundle = bundle_fn()
                except Exception:
                    bundle = None

        if bundle is not None:
            keys_fn = getattr(bundle, "full_config_keys", None)
            val_fn = getattr(bundle, "full_config_value", None) or getattr(bundle, "config_value", None)
            if callable(keys_fn) and callable(val_fn):
                try:
                    keys = keys_fn()
                    if isinstance(keys, (list, tuple, set)):
                        for k in keys:
                            ks = str(k)
                            if not ks:
                                continue
                            try:
                                v = val_fn(ks)
                                if v is not None:
                                    project_settings[ks] = v
                            except Exception:
                                continue
                except Exception:
                    pass

        ctx["project_settings"] = project_settings
        return ctx

    def build_printer_payload(self, host_ctx: dict[str, Any] | None = None) -> dict[str, Any]:
        """Construct the UI-facing `printer` metadata dictionary from `host_ctx`."""
        ctx = host_ctx if isinstance(host_ctx, dict) else self.read_host_context()
        return {
            "name": ctx["printer_name"],
            "process_name": ctx["process_name"],
            "filament_name": ctx["filament_name"],
            "orca_version": ctx["orca_version"],
            "bed_x": ctx["bed_x"],
            "bed_y": ctx["bed_y"],
            "bed_shape": ctx.get("bed_shape", "rectangular"),
            "bed_center": ctx.get("bed_center", [round(ctx["bed_x"] * 0.5, 2), round(ctx["bed_y"] * 0.5, 2)]),
            "max_z": ctx["max_z"],
            "nozzle_mm": ctx["nozzle_mm"],
            "layer_height_mm": ctx["layer_height_mm"],
            "line_width_mm": ctx["line_width_mm"],
        }

    def build_initial_context(self, mode: str = "page") -> dict[str, Any]:
        host_ctx = self.read_host_context()
        presets_dir = self.get_presets_dir()
        export_dir = self.get_export_dir()
        params = self.current_params
        return {
            "mode": mode,
            "lang": host_ctx["lang"],
            "theme": host_ctx["theme"],
            "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
            "printer": self.build_printer_payload(host_ctx),
            "builtin_presets": BUILTIN_PRESETS,
            "user_presets": load_user_presets(presets_dir),
            "params": params,
            "export_dir": str(export_dir),
        }

    def _prepare_effective_vase_params(
        self,
        params: dict[str, Any],
        *,
        is_stl_export: bool,
        include_saucer: bool,
    ) -> dict[str, Any]:
        """Ensure `.STL` exports (when `stl_always_open_hollow` is True) and Vase+Saucer combos
        never generate a sealed top-capped Spiral Vase solid block.
        """
        effective = copy.deepcopy(params)
        if str(effective.get("print_mode", "shelled_hollow")) == "spiral_vase":
            force_open_hollow = bool(include_saucer) or (
                bool(is_stl_export) and bool(effective.get("stl_always_open_hollow", True))
            )
            if force_open_hollow:
                effective["print_mode"] = "shelled_hollow"
                effective["wall_thickness_mm"] = max(
                    0.8,
                    float(effective.get("wall_thickness_mm", 2.4)),
                )
                effective["bottom_thickness_mm"] = max(
                    1.0,
                    float(effective.get("bottom_thickness_mm", 3.2)),
                )
        return effective

    def _compute_process_preset_updates(
        self,
        params: dict[str, Any],
        host_ctx: dict[str, Any],
        include_saucer: bool,
    ) -> dict[str, str]:
        """Build key/value strings for `orca.host.preset.process.begin_update()`."""
        print_mode = str(params.get("print_mode", "shelled_hollow"))
        use_spiral = (print_mode == "spiral_vase") and (not include_saucer)

        if use_spiral:
            smooth = bool(params.get("spiral_smooth", True))
            bottom_layers = max(2, min(15, int(params.get("spiral_bottom_layers", 5))))
            spiral_lw = max(0.40, min(1.20, float(params.get("spiral_line_width_mm", 0.65))))
            return {
                "spiral_mode": "1",
                "spiral_mode_smooth": "1" if smooth else "0",
                "wall_loops": "1",
                "top_shell_layers": "0",
                "sparse_infill_density": "0%",
                "bottom_shell_layers": str(bottom_layers),
                "outer_wall_line_width": f"{spiral_lw:.2f}",
            }

        # Shelled hollow mode OR multi-object plate (vase + saucer)
        lw = max(0.25, float(host_ctx.get("line_width_mm", 0.42)))
        lh = max(0.08, float(host_ctx.get("layer_height_mm", 0.20)))

        wall_mm = max(0.8, float(params.get("wall_thickness_mm", 2.4)))
        bot_mm = max(1.0, float(params.get("bottom_thickness_mm", 3.2)))
        wall_loops = max(2, min(15, int(round(wall_mm / (2.0 * lw)))))
        bottom_layers = max(3, min(125, int(round(bot_mm / lh))))

        updates: dict[str, str] = {
            "spiral_mode": "0",
            "spiral_mode_smooth": "0",
            "wall_loops": str(wall_loops),
            "bottom_shell_layers": str(bottom_layers),
        }
        if int(host_ctx.get("top_shell_layers", 4)) <= 0:
            updates["top_shell_layers"] = "4"
        if str(host_ctx.get("sparse_infill_density", "15%")).strip() in ("", "0", "0%"):
            updates["sparse_infill_density"] = "15%"
        return updates

    def _apply_process_presets(self, updates: dict[str, str]) -> dict[str, Any]:
        """Apply process preset changes on the calling background worker thread.

        NEVER call `orca.host.preset.process.begin_update()` on the wxWidgets UI thread!
        """
        outcome: dict[str, Any] = {"applied": False, "error": None}
        if not updates:
            return outcome
        try:
            host = getattr(orca, "host", None)
            preset_ns = getattr(host, "preset", None) if host is not None else None
            process_ed = getattr(preset_ns, "process", None) if preset_ns is not None else None
            begin_fn = getattr(process_ed, "begin_update", None) if process_ed is not None else None
            if not callable(begin_fn):
                return outcome

            tx = begin_fn()
            if tx is None:
                return outcome

            staged_any = False
            for key, val in updates.items():
                try:
                    tx.set(str(key), str(val))
                    staged_any = True
                except Exception:
                    continue

            if staged_any:
                commit_fn = getattr(tx, "commit", None)
                if callable(commit_fn):
                    commit_fn()
                outcome["applied"] = True
        except Exception as exc:
            outcome["error"] = str(exc)
        return outcome

    def _apply_process_presets_async(
        self,
        updates: dict[str, str],
        delay_sec: float = 0.0,
    ) -> tuple[threading.Thread, dict[str, Any]]:
        """Apply process preset changes strictly on a background daemon thread."""
        outcome: dict[str, Any] = {"applied": False, "error": None}

        def _worker() -> None:
            if delay_sec > 0.0:
                time.sleep(delay_sec)
            res = self._apply_process_presets(updates)
            outcome.update(res)

        thread = threading.Thread(
            target=_worker,
            name="OrcaVaseStudio-PresetUpdater",
            daemon=True,
        )
        thread.start()
        return thread, outcome

    def _write_stl_resilient(self, directory: Path, stem: str, mesh: Any, header: str) -> Path:
        target = directory / f"{stem}.stl"
        try:
            return Path(write_binary_stl(target, mesh, header_name=header))
        except PermissionError:
            alt = directory / f"{stem}_{int(time.time() * 1000)}.stl"
            return Path(write_binary_stl(alt, mesh, header_name=header))

    def _notify_host_toast(
        self,
        text: str,
        level_name: str = "RegularNotificationLevel",
    ) -> None:
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        push_fn = getattr(ui, "push_notification", None) if ui is not None else None
        if not callable(push_fn):
            return
        lvl_enum = getattr(ui, "NotificationLevel", None)
        level = None
        if lvl_enum is not None:
            level = getattr(
                lvl_enum,
                level_name,
                getattr(lvl_enum, "RegularNotificationLevel", None),
            )
        try:
            if level is not None:
                try:
                    push_fn(level, text)
                    return
                except TypeError:
                    push_fn(text)
                    return
            push_fn(text)
        except Exception:
            pass

    def handle_message(
        self,
        raw_data: Any,
        send_fn: Callable[[dict[str, Any]], None],
        default_mode: str = "page",
    ) -> None:
        """Process incoming WebView2 bridge payload and send responses via `send_fn`."""
        try:
            msg = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
        except Exception as exc:
            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": "parse_error",
                    "message": f"Invalid JSON message: {exc}",
                    "paths": [],
                }
            )
            return

        if not isinstance(msg, dict):
            return

        msg_type = str(msg.get("type") or "").strip()

        try:
            if msg_type == "ready":
                mode = str(msg.get("mode") or default_mode)
                init_ctx = self.build_initial_context(mode=mode)
                host_ctx = self.read_host_context()
                params = init_ctx["params"]
                vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                report = analyze_printability(vase_mesh, params, host_context=host_ctx)

                send_fn({"type": "init_state", **init_ctx})
                send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "sync_printer":
                host_ctx = self.read_host_context()
                printer_info = self.build_printer_payload(host_ctx)
                send_fn(
                    {
                        "type": "printer_updated",
                        "printer": printer_info,
                        "lang": host_ctx["lang"],
                        "theme": host_ctx["theme"],
                        "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                    }
                )
                raw_params = msg.get("params")
                if isinstance(raw_params, dict):
                    params = self.set_current_params(raw_params)
                    vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                    report = analyze_printability(vase_mesh, params, host_context=host_ctx)
                    send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "analyze":
                params = self.set_current_params(msg.get("params") or self.current_params)
                host_ctx = self.read_host_context()
                vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                report = analyze_printability(vase_mesh, params, host_context=host_ctx)
                send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "randomize":
                raw_seed = msg.get("seed")
                seed_val: int | None = None
                if raw_seed is not None and raw_seed != "":
                    try:
                        seed_val = int(raw_seed)
                    except (TypeError, ValueError):
                        seed_val = None
                base_params = normalize_params(msg.get("params") or self.current_params)
                randomized = generate_random_printable_params(seed=seed_val, current_params=base_params)
                params = self.set_current_params(randomized)
                send_fn(
                    {
                        "type": "params_updated",
                        "params": params,
                        "source": "randomize",
                    }
                )
                return

            if msg_type == "preset_save":
                params = self.set_current_params(msg.get("params") or self.current_params)
                preset_name = str(msg.get("name") or params.get("name") or "Meu Vaso").strip() or "Meu Vaso"
                preset_id = msg.get("id") or msg.get("preset_id")
                preset_id_str = str(preset_id).strip() if preset_id else None
                user_presets = save_user_preset(
                    self.get_presets_dir(),
                    name=preset_name,
                    params=params,
                    preset_id=preset_id_str,
                )
                send_fn(
                    {
                        "type": "presets_updated",
                        "user_presets": user_presets,
                    }
                )
                return

            if msg_type == "preset_delete":
                preset_id = str(msg.get("id") or msg.get("preset_id") or "").strip()
                user_presets = delete_user_preset(self.get_presets_dir(), preset_id=preset_id)
                send_fn(
                    {
                        "type": "presets_updated",
                        "user_presets": user_presets,
                    }
                )
                return

            if msg_type == "export_file":
                params = self.set_current_params(msg.get("params") or self.current_params)
                fmt = str(msg.get("format") or "3mf").strip().lower().lstrip(".")
                if fmt not in ("3mf", "stl"):
                    fmt = "3mf"
                include_saucer = bool(msg.get("include_saucer", False))

                host_ctx = self.read_host_context()
                lang = host_ctx["lang"]
                export_dir = self.get_export_dir()

                effective_params = self._prepare_effective_vase_params(
                    params,
                    is_stl_export=(fmt == "stl"),
                    include_saucer=include_saucer,
                )
                vase_mesh = generate_vase_mesh(
                    effective_params,
                    layer_height_mm=host_ctx["layer_height_mm"],
                )
                report = analyze_printability(vase_mesh, effective_params, host_context=host_ctx)

                raw_filename = str(msg.get("filename") or "").strip()
                if raw_filename:
                    base_stem = _slugify_filename(Path(raw_filename).stem, fallback="vaso")
                else:
                    base_stem = _slugify_filename(params.get("name", "vaso"), fallback="vaso")

                paths: list[str] = []
                if fmt == "3mf":
                    target_3mf = export_dir / f"{base_stem}.3mf"
                    host_cfg = self.read_full_host_config_snapshot(host_ctx)
                    cx = host_ctx["bed_x"] / 2.0
                    cy = host_ctx["bed_y"] / 2.0

                    vase_label = str(params.get("name") or ("Vaso" if lang == "pt" else "Vase"))

                    if include_saucer:
                        saucer_mesh = generate_saucer_mesh(effective_params)
                        vase_rx = float(vase_mesh.bounds_mm["size"][0]) / 2.0
                        saucer_rx = float(saucer_mesh.bounds_mm["size"][0]) / 2.0
                        gap_mm = 10.0
                        total_w = 2.0 * vase_rx + gap_mm + 2.0 * saucer_rx
                        vase_pos = (round(cx - total_w / 2.0 + vase_rx, 2), round(cy, 2), 0.0)
                        saucer_pos = (round(cx + total_w / 2.0 - saucer_rx, 2), round(cy, 2), 0.0)
                        saucer_label = "Prato" if lang == "pt" else "Saucer"
                        items = [
                            (vase_label, vase_mesh, vase_pos),
                            (saucer_label, saucer_mesh, saucer_pos),
                        ]
                    else:
                        items = [(vase_label, vase_mesh, (round(cx, 2), round(cy, 2), 0.0))]

                    written_3mf = Path(
                        write_orca_3mf(target_3mf, items, effective_params, host_config=host_cfg)
                    )
                    paths.append(str(written_3mf))
                else:
                    vase_stl = self._write_stl_resilient(
                        export_dir,
                        base_stem,
                        vase_mesh,
                        header=f"OrcaVaseStudio:{base_stem}",
                    )
                    paths.append(str(vase_stl))
                    if include_saucer:
                        saucer_mesh = generate_saucer_mesh(effective_params)
                        saucer_suffix = "prato" if lang == "pt" else "saucer"
                        saucer_stl = self._write_stl_resilient(
                            export_dir,
                            f"{base_stem}_{saucer_suffix}",
                            saucer_mesh,
                            header=f"OrcaVaseStudio:{base_stem}_{saucer_suffix}",
                        )
                        paths.append(str(saucer_stl))

                open_mouth_note = ""
                if (
                    fmt == "stl"
                    and params.get("print_mode") == "spiral_vase"
                    and effective_params.get("print_mode") == "shelled_hollow"
                ):
                    open_mouth_note = (
                        f" (boca aberta oca {effective_params['wall_thickness_mm']:.1f} mm)"
                        if lang == "pt"
                        else f" (open-mouthed {effective_params['wall_thickness_mm']:.1f} mm shell)"
                    )

                ok_msg = (
                    f"Arquivo exportado com sucesso: {Path(paths[0]).name}{open_mouth_note}"
                    if lang == "pt"
                    else f"Exported successfully: {Path(paths[0]).name}{open_mouth_note}"
                )
                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "export_file",
                        "format": fmt,
                        "path": paths[0],
                        "paths": paths,
                        "message": ok_msg,
                        "report": report,
                    }
                )
                return

            if msg_type == "send_to_plater":
                params = self.set_current_params(msg.get("params") or self.current_params)
                include_saucer = bool(msg.get("include_saucer", False))
                auto_cfg = bool(params.get("auto_configure_slicer", True))

                host_ctx = self.read_host_context()
                lang = host_ctx["lang"]
                export_dir = self.get_export_dir()

                effective_params = self._prepare_effective_vase_params(
                    params,
                    is_stl_export=False,
                    include_saucer=include_saucer,
                )
                vase_mesh = generate_vase_mesh(
                    effective_params,
                    layer_height_mm=host_ctx["layer_height_mm"],
                )
                report = analyze_printability(vase_mesh, effective_params, host_context=host_ctx)

                base_stem = _slugify_filename(params.get("name", "vaso"), fallback="vaso")
                vase_stl = self._write_stl_resilient(
                    export_dir,
                    f"{base_stem}_plater",
                    vase_mesh,
                    header=f"OrcaVaseStudio:{base_stem}",
                )
                stl_paths = [str(vase_stl)]

                if include_saucer:
                    saucer_mesh = generate_saucer_mesh(effective_params)
                    saucer_suffix = "prato" if lang == "pt" else "saucer"
                    saucer_stl = self._write_stl_resilient(
                        export_dir,
                        f"{base_stem}_{saucer_suffix}_plater",
                        saucer_mesh,
                        header=f"OrcaVaseStudio:{base_stem}_{saucer_suffix}",
                    )
                    stl_paths.append(str(saucer_stl))

                copydata_payload = _format_other_instance_payload(stl_paths)
                updates: dict[str, str] = {}
                if auto_cfg:
                    updates = self._compute_process_preset_updates(
                        params=effective_params,
                        host_ctx=host_ctx,
                        include_saucer=include_saucer,
                    )

                native_host = _is_native_orca_host()
                copydata_delay = 0.06 if native_host else 0.01
                preset_delay = 0.45 if native_host else 0.01
                dispatch_outcome: dict[str, Any] = {
                    "ipc_ok": False,
                    "ipc_message": "",
                    "hwnd": None,
                    "thread_id": None,
                    "preset_applied": False,
                    "preset_error": None,
                }
                self._last_plater_outcome = dispatch_outcome

                def _plater_bg_worker() -> None:
                    dispatch_outcome["thread_id"] = threading.get_ident()
                    if copydata_delay > 0.0:
                        time.sleep(copydata_delay)

                    hwnd = _find_orca_mainframe_hwnd()
                    dispatch_outcome["hwnd"] = hwnd
                    ipc_ok, ipc_msg = _dispatch_copydata_to_hwnd(hwnd or 0, copydata_payload)
                    if not ipc_ok and sys.platform != "win32":
                        ipc_ok, ipc_msg = _dispatch_non_win32_plater_open(stl_paths)
                    dispatch_outcome["ipc_ok"] = ipc_ok
                    dispatch_outcome["ipc_message"] = ipc_msg

                    if auto_cfg and updates:
                        if preset_delay > 0.0:
                            time.sleep(preset_delay)
                        preset_res = self._apply_process_presets(updates)
                        dispatch_outcome["preset_applied"] = bool(preset_res.get("applied", False))
                        dispatch_outcome["preset_error"] = preset_res.get("error")

                worker = threading.Thread(
                    target=_plater_bg_worker,
                    name="OrcaVaseStudio-PlaterDispatch",
                    daemon=True,
                )
                self._last_plater_worker = worker
                worker.start()

                if not native_host:
                    # Safe to join in standalone/test harness; NEVER join on native wxWidgets UI thread!
                    worker.join(timeout=4.0)
                    slicer_configured = bool(dispatch_outcome.get("preset_applied", False))
                else:
                    process_ed = getattr(
                        getattr(getattr(orca, "host", None), "preset", None),
                        "process",
                        None,
                    )
                    slicer_configured = bool(auto_cfg and hasattr(process_ed, "begin_update"))

                saucer_spiral_note = ""
                if include_saucer and params.get("print_mode") == "spiral_vase":
                    saucer_spiral_note = (
                        " (Convertido para Vaso Oco Aberto para fatiar vaso + prato juntos.)"
                        if lang == "pt"
                        else " (Converted to open hollow shell to slice vase + saucer together.)"
                    )

                msg_text = (
                    f"Enviado para a mesa do OrcaSlicer ({len(stl_paths)} objeto(s)).{saucer_spiral_note}"
                    if lang == "pt"
                    else f"Sent to OrcaSlicer Plater ({len(stl_paths)} object(s)).{saucer_spiral_note}"
                )
                self._notify_host_toast(msg_text)

                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "send_to_plater",
                        "path": stl_paths[0],
                        "paths": stl_paths,
                        "message": msg_text,
                        "report": report,
                        "slicer_configured": slicer_configured,
                    }
                )
                return

            if msg_type == "open_exports_folder":
                export_dir = self.get_export_dir()
                lang = self.read_host_context()["lang"]
                startfile_fn = getattr(os, "startfile", None)
                if callable(startfile_fn) and (_is_native_orca_host() or _is_mock_callable(startfile_fn)):
                    try:
                        startfile_fn(str(export_dir))
                    except Exception:
                        pass
                elif sys.platform != "win32" and _is_native_orca_host():
                    try:
                        import subprocess

                        opener = "open" if sys.platform == "darwin" else "xdg-open"
                        subprocess.Popen(
                            [opener, str(export_dir)],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                        )
                    except Exception:
                        pass

                msg_text = (
                    f"Pasta de exportação: {export_dir}"
                    if lang == "pt"
                    else f"Exports folder: {export_dir}"
                )
                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "open_exports_folder",
                        "path": str(export_dir),
                        "paths": [str(export_dir)],
                        "message": msg_text,
                    }
                )
                return

            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": msg_type or "unknown",
                    "message": f"Unsupported message type: {msg_type!r}",
                    "paths": [],
                }
            )
        except Exception as exc:
            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": msg_type or "error",
                    "message": str(exc),
                    "paths": [],
                }
            )


_SHARED_CONTROLLER = VaseStudioController()

_SYNC_LIFECYCLE_EVENT_NAMES: frozenset[str] = frozenset(
    {"PresetSelected", "PresetSaved", "NewProject", "ProjectOpened"}
)
_VALID_DOCK_SIDES: frozenset[str] = frozenset({"left", "right", "bottom", "float"})


def _is_sync_lifecycle_event(event: Any) -> bool:
    """Match `orca.LifecycleEvent` enum values or names for preset/project changes."""
    ev_cls = getattr(orca, "LifecycleEvent", None)
    if ev_cls is not None:
        for nm in _SYNC_LIFECYCLE_EVENT_NAMES:
            cand = getattr(ev_cls, nm, None)
            if cand is not None and event == cand:
                return True
    ev_name = str(getattr(event, "name", event) or "")
    return any(k in ev_name for k in _SYNC_LIFECYCLE_EVENT_NAMES)


def _read_capability_config(cap: Any) -> dict[str, Any]:
    """Read `PythonPluginBase.get_config()` JSON string merged over `get_default_config()`."""
    defaults: dict[str, Any] = {}
    def_fn = getattr(cap, "get_default_config", None)
    if callable(def_fn):
        try:
            got_def = def_fn()
            if isinstance(got_def, dict):
                defaults = dict(got_def)
        except Exception:
            defaults = {}

    get_fn = getattr(cap, "get_config", None)
    if not callable(get_fn):
        return defaults
    try:
        raw = get_fn()
        if isinstance(raw, str) and raw.strip():
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                merged = dict(defaults)
                merged.update(parsed)
                return merged
        elif isinstance(raw, dict):
            merged = dict(defaults)
            merged.update(raw)
            return merged
    except Exception:
        pass
    return defaults


def _apply_capability_config_to_controller(
    controller: VaseStudioController,
    cfg: dict[str, Any],
) -> None:
    """Apply user-saved capability configuration overrides onto controller parameters."""
    if not cfg:
        return
    updates: dict[str, Any] = {}
    mode_val = cfg.get("default_print_mode")
    if mode_val in ("shelled_hollow", "spiral_vase"):
        updates["print_mode"] = mode_val
    if isinstance(cfg.get("auto_configure_slicer"), bool):
        updates["auto_configure_slicer"] = cfg["auto_configure_slicer"]
    if isinstance(cfg.get("stl_always_open_hollow"), bool):
        updates["stl_always_open_hollow"] = cfg["stl_always_open_hollow"]
    if updates:
        cur = controller.current_params
        cur.update(updates)
        controller.set_current_params(cur)


# ---------------------------------------------------------------------------
# OrcaSlicer Plugin Capabilities (Top-Bar Page + Docked Side Panel)
# ---------------------------------------------------------------------------


class VaseStudioPageCapability(orca.pages.PagesPluginCapabilityBase):
    """Full-screen top-bar tab (`Gerador de Vasos`) beside Prepare / Preview / Device."""

    def __init__(self, controller: VaseStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Gerador de Vasos"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "default_print_mode": "shelled_hollow",
            "auto_configure_slicer": True,
            "stl_always_open_hollow": True,
        }

    def on_load(self) -> None:
        _apply_capability_config_to_controller(
            self._controller,
            _read_capability_config(self),
        )

    def get_icon(self) -> str:
        storage_dir = _resolve_storage_dir(in_callback=True)
        existing_candidates: list[Path] = []
        try:
            existing_candidates.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        existing_candidates.extend(
            [
                storage_dir / "icon.svg",
                _default_installed_plugin_dir() / "icon.svg",
            ]
        )
        for cand in existing_candidates:
            try:
                if cand.is_file() and cand.stat().st_size > 0:
                    return str(cand)
            except Exception:
                continue

        # Auto-materialize embedded `icon.svg` when user side-loaded only `orca_vase_generator.py`
        write_targets: list[Path] = [
            storage_dir / "icon.svg",
            _default_plugin_data_dir() / "icon.svg",
        ]
        try:
            write_targets.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        write_targets.append(Path.home() / "Documents" / "OrcaVaseStudio" / "icon.svg")

        seen_dirs: set[str] = set()
        for target in write_targets:
            key = str(target)
            if key in seen_dirs:
                continue
            seen_dirs.add(key)
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                with open(target, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(ICON_SVG_CONTENT)
                if target.is_file() and target.stat().st_size > 0:
                    return str(target)
            except Exception:
                continue
        return ""

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="page")
        return get_studio_html(mode="page", initial_context=initial_ctx)

    def post_message(self, data: Any) -> None:
        super_post = getattr(super(), "post_message", None)
        if callable(super_post):
            super_post(data)

    def on_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self.post_message,
            default_mode="page",
        )

    def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
        """Push live `printer_updated` + `analysis_result` whenever OrcaSlicer switches presets or projects."""
        if not _is_sync_lifecycle_event(event):
            return
        try:
            host_ctx = self._controller.read_host_context()
            printer_info = self._controller.build_printer_payload(host_ctx)
            self.post_message(
                {
                    "type": "printer_updated",
                    "printer": printer_info,
                    "lang": host_ctx["lang"],
                    "theme": host_ctx["theme"],
                    "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                }
            )
            params = self._controller.current_params
            vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
            report = analyze_printability(vase_mesh, params, host_context=host_ctx)
            self.post_message({"type": "analysis_result", "report": report})
        except Exception:
            pass


class VaseStudioDockCapability(orca.script.ScriptPluginCapabilityBase):
    """Opens/shows a docked right-hand Vase Studio panel directly beside the 3D Plater."""

    _active_panel: Any = None
    _panel_lock = threading.RLock()

    def __init__(self, controller: VaseStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Orca Vase Studio - Painel Lateral"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "dock": "right",
            "width": 420,
            "height": 780,
            "auto_configure_slicer": True,
            "stl_always_open_hollow": True,
        }

    def on_load(self) -> None:
        _apply_capability_config_to_controller(
            self._controller,
            _read_capability_config(self),
        )

    def on_unload(self) -> None:
        with self._panel_lock:
            VaseStudioDockCapability._active_panel = None

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="dock")
        return get_studio_html(mode="dock", initial_context=initial_ctx)

    def _post_to_panel(self, payload: dict[str, Any]) -> None:
        with self._panel_lock:
            panel = VaseStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            is_open_fn = getattr(panel, "is_open", None)
            if callable(is_open_fn) and not is_open_fn():
                return
            post_fn = getattr(panel, "post", None)
            if callable(post_fn):
                post_fn(payload)
        except Exception:
            pass

    def _on_panel_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self._post_to_panel,
            default_mode="dock",
        )

    def _on_panel_close(self) -> None:
        with self._panel_lock:
            VaseStudioDockCapability._active_panel = None

    def on_message(self, data: Any) -> None:
        """Direct message entry point for testing or programmatic invocation."""
        self._on_panel_message(data)

    def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
        """Keep any open docked side panel synced when OrcaSlicer switches presets or projects."""
        if not _is_sync_lifecycle_event(event):
            return
        with self._panel_lock:
            panel = VaseStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            host_ctx = self._controller.read_host_context()
            printer_info = self._controller.build_printer_payload(host_ctx)
            self._post_to_panel(
                {
                    "type": "printer_updated",
                    "printer": printer_info,
                    "lang": host_ctx["lang"],
                    "theme": host_ctx["theme"],
                    "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                }
            )
            params = self._controller.current_params
            vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
            report = analyze_printability(vase_mesh, params, host_context=host_ctx)
            self._post_to_panel({"type": "analysis_result", "report": report})
        except Exception:
            pass

    def execute(self) -> Any:
        """Open or focus the docked Vase Studio panel beside the 3D Plater.

        Safe whether invoked on the main/UI thread (documented Wiki contract) or on
        `ScriptAsyncRuntime`'s background worker (`OrcaSlicer.dll` v2.5.1), as
        `orca.host.ui.create_dock_panel` marshals panel creation onto the UI thread.
        """
        cfg = _read_capability_config(self)
        _apply_capability_config_to_controller(self._controller, cfg)
        dock_side = str(cfg.get("dock") or "right").strip().lower()
        if dock_side not in _VALID_DOCK_SIDES:
            dock_side = "right"
        dock_w = max(280, min(960, int(_extract_first_float(cfg.get("width"), 420.0))))
        dock_h = max(360, min(1600, int(_extract_first_float(cfg.get("height"), 780.0))))

        with self._panel_lock:
            existing = VaseStudioDockCapability._active_panel

        if existing is not None:
            try:
                is_open_fn = getattr(existing, "is_open", None)
                if not callable(is_open_fn) or is_open_fn():
                    show_fn = getattr(existing, "show", None)
                    if callable(show_fn):
                        show_fn()
                    init_ctx = self._controller.build_initial_context(mode="dock")
                    self._post_to_panel({"type": "init_state", **init_ctx})
                    return _make_execution_result_success("Painel lateral Orca Vase Studio exibido.")
            except Exception:
                with self._panel_lock:
                    VaseStudioDockCapability._active_panel = None

        html = self.get_ui()
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        create_dock_fn = getattr(ui, "create_dock_panel", None) if ui is not None else None

        if callable(create_dock_fn):
            panel = create_dock_fn(
                html,
                title="Orca Vase Studio",
                width=dock_w,
                height=dock_h,
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
                dock=dock_side,
            )
            with self._panel_lock:
                VaseStudioDockCapability._active_panel = panel
            if panel is not None:
                show_fn = getattr(panel, "show", None)
                if callable(show_fn):
                    try:
                        show_fn()
                    except Exception:
                        pass
            return _make_execution_result_success("Painel lateral Orca Vase Studio aberto.")

        # Fallback if `create_dock_panel` is unavailable in an older/mocked environment
        create_win_fn = getattr(ui, "create_window", None) if ui is not None else None
        if callable(create_win_fn):
            panel = create_win_fn(
                html,
                title="Orca Vase Studio",
                width=max(440, dock_w),
                height=max(800, dock_h),
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
            )
            with self._panel_lock:
                VaseStudioDockCapability._active_panel = panel
            return _make_execution_result_success("Janela Orca Vase Studio aberta.")

        return _make_execution_result_success("Orca Vase Studio pronto.")


# ---------------------------------------------------------------------------
# Single `@orca.plugin` Entry Point Class
# ---------------------------------------------------------------------------


@orca.plugin
class OrcaVaseStudioPlugin(orca.base):
    """OrcaSlicer 2.5.1+ Native Plugin Entry Point for Orca Vase Studio."""

    def __init__(self) -> None:
        super().__init__()

    def register_capabilities(self) -> None:
        plugin_dir = _default_installed_plugin_dir()
        plugin_data_dir = _default_plugin_data_dir()
        docs_dir = Path.home() / "Documents" / "OrcaVaseStudio"

        candidate_dirs: list[Path] = [
            plugin_dir,
            plugin_data_dir,
            docs_dir,
        ]
        for extra_fn in (
            lambda: Path(__file__).resolve().parent,
            lambda: _resolve_storage_dir(in_callback=False),
        ):
            try:
                extra_dir = extra_fn()
                if str(extra_dir).strip():
                    candidate_dirs.append(extra_dir)
            except Exception:
                continue

        fs_targets: list[str] = []
        for d in candidate_dirs:
            d_str = str(d).strip()
            if not d_str:
                continue
            cand = f"{d_str}/*"
            if cand not in fs_targets:
                fs_targets.append(cand)

        req_fn = getattr(orca, "request_permissions", None)
        if callable(req_fn):
            req_fn(
                fs_read=list(fs_targets),
                fs_readwrite=list(fs_targets),
                threading=True,
            )

        orca.register_capability(VaseStudioPageCapability)
        orca.register_capability(VaseStudioDockCapability)
