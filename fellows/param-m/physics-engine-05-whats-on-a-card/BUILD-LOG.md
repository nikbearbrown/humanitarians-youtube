# BUILD-LOG — whats-on-a-card

Physics Engine series, 5 of 12. Built 2026-10-31.

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

- **Preview QC (3 fixes):** B01 caption line ran into the card and "Common mistakes"
  wrapped → line moved down, label column widened with nowrap; B06 strip wrapped to
  two lines → shortened; B06 content sat high over an empty middle → moved down.
- **Docs vs table.** `COVERAGE.md`'s heading still says "16 cards"; its table and the
  code reflect the later library. Only figures the table and code agree on are used.
- **Project code not executed** (auto-mode permission check); results are
  repo-reported; MECH-005 (2.3717 m/s) and Moon escape velocity (2.375 km/s) hand-checked.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
