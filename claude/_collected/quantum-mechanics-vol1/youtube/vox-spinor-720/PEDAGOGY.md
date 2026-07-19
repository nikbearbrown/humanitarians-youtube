# PEDAGOGY AUDIT — vox-spinor-720

## Act structure check

| Act | Beat | Present? |
|-----|------|----------|
| COLD OPEN | B01 | YES — baseball vs electron contrast hook |
| THE QUESTION | B03 | YES — 360° doesn't return the state |
| THE PROBLEM | B02 | YES — classical rotation for contrast |
| THE MECHANISM | B04–B06 | YES — theta/2, minus sign at 360°, return at 720° |
| THE IMPLICATION | B07 | YES — interference reveals the minus sign |
| THE EXAMPLE | B08 | YES — 1975 neutron interferometry experiment |
| EXTRA | B09 | YES — double cover concept |
| RECAP | B10 | YES — tight four-line summary |

## Analogy audit
- "Baseball vs electron" — strong contrast opener
- "Sign flag" on the Bloch arrow — concrete visual
- "Amplitudes add, not probabilities" — correct key distinction
- Neutron interferometer: real physical confirmation

## Misconception addressed
- "360° must return anything to original state" — corrected (B05: minus sign)
- "Minus sign is unmeasurable" — corrected (B07: interference)

## Color law compliance
- TEAL = quantum spinor / 720° period / correct
- CRIMSON = classical vector / 360° period / contrast

## Pacing check
- Total: ~97s narration, 10 beats
- Mechanism before experiment: YES

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Privet, Medhavy" (Russian; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE 720 DEGREE TURN`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-spinor-720`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-spinor-720 --only B00,B11,B12`

VERDICT: PASS
