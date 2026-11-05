# BUILD-LOG — check-it-another-way

Physics Engine series, 8 of 12. Built 2026-10-31.

## Order of work

1. Read `engine/pipeline.py` `verify()`, `models.py`, the `formula_kb.py` verify_fn
   lines, golden set EM-004/EM-005 at `jashshah127/humanitariansai@2dc4aa4`; every
   figure ledgered in SOURCES.md.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat → Kokoro `af_bella` audio;
   checked with faster-whisper (tiny.en).
4. Preview stills before the 4K render; layout fixes applied.
5. Rendered at `--scale=2` (3840x2160) in slow mode (nice 19, background QoS);
   `./art final` → 4K master.

## What broke, and the fix

- **Preview QC:** layout overflows fixed before the 4K render.
- **Hand check:** EM-005 9 V x (1 - e^-1) = 5.6891 V matches the golden set.
- **Project code not executed** (auto-mode permission check); results are repo-reported.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
