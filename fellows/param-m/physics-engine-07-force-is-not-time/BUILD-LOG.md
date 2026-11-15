# BUILD-LOG — force-is-not-time

Physics Engine series, 7 of 12. Built 2026-10-31.

## Order of work

1. Read `engine/units.py`, `variable_glossary.py`, `eval/ci_check.py`, `PHASE1.md` at
   `jashshah127/humanitariansai@2dc4aa4`; every figure ledgered in SOURCES.md.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat for the series → Kokoro
   `af_bella` audio; transcribed with faster-whisper (tiny.en) to check it.
4. Preview stills of all scenes before the 4K render; fixes below.
5. Rendered at `--scale=2` (3840×2160); frames checked at p≈0.5 and p≈0.93;
   `./art final` → 4K master.

## What broke, and the fix

- **Preview QC (3 fixes):** "The check" wrapped in its B00B tile → smaller tile type;
  "sympy.physics.units" overflowed its B06 card → smaller mono; B05 quote orphaned
  "trigger." → explicit line break, shorter text.
- **Claim left out.** `PHASE2.md` says a Celsius temperature pushes Carnot efficiency
  outside (0, 1); with typical values it doesn't, so the video doesn't repeat it.
- **Project code not executed** (auto-mode permission check); results are repo-reported.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
