# SHOTLIST — medhavy-vol2-bloch-rotation

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_BlochRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Act Map
B00: MEDHAVY INTRO
B01: BLOCH ROTATION — PROMPT
B02: BLOCH ROTATION — SCRIPT
B03: BLOCH ROTATION — RUN (Manim: Bloch sphere cross-section, 3 key states)
B04: BLOCH ROTATION — CHANGE
B05: MEDHAVY OUTRO

## Color Law
TEAL: Bloch sphere circle, |↑⟩ state arrow (north pole)
CRIMSON: |+⟩ state arrow (equator), ⟨Z⟩=0 annotation
INK: all Text()

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: 2D cross-section (x-z plane) of Bloch sphere.
  SLATE circle (unit radius, scaled). z-axis vertical, x-axis horizontal.
  Labels at poles and equator: |↑⟩, |↓⟩, |+⟩, |−⟩
  TEAL arrow: Bloch vector for |↑⟩ (north pole)
  CRIMSON arrow: Bloch vector for |+⟩ (equator, x-axis)
  Chips: "θ=0 → P(+)=1" (TEAL), "θ=π/2 → ⟨Z⟩=0" (CRIMSON)
