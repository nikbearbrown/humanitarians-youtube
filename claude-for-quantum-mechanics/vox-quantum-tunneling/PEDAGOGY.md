# PEDAGOGY AUDIT — vox-quantum-tunneling

## Act structure check

| Act | Beats | Present? | Notes |
|---|---|---|---|
| COLD OPEN | B01–B02 | YES | Classical bounce shown. No thesis. |
| THE QUESTION | B03 | YES | CARD + narration: "Classical predicts total reflection when E < V. Here some fraction transmits. Why?" |
| THE PROBLEM | B04–B05 | YES | Exponential decay + non-zero tail |
| THE MECHANISM | B06–B07 | YES | T ~ e^(-2kappa*L); same energy after tunnel |
| THE IMPLICATION | B08 | YES | Alpha decay, STM, solar fusion |
| THE EXAMPLE | B09 | YES | Illustrative numbers, right before recap |
| RECAP | B10 | YES | Endcard + QUANTUM MECHANICS |

## Key-case cold open: PASS (classical ball bouncing shown)
## Gap formula: PASS (B03 card + narration)
## Utility-framing lint: PASS (no forbidden phrases)
## Vocabulary law: PASS (all terms debut after need established)
## Equations: PASS (T ~ e^(-2kappa*L) is a labeled ratio, not derived)
## Recap: PASS (question→answer + QUANTUM MECHANICS)
## THE EXAMPLE: PASS (B09, illustrative labeled, before B10 recap)
## Duration: ~98s < 5:00. PASS.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Bonjour, Medhavy" (French; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THROUGH THE WALL`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-quantum-tunneling`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-quantum-tunneling --only B00,B11,B12`

VERDICT: PASS
