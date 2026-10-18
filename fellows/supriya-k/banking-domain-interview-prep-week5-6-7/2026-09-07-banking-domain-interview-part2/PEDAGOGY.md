# PEDAGOGY — The Running-Balance Bug Hiding in a Correct-Looking SQL Query — v3

GATE P review of the **v3 narration** (2026-10-16, branch `banking-reels-v3`). v1 passed GATE P
earlier (baseline commit 516aeb8). v3 changes every beat, so it needs a fresh signature before
any audio is generated.

## Why v3 exists
- PM rules: exact intro, "Supriya" on every beat, real 4K bitrate, and a full-length 9:16 that
  fills every frame. v1 measured 167.7s; v3 targets ~156s (424 words), so the 9:16 stays full-
  length with its endcard under the 180s cap.
- Fact-check (2026-10-16): v1 explained the wrong mechanism (a WHERE "in an earlier CTE"; the
  bug's WHERE is in the same CTE as SUM() OVER), presented hand-typed numbers as query runs, and
  paraphrased its handoff prompt. All corrected; see `FACTCHECK.md`, "v3 corrections".
- The receipt is a real SQLite run of the shown MySQL, with DATE_FORMAT → strftime disclosed
  (Supriya chose option b, 2026-10-16).

## Spine check (cli-explainer)
INTRO B00 → PROBLEM B01–B02 → cycle 1 (CLI B03 → CODE B04 → OUTPUT B05) → revision (CLI B06 →
CODE B07 → OUTPUT B08) → SUMMARY B09 → HANDOFF B10 (read verbatim, then discussed) → OUTRO B11. ✓
Both cycles stay in the 9:16 (the revision is the fix).

## What changed for the viewer
- Lost: v1's outro sign-off ("building it with Claude, then taking it apart"), and some
  repetition in B01 and B06.
- Gained: the book's own diagnosis in B05 ("not a balance — the net change since January").

## For your review
1. [x] The v3 script in `NARRATION-SCRIPT.md` reads naturally aloud (~156s est.).
2. [x] The corrections above are acceptable.
3. [x] The YOUR TURN prompt and its spoken discussion are what you want.

**VERDICT: PASS**

Signed: Supriya Kushwaha (human, author)  Date: 2026-10-16  Evidence: "PASS" given in chat on the v3 script as presented.
