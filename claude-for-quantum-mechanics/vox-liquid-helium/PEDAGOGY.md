# PEDAGOGY AUDIT — vox-liquid-helium

## Concept chain
1. (B01) Hook: Helium stays liquid at absolute zero. Unusual.
2. (B02) Setup: Cooling removes thermal energy; classically atoms should freeze into lattice.
3. (B03) Question: At 0 K no thermal motion remains — why doesn't helium freeze?
4. (B04) Answer: Zero-point energy. Confinement costs irreducible kinetic energy.
5. (B05) Numbers: Helium in lattice site (3 Å sphere) → ZPE ~10 meV per atom.
6. (B06) Key comparison: van der Waals binding ~1 meV. ZPE wins. Atoms shake free.
7. (B07) Contrast with neon: heavier → smaller ZPE → lattice wins → freezes.
8. (B08) Pressure override: above 25 atm deeper well overwhelms ZPE; helium finally freezes.
9. (B09) Universality: ZPE is real — Casimir force, vacuum energy.
10. (B10) Recap.

## Conceptual prerequisites
- Absolute zero, lattice/crystal structure, kinetic energy
- The idea that quantum ground states carry nonzero energy

## Pedagogy checks
- Problem stated before answer (B02 setup, B03 question on screen).
- Question appears on screen in B03.
- Concrete numbers in B05-B06 make the concept tangible.
- Neon contrast (B07) makes the mass-dependence clear.
- Pressure fix (B08) prevents the misconception that helium never freezes.
- Color law: TEAL = quantum motion / ZPE / real; CRIMSON = classical freeze / wrong prediction.

## Exclusions enforced
- No Casimir force calculation.
- No superfluid transition.
- No ladder-operator algebra.
- No He-4/He-3 distinction.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Cześć, Medhavy" (Polish; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE QUANTUM LIQUID`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-liquid-helium`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-liquid-helium --only B00,B11,B12`

VERDICT: PASS
