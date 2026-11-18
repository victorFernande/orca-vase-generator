"""Build bilingual 1600x900 SVG banners using actual Vase Studio geometry.

Artwork template adapted from Orca Gear Studio (MIT; see LICENSE).
Copyright (c) 2026 Orca Gear Studio (shared artwork template).
Copyright (c) 2026 Orca Vase Studio (Vase artwork).
This is a development tool; it does not install or modify the plugin.
"""
from __future__ import annotations

import base64
from html import escape
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vase_studio.mesh_generator import generate_vase_mesh, generate_saucer_mesh
from vase_studio.schema import normalize_params
import numpy as np

OUT = ROOT / "assets" / "marketplace"
ACCENT = "#15dfae"
LANG = "en"


def tr(en, pt):
    return pt if LANG == "pt-BR" else en


def text(x, y, value, size=26, color="#eaf4f0", weight=400, spacing=0):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{escape(value)}</text>'


def right_text(x, y, value, size=18, color="#9cb8af", weight=400, spacing=1.5):
    return text(x,y,value,size,color,weight,spacing).replace('<text ', '<text text-anchor="end" ', 1)


def frame(section):
    return ['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
            '<style>text{font-family:Segoe UI,Arial,sans-serif}</style>',
            '<defs><radialGradient id="glow"><stop stop-color="#17483e"/><stop offset="1" stop-color="#11191b"/></radialGradient></defs>',
            '<rect width="1600" height="900" fill="#11191b"/>',
            '<ellipse cx="1200" cy="450" rx="660" ry="500" fill="url(#glow)"/>',
            '<path d="M64 112H1536M64 830H1536" stroke="#30443f"/>',
            text(64,71,"ORCA VASE STUDIO",25,ACCENT,700,3),
            right_text(1536,71,section),
            text(64,871,tr("PARAMETRIC VASES  /  NATIVE ORCASLICER PLUGIN","VASOS PARAMÉTRICOS  /  PLUGIN NATIVO DO ORCASLICER"),16,"#9cb8af",400,1.5),
            right_text(1536,854,tr("FREE + OPEN SOURCE","GRATUITO + CÓDIGO ABERTO"),14,ACCENT,600),
            right_text(1536,885,"By @VictorFernande",20,"#eaf4f0",600,0)]


def mesh_svg(mesh, x, y, width, height, color=(21,223,174), azimuth=-45, altitude=24):
    """Orthographic editorial projection of the real mesh, preserving its opening."""
    az, al = np.radians([azimuth,altitude])
    right = np.array([-np.sin(az),np.cos(az),0.0])
    camera = np.array([np.cos(az)*np.cos(al),np.sin(az)*np.cos(al),np.sin(al)])
    up = np.cross(camera,right)
    vertices = mesh.vertices.astype(float)
    xy = np.column_stack((vertices@right,-(vertices@up)))
    lo,hi = xy.min(axis=0),xy.max(axis=0)
    scale = min(width/(hi[0]-lo[0]),height/(hi[1]-lo[1]))
    xy = (xy-(lo+hi)/2)*scale+[x+width/2,y+height/2]
    depth = vertices@camera
    faces = mesh.triangles
    normals = mesh.face_normals.astype(float)
    visible = np.flatnonzero(normals@camera>1e-6)
    visible = visible[np.argsort(depth[faces[visible]].mean(axis=1))]
    light = np.array([-.35,-.45,1.0]); light/=np.linalg.norm(light)
    shade = np.clip(.43+.57*np.maximum(0,normals@light),.35,1)
    parts=['<g stroke-linejoin="round">']; paths=[]; last_fill=None
    def flush():
        if paths:
            parts.append(f'<path d="{"".join(paths)}" fill="{last_fill}" stroke="{last_fill}" stroke-width="0.35"/>')
            paths.clear()
    for i in visible:
        rgb=np.clip(np.array(color)*shade[i],0,255).astype(int)
        fill='#'+''.join(f'{v:02x}' for v in rgb)
        if fill!=last_fill:
            flush(); last_fill=fill
        points=xy[faces[i]]
        paths.append(f'M{points[0,0]:.3f},{points[0,1]:.3f}L{points[1,0]:.3f},{points[1,1]:.3f}L{points[2,0]:.3f},{points[2,1]:.3f}Z')
    flush(); parts.append('</g>')
    return ''.join(parts)


def params(kind="waves", **overrides):
    textures={name:{"enabled":name==kind} for name in ("ribbed","waves","origami","cellular")}
    textures["ribbed"].update({"count":30,"depth_mm":3.2,"twist_deg":65})
    return normalize_params({"resolution_angular":128,"resolution_vertical":100,"textures":textures,**overrides})


def write(name, parts):
    target=OUT/(name+'.svg')
    target.write_text('\n'.join(parts)+'\n</svg>\n',encoding='utf-8',newline='\n')
    print(f'{target.name}: {target.stat().st_size:,} bytes')


def main():
    global LANG
    OUT.mkdir(parents=True,exist_ok=True)
    meshes={kind:generate_vase_mesh(params(kind)) for kind in ("ribbed","waves","origami","cellular")}
    variants={kind:mesh_svg(mesh,0,0,300,340) for kind,mesh in meshes.items()}
    hero=mesh_svg(meshes['waves'],810,150,710,620)
    gardening=params('ribbed',height_mm=90,base_diameter_mm=100,belly_diameter_mm=124,
                     waist_diameter_mm=126,neck_diameter_mm=130,lip_flare_mm=1,
                     wall_thickness_mm=3,bottom_thickness_mm=3,
                     drainage={"enabled":True,"hole_count":5,"hole_diameter_mm":8})
    planter=mesh_svg(generate_vase_mesh(gardening),825,170,710,380,altitude=65)
    saucer=mesh_svg(generate_saucer_mesh(gardening),865,590,630,175,altitude=40,color=(239,176,99))
    screenshot=base64.b64encode((OUT/'source-inspection.png').read_bytes()).decode('ascii')
    for LANG in ('en','pt-BR'):
        p=frame(tr('01 / CREATE','01 / CRIE'))
        p += [text(64,202,tr('FROM AN IDEA','DA IDEIA À PEÇA'),21,ACCENT,600,3),
              text(58,309,tr('YOUR VASE.','VASOS.'),85,weight=750),
              text(58,411,tr('YOUR STYLE.','DO SEU JEITO.'),tr(85,73),ACCENT,750),
              text(64,493,tr('Shape, texture and inspect.','Modele, texturize e inspecione.'),30),
              text(64,539,tr('Without leaving OrcaSlicer.','Sem sair do OrcaSlicer.'),30,'#9cb8af'),
              '<rect x="64" y="601" width="610" height="56" rx="28" fill="#19362e" stroke="#2e6b57"/>',
              text(88,638,tr('VASES  /  PLANTERS  /  MATCHING SAUCERS','VASOS  /  CACHEPÔS  /  PRATINHOS'),20,ACCENT,600),
              text(64,748,tr('FROM SILHOUETTE TO SURFACE','DA SILHUETA À SUPERFÍCIE'),19,weight=700,spacing=2),
              text(64,783,tr('Dimensional sliders + freeform 2D curve','Controles de medidas + curva livre 2D'),23,'#9cb8af'),
              hero,text(1030,797,tr('ACTUAL PLUGIN GEOMETRY','GEOMETRIA REAL DO PLUGIN'),16,'#9cb8af',400,2)]
        write('01-vase-studio-'+LANG,p)

        p=frame(tr('02 / TEXTURES','02 / TEXTURAS'))
        p += [text(64,204,tr('FOUR TEXTURES. MIX YOUR OWN.','QUATRO TEXTURAS. COMBINE DO SEU JEITO.'),tr(55,50),weight=700),
              text(64,253,tr('Layer relief, density and twist to create a surface that is yours.','Combine relevo, densidade e torção para criar uma superfície própria.'),26,'#9cb8af')]
        cards=[('ribbed',tr('RIBBED / FLUTED','CANAIS / FRISOS'),tr('Ribs, spacing and helical twist.','Frisos, espaçamento e torção.')),
               ('waves',tr('ORGANIC WAVES','ONDAS ORGÂNICAS'),tr('Flowing, layered undulations.','Ondulações e ritmo orgânico.')),
               ('origami',tr('ORIGAMI DIAMOND','ORIGAMI DIAMANTE'),tr('Geometric folds and creases.','Dobras e vincos geométricos.')),
               ('cellular',tr('CELLULAR / CORAL','CELULAR / CORAL'),tr('Dimensional organic relief.','Relevo orgânico dimensional.'))]
        for i,(kind,title,subtitle) in enumerate(cards):
            x=64+i*375
            p += [f'<rect x="{x}" y="300" width="347" height="480" rx="20" fill="#172123" stroke="#30443f"/>',
                  text(x+20,347,f'0{i+1}',19,ACCENT,600,2),
                  f'<g transform="translate({x+23},350)">{variants[kind]}</g>',
                  text(x+20,718,title,22,weight=700),text(x+20,756,subtitle,17,'#9cb8af')]
        write('02-surface-textures-'+LANG,p)

        p=frame(tr('03 / INSPECT','03 / INSPECIONE'))
        p += [text(64,247,tr('SEE INSIDE.','VEJA POR DENTRO.'),tr(65,56),weight=700),
              text(64,325,tr('MEASURE IN mm.','MEÇA EM mm.'),61,ACCENT,700),
              text(64,417,tr('Hollow walls, cut views and calipers.','Paredes ocas, cortes e cotas.'),28),
              text(64,462,tr('Inspect the model before slicing.','Confira o modelo antes de fatiar.'),26,'#9cb8af'),
              text(64,573,tr('01   X-RAY + WALL DIMENSIONS','01   RAIO-X + COTAS DA PAREDE'),22,ACCENT,600),
              text(64,635,tr('02   VERTICAL + HORIZONTAL CUTS','02   CORTES VERTICAL + HORIZONTAL'),22,ACCENT,600),
              text(64,697,tr('03   OVERHANG HEATMAP','03   MAPA DE OVERHANG'),22,ACCENT,600),
              '<rect x="704" y="175" width="832" height="580" rx="14" fill="#1d2528" stroke="#496057"/>',
              f'<image href="data:image/png;base64,{screenshot}" x="716" y="187" width="808" height="556" preserveAspectRatio="xMidYMid meet"/>',
              text(925,788,tr('ACTUAL PLUGIN SCREENSHOT','CAPTURA REAL DO PLUGIN'),16,'#9cb8af',400,2)]
        write('03-wall-inspection-'+LANG,p)

        p=frame(tr('04 / PLANTERS','04 / CACHEPÔS'))
        p += [text(64,235,tr('PLANTERS.','CACHEPÔS.'),79,weight=750),
              text(64,330,tr('WITH THE','COM OS'),71,ACCENT,750),
              text(64,425,tr('DETAILS.','DETALHES.'),71,ACCENT,750),
              text(64,508,tr('Drainage and a matching saucer.','Drenagem e um pratinho coordenado.'),28),
              text(64,552,tr('Design both in the same workspace.','Projete os dois no mesmo lugar.'),26,'#9cb8af'),
              text(64,647,tr('01   CONFIGURABLE DRAINAGE','01   DRENAGEM CONFIGURÁVEL'),22,ACCENT,600),
              text(64,705,tr('02   SAUCER WITH RAISED INNER RIBS','02   PRATO COM NERVURAS INTERNAS'),22,ACCENT,600),
              text(64,783,tr('STL / 3MF export + build-plate delivery','Exportação STL / 3MF + envio à mesa'),23,'#9cb8af'),
              planter,saucer,
              text(1090,568,tr('PLANTER','CACHEPÔ'),16,'#9cb8af',600,2),
              text(1000,798,tr('MATCHING SAUCER','PRATINHO COORDENADO'),16,'#9cb8af',600,2)]
        write('04-planter-saucer-'+LANG,p)


if __name__=='__main__':
    main()
