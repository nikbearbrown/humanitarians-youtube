# BUILD-LOG — dont-invent-the-mass

Physics Engine series, 4 of 12. Built 2026-10-31.

## Order of work

1. Read the source at `jashshah127/humanitariansai@2dc4aa4`; every figure ledgered in
   SOURCES.md and hand-checked where arithmetic is involved.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat for the series → Kokoro
   `af_bella` audio; transcribed with faster-whisper (tiny.en) to check it.
4. Preview stills of all 9 scenes before the 4K render; fixes below.
5. Rendered at `--scale=2` (3840×2160); frames checked at p≈0.5 and p≈0.93;
   `./art final` → 4K master.

## What broke, and the fix

- **Preview QC (3 fixes):** B01 flow row overflowed both frame edges → shorter chip
  text, smaller type; B04 strip wrapped with an orphaned "is wrong." → shortened;
  B02 "Before the fix" label wrapped → nowrap, wider column.
- **Docs disagree with each other.** `PHASE2.md`'s status table still lists the
  invented-values bug as known; its "Symbolic input mode" section says fixed and
  shows output. The video follows the section with evidence.
- **Project code not executed** (auto-mode permission check); results are
  repo-reported; the pulley formula hand-checked against MECH-003.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
