"""Closed ribbon shells, reference-coordinate fixtures and real JS mesh parity."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import test_geometry_manifold as _setup
import numpy as np
from vase_studio.ribbon_geometry import ribbon_plan, build_ribbon_mesh, RIBBON_JS
from vase_studio.mesh_generator import generate_vase_mesh
from vase_studio.schema import normalize_params
from vase_studio.printability import analyze_printability


def ribbon_params(**overrides):
    return normalize_params({"height_mm": 60, "resolution_angular": 96, "resolution_vertical": 60,
        "textures": {"geometric": {"enabled": True, "pattern": "folded_petals",
            "cells_around": 3, "cells_vertical": 4, "ribbon_quality": "draft", **overrides}}})


class TestRibbonGeometry(unittest.TestCase):
    def assert_closed_oriented_shell(self, vertices, triangles):
        self.assertTrue(np.isfinite(vertices).all())
        edges = np.concatenate((triangles[:, [0, 1]], triangles[:, [1, 2]], triangles[:, [2, 0]]))
        undirected = np.sort(edges, axis=1)
        _, inverse, counts = np.unique(undirected, axis=0, return_inverse=True, return_counts=True)
        np.testing.assert_array_equal(counts, 2)
        sums = np.bincount(inverse, weights=np.where(edges[:, 0] < edges[:, 1], 1, -1))
        np.testing.assert_array_equal(sums, 0)
        self.assertEqual(len(vertices) - len(counts) + len(triangles), 2)
        a, b, c = vertices[triangles[:, 0]], vertices[triangles[:, 1]], vertices[triangles[:, 2]]
        cross = np.cross(b - a, c - a)
        self.assertGreater(float(np.linalg.norm(cross, axis=1).min()), 1e-8)
        self.assertGreater(float(np.einsum('ij,ij->', a, cross) / 6), 0)
        # Prove connectivity, rather than deriving it from an Euler sum.
        adjacency = [[] for _ in vertices]
        for a, b in edges:
            adjacency[a].append(b)
        visited = {0}
        todo = [0]
        while todo:
            for nxt in adjacency[todo.pop()]:
                if nxt not in visited:
                    visited.add(int(nxt)); todo.append(int(nxt))
        self.assertEqual(len(visited), len(vertices))

    def test_every_ribbon_is_closed_oriented_connected_and_positive(self):
        p = ribbon_params()
        plan = ribbon_plan(p)
        vertices, triangles = build_ribbon_mesh(p, np.full(plan["nz"] + 1, 50.0))
        self.assertEqual(vertices.shape, (plan["vertices"], 3))
        self.assertEqual(triangles.shape, (plan["triangles"], 3))
        per_v, per_f = plan["vertices"] // 3, plan["triangles"] // 3
        for i in range(3):
            self.assert_closed_oriented_shell(vertices[i * per_v:(i + 1) * per_v],
                triangles[i * per_f:(i + 1) * per_f] - i * per_v)
        self.assertEqual(float(vertices[:, 2].min()), 0)
        self.assertEqual(float(vertices[:, 2].max()), p["height_mm"])

    def test_reference_coordinate_fixture(self):
        fixture = json.loads((Path(__file__).parent / 'fixtures/vase_maker_ribbon_samples.json').read_text(encoding='utf8'))
        p = ribbon_params(**fixture['geometric'])
        plan = ribbon_plan(p)
        vertices, _ = build_ribbon_mesh(p, np.full(plan['nz'] + 1, 50.0))
        for item in fixture['samples']:
            np.testing.assert_allclose(vertices[item['index']], item['position'], atol=1e-10, rtol=1e-10)

    def test_quality_and_actual_vase_boundaries_and_warning(self):
        sizes = []
        for quality in ('draft', 'normal', 'fine'):
            p = ribbon_params(ribbon_quality=quality)
            sizes.append(ribbon_plan(p)['triangles'])
        self.assertLess(sizes[0], sizes[1]); self.assertLess(sizes[1], sizes[2])
        adaptive = ribbon_params(ribbon_quality='adaptive', ribbon_nozzle_mm=0.4)
        small_nozzle = ribbon_plan(adaptive)
        adaptive['textures']['geometric']['ribbon_nozzle_mm'] = 0.8
        self.assertLess(ribbon_plan(adaptive)['triangles'], small_nozzle['triangles'])
        p = ribbon_params()
        mesh = generate_vase_mesh(p)
        self.assertAlmostEqual(mesh.bounds_mm['min'][2], 0)
        self.assertAlmostEqual(mesh.bounds_mm['max'][2], p['height_mm'])
        self.assertGreater(len(mesh.triangles), ribbon_plan(p)['triangles'])
        report = analyze_printability(mesh, p)
        self.assertIn('RIBBON_ASSEMBLY', [w['code'] for w in report['warnings']])
        self.assertEqual(report['triangle_count'], len(mesh.triangles))

    def test_constraints_are_explicit_and_large_mesh_is_rejected_before_allocating(self):
        p = ribbon_params()
        p['print_mode'] = 'spiral_vase'; p['polygon_sides'] = 6
        p['textures']['waves']['enabled'] = True
        normalized = normalize_params(p)
        self.assertEqual(normalized['print_mode'], 'shelled_hollow')
        self.assertEqual(normalized['polygon_sides'], 0)
        self.assertFalse(normalized['textures']['waves']['enabled'])
        p = ribbon_params(cells_around=36, cells_vertical=24, ribbon_quality='fine')
        p['height_mm'] = 500
        with self.assertRaisesRegex(ValueError, 'too large'):
            generate_vase_mesh(p)
        p = ribbon_params()
        p.update(wall_thickness_mm=25, use_custom_profile=True, profile_points=[[0, 8], [1, 10]])
        with self.assertRaisesRegex(ValueError, 'too narrow'):
            generate_vase_mesh(p)

    @unittest.skipUnless(shutil.which('node'), 'Node required for production JS parity')
    def test_browser_and_numpy_positions_and_oriented_triangles_match(self):
        p = ribbon_params(twist_deg=-85, phase_deg=37, strength_middle=0.35)
        plan = ribbon_plan(p)
        radii = (50 + 4 * np.sin(np.linspace(0, np.pi, plan['nz'] + 1))).tolist()
        vertices, triangles = build_ribbon_mesh(p, radii)
        script = RIBBON_JS + "\nconst d=JSON.parse(require('fs').readFileSync(0,'utf8')),m=buildRibbonMesh(d.p,d.radii,false);console.log(JSON.stringify({positions:Array.from(m.positions),indices:Array.from(m.indices)}));"
        result = subprocess.run([shutil.which('node'), '-e', script], input=json.dumps({'p':p,'radii':radii}),
            text=True, capture_output=True, check=True)
        actual = json.loads(result.stdout)
        np.testing.assert_allclose(np.asarray(actual['positions']).reshape(-1,3), vertices, atol=4e-6, rtol=1e-7)
        def canonical(a):
            a = np.asarray(a).reshape(-1,3)
            a = np.stack([np.roll(row,-int(np.argmin(row))) for row in a])
            return a[np.lexsort((a[:,2],a[:,1],a[:,0]))]
        np.testing.assert_array_equal(canonical(actual['indices']), canonical(triangles))

    def test_three_distribution_formats_generate_ribbons_without_source_checkout(self):
        root = Path(__file__).resolve().parents[1]
        artifacts = [root / 'dist/orca_vase_generator.py', root / 'dist/orca_vase_generator_any.py',
                     root / 'dist/orca_vase_generator-1.3.0-py3-none-any.whl']
        code = r'''
import sys,importlib.util,zipfile
from pathlib import Path
p=Path(sys.argv[1])
if p.suffix=='.whl':
 sys.path.insert(0,str(p))
 import vase_studio as api
 from vase_studio.studio_ui import get_studio_html
 assert api.__version__=='1.3.0'
 with zipfile.ZipFile(p) as z:
  notice=z.read('vase_studio/ribbon_geometry.py').decode()
  assert 'Copyright (c) 2026 Dante x' in notice and 'Permission is hereby granted' in notice
else:
 spec=importlib.util.spec_from_file_location('ribbon_isolated',p)
 api=importlib.util.module_from_spec(spec);sys.modules[spec.name]=api;spec.loader.exec_module(api)
 get_studio_html=api.get_studio_html
 notice=p.read_text(encoding='utf8')
 assert 'Copyright (c) 2026 Dante x' in notice and 'Permission is hereby granted' in notice
params=api.normalize_params({'height_mm':60,'resolution_angular':96,'resolution_vertical':60,'textures':{'geometric':{'enabled':True,'pattern':'folded_petals','cells_around':3,'cells_vertical':4,'ribbon_quality':'draft'}}})
mesh=api.generate_vase_mesh(params)
assert len(mesh.triangles)>30000 and mesh.volume_cm3>0
assert mesh.bounds_mm['min'][2]==0 and mesh.bounds_mm['max'][2]==60
assert 'sel-ribbon-quality' in get_studio_html('dock',{'params':params})
'''
        with tempfile.TemporaryDirectory() as isolated:
            for artifact in artifacts:
                result = subprocess.run([sys.executable,'-I','-B','-W','error','-c',code,str(artifact)],
                    cwd=isolated,text=True,capture_output=True)
                self.assertEqual(result.returncode,0,(artifact.name,result.stderr))


if __name__ == '__main__':
    unittest.main()
