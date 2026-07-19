# PEDAGOGY AUDIT — vox-spinning-phase

| Act | Beats | Present? |
|---|---|---|
| COLD OPEN | B01–B02 | YES — concrete paradox: nothing moves, yet it spins |
| THE QUESTION | B03 | YES — CARD + narration: spinning thing casting still shadow |
| THE PROBLEM | B04–B05 | YES — clock hand model, phase rotation rate |
| THE MECHANISM | B06–B07 | YES — |psi|^2 = length^2, independent of rotation angle |
| THE IMPLICATION | B08 | YES — mixing two rates makes shadow move |
| THE EXAMPLE | B09 | YES — illustrative 1 eV, 1.5e15 rotations/sec |
| RECAP | B10 | YES — endcard + QUANTUM MECHANICS |

All checklist items PASS. Duration ~99s < 5:00.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Hallo, Medhavy" (German; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE SPINNING CLOCK`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-spinning-phase`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-spinning-phase --only B00,B11,B12`

VERDICT: PASS
