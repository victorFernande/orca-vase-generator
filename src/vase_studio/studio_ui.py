"""Self-contained offline HTML5 + CSS3 + WebGL2 + 2D Curve Studio UI for Orca Vase Studio.

Generates the interactive 3D & 2D parametric vase design studio for both:
- `mode="page"`: Wide 3-column studio tab inside OrcaSlicer (`PagesPluginCapabilityBase`)
- `mode="dock"`: Compact tabbed side-docked panel beside OrcaSlicer's 3D Plater (`UiDockPanel`)

Zero external CDN scripts, stylesheets, or web fonts are referenced so WebView2 runs 100% offline
without network permission prompts.
"""

from __future__ import annotations

import copy
import json
from typing import Any
from html import escape as _escape_language_label
from .locale_catalog import locale_payload, discovered_language_packs
from .language_packs import resolve_language
from .geometric_patterns import GEOMETRIC_JS
from .ribbon_geometry import RIBBON_JS

if "DEFAULT_PARAMS" not in globals():
    try:
        from .schema import DEFAULT_PARAMS
    except Exception:
        DEFAULT_PARAMS = None  # type: ignore[assignment]

if "BUILTIN_PRESETS" not in globals():
    try:
        from .presets_catalog import BUILTIN_PRESETS
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
<html lang="__INITIAL_LANG__" dir="__INITIAL_DIRECTION__" data-theme="__INITIAL_THEME__">
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
      <select id="lang-select" class="btn" style="max-width:116px;padding:4px" aria-label="Language" title="Language">__LANGUAGE_OPTIONS__</select>
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
        <button id="btn-cut-off" data-i18n="btn_off" class="btn" style="padding:3px 7px;font-size:10.5px;">Off</button>
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
          <div class="tex-card" data-tex-card="geometric">
            <div class="tex-head" data-tex-toggle-expand="geometric">
              <div class="tex-title-wrap"><span class="tex-chevron">▶</span> <span data-i18n="tex_geometric">Geometric Relief</span></div>
              <label class="toggle-switch" onclick="event.stopPropagation();"><input id="chk-tex-geometric" type="checkbox" /><span class="toggle-track"></span></label>
            </div>
            <div class="tex-body">
              <label class="ctrl-label" for="sel-geometric-pattern" data-i18n="lbl_geometric_pattern">Sidewall Pattern</label>
              <select id="sel-geometric-pattern" class="vp-select">
                <option value="diamond" data-i18n="pattern_diamond">Diamond Facets</option>
                <option value="leaf_scales" data-i18n="pattern_leaf_scales">Leaf Scales</option>
                <option value="crater_cells" data-i18n="pattern_crater_cells">Crater Cells</option>
                <option value="folded_petals" data-i18n="pattern_folded_petals">Folded Petals</option>
                <option value="spiral_bloom" data-i18n="pattern_spiral_bloom">Spiral Bloom</option>
                <option value="ripple" data-i18n="pattern_ripple">Ripple Rings</option>
                <option value="coral" data-i18n="pattern_coral">Coral Lattice</option>
              </select>
              <div data-slider="textures.geometric.depth_mm"></div>
              <div data-slider="textures.geometric.cells_around"></div>
              <div data-slider="textures.geometric.cells_vertical"></div>
              <div data-slider="textures.geometric.twist_deg"></div>
              <div data-slider="textures.geometric.phase_deg"></div>
              <div id="box-ribbon-opts" style="display:none;flex-direction:column;gap:6px;">
                <label for="sel-ribbon-quality" class="ctrl-label" data-i18n="lbl_ribbon_quality">Ribbon Quality</label>
                <select id="sel-ribbon-quality" class="vp-select">
                  <option value="draft" data-i18n="quality_draft">Draft</option>
                  <option value="normal" data-i18n="quality_normal">Normal</option>
                  <option value="fine" data-i18n="quality_fine">Fine</option>
                  <option value="adaptive" data-i18n="quality_adaptive">Adaptive</option>
                </select>
                <div data-slider="textures.geometric.ribbon_width_mm"></div>
                <div data-slider="textures.geometric.ribbon_thickness_mm"></div>
                <div data-slider="textures.geometric.ribbon_curl_deg"></div>
                <div data-slider="textures.geometric.ribbon_flatten_pct"></div>
                <div class="helper-note" data-i18n="hint_ribbon_flatten">Brings folds closer to the cup without thinning the ribbons. Steep overhangs may remain; check the sliced preview.</div>
                <div data-slider="textures.geometric.ribbon_overlap_mm"></div>
                <div data-slider="textures.geometric.ribbon_stretch_pct"></div>
                <div data-slider="textures.geometric.ribbon_stagger"></div>
                <div class="helper-note" data-i18n="hint_ribbons">Round hollow cup with closed overlapping ribbons. Check the sliced result. Spiral mode and other textures are unavailable.</div>
              </div>
              <div data-slider="textures.geometric.strength_bottom"></div>
              <div data-slider="textures.geometric.strength_middle"></div>
              <div data-slider="textures.geometric.strength_top"></div>
              <div id="hint-geometric" class="helper-note" data-i18n="hint_geometric">Relief is part of the wall. Combine layers or disable other textures for a clean pattern.</div>
            </div>
          </div>

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
      geometric: {enabled: false, pattern: "leaf_scales", depth_mm: 3.0, cells_around: 14, cells_vertical: 10, twist_deg: 0, phase_deg: 0, strength_bottom: 1, strength_middle: 1, strength_top: 1, ribbon_width_mm: 34, ribbon_thickness_mm: 1.2, ribbon_curl_deg: 382, ribbon_flatten_pct: 0, ribbon_overlap_mm: 1.4, ribbon_stretch_pct: 8, ribbon_stagger: 0.5, ribbon_quality: "fine"},
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
    const geoSrc = (texSrc.geometric && typeof texSrc.geometric === "object") ? texSrc.geometric : {};
    const drnSrc = (src.drainage && typeof src.drainage === "object") ? src.drainage : {};
    const sauSrc = (src.saucer && typeof src.saucer === "object") ? src.saucer : {};

    let polySides = clampInt(src.polygon_sides, 0, 0, 24);
    if (polySides > 0 && polySides < 3) polySides = 3;

    const pmRaw = String(src.print_mode !== undefined ? src.print_mode : "shelled_hollow").trim().toLowerCase();
    const printMode = pmRaw === "spiral_vase" ? "spiral_vase" : "shelled_hollow";

    const cleanName = String(src.name !== undefined ? src.name : JS_DEFAULT_PARAMS.name).trim().slice(0, 80) || "Ondas Organicas";

    const normalized = {
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
        geometric: {
          enabled: toBool(geoSrc.enabled, false),
          pattern: ["diamond", "leaf_scales", "crater_cells", "folded_petals", "spiral_bloom", "ripple", "coral"].includes(geoSrc.pattern) ? geoSrc.pattern : "leaf_scales",
          depth_mm: clampFloat(geoSrc.depth_mm, 3, -8, 8),
          cells_around: clampInt(geoSrc.cells_around, 14, 3, 36),
          cells_vertical: clampInt(geoSrc.cells_vertical, 10, 2, 24),
          twist_deg: clampFloat(geoSrc.twist_deg, 0, -720, 720),
          phase_deg: clampFloat(geoSrc.phase_deg, 0, 0, 360),
          strength_bottom: clampFloat(geoSrc.strength_bottom, 1, 0, 2),
          strength_middle: clampFloat(geoSrc.strength_middle, 1, 0, 2),
          strength_top: clampFloat(geoSrc.strength_top, 1, 0, 2),
          ribbon_width_mm: clampFloat(geoSrc.ribbon_width_mm,34,8,80),
          ribbon_thickness_mm: clampFloat(geoSrc.ribbon_thickness_mm,1.2,0.4,4),
          ribbon_curl_deg: clampFloat(geoSrc.ribbon_curl_deg,382,180,430),
          ribbon_flatten_pct: clampFloat(geoSrc.ribbon_flatten_pct,0,0,60),
          ribbon_overlap_mm: clampFloat(geoSrc.ribbon_overlap_mm,1.4,0,4),
          ribbon_stretch_pct: clampFloat(geoSrc.ribbon_stretch_pct,8,0,25),
          ribbon_stagger: clampFloat(geoSrc.ribbon_stagger,0.5,0,1),
          ribbon_quality: ['draft','normal','fine','adaptive'].includes(geoSrc.ribbon_quality)?geoSrc.ribbon_quality:'fine',
          ribbon_nozzle_mm: clampFloat(geoSrc.ribbon_nozzle_mm,0.4,0.2,1.2)
        },
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
    if(normalized.textures.geometric.enabled && normalized.textures.geometric.pattern==='folded_petals') {
      normalized.print_mode='shelled_hollow';
      normalized.polygon_sides=0;
      for(const name of ['ribbed','waves','origami','cellular']) normalized.textures[name].enabled=false;
    }
    return normalized;
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

  __GEOMETRIC_JS__
  __RIBBON_JS__

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

    const geo = textures.geometric;
    if (geo && geo.enabled && Math.abs(geo.depth_mm) > 1e-9) {
      dr += geometricDisplacement(zNorm, thetaG, geo);
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
    ribbonPlan: ribbonPlan,
    buildRibbonMesh: buildRibbonMesh,
    normalizeParams: normalizeParams,
    evaluateRadiusGrid: evaluateRadiusGrid,
    evaluateSurfaceRadius: evaluateSurfaceRadius,
    hash3U32: hash3U32,
    valueNoise3DScalar: valueNoise3DScalar
  };

  // ==========================================================================
  // 3. Translations (PT-BR & EN) & Slider Metadata
  // ==========================================================================
  const LOCALE_DATA = __VASE_LOCALE_PACKS__;
  const LANGUAGE_METADATA = LOCALE_DATA.metadata;
  const LANGUAGES = LANGUAGE_METADATA.map(function(item) { return item.code; });
  const LOCALE_VOCABULARY = LOCALE_DATA.vocabulary;
  const I18N = {};
  for (const language of LANGUAGES) {
    const catalog = LOCALE_VOCABULARY[language] || {};
    I18N[language] = Object.fromEntries(Object.entries(LOCALE_DATA.messages).map(function(entry) {
      return [entry[0], catalog["ui:" + entry[0] + "::" + entry[1]] || catalog[entry[1]] || entry[1]];
    }));
  }
  function normalizeLanguage(value) {
    let code = String(value || "").trim().toLowerCase().replace(/_/g, "-").split(/[.@]/)[0];
    if (!code) return LANGUAGES.includes("pt") ? "pt" : "en";
    while (code) {
      if (LANGUAGES.includes(code)) return code;
      code = code.includes("-") ? code.slice(0, code.lastIndexOf("-")) : "";
    }
    return "en";
  }
  function localizedText(english) {
    const catalog = LOCALE_VOCABULARY[state.lang] || {};
    return catalog[english] || english;
  }
  function localizedWarning(warning) {
    const source = warning.en || warning.pt || "";
    const catalog = LOCALE_VOCABULARY[state.lang] || {};
    if (catalog[source]) return catalog[source];
    for (const template of Object.keys(catalog)) {
      if (!template.includes("{")) continue;
      const names = [];
      const pattern = template.split(/(\{[a-z]+\})/).map(function(part) {
        if (/^\{[a-z]+\}$/.test(part)) { names.push(part.slice(1, -1)); return "(.+?)"; }
        return part.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      }).join("");
      const match = source.match(new RegExp("^" + pattern + "$"));
      if (match) {
        let result = catalog[template];
        names.forEach(function(name, i) { result = result.replace("{" + name + "}", match[i + 1]); });
        return result;
      }
    }
    return source;
  }
  function sliderLabel(spec) { return localizedText(spec.en); }
  function sliderUnit(unit) {
    return localizedText(({seg:"Segments",cam:"Layers",un:"Count",oct:"Octaves"})[unit] || unit);
  }
  const STATIC_ATTRIBUTES = [];
  function initializeStaticTranslations() {
    document.querySelectorAll("[title], [placeholder], [aria-label]").forEach(function(node) {
      for (const attr of ["title", "placeholder", "aria-label"]) {
        const value = node.getAttribute(attr);
        if (value) STATIC_ATTRIBUTES.push({node: node, attr: attr, value: value});
      }
    });
  }
  function translateStaticAttributes() {
    for (const entry of STATIC_ATTRIBUTES) {
      let source = entry.value;
      if (source === "Nome do preset...") source = "Preset name...";
      if (source === "Dark / Light") source = "Toggle Theme";
      if (source.startsWith("Undo (")) source = localizedText("Undo") + " (Ctrl+Z)";
      else if (source.startsWith("Redo (")) source = localizedText("Redo") + " (Ctrl+Y)";
      else source = localizedText(source);
      entry.node.setAttribute(entry.attr, source);
    }
  }

  const SLIDER_SPECS = [
    { path: "height_mm", min: 30, max: 500, step: 1, unit: "mm", en: "Total Height" },
    { path: "base_diameter_mm", min: 20, max: 450, step: 1, unit: "mm", en: "Base Diameter" },
    { path: "belly_diameter_mm", min: 20, max: 450, step: 1, unit: "mm", en: "Belly Diameter" },
    { path: "belly_height_ratio", min: 0.08, max: 0.85, step: 0.01, unit: "h", en: "Belly Height Ratio" },
    { path: "waist_diameter_mm", min: 16, max: 450, step: 1, unit: "mm", en: "Waist Diameter" },
    { path: "waist_height_ratio", min: 0.15, max: 0.92, step: 0.01, unit: "h", en: "Waist Height Ratio" },
    { path: "neck_diameter_mm", min: 16, max: 450, step: 1, unit: "mm", en: "Neck Diameter" },
    { path: "lip_flare_mm", min: -15, max: 25, step: 0.5, unit: "mm", en: "Top Lip Flare" },
    { path: "lip_bevel_mm", min: 0, max: 4, step: 0.2, unit: "mm", en: "Top Rim Bevel" },
    { path: "polygon_sides", min: 0, max: 24, step: 1, unit: "n", en: "Polygon Sides (0=Circle)" },
    { path: "polygon_roundness", min: 0, max: 1, step: 0.02, unit: "", en: "Polygon Roundness" },
    { path: "resolution_angular", min: 64, max: 360, step: 8, unit: "seg", en: "Angular Resolution" },
    { path: "resolution_vertical", min: 60, max: 400, step: 10, unit: "cam", en: "Vertical Resolution" },

    { path: "bottom_fade_mm", min: 0, max: 60, step: 1, unit: "mm", en: "Bottom Texture Fade" },
    { path: "top_fade_mm", min: 0, max: 60, step: 1, unit: "mm", en: "Top Texture Fade" },
    { path: "global_twist_deg", min: -720, max: 720, step: 5, unit: "°", en: "Global Helical Twist" },

    { path: "textures.geometric.ribbon_width_mm", min: 8, max: 80, step: 0.5, unit: "mm", en: "Ribbon Width" },
    { path: "textures.geometric.ribbon_thickness_mm", min: 0.4, max: 4, step: 0.1, unit: "mm", en: "Ribbon Thickness" },
    { path: "textures.geometric.ribbon_curl_deg", min: 180, max: 430, step: 1, unit: "°", en: "Ribbon Curl" },
    { path: "textures.geometric.ribbon_flatten_pct", min: 0, max: 60, step: 5, unit: "%", en: "Ribbon Flattening" },
    { path: "textures.geometric.ribbon_overlap_mm", min: 0, max: 4, step: 0.1, unit: "mm", en: "Ribbon Overlap" },
    { path: "textures.geometric.ribbon_stretch_pct", min: 0, max: 25, step: 1, unit: "%", en: "Ribbon Stretch" },
    { path: "textures.geometric.ribbon_stagger", min: 0, max: 1, step: 0.05, unit: "", en: "Ribbon Stagger" },
    { path: "textures.geometric.depth_mm", min: -8, max: 8, step: 0.1, unit: "mm", en: "Relief Depth" },
    { path: "textures.geometric.cells_around", min: 3, max: 36, step: 1, unit: "", en: "Pattern Columns" },
    { path: "textures.geometric.cells_vertical", min: 2, max: 24, step: 1, unit: "", en: "Pattern Rows" },
    { path: "textures.geometric.twist_deg", min: -720, max: 720, step: 5, unit: "°", en: "Pattern Twist" },
    { path: "textures.geometric.phase_deg", min: 0, max: 360, step: 5, unit: "°", en: "Pattern Phase" },
    { path: "textures.geometric.strength_bottom", min: 0, max: 2, step: 0.05, unit: "×", en: "Bottom Relief Strength" },
    { path: "textures.geometric.strength_middle", min: 0, max: 2, step: 0.05, unit: "×", en: "Middle Relief Strength" },
    { path: "textures.geometric.strength_top", min: 0, max: 2, step: 0.05, unit: "×", en: "Top Relief Strength" },

    { path: "textures.ribbed.depth_mm", min: -15, max: 15, step: 0.2, unit: "mm", en: "Rib Depth" },
    { path: "textures.ribbed.count", min: 3, max: 180, step: 1, unit: "un", en: "Rib Count (Density)" },
    { path: "textures.ribbed.duty_cycle", min: 0.10, max: 0.90, step: 0.02, unit: "", en: "Rib Width / Duty Cycle" },
    { path: "textures.ribbed.sharpness", min: 0, max: 1, step: 0.02, unit: "", en: "Crest Sharpness" },
    { path: "textures.ribbed.twist_deg", min: -720, max: 720, step: 5, unit: "°", en: "Rib Helical Twist" },
    { path: "textures.ribbed.phase_deg", min: 0, max: 360, step: 5, unit: "°", en: "Angular Phase" },

    { path: "textures.waves.depth_mm", min: -15, max: 15, step: 0.2, unit: "mm", en: "Wave Depth" },
    { path: "textures.waves.vertical_wavelength_mm", min: 4, max: 120, step: 1, unit: "mm", en: "Vertical Wavelength" },
    { path: "textures.waves.angular_lobes", min: 0, max: 48, step: 1, unit: "un", en: "Angular Lobes" },
    { path: "textures.waves.interference_mix", min: 0, max: 1, step: 0.02, unit: "", en: "Counter-Wave Mix" },
    { path: "textures.waves.wave_skew", min: -0.8, max: 0.8, step: 0.05, unit: "", en: "Wave Skew" },
    { path: "textures.waves.phase_deg", min: 0, max: 360, step: 5, unit: "°", en: "Wave Phase" },

    { path: "textures.origami.depth_mm", min: -15, max: 15, step: 0.2, unit: "mm", en: "Facet Depth" },
    { path: "textures.origami.cells_around", min: 3, max: 60, step: 1, unit: "un", en: "Cells Around" },
    { path: "textures.origami.cells_vertical", min: 2, max: 50, step: 1, unit: "un", en: "Vertical Tiers" },
    { path: "textures.origami.crease_sharpness", min: 0, max: 1, step: 0.02, unit: "", en: "Crease Sharpness" },
    { path: "textures.origami.stagger", min: 0, max: 1, step: 0.05, unit: "", en: "Row Stagger" },

    { path: "textures.cellular.depth_mm", min: -12, max: 12, step: 0.2, unit: "mm", en: "Cellular Depth" },
    { path: "textures.cellular.scale_angular", min: 2, max: 40, step: 1, unit: "un", en: "Angular Cell Scale" },
    { path: "textures.cellular.scale_vertical_mm", min: 5, max: 100, step: 1, unit: "mm", en: "Vertical Cell Size" },
    { path: "textures.cellular.octaves", min: 1, max: 4, step: 1, unit: "oct", en: "Detail Octaves" },
    { path: "textures.cellular.seed", min: 1, max: 99999, step: 1, unit: "#", en: "Pattern Seed" },

    { path: "spiral_line_width_mm", min: 0.40, max: 1.20, step: 0.02, unit: "mm", en: "Spiral Line Width" },
    { path: "spiral_bottom_layers", min: 2, max: 15, step: 1, unit: "cam", en: "Bottom Solid Layers" },
    { path: "wall_thickness_mm", min: 0.8, max: 25, step: 0.1, unit: "mm", en: "Wall Thickness" },
    { path: "bottom_thickness_mm", min: 1.0, max: 25, step: 0.2, unit: "mm", en: "Bottom Floor Thickness" },
    { path: "max_safe_overhang_deg", min: 35, max: 65, step: 1, unit: "°", en: "Max Safe Overhang" },

    { path: "drainage.hole_count", min: 1, max: 9, step: 1, unit: "un", en: "Drainage Hole Count" },
    { path: "drainage.hole_diameter_mm", min: 3, max: 20, step: 0.5, unit: "mm", en: "Hole Diameter" },
    { path: "drainage.ring_radius_ratio", min: 0, max: 0.68, step: 0.02, unit: "r", en: "Ring Radius Ratio" },

    { path: "saucer.clearance_mm", min: 3, max: 25, step: 0.5, unit: "mm", en: "Saucer Inner Clearance" },
    { path: "saucer.rim_height_mm", min: 10, max: 60, step: 1, unit: "mm", en: "Saucer Rim Height" },
    { path: "saucer.wall_thickness_mm", min: 1.2, max: 5.0, step: 0.2, unit: "mm", en: "Saucer Wall Thickness" },
    { path: "saucer.floor_thickness_mm", min: 1.2, max: 6.0, step: 0.2, unit: "mm", en: "Saucer Floor Thickness" },
    { path: "saucer.inner_ribs_height_mm", min: 0, max: 6.0, step: 0.2, unit: "mm", en: "Inner Drainage Ribs" }
  ];

  // ==========================================================================
  // 4. Studio Application State & Undo/Redo Stack
  // ==========================================================================
  const initCtx = (BOOT_PAYLOAD && BOOT_PAYLOAD.initial_context) ? BOOT_PAYLOAD.initial_context : {};
  const state = {
    mode: BOOT_PAYLOAD.mode === "dock" ? "dock" : "page",
    lang: normalizeLanguage(initCtx.lang),
    manualLanguageSelected: Boolean(initCtx.language_override),
    pendingLanguage: null,
    deferredLanguageUpdate: null,
    nextLanguageRequest: 0,
    languageRevision: Number(initCtx.language_revision || 0),
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
    const dict = I18N[state.lang] || I18N.en;
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
      if (msg.lang && !state.manualLanguageSelected) state.lang = normalizeLanguage(msg.lang);
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
      if (msg.lang && !state.manualLanguageSelected && normalizeLanguage(msg.lang) !== state.lang) {
        state.lang = normalizeLanguage(msg.lang);
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

    if (msg.type === "preferences_updated" && msg.lang) {
      const revision = Number(msg.language_revision || 0);
      if (revision && revision < state.languageRevision) return;
      if (state.pendingLanguage) {
        const pending = state.pendingLanguage;
        if (msg.source_mode === state.mode && Number(msg.request_id || 0) < pending.id) return;
        if (normalizeLanguage(msg.lang) !== pending.lang) {
          if (msg.source_mode !== state.mode && revision > Number(state.deferredLanguageUpdate?.language_revision || 0)) state.deferredLanguageUpdate = msg;
          return;
        }
        state.pendingLanguage = null;
      }
      const resolved = Number(state.deferredLanguageUpdate?.language_revision || 0) > revision ? state.deferredLanguageUpdate : msg;
      state.deferredLanguageUpdate = null;
      state.languageRevision = Math.max(state.languageRevision, Number(resolved.language_revision || 0));
      state.manualLanguageSelected = true;
      state.lang = normalizeLanguage(resolved.lang);
      applyThemeAndLanguage();
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
        if (state.wireframe) wire.push(x1, y1, z1, x2, y2, z2);
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
      (t.cellular.enabled && Math.abs(t.cellular.depth_mm) > 0.05) ||
      (t.geometric.enabled && Math.abs(t.geometric.depth_mm) > 0.05 && Math.max(t.geometric.strength_bottom, t.geometric.strength_middle, t.geometric.strength_top) > 0)
    );
  }

  function buildCupStudioGeometry(p, fastInteractive) {
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

  function buildFullStudioGeometry(rawParams, fastInteractive) {
    const p=normalizeParams(rawParams),g=p.textures.geometric;
    const cup=buildCupStudioGeometry(p,fastInteractive);
    if (!(g.enabled && g.pattern==='folded_petals')) {
      state.lastRibbonGeometry=null;
      return cup;
    }
    const plan=ribbonPlan(p,fastInteractive);
    if (ribbonPlan(p,false).triangles>3000000) throw Error('Ribbon mesh is too large. Reduce ribbon count or choose a lower ribbon quality.');
    const radii=evaluateRadiusGrid(p,plan.nz+1,3).radii.map(row=>row[0]);
    if(Math.min(...radii)-p.wall_thickness_mm<=2) throw Error('The cup is too narrow for its wall. Increase the profile diameter or reduce wall thickness.');
    const ribbons=buildRibbonMesh(p,radii,fastInteractive),offset=cup.positions.length/3;
    const baseDims=state.clientMetrics.dims.slice();
    const localMin=[-baseDims[0]/2,-baseDims[1]/2,0],localMax=[baseDims[0]/2,baseDims[1]/2,p.height_mm];
    const placement=state.lastGeoData;
    for(let i=0;i<ribbons.positions.length;i+=3) {
      for(let j=0;j<3;j++) {localMin[j]=Math.min(localMin[j],ribbons.positions[i+j]);localMax[j]=Math.max(localMax[j],ribbons.positions[i+j]);}
      ribbons.positions[i]+=placement.vaseOffsetX;
      ribbons.positions[i+2]+=placement.vaseLiftZ;
    }
    state.lastRibbonGeometry=ribbons;
    const join=(a,b,Type)=>{const out=new Type(a.length+b.length);out.set(a);out.set(b,a.length);return out;};
    for(const key of ['positions','normals','overhangs','parts','roles']) cup[key]=join(cup[key],ribbons[key],Float32Array);
    const shifted=new Uint32Array(ribbons.indices.length);
    for(let i=0;i<shifted.length;i++) shifted[i]=ribbons.indices[i]+offset;
    cup.indices=join(cup.indices,shifted,Uint32Array);
    if (state.wireframe) {
      const lines=plan.count*2*((plan.nz+1)*plan.nu+plan.nz*(plan.nu+1));
      const wire=new Float32Array(lines*6);
      let w=0;
      const perSide=(plan.nz+1)*(plan.nu+1);
      const line=(a,b)=>{for(let j=0;j<3;j++) wire[w++]=ribbons.positions[a*3+j];for(let j=0;j<3;j++) wire[w++]=ribbons.positions[b*3+j];};
      for(let strip=0;strip<plan.count;strip++) for(let side=0;side<2;side++) for(let iz=0;iz<=plan.nz;iz++) for(let iu=0;iu<=plan.nu;iu++) {
        const a=(strip*2+side)*perSide+iz*(plan.nu+1)+iu;
        if(iu<plan.nu) line(a,a+1);
        if(iz<plan.nz) line(a,a+plan.nu+1);
      }
      cup.wirePositions=join(cup.wirePositions,wire,Float32Array);
    }
    const min=[Infinity,Infinity,Infinity],max=[-Infinity,-Infinity,-Infinity];
    for(let i=0;i<cup.positions.length;i+=3) for(let j=0;j<3;j++) {min[j]=Math.min(min[j],cup.positions[i+j]);max[j]=Math.max(max[j],cup.positions[i+j]);}
    state.clientMetrics.dims=localMax.map((v,j)=>v-localMin[j]);
    state.clientMetrics.tris+=ribbonPlan(p,false).triangles;
    state.clientMetrics.weightG+=ribbons.volumeCm3*1.24;
    const bx=Number(state.printer.bed_x)||220,by=Number(state.printer.bed_y)||220;
    let maxRadius=0;
    for(let i=0;i<cup.positions.length;i+=3) maxRadius=Math.max(maxRadius,Math.hypot(cup.positions[i],cup.positions[i+1]));
    const fit=String(state.printer.bed_shape||'').toLowerCase()==='circular'?2*maxRadius<=Math.min(bx,by):(max[0]-min[0]<=bx&&max[1]-min[1]<=by);
    state.clientMetrics.fitsBed=state.clientMetrics.fitsBed&&fit;
    for(let i=0;i<ribbons.overhangs.length;i++) state.clientMetrics.maxOverhang=Math.max(state.clientMetrics.maxOverhang,ribbons.overhangs[i]);
    return cup;
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
    const dims = state.clientMetrics.dims;
    const canvas = document.getElementById("gl-canvas");
    const aspect = canvas && canvas.clientHeight > 0 ? canvas.clientWidth / canvas.clientHeight : 1;
    const halfVertical = 19 * DEG2RAD;
    const halfHorizontal = Math.atan(Math.tan(halfVertical) * Math.max(0.05, aspect));
    const halfFov = Math.min(halfVertical, halfHorizontal);
    // A bounding sphere fits every camera angle, including custom profiles and
    // relief extending beyond the nominal silhouette. Leave space for the HUD.
    const radius = Math.hypot(dims[0], dims[1], dims[2]) * 0.5;
    camera.target = [0.0, 0.0, h * 0.5];
    camera.distance = Math.max(170.0, radius / Math.sin(halfFov) * 1.15);
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
          '<span class="ctrl-label" data-spec-label="' + spec.path + '"></span>' +
          '<div class="ctrl-val-wrap">' +
            '<input class="ctrl-num" type="number" min="' + spec.min + '" max="' + spec.max + '" step="' + spec.step + '" value="' + Number(initVal).toFixed(decs) + '" />' +
            '<span class="ctrl-unit"></span>' +
          '</div>' +
        '</div>' +
        '<input class="orca-slider" type="range" min="' + spec.min + '" max="' + spec.max + '" step="' + spec.step + '" value="' + initVal + '" />';

      const rangeEl = host.querySelector('input[type="range"]');
      const numEl = host.querySelector('input[type="number"]');
      const labelEl = host.querySelector("[data-spec-label]");
      if (labelEl) labelEl.textContent = sliderLabel(spec);
      const unitEl = host.querySelector(".ctrl-unit");
      if (unitEl) unitEl.textContent = sliderUnit(spec.unit);

      sliderRefs[spec.path] = { spec: spec, rangeEl: rangeEl, numEl: numEl, labelEl: labelEl, unitEl:host.querySelector(".ctrl-unit"), decs: decs };

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
          lbl.textContent = localizedText("Off");
        } else {
          const zMm = Math.round(state.params.height_mm * (state.zSlicePct / 100.0));
          lbl.textContent = state.zSlicePct + "% (" + zMm + "mm)";
        }
      } else {
        lbl.textContent = state.crossCutPct === 0 ? localizedText("Off") : (state.crossCutPct + "%");
      }
    }
  }

  function updateDerivedBadges() {
    const polyBadge = document.getElementById("poly-badge");
    if (polyBadge) {
      const n = state.params.polygon_sides | 0;
      polyBadge.textContent = n < 3 ? tr("poly_circle") : tr("poly_sides_fmt").replace("{n}", String(n));
    }

    const ribbonMode=state.params.textures.geometric.enabled && state.params.textures.geometric.pattern==='folded_petals';
    const ribbonBox=document.getElementById('box-ribbon-opts');
    if(ribbonBox) ribbonBox.style.display=ribbonMode?'flex':'none';
    const reliefHint=document.getElementById('hint-geometric');
    if(reliefHint) reliefHint.style.display=ribbonMode?'none':'block';
    const ribbonQuality=document.getElementById('sel-ribbon-quality');
    if(ribbonQuality) ribbonQuality.value=state.params.textures.geometric.ribbon_quality;
    const depthControl=document.querySelector('[data-slider="textures.geometric.depth_mm"]');
    if(depthControl) depthControl.style.display=ribbonMode?'none':'flex';
    for(const name of ['ribbed','waves','origami','cellular']) {
      const toggle=document.getElementById('chk-tex-'+name);
      if(toggle) toggle.disabled=ribbonMode;
    }
    const spiralChoice=document.getElementById('btn-mode-spiral');
    if(spiralChoice) spiralChoice.disabled=ribbonMode;
    for(const [path,label] of [['cells_around','Ribbon Count'],['cells_vertical','Ribbon Loops'],['strength_bottom','Bottom Ribbon Strength'],['strength_middle','Middle Ribbon Strength'],['strength_top','Top Ribbon Strength']]) {
      const ref=sliderRefs['textures.geometric.'+path];
      if(ref?.labelEl) ref.labelEl.textContent=ribbonMode?localizedText(label):sliderLabel(ref.spec);
    }
    const activeTexBadge = document.getElementById("active-tex-badge");
    if (activeTexBadge) {
      let c = 0;
      const t = state.params.textures;
      if (t.ribbed.enabled) c++;
      if (t.waves.enabled) c++;
      if (t.origami.enabled) c++;
      if (t.cellular.enabled) c++;
      if (t.geometric.enabled) c++;
      activeTexBadge.textContent = tr("active_tex_fmt").replace("{n}", String(c));
    }

    const texNames = ["ribbed", "waves", "origami", "cellular", "geometric"];
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
    setChk("chk-tex-geometric", state.params.textures.geometric.enabled);
    const geoSelect = document.getElementById("sel-geometric-pattern");
    if (geoSelect) geoSelect.value = state.params.textures.geometric.pattern;
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

      const title = item._isUser ? (item.name || item.title_pt || item.title_en || "Preset") : localizedText(item.title_en || item.title_pt || "Preset");
      const desc = item._isUser ? (item.description_en || item.description_pt || "") : localizedText(item.description_en || item.description_pt || "");

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
        delBtn.title = localizedText("Delete");
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
        const texKeys = ["ribbed", "waves", "origami", "cellular", "geometric"];
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
          div.textContent = localizedWarning(w);
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

  initializeStaticTranslations();

  function applyThemeAndLanguage() {
    document.documentElement.setAttribute("data-theme", state.theme);
    document.documentElement.setAttribute("lang", state.lang);
    const languageMeta = LANGUAGE_METADATA.find(function(item) { return item.code === state.lang; });
    document.documentElement.setAttribute("dir", languageMeta ? languageMeta.direction : "ltr");
    if (document.body) {
      document.body.setAttribute("data-mode", state.mode);
    }

    const langSelect = document.getElementById("lang-select");
    if (langSelect) langSelect.value = state.lang;
    translateStaticAttributes();

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
        ref.labelEl.textContent = sliderLabel(ref.spec);
      }
      if (ref.unitEl) ref.unitEl.textContent = sliderUnit(ref.spec.unit);
    }

    updateDerivedBadges();
    renderPresetsGrid();
    updatePrintabilityHud();
    draw2DCurveEditor();
    requestRender();
  }

  function rebuildScene(fastInteractive) {
    state.params=normalizeParams(state.params);
    state.params.textures.geometric.ribbon_nozzle_mm=clampFloat(state.printer.nozzle_mm,0.4,0.2,1.2);
    syncControlsFromState();
    let geo;
    const wasInvalid=Boolean(state.geometryError);
    const previousGeometry={data:state.lastGeoData,metrics:state.clientMetrics,ribbons:state.lastRibbonGeometry};
    try {
      geo = buildFullStudioGeometry(state.params, Boolean(fastInteractive));
      state.geometryError=null;
      if(wasInvalid) {
        const banner=document.getElementById('toast-banner');
        if(banner) banner.classList.remove('visible','error');
        if(toastTimer) clearTimeout(toastTimer);
      }
    } catch(error) {
      state.lastGeoData=previousGeometry.data;
      state.clientMetrics=previousGeometry.metrics;
      state.lastRibbonGeometry=previousGeometry.ribbons;
      state.geometryError=String(error.message||error);
      setActionButtonsBusy(false);
      showToast(localizedText(state.geometryError),true);
      return;
    }
    setActionButtonsBusy(state.busyAction);
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
      btns[i].disabled = busy || Boolean(state.geometryError);
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

    on("lang-select", "change", function () {
      state.lang = normalizeLanguage(document.getElementById("lang-select").value);
      state.manualLanguageSelected = true;
      const requestId = ++state.nextLanguageRequest;
      state.pendingLanguage = {id:requestId,lang:state.lang};
      applyThemeAndLanguage();
      if (!sendToHost({type:"set_language",lang:state.lang,mode:state.mode,request_id:requestId})) state.pendingLanguage = null;
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
      rebuildScene(false);
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
    bindTexChk("chk-tex-geometric", "geometric");
    on("sel-geometric-pattern", "change", function (e) {
      pushUndoSnapshot(state.params);
      state.params.textures.geometric.pattern = e.target.value;
      state.params.textures.geometric.enabled = true;
      if(e.target.value==='folded_petals') {
        state.params.textures.geometric.cells_around=8;
        state.params.textures.geometric.cells_vertical=4;
      }
      state.params=normalizeParams(state.params);
      syncControlsFromState();
      rebuildScene(false);
      scheduleHostAnalyze();
    });
    on("sel-ribbon-quality", "change", function(e) {
      pushUndoSnapshot(state.params);
      state.params.textures.geometric.ribbon_quality=e.target.value;
      rebuildScene(false);
      scheduleHostAnalyze();
    });

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
            showToast(localizedText("OrcaSlicer host bridge not connected (Standalone Preview)."), true);
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
            showToast(localizedText("OrcaSlicer host bridge not connected (Standalone Preview)."), true);
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

    packs = discovered_language_packs()
    norm_lang = resolve_language(ctx.get("lang"), packs)
    ctx["lang"] = norm_lang

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
    html = html.replace("__GEOMETRIC_JS__", GEOMETRIC_JS)
    html = html.replace("__RIBBON_JS__", RIBBON_JS)
    html = html.replace("__VASE_LOCALE_PACKS__", _studio_ui_safe_json(locale_payload(packs)))
    options = "".join('<option value="' + _escape_language_label(code, quote=True) + '">' + _escape_language_label(pack["native_name"]) + '</option>' for code, pack in packs.items())
    html = html.replace("__LANGUAGE_OPTIONS__", options)
    html = html.replace("__INITIAL_DIRECTION__", packs[norm_lang]["direction"])
    html = html.replace("__INITIAL_LANG__", norm_lang)
    html = html.replace("__INITIAL_THEME__", norm_theme)
    html = html.replace("__INITIAL_MODE__", norm_mode)
    html = html.replace("__ORCA_VASE_STUDIO_BOOT_JSON__", _studio_ui_safe_json(boot_payload))
    return html
