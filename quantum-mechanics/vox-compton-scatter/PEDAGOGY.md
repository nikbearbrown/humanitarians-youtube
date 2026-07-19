# PEDAGOGY AUDIT — vox-compton-scatter

## Concept chain
1. (B01) Hook: X-rays change wavelength — light acts like a billiard ball.
2. (B02) Classical failure: wave theory predicts zero shift — electron re-radiates at same frequency.
3. (B03) Question card: measured 0.071 → 0.073 nm; classical says no change; what gives?
4. (B04) Answer: photon carries momentum p = h/λ; elastic collision transfers energy to electron.
5. (B05) Formula: Δλ = (h/mₑc)(1−cosθ); Compton wavelength = 2.426 pm.
6. (B06) Angle dependence: 0° → no shift; 90° → 2.4 pm; 180° → 4.85 pm.
7. (B07) Numbers: 17.5 keV photon at 90°; 0.24 keV to electron.
8. (B08) Citation: Compton 1923, Nobel 1927; wave model crossed, particle model checked.
9. (B09) Bridge: photoelectric + Compton = both require light as discrete packets.
10. (B10) Recap.

## Conceptual prerequisites
- Wavelength, frequency, energy, momentum
- The idea that light carries momentum

## Pedagogy checks
- Problem stated before answer (B02 sets up classical failure, B03 question on screen).
- Question on screen in B03.
- Numbers in B05-B07 make the concept concrete.
- Color law: TEAL = quantum/correct, CRIMSON = classical/wrong.
- No relativistic kinematics algebra introduced.

## Exclusions enforced
- No relativistic-kinematics algebra.
- No Thomson scattering cross-section.
- No photoelectric effect recap.
- No Compton wavelength derivation.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Jambo, Medhavy" (Swahili; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE BILLIARD SHOT`. New Wonder-register narration. New audio: beat-B00.mp3.
- 7 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a). No narration; 2-second visual receipts. No audio generation needed.
- B11 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B12 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B10 narration, audio files, and graphic/manim references untouched. SlateCard remotion objects in inner beat shots preserved exactly.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-compton-scatter`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-compton-scatter --only B00,B11,B12`

VERDICT: PASS
