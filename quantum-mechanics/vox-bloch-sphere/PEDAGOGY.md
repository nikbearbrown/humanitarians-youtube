# PEDAGOGY AUDIT — vox-bloch-sphere

## Act structure check

| Act | Beat | Present? |
|-----|------|----------|
| COLD OPEN | B01 | YES — "every superposition is a point on a sphere" hook |
| THE QUESTION | B03 | YES — 4 params → 2 → why a sphere? |
| THE PROBLEM | B02 | YES — parameter counting |
| THE MECHANISM | B04–B07 | YES — theta/phi, poles, equator, relative phase, global phase |
| THE IMPLICATION | B08 | YES — Bloch vector as sanity check |
| THE EXAMPLE | B09 | YES — physical qubits: electron, photon, circuit |
| RECAP | B10 | YES — four-line summary |

## Analogy audit
- "Pointing to a spot on a sphere" — direct geometric intuition
- "Poles are definite, equator is superposition" — clean physical meaning
- "Runtime check: |r|=1" — practical utility for students

## Misconception addressed
- "Global phase is physically real" — corrected (B07)
- "Qubit has 4 free parameters" — corrected via counting (B02, B03)

## Color law compliance
- TEAL = Bloch sphere surface / pure states / observable
- CRIMSON = global phase / unobservable / removed from state space

## Pacing check
- Total: ~96s narration, 10 beats
- Mechanism before example: YES

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Ahoj, Medhavy" (Czech; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE QUBIT SPHERE`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-bloch-sphere`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-bloch-sphere --only B00,B11,B12`

VERDICT: PASS
