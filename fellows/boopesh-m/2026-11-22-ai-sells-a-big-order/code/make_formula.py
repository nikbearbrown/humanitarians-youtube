#!/usr/bin/env python3
"""Typeset the one on-screen formula (Almgren & Chriss, Dec 2000, eq. 17) to SVG.

Uses the toolkit's runtime/scripts/typeset_math.py (matplotlib MathText -> outlined
SVG paths, no LaTeX). Written for both the 16:9 and the 9:16 scenes.
Algebra check (FACTCHECK.md): with x_0 = X, x_N = 0, the trajectory
x_j = X sinh(kappa (T - t_j)) / sinh(kappa T) is eq. (17); in code/execution_rl.py
tau = 1, T = N = 10, t_j = j, and kappa solves 2 (cosh kappa - 1) = LAMBDA SIGMA^2 / ETA.
"""
import base64
import sys
from pathlib import Path

TOOLKIT = Path("/home/user/nikbearbrown/brutalist.art/runtime/scripts")
sys.path.insert(0, str(TOOLKIT))
from typeset_math import typeset  # noqa: E402

REEL = Path(__file__).resolve().parents[1]
EXPR = r"x_j \;=\; X\,\frac{\sinh\,\kappa\,(T - t_j)}{\sinh\,\kappa\,T}"

for out, colour in ((REEL / "assets" / "ac-formula-ink.svg", "#2B2A26"),):
    data = typeset(EXPR, color=colour)
    svg = base64.b64decode(data["src"].split(",", 1)[1])
    out.parent.mkdir(exist_ok=True)
    out.write_bytes(svg)
    (REEL / "short" / "assets").mkdir(parents=True, exist_ok=True)
    (REEL / "short" / "assets" / out.name).write_bytes(svg)
    print(f"{out}: aspect {data['aspect']:.3f}  expr {EXPR}")
