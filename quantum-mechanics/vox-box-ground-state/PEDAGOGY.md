# PEDAGOGY AUDIT — vox-box-ground-state

## Act structure check (mandatory order)

| Act | Beats | Present? | Notes |
|---|---|---|---|
| COLD OPEN | B01–B02 | YES | Classical marble shown at rest with zero energy. Concrete, no thesis. |
| THE QUESTION | B03 | YES | CARD on screen + narration: "Classical physics predicts E=0 is allowed. The quantum particle's lowest energy is above zero. Why?" |
| THE PROBLEM | B04–B06 | YES | Wavefunction boundary conditions; minimum arch established |
| THE MECHANISM | B07–B09 | YES | Curvature = momentum = kinetic energy; zero is void |
| THE IMPLICATION | B08 | YES | Tighter box → higher energy (embedded in mechanism) |
| THE EXAMPLE | B10 | YES | Illustrative 1 nm box, 0.38 eV, comparison to visible light |
| RECAP | B11 | YES | Endcard: arch → momentum → energy → zero forbidden + QUANTUM MECHANICS |

## Key-case cold open check
- B01–B02: Classical marble shown sitting still. Concrete, no thesis. PASS.

## Gap formula check (THE QUESTION beat B03)
- "Classical physics predicts E = 0 is allowed. The quantum particle's lowest energy is above zero. Why?"
- Named on screen (CARD copy): "Classical physics predicts E = 0 is allowed. The quantum particle's lowest energy is above zero. Why?"
- Named in narration: B03 narration restates this.
- PASS.

## Utility-framing lint
Scanning for "is critical for" / "important to understand" / "we'll cover" / "in this video":
- None found in any beat narration.
- PASS.

## Vocabulary law (no term debuts before viewer needs it)
- wavefunction: debuts B04 after B03 establishes we need to describe the quantum particle's state. PASS.
- boundary condition: not named explicitly — shown as "walls force zero" in B04. PASS.
- ground state: debuts B06 as the name for the minimum arch already shown. PASS.
- momentum: debuts B07 after curvature established. PASS.
- kinetic energy: debuts B08 after momentum named. PASS.
- electron-volts: debuts B10 in illustrative example with immediate comparison context. PASS.

## Equations check
- No equations on screen in any beat.
- "E1 = pi²ℏ²/2mL²" not written — it is the formula behind the result but excluded from screen.
- Card exclusions: no eight-step derivation, no normalization, no n² table. Confirmed absent.
- PASS.

## Recap endcard check
- B11: "The wavefunction must arch. Any arch is momentum. Momentum is energy. Zero is forbidden."
- Kicker: "QUANTUM MECHANICS" on screen via LabelChip.
- No full book title, no chapter number. PASS.

## THE EXAMPLE act check
- B10 present, right before RECAP (B11). Illustrative numbers (1 nm box, 0.38 eV). Labeled "illustrative example" in narration. Comparison to visible light 2 eV gives scale. PASS.

## Duration check
- Total estimated: 111s (~1:51). Well under 5:00. PASS.

## Summary
All checklist items: PASS.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B01 title card → B00 `ClaudeComposerAsk` cold open, claude-medhavy channel. Greeting: "Hej, Medhavy" (Swedish; Medhavy 1-word budget, Wagwan is Bear-only). Topic eyebrow: `QUANTUM MECHANICS · THE FLOOR`. New Wonder-register narration. New audio: beat-B00.mp3.
- 8 ASK micro-beats inserted before each Manim/GRAPHIC beat (B01a, B03a, B04a, B05a, B06a, B07a, B08a, B09a). No narration; 2-second visual receipts. No audio generation needed.
- B12 `OutroSeries` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B13 `OutroCTA` → `ClaudeTitleOutro` restating full episode title, `@Medhavy` handle. New audio needed.
- Inner beats B02–B11 narration, audio files, and graphic/manim references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (was ElevenLabs NBB): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-box-ground-state`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/vox-box-ground-state --only B00,B12,B13`

VERDICT: PASS
