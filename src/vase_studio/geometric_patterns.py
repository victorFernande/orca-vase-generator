"""Periodic sidewall reliefs, evaluated identically by NumPy and the offline preview.

Original analytic patterns inspired by the public Vase Maker gallery. No source
from the reference plugin is included. Relief is part of the existing continuous
radial surface, so it does not introduce overlapping decorative solids.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np

GEOMETRIC_PATTERNS = (
    "diamond", "leaf_scales", "crater_cells", "folded_petals",
    "spiral_bloom", "ripple", "coral",
)

GEOMETRIC_DEFAULTS = {
    "enabled": False, "pattern": "leaf_scales", "depth_mm": 3.0,
    "cells_around": 14, "cells_vertical": 10, "twist_deg": 0.0,
    "phase_deg": 0.0, "strength_bottom": 1.0,
    "strength_middle": 1.0, "strength_top": 1.0,
    "ribbon_width_mm": 34.0, "ribbon_thickness_mm": 1.2,
    "ribbon_curl_deg": 382.0, "ribbon_overlap_mm": 1.4,
    "ribbon_stretch_pct": 8.0, "ribbon_stagger": 0.5,
    "ribbon_quality": "fine",
    "ribbon_nozzle_mm": 0.4,
}


def geometric_displacement(z_norm: np.ndarray, theta: np.ndarray, p: dict) -> np.ndarray:
    """Return bounded radial relief in mm; angular seam is exactly periodic.

    Staggered cells are evaluated in three neighboring rows. Their compact
    support fades to zero before the row leaves the window, avoiding the steps
    caused by directly switching a row's angular phase at integer heights.
    """
    import numpy as np

    if p["pattern"] == "folded_petals":
        return np.zeros(np.broadcast_shapes(z_norm.shape, theta.shape), dtype=np.float64)

    u = (theta + np.deg2rad(p["twist_deg"]) * z_norm + np.deg2rad(p["phase_deg"])) * p["cells_around"] / (2 * np.pi)
    v = z_norm * p["cells_vertical"]
    pattern = p["pattern"]
    if pattern == "ripple":
        relief = np.sin(2 * np.pi * v + 0.35 * np.sin(2 * np.pi * u))
    elif pattern == "spiral_bloom":
        relief = (np.cos(2 * np.pi * (u + v)) + 0.3 * np.cos(2 * np.pi * (u - v))) / 1.3
    elif pattern == "coral":
        a = np.sin(2 * np.pi * u + 0.9 * np.sin(2 * np.pi * v))
        b = np.sin(2 * np.pi * v + 0.9 * np.sin(2 * np.pi * u))
        relief = 1 - 2 * np.abs(a * b)
    else:
        relief = np.zeros(np.broadcast_shapes(u.shape, v.shape), dtype=np.float64)
        center_row = np.floor(v)
        for offset in (-1, 0, 1):
            row = center_row + offset
            x = np.mod(u - np.mod(row, 2) * 0.5 + 0.5, 1) - 0.5
            y = v - row
            if pattern == "diamond":
                cell = np.maximum(0, 1 - 2 * np.abs(x) - np.abs(y) / 0.6)
            else:
                q = (x / 0.48) ** 2 + (y / 0.62) ** 2
                support = np.maximum(0, 1 - q)
                if pattern == "crater_cells":
                    # A recessed basin surrounded by a raised, continuous lip.
                    cell = support ** 2 * (5 * q - 1)
                elif pattern == "folded_petals":
                    cell = support * (0.25 + 1.5 * np.abs(x)) * (0.75 + 0.25 * y / 0.62)
                else:  # leaf_scales: a pointed overlapping lens with central vein
                    cell = support ** 2 * (1 - 0.45 * np.abs(x) / 0.48) * (0.7 + 0.3 * y / 0.62)
            relief += cell
        relief = np.clip(relief, -1, 1)
    # C1 interpolation at the middle zone; endpoints keep their exact strengths.
    t = np.clip(np.where(z_norm < 0.5, z_norm * 2, (z_norm - 0.5) * 2), 0, 1)
    t = t * t * (3 - 2 * t)
    low = np.where(z_norm < 0.5, p["strength_bottom"], p["strength_middle"])
    high = np.where(z_norm < 0.5, p["strength_middle"], p["strength_top"])
    return relief * p["depth_mm"] * (low + (high - low) * t)


# Kept next to the NumPy evaluator so parity tests can exercise the production
# browser function directly, including fractional coordinates and angular seam.
GEOMETRIC_JS = r"""
  function geometricDisplacement(zNorm, theta, p) {
    if (p.pattern === "folded_petals") return 0;
    const u = (theta + p.twist_deg * Math.PI / 180 * zNorm + p.phase_deg * Math.PI / 180) * p.cells_around / (2 * Math.PI);
    const v = zNorm * p.cells_vertical;
    let relief = 0;
    if (p.pattern === "ripple") {
      relief = Math.sin(2 * Math.PI * v + 0.35 * Math.sin(2 * Math.PI * u));
    } else if (p.pattern === "spiral_bloom") {
      relief = (Math.cos(2 * Math.PI * (u + v)) + 0.3 * Math.cos(2 * Math.PI * (u - v))) / 1.3;
    } else if (p.pattern === "coral") {
      const a = Math.sin(2 * Math.PI * u + 0.9 * Math.sin(2 * Math.PI * v));
      const b = Math.sin(2 * Math.PI * v + 0.9 * Math.sin(2 * Math.PI * u));
      relief = 1 - 2 * Math.abs(a * b);
    } else {
      const centerRow = Math.floor(v);
      for (let offset = -1; offset <= 1; offset++) {
        const row = centerRow + offset;
        const rowParity = ((row % 2) + 2) % 2;
        const rawX = u - rowParity * 0.5 + 0.5;
        const x = rawX - Math.floor(rawX) - 0.5;
        const y = v - row;
        let cell;
        if (p.pattern === "diamond") {
          cell = Math.max(0, 1 - 2 * Math.abs(x) - Math.abs(y) / 0.6);
        } else {
          const q = (x / 0.48) ** 2 + (y / 0.62) ** 2;
          const support = Math.max(0, 1 - q);
          if (p.pattern === "crater_cells") cell = support ** 2 * (5 * q - 1);
          else if (p.pattern === "folded_petals") cell = support * (0.25 + 1.5 * Math.abs(x)) * (0.75 + 0.25 * y / 0.62);
          else cell = support ** 2 * (1 - 0.45 * Math.abs(x) / 0.48) * (0.7 + 0.3 * y / 0.62);
        }
        relief += cell;
      }
      relief = Math.max(-1, Math.min(1, relief));
    }
    let t = Math.max(0, Math.min(1, zNorm < 0.5 ? zNorm * 2 : (zNorm - 0.5) * 2));
    t = t * t * (3 - 2 * t);
    const low = zNorm < 0.5 ? p.strength_bottom : p.strength_middle;
    const high = zNorm < 0.5 ? p.strength_middle : p.strength_top;
    return relief * p.depth_mm * (low + (high - low) * t);
  }
"""
