# Week 32 work video

*Step Two Was the Last One I Built.* Tanmay Kulkarni, for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The contribution

**[nikbearbrown/mycroft#94](https://github.com/nikbearbrown/mycroft/pull/94)**, merged 2026-11-23 as `fef5caa` (one commit from the fork branch `Tanmay-Kulk/mycroft` @ `portfolio-price-fetcher-ingest-inputs`): the Portfolio Price Fetcher recipe, step 2 (ingest declared inputs, sample mode), the step that was written last.

- **Step 2** reads the run settings, the declared workflow and each price file; checks each file against the SHA-256 frozen in a manifest; keeps each file exactly as it came; rejects a file that is unlisted, changed, missing or not JSON; and does not judge whether a price makes sense (that stays with steps 3 and 4).
- **Evidence:** 19 files added, 0 edited, 0 removed; a self-test of 28 checks with break tests; outputs byte-identical on rerun; the same files as step 3 sees in all six sample sets.

## The angle

**A stand-in for an unbuilt step is a loan: when the real step arrives, ask what it stood in for, what it skipped, and what happens when both get the same wrong input.** Two sentences in the recipe ("since step 2 is still open", "since step 4 is still open") were true when written. Run on one deliberately wrong file (two digits switched, on a scratch copy), step 1 stops, step 3 on its own passes it, and step 5 prices the portfolio 1,800.00 higher (24.35% against 21.00%); the new step 2 turns the file away on a hash mismatch.

## The files

| | Film | Format | Audio |
|---|---|---|---|
| **Long** | Step Two Was the Last One I Built | 3840x2160 · 30 fps · 4:26 (266.3 s) | -14.7 LUFS, true peak -1.9 dBTP |
| **Short** | Step Two Was the Last One I Built (Short) | 2160x3840 · 30 fps · 1:43 (103.3 s) | -14.6 LUFS, true peak -1.9 dBTP |

Narration is Kokoro `am_onyx` (`beat_sheet.json` records the voice). Visuals are original code-drawn animations; the type is Arial and Menlo (macOS system fonts). Every figure on screen comes from a rerun of our own recipe's scripts, not typed.

**Structure:**
- **Long, "ONE ROW, TWO STAND-INS":** the six-step row tagged with when each step was built; the three-question check is voiced and shown in B01 and carried through the film; all six sample sets, then one wrong file down the old route and through the new step; the film ends on the viewer's own check and the line "a stand-in is a loan".
- **Short, one persistent scene:** a six-step column stays on screen; stand-ins, the wrong file, the old route, the new door, the limits and the viewer's task; the last frame returns to the first.

## How it was checked

| | Long | Short |
|---|---|---|
| Rubric | teaching rubric /12 + production gate | Shorts rubric /12 + measured compiled-file gate |
| Result | 12/12, every measured check passes (`PROOF-REVIEW.md`) | 12/12, every measured check passes (`PROOF-REVIEW.md`) |
| Gate P (narration read aloud) | signed 2026-11-23, two logged amendments (`PEDAGOGY.md`) | signed 2026-11-23 |
| Numbers | each figure traced to a rerun of our own scripts in `FACTCHECK.md` | same |

## Records in this folder

`ANGLE.md` (the contribution as the basis for the film, the uniqueness audit, the approved angle), `READ-ALOUD.md` and `READ-ALOUD-SHORT.md` (the signed narration), `beat_sheet.json` and `beat_sheet-short.json` (narration, picture plan and measured timing per beat), `FACTCHECK.md`, `PEDAGOGY.md`, `FRICTIONAL.md` (drafted after the fact, reviewed by Tanmay), `PROOF-REVIEW.md`. Also here: `step-two-was-the-last-one-i-built-youtube.md` and `step-two-was-the-last-one-i-built-short-youtube.md` (the YouTube descriptions), and `step-two-was-the-last-one-i-built(.srt/.vtt)` and `step-two-was-the-last-one-i-built-short(.srt/.vtt)` (captions, timed to the measured audio).

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
