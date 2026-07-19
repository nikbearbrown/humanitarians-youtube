# SHOTLIST — medhavy-vol3-golden-rule

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_GoldenRuleRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Color Law
TEAL: Γ(V) = (2π/ℏ)ρV² parabolic rate curve
CRIMSON: Reference dot at H 2p→1s value (V_H, A_H)
INK: all Text()

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: rate curve Γ vs V (eV), V ∈ [0, 2]
  x_range=[0, 2] eV; y_range=[0, 25] (in 10⁸ s⁻¹ units)
  TEAL parabola Γ ∝ V²
  CRIMSON dot at (V_H_display, A_H_display) where curve hits A_H
  x-axis label: "V  (eV)"; y-axis label: "Γ  (10⁸ s⁻¹)"
  Chips: "Γ ∝ V²  (log-log slope = 2)" (TEAL), "H 2p: Γ = 6.27×10⁸ s⁻¹" (CRIMSON)
