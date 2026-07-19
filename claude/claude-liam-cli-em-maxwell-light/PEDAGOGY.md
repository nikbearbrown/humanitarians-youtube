# PEDAGOGY — claude-liam-cli-em-maxwell-light

## Concept
Maxwell's Equations Consistency Checker: Light Falls Out

Maxwell added one term — displacement current — to resolve a mathematical
inconsistency in Ampère's law. In empty space with no sources, the corrected
equations produce a wave equation whose speed is 1/√(μ₀ε₀). Plugging in
constants measured entirely from electric and magnetic experiments (no optics),
you get 2.9979 × 10⁸ m/s — the measured speed of light. This reel builds that
check with Claude and runs a numerical wave simulation to confirm it.

## Learning objectives
1. Understand that Maxwell's displacement current was motivated by mathematical
   consistency, not experiment — a striking example of theory leading discovery.
2. Connect the wave speed formula c = 1/√(μ₀ε₀) to physical constants measurable
   with no reference to light.
3. See the leapfrog (Yee) scheme for the 1D wave equation and understand the
   Courant stability condition (r ≤ 1).
4. Understand superposition as a consequence of linearity — pulses pass through
   each other unchanged; EM waves do not scatter off each other.

## Pedagogical approach
- Teardown voice: problem → build → check → change → meaning → next move.
- Real code shown in B03 (ACTUAL-CODE LAW): the same script that produced the
  output numbers.
- Two Manim scenes make the abstract numerical output visual: the packet
  propagating at c (B04), and superposition in action (B06).
- "Your Turn" (B08) asks the viewer to probe numerical dispersion with a square
  wave — a natural follow-up that reveals finite-difference artifacts.

## Accuracy notes
- c_derived = 1/√(μ₀ε₀): uses scipy.constants mu_0 = 4π × 10⁻⁷ H/m and
  epsilon_0 = 8.8541878128 × 10⁻¹² F/m → c = 2.997924... × 10⁸ m/s.
  scipy.constants.c = 2.99792458 × 10⁸ m/s (exact by 1983 SI definition).
  Fractional error ≈ 4 × 10⁻⁷ (from rounding in constants, not physics).
- Leapfrog (Yee) scheme: second-order accurate in space and time. Courant = 0.5
  is safely below the stability limit of 1.
- Superposition: exact consequence of linearity of the wave equation. Pulses
  emerge completely unchanged — no amplitude loss, no phase shift.

## Prerequisites
- Basic calculus (partial derivatives conceptually)
- What a differential equation is (vague familiarity is enough)
- No prior electromagnetism required — the reel explains the contradiction and
  the fix from scratch

## VERDICT: PASS
