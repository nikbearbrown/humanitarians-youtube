# PEDAGOGY AUDIT — vox-double-slit-self

| Act | Beats | Present? |
|---|---|---|
| COLD OPEN | B01–B02 | YES — concrete mystery shown |
| THE QUESTION | B03 | YES — CARD + narration |
| THE PROBLEM | B04–B05 | YES — dot + both-slit wave |
| THE MECHANISM | B06–B07 | YES — interference builds pattern |
| THE IMPLICATION | B08 | YES — de Broglie wavelength |
| THE EXAMPLE | B09 | YES — illustrative 54 eV numbers |
| RECAP | B10 | YES — endcard + QUANTUM MECHANICS |

All checklist items PASS. Duration ~99s < 5:00.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Annyeong, Medhavy" (Korean; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · ONE ELECTRON`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-double-slit-self`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-double-slit-self --only B00,B11,B12`

VERDICT: PASS
