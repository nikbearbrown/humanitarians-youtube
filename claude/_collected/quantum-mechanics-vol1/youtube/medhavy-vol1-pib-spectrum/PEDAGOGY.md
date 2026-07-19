# PEDAGOGY — medhavy-vol1-pib-spectrum

## What the learner already knows
- Sine waves and boundary conditions (waves that vanish at fixed endpoints)
- Basic energy concepts in eV
- What a wavefunction is (probability amplitude)

## What this reel teaches
**The workflow, not the physics:** how to write a generation prompt that specifies
the physical rule (E_n = n²π²ℏ²/2mL²), the concrete numbers (L=2 nm, m=m_e),
and the visual artifact (energy ladder with n=1,2,3 wavefunctions). How to read
the generated code and find the physics line. How to verify two testable
predictions (ratio E₂/E₁ = 4; L-scaling as 1/L²). How to issue a follow-up
change command.

## Loop structure
1. PROMPT: specify rule + numbers + visual → claude generates the scene
2. SCRIPT: read the file, find E_n calculation line, verify n² exponent
3. RUN: watch the energy ladder animate; check E₂/E₁ = 4 with ratio chip
4. CHANGE: update to add L-slider showing 1/L² dependence

## Physics gate numbers
- E₁(L=2 nm) = 0.094 eV ✓ (FACTCHECK verified)
- E₂/E₁ = 4.000 ✓
- E₃/E₁ = 9.000 ✓
- P1: ratio 4 (unit-independent test)
- P2: L halved → E₁ quadruples (0.094 → 0.376 eV)

## Act structure compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- Pronunciation: narration uses "med dahvy"; screen shows "Medhavy" ✓
- No sentence-length labels on Manim frames ✓
- All Text() in INK ✓
- Shape fills use TEAL/CRIMSON only ✓

## Utility-framing lint
- No "important to understand" or "in this video" in narration ✓
- Focus on the workflow loop (prompt→read→run→check→change) ✓

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B00 `MedhavyOpen` → `ClaudeComposerAsk` cold open. Greeting: "Bula, Medhavy" (Fijian; Medhavy 1-word budget). Topic eyebrow: `QUANTUM MECHANICS · ENERGY LADDER`. New Wonder-register narration. New audio: beat-B00.mp3 (replaces old intro).
- No ASK micro-beats inserted — inner beats are screen recordings/code displays, not Manim-generated graphics.
- B05 `MedhavyOutro` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B06 new `ClaudeTitleOutro` beat added. New audio needed.
- Inner beats B01–B04 narration, audio files, and remotion references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (existing use voice_id 1sgY6Voq1aexKOB1IJ2D directly): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/medhavy-vol1-pib-spectrum`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/medhavy-vol1-pib-spectrum --only B00,B05,B06`

VERDICT: PASS
