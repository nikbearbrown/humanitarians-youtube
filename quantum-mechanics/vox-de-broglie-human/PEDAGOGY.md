# PEDAGOGY AUDIT — vox-de-broglie-human

## Act structure check

| Act | Beat | Present? |
|-----|------|----------|
| COLD OPEN | B01 | YES — electrons diffract, you don't — same physics |
| THE QUESTION | B03 | YES — electron diffract, why not you? |
| THE PROBLEM | B02 | YES — de Broglie formula |
| THE MECHANISM | B04–B06 | YES — calculation, scale comparison, slit condition |
| THE IMPLICATION | B07 | YES — quantum never turns off, just undetectable |
| THE EXAMPLE | B08 | YES — buckyball diffraction as largest real example |
| THE CONCLUSION | B09 | YES — classical limit quantitative |
| RECAP | B10 | YES — four-line summary |

## Analogy audit
- "Walking through a doorway" — direct everyday experience
- Proton radius comparison — gives sense of scale of 10^-35 m
- Buckyball as largest diffracted object: 1999 experiment = concrete landmark

## Misconception addressed
- "Quantum mechanics only applies to small things" — corrected (B07, B09)
- "Diffraction needs waves, not particles" — not explicitly addressed (not required)

## Color law compliance
- TEAL = quantum / wavelength visible / diffraction works
- CRIMSON = classical / wavelength unmeasurably small

## Pacing check
- Total: ~95s narration, 10 beats
- Calculation before scale comparison: YES
- Scale comparison before implication: YES

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Merhaba, Medhavy" (Turkish; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE INVISIBLE WAVE`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-de-broglie-human`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-de-broglie-human --only B00,B11,B12`

VERDICT: PASS
