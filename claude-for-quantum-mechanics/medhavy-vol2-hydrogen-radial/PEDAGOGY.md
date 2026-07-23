# PEDAGOGY — medhavy-vol2-hydrogen-radial

## What the learner already knows
Hydrogen wavefunction ψ₁₀₀, spherical harmonics, Born rule, expectation values.

## What this reel teaches
The workflow: how to prompt Claude Code to plot the 1s radial probability
density P(r) = (4/a₀³)r²e^(-2r/a₀), read the generated code and verify the
r² prefactor (the single most common error), run the sim and check two
predictions (peak at a₀, mean at 3a₀/2), then iterate to shade the area
beyond the peak.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- P(r) = (4/a₀³)r²e^(-2r/a₀) ✓ FACTCHECK
- r_mp = a₀ ≈ 0.0529 nm ✓
- ⟨r⟩ = 3a₀/2 ≈ 0.0794 nm ✓
- P1: P(r) peaks at r = a₀
- P2: ⟨r⟩ = 1.5a₀ > a₀ (right-skewed)

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
