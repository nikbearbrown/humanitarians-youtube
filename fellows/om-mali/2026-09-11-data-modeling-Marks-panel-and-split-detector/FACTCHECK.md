# Fact-check gate — building-the-marks-panel-and-the-split-detector (week 7)

Every number spoken or shown was checked against `figdata_week7.json`, which
`scripts/make_week7_figures.py` in the project repo queries from the marks panel at build
time and dumps before anything is drawn. **Rows 9, 12, 18 and 20 are the ones to read before
signing.**

Verdict types, as in weeks 1, 2, 4, 5 and 6:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read the numbers.
- `REPRODUCIBLE` — re-run the committed query/script against the project database.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | 5,806 filed holdings go into the panel | B02/B09 | REPRODUCIBLE | `figdata.coverage.holdings` = **5806** — the same population week 6 decided. Asserted at injection. |
| 2 | 28 were rejected last month as belonging to nothing | B02/B09 | REPRODUCIBLE | `figdata.coverage.rejected_not_in_universe` = **28**. This is week 6's canary — 28 holdings of a similarly-named business — carried forward, not re-litigated here. |
| 3 | 72 sit on filings a later amendment replaced | B02/B09 | REPRODUCIBLE | `figdata.coverage.superseded_by_amendment` = **72**. |
| 4 | The remaining 5,706 aggregate into marks, and it reconciles exactly | B02/B09 | REPRODUCIBLE | 5806 − 28 − 72 = **5706** = `coverage.lines_in_marks`, and `coverage.reconciles` is `true`. The injection asserts the arithmetic rather than trusting the flag, and B02 performs the subtraction on screen. |
| 5 | 5,479 marks — one fund's price for one security at one period end | B00/B01/B02/B09 | REPRODUCIBLE | `figdata.totals.marks` = **5479**, across `securities` 232, `periods` 55, `companies` 10. A mark is **not** a valuation of the company; it is what one fund wrote down. |
| 6 | 5,185 priced · 301 blocked, and the block reasons sum | B02 | REPRODUCIBLE | `totals.priced` 5185, `totals.blocked` 301; `blocks[]` sums to 301 (230 + 58 + 7 + 6). Asserted. Note 5185 + 301 ≠ 5479 by exactly 7 — see row 7. |
| 7 | 7 marks are priced but blocked from every change series, awaiting Week 8 | B02/B07/B09 | REPRODUCIBLE | The `confirmed split, awaiting adjustment (Week 8)` block holds **7** marks, matching `sum(quarantine[].blocked)` = 7. Those 7 carry a price but are held out of the change series, which is why priced + unpriceable (294) = 5479 while blocked reads 301. Both identities asserted. |
| 8 | The rule that ships is a RELATIVE 1% window | B00/B04/B09 | REPRODUCIBLE | `figdata.tolerance` = **0.01**, asserted. Imported by both the detector and week 6's review queue. |
| 9 | **The OLD window was ±0.02 absolute — and that number is NOT in figdata** | B00/B04/B09 | AUTHOR-ASSERTED — **read this one** | `figdata_week7.json` carries only the tolerance that ships. The previous window comes from `narration_script.md` and `plan.md`. It is passed into the build as a named constant `OLD_WINDOW`, and B04's on-screen source line says so rather than citing a file that does not contain it. Everything else on that beat is measured. |
| 10 | Perplexity: $695.04 → $58.26, a ratio of 11.93 | B03/B04/B07/B09 | EXTERNALLY VERIFIABLE | `figdata.quarantine`, the `COM:UNSPECIFIED` row — **ARK's common line**, 2026-01-30 → 2026-04-30. `ratio_min` = `ratio_max` = **11.9300**, asserted. |
| 11 | Read naively that is a 92% collapse | B03 | REPRODUCIBLE | Derived at injection from the two filed prices: 1 − 58.2595/695.0374 = **91.6%**, spoken and shown as 92%. Never typed. |
| 12 | **11.93 sits 0.07 from 12.00, and the old window missed it by a factor of three** | B04/B09 | REPRODUCIBLE (the gap) + AUTHOR-ASSERTED (the window) — **read this one** | The gap, 12.00 − 11.93 = **0.07**, is derived from the measured ratio. The *factor of three* is 0.07 ÷ 0.02, and the 0.02 is row 9's script-sourced number. Under the new rule the window at 12 is 0.12, which contains 0.07 — also derived. If the old window was not 0.02, this ratio changes and the beat would need re-cutting. |
| 13 | It looked correct only because the other Perplexity step landed on exactly 10 | B04 | REPRODUCIBLE | `quarantine`, the `PFD:E-1` and `PFD:D-1` rows: `ratio_min` = `ratio_max` = **10.0000**, which sits inside any window centred on a whole number. That is why an absolute ±0.02 rule passed its own smoke test. |
| 14 | Perplexity's share count went 19,395 → 193,950 | B05/B09 | EXTERNALLY VERIFIABLE | `figdata.perplexity`, the last two period ends. The injection asserts the second is exactly ten times the first. **This is the T. Rowe PREFERRED line (ratio 10.0000) — a different security from the 11.93 common line in rows 10–12**, and B04 and B05 both name their class on screen so the two are not conflated. |
| 15 | …while the filed value did not move: $13,488,132.50 at both period ends | B05/B09 | EXTERNALLY VERIFIABLE | `perplexity[*].value_usd`, identical **to the cent**, asserted — including an assertion that the value still carries decimals. The README records this being rounded to $4,228,994-style whole dollars while the caption said "the same dollars", so the rounding was doing part of the argument. |
| 16 | Anthropic held 89,078 shares in all 13 quarters; the step reverses | B06/B09 | REPRODUCIBLE | `figdata.anthropic`: one distinct `shares` value across **13** rows, asserted. The suspected step is $12.18 → $48.94 (×4.02) and the next quarter is $30.00 — a fall, which a split never produces. Also asserted. |
| 17 | SpaceX: constant 22,368 shares, value exactly doubled | B06/B09 | REPRODUCIBLE | `figdata.spacex`: one distinct `shares` value; $4,742,016.00 → $9,484,032.00 is exactly ×2, asserted; the series continues to $526.59 rather than reverting. |
| 18 | **All 7 quarantined series were adjudicated by a named person with a written reason** | B01/B06/B09 | REPRODUCIBLE (the records) + AUTHOR-ASSERTED (the requirement) — **read this one** | Every `quarantine[]` row has `adjudicated: true` and a `note` containing "Om Mali"; both asserted. That the *code requires* a name and a reason is a claim about the author's implementation, carried over from week 6 — the data shows the records exist, not that they were compulsory. Three companies, two verdicts (3 `split`, 4 `not_a_split`). |
| 19 | 11.93 = a 10-for-1 split AND a 16% markdown in the same quarter | B07/B09 | REPRODUCIBLE | `quarantine` stores `ratio_min/max` (11.9300) and `factor` (10.0000) as **separate fields**; the injection asserts they differ. The markdown is derived: 1 − 58.2595 ÷ (695.0374 ÷ 10) = **16.2%**. Dividing by 11.93 would erase it. |
| 20 | **7 checks: 6 pass, 1 unreachable, 0 fail — and 10 manager families agree where 4 were expected** | B08/B09 | REPRODUCIBLE — **read this one** | `figdata.checks` has 7 entries; the counts are **computed at injection** (`passed is True` / `False` / `None`), never typed — the README records the figure's title hardcoding "0 fail" and disagreeing with its own table. The unreachable check carries its reason and the injection asserts that it does. On the agreement: `figdata.agreement.families` = **10**, but in **two clusters** — 8 at $259.1364 and 2 at $259.1400, 0.0036 apart. "Ten agree" is true **at the cent**; the reel says so rather than implying exact equality. |

## What this cut deliberately does NOT claim

- **The detector was not broken.** It was too narrow. It caught the step at exactly 10.0000 and
  missed the one at 11.93 — which is the case `plan.md` itself names. The word "broken" is not
  in the narration.
- **The splits are not adjusted.** They are detected, quarantined and decided. Applying the
  factor is Week 8, and the 7 Perplexity marks stay blocked from every change series until then.
- **A mark is not a valuation.** This project publishes what funds wrote down, and nothing more.
- **An unreachable check is not a pass.** Row 20. It reports why it cannot run.
- **The ten managers do not agree exactly.** Row 20. Two clusters, four thousandths apart.
- **No claim about how often marks move** — that is next week, and the reel says so rather than
  gesturing at it.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "Three looked like splits" | "Three companies threw one" | The data holds **7 quarantined series** across **3 companies**. "Three" is a company count; saying so stops it being read as three series and contradicting the 7 on screen at B02. |
| The evidence beat and the tolerance beat both say "Perplexity" without distinguishing | each beat names its **security class** on screen | They are two different securities: the 11.93 is ARK's common line, the ×10 share evidence is T. Rowe's preferred line. The script glides between them; the frames do not. |
| "Ten do." | "Ten do, in two clusters four thousandths of a dollar apart." | True as written, but it implies exact agreement. The clusters are in the data and are a more interesting fact than the round number. |
| "That window misses it by a factor of three" | same, with the arithmetic on screen | Spoken alone it is an assertion. The frame shows the 0.07 gap measured against the 0.02 window, so the factor is visible rather than claimed. |

## Before publishing

Rows 9, 12, 18 and 20 are the four a reviewer is most likely to challenge. Row 9 is the only
number in the reel that no committed artifact backs — if the old window was not ±0.02, row 12's
"factor of three" changes with it and B04 needs re-cutting. Rows 18 and 20 are places where the
honest statement is narrower than the flattering one. Everything else traces to
`figdata_week7.json` under an assertion. Publishing remains a separate, explicitly authorized
step.
