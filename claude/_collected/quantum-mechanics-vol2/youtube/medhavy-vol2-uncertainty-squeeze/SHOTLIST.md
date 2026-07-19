# SHOTLIST — medhavy-vol2-uncertainty-squeeze

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_UncertaintyRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Act Map
B00: MEDHAVY INTRO
B01: UNCERTAINTY SQUEEZE — PROMPT
B02: UNCERTAINTY SQUEEZE — SCRIPT
B03: UNCERTAINTY SQUEEZE — RUN (Manim: hyperbola + two state points)
B04: UNCERTAINTY SQUEEZE — CHANGE
B05: MEDHAVY OUTRO

## Color Law
TEAL: hyperbola boundary σ_x σ_p = ℏ/2; allowed-region label
CRIMSON: squeezed state point (σ_x = 0.5 nm)
INK: all Text()

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: σ_p (y) vs σ_x (x) axes.
  TEAL hyperbola curve for σ_p = ℏ/(2σ_x).
  TEAL dot at (1 nm, σ_p(1 nm)) — original state on boundary.
  CRIMSON dot at (0.5 nm, σ_p(0.5 nm)) — squeezed state on boundary.
  Dashed horizontal line at σ_p(1 nm) for comparison.
  Chips: "σ_x σ_p = ℏ/2" (TEAL), "halve σ_x → double σ_p" (CRIMSON)
