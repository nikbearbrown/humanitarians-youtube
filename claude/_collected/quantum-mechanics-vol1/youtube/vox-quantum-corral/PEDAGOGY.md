# PEDAGOGY AUDIT — vox-quantum-corral

## Concept chain
1. (B01) Hook: IBM 1993, 48 iron atoms, concentric rings nobody placed.
2. (B02) Setup: Ring of iron atoms acts as a wall; electrons bounce back.
3. (B03) Question: Classical would be smooth; quantum shows rings. Where do they come from?
4. (B04) Answer: Wave function must vanish at boundary; only modes that fit survive.
5. (B05) Discrete modes: first mode = central peak; second mode = peak + ring; etc.
6. (B06) Numbers: 7 nm corral, ground-state wavelength ~14 nm.
7. (B07) Analogy: guitar string harmonics — ends fixed → only harmonics survive.
8. (B08) Universality: same principle in quantum dots, wells, atoms.
9. (B09) Historical impact: Crommie et al. 1993, wave function as photograph.
10. (B10) Recap.

## Conceptual prerequisites
- Standing wave, boundary condition, wavelength
- The idea that only certain waves fit a bounded space

## Pedagogy checks
- Problem stated before answer (B02-B03 establish the puzzle, B03 question on screen).
- Question on screen in B03.
- Guitar string analogy (B07) connects to familiar experience.
- Numbers in B06 make the concept concrete.
- Color law: TEAL = fitting modes / standing waves; CRIMSON = non-fitting / classical smooth.
- No Bessel-function formalism introduced.

## Exclusions enforced
- No Schrödinger equation derivation.
- No Bessel-function radial eigenstates.
- No STM tip mechanics.
- No comparison to infinite-square-well energies.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Selam, Medhavy" (Amharic; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · QUANTIZATION MADE VISIBLE`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-quantum-corral`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-quantum-corral --only B00,B11,B12`

VERDICT: PASS
