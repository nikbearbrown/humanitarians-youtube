# PEDAGOGY — medhavy-vol2-bloch-rotation

## What the learner already knows
Qubit state |ψ⟩=α|↑⟩+β|↓⟩, Born rule, Pauli matrices, measurement postulate.

## What this reel teaches
The workflow: how to prompt Claude Code to draw the Bloch sphere cross-section
and place key states on it, read the generated code and verify the half-angle
parameterization (θ/2, not θ), run the sim and check two predictions (|↑⟩ at
north pole gives P(+)=1, equatorial state gives ⟨Z⟩=0), then iterate to add
the |−⟩ label.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- |ψ⟩ = cos(θ/2)|↑⟩ + e^(iφ)sin(θ/2)|↓⟩ ✓ FACTCHECK
- |↑⟩: θ=0 → north pole ✓
- |+⟩: θ=π/2 → equator ✓
- P1: θ=0 → P(+) = cos²(0) = 1
- P2: θ=π/2 → ⟨Z⟩ = cos(π/2) = 0

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
