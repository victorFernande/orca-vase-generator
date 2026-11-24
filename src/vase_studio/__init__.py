"""Orca Vase Studio — Parametric 3D Vase & Planter Generator Engine."""

from __future__ import annotations

from .schema import DEFAULT_PARAMS, SCHEMA_VERSION, normalize_params
from .mesh_generator import (
    MeshData,
    evaluate_radius_grid,
    generate_saucer_mesh,
    generate_vase_mesh,
)
from .printability import analyze_printability
from .plugin_main import (
    OrcaVaseStudioPlugin,
    VaseStudioDockCapability,
    VaseStudioPageCapability,
)

__version__ = "1.3.3"

__all__ = [
    "SCHEMA_VERSION",
    "DEFAULT_PARAMS",
    "normalize_params",
    "MeshData",
    "evaluate_radius_grid",
    "generate_vase_mesh",
    "generate_saucer_mesh",
    "analyze_printability",
    "OrcaVaseStudioPlugin",
    "VaseStudioPageCapability",
    "VaseStudioDockCapability",
]
