# PEDAGOGY — medhavy-vol3-stm-tunneling

## What the learner already knows
WKB approximation, tunneling through a barrier, exponential decay of wavefunctions.

## What this reel teaches
The workflow: how to prompt Claude Code to build an STM tunneling current curve,
read the code and verify κ = √(2mφ)/ℏ ≈ 1.02 Å⁻¹ for φ=4 eV, run and check
two predictions (semi-log slope = −2κ, seven-times current rule per Å), then
iterate to add a second work-function curve.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- κ = √(2mφ)/ℏ ≈ 1.024 Å⁻¹ for φ=4 eV ✓ FACTCHECK
- exp(2κ × 1 Å) = exp(2.048) ≈ 7.75 ✓ (Binnig-Rohrer rule)
- P1: ln(I) vs d has slope −2κ ≈ −2.05 Å⁻¹
- P2: +1 Å gap → current × (1/7.4) rule

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
