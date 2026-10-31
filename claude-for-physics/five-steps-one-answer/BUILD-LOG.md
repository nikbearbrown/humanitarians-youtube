# BUILD-LOG — five-steps-one-answer

Physics Engine series, 3 of 17. Built 2026-10-31.

## Order of work

1. Read `engine/pipeline.py`, `parse.py`, `formula_kb.py`, `models.py` at `2dc4aa4`;
   picked golden-set MECH-001 as the one worked problem (video 11 owns Atwood).
2. Counted cards from the code, not the docs: 8 + 8 + 9 + 6 = 31; six whose
   `solves_for` includes `v` or `s`. Arithmetic hand-checked (30, 180, 900 ÷ 5).
3. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes in `PhysicsEngine03.tsx`.
4. GATE P: standing approval from Param Madan in chat for the series → Kokoro
   `af_bella` audio, 222.7 s; transcribed with faster-whisper to check it.
5. Preview stills of all 9 scenes before the 4K render; one fix (below).
6. Rendered at `--scale=2` (3840×2160); frames checked at p≈0.5 and p≈0.93;
   `./art final` → 4K master.

## What broke, and the fix

- **"One half" heard as "1.5".** B05 rephrased to "half of acceleration, times time
  squared"; regenerated.
- **Sentence break after "A.I."** B07 "for any A.I. answer. Ask…" was voiced as
  "any AI. Answer, ask…". Rephrased to "Whenever an A.I. model gives you an answer,
  ask…"; regenerated.
- **Label collision.** B03's "Electricity & magnetism" group label ran into
  "Waves" in the preview still → shortened to "Electricity & mag.".
- **Docs vs code.** `engine/README.md` still calls Parse a placeholder; `parse.py`
  at the same commit implements it. The video follows the code.
- **Project code not executed** (auto-mode permission check); results are
  repo-reported or hand-checked.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
