"""Curled ribbon surfaces adapted from Vase Maker 0.8.19 (MIT).

Copyright (c) 2026 Dante x, original ribbon construction.
Copyright (c) 2026 Orca Vase Studio, vectorized and browser implementations.
SPDX-License-Identifier: MIT

Source: https://cloud.orcaslicer.com/p/3e9de58df37d
The cup and ribbons are separately closed solids, as in the reference. This
module does not claim to Boolean-union intersecting surfaces.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from __future__ import annotations

import math


def ribbon_plan(params: dict, interactive: bool = False) -> dict:
    g = params["textures"]["geometric"]
    quality = "draft" if interactive else g["ribbon_quality"]
    dz, row_factor, width_steps = {
        "draft": (1.5, 8, 16), "normal": (0.55, 16, 24),
        "fine": (0.28, 28, 36), "adaptive": (0.6, 14, 22),
    }[quality]
    if quality == "adaptive":
        nozzle = g["ribbon_nozzle_mm"]
        dz = max(0.55, nozzle * 1.5)
        width_steps = min(28, max(12, math.ceil(g["ribbon_width_mm"] / max(1.6, nozzle * 4))))
    nz = min(1200, max(g["cells_vertical"] * row_factor, math.ceil(params["height_mm"] / dz)))
    vertices_per_ribbon = 2 * (width_steps + 1) * (nz + 1)
    triangles_per_ribbon = 4 * width_steps * nz + 4 * nz + 4 * width_steps
    count = g["cells_around"]
    return {"nz": nz, "nu": width_steps, "count": count,
            "vertices": count * vertices_per_ribbon,
            "triangles": count * triangles_per_ribbon}


def ribbon_triangles(nz: int, nu: int):
    """Oriented, closed boundary of one thick rectangular parametric strip."""
    import numpy as np

    grid = np.arange((nz + 1) * (nu + 1), dtype=np.int32).reshape(nz + 1, nu + 1)
    back = grid.size
    a, b, c, d = grid[:-1, :-1], grid[:-1, 1:], grid[1:, 1:], grid[1:, :-1]
    chunks = [np.stack((a, b, c), -1).reshape(-1, 3), np.stack((a, c, d), -1).reshape(-1, 3),
              np.stack((a + back, d + back, c + back), -1).reshape(-1, 3),
              np.stack((a + back, c + back, b + back), -1).reshape(-1, 3)]
    # Traverse the perimeter in the front surface's CCW parameter order.
    loop = np.concatenate((grid[0, :], grid[1:, -1], grid[-1, -2::-1], grid[-2:0:-1, 0]))
    nxt = np.roll(loop, -1)
    chunks += [np.column_stack((loop, loop + back, nxt + back)),
               np.column_stack((loop, nxt + back, nxt))]
    return np.concatenate(chunks)


def build_ribbon_mesh(params: dict, profile_radii, interactive: bool = False):
    """Vectorize the reference's midpoint/normal/offset construction per ribbon."""
    import numpy as np

    g = params["textures"]["geometric"]
    plan = ribbon_plan(params, interactive)
    nz, nu, count = plan["nz"], plan["nu"], plan["count"]
    radii = np.asarray(profile_radii, dtype=np.float64)
    if radii.shape != (nz + 1,):
        raise ValueError("Ribbon profile sampling does not match the mesh plan")
    t = np.linspace(0, 1, nz + 1)[:, None]
    q = np.linspace(0, 1, nu + 1)[None, :]
    strength = np.where(t <= 0.5,
        g["strength_bottom"] + (g["strength_middle"] - g["strength_bottom"]) * 2 * t,
        g["strength_middle"] + (g["strength_top"] - g["strength_middle"]) * 2 * (t - 0.5))
    twist = math.radians(g["twist_deg"] + params["global_twist_deg"])
    phase = math.radians(g["phase_deg"])
    vertices = []
    triangles = []
    strip_tris = ribbon_triangles(nz, nu)
    vertex_offset = 0
    for strip in range(count):
        row_phase = 2 * math.pi * g["ribbon_stagger"] * (strip % 2)
        blend = 0.5 + 0.5 * np.cos(2 * math.pi * g["cells_vertical"] * t + row_phase)
        blend = blend * blend * (3 - 2 * blend) * np.clip(strength, 0, 1.5)
        sweep = math.radians(32) + (math.radians(g["ribbon_curl_deg"]) - math.radians(32)) * blend
        arc_length = g["ribbon_width_mm"] * (1 + g["ribbon_stretch_pct"] / 100 * blend)
        base_radius = arc_length / sweep
        theta = (q - 0.5) * sweep
        local_radius = base_radius + g["ribbon_overlap_mm"] * blend * (0.5 - q)
        tangent = local_radius * np.sin(theta)
        radial = base_radius - local_radius * np.cos(theta)
        radial += 0.35 * g["ribbon_overlap_mm"] * blend * np.tanh((0.5 - q) * 7) * np.abs(2 * q - 1) ** 1.8
        center = 2 * math.pi * strip / count + twist * t + phase
        radius = radii[:, None] + radial
        mid = np.stack((radius * np.cos(center) - tangent * np.sin(center),
                        radius * np.sin(center) + tangent * np.cos(center),
                        np.broadcast_to(t * params["height_mm"], radius.shape)), axis=-1)
        # Centered differences match the reference's endpoint-aware tangents.
        tu = np.concatenate((mid[:, 1:2] - mid[:, :1], mid[:, 2:] - mid[:, :-2], mid[:, -1:] - mid[:, -2:-1]), axis=1)
        tz = np.concatenate((mid[1:2] - mid[:1], mid[2:] - mid[:-2], mid[-1:] - mid[-2:-1]), axis=0)
        normals = np.cross(tu, tz)
        lengths = np.linalg.norm(normals, axis=-1, keepdims=True)
        if np.any(lengths < 1e-10):
            raise ValueError("Ribbon surface has a collapsed tangent; adjust width, curl or overlap")
        normals /= lengths
        edge = np.clip(np.minimum(q, 1 - q) / 0.12, 0, 1)
        edge = edge * edge * (3 - 2 * edge)
        thickness = g["ribbon_thickness_mm"] / (1 + g["ribbon_stretch_pct"] / 100 * blend)
        thickness = thickness * (0.35 + 0.65 * edge)
        front = mid + normals * thickness[..., None] * 0.5
        back = mid - normals * thickness[..., None] * 0.5
        for face in (front, back):
            np.clip(face[:, :, 2], 0, params["height_mm"], out=face[:, :, 2])
            face[0, :, 2] = 0
            face[-1, :, 2] = params["height_mm"]
        verts = np.concatenate((front.reshape(-1, 3), back.reshape(-1, 3)))
        vertices.append(verts)
        triangles.append(strip_tris + vertex_offset)
        vertex_offset += len(verts)
    return np.concatenate(vertices), np.concatenate(triangles)


RIBBON_JS = r"""
  function ribbonPlan(p, interactive) {
    const g=p.textures.geometric;
    const nozzle=g.ribbon_nozzle_mm;
    const spec={draft:[1.5,8,16],normal:[0.55,16,24],fine:[0.28,28,36],adaptive:[Math.max(0.55,nozzle*1.5),14,Math.min(28,Math.max(12,Math.ceil(g.ribbon_width_mm/Math.max(1.6,nozzle*4))))]}[interactive?'draft':g.ribbon_quality];
    const nz=Math.min(1200,Math.max(g.cells_vertical*spec[1],Math.ceil(p.height_mm/spec[0]))),nu=spec[2],count=g.cells_around;
    return {nz,nu,count,vertices:count*2*(nu+1)*(nz+1),triangles:count*(4*nu*nz+4*nz+4*nu)};
  }
  function buildRibbonMesh(p, profileRadii, interactive) {
    const g=p.textures.geometric,plan=ribbonPlan(p,interactive),{nz,nu,count}=plan;
    const positions=new Float32Array(plan.vertices*3),indices=new Uint32Array(plan.triangles*3);
    const normals=new Float32Array(positions.length),overhangs=new Float32Array(plan.vertices);
    const parts=new Float32Array(plan.vertices),roles=new Float32Array(plan.vertices);
    const perSide=(nz+1)*(nu+1),perStrip=2*perSide;
    let ti=0;
    const tri=(a,b,c)=>{indices[ti++]=a;indices[ti++]=b;indices[ti++]=c;};
    for(let strip=0;strip<count;strip++) {
      const mid=new Float64Array(perSide*3),thickness=new Float64Array(perSide);
      for(let iz=0;iz<=nz;iz++) {
        const t=iz/nz,strength=t<=0.5?g.strength_bottom+(g.strength_middle-g.strength_bottom)*2*t:g.strength_middle+(g.strength_top-g.strength_middle)*2*(t-0.5);
        let blend=0.5+0.5*Math.cos(2*Math.PI*g.cells_vertical*t+2*Math.PI*g.ribbon_stagger*(strip%2));
        blend=blend*blend*(3-2*blend)*Math.max(0,Math.min(1.5,strength));
        const sweep=32*Math.PI/180+(g.ribbon_curl_deg-32)*Math.PI/180*blend;
        const baseRadius=g.ribbon_width_mm*(1+g.ribbon_stretch_pct/100*blend)/sweep;
        const center=2*Math.PI*strip/count+(g.twist_deg+p.global_twist_deg)*Math.PI/180*t+g.phase_deg*Math.PI/180;
        const cc=Math.cos(center),ss=Math.sin(center);
        for(let iu=0;iu<=nu;iu++) {
          const q=iu/nu,theta=(q-0.5)*sweep,localRadius=baseRadius+g.ribbon_overlap_mm*blend*(0.5-q);
          const tangent=localRadius*Math.sin(theta);
          let radial=baseRadius-localRadius*Math.cos(theta);
          radial+=0.35*g.ribbon_overlap_mm*blend*Math.tanh((0.5-q)*7)*Math.abs(2*q-1)**1.8;
          const radius=profileRadii[iz]+radial,k=iz*(nu+1)+iu;
          mid[k*3]=radius*cc-tangent*ss;mid[k*3+1]=radius*ss+tangent*cc;mid[k*3+2]=t*p.height_mm;
          let edge=Math.max(0,Math.min(1,Math.min(q,1-q)/0.12));edge=edge*edge*(3-2*edge);
          thickness[k]=g.ribbon_thickness_mm/(1+g.ribbon_stretch_pct/100*blend)*(0.35+0.65*edge);
        }
      }
      const offset=strip*perStrip;
      for(let iz=0;iz<=nz;iz++) for(let iu=0;iu<=nu;iu++) {
        const k=iz*(nu+1)+iu,ua=(iz*(nu+1)+Math.max(0,iu-1))*3,ub=(iz*(nu+1)+Math.min(nu,iu+1))*3;
        const za=(Math.max(0,iz-1)*(nu+1)+iu)*3,zb=(Math.min(nz,iz+1)*(nu+1)+iu)*3;
        const ux=mid[ub]-mid[ua],uy=mid[ub+1]-mid[ua+1],uz=mid[ub+2]-mid[ua+2];
        const zx=mid[zb]-mid[za],zy=mid[zb+1]-mid[za+1],zz=mid[zb+2]-mid[za+2];
        const nx=uy*zz-uz*zy,ny=uz*zx-ux*zz,nzv=ux*zy-uy*zx;
        const length=Math.hypot(nx,ny,nzv);
        if(length<1e-10) throw Error('Ribbon surface has a collapsed tangent; adjust width, curl or overlap');
        const h=thickness[k]*0.5/length;
        for(let side=0;side<2;side++) {
          const sign=side===0?1:-1,out=(offset+side*perSide+k)*3;
          positions[out]=mid[k*3]+sign*nx*h;positions[out+1]=mid[k*3+1]+sign*ny*h;
          positions[out+2]=iz===0?0:(iz===nz?p.height_mm:Math.max(0,Math.min(p.height_mm,mid[k*3+2]+sign*nzv*h)));
        }
      }
      const at=(iz,iu)=>offset+iz*(nu+1)+iu;
      for(let iz=0;iz<nz;iz++) for(let iu=0;iu<nu;iu++) {
        const a=at(iz,iu),b=at(iz,iu+1),c=at(iz+1,iu+1),d=at(iz+1,iu);
        tri(a,b,c);tri(a,c,d);tri(a+perSide,d+perSide,c+perSide);tri(a+perSide,c+perSide,b+perSide);
      }
      const loop=[];
      for(let iu=0;iu<=nu;iu++) loop.push(at(0,iu));
      for(let iz=1;iz<=nz;iz++) loop.push(at(iz,nu));
      for(let iu=nu-1;iu>=0;iu--) loop.push(at(nz,iu));
      for(let iz=nz-1;iz>0;iz--) loop.push(at(iz,0));
      for(let k=0;k<loop.length;k++) {const a=loop[k],b=loop[(k+1)%loop.length];tri(a,a+perSide,b+perSide);tri(a,b+perSide,b);}
    }
    // Area-weighted normals from the exported indexed boundary, including caps.
    let signedVolume=0;
    for(let i=0;i<indices.length;i+=3) {
      const a=indices[i]*3,b=indices[i+1]*3,c=indices[i+2]*3;
      const ux=positions[b]-positions[a],uy=positions[b+1]-positions[a+1],uz=positions[b+2]-positions[a+2];
      const vx=positions[c]-positions[a],vy=positions[c+1]-positions[a+1],vz=positions[c+2]-positions[a+2];
      const nx=uy*vz-uz*vy,ny=uz*vx-ux*vz,nzv=ux*vy-uy*vx;
      signedVolume+=positions[a]*nx+positions[a+1]*ny+positions[a+2]*nzv;
      for(const k of [a,b,c]) {normals[k]+=nx;normals[k+1]+=ny;normals[k+2]+=nzv;}
    }
    for(let i=0;i<normals.length;i+=3) {
      const l=Math.hypot(normals[i],normals[i+1],normals[i+2])||1;
      normals[i]/=l;normals[i+1]/=l;normals[i+2]/=l;
      overhangs[i/3]=Math.asin(Math.max(0,-normals[i+2]))*180/Math.PI;
    }
    return {positions,indices,normals,overhangs,parts,roles,volumeCm3:signedVolume/6000};
  }
"""
