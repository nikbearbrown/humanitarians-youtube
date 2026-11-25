# Week 31 work video

*What Draft Is Waiting For: Reading a Status as a Claim.* Tanmay Kulkarni, in for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The contribution

**[nikbearbrown/mycroft#90](https://github.com/nikbearbrown/mycroft/pull/90)**, merged 2026-11-17 as `894be6c` (one commit from the fork branch `Tanmay-Kulk/mycroft` @ `portfolio-price-fetcher-quality-check-and-report`): the Portfolio Price Fetcher recipe, steps 4 (transform and quality check) and 6 (produce human report), in sample mode. **50 files, all added, none modified, removed or renamed** (the rule this week: add files, edit none). It builds on [#64](https://github.com/nikbearbrown/mycroft/pull/64) (steps 1, 3 and 5 of the same recipe).

- **Step 4** looks across a set of prices: two records for one ticker (identical ones collapse; ones that differ are both rejected, since a person decides which is right), a holding with no price, a price taken from the previous close, a day move over 15%, a price over 3x or under a third of the buy price. The three numeric lines are labelled "ours, a judgment".
- **Step 6** writes the report (the recipe's fifteen sections) and the agent log (its sixteen fields) from what steps 1, 3, 4 and 5 leave behind, judges the stop conditions from evidence, and only ever recommends a sample-mode next phase.
- **Evidence:** four invented fixture sets, sample outputs for each, and a self-test of 24 checks with break tests on both scripts and a "did not test" list.

## The angle

**A status word is a claim, and each rung of a status ladder asks for a different piece of evidence: ask which rung, then ask to see the evidence.** The film climbs the repository's five-rung ladder (draft, specified, runnable on sample data, runnable live, verified) with real records: the stress-test recipe against rung one's written test, the contradiction detector's six gate records (what each covers, the risk left, what voids it, and the version they name against the version the recipe is now), and this week's self-test with its "did not test" section. It ends with three questions to ask of any "it works" and a task for the viewer's own project. The angle passed a uniqueness audit against all thirteen earlier work videos (`ANGLE.md`).

## The files

| | Film | Format | Audio |
|---|---|---|---|
| **Long** | What Draft Is Waiting For: Reading a Status as a Claim | 3840x2160 · 30 fps · 3:42 (222.4 s) | -14.8 LUFS, true peak -2.2 dBTP |
| **Short** | What Draft Is Waiting For: Reading a Status as a Claim (Short) | 2160x3840 · 30 fps · 2:06 (125.8 s) | -14.5 LUFS, true peak -1.9 dBTP |

Narration is Kokoro `am_onyx` (`beat_sheet.json` records the voice). Visuals are original code-drawn animations; the type is Arial and Menlo (macOS system fonts). Every fact on screen is read from the merged repository, not typed.

**Structure:**
- **Long, "ONE LADDER, FIVE MARKERS":** the ladder is on screen from B02 and markers arrive as each recipe is named; one rung is climbed with real evidence, the record is shown to age (the friction beat), and the film ends on three questions.
- **Short, one persistent scene:** three plain questions over an empty ladder, then what a recipe is, the ladder, what each rung asks, the records, the record that ages, what was not tested, and the three questions; every term is defined before it carries evidence; the last frame returns to the first, so it loops, and it ends on the long film's exact title.

## How it was checked

| | Long | Short |
|---|---|---|
| Rubric | teaching rubric /12 + production gate | Shorts rubric /12 + measured compiled-file gate |
| Result | 12/12, every measured check passes (`PROOF-REVIEW.md`) | 12/12, every measured check passes (`PROOF-REVIEW.md`) |
| Gate P (narration read aloud) | signed 2026-11-17 (`PEDAGOGY.md`) | signed 2026-11-17 (`PEDAGOGY.md`) |
| Numbers | each figure traced to a committed file or the repository's own command in `FACTCHECK.md` (26 of 26) | same |

## Records in this folder

`ANGLE.md` (the contribution as the basis for the film, the uniqueness audit, the approved angle), `READ-ALOUD.md` and `READ-ALOUD-SHORT.md` (the signed narration), `beat_sheet.json` and `beat_sheet-short.json` (narration, picture plan and measured timing per beat), `FACTCHECK.md`, `PEDAGOGY.md`, `FRICTIONAL.md`, `PROOF-REVIEW.md`.

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
