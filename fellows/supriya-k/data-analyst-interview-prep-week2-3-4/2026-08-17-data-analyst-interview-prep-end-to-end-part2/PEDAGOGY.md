# PEDAGOGY — The SQL Interview Bug Even a Correct-Looking Query Can Hide (hai cli-explainer) — v2

GATE P review of the **v2 narration** (2026-10-16). v1 passed GATE P on 2026-07-24
(signature in git history). v2 changes every beat, so it needs a fresh signature before
any audio is generated.

## Why v2 exists
- PM rules (2026-10-01): exact intro, "Supriya" on every beat, real 4K bitrate, and a
  full-length 9:16 that fills every frame. v1 measured 234.9s; v2 targets ~157s (450 words),
  so with the 4.5s endcard the vertical stays full-length under the 180s cap, with margin.
- Fidelity: the receipt is now a real SQLite run (`sql/`). The v1 screen showed a wrong
  GROUP BY total, B07 over-simplified the diff, and B10 paraphrased its prompt (see
  `FACTCHECK.md`, "v2 corrections").

## Branding / identity
- B00 opens "Hi, I am Supriya and this video is about a SQL interview bug that even a
  correct-looking query can hide." ✓ The "for Humanitarians AI" wording is gone from the
  open and outro. "Supriya" is primary on screen; `@HumanitariansAI` stays small. ✓

## Spine check (cli-explainer)
- INTRO B00 → PROBLEM B01–B02 → cycle 1 (CLI B03 → CODE B04 → OUTPUT B05) → cycle 2
  revision (CLI B06 → CODE B07 → better OUTPUT B08) → SUMMARY B09 → HANDOFF B10 → OUTRO B11. ✓
- The 9:16 keeps both cycles (no beats cut; the revision is the fix itself), as in
  correlation-is-not-causation.
- HANDOFF LAW: the prompt is read aloud verbatim, then discussed ("test the fix yourself on a
  real tie"); that line also carries the HAI "verify the AI" spine. ✓

## What changed for the viewer
- Lost: the names Jon/Priya/Maya (now user ids, matching the screen); "top product per city";
  the v1 closer "Check the case the happy path skips"; some re-statement in B05 and B09.
- Kept: the trap, top-N stakes, why a window function, both build cycles, the four-rows-
  for-three-users failure, the ROW_NUMBER + tiebreaker fix, and the lesson.

## For your review
1. [x] The v2 script in `NARRATION-SCRIPT.md` reads naturally aloud (~157s est.).
2. [x] The corrections and cuts above are acceptable.
3. [x] The YOUR TURN prompt and its spoken discussion are what you want.

**VERDICT: PASS**

Signed: Supriya Kushwaha (human, author)  Date: 2026-10-16  Evidence: "PASS" given in chat on the v2 script, with one requested edit applied: B10's on-screen prompt drops the "[paste it]" cue so it reads identically spoken and on screen; the paste instruction moved into the spoken discussion ("Paste your query under it, then test the fix yourself on a real tie.").

## Addendum — length trim after audio (2026-10-16)

Measured audio was 175.57s (Kokoro reads "101" as "one hundred and one"), about 2s over the
173.5s narration budget for a full-length 9:16 with the endcard. Supriya chose to trim ~15 words:

- B01: "Top-N per group is one of the most common SQL interview patterns: top track per user, top order per customer." → "Top-N per group, like top track per user, is one of the most common SQL interview patterns."
- B03: drop "In an interview you'd narrate that plan as you type."

Only B01 and B03 audio is regenerated. Estimated new total: see the build log.

**ADDENDUM VERDICT: PASS**

Signed: Supriya Kushwaha (human, author)  Date: 2026-10-16  Evidence: "PASS" given in chat on the two edits as presented.
