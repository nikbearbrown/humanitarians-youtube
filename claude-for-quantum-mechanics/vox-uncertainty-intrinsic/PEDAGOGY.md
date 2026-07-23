# PEDAGOGY AUDIT — vox-uncertainty-intrinsic

## Act structure check

| Act | Beat | Present? |
|-----|------|----------|
| COLD OPEN | B01 | YES — myth-busting hook: "not about bumping" |
| THE QUESTION | B03 | YES — no bump, yet limit persists |
| THE PROBLEM | B02 | YES — two histograms, no electron measured twice |
| THE MECHANISM | B04–B07 | YES — commutator, spike vs wave, Gaussian, Robertson |
| THE IMPLICATION | B08 | YES — commuting operators CAN be simultaneously sharp |
| THE EXAMPLE | B09 | YES — atom confinement, zero-point energy consequence |
| RECAP | B10 | YES — four-line summary |

## Analogy audit
- "Two histograms, no electron measured twice" — powerful falsification of disturbance myth
- "Spike in x = flat in p" — direct Fourier intuition
- "Gaussian = tightest compromise" — concrete minimum
- "Atoms collapsing" — high-stakes real consequence

## Misconception addressed
- Heisenberg microscope (photon kicks electron) myth — explicitly corrected (B01, B03)
- "Uncertainty is a practical measurement limit" — corrected (B03, B07)
- "All pairs of observables are uncertain" — corrected (B08: commuting pairs)

## Color law compliance
- TEAL = intrinsic quantum uncertainty / correct interpretation
- CRIMSON = disturbance myth / incorrect classical story

## Pacing check
- Total: ~99s narration, 10 beats
- No beat exceeds 11s narration
- Mechanism before example: YES

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Vanakkam, Medhavy" (Tamil; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE INTRINSIC LIMIT`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-uncertainty-intrinsic`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-uncertainty-intrinsic --only B00,B11,B12`

VERDICT: PASS
