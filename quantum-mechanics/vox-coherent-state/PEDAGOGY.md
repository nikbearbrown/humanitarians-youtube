# PEDAGOGY AUDIT — vox-coherent-state

## Concept chain
1. (B01) Hook: free packet spreads; special packet in harmonic well doesn't.
2. (B02) Demonstration: free Gaussian spreading over time.
3. (B03) Question: same Gaussian in a parabolic well never spreads — why?
4. (B04) Answer: restoring force cancels Fourier-component fanning; width stays locked.
5. (B05) The coherent state: oscillates at classical ω; σₓσₚ = ℏ/2 always.
6. (B06) Uniqueness: every other state in the well changes shape; only coherent state doesn't.
7. (B07) Analogy: classical ball in a bowl — coherent state is the quantum version.
8. (B08) Real-world: laser light is a coherent state; Glauber 1963; Nobel 2005.
9. (B09) Universality: coherent states underlie every laser, fiber, and quantum optics experiment.
10. (B10) Recap.

## Conceptual prerequisites
- Wave packet spreading (Candidate 12 / vox-packet-spreading)
- Harmonic oscillator potential
- Uncertainty principle

## Pedagogy checks
- Problem is stated before the answer (B02 shows the puzzle, B03 asks the question on screen).
- Question on screen in B03.
- Core concept (minimum-uncertainty, non-spreading) repeated at B05 and B10.
- Color law: TEAL = coherent state / non-spreading / locked; CRIMSON = free packet / spreading.
- Laser connection provides concrete real-world payoff (B08-B09).
- No jargon (coherent state, σₓσₚ) introduced without context.

## Exclusions enforced
- No |n⟩ expansion formula.
- No Poisson statistics derivation.
- No ladder-operator eigenvalue algebra.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Salaam, Medhavy" (Arabic/Persian; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE LOCKED WIDTH`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim beat (B02a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B01–B10 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-coherent-state`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-coherent-state --only B00,B11,B12`

VERDICT: PASS
