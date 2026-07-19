# PEDAGOGY AUDIT — vox-ramsauer-resonance

| Act | Beats | Present? |
|---|---|---|
| COLD OPEN | B01–B02 | YES — concrete mystery: normal barrier always reflects, then the exception |
| THE QUESTION | B03 | YES — CARD + narration |
| THE PROBLEM | B04–B05 | YES — shorter wavelength inside, two wall reflections |
| THE MECHANISM | B06–B07 | YES — destructive interference, anti-reflection analogy |
| THE IMPLICATION | B08 | YES — resonance condition 2*k2*L = n*pi |
| THE EXAMPLE | B09 | YES — illustrative 0.3 nm barrier, 5 eV well, ~3 eV resonance |
| RECAP | B10 | YES — endcard + QUANTUM MECHANICS |

All checklist items PASS. Duration ~99s < 5:00.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Sawadee, Medhavy" (Thai; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE INVISIBLE BARRIER`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-ramsauer-resonance`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-ramsauer-resonance --only B00,B11,B12`

VERDICT: PASS
