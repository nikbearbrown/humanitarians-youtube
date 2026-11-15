# BUILD-LOG — the-engine-that-says-no

Physics Engine series, 6 of 12. Built 2026-10-31.

## Order of work

1. Read `engine/pipeline.py` `plan()`, `PHASE1.md`, `PHASE2.md`, `eval/ci_check.py` at
   `jashshah127/humanitariansai@2dc4aa4`; every figure ledgered in SOURCES.md.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat for the series → Kokoro
   `af_bella` audio; transcribed with faster-whisper (tiny.en) to check it.
4. Preview stills of all 9 scenes before the 4K render; fixes below.
5. Rendered at `--scale=2` (3840×2160); frames checked at p≈0.5 and p≈0.93;
   `./art final` → 4K master.

## What broke, and the fix

- **Preview QC:** B05 chip row overflowed both frame edges → equation moved to the
  caption, shorter chips; B05 quote wrapped with an orphaned "gap." → wider card;
  B02 third reason ran off the right edge → shorter reason string; B06 eyebrow label
  was unpositioned → absolutely positioned under the spark line.
- **Overload timeout.** Running preview stills alongside a 4K master on the 8 GB M1
  timed out the headless browser (load average ~106). Stopped the stills; one job at a
  time from then on.
- **Series resized to 12.** Labels changed from "6 of 12" to "6 of 12" before render.
- **Project code not executed** (auto-mode permission check); results are repo-reported.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
