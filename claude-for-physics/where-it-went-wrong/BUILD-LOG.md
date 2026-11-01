# BUILD-LOG — where-it-went-wrong

Physics Engine series, 10 of 12. Built 2026-10-31.

## Order of work

1. Read the grade-mode code and docs at `jashshah127/humanitariansai@2dc4aa4`; every
   figure ledgered in SOURCES.md.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat → Kokoro `af_bella` audio;
   checked with faster-whisper (tiny.en) — only name/term mishearings.
4. Preview stills of all 9 scenes before the 4K render; two first stills timed out
   (overloaded laptop), re-run clean.
5. Rendered at `--scale=2` (3840x2160); `./art final` → 4K master; QC sheet clean.

## What broke, and the fix

- **Browser timeouts** on preview stills under load: re-ran, no scene changes needed.
- **Not claimed:** no student has used grade mode; nothing is deployed (B06 says so).
- **Project code not executed** (auto-mode permission check); results are repo-reported.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
