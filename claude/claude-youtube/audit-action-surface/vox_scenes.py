import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# audit-action-surface -- Audit an Agent's Action Surface Before Running a Task with Claude
# AGENTIC AI · CLI video · 10 beats
# Color law: TEAL = safe/verified/correct; CRIMSON = risk/error/unverified

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# All output beats are Remotion (PermissionMatrixFill) -- no Manim scenes needed.
# Terminal/brand beats are Remotion (NikBearBrownTerminalAsk, CodeBlock, Open, Outro).
