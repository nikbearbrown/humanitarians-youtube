# PEDAGOGY — medhavy-vol1-packet-spread

## What the learner already knows
Fourier superposition, free-particle Schrödinger equation, Gaussian integrals, uncertainty principle basics.

## What this reel teaches
The workflow: how to prompt Claude Code to simulate a Gaussian wave packet
spreading over time, read the generated code and verify the σ(t) formula
and doubling-time formula τ=2mσ₀²/ℏ, run the simulation and check two
predictions (centroid moves at classical group velocity, width reaches √2·σ₀
at t=τ), then iterate to annotate the doubling point.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- σ(t) = σ₀√(1+(ℏt/2mσ₀²)²) ✓ FACTCHECK
- τ = 2mσ₀²/ℏ ≈ 17.3 fs for σ₀=1 nm, m=m_e ✓
- σ(τ) = √2·σ₀ exactly ✓
- v_g = ℏk₀/m (classical velocity) ✓
- P1: centroid moves at v_g
- P2: width reaches √2·σ₀ at t=τ

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B00 `MedhavyOpen` → `ClaudeComposerAsk` cold open. Greeting: "Aloha, Medhavy" (Hawaiian; Medhavy 1-word budget). Topic eyebrow: `QUANTUM MECHANICS · WAVE PACKET`. New Wonder-register narration. New audio: beat-B00.mp3 (replaces old intro).
- No ASK micro-beats inserted — inner beats are screen recordings/code displays, not Manim-generated graphics.
- B05 `MedhavyOutro` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B06 new `ClaudeTitleOutro` beat added. New audio needed.
- Inner beats B01–B04 narration, audio files, and remotion references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (existing use voice_id 1sgY6Voq1aexKOB1IJ2D directly): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/medhavy-vol1-packet-spread`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/medhavy-vol1-packet-spread --only B00,B05,B06`

VERDICT: PASS
