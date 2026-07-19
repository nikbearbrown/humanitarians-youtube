# SHOTLIST — medhavy-vol3-variational-floor

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_VariationalRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Color Law
TEAL: E(Z*) variational energy curve
CRIMSON: True ground state floor at E₀ = -79.0 eV (dashed horizontal line)
INK: all Text()

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: E(Z*) vs Z* for helium
  x_range=[1, 3]; y_range=[-82, -60] eV
  TEAL curve: E(Z*) = 27.2 × (Z*² − 3.375 × Z*)
  CRIMSON dashed floor at E = -79.0 eV
  TEAL dot at minimum (Z*=1.6875, E=-77.5 eV)
  Labels: minimum annotation, floor label
  Chips: "min at Z*=1.69: −77.5 eV" (TEAL), "true E₀=−79.0 eV (NIST)" (CRIMSON)
