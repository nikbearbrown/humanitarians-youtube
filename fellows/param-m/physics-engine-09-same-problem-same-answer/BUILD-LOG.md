# BUILD-LOG — same-problem-same-answer

Physics Engine series, 9 of 12. Built 2026-10-31.

## Order of work

1. Read `engine/README.md` V2, `pipeline.py` `solve_physics_problem()`, `parse.py`,
   `eval/demo.py` V2 checks, `EVALUATION.md` at `jashshah127/humanitariansai@2dc4aa4`;
   every figure ledgered in SOURCES.md.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat → Kokoro `af_bella` audio;
   checked with faster-whisper (tiny.en).
4. Preview stills before the 4K render; layout fixes applied.
5. Rendered at `--scale=2` (3840x2160) in slow mode (nice 19, background QoS);
   `./art final` → 4K master.

## What broke, and the fix

- **6 of 11 beats timed out** on the first render ("Timed out … while trying to connect
  to the browser"): the laptop was overloaded, not a scene bug. Re-ran the render;
  the filled beats were skipped and the 6 rendered cleanly.
- **Not claimed:** the engine isn't deterministic end to end; parsing uses a model and
  can vary (B06 says so).
- **Project code not executed** (auto-mode permission check); results are repo-reported.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
