"""Comprehensive geometry, 2-manifold watertightness, saucer, and printability tests."""

from __future__ import annotations

import copy
import math
import sys

sys.dont_write_bytecode = True

import unittest
import os
from collections import Counter, deque
from pathlib import Path


def _resolve_orca_site_packages() -> Path:
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "").strip()
        base = Path(appdata) / "OrcaSlicer" if appdata else Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    else:
        xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
        base = (Path(xdg) if xdg else (Path.home() / ".config")) / "OrcaSlicer"
    return base / "python" / "packages" / f"cp{sys.version_info.major}{sys.version_info.minor}"


ORCA_SITE_PACKAGES = _resolve_orca_site_packages()
PROJECT_SRC = Path(__file__).resolve().parent.parent / "src"
for _p in (ORCA_SITE_PACKAGES, PROJECT_SRC):
    _ps = str(_p)
    if _ps not in sys.path:
        sys.path.insert(0, _ps)

import numpy as np

from vase_studio.mesh_generator import (
    MeshData,
    evaluate_radius_grid,
    generate_saucer_mesh,
    generate_vase_mesh,
)
from vase_studio.presets_catalog import BUILTIN_PRESETS
from vase_studio.printability import analyze_printability
from vase_studio.schema import DEFAULT_PARAMS, SCHEMA_VERSION, normalize_params


class TestGeometryManifold(unittest.TestCase):
    """Strict 2-manifold topology, bounds, volume, and printability verification."""

    def assert_strict_2_manifold(
        self,
        mesh: MeshData,
        label: str,
        *,
        expected_genus: int | None = None,
        min_volume_cm3: float = 0.05,
    ) -> dict[str, float | int]:
        """Verify MeshData obeys every geometric and topological 2-manifold invariant."""
        self.assertIsInstance(mesh, MeshData, f"{label}: must return MeshData")

        verts = mesh.vertices
        tris = mesh.triangles
        normals = mesh.face_normals

        self.assertIsInstance(verts, np.ndarray, f"{label}: vertices must be ndarray")
        self.assertIsInstance(tris, np.ndarray, f"{label}: triangles must be ndarray")
        self.assertIsInstance(normals, np.ndarray, f"{label}: face_normals must be ndarray")

        self.assertEqual(verts.ndim, 2, f"{label}: vertices ndim != 2")
        self.assertEqual(verts.shape[1], 3, f"{label}: vertices shape[1] != 3")
        self.assertGreaterEqual(verts.shape[0], 4, f"{label}: fewer than 4 vertices")

        self.assertEqual(tris.ndim, 2, f"{label}: triangles ndim != 2")
        self.assertEqual(tris.shape[1], 3, f"{label}: triangles shape[1] != 3")
        self.assertGreaterEqual(tris.shape[0], 4, f"{label}: fewer than 4 triangles")

        self.assertEqual(
            normals.shape,
            tris.shape,
            f"{label}: face_normals shape {normals.shape} != triangles shape {tris.shape}",
        )

        # 1. Zero NaN / Inf anywhere
        self.assertTrue(np.all(np.isfinite(verts)), f"{label}: NaN or Inf found in vertices")
        self.assertTrue(np.all(np.isfinite(normals)), f"{label}: NaN or Inf found in face_normals")
        self.assertTrue(math.isfinite(float(mesh.volume_cm3)), f"{label}: volume_cm3 is not finite")

        # 2. Valid index bounds
        n_verts = verts.shape[0]
        self.assertGreaterEqual(int(tris.min()), 0, f"{label}: negative vertex index in triangles")
        self.assertLess(int(tris.max()), n_verts, f"{label}: out-of-range vertex index in triangles")

        # 3. Exact bed placement min(Z) == 0.0 & XY centering
        min_xyz = verts.min(axis=0)
        max_xyz = verts.max(axis=0)
        self.assertAlmostEqual(
            float(min_xyz[2]),
            0.0,
            places=4,
            msg=f"{label}: min(Z) must equal 0.0, got {float(min_xyz[2]):.6f}",
        )
        center_x = 0.5 * float(min_xyz[0] + max_xyz[0])
        center_y = 0.5 * float(min_xyz[1] + max_xyz[1])
        self.assertLess(abs(center_x), 15.0, f"{label}: mesh X center drifted ({center_x:.2f} mm)")
        self.assertLess(abs(center_y), 15.0, f"{label}: mesh Y center drifted ({center_y:.2f} mm)")

        # 4. Bounds metadata consistency
        self.assertIn("min", mesh.bounds_mm)
        self.assertIn("max", mesh.bounds_mm)
        self.assertIn("size", mesh.bounds_mm)
        np.testing.assert_allclose(mesh.bounds_mm["min"], min_xyz, atol=1e-2)
        np.testing.assert_allclose(mesh.bounds_mm["max"], max_xyz, atol=1e-2)
        np.testing.assert_allclose(mesh.bounds_mm["size"], max_xyz - min_xyz, atol=1e-2)

        # 5. Zero degenerate / zero-area faces & unit outward face normals
        u_idx = tris[:, 0]
        v_idx = tris[:, 1]
        w_idx = tris[:, 2]
        repeated_verts = np.any((u_idx == v_idx) | (v_idx == w_idx) | (w_idx == u_idx))
        self.assertFalse(bool(repeated_verts), f"{label}: triangle with repeated vertex indices")

        v0 = verts[u_idx].astype(np.float64)
        v1 = verts[v_idx].astype(np.float64)
        v2 = verts[w_idx].astype(np.float64)
        cross = np.cross(v1 - v0, v2 - v0)
        double_areas = np.linalg.norm(cross, axis=1)
        min_double_area = float(double_areas.min())
        self.assertGreater(
            min_double_area,
            1e-9,
            f"{label}: degenerate zero-area face detected (min 2*area = {min_double_area:.3e})",
        )

        norm_lengths = np.linalg.norm(normals.astype(np.float64), axis=1)
        np.testing.assert_allclose(
            norm_lengths,
            1.0,
            atol=1e-2,
            err_msg=f"{label}: face_normals are not unit vectors",
        )
        computed_normals = cross / double_areas[:, None]
        alignment = np.einsum("ij,ij->i", normals.astype(np.float64), computed_normals)
        self.assertGreater(
            float(alignment.min()),
            0.95,
            f"{label}: stored face_normals disagree with CCW triangle winding (min dot={alignment.min():.4f})",
        )

        # 6. Strict 2-manifold directed edge pairing:
        #    Every directed edge (u, v) has count == 1 and reverse (v, u) has count == 1.
        edge_counter: Counter[tuple[int, int]] = Counter()
        for a, b, c in tris.tolist():
            edge_counter[(a, b)] += 1
            edge_counter[(b, c)] += 1
            edge_counter[(c, a)] += 1

        n_faces = tris.shape[0]
        non_unit_edges = [(e, cnt) for e, cnt in edge_counter.items() if cnt != 1]
        self.assertEqual(
            len(non_unit_edges),
            0,
            f"{label}: {len(non_unit_edges)} non-manifold duplicate directed edges (sample: {non_unit_edges[:5]})",
        )
        self.assertEqual(
            len(edge_counter),
            3 * n_faces,
            f"{label}: unique directed edge count {len(edge_counter)} != 3*F ({3 * n_faces})",
        )

        open_boundary_edges = [
            e for e in edge_counter if edge_counter.get((e[1], e[0]), 0) != 1
        ]
        self.assertEqual(
            len(open_boundary_edges),
            0,
            f"{label}: {len(open_boundary_edges)} open boundary edges (sample: {open_boundary_edges[:5]})",
        )

        # Also check that distinct vertex indices do not hide unwelded duplicate boundary seams:
        # Quantize coordinates to 1e-4 mm and check geometric directed edges too.
        quantized = np.round(verts.astype(np.float64) * 10000.0).astype(np.int64)
        _, inv_map = np.unique(quantized, axis=0, return_inverse=True)
        geom_tris = inv_map[tris]
        geom_deg = int(
            np.sum(
                (geom_tris[:, 0] == geom_tris[:, 1])
                | (geom_tris[:, 1] == geom_tris[:, 2])
                | (geom_tris[:, 2] == geom_tris[:, 0])
            )
        )
        self.assertEqual(geom_deg, 0, f"{label}: geometrically collapsed triangles found ({geom_deg})")

        # 7. Positive outward signed volume (CCW right-hand rule)
        signed_vol_mm3 = float(np.sum(np.einsum("ij,ij->i", v0, cross))) / 6.0
        signed_vol_cm3 = signed_vol_mm3 / 1000.0
        self.assertGreater(
            signed_vol_cm3,
            min_volume_cm3,
            f"{label}: signed volume must be > {min_volume_cm3} cm3 (got {signed_vol_cm3:.4f})",
        )
        self.assertGreater(
            float(mesh.volume_cm3),
            min_volume_cm3,
            f"{label}: mesh.volume_cm3 must be > {min_volume_cm3} (got {mesh.volume_cm3:.4f})",
        )
        self.assertAlmostEqual(
            float(mesh.volume_cm3),
            signed_vol_cm3,
            delta=max(0.05, abs(signed_vol_cm3) * 0.03),
            msg=f"{label}: mesh.volume_cm3 ({mesh.volume_cm3:.4f}) != divergence volume ({signed_vol_cm3:.4f})",
        )

        # 8. Optional Euler characteristic / genus verification (V - E + F == 2 - 2g)
        used_verts = set(tris.reshape(-1).tolist())
        v_used = len(used_verts)
        e_undirected = (3 * n_faces) // 2
        euler_chi = v_used - e_undirected + n_faces
        if expected_genus is not None:
            # Verify single connected surface component first
            adj: dict[int, list[int]] = {v: [] for v in used_verts}
            for u, v in edge_counter:
                adj[u].append(v)
            start_v = next(iter(used_verts))
            visited = {start_v}
            q = deque([start_v])
            while q:
                cur = q.popleft()
                for nxt in adj[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            if len(visited) == v_used:
                expected_chi = 2 - 2 * expected_genus
                self.assertEqual(
                    euler_chi,
                    expected_chi,
                    f"{label}: Euler characteristic V-E+F={euler_chi} != {expected_chi} for genus={expected_genus}",
                )

        return {
            "vertices": n_verts,
            "faces": n_faces,
            "volume_cm3": signed_vol_cm3,
            "euler_chi": euler_chi,
        }

    def assert_open_mouthed_hollow_vase(
        self,
        mesh: MeshData,
        height_mm: float,
        label: str,
    ) -> dict[str, int]:
        """Verify the vase has an open top mouth (0 cap fan at (0, 0, height_mm)) and real inner cavity."""
        verts = mesh.vertices.astype(np.float64)
        tris = mesh.triangles
        normals = mesh.face_normals.astype(np.float64)

        tri_verts = verts[tris]  # (F, 3, 3)
        vert_r = np.hypot(tri_verts[:, :, 0], tri_verts[:, :, 1])
        vert_z = tri_verts[:, :, 2]

        # Zero triangle fan closing (0, 0, height_mm) at Z == height_mm
        touches_top_center = np.any(
            (vert_r < 1.0) & (np.abs(vert_z - float(height_mm)) < 0.5),
            axis=1,
        )
        top_center_cap_tris = int(np.sum(touches_top_center))
        self.assertEqual(
            top_center_cap_tris,
            0,
            f"{label}: expected open mouth (0 triangles touching (0, 0, {height_mm})), found {top_center_cap_tris}",
        )

        # Genuinely hollow interior: inward-pointing cavity wall triangles in upper body
        centroids = tri_verts.mean(axis=1)
        r_c = np.hypot(centroids[:, 0], centroids[:, 1])
        upper_mask = (centroids[:, 2] > 0.40 * float(height_mm)) & (r_c > 1.0)
        radial_dot = np.zeros(len(tris), dtype=np.float64)
        radial_dot[upper_mask] = (
            normals[upper_mask, 0] * centroids[upper_mask, 0]
            + normals[upper_mask, 1] * centroids[upper_mask, 1]
        ) / r_c[upper_mask]
        inward_cavity_tris = int(np.sum(upper_mask & (radial_dot < -0.15)))
        self.assertGreater(
            inward_cavity_tris,
            0,
            f"{label}: expected inward_cavity_tris > 0 for open hollow vase, got 0",
        )

        return {
            "top_center_cap_tris": top_center_cap_tris,
            "inward_cavity_tris": inward_cavity_tris,
        }

    def test_01_schema_defaults_and_normalization(self) -> None:
        self.assertEqual(SCHEMA_VERSION, "1.0")
        required_keys = {
            "name",
            "height_mm",
            "base_diameter_mm",
            "belly_diameter_mm",
            "belly_height_ratio",
            "waist_diameter_mm",
            "waist_height_ratio",
            "neck_diameter_mm",
            "lip_flare_mm",
            "lip_bevel_mm",
            "polygon_sides",
            "polygon_roundness",
            "use_custom_profile",
            "profile_points",
            "resolution_angular",
            "resolution_vertical",
            "bottom_fade_mm",
            "top_fade_mm",
            "global_twist_deg",
            "textures",
            "print_mode",
            "stl_always_open_hollow",
            "auto_configure_slicer",
            "spiral_line_width_mm",
            "spiral_bottom_layers",
            "spiral_smooth",
            "wall_thickness_mm",
            "bottom_thickness_mm",
            "auto_clamp_overhang",
            "max_safe_overhang_deg",
            "drainage",
            "saucer",
        }
        self.assertTrue(required_keys.issubset(set(DEFAULT_PARAMS.keys())))
        self.assertEqual(DEFAULT_PARAMS["print_mode"], "shelled_hollow")
        self.assertIs(DEFAULT_PARAMS["stl_always_open_hollow"], True)
        self.assertAlmostEqual(float(DEFAULT_PARAMS["wall_thickness_mm"]), 2.4, places=4)
        self.assertAlmostEqual(float(DEFAULT_PARAMS["bottom_thickness_mm"]), 3.2, places=4)
        self.assertEqual(
            set(DEFAULT_PARAMS["textures"].keys()),
            {"ribbed", "waves", "origami", "cellular", "geometric"},
        )

        # Deep copy isolation
        norm = normalize_params(None)
        self.assertEqual(norm["print_mode"], "shelled_hollow")
        self.assertIs(norm["stl_always_open_hollow"], True)
        norm["textures"]["waves"]["depth_mm"] = 999.0
        self.assertEqual(DEFAULT_PARAMS["textures"]["waves"]["depth_mm"], 3.0)

        # Thick wall range [0.8, 25.0], bottom range [1.0, 25.0], and stl_always_open_hollow boolean normalization
        thick_25 = normalize_params(
            {
                "wall_thickness_mm": 25.0,
                "bottom_thickness_mm": 25.0,
                "stl_always_open_hollow": False,
            }
        )
        self.assertEqual(thick_25["wall_thickness_mm"], 25.0)
        self.assertEqual(thick_25["bottom_thickness_mm"], 25.0)
        self.assertIs(thick_25["stl_always_open_hollow"], False)

        # Malformed / out-of-bounds clamping
        malformed = {
            "height_mm": "9999",
            "base_diameter_mm": "-5.0",
            "resolution_angular": "12",
            "resolution_vertical": "9000",
            "print_mode": "invalid_mode",
            "stl_always_open_hollow": "false",
            "wall_thickness_mm": "99.0",
            "bottom_thickness_mm": "99.0",
            "polygon_sides": 2,
            "use_custom_profile": True,
            "profile_points": [[0.8, 500.0], [0.2, -10.0]],
            "drainage": {"enabled": True, "hole_count": 99, "hole_diameter_mm": 0.5},
        }
        clamped = normalize_params(malformed)
        self.assertEqual(clamped["height_mm"], 500.0)
        self.assertEqual(clamped["base_diameter_mm"], 20.0)
        self.assertEqual(clamped["resolution_angular"], 64)
        self.assertEqual(clamped["resolution_vertical"], 400)
        self.assertEqual(clamped["print_mode"], "shelled_hollow")
        self.assertIs(clamped["stl_always_open_hollow"], False)
        self.assertEqual(clamped["wall_thickness_mm"], 25.0)
        self.assertEqual(clamped["bottom_thickness_mm"], 25.0)
        self.assertIn(clamped["polygon_sides"], {0} | set(range(3, 25)))
        self.assertLessEqual(clamped["drainage"]["hole_count"], 9)
        self.assertGreaterEqual(clamped["drainage"]["hole_diameter_mm"], 3.0)
        self.assertAlmostEqual(clamped["profile_points"][0][0], 0.0, places=5)
        self.assertAlmostEqual(clamped["profile_points"][-1][0], 1.0, places=5)

        min_clamped = normalize_params(
            {"wall_thickness_mm": 0.1, "bottom_thickness_mm": 0.1, "stl_always_open_hollow": "1"}
        )
        self.assertEqual(min_clamped["wall_thickness_mm"], 0.8)
        self.assertEqual(min_clamped["bottom_thickness_mm"], 1.0)
        self.assertIs(min_clamped["stl_always_open_hollow"], True)

    def test_02_default_params_full_resolution_manifold(self) -> None:
        self.assertEqual(DEFAULT_PARAMS["print_mode"], "shelled_hollow")
        self.assertIs(DEFAULT_PARAMS["stl_always_open_hollow"], True)
        mesh = generate_vase_mesh(DEFAULT_PARAMS)
        stats = self.assert_strict_2_manifold(mesh, "DEFAULT_PARAMS", expected_genus=0)
        hollow_stats = self.assert_open_mouthed_hollow_vase(
            mesh, float(DEFAULT_PARAMS["height_mm"]), "DEFAULT_PARAMS"
        )
        self.assertAlmostEqual(mesh.bounds_mm["size"][2], DEFAULT_PARAMS["height_mm"], delta=0.5)
        self.assertGreater(stats["faces"], 50000)
        self.assertGreater(hollow_stats["inward_cavity_tris"], 1000)

    def test_03_all_12_builtin_presets_manifold(self) -> None:
        self.assertEqual(
            len(BUILTIN_PRESETS),
            12,
            f"Expected exactly 12 BUILTIN_PRESETS, got {len(BUILTIN_PRESETS)}",
        )
        for idx, preset in enumerate(BUILTIN_PRESETS):
            pid = preset.get("id", f"preset_{idx}")
            with self.subTest(preset_id=pid):
                raw_params = preset["params"]
                self.assertEqual(
                    raw_params.get("print_mode"),
                    "shelled_hollow",
                    f"builtin_preset[{pid}] must default to print_mode=='shelled_hollow'",
                )
                params = copy.deepcopy(raw_params)
                norm_p = normalize_params(params)
                self.assertEqual(norm_p["print_mode"], "shelled_hollow")
                self.assertIs(norm_p["stl_always_open_hollow"], True)
                # Keep preset exact topology & textures, cap grid slightly only if ultra-dense
                params["resolution_angular"] = min(int(params.get("resolution_angular", 160)), 144)
                params["resolution_vertical"] = min(int(params.get("resolution_vertical", 140)), 120)
                mesh = generate_vase_mesh(params)
                self.assert_strict_2_manifold(mesh, f"builtin_preset[{pid}]")
                self.assert_open_mouthed_hollow_vase(
                    mesh, float(norm_p["height_mm"]), f"builtin_preset[{pid}]"
                )

    def test_04_spiral_vase_drainage_off_and_on_1_3_4_6_holes(self) -> None:
        base_params = normalize_params(
            {
                "print_mode": "spiral_vase",
                "height_mm": 120.0,
                "base_diameter_mm": 84.0,
                "resolution_angular": 96,
                "resolution_vertical": 80,
                "spiral_bottom_layers": 5,
                "drainage": {
                    "enabled": False,
                    "hole_count": 4,
                    "hole_diameter_mm": 8.0,
                    "ring_radius_ratio": 0.45,
                },
            }
        )
        solid_mesh = generate_vase_mesh(base_params, layer_height_mm=0.2)
        solid_stats = self.assert_strict_2_manifold(
            solid_mesh, "spiral_vase[drainage=off]", expected_genus=0
        )

        layer_h = 0.2
        z_cap_expected = min(5 * layer_h + 0.30, 0.35 * 120.0)

        for hole_count in (1, 3, 4, 6):
            with self.subTest(hole_count=hole_count):
                p = copy.deepcopy(base_params)
                p["drainage"]["enabled"] = True
                p["drainage"]["hole_count"] = hole_count
                if hole_count == 1:
                    p["drainage"]["ring_radius_ratio"] = 0.0
                mesh = generate_vase_mesh(p, layer_height_mm=layer_h)
                stats = self.assert_strict_2_manifold(
                    mesh, f"spiral_vase[holes={hole_count}]", expected_genus=0
                )
                # Blind cavities must reduce solid mesh volume slightly
                self.assertLess(
                    stats["volume_cm3"],
                    solid_stats["volume_cm3"],
                    f"spiral_vase[holes={hole_count}] blind cavities should subtract volume",
                )
                # Above Z_cap + 0.5mm and below height - 0.5mm, no interior cavity vertices should exist
                verts = mesh.vertices
                mid_mask = (verts[:, 2] > z_cap_expected + 0.5) & (verts[:, 2] < 119.5)
                if np.any(mid_mask):
                    mid_radii = np.hypot(verts[mid_mask, 0], verts[mid_mask, 1])
                    self.assertGreater(
                        float(mid_radii.min()),
                        18.0,
                        f"spiral_vase[holes={hole_count}] cavity leaked above Z_cap ({z_cap_expected} mm)!",
                    )

        # Also test 1 offset hole (ring_radius_ratio > 0)
        p_offset_1 = copy.deepcopy(base_params)
        p_offset_1["drainage"] = {
            "enabled": True,
            "hole_count": 1,
            "hole_diameter_mm": 8.0,
            "ring_radius_ratio": 0.40,
        }
        mesh_offset_1 = generate_vase_mesh(p_offset_1, layer_height_mm=layer_h)
        self.assert_strict_2_manifold(mesh_offset_1, "spiral_vase[holes=1,offset]")

    def test_05_shelled_hollow_drainage_off_and_on_1_3_4_6_holes(self) -> None:
        base_params = normalize_params(
            {
                "print_mode": "shelled_hollow",
                "height_mm": 120.0,
                "base_diameter_mm": 86.0,
                "belly_diameter_mm": 104.0,
                "waist_diameter_mm": 74.0,
                "neck_diameter_mm": 82.0,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "lip_bevel_mm": 1.0,
                "resolution_angular": 96,
                "resolution_vertical": 80,
                "drainage": {
                    "enabled": False,
                    "hole_count": 4,
                    "hole_diameter_mm": 8.0,
                    "ring_radius_ratio": 0.45,
                },
            }
        )
        # Compare against solid spiral_vase volume for the same outer geometry
        p_solid = copy.deepcopy(base_params)
        p_solid["print_mode"] = "spiral_vase"
        solid_mesh = generate_vase_mesh(p_solid)

        hollow_no_holes = generate_vase_mesh(base_params)
        hollow_stats = self.assert_strict_2_manifold(
            hollow_no_holes, "shelled_hollow[drainage=off]", expected_genus=0
        )
        self.assertLess(
            hollow_stats["volume_cm3"],
            0.55 * float(solid_mesh.volume_cm3),
            "shelled_hollow volume must be substantially smaller than solid spiral_vase volume",
        )

        for hole_count in (1, 3, 4, 6):
            with self.subTest(hole_count=hole_count):
                p = copy.deepcopy(base_params)
                p["drainage"]["enabled"] = True
                p["drainage"]["hole_count"] = hole_count
                p["drainage"]["ring_radius_ratio"] = 0.0 if hole_count == 1 else 0.45
                mesh = generate_vase_mesh(p)
                stats = self.assert_strict_2_manifold(
                    mesh,
                    f"shelled_hollow[holes={hole_count}]",
                    expected_genus=hole_count,
                )
                self.assertLess(
                    stats["volume_cm3"],
                    hollow_stats["volume_cm3"],
                    f"shelled_hollow[holes={hole_count}] through-holes must subtract floor volume",
                )

        # Also test hole_count=1 with offset ring_radius_ratio > 0
        p_off1 = copy.deepcopy(base_params)
        p_off1["drainage"] = {
            "enabled": True,
            "hole_count": 1,
            "hole_diameter_mm": 8.0,
            "ring_radius_ratio": 0.40,
        }
        mesh_off1 = generate_vase_mesh(p_off1)
        self.assert_strict_2_manifold(
            mesh_off1, "shelled_hollow[holes=1,offset]", expected_genus=1
        )
        self.assert_open_mouthed_hollow_vase(mesh_off1, 120.0, "shelled_hollow[holes=1,offset]")

    def test_05b_thick_walls_25mm_narrow_waist_and_drainage_1_4_9(self) -> None:
        """Verify extreme thick walls (25.0 mm wall & bottom), narrow waists, and 1/4/9 drainage holes."""
        # 1. Standard vase at max 25 mm wall & 25 mm bottom
        thick_std = normalize_params(
            {
                "print_mode": "shelled_hollow",
                "height_mm": 130.0,
                "base_diameter_mm": 86.0,
                "belly_diameter_mm": 106.0,
                "waist_diameter_mm": 74.0,
                "neck_diameter_mm": 84.0,
                "wall_thickness_mm": 25.0,
                "bottom_thickness_mm": 25.0,
                "lip_bevel_mm": 2.0,
                "resolution_angular": 96,
                "resolution_vertical": 84,
                "drainage": {"enabled": False},
            }
        )
        self.assertEqual(thick_std["wall_thickness_mm"], 25.0)
        self.assertEqual(thick_std["bottom_thickness_mm"], 25.0)
        mesh_std = generate_vase_mesh(thick_std)
        self.assert_strict_2_manifold(mesh_std, "thick_25mm_std[drainage=off]", expected_genus=0)
        self.assert_open_mouthed_hollow_vase(mesh_std, 130.0, "thick_25mm_std[drainage=off]")

        # 2. Narrow-waist textured vase with 25 mm wall & 25 mm bottom (drainage off & 1, 4, 9 holes)
        narrow_waist_base = normalize_params(
            {
                "print_mode": "shelled_hollow",
                "height_mm": 115.0,
                "base_diameter_mm": 68.0,
                "belly_diameter_mm": 90.0,
                "belly_height_ratio": 0.32,
                "waist_diameter_mm": 30.0,
                "waist_height_ratio": 0.68,
                "neck_diameter_mm": 42.0,
                "lip_flare_mm": 3.0,
                "lip_bevel_mm": 2.5,
                "wall_thickness_mm": 25.0,
                "bottom_thickness_mm": 25.0,
                "resolution_angular": 96,
                "resolution_vertical": 84,
                "textures": {
                    "ribbed": {"enabled": True, "depth_mm": 1.8, "count": 20},
                    "waves": {"enabled": True, "depth_mm": 1.5, "vertical_wavelength_mm": 24.0, "angular_lobes": 4},
                },
                "drainage": {
                    "enabled": False,
                    "hole_count": 4,
                    "hole_diameter_mm": 10.0,
                    "ring_radius_ratio": 0.50,
                },
            }
        )
        mesh_narrow_no_drain = generate_vase_mesh(narrow_waist_base)
        self.assert_strict_2_manifold(
            mesh_narrow_no_drain, "narrow_waist_25mm[drainage=off]", expected_genus=0
        )
        self.assert_open_mouthed_hollow_vase(
            mesh_narrow_no_drain, 115.0, "narrow_waist_25mm[drainage=off]"
        )

        for hole_count in (1, 4, 9):
            with self.subTest(case="narrow_waist_25mm", hole_count=hole_count):
                p = copy.deepcopy(narrow_waist_base)
                p["drainage"]["enabled"] = True
                p["drainage"]["hole_count"] = hole_count
                p["drainage"]["ring_radius_ratio"] = 0.0 if hole_count == 1 else 0.50
                mesh_h = generate_vase_mesh(p)
                self.assert_strict_2_manifold(
                    mesh_h,
                    f"narrow_waist_25mm[holes={hole_count}]",
                    expected_genus=hole_count,
                )
                self.assert_open_mouthed_hollow_vase(
                    mesh_h, 115.0, f"narrow_waist_25mm[holes={hole_count}]"
                )

        # 3. Short bowl (height=35 mm) with bottom_thickness=25 mm & wall_thickness=25 mm + 4 holes
        short_thick = normalize_params(
            {
                "print_mode": "shelled_hollow",
                "height_mm": 35.0,
                "base_diameter_mm": 64.0,
                "belly_diameter_mm": 72.0,
                "waist_diameter_mm": 58.0,
                "neck_diameter_mm": 66.0,
                "wall_thickness_mm": 25.0,
                "bottom_thickness_mm": 25.0,
                "resolution_angular": 84,
                "resolution_vertical": 64,
                "drainage": {
                    "enabled": True,
                    "hole_count": 4,
                    "hole_diameter_mm": 8.0,
                    "ring_radius_ratio": 0.45,
                },
            }
        )
        mesh_short = generate_vase_mesh(short_thick)
        self.assert_strict_2_manifold(mesh_short, "short_bowl_25mm[holes=4]", expected_genus=4)
        self.assert_open_mouthed_hollow_vase(mesh_short, 35.0, "short_bowl_25mm[holes=4]")

    def test_06_all_textures_custom_profile_and_polygonal_grid(self) -> None:
        params = normalize_params(
            {
                "height_mm": 140.0,
                "polygon_sides": 6,
                "polygon_roundness": 0.25,
                "global_twist_deg": 75.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 36.0],
                    [0.28, 52.0],
                    [0.62, 33.0],
                    [0.88, 42.0],
                    [1.0, 46.0],
                ],
                "resolution_angular": 96,
                "resolution_vertical": 72,
                "textures": {
                    "ribbed": {"enabled": True, "depth_mm": 1.8, "count": 24, "duty_cycle": 0.55, "sharpness": 0.6},
                    "waves": {"enabled": True, "depth_mm": 1.5, "vertical_wavelength_mm": 24.0, "angular_lobes": 5},
                    "origami": {"enabled": True, "depth_mm": 1.6, "cells_around": 10, "cells_vertical": 6},
                    "cellular": {"enabled": True, "depth_mm": 1.4, "scale_angular": 8, "ridge_mode": True, "seed": 101},
                },
            }
        )
        z_vals, theta_vals, radii = evaluate_radius_grid(params, n_z=50, n_theta=64)
        self.assertEqual(z_vals.shape, (50,))
        self.assertEqual(theta_vals.shape, (64,))
        self.assertEqual(radii.shape, (50, 64))
        self.assertGreaterEqual(float(radii.min()), 6.0 - 1e-5)

        # Deterministic cellular noise check
        _, _, radii_same = evaluate_radius_grid(params, n_z=50, n_theta=64)
        np.testing.assert_allclose(radii, radii_same, atol=1e-6)

        params_diff_seed = copy.deepcopy(params)
        params_diff_seed["textures"]["cellular"]["seed"] = 999
        _, _, radii_diff = evaluate_radius_grid(params_diff_seed, n_z=50, n_theta=64)
        self.assertGreater(float(np.max(np.abs(radii - radii_diff))), 0.05)

        mesh = generate_vase_mesh(params)
        self.assert_strict_2_manifold(mesh, "combined_textures_custom_profile")

    def test_07_auto_clamp_overhang(self) -> None:
        steep_params = normalize_params(
            {
                "height_mm": 100.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 20.0],
                    [0.35, 85.0],
                    [0.75, 25.0],
                    [1.0, 75.0],
                ],
                "resolution_angular": 80,
                "resolution_vertical": 100,
                "textures": {
                    "waves": {
                        "enabled": True,
                        "depth_mm": 8.0,
                        "vertical_wavelength_mm": 12.0,
                        "angular_lobes": 4,
                    }
                },
                "auto_clamp_overhang": False,
                "max_safe_overhang_deg": 45.0,
            }
        )
        unclamped_mesh = generate_vase_mesh(steep_params)
        self.assert_strict_2_manifold(unclamped_mesh, "overhang_unclamped")
        rep_unclamped = analyze_printability(unclamped_mesh, steep_params)
        self.assertGreater(rep_unclamped["max_overhang_deg"], 50.0)

        clamped_params = copy.deepcopy(steep_params)
        clamped_params["auto_clamp_overhang"] = True
        z_vals, _, radii = evaluate_radius_grid(clamped_params)
        dz = np.diff(z_vals)[:, None]
        dr = np.abs(np.diff(radii, axis=0))
        max_slope_allowed = math.tan(math.radians(45.0))
        self.assertLessEqual(
            float(np.max(dr / np.maximum(dz, 1e-6))),
            max_slope_allowed + 1e-3,
            "auto_clamp_overhang failed to bound |dR/dz| <= tan(max_safe_overhang_deg)",
        )

        clamped_mesh = generate_vase_mesh(clamped_params)
        self.assert_strict_2_manifold(clamped_mesh, "overhang_clamped")
        rep_clamped = analyze_printability(clamped_mesh, clamped_params)
        self.assertLess(rep_clamped["max_overhang_deg"], rep_unclamped["max_overhang_deg"])
        self.assertLessEqual(rep_clamped["critical_faces_pct"], 1.0)

    def test_08_generate_saucer_mesh_manifold(self) -> None:
        for match_tex, ribs_h in ((True, 2.0), (False, 0.0)):
            with self.subTest(match_vase_texture=match_tex, inner_ribs_height_mm=ribs_h):
                params = normalize_params(
                    {
                        "base_diameter_mm": 80.0,
                        "resolution_angular": 96,
                        "textures": {
                            "ribbed": {"enabled": True, "depth_mm": 2.2, "count": 28},
                            "waves": {"enabled": False},
                        },
                        "saucer": {
                            "clearance_mm": 8.0,
                            "rim_height_mm": 22.0,
                            "wall_thickness_mm": 2.4,
                            "floor_thickness_mm": 2.6,
                            "inner_ribs_height_mm": ribs_h,
                            "match_vase_texture": match_tex,
                        },
                    }
                )
                saucer = generate_saucer_mesh(params)
                self.assert_strict_2_manifold(
                    saucer,
                    f"saucer[tex={match_tex},ribs={ribs_h}]",
                    expected_genus=0,
                )
                # Outer diameter must comfortably exceed base_diameter + 2 * clearance
                min_expected_diam = 80.0 + 2.0 * 8.0
                self.assertGreater(saucer.bounds_mm["size"][0], min_expected_diam)
                self.assertGreater(saucer.bounds_mm["size"][1], min_expected_diam)
                self.assertAlmostEqual(saucer.bounds_mm["size"][2], 22.0, delta=1.5)

    def test_09_analyze_printability_trigonometry_and_limits(self) -> None:
        # Pure 45-degree outward frustum: radius grows from 30 mm to 90 mm over height 60 mm (dR/dz = 1 -> 45 deg)
        frustum_params = normalize_params(
            {
                "height_mm": 60.0,
                "use_custom_profile": True,
                "profile_points": [[0.0, 30.0], [0.5, 60.0], [1.0, 90.0]],
                "lip_flare_mm": 0.0,
                "lip_bevel_mm": 0.0,
                "bottom_fade_mm": 0.0,
                "top_fade_mm": 0.0,
                "resolution_angular": 96,
                "resolution_vertical": 60,
                "textures": {"waves": {"enabled": False}},
                "print_mode": "spiral_vase",
            }
        )
        frustum_mesh = generate_vase_mesh(frustum_params)
        report = analyze_printability(frustum_mesh, frustum_params)

        expected_keys = {
            "max_overhang_deg",
            "warning_faces_pct",
            "critical_faces_pct",
            "fits_bed",
            "fits_height",
            "spiral_gap_risk",
            "estimated_weight_g",
            "estimated_volume_cm3",
            "dimensions_mm",
            "triangle_count",
            "warnings",
        }
        self.assertTrue(expected_keys.issubset(set(report.keys())))
        self.assertAlmostEqual(float(report["max_overhang_deg"]), 45.0, delta=2.5)
        self.assertTrue(report["fits_bed"])
        self.assertTrue(report["fits_height"])
        self.assertEqual(report["triangle_count"], len(frustum_mesh.triangles))
        self.assertGreater(report["estimated_weight_g"], 0.0)

        # Small printer bed & low Z limit must trigger fits_bed=False, fits_height=False, and bilingual warnings
        tiny_host = {
            "bed_x": 100.0,
            "bed_y": 100.0,
            "max_z": 40.0,
            "nozzle_mm": 0.4,
            "layer_height_mm": 0.2,
            "line_width_mm": 0.42,
        }
        report_overflow = analyze_printability(frustum_mesh, frustum_params, host_context=tiny_host)
        self.assertFalse(report_overflow["fits_bed"])
        self.assertFalse(report_overflow["fits_height"])
        self.assertGreaterEqual(len(report_overflow["warnings"]), 2)
        for w in report_overflow["warnings"]:
            self.assertIn("code", w)
            self.assertTrue(bool(w.get("pt")))
            self.assertTrue(bool(w.get("en")))

        # Large-format 450 mm tall x 360 mm diameter vase on 420x420x480 vs 180x180x180 & circular Ø300mm beds
        large_params = normalize_params(
            {
                "name": "Neptune Max Amphora",
                "height_mm": 450.0,
                "base_diameter_mm": 220.0,
                "belly_diameter_mm": 360.0,
                "waist_diameter_mm": 260.0,
                "neck_diameter_mm": 280.0,
                "resolution_angular": 72,
                "resolution_vertical": 72,
                "print_mode": "shelled_hollow",
                "wall_thickness_mm": 3.0,
                "bottom_thickness_mm": 4.0,
            }
        )
        self.assertEqual(large_params["height_mm"], 450.0)
        self.assertEqual(large_params["belly_diameter_mm"], 360.0)
        large_mesh = generate_vase_mesh(large_params)
        self.assert_strict_2_manifold(large_mesh, "large_450mm_amphora", expected_genus=0)
        self.assert_open_mouthed_hollow_vase(large_mesh, 450.0, "large_450mm_amphora")

        rep_420 = analyze_printability(
            large_mesh,
            large_params,
            host_context={"bed_x": 420.0, "bed_y": 420.0, "max_z": 480.0, "nozzle_mm": 0.6, "line_width_mm": 0.66},
        )
        self.assertTrue(rep_420["fits_bed"])
        self.assertTrue(rep_420["fits_height"])

        rep_180 = analyze_printability(
            large_mesh,
            large_params,
            host_context={"bed_x": 180.0, "bed_y": 180.0, "max_z": 180.0, "nozzle_mm": 0.4, "line_width_mm": 0.42},
        )
        self.assertFalse(rep_180["fits_bed"])
        self.assertFalse(rep_180["fits_height"])

        rep_delta_300 = analyze_printability(
            large_mesh,
            large_params,
            host_context={
                "bed_x": 300.0,
                "bed_y": 300.0,
                "bed_shape": "circular",
                "max_z": 480.0,
                "nozzle_mm": 0.4,
                "line_width_mm": 0.42,
            },
        )
        self.assertFalse(rep_delta_300["fits_bed"])
        self.assertTrue(rep_delta_300["fits_height"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
