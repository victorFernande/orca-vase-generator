"""Continuous periodic relief, manufacturing topology and browser/export parity."""
from __future__ import annotations

import copy
import json
import shutil
import subprocess
import unittest

import test_geometry_manifold as _topology
import numpy as np
from vase_studio.geometric_patterns import GEOMETRIC_PATTERNS, GEOMETRIC_JS, geometric_displacement
from vase_studio.mesh_generator import evaluate_radius_grid, generate_vase_mesh, generate_saucer_mesh
from vase_studio.schema import normalize_params
from vase_studio.studio_ui import get_studio_html


def relief_params(pattern, **overrides):
    return normalize_params({"resolution_angular": 96, "resolution_vertical": 90,
        "textures": {"waves": {"enabled": False}, "geometric": {
            "enabled": True, "pattern": pattern, **overrides}}})


class TestGeometricPatterns(unittest.TestCase):
    def test_normalization_and_disabled_compatibility(self):
        p = relief_params("invalid", depth_mm=float("nan"), cells_around=1000,
                          cells_vertical=-2, strength_bottom=-1, strength_top=99)
        g = p["textures"]["geometric"]
        self.assertEqual((g["pattern"], g["depth_mm"], g["cells_around"], g["cells_vertical"]),
                         ("leaf_scales", 3, 36, 2))
        self.assertEqual((g["strength_bottom"], g["strength_top"]), (0, 2))
        baseline = normalize_params(None)
        disabled = copy.deepcopy(baseline)
        disabled["textures"]["geometric"].update(pattern="folded_petals", depth_mm=8)
        np.testing.assert_array_equal(evaluate_radius_grid(baseline)[2], evaluate_radius_grid(disabled)[2])

    def test_all_patterns_seam_continuity_bounds_and_zone_strengths(self):
        z = np.linspace(0, 1, 1001)[:, None]
        theta = np.linspace(-2 * np.pi, 4 * np.pi, 91)[None, :]
        for pattern in GEOMETRIC_PATTERNS:
            with self.subTest(pattern=pattern):
                g = relief_params(pattern, twist_deg=137, phase_deg=21)["textures"]["geometric"]
                a = geometric_displacement(z, theta, g)
                self.assertTrue(np.isfinite(a).all())
                self.assertGreater(float(np.ptp(a)), 0.5)
                self.assertLessEqual(float(np.abs(a).max()), 3 + 1e-12)
                np.testing.assert_allclose(a, geometric_displacement(z, theta + 2 * np.pi, g), atol=2e-12)
                # A discontinuous stagger implementation jumps at integer rows.
                rows = np.arange(1, g["cells_vertical"])[:, None] / g["cells_vertical"]
                left = geometric_displacement(rows - 1e-9, theta, g)
                right = geometric_displacement(rows + 1e-9, theta, g)
                self.assertLess(float(np.max(np.abs(left - right))), 2e-5)
                g.update(strength_bottom=0, strength_middle=0, strength_top=0)
                np.testing.assert_array_equal(geometric_displacement(z, theta, g), np.zeros_like(a))
                g.update(strength_bottom=0, strength_middle=1, strength_top=2)
                endpoints = geometric_displacement(np.array([[0.0], [0.5], [1.0]]), theta, g)
                g.update(strength_bottom=1, strength_middle=1, strength_top=1)
                reference = geometric_displacement(np.array([[0.0], [0.5], [1.0]]), theta, g)
                np.testing.assert_allclose(endpoints, reference * np.array([[0], [1], [2]]), atol=1e-12)

    def test_all_patterns_manifold_hollow_spiral_drainage_and_saucer(self):
        topology = _topology.TestGeometryManifold(methodName="runTest")
        for pattern in GEOMETRIC_PATTERNS:
            for mode in ("shelled_hollow", "spiral_vase"):
                p = relief_params(pattern)
                p["print_mode"] = mode
                p["drainage"].update(enabled=True, hole_count=3)
                with self.subTest(pattern=pattern, mode=mode):
                    mesh = generate_vase_mesh(p)
                    topology.assert_strict_2_manifold(mesh, pattern + mode,
                        expected_genus=3 if mode == "shelled_hollow" else 0)
            topology.assert_strict_2_manifold(generate_saucer_mesh(p), pattern + "_saucer", expected_genus=0)

    def test_signed_depth_and_composition(self):
        for pattern in GEOMETRIC_PATTERNS:
            p = relief_params(pattern)
            g = p["textures"]["geometric"]
            _, _, positive = evaluate_radius_grid(p)
            g["enabled"] = False
            _, _, base = evaluate_radius_grid(p)
            g.update(enabled=True, depth_mm=-3)
            _, _, negative = evaluate_radius_grid(p)
            np.testing.assert_allclose(positive + negative, 2 * base, atol=1e-12)
            g["depth_mm"] = 3
            p["textures"]["ribbed"]["enabled"] = True
            mixed = evaluate_radius_grid(p)[2]
            g["enabled"] = False
            ribs = evaluate_radius_grid(p)[2]
            np.testing.assert_allclose(mixed - ribs, positive - base, atol=1e-12)

    def test_extreme_relief_narrow_custom_profile_and_overhang_clamp(self):
        topology = _topology.TestGeometryManifold(methodName="runTest")
        for pattern in GEOMETRIC_PATTERNS:
            p = relief_params(pattern, depth_mm=-8, cells_around=36, cells_vertical=24,
                twist_deg=720, strength_bottom=2, strength_middle=2, strength_top=2)
            p.update(use_custom_profile=True, profile_points=[[0, 16], [0.5, 8], [1, 18]],
                     wall_thickness_mm=25, bottom_thickness_mm=25, auto_clamp_overhang=True)
            p = normalize_params(p)
            z, _, radii = evaluate_radius_grid(p)
            self.assertGreaterEqual(float(radii.min()), 6)
            slopes = np.abs(np.diff(radii, axis=0) / np.diff(z)[:, None])
            self.assertLessEqual(float(slopes.max()), np.tan(np.deg2rad(p["max_safe_overhang_deg"])) + 1e-10)
            topology.assert_strict_2_manifold(generate_vase_mesh(p), pattern + "_extreme", expected_genus=0)

    @unittest.skipUnless(shutil.which("node"), "Node required for production JS parity")
    def test_production_js_relief_matches_numpy(self):
        theta = np.linspace(-2 * np.pi, 4 * np.pi, 113)[None, :]
        z = np.linspace(0, 1, 79)[:, None]
        cases = []
        for pattern in GEOMETRIC_PATTERNS:
            g = relief_params(pattern, twist_deg=-235, phase_deg=313, depth_mm=-6.7,
                strength_bottom=0.2, strength_middle=1.8, strength_top=0.7)["textures"]["geometric"]
            cases.append({"p": g, "expected": geometric_displacement(z, theta, g).tolist()})
        js = GEOMETRIC_JS + "\nconst data=JSON.parse(require('fs').readFileSync(0,'utf8')); console.log(JSON.stringify(data.cases.map(c=>data.z.map(z=>data.theta.map(t=>geometricDisplacement(z,t,c.p))))));"
        proc = subprocess.run([shutil.which("node"), "-e", js], input=json.dumps({"cases": cases,
            "z": z[:, 0].tolist(), "theta": theta[0].tolist()}), text=True, capture_output=True, check=True)
        actual = json.loads(proc.stdout)
        for case, result in zip(cases, actual):
            np.testing.assert_allclose(result, case["expected"], atol=2e-11, rtol=2e-11)
        # The tested function is embedded into both production views.
        for mode in ("page", "dock"):
            html = get_studio_html(mode)
            self.assertIn(GEOMETRIC_JS, html)
            self.assertNotIn("__GEOMETRIC_JS__", html)


if __name__ == "__main__":
    unittest.main()
