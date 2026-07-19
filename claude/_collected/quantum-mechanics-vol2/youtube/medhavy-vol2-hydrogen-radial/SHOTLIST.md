# SHOTLIST — medhavy-vol2-hydrogen-radial

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_HydrogenRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Act Map
B00: MEDHAVY INTRO
B01: HYDROGEN RADIAL — PROMPT
B02: HYDROGEN RADIAL — SCRIPT
B03: HYDROGEN RADIAL — RUN (Manim: P(r) curve with r_mp and ⟨r⟩ markers)
B04: HYDROGEN RADIAL — CHANGE
B05: MEDHAVY OUTRO

## Color Law
TEAL: P(r) curve, r_mp marker (mode)
CRIMSON: ⟨r⟩ marker (mean), mean annotation
INK: all Text()

## Exclusions
No 3D orbital visualization, no 2p/3d radial functions, no
angular wavefunctions, no emission spectrum derivation.

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: P(r) vs r curve on Axes.
  x_range=[0, 7a₀], y_range=[0, 0.55 a₀⁻¹] (normalized)
  TEAL curve for P(r).
  TEAL vertical dashed line at r = a₀ labeled "r_mp = a₀"
  CRIMSON vertical dashed line at r = 1.5a₀ labeled "⟨r⟩ = 3a₀/2"
  Both labeled ABOVE the x-axis.
  Shaded area between curve and x-axis (light TEAL fill).
  Chips: "r_mp = a₀" (TEAL), "⟨r⟩ = 1.5 a₀" (CRIMSON)
