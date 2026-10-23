# CHECKS-REPORT — measuring-how-private-marks-move-and-propagate

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW). |
| B01 | SHOW | Claim: four questions, four answers against expectation. Four rows land in sequence, each carrying the measured answer beside the expectation it beat, then the measured population rules off beneath. The reel's whole shape is legible in ten seconds. |
| B02 | SHOW | Claim: 25% is a result, not a threshold choice. The plan's band draws as a grey span, the measured value lands visibly outside and below it, and three widened definitions then CLIMB toward the band and stop short. The argument is the gap, and the gap is drawn. |
| B03 | SHOW | Claim: the headline describes nobody. Ten bars grow in rank order with their own step counts, then the panel-wide rate is drawn as a vertical rule ACROSS them — passing near almost none. The uselessness is visible rather than asserted. |
| B04 | SHOW | Claim: different prices on the same date are normal. 130 spreads fill a field as one dot per group, the median line drops through them, the groups above the measured p90 light, and the counts resolve. |
| B05 | SHOW | Claim: some of that spread is a round arriving. Eleven real marks land across two period-end columns, the old and new levels band, and the managers present at both ends are joined so the crossing is a drawn motion. |
| B06 | SHOW | Claim: a new level reaches half its holders in a median of 30 days. 37 lags fill a 0–92 day axis; the 15 zero-day events stack visibly at the origin, which is the distribution's shape and not a number. |
| B07 | SHOW | Claim: the lag is bounded, and one earlier claim did not survive. Two bound cards land, then the old caption sets and is struck through, then two evidence rows show the arithmetic that removed it — 27 vs 30 days, 3/9 vs 12/28. |
| B08 | SHOW | Claim: every statistic ran behind a guard. The panel total sets, two exclusions subtract in sequence, three zero counters land, and the reel closes on three things none of it shows. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B04's
  below-p90 dots at 0.62 and B05's mid-crossing marks in `SOFT`
- Comparisons shown side-by-side, held ≥2s ✓ — B02's band against the measured mark, B03's
  ten bars against the panel rule, B05's two period-end columns, B06's median against the
  zero stack and B07's two evidence rows all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01 — the four questions, each with the expectation it was tested against,
                 before any of them is answered in detail
WORKED EXAMPLE ✓ B05 — one real window, 8 managers and 11 marks, followed mark by mark; it
                 exists to stop B04 being over-read
FALSIFIABILITY ✓ B02 pre-registers the way the finding could be wrong (a threshold artifact)
                 and then tests it three ways;
                 B07 shows a caption the author wrote, checked, and deleted, with the
                 arithmetic that killed it;
                 B08 closes on what none of the measurement shows
SCAFFOLDED TASK ✓ B10 — split a metric you report as one number by its obvious dimension and
                 ask whether the headline still describes anything
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected by build_beat_sheet.py from
                 figdata_week8.json; the injection ASSERTS the population reconciliation
                 (5,479 − 301 = 5,178 = 4,079 steps + 1,099 first observations), the 25.0%
                 share, that ALL THREE widenings stay under the plan's band and increase
                 monotonically, the by-company floor and ceiling, the 130/92 same-date
                 counts, the measured p90, the window's 8-manager 11-mark count and its
                 clustered levels, the 37 events with their median and zero-day count, and
                 that the smaller propagation events reach the same period end MORE often —
                 and fails the build otherwise
```

**0 violations.** Three authoring judgment calls are logged in `BUILD-LOG.md` rather than
passed silently: the seven script sections split into eight body beats, speaking Groq's 0.0%
floor where the script said OpenAI's 1%, and narrowing "disagreement" to "different prices on
the same date".

## Two figures that are computed here rather than drawn from a constant

The README records both as defects in the original drawing code, and both are handled by
deriving the value at injection rather than by correcting a number:

- **The window's levels** come from single-linkage clustering at the findings module's own
  2% relative gap, not from `price > 220`. That is what surfaces the two managers sitting
  *between* the old and new levels — a binary threshold would have put them on one side and
  erased the beat's argument.
- **The dispersion highlight** is the measured p90, not `spread >= 0.4`. It currently lands at
  40.5%, near the old constant, which is exactly why a hard-coded version could survive
  unnoticed.

## What this cut is asked NOT to do, and does not

| The README says | This cut |
|---|---|
| **25% is a disagreement with the plan, not a bug** | B02 draws the plan's band and the measured value as two marks on one axis, and shows three widenings failing to reach it. The word "bug" is not in the narration. |
| **Same-date spread is not automatically disagreement** | B04's narration says "different prices on the same date", and B05 is a whole beat devoted to the alternative reading. |
| **Every number sits behind a guard** | B08 performs the exclusion on screen and closes the reel on limits rather than findings. |
| Red is the primary series, never a warning | Terracotta marks the measured result throughout — the 25%, the X.AI bar, the above-p90 groups, the new price level, the zero-day events. It never marks a hazard. |
