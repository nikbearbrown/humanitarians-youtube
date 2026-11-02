# BUILD-LOG — measure-first

Physics Engine series, 12 of 12. Built 2026-10-31.

## Order of work

1. Read the project plan, decision log, golden set, UGPhysics notes and status table at
   `jashshah127/humanitariansai@2dc4aa4`; every figure ledgered in SOURCES.md.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat → Kokoro `af_bella` audio;
   checked with faster-whisper (tiny.en).
4. Preview stills of all 9 scenes before the 4K render — clean.
5. Rendered at `--scale=2` (3840x2160) in slow mode; `./art final` → 4K master.

## What broke, and the fix

- **Render timeouts overnight** under background-QoS throttling: nothing usable; added
  `--timeout=300000` and an orphaned-browser reaper, then all 11 beats rendered in one pass.
- **Not claimed:** the plain-AI baseline has never been run, and nothing is deployed
  (B06 says so).
- **Project code not executed** (auto-mode permission check); results are repo-reported.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
