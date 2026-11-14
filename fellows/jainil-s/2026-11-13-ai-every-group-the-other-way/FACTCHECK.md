# FACTCHECK — Every Group Went The Other Way

Week ending 2026-11-13 · `ai-` track.

Two kinds of evidence, kept separate on purpose.

**REAL DATA.** The six largest departments of the UC Berkeley 1973 graduate
admissions table — Bickel, Hammel & O'Connell, *Science* 187(4175), 1975; the
same table distributed as `UCBAdmissions` in R. Published, verifiable, and not
constructed here. Every Berkeley figure on screen is **derived from the
published counts** by `simpson_evidence.py`, never transcribed as a
percentage, so a rate cannot drift from the count it comes from.

**SIMULATION.** A seeded synthetic check of the one thing the real table
cannot answer: whether a reversal needs a confounder at all. Its numbers are
deliberately **not** quoted on screen — see the cut list.

---

## Verified — on screen or spoken

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Berkeley 1973, six largest departments | ✅ | `BERKELEY` table, counts from Bickel et al. |
| 2 | Aggregate: men **44.5%**, women **30.4%** | ✅ | 1198/2691 and 557/1835, computed |
| 3 | The gap is **14.2 points** toward men; spoken as "fourteen points" | ✅ | `aggregate.gap_pp` |
| 4 | Women admitted at a higher rate in **4 of 6** departments | ✅ | A, B, D, F — `departments_favouring_women` |
| 5 | Dept A: men 62.1%, women 82.4% | ✅ | 512/825, 89/108 |
| 6 | Dept B: men 63.0%, women 68.0% | ✅ | 353/560, 17/25 |
| 7 | Dept C: men 36.9%, women 34.1% (men lead) | ✅ | 120/325, 202/593 |
| 8 | Dept D: men 33.1%, women 34.9% | ✅ | 138/417, 131/375 |
| 9 | Dept E: men 27.7%, women 23.9% (men lead) | ✅ | 53/191, 94/393 |
| 10 | Dept F: men 5.9%, women 7.0% | ✅ | 22/373, 24/341 |
| 11 | Selectivity: A admits **64.4%**, F admits **6.4%** | ✅ | `shares.overall_rate`; "ten times harder" is 64.4/6.4 ≈ 10.1 |
| 12 | A and B took **51%** of men's applications | ✅ | `easy_share_men` = 0.51 |
| 13 | A and B took **7%** of women's applications | ✅ | `easy_share_women` = 0.07 |
| 14 | **72%** of women's applications went to C, E or F | ✅ | 32.3 + 21.4 + 18.6 = 72.3%. **Corrected — see below** |
| 15 | Standardised: women's own rates, men's application pattern → **51.6%** | ✅ | `standardised_women_rate`; direct standardisation |
| 16 | That is above men's 44.5% — a 14-point deficit becomes a **+7.1** surplus | ✅ | `standardised_vs_men_pp` |
| 17 | B00's spoken figures are the **same six departments** as B02: 44.5% men, 30% women | ✅ | Rescoped during the build — see correction 2 |

## Corrections applied during the build

**1 — An invented percentage in card text.** B04's women card read *"74%
applied to C, E or F."* The data says **72.3%**. I typed 74 from memory; no
source produced it. Corrected to 72%.

The reconciliation pass that rewrites numeric props from
`simpson_results.json` reported every prop matching — and it was right, because
this figure lived inside a **card line**, which is prose. Numbers embedded in
sentences are invisible to that check and have to be read against the source
by hand. Recorded in `PROMPTS.md` so the next reel treats prose figures as a
separate pass.

**2 — Two different "overall" figures, caught before render.** B00 was first
written around the famous headline numbers for the *whole* 1973 applicant pool
(~44% of men, ~35% of women), while every other beat analyses the six largest
departments (44.5% and 30.4%). Both figures are correct and they describe
**different populations** — but a reel arguing that people misread aggregates
cannot itself put two different aggregates on the viewer without flagging it.

Rather than add a caveat, B00 was rescoped to the six-department figures so the
whole reel speaks about one population throughout. B02's total row is labelled
**"All six"** rather than "overall" for the same reason. The famous
full-pool numbers appear nowhere in the reel.

## Claims considered and cut

- **Any verbatim quote from Bickel et al.** The paper's conclusion about
  earlier educational screening is paraphrased and attributed, never quoted on
  screen. I could not retrieve the full text to verify exact wording, and
  VERBATIM QUOTE LAW requires an exact match. A paraphrase with attribution is
  honest; an approximate quotation is not.
- **"There was no bias at Berkeley."** Not claimed, and B06 argues against
  reading the reel that way. What the department-level data supports is
  narrower: the aggregate gap is accounted for by where people applied. The
  authors themselves pointed upstream, at what shaped those application
  patterns. The reel's landing is that disaggregation **relocated** the
  question rather than closing it.
- **The simulation's numbers** (reversal rate against routing imbalance:
  ~0.6% at zero imbalance, ~99.6% at 20%). Measured and shipped in
  `simpson_evidence.py`, but not spoken or shown. The reel states the
  qualitative fact it establishes — a reversal requires a confounder
  correlated with both the grouping and the outcome — and does not quote a
  synthetic figure next to real data where a viewer might take it as part of
  the Berkeley result.
- **Any lawsuit.** A commonly repeated claim that Berkeley was sued over these
  admissions could not be verified; one secondary source says it is
  overstated. Cut entirely rather than hedged.
- **Modern re-examinations of the dataset.** Out of scope for a 2:30 reel and
  would need their own sourcing.

## Scope

Six departments of one university in one year. The reel uses them to
demonstrate a general arithmetic phenomenon, not to characterise admissions
anywhere else or at any other time.
