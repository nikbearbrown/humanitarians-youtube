# PEDAGOGY AUDIT — vox-photoelectric

## Concept chain
1. (B01) Hook: Red lamp → zero electrons; UV penlight → electrons. Difference is frequency.
2. (B02) Three experimental facts that classical wave theory cannot explain.
3. (B03) Question: Why does a sharp threshold exist at all?
4. (B04) Answer: Light comes as photons, each carrying hν; one photon, one electron.
5. (B05) Einstein equation: KE = hν − Φ; below threshold, no escape.
6. (B06) Sodium worked example: 546 nm (2.27 eV) fails; 300 nm (4.13 eV) succeeds.
7. (B07) Key insight: photons cannot pool energy — each acts alone.
8. (B08) Intensity vs frequency: intensity = count, frequency = energy per photon.
9. (B09) Millikan confirmation; Einstein Nobel 1921.
10. (B10) Recap.

## Conceptual prerequisites
- Frequency, wavelength, energy of light
- Work function as an escape energy
- The idea that light could be discrete

## Pedagogy checks
- Problem stated before answer (B02 lays out the puzzle; B03 asks the question on screen).
- Question on screen in B03.
- The worked example (B06) makes the numbers concrete.
- Color law: TEAL = above threshold / ejected; CRIMSON = below threshold / blocked.
- "Photons cannot pool" (B07) addresses the most common misconception.
- No jargon introduced without immediate definition.

## Exclusions enforced
- No stopping-potential algebra.
- No Einstein-equation derivation.
- No Compton scattering.
- No detailed Millikan biography.

VERDICT: PASS

---

## Refactor addendum — Claude cut (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open. Greeting: "Hola, Bear" (Spanish; Wagwan check: charsum % 10 = 1, not 0). Topic eyebrow: `QUANTUM MECHANICS · THE THRESHOLD`. Narration reuses beat-B01.mp3 (same hook text — no new audio spend).
- 7 ASK micro-beats inserted (B01a, B03a, B04a, B05a, B06a, B07a, B08a) before each Manim graphic beat. No narration; 2-second visual receipts showing the generation prompt. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." Command: copper work-function exercise. New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title with terracotta period, `@HumanitariansAI` beneath. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched.
- New audio to generate: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-photoelectric --only B11,B12`

VERDICT: PASS
