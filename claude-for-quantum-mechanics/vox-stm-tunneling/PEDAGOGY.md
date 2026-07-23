# PEDAGOGY AUDIT — vox-stm-tunneling

## Concept chain
1. (B01) Hook: STM images single atoms — secret is the factor-of-ten per ångström.
2. (B02) Setup: tip hovers without touching; electrons tunnel across the vacuum gap.
3. (B03) Question: classically no current should flow — so why does it?
4. (B04) Answer part 1: wavefunction decays exponentially in the barrier, ψ ~ e^(−κd).
5. (B05) Answer part 2: current ∝ ψ² ~ e^(−2κd); κ ≈ 1.025 Å⁻¹ for 4 eV barrier.
6. (B06) The key number: 1 Å gap increase → current drops by factor ~7–10.
7. (B07) Why atomic resolution: the single closest atom on the tip dominates by 7–10×.
8. (B08) How scanning works: current spike as tip passes over each surface atom.
9. (B09) Universality: same exponential in alpha decay and photosynthesis.
10. (B10) Recap.

## Conceptual prerequisites
- Quantum tunneling basics (covered in Candidate 03 / vox-quantum-tunneling)
- Exponential decay
- Electric current

## Pedagogy checks
- Problem is stated before the answer (B02-B03 establish the puzzle).
- Question appears on screen in B03.
- The core number (factor of ten per ångström) is repeated at hook (B01) and recap (B10).
- Color law: TEAL = current/quantum/works; CRIMSON = classical/gap/no current.
- No jargon introduced without context.
- The video does not go beyond the stated exclusions.

## Exclusions enforced
- No work-function derivation of κ.
- No feedback-electronics detail.
- No barrier-matching algebra.
- No four-region wavefunction matching.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Halo, Medhavy" (Indonesian; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE EXPONENTIAL RULER`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-stm-tunneling`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-stm-tunneling --only B00,B11,B12`

VERDICT: PASS
