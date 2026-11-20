"""Message adapters for discovered offline JSON language packs.

Catalog text lives in locales/*.json; this module contains only stable English
message identifiers and the public formatting adapters used by UI and controller.
"""
from __future__ import annotations
from .language_packs import load_language_packs, resolve_language, language_pack_payload

UI_MESSAGES = {'btn_surprise': 'Surprise Me',
 'tab_shape': 'Shape',
 'tab_textures': 'Textures',
 'tab_print': 'Wall & Print',
 'tab_presets': 'Presets',
 'sec_presets': 'Preset Gallery',
 'btn_save_preset': '+ Save',
 'btn_ok': 'Save',
 'cat_all': 'All',
 'cat_organic': 'Organic',
 'cat_geometric': 'Geometric',
 'cat_planter': 'Planters',
 'cat_user': 'Saved',
 'sec_silhouette': 'Silhouette & 2D Curve',
 'mode_sliders': 'Sliders',
 'mode_curve': 'Freeform 2D Curve',
 'btn_to_curve': 'Sliders → Curve',
 'hint_curve_sliders': 'Drag handles directly on the 2D silhouette or fine-tune sliders below.',
 'hint_curve_free': 'Drag knots · Click curve to add knot · Double-click/right-click interior knot '
                    'to remove.',
 'sec_resolution': 'Mesh Resolution',
 'mat_emerald': 'Orca Emerald Silk',
 'mat_terracotta': 'Terracotta Clay',
 'mat_white': 'Matte White Ceramic',
 'mat_copper': 'Copper Bronze',
 'mat_xray': '🔬 X-Ray / Wall (Translucent)',
 'mat_heatmap': 'Overhang Heatmap (°)',
 'vp_xray': '🔬 X-Ray / Wall',
 'vp_calipers': '📏 mm Calipers',
 'vp_heatmap': '🔥 Overhang',
 'vp_wire': '⌗ Wireframe',
 'vp_saucer': '🍽 Saucer',
 'vp_layout_nested': 'Nested',
 'vp_layout_side': 'Side-by-Side',
 'hud_title': 'Printability',
 'hud_wall_floor': 'Wall / Floor',
 'hud_mouth_hole': 'Ø Mouth Bore',
 'hud_dims': 'Dimensions (mm)',
 'hud_overhang': 'Max Overhang',
 'hud_weight': 'Est. Filament',
 'hud_Tris': 'Triangles',
 'leg_outer': 'Outer Wall',
 'leg_inner': 'Cavity & Floor',
 'cam_front': 'Front',
 'cam_top': 'Top',
 'cam_bottom': 'Bottom',
 'cam_fit': 'Fit View',
 'vp_cut': '✂ Cross-Section Cut',
 'vp_cut_y': '✂ Vertical Cut (Profile Y)',
 'vp_cut_z': '💿 Horizontal Z Slice (Plan 5%–100%)',
 'sec_envelope': 'Envelope & Global Twist',
 'sec_textures': 'Combinable Textures',
 'tex_ribbed': 'Ribbed / Fluted',
 'tex_waves': 'Organic Waves',
 'tex_origami': 'Origami Diamond',
 'tex_cellular': 'Cellular / Coral 3D',
 'lbl_ridge_mode': 'Ridged Coral Veins',
 'sec_print_mode': 'Wall & Opening (mm)',
 'mode_hollow': 'True Hollow Vase (mm Wall)',
 'mode_spiral': 'Spiral Mode (1 Line)',
 'lbl_stl_open_hollow': 'Always keep open mouth on .STL export',
 'note_spiral_honest': 'Spiral Mode builds a solid base block whose top is removed by the slicer '
                       '(.3MF). Keep the toggle below checked so .STL exports stay open!',
 'banner_spiral_safe': 'Spiral Mode: solid base block for .3MF (slicer removes top) · .STL '
                       'protected w/ Open Mouth',
 'banner_spiral_closed': 'Warning: Solid Spiral Block — .STL will export CLOSED at top for Spiral '
                         'Slicing!',
 'perim_hint_fmt': '≈ {n} loops of {lw} mm · Bore Ø {id} mm',
 'spiral_floor_fmt': '≈ {mm} mm floor ({n} lay.) · Nozzle {noz}mm (ideal {wmin}–{wmax} mm)',
 'wall_badge_hollow': 'Hollow · {w} mm',
 'wall_badge_spiral': 'Spiral · {w} mm',
 'cal_ext': 'Ø Outer: {v} mm',
 'cal_hole': 'Ø Bore: {v} mm',
 'cal_wall': 'Wall: {v} mm',
 'cal_wall_range': 'Wall: {v} mm ({min}–{max} mm)',
 'cal_floor': 'Bottom: {v} mm',
 'cal_z_slice': '💿 Z Slice = {z} mm ({pct}%)',
 'lbl_2d_wall': 'Wall {v} mm',
 'lbl_2d_floor': 'Bottom {v} mm',
 'lbl_2d_hole': 'Ø Bore {v} mm',
 'lbl_2d_spiral_cap': 'Spiral Cap (.3MF)',
 'lbl_auto_slicer': 'Auto-configure OrcaSlicer on send',
 'lbl_spiral_smooth': 'Smooth Spiral XY Seam',
 'lbl_clamp_overhang': 'Auto-Clamp Overhang Slope',
 'sec_gardening': 'Gardening: Drainage & Saucer',
 'lbl_drainage': 'Bottom Drainage Holes',
 'note_drainage_spiral': 'Smart blind cavities through solid bottom layers: real drainage holes '
                         'without breaking single-contour Spiral Vase!',
 'note_drainage_hollow': 'Watertight cylindrical drainage tunnels straight through the hollow pot '
                         'floor.',
 'lbl_include_saucer': 'Include Matching Saucer',
 'warn_saucer_spiral': 'Vase + Saucer together automatically switch to Open Hollow Mesh on '
                       'send/export.',
 'lbl_saucer_tex': 'Match Vase Texture on Saucer',
 'btn_send_plater': 'Send to OrcaSlicer Plater',
 'btn_exp_3mf': 'Export .3MF',
 'btn_exp_stl': 'Export .STL',
 'poly_circle': 'Smooth Circle',
 'poly_sides_fmt': '{n}-Gon',
 'active_tex_fmt': '{n} active',
 'bed_exceeded': 'Exceeds printer build volume ({bx}×{by}×{bz} mm)!',
 'btn_fit_printer': 'Fit to Printer',
 'printer_sync_tip': 'Click to sync active OrcaSlicer printer',
 'toast_printer_synced': 'Synced active printer: {name} ({dims})',
 'toast_fitted_printer': 'Dimensions fitted to {name} build volume!',
 'status_ok': 'PRINTABLE',
 'status_warn': 'WARNING',
 'status_crit': 'CRITICAL',
 'toast_randomized': 'Generated printable vase design!',
 'toast_preset_saved': 'Preset saved!',
 'toast_converted_curve': 'Converted sliders to PCHIP Freeform Curve!',
 'btn_off': 'Off'}


UI_MESSAGES.update({'tex_geometric': 'Geometric Relief', 'lbl_geometric_pattern': 'Sidewall Pattern', 'pattern_diamond': 'Diamond Facets', 'pattern_leaf_scales': 'Leaf Scales', 'pattern_crater_cells': 'Crater Cells', 'pattern_folded_petals': 'Folded Petals', 'pattern_spiral_bloom': 'Spiral Bloom', 'pattern_ripple': 'Ripple Rings', 'pattern_coral': 'Coral Lattice', 'hint_geometric': 'Relief is part of the wall. Combine layers or disable other textures for a clean pattern.'})

UI_MESSAGES.update({'lbl_ribbon_quality': 'Ribbon Quality', 'quality_draft': 'Draft', 'quality_normal': 'Normal', 'quality_fine': 'Fine', 'quality_adaptive': 'Adaptive', 'hint_ribbons': 'Round hollow cup with closed overlapping ribbons. Check the sliced result. Spiral mode and other textures are unavailable.'})


def discovered_language_packs() -> dict:
    return load_language_packs()[0]


def supported_languages() -> tuple[str, ...]:
    return tuple(discovered_language_packs())


def normalize_language(value: object, default: str = "pt") -> str:
    return resolve_language(value, discovered_language_packs(), default)


def locale_vocabulary() -> dict[str, dict[str, str]]:
    return {code: pack["translations"] for code, pack in discovered_language_packs().items()}


def locale_payload(packs: dict | None = None) -> dict:
    packs = discovered_language_packs() if packs is None else packs
    return {"metadata": language_pack_payload(packs),
            "vocabulary": {code: pack["translations"] for code, pack in packs.items()},
            "messages": UI_MESSAGES}


def translate_text(text: str, language: object) -> str:
    packs = discovered_language_packs()
    code = resolve_language(language, packs)
    return packs[code]["translations"].get(text, text)
