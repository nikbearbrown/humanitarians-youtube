# Fact-check gate — measuring-how-private-marks-move-and-propagate (week 8)

Every number spoken or shown was checked against `figdata_week8.json`, which
`scripts/make_week8_figures.py` in the project repo queries from the marks panel at build
time and dumps before anything is drawn. **Rows 6, 9, 18 and 20 are the ones to read before
signing.**

Verdict types, as in weeks 1, 2, 4, 5, 6 and 7:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read the numbers.
- `REPRODUCIBLE` — re-run the committed query/script against the project database.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | 5,479 marks in the panel | B00/B08/B09 | REPRODUCIBLE | `figdata.guards.marks` = **5479** — week 7's output, carried forward unchanged. Asserted. |
| 2 | 294 unpriced and 301 split-blocked marks are excluded before any statistic | B08/B09 | REPRODUCIBLE | `guards.unpriced` = 294, `guards.change_blocked` = 301. The 301 are week 7's blocked series; the exclusion happens before counting, not after. |
| 3 | No unadjudicated split, no incomplete run, no statistic over one | B08/B09 | REPRODUCIBLE | `guards.unadjudicated_splits` = `guards.incomplete_runs` = `guards.on_incomplete_runs` = **0**. The first two are asserted; a non-zero value fails the build. |
| 4 | 5,178 marks measured — and the population reconciles | B01/B08/B09 | REPRODUCIBLE | `remark.overall.marks` = 5178 = 5479 − 301, and `steps` 4079 + `first_observation` 1099 = 5178. Both identities asserted, so a figure cannot quietly measure a different population than it claims. |
| 5 | 25.0% of 4,079 consecutive observations carried forward unchanged | B00/B02/B09 | REPRODUCIBLE | `remark.overall`: unchanged **1019**, steps **4079**, share **0.2498**. `moved + unchanged == steps` asserted. |
| 6 | **The plan expected 30–40%** | B02/B09 | AUTHOR-ASSERTED (recorded) — **read this one** | `remark.plan_expectation` = "30-40% of consecutive observations unchanged". The string is in the figure data, so the *expectation* is on record rather than remembered — but it is the author's own prior, not a measurement. The entire framing of B02 ("a disagreement with the plan, not a bug") rests on it. |
| 7 | Widening "unchanged" three ways still stays under the band | B02/B09 | REPRODUCIBLE | `remark.sensitivity`: exact **0.2498**, within 0.1% **0.2631**, within 1% **0.2962**. The injection asserts all three are below 0.30 **and** that they increase monotonically — if any widening reached the band, the finding would be a threshold artifact and the build would fail rather than ship it. |
| 8 | The company split covers every step | B03 | REPRODUCIBLE | `remark.by_company` — 10 rows whose `steps` sum to 4079, asserted. Nothing is dropped between the headline and the breakdown. |
| 9 | **The same statistic runs 0.0% to 48.5% by company** | B00/B03/B09/B10 | REPRODUCIBLE — **read this one** | `by_company`: the floor is **Groq at 0.0%** and the ceiling **X.AI at 48.5%**, both asserted. The narration script said "from one percent unchanged for OpenAI"; OpenAI is 1.1% and is the lowest *meaningful* sample, but Groq's 0.0% is the true floor and is on the chart. The reel says zero and shows every bar's step count, because saying 1% while displaying a 0% bar would be a visible mismatch. |
| 10 | Anthropic and OpenAI are repriced at nearly every observation | B03 | REPRODUCIBLE | `by_company`: Anthropic 2.2% unchanged over 271 steps, OpenAI 1.1% over 95. |
| 11 | X.AI and SpaceX are carried forward a third to a half of the time | B03 | REPRODUCIBLE | X.AI 48.5% over 171 steps, SpaceX 37.4% over 1,259. |
| 12 | Sample sizes span two orders of magnitude | B03 | REPRODUCIBLE | **10** steps (Perplexity) to **1,812** (Databricks) — the smallest sample is Perplexity's, not Groq's 11. Every bar carries its own n on screen, so a 0.0% built on 11 steps cannot be read as equivalent to a 19.8% built on 1,812. |
| 13 | 130 same-date groups | B01/B04/B09 | REPRODUCIBLE | `same_date_stats.groups` = **130**, and `same_date.steady` (38) + `same_date.transition` (92) = 130, asserted. |
| 14 | Median same-date spread is 10.8% | B00/B01/B04/B09 | REPRODUCIBLE | `same_date_stats.median` = **0.1082**, asserted. Max is 111.9%. |
| 15 | 92 of 130 groups hold more than one distinct price level | B01/B04/B09 | REPRODUCIBLE | `same_date_stats.multi_level` = 92 = `len(same_date.transition)`, asserted. 35 of 130 agree to within 1%; the 38 steady groups have a median spread of 0.0%. |
| 16 | The dispersion highlight is the measured 90th percentile | B04 | REPRODUCIBLE | `same_date_stats.p90` = **0.405**, asserted against a literal. The README records the highlight being hard-coded at `spread >= 0.4`; it now marks whatever the measured p90 is, which happens to land near the old constant. |
| 17 | The window: Anthropic preferred, 8 managers, 11 marks, $140.97 → $261.57 | B05/B09 | EXTERNALLY VERIFIABLE | `figdata.window` — 11 rows, 8 distinct managers, 2 distinct period ends. The counts are **counted at injection**, asserted; the README records a subtitle hard-coding "Nine managers". |
| 18 | **The window's levels are clustered, not thresholded** | B05 | REPRODUCIBLE — **read this one** | The old figure split the dots at `price > 220`. The reel runs single-linkage at `same_date.level_rel` (2% relative gap) — the same rule the findings module uses — giving **four** levels: 2 marks near $141 (the old level), singletons at $203.36 and $243.40, and 7 marks from $250.91 to $261.57 (the new level). The two singletons are managers mid-crossing, which is the beat's actual point and which a binary threshold would have erased. |
| 19 | 37 levels adopted by 3+ managers: median 30 days to half, 15 at zero, slowest 92 | B00/B01/B06/B09 | REPRODUCIBLE | `propagation`: `events_counted` 37, `median_lag_to_half_days` 30, `max_lag_to_half_days` 92. The median and max are re-derived from `events[].lag_to_half_days` and asserted to match the stored summary; the 15 zero-day events are counted, not quoted. Median to ALL holders is 90 days with a tail to 427 — reported as the weaker number and labelled as such. |
| 20 | **"The biggest events are the fastest" was checked and removed** | B07 | REPRODUCIBLE — **read this one** | Computed at injection: 9 events with 10+ managers have a median of **27** days to half against **30** for the other 28 — a 3-day gap on 9 events — while the *smaller* events reach the same period end more often, **12/28 against 3/9**. The injection asserts that second inequality, so the removed claim cannot creep back. The README records this as a caption the drawing code made and the data did not support. |

## What this cut deliberately does NOT claim

- **These are fund marks, not transactions.** Nobody traded at these prices. B08 says it on
  screen, in the report's own words.
- **A same-date spread is not automatically a disagreement about value.** Some of it is a round
  arriving that some managers have booked and others have not. B05 exists to show one window
  where both readings are visible at once, and the narration says "different prices on the same
  date", not "managers disagree".
- **A propagation lag is observability, not diligence.** The reporting calendar sets the floor:
  across 55 period ends the panel sees only 5 distinct days of the month, so a manager filing on
  the 30th cannot reflect a 31st repricing any sooner. B07.
- **The biggest events are not shown to be fastest.** Row 20.
- **25% is not presented as a bug.** It is a disagreement with a recorded prior, and it survives
  every widening tried. Row 7.
- **No claim about why any manager holds the price it holds.** The panel sees filings, not
  valuation committees.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "from one percent unchanged for OpenAI to forty eight percent" | "from zero for Groq to forty-eight percent for X dot A I" | Row 9. Groq's 0.0% is the true floor and appears on the chart; saying "one percent" over a visible 0% bar is a mismatch a viewer can see. Every bar carries its step count so the 11-step sample is not mistaken for a strong one. |
| "the median spread … is just under eleven percent … Disagreement is the normal state" | "…Different prices on the same date is the normal state" | The README's own warning: same-date spread is not automatically disagreement about value. The claim is narrowed to what the measurement supports, and B05 then shows why. |
| "eight managers, eleven marks" *(figure said nine managers)* | same, counted | Row 17. The counts are derived from the plotted rows rather than written into a subtitle. |
| "the biggest events are the fastest" *(earlier caption)* | removed, and the arithmetic that removed it is on screen | Row 20. The beat shows 27 vs 30 days and 3/9 vs 12/28 rather than asserting the correction. |

## Before publishing

Rows 6, 9, 18 and 20 are the four a reviewer is most likely to challenge. Row 6 is the only
load-bearing number that is a prior rather than a measurement — if the plan did not say 30–40%,
B02's framing goes with it. Rows 9 and 18 are places where the frames are more precise than the
script. Row 20 is a claim the author made and then disproved against his own data. Everything
else traces to `figdata_week8.json` under an assertion. Publishing remains a separate,
explicitly authorized step.
