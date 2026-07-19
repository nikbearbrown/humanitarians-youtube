# PEDAGOGY — medhavy-vol2-uncertainty-squeeze

## What the learner already knows
Position and momentum operators, commutator [x,p]=iℏ, standard deviation, Gaussian states.

## What this reel teaches
The workflow: how to prompt Claude Code to visualize the Kennard inequality
as a hyperbola in σ_x–σ_p space, read the generated code and verify the
ℏ/2 denominator (not ℏ), run the sim and check two predictions (Gaussian
state sits ON the hyperbola, squeezing σ_x by 2 doubles σ_p exactly), then
iterate to add an allowed-region shade.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- σ_x σ_p ≥ ℏ/2 ✓ FACTCHECK
- Gaussian minimum: σ_x σ_p = ℏ/2 ✓
- σ_x = 1 nm → σ_p = 5.27×10⁻²⁶ kg·m/s ✓
- P1: minimum uncertainty state lies ON the hyperbola
- P2: halving σ_x doubles σ_p

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
