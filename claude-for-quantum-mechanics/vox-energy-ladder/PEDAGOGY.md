# PEDAGOGY AUDIT — vox-energy-ladder

## Act structure check

| Act | Beat | Present? |
|-----|------|----------|
| COLD OPEN | B01 | YES — relatable examples (guitar, molecule, laser) |
| THE QUESTION | B03 | YES — smooth parabola forces discrete staircase |
| THE PROBLEM | B02 | YES — classical vs quantum energy |
| THE MECHANISM | B04–B07 | YES — ladder operators, ground state, full spectrum |
| THE IMPLICATION | B08 | YES — infrared spectrum ruler analogy |
| THE EXAMPLE | B09 | YES — liquid helium concrete consequence |
| RECAP | B10 | YES — tight four-line summary |

## Analogy audit
- Ladder/rungs: strong, direct physical image
- Guitar string evenly spaced overtones: accessible prior knowledge
- "Ruler" for infrared spectrum: concrete and visual
- Helium refusing to freeze: memorable real-world consequence

## Misconception addressed
- "Ground state has zero energy" — explicitly corrected (B06)
- "Classical oscillator has discrete energies" — corrected (B02)
- "Zero-point energy is just a math artifact" — corrected (B09)

## Color law compliance
- TEAL = quantum ladder / quantized / correct
- CRIMSON = classical continuous / disallowed

## Pacing check
- Total: ~100s narration, 10 beats
- No beat exceeds 11s narration
- Mechanics explained before example: YES

## Prerequisite check
- Assumes: wave function basics, Heisenberg uncertainty (mentioned not derived)
- No prior knowledge of operators required (concept introduced fresh)

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Shalom, Medhavy" (Hebrew; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE EQUAL STEPS`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-energy-ladder`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-energy-ladder --only B00,B11,B12`

VERDICT: PASS
