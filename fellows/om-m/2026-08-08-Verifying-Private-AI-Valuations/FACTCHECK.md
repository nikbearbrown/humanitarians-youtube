# Fact-check gate

Status: **ALL 20 ROWS CLEARED.** Rows 6, 15, and 20 were resolved directly by the author during
the 2026-08-08 build session (see below). Rows 1-5, 7-14, and 16-19 were confirmed by the author
(Om Mali) against the underlying filings and scripts on 2026-08-08.

## Resolved during the 2026-08-08 build session

- **Row 15** — narration corrected from "about five hundred times" to "about six hundred times"
  in `beat_sheet.json`, matching the real ~606x ratio. Audio regenerated to match.
- **Row 6** — kept "Identical, to the cent" as written, by author decision; defensible since all
  four figures round to $259.14 even though full precision differs ($259.14 vs $259.1364).
- **Row 20** — author confirmed the B00 personal-intro narration (and the rest of the cut) to
  proceed as written.

## Why this file looks different from the other Om Mali fact-checks

The previous reports in this folder describe a private n8n workflow and Postgres database, so
every claim was `AUTHOR-ASSERTED` and unverifiable by anyone else. **This week is the opposite.**
Almost every number spoken here comes from public SEC filings with published accession numbers,
or from a public bulk data file anyone can download and re-query. That makes most of this cut
independently checkable, which is unusual and worth stating plainly.

Three verdict types are used:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read the numbers.
- `REPRODUCIBLE` — download the same public file and re-run the query; the script is committed.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, or decision.

| # | Claim | Beat | Verdict | Note |
|---|---|---|---|---|
| 1 | Nineteen Anthropic positions were read by hand from six fund families | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Confirm the count is 19 and not 16. An earlier draft said 16; the fixture was also corrected mid-session when three positions turned out to belong to accession `0000035402-26-003406`, not `...-003312`. Recount against `tests/fixtures/week1_verified_marks.json`. |
| 2 | Fidelity priced Anthropic at $259.14 | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Accessions `0000035402-26-003299`, `-003310`, `-003312`, `-003406`, period 2026-03-31. |
| 3 | T. Rowe Price priced it the same | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Accession `0001099263-26-006576`. **Actual figure is $259.1364, not $259.14.** |
| 4 | Alger priced it the same | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Accessions `0000940400-26-025773`, `-025787`, period 2026-04-30. **Actual figure is $259.1364.** |
| 5 | ARK priced it the same | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Accession `0000940400-26-025087`. Exactly $259.14. |
| 6 | **"Identical, to the cent"** | B02 | RESOLVED — KEPT AS WRITTEN | True only after rounding. Fidelity and ARK carry $259.14 exactly; T. Rowe and Alger carry $259.1364. Author decided 2026-08-08 to keep the line as written since all four round to $259.14. |
| 7 | BlackRock marked $589.0095 on 2026-05-29 | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Accession `0000940400-26-028432`. |
| 8 | Capital Group marked $589.0095 on 2026-05-31 | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Accession `0001193125-26-323082`. Note `plan.md` claimed these two differed ($589.01 vs $589.00); they do not. |
| 9 | "Matching to four decimal places, two days apart" | B02 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Both figures are 589.0095. Dates are 29 and 31 May, so "two days apart" is correct. |
| 10 | The plan's filter dropped five of six managers | B03 | CONFIRMED (was REPRODUCIBLE) | `python scripts/verify_week1_marks.py` prints the filter comparison. Confirm it still reports 1 manager kept. |
| 11 | Funds write "N/A" or nine zeros for a missing identifier | B03 | CONFIRMED (was EXTERNALLY VERIFIABLE) | Visible in the raw `primary_doc.xml` of the accessions above. |
| 12 | Two funds flag restricted stock as unrestricted | B03 | CONFIRMED (was EXTERNALLY VERIFIABLE) | ARK and Capital Group report `isRestrictedSec = N` on Anthropic preferred. Confirm this is still the case in the live filings. |
| 13 | The plan expected "a few thousand" rows per quarter | B03 | CONFIRMED (was AUTHOR-ASSERTED) | `plan.md` line 401 says "a few thousand out". Confirm the line is unchanged. |
| 14 | The real number was 606,028 rows per quarter | B03 | CONFIRMED (was REPRODUCIBLE) | `python scripts/check_bulk_vs_xml.py data/2026q2_nport`, section Q2. Requires the 2026 Q2 bulk zip (440.7 MB, public). |
| 15 | **"Shrank the hardest part by about six hundred times"** | B03 | RESOLVED — CORRECTED & CONFIRMED | 606,028 ÷ ~1,000 is roughly 606x. Narration corrected from "five hundred" to "six hundred" and audio regenerated, 2026-08-08. The ~1,000 figure itself confirmed by the author. |
| 16 | The bulk data matched the hand-read filings 15 out of 15 | B04 | CONFIRMED (was REPRODUCIBLE) | `check_bulk_vs_xml.py` section Q1 prints "exact matches ... 15 mismatches: 0". Note this covers the 15 rows whose accessions appear in 2026 Q2; BlackRock and Capital Group filed in Q3 and are not in this comparison. |
| 17 | Universe v1 is frozen at six companies | B04 | CONFIRMED (was AUTHOR-ASSERTED) | The author cleared this gate on 2026-08-08. Recorded in `universe_v1.json`. |
| 18 | SpaceX was added; it was not in the original plan | B04 | CONFIRMED (was AUTHOR-ASSERTED) | Confirm against `plan.md`'s universe table, which lists Databricks, Anthropic, X.AI, Anduril, OpenAI, Figure AI, Cohere, Perplexity, Groq, Scale AI. |
| 19 | Every Cohere match was Coherent Corp, a public optics company | B04 | CONFIRMED (was REPRODUCIBLE) | 1,094 rows across three spellings, zero at Level 3. Confirm Coherent Corp's business description is fairly summarized as "optics" for a lay audience. |
| 20 | Personal framing: "Hi, I'm Om Mali" and the video's stated scope | B00 | RESOLVED — AUTHOR CONFIRMED | Author confirmed 2026-08-08 to proceed with the narration as written (personal intro, dash-free style, B00/B01 restructuring). |

## What's already checked

`PEDAGOGY.md` confirms act order, cold-open structure, utility-framing lint, and an honesty
audit — all PASS, cut marked **VERDICT: PASS** as of 2026-08-08.

The three pantry figures passed the Mycroft repo's deterministic layout audit with zero flags.
That checks geometry, not truth — but rows 1-20 above now cover the truth too.

## Before publishing

All 20 rows are confirmed as of 2026-08-08 (Om Mali). The video (`verifying-private-ai-valuations.mp4`,
3840x2160, 112.7s) is fact-check-clear. Publishing itself is still a separate, explicit
authorization — this file clears the content, not the act of publishing.

## Known artifact problem

The SVG sources for the three pantry figures were generated in the Mycroft repo at
`images/private-ai-valuation-agent/` and **are no longer present in that working tree.** They
were not committed, and they were not found in the repo's `archive/`. The cause is not
established. The PNGs in `pantry/` are intact and are currently the only copies of these
figures. Regenerate the SVG sources inside `data/raw/Private_AI_Valuation_Agent/` before
attempting any edit to a figure.
