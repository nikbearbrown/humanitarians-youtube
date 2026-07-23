# PEDAGOGY AUDIT — vox-ultraviolet-catastrophe

| Act | Beats | Present? |
|---|---|---|
| COLD OPEN | B01–B02 | YES — concrete mystery: hot oven, classical prediction |
| THE QUESTION | B03 | YES — CARD + narration: infinite energy |
| THE PROBLEM | B04–B05 | YES — classical curve climbs forever; Planck's fix |
| THE MECHANISM | B06–B07 | YES — high-freq modes starved; Planck curve matches data |
| THE IMPLICATION | B08 | YES — energy not continuous, whole packets only |
| THE EXAMPLE | B09 | YES — illustrative 3000 K, kBT vs hν comparison |
| RECAP | B10 | YES — endcard + QUANTUM MECHANICS |

All checklist items PASS. Duration ~99s < 5:00.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Ciao, Medhavy" (Italian; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE CATASTROPHE`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-ultraviolet-catastrophe`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-ultraviolet-catastrophe --only B00,B11,B12`

VERDICT: PASS
