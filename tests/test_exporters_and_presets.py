"""Comprehensive tests for binary STL, OrcaSlicer 2.5.1 3MF archives, presets CRUD, and randomizer."""

from __future__ import annotations

import copy
import json
import math
import struct
import sys

sys.dont_write_bytecode = True

import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
import os
from collections import Counter
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

from vase_studio.exporters import write_binary_stl, write_orca_3mf
from vase_studio.mesh_generator import generate_saucer_mesh, generate_vase_mesh
from vase_studio.presets_catalog import (
    BUILTIN_PRESETS,
    delete_user_preset,
    generate_random_printable_params,
    load_user_presets,
    save_user_preset,
)
from vase_studio.printability import analyze_printability
from vase_studio.schema import DEFAULT_PARAMS, normalize_params


def _strip_ns(tag: str) -> str:
    return tag.split("}", 1)[1] if "}" in tag else tag


class TestExportersAndPresets(unittest.TestCase):
    """Validate binary STL byte layout, OrcaSlicer 3MF XML/JSON structure, presets, and randomizer."""

    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory(prefix="orca_vase_qa_exp_")
        self.tmp_path = Path(self._tmpdir.name)

    def tearDown(self) -> None:
        self._tmpdir.cleanup()

    def test_01_write_binary_stl_header_count_and_exact_byte_size(self) -> None:
        for mode in ("spiral_vase", "shelled_hollow"):
            with self.subTest(print_mode=mode):
                params = normalize_params(
                    {
                        "print_mode": mode,
                        "resolution_angular": 72,
                        "resolution_vertical": 60,
                        "drainage": {"enabled": True, "hole_count": 3},
                    }
                )
                mesh = generate_vase_mesh(params)
                n_faces = int(mesh.triangles.shape[0])

                stl_file = self.tmp_path / f"vase_{mode}.stl"
                returned_path = write_binary_stl(stl_file, mesh, header_name="OrcaVaseQA")
                self.assertEqual(Path(returned_path).resolve(), stl_file.resolve())
                self.assertTrue(stl_file.is_file())

                expected_bytes = 84 + 50 * n_faces
                raw = stl_file.read_bytes()
                self.assertEqual(
                    len(raw),
                    expected_bytes,
                    f"Binary STL byte size {len(raw)} != 84 + 50*{n_faces} ({expected_bytes})",
                )

                header = raw[:80]
                self.assertIn(b"OrcaVaseQA", header)
                (tri_count,) = struct.unpack("<I", raw[80:84])
                self.assertEqual(tri_count, n_faces)

                stl_dtype = np.dtype(
                    [
                        ("normal", "<f4", (3,)),
                        ("v0", "<f4", (3,)),
                        ("v1", "<f4", (3,)),
                        ("v2", "<f4", (3,)),
                        ("attr", "<u2"),
                    ]
                )
                records = np.frombuffer(raw, dtype=stl_dtype, offset=84)
                self.assertEqual(len(records), n_faces)
                self.assertTrue(np.all(np.isfinite(records["normal"])))
                self.assertTrue(np.all(np.isfinite(records["v0"])))
                self.assertTrue(np.all(np.isfinite(records["v1"])))
                self.assertTrue(np.all(np.isfinite(records["v2"])))

                expected_tris = mesh.vertices[mesh.triangles]
                np.testing.assert_allclose(records["v0"], expected_tris[:, 0], atol=1e-5)
                np.testing.assert_allclose(records["v1"], expected_tris[:, 1], atol=1e-5)
                np.testing.assert_allclose(records["v2"], expected_tris[:, 2], atol=1e-5)

    def test_02_write_orca_3mf_spiral_vase_structure_and_overrides(self) -> None:
        params = normalize_params(
            {
                "name": "Ondas QA",
                "print_mode": "spiral_vase",
                "auto_configure_slicer": True,
                "spiral_smooth": True,
                "spiral_bottom_layers": 6,
                "spiral_line_width_mm": 0.68,
                "resolution_angular": 72,
                "resolution_vertical": 60,
            }
        )
        mesh = generate_vase_mesh(params)
        host_config = {
            "bed_x": 220.0,
            "bed_y": 220.0,
            "project_settings": {
                "printer_settings_id": "Anycubic Kobra X 0.4 nozzle",
                "filament_settings_id": ["Generic PLA @System"],
                "layer_height": "0.2",
            },
        }
        out_3mf = self.tmp_path / "vase_spiral.3mf"
        ret = write_orca_3mf(
            out_3mf,
            [("Ondas_QA", mesh, (110.0, 110.0, 0.0))],
            params,
            host_config=host_config,
        )
        self.assertEqual(Path(ret).resolve(), out_3mf.resolve())
        self.assertTrue(out_3mf.is_file())
        self.assertTrue(zipfile.is_zipfile(out_3mf))

        with zipfile.ZipFile(out_3mf, "r") as zf:
            self.assertIsNone(zf.testzip(), "Corrupted ZIP entries in .3mf")
            names = set(zf.namelist())
            required_members = {
                "[Content_Types].xml",
                "_rels/.rels",
                "3D/3dmodel.model",
                "Metadata/model_settings.config",
                "Metadata/project_settings.config",
            }
            self.assertTrue(
                required_members.issubset(names),
                f"Missing required 3MF archive entries: {required_members - names}",
            )

            # 1. XML parse [Content_Types].xml
            ct_root = ET.fromstring(zf.read("[Content_Types].xml"))
            self.assertEqual(_strip_ns(ct_root.tag), "Types")
            ct_exts = {el.attrib.get("Extension", "").lower() for el in ct_root}
            self.assertIn("rels", ct_exts)
            self.assertIn("model", ct_exts)

            # 2. XML parse _rels/.rels
            rels_root = ET.fromstring(zf.read("_rels/.rels"))
            self.assertEqual(_strip_ns(rels_root.tag), "Relationships")
            targets = [el.attrib.get("Target", "") for el in rels_root]
            self.assertTrue(
                any(t.lstrip("/") == "3D/3dmodel.model" for t in targets),
                f"_rels/.rels missing 3D/3dmodel.model target: {targets}",
            )

            # 3. XML parse 3D/3dmodel.model (plus any sub-object .model files if split)
            model_root = ET.fromstring(zf.read("3D/3dmodel.model"))
            self.assertEqual(_strip_ns(model_root.tag), "model")
            self.assertEqual(model_root.attrib.get("unit"), "millimeter")

            meta_map = {
                el.attrib.get("name"): (el.text or "").strip()
                for el in model_root
                if _strip_ns(el.tag) == "metadata"
            }
            self.assertIn("Application", meta_map)
            self.assertIn("OrcaSlicer", meta_map["Application"])
            self.assertEqual(meta_map.get("BambuStudio:3mfVersion"), "1")

            # Count vertices & triangles across all .model XML files in archive
            total_verts = 0
            total_tris = 0
            for member in names:
                if member.endswith(".model"):
                    m_root = ET.fromstring(zf.read(member))
                    for el in m_root.iter():
                        tag = _strip_ns(el.tag)
                        if tag == "vertex":
                            total_verts += 1
                        elif tag == "triangle":
                            total_tris += 1
            self.assertEqual(total_verts, int(mesh.vertices.shape[0]))
            self.assertEqual(total_tris, int(mesh.triangles.shape[0]))

            build_items = [
                el
                for el in model_root.iter()
                if _strip_ns(el.tag) == "item"
            ]
            self.assertEqual(len(build_items), 1)
            tf_parts = [float(x) for x in build_items[0].attrib["transform"].split()]
            self.assertEqual(len(tf_parts), 12)
            self.assertAlmostEqual(tf_parts[9], 110.0, delta=1.0)
            self.assertAlmostEqual(tf_parts[10], 110.0, delta=1.0)
            self.assertAlmostEqual(tf_parts[11], 0.0, delta=1e-3)

            # 4. XML parse Metadata/model_settings.config
            ms_root = ET.fromstring(zf.read("Metadata/model_settings.config"))
            self.assertEqual(_strip_ns(ms_root.tag), "config")
            ms_tags = {_strip_ns(el.tag) for el in ms_root}
            self.assertIn("object", ms_tags)
            self.assertIn("plate", ms_tags)

            # 5. JSON parse Metadata/project_settings.config
            proj_cfg = json.loads(zf.read("Metadata/project_settings.config").decode("utf-8"))
            self.assertIsInstance(proj_cfg, dict)
            self.assertEqual(
                proj_cfg.get("printer_settings_id"),
                "Anycubic Kobra X 0.4 nozzle",
            )
            self.assertEqual(proj_cfg.get("spiral_mode"), "1")
            self.assertEqual(proj_cfg.get("spiral_mode_smooth"), "1")
            self.assertEqual(proj_cfg.get("wall_loops"), "1")
            self.assertEqual(proj_cfg.get("top_shell_layers"), "0")
            self.assertEqual(proj_cfg.get("sparse_infill_density"), "0%")
            self.assertEqual(proj_cfg.get("bottom_shell_layers"), "6")
            self.assertAlmostEqual(float(proj_cfg["outer_wall_line_width"]), 0.68, places=2)

        # Also test spiral_smooth = False override
        params_unsmooth = copy.deepcopy(params)
        params_unsmooth["spiral_smooth"] = False
        out_unsmooth = self.tmp_path / "vase_spiral_unsmooth.3mf"
        write_orca_3mf(out_unsmooth, [("Ondas_QA", mesh, (110.0, 110.0, 0.0))], params_unsmooth)
        with zipfile.ZipFile(out_unsmooth, "r") as zf:
            proj_cfg2 = json.loads(zf.read("Metadata/project_settings.config").decode("utf-8"))
            self.assertEqual(proj_cfg2.get("spiral_mode"), "1")
            self.assertEqual(proj_cfg2.get("spiral_mode_smooth"), "0")

    def test_03_write_orca_3mf_shelled_hollow_and_multi_item_saucer(self) -> None:
        params = normalize_params(
            {
                "name": "Cachepo Jardim",
                "print_mode": "shelled_hollow",
                "auto_configure_slicer": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "base_diameter_mm": 76.0,
                "resolution_angular": 72,
                "resolution_vertical": 60,
                "drainage": {"enabled": True, "hole_count": 4, "hole_diameter_mm": 8.0},
            }
        )
        vase_mesh = generate_vase_mesh(params)
        saucer_mesh = generate_saucer_mesh(params)

        out_3mf = self.tmp_path / "cachepo_with_saucer.3mf"
        write_orca_3mf(
            out_3mf,
            [
                ("Cachepo", vase_mesh, (65.0, 110.0, 0.0)),
                ("Pratinho", saucer_mesh, (165.0, 110.0, 0.0)),
            ],
            params,
            host_config={"bed_x": 220.0, "bed_y": 220.0, "project_settings": {"spiral_mode": "1"}},
        )

        with zipfile.ZipFile(out_3mf, "r") as zf:
            self.assertIsNone(zf.testzip())
            model_root = ET.fromstring(zf.read("3D/3dmodel.model"))
            build_items = [el for el in model_root.iter() if _strip_ns(el.tag) == "item"]
            self.assertEqual(len(build_items), 2)

            tf0 = [float(x) for x in build_items[0].attrib["transform"].split()]
            tf1 = [float(x) for x in build_items[1].attrib["transform"].split()]
            dist_xy = math.hypot(tf1[9] - tf0[9], tf1[10] - tf0[10])
            self.assertGreater(dist_xy, 40.0, "Vase and saucer transforms overlap on build plate")

            ms_root = ET.fromstring(zf.read("Metadata/model_settings.config"))
            ms_objects = [el for el in ms_root if _strip_ns(el.tag) == "object"]
            self.assertGreaterEqual(len(ms_objects), 1)

            proj_cfg = json.loads(zf.read("Metadata/project_settings.config").decode("utf-8"))
            self.assertEqual(
                proj_cfg.get("spiral_mode"),
                "0",
                "shelled_hollow 3MF must force spiral_mode == '0'",
            )

    def _inspect_binary_stl_open_mouth(self, stl_path: Path, height_mm: float) -> dict[str, int]:
        raw = stl_path.read_bytes()
        (tri_count,) = struct.unpack("<I", raw[80:84])
        self.assertEqual(len(raw), 84 + 50 * tri_count)
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

    def test_04_builtin_presets_all_shelled_hollow_and_open_mouth_stl(self) -> None:
        self.assertEqual(len(BUILTIN_PRESETS), 12)
        seen_ids: set[str] = set()
        categories: set[str] = set()
        has_drainage_preset = False

        for p in BUILTIN_PRESETS:
            for field in (
                "id",
                "title_pt",
                "title_en",
                "category",
                "description_pt",
                "description_en",
                "params",
            ):
                self.assertIn(field, p, f"Preset missing field {field}")
                self.assertTrue(bool(p[field]), f"Preset {p.get('id')} has empty {field}")

            pid = p["id"]
            self.assertNotIn(pid, seen_ids, f"Duplicate preset id: {pid}")
            seen_ids.add(pid)
            categories.add(p["category"])

            with self.subTest(preset_id=pid):
                self.assertEqual(
                    p["params"].get("print_mode"),
                    "shelled_hollow",
                    f"Preset {pid} must explicitly use 'shelled_hollow'",
                )
                norm_p = normalize_params(p["params"])
                self.assertEqual(norm_p["print_mode"], "shelled_hollow")
                self.assertIs(norm_p["stl_always_open_hollow"], True)
                self.assertGreaterEqual(float(norm_p["wall_thickness_mm"]), 0.8)
                if norm_p["drainage"]["enabled"]:
                    has_drainage_preset = True

                # Export .STL for every builtin preset and verify open mouth (0 triangles at (0, 0, height_mm))
                fast_p = copy.deepcopy(norm_p)
                fast_p["resolution_angular"] = min(int(fast_p["resolution_angular"]), 96)
                fast_p["resolution_vertical"] = min(int(fast_p["resolution_vertical"]), 72)
                mesh = generate_vase_mesh(fast_p)
                stl_out = self.tmp_path / f"preset_{pid}.stl"
                write_binary_stl(stl_out, mesh, header_name=f"Preset:{pid}")
                stl_stats = self._inspect_binary_stl_open_mouth(stl_out, float(fast_p["height_mm"]))
                self.assertEqual(
                    stl_stats["top_center_cap_tris"],
                    0,
                    f"Preset {pid} exported .STL with {stl_stats['top_center_cap_tris']} mouth-closing triangles!",
                )
                self.assertGreater(
                    stl_stats["inward_cavity_tris"],
                    0,
                    f"Preset {pid} exported .STL with 0 inward cavity triangles!",
                )

        self.assertGreaterEqual(len(categories), 3, "Expected diverse preset categories")
        self.assertTrue(has_drainage_preset, "Expected at least one gardening/drainage preset")

    def test_05_user_presets_save_load_update_and_delete(self) -> None:
        preset_dir = self.tmp_path / "user_presets_store"
        self.assertEqual(load_user_presets(preset_dir), [])

        p1 = normalize_params({"name": "Vaso Zen", "height_mm": 175.0, "polygon_sides": 8})
        after_1 = save_user_preset(preset_dir, "Vaso Zen", p1)
        self.assertEqual(len(after_1), 1)
        id1 = after_1[0]["id"]
        self.assertTrue(bool(id1))

        # Large-format 450 mm tall x 380 mm diameter preset must roundtrip without 350/280 clamping
        p_large = normalize_params(
            {
                "name": "Maxi Coluna 450",
                "height_mm": 450.0,
                "base_diameter_mm": 240.0,
                "belly_diameter_mm": 380.0,
                "waist_diameter_mm": 300.0,
                "neck_diameter_mm": 320.0,
            }
        )
        save_user_preset(preset_dir, "Maxi Coluna 450", p_large, preset_id="maxi_450")
        reloaded_large = [u for u in load_user_presets(preset_dir) if u["id"] == "maxi_450"][0]
        self.assertEqual(reloaded_large["params"]["height_mm"], 450.0)
        self.assertEqual(reloaded_large["params"]["belly_diameter_mm"], 380.0)
        delete_user_preset(preset_dir, "maxi_450")

        p2 = normalize_params({"name": "Cachepo Mini", "height_mm": 95.0, "print_mode": "shelled_hollow"})
        after_2 = save_user_preset(preset_dir, "Cachepo Mini", p2)
        self.assertEqual(len(after_2), 2)
        id2 = [x["id"] for x in after_2 if x["id"] != id1][0]

        reloaded = load_user_presets(preset_dir)
        self.assertEqual(len(reloaded), 2)

        # Update existing preset by preset_id
        p1_updated = copy.deepcopy(p1)
        p1_updated["height_mm"] = 210.0
        after_upd = save_user_preset(preset_dir, "Vaso Zen XL", p1_updated, preset_id=id1)
        self.assertEqual(len(after_upd), 2)
        matched = [x for x in load_user_presets(preset_dir) if x["id"] == id1][0]
        self.assertEqual(matched["params"]["height_mm"], 210.0)

        # Delete first preset
        after_del1 = delete_user_preset(preset_dir, id1)
        self.assertEqual(len(after_del1), 1)
        self.assertEqual(after_del1[0]["id"], id2)

        # Deleting unknown id must be safe no-op
        after_noop = delete_user_preset(preset_dir, "non_existent_id_xyz")
        self.assertEqual(len(after_noop), 1)

        # Delete final preset
        after_del2 = delete_user_preset(preset_dir, id2)
        self.assertEqual(after_del2, [])
        self.assertEqual(load_user_presets(preset_dir), [])

    def test_06_generate_random_printable_params_across_15_seeds(self) -> None:
        heights_seen: set[float] = set()
        bases_seen: set[float] = set()

        for seed in range(1, 16):
            with self.subTest(seed=seed):
                rnd1 = generate_random_printable_params(seed=seed, current_params=DEFAULT_PARAMS)
                rnd2 = generate_random_printable_params(seed=seed, current_params=DEFAULT_PARAMS)
                self.assertEqual(rnd1, rnd2, f"Randomizer must be deterministic for seed={seed}")

                norm = normalize_params(rnd1)
                self.assertEqual(norm["print_mode"], "shelled_hollow")
                self.assertIs(norm["stl_always_open_hollow"], True)
                heights_seen.add(round(float(norm["height_mm"]), 2))
                bases_seen.add(round(float(norm["base_diameter_mm"]), 2))

                # Fast mesh & printability verification for every seed
                fast = copy.deepcopy(norm)
                fast["resolution_angular"] = 72
                fast["resolution_vertical"] = 60
                mesh = generate_vase_mesh(fast)

                self.assertTrue(np.all(np.isfinite(mesh.vertices)))
                self.assertAlmostEqual(float(mesh.vertices[:, 2].min()), 0.0, places=4)
                self.assertGreater(float(mesh.volume_cm3), 0.1)

                tri_v = mesh.vertices[mesh.triangles]
                top_cap_tris = int(
                    np.sum(
                        np.any(
                            (np.hypot(tri_v[:, :, 0], tri_v[:, :, 1]) < 1.0)
                            & (np.abs(tri_v[:, :, 2] - float(fast["height_mm"])) < 0.5),
                            axis=1,
                        )
                    )
                )
                self.assertEqual(top_cap_tris, 0, f"Seed {seed} unexpectedly closed the vase mouth")

                # Quick watertight check
                ec: Counter[tuple[int, int]] = Counter()
                for a, b, c in mesh.triangles.tolist():
                    ec[(a, b)] += 1
                    ec[(b, c)] += 1
                    ec[(c, a)] += 1
                open_edges = [e for e in ec if ec.get((e[1], e[0]), 0) != 1]
                self.assertEqual(len(open_edges), 0, f"Seed {seed} produced open boundary edges")

                rep = analyze_printability(mesh, fast)
                self.assertTrue(rep["fits_bed"], f"Seed {seed} exceeded default 220x220 bed")
                self.assertTrue(rep["fits_height"], f"Seed {seed} exceeded default 250mm height")

        self.assertGreaterEqual(len(heights_seen), 8, "Randomizer lacked height diversity across 15 seeds")
        self.assertGreaterEqual(len(bases_seen), 8, "Randomizer lacked base diameter diversity across 15 seeds")


if __name__ == "__main__":
    unittest.main(verbosity=2)
