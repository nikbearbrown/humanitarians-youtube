# SHOTLIST — medhavy-vol3-stm-tunneling

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_STMRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Color Law
TEAL: I(d) = exp(−2κd) tunneling curve
CRIMSON: Two marker dots 1 Å apart showing 7× current ratio
INK: all Text()

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: semi-log plot of I vs d (d in Å, I on natural-log y-axis)
  x_range=[1, 10] Å; y_range=[−14, 0] (ln I units)
  TEAL curve: ln(I) = −2κd, κ=1.024 Å⁻¹
  CRIMSON dots at (d=4, ln I_4) and (d=5, ln I_5), DoubleArrow between them
  Gap label: "×7.4 per Å"
  Chips: "slope = −2κ ≈ −2.05 Å⁻¹" (TEAL), "×7 per Å gap" (CRIMSON)
