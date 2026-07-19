# PEDAGOGY — medhavy-vol3-variational-floor

## What the learner already knows
Ground state energy, hydrogen-like atoms, effective nuclear charge.

## What this reel teaches
The workflow: how to prompt Claude Code to build a variational energy vs Z* plot
for helium, read the code and verify E(Z*) = 27.2×(Z*²-3.375Z*), run and check
two predictions (minimum at Z*=1.6875, E_min=-77.5 eV; floor at E₀=-79.0 eV
never crossed), then iterate to add a better trial state.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- E(Z*) = 27.2 × (Z*² − 3.375 Z*) for He, with 5/8 screening ✓ FACTCHECK
- Minimum: Z* = 27/16 = 1.6875, E_min = -77.5 eV ✓
- True E₀ = -79.0 eV (NIST) ✓
- P1: curve minimum above -79.0 eV floor
- P2: minimum at Z*=1.6875

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- All Text() in INK ✓

VERDICT: PASS
