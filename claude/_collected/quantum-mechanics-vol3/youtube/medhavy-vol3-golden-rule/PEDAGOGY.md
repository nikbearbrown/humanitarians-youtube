# PEDAGOGY — medhavy-vol3-golden-rule

## What the learner already knows
Time-dependent perturbation theory, hydrogen energy levels, emission spectra.

## What this reel teaches
The workflow: how to prompt Claude Code to build a Fermi's Golden Rule rate-vs-coupling
plot, read the code and verify Γ = (2π/ℏ)|V|²ρ, run and check two predictions
(quadratic V² scaling, H 2p→1s rate = 6.27×10⁸ s⁻¹), then iterate to add a
linear comparison line.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- Γ = (2π/ℏ)|⟨f|V̂|i⟩|²ρ(E_f) ✓ FACTCHECK
- A(H 2p→1s) = 6.27×10⁸ s⁻¹ (NIST) ✓
- P1: rate scales as V² (log-log slope = 2)
- P2: at H matrix element, Γ = 6.27×10⁸ s⁻¹

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- All Text() in INK ✓

VERDICT: PASS
