# Fact-check gate — bulk-ingestion-at-scale (week 2)

Status: **20 of 20 rows traced to a primary source.** Every number spoken or shown was checked
against `figdata_week2.json` (which the Mycroft repo queries directly from the built Parquet —
no figure number is typed by hand) or against `docs/worklog.md` in that repo. **Row 16 is the
one row that needed derivation rather than a direct quote — read it before signing.**

Verdict types, same as week 1:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read the numbers.
- `REPRODUCIBLE` — re-run the committed query/script against the public data.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | 14 quarters of SEC bulk data, 2023Q1–2026Q2, about 6 GB | B00/B02 | REPRODUCIBLE | worklog: "Downloaded 14 quarters, 2023Q1–2026Q2 (**5.9 GB**)". Narration says "about six gigabytes" — a rounding of 5.9, not a new figure. |
| 2 | 80,571,213 source holding rows | B00/B01/B02 | REPRODUCIBLE | worklog: "80,571,213 source → 22,041,937 private → 5,806 universe". `figdata.funnel.source`. |
| 3 | 22,041,937 private positions | B02 | REPRODUCIBLE | Same line. `figdata.funnel.private`. |
| 4 | 5,806 name-matched marks | B00/B02 | REPRODUCIBLE | Same line. `figdata.funnel.universe`. Also "5,806 raw_holdings" loaded. |
| 5 | Every stage reconciles against the stage above it | B02 | REPRODUCIBLE | worklog: "14 of 14 quarters reconcile exactly at every boundary". |
| 6 | The 5,806 are 7 universe v1 companies + 4 watchlisted | B02 (on-screen gloss) | REPRODUCIBLE | worklog flags this as a figure defect already corrected: the stage previously read "7 AI companies", relabelled because the rows include xAI, Perplexity, Groq and Cohere. The corrected label is carried here verbatim. |
| 7 | Anthropic: 33 observation dates | B00/B03 | REPRODUCIBLE | `figdata.anthropic` has exactly 33 entries (counted programmatically, not by eye). worklog: "33 period ends". |
| 8 | From about $12/share in 2023 to over $300 this April | B03 | REPRODUCIBLE | First entry 2023-04-28 = **$11.79**; last 2026-04-30 = **$333.60**. worklog: "$11.79 →". Both labels on screen are the exact figures. |
| 9 | The series is a staircase — marks move only on a repricing | B03 | REPRODUCIBLE (shape), INTERPRETIVE (cause) | The flat-then-jump shape is visible in `figdata.anthropic` and the beat draws the real points. The *causal* reading (a mark moves when a funding round reprices it) is the project's stated core assumption; worklog: "the propagation-lag claim rests on this and it now has evidence across the full panel." Narration frames it as what the data now shows, not as proof. |
| 10 | 7 completely independent fund managers agree at $259.14 | B04 | REPRODUCIBLE | `figdata.convergence`: date 2026-03-31, families 7 — BlackRock, Capital Group, Coatue, Fidelity, JPMorgan, New York Life, T. Rowe Price. All seven are named on screen. |
| 11 | 24 registrations collapse to 7 decision-makers | B04 | REPRODUCIBLE | `figdata.convergence.ciks` = 24. worklog records "25 managers agree" as a **caught figure defect** — counting CIKs would have overstated independence. The corrected framing is used here. |
| 12 | The $589.0095 mark verified by hand in week 1 is not in the bulk data | B05 | REPRODUCIBLE | worklog: "The $589.0095 Anthropic repricing hand-verified in Week 1 is not in the bulk data at all", pinned by `test_bulk_cannot_reach_the_589_repricing`. |
| 13 | The archive is keyed to filing date; funds file ~8 weeks late | B05 | REPRODUCIBLE | worklog: "filings lag their period by **~56 days**… the as-of window runs roughly two months behind". 56 days = 8 weeks exactly. |
| 14 | The 2026 Q2 archive reaches only 30 Apr 2026 | B05 | REPRODUCIBLE | worklog: "…is **2026-04-30**, not 2026-06-30". `figdata.per_quarter` 2026q2 `latest` = 2026-04-30. |
| 15 | Variable Insurance Products Fund I–IV are Fidelity (CIKs 356494 / 831016 / 927384 / 720318) | B06 | EXTERNALLY VERIFIABLE | worklog names all four CIKs. All four appear on screen exactly as listed. |
| 16 | **"My code counted one manager as five"** | B06 | CONFIRMED BY DERIVATION — **read this one** | The worklog's own headline says the VIP funds "counted as **four** independent managers", which reads like a contradiction. It is not: Fidelity's main registrations were already mapped to one family (15 CIKs), and the four unmapped VIP CIKs appeared as four *additional* families. One real manager therefore presented as 1 + 4 = **5**. The fix moves Fidelity from 15 CIKs to 19. The narration's "five" is correct, but it is derived rather than quoted — confirm the derivation before publishing. |
| 17 | SpaceX: common (EC) at $112.00, preferred (EP) at $1,120.00, one filing | B07 | EXTERNALLY VERIFIABLE | `figdata.spacex_filing`: EC px 112.0 (2 rows), EP px 1120.0 (4 rows). Accession 0001752724-24-195357, Baron Focused Growth Fund, 2024-06-30. All six rows shown on screen are the real shares/value/price triples. |
| 18 | "Exactly ten times apart" | B07 | REPRODUCIBLE | 112.00 × 10 = 1,120.00, and every value/balance pair in the fixture divides to exactly those two prices. |
| 19 | 309 cases, and no other company shows it | B07 | REPRODUCIBLE | worklog: "**309 of 624 SpaceX fund/period groups show a ratio of exactly 10.000, and no other**…". Narration says "three hundred and nine cases… across the panel"; the on-screen footer carries the full "309 of 624". |
| 20 | 33 tests passing / 14 quarters loaded | B08 (verdict card) | REPRODUCIBLE | worklog: "**33 tests**" passing after the downloader work. Loaded: "183 funds, 1,512 filings, 5,806 raw_holdings". |

## What this cut deliberately does NOT claim

- **No valuation of any company.** The narration says these are marks funds *report*, never what a
  company is worth. The script's own note — "Don't oversell the price history" — is honoured.
- **No trading claim.** The lag beat (B05) actively argues the opposite: the data cannot reach
  anything recent.
- **The two figures the script pairs are split** (staircase / archive-lag, and the two traps), so
  no beat carries a second idea. No claim was added or dropped in the split.

## Rounding, and why each one is safe

| Spoken | On screen | Why |
|---|---|---|
| "about six gigabytes" | — | 5.9 GB |
| "eighty and a half million" | 80,571,213 | script's own instruction: exact figure on screen, rounded in voice |
| "twenty-two million" | 22,041,937 | same |
| "fifty-eight hundred" | 5,806 | same |
| "about twelve dollars" | $11.79 | same |
| "over three hundred" | $333.60 | same |
| "eleven twenty" | $1,120.00 | script's own spoken form |
| "about eight weeks" | ~56 days | 56 days = 8 weeks exactly |

## Before publishing

Row 16 is the only row that is derived rather than quoted, and it is the row a reviewer is most
likely to challenge. Everything else traces to a committed script, a public archive, or a named
accession. Publishing remains a separate, explicitly authorized step — this file clears the
content, not the act of publishing.
