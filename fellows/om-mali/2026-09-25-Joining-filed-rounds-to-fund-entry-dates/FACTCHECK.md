# Fact-check gate — joining-filed-rounds-to-fund-entry-dates (week 9)

Every number spoken or shown was checked against `figdata_week9.json`, which
`scripts/make_week9_figures.py` in the project repo queries from the database at build time
and dumps before anything is drawn. **Rows 6, 9, 14 and 19 are the ones to read before
signing.**

Verdict types, as in weeks 1–8:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read it.
- `REPRODUCIBLE` — re-run the committed query/script against the project database.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | Two new sources beside N-PORT: Form D and the Reg S-X 12-12 footnote | B00/B01/B09 | REPRODUCIBLE | `form_d` and `ncsr` are separate blocks in the figure data. N-PORT is what weeks 1–8 were built on; it carries a position's value at a month end and never a purchase date. |
| 2 | A name scan over 49 quarters returns 706 rows | B00/B02/B09 | REPRODUCIBLE | `form_d.quarters_scanned` = **49**, `form_d.rows` = **706**, spanning `2014q1`–`2026q1`. Asserted. |
| 3 | 595 of those — 84.3% — are feeder vehicles, not the company | B00/B02/B09 | REPRODUCIBLE | `form_d.by_class`: `pooled_vehicle` **595** rows across 481 filers, `candidate_operating` **111** across 46. The two classes sum to 706, and the 84.3% is derived at injection. All asserted. |
| 4 | "Anthropic Jan 2026 a Series of CGF2021 LLC" is a real feeder name | B02 | EXTERNALLY VERIFIABLE | Named in `README.md` as the worked example. It is a fund raising money to buy Anthropic shares on the secondary market; the amount it reports selling is its own raise. |
| 5 | The Form D archive has a gap, and orphan quarters are deliberately excluded | B02 | REPRODUCIBLE | `form_d.archive_gap` — 2008Q2–2013Q4 are not published by the SEC; 2008Q1 and 2012Q1 exist as orphans and are excluded so the earliest observed filing is a property of a contiguous archive rather than of which orphan a company happened to appear in. Asserted present, and shown on B02 rather than left in the paperwork. |
| 6 | **A 2014 filer normalises to exactly the same string as X.AI and is a different company** | B03/B09 | AUTHOR-ASSERTED — **read this one** | **Not in `figdata_week9.json`.** It comes from `narration_script.md` and the filings behind it, and is passed into the build as a named constant `XAI_COLLISION` with B03's on-screen source line saying so. It is load-bearing: it is the evidence that no better string normalisation would fix the join, which is what justifies a human confirming each identifier. |
| 7 | The scan's own output carries a row labelled FALSE POSITIVE | B03 | REPRODUCIBLE | `form_d.by_company` contains `Cohere Inc. [FALSE POSITIVE]` — 47 vehicles, 24 candidates, 29 filers. It matched by name and is not in the universe. It is left visible in the data rather than quietly dropped, which is the same discipline week 6's canary was recorded with. |
| 8 | 60 filings fetched, 58 with the footnote, 31 with parsed lots, 30 registrants | B01/B09 | REPRODUCIBLE | `ncsr.filings`. Asserted on the filings and with-lots counts. |
| 9 | **Five layouts: four tables with different headings, one with no table, a sixth needing no new code** | B04/B09 | AUTHOR-ASSERTED — **read this one** | **Not in `figdata_week9.json`**, which carries filers and lot counts but no layout taxonomy. Passed as `LAYOUT_COUNT` with B04's source line saying so. What the data *does* support is on the same frame: ten filers carry lots, and exactly one of them reports cost at fund level rather than per position. |
| 10 | 249 positions, 227 with a position cost | B00/B04/B09 | REPRODUCIBLE | `by_filer[]` — lots sum to **249**, `position_cost` to **227**, `fund_cost` to **22**, and 227 + 22 = 249. All asserted, so "227 with a cost" cannot be read as 22 positions having none. |
| 11 | The other 22 are Baron's, reported at fund level | B04 | REPRODUCIBLE | The injection asserts that **exactly one** filer has `fund_cost > 0` and `position_cost == 0`. If a second ever appeared, the build would fail rather than let the beat's sentence go stale. |
| 12 | Entry dates reach back to 2015-01-20 | B00/B05/B09 | EXTERNALLY VERIFIABLE | `entry_vs_mark` — the earliest `first_entry` in the set, SpaceX. Asserted against the literal date. |
| 13 | That is 7.9 years before the panel's first mark for the same company | B05/B09 | REPRODUCIBLE | Derived at injection from `first_entry` 2015-01-20 and `first_mark` 2022-11-30. The script says "nearly eight years"; the figure on screen is the computed 7.9. |
| 14 | **Only 3 of 7 companies genuinely reach back** | B05/B09 | REPRODUCIBLE — **read this one** | Derived: `first_entry < first_mark` holds for SpaceX, Databricks and X.AI only. `README.md` records the source figure being titled as though all seven did, with four negative. The reason is on the frame: only the LATEST annual and semi-annual per registrant were fetched, so older purchases disclosed in older reports are not in view. This is a floor on the record, not the record. |
| 15 | 90 manager–company pairs, 30 managers, 10 companies | B06/B09 | REPRODUCIBLE | `exposure[]` — all three counts asserted. Percentages are each filer's own reported percentage of net assets, not a recomputation. |
| 16 | 10 of 18 acquisition dates land on the exact day an issuer reported a sale | B00/B07/B09 | REPRODUCIBLE | `corroboration`: `dates_in_window` **18**, `hits["0"]` **10**, `share["0"]` **0.5556**. The injection also asserts that the 18 `pairs[]` rows contain exactly 10 with `gap_days == 0`, so the summary and the detail cannot disagree. |
| 17 | Databricks, 2019-10-22: five separate fund managers name the same day | B07/B09 | EXTERNALLY VERIFIABLE | `corroboration.pairs` — that row has `gap_days` 0 and `registrants` **5**. Asserted by company and date rather than by index. |
| 18 | The company filed saying it sold $400M of stock that day | B07 | AUTHOR-ASSERTED | **Not in `figdata_week9.json`.** Passed as `DBX_ROUND_USD` with B07's source line saying so. The *agreement* in row 17 does not depend on it; the amount is context. |
| 19 | **Counted against every acquisition date, 56% reads as 33%** | B08/B09 | REPRODUCIBLE — **read this one** | `corroboration.by_company.dates_outside_window` sums to **12**; 18 + 12 = 30, and 10/30 = **0.3333**, asserted. One company stopped filing Form D in mid-2022, so its later purchases have no round to be near and the distance to the nearest one measures the end of the archive rather than a fund's behaviour. The reel shows both readings side by side rather than choosing one. |
| 20 | Agreement is evidence, not causation | B07/B09 | REPRODUCIBLE (recorded) | `corroboration.caveat`, asserted present: a fund buying on the day an issuer reports a first sale is consistent with participating in that round **and** with a secondary purchase that settled the same day. What it is not is circular — neither filing cites the other. |

## What this cut deliberately does NOT claim

- **No valuation.** Neither source carries shares outstanding, so nothing here divides to a
  company value.
- **No return.** A footnote cost over a later mark is not one, because the share count may have
  changed in between — week 7's split detector blocked 301 marks for exactly that reason.
- **No causation.** Row 20.
- **Not a history of fund entries.** Row 14 — a floor, and the frame says why.
- **No claim about why a manager holds what it holds.** B06 says "concentration, not
  conviction"; a large percentage of net assets is a fact about the fund's size as much as
  about the position.
- **No claim that the name scan is merely noisy.** It is 84% wrong, which is a design input
  rather than a quality note.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "Entry dates reaching back to January twenty fifteen, nearly eight years before its first observation" | same, plus "only three of the seven companies genuinely reach back" | Row 14. The script's line is true of the company it describes and not of the set. The beat shows all seven and accents the three, with the reason. |
| "two hundred and twenty seven with a cost" | same, with the other 22 named on the frame | Row 11. "227 with a cost" invites the reading that 22 have none; they have a fund-level cost instead. |
| "one filer from twenty fourteen normalises to exactly the same string as xAI" | same, attributed on screen as not being in the figure data | Row 6. It is the beat's strongest evidence and the one thing on it that no committed artifact backs. |
| "The company filed saying it sold four hundred million dollars of stock" | same, attributed on screen | Row 18. The agreement stands without the amount; the amount is the only part that is not in the data. |

## Before publishing

Rows 6, 9 and 18 are the three values in this reel that `figdata_week9.json` does not contain.
Each is passed as a named constant and each beat that uses one says so on screen. Row 6 is the
one that matters most: if that collision is not real, B03 loses the evidence that motivates a
human-confirmed join key, and the argument would need rebuilding rather than rewording. Row 14
is where the frames are more careful than the script, and row 19 is where the reel shows how
easily its own headline could be restated. Everything else traces to `figdata_week9.json` under
an assertion. Publishing remains a separate, explicitly authorized step.
