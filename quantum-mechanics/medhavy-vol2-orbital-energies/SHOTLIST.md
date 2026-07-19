# SHOTLIST — medhavy-vol2-orbital-energies

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_OrbitalRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Color Law
TEAL: Hydrogen levels (degenerate, all at same height)
CRIMSON: Sodium levels (split, 3s lower than 3p)
INK: all Text()

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: two-column energy level diagram.
  LEFT: Hydrogen n=3 — TEAL lines for 3s, 3p, 3d all at same y (degenerate)
  RIGHT: Sodium n=3 — CRIMSON lines: 3s lower, 3p higher, gap labeled
  x_range=[-1, 1] (no units), y_range=[-6, 0] in eV
  Labels at right of each line, placed off the strokes
  Chips: "H: 3s=3p=3d" (TEAL), "Na: E(3s)<E(3p)" (CRIMSON)
