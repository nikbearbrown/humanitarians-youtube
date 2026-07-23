# SHOTLIST — medhavy-vol1-sandbox-benchmark

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_SandboxRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Act Map
B00: MEDHAVY INTRO
B01: SANDBOX — PROMPT
B02: SANDBOX — SCRIPT
B03: SANDBOX — RUN (Manim: tridiagonal H, analytic vs numerical levels)
B04: SANDBOX — CHANGE
B05: MEDHAVY OUTRO

## Color Law
TEAL: numerical eigenvalue dots, matrix diagonal label
CRIMSON: analytic eigenvalue lines, error annotation
INK: all Text()

## Exclusions
No Numerov shooting method, no time evolution mode, no Crank-Nicolson,
no explicit Euler stability analysis on screen.

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: two-panel layout.
  Left: schematic tridiagonal matrix (5×5 excerpt) with diagonal=2t_k,
        off-diagonals=-t_k. INK rectangles; TEAL diagonal label; CRIMSON off-diag.
  Right: energy level comparison — CRIMSON horizontal lines = analytic E_n,
         TEAL dots = numerical E_n — for n=1..4.
         Labels: n=1 ratio 1.000, n=2 ratio 4.000, etc.
  Chips: "E₂/E₁ = 4.000" (TEAL), "error < 10⁻⁵" (CRIMSON)
