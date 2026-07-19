# FACTCHECK — vox-comma-orphan

Source of truth: `books/the-reallocation-engine/chapters/05-verifying-the-data.md`
(the "Worked example: one company end to end," §133–150, and the chapter thesis §9).
Every narration line, viz count, and card string checked below. Verdicts:
✓ holds · minor (editorial/simplification, defended) · WRONG (must fix before render).

No claim in this film depends on the base-rate / Bayes material (0.68 → 0.38, the 8%
SIC prior) — that content is deliberately excluded (candidate 05), so it is out of scope
here and not asserted anywhere.

| # | Claim (beat) | Verdict | Source / derivation | Note |
|---|---|---|---|---|
| 1 | The missingness check / audit reports **zero missing values** (B01, B02, B09) | ✓ | §143: "the dataset's missingness check reported zero missing values — because the rows are present, just in separate buckets that don't join." | Load-bearing fact of the whole film. |
| 2 | To that check, "missing" = an **empty cell / blank**; it scans **down each column** and finds none (B03, B09) | ✓ (minor) | Standard definition of a column-wise null/missingness check; consistent with §143 (rows present ⇒ nothing reads as missing). | Editorial phrasing of a standard data-quality check; accurate to this example. |
| 3 | Two datasets: **DOL LCA filings** joined to **USCIS H-1B approvals**, joined **on employer/company name** (B04) | ✓ | §24, §37, §56, §117: LCA disclosure data joined to USCIS approval records; §141 the join matches on employer name. | "Labor Department filings" = DOL LCA; "immigration approvals" = USCIS H-1B approvals — lay simplifications, defended below. |
| 4 | The join makes a company's records **line up across both sides** when names match (B05) | ✓ | §26, §141 — grouping/matching by employer name is the join mechanism. | — |
| 5 | One company, **twelve filings over three years** (B06, B08) | ✓ | §139: "twelve LCA filings over three years." | Exact. |
| 6 | The name was typed two ways: **ten "BioTechCo LLC" + two "BioTechCo, LLC"** (comma) (B06) | ✓ | §141: "'BioTechCo LLC' (ten rows) and 'BioTechCo, LLC' (two rows — note the comma)." | Exact, verbatim. 10 + 2 = 12 ✓. |
| 7 | The join **normalized case but not punctuation**, so the 2 comma rows **did not join** (B07) | ✓ | §141: "The join script normalized case but did not strip punctuation. The two rows filed under 'BioTechCo, LLC' did not join to the USCIS data." | Exact. USCIS side is "BIOTECHCO LLC" (all caps, no comma), §141. |
| 8 | The count then reads **ten, not twelve**; the approval rate is on the **wrong denominator** (B08) | ✓ | §141: "They appear in the LCA count but not in the approval count. The approval rate calculation is therefore based on ten LCA filings, not twelve." | No approval-rate number is printed (kept out — Bayes-adjacent). |
| 9 | **Every record is correct; the total is not** — "not a data error" (B08) | ✓ | §143: "The gap is not a data error. Both records are correct. The join is the fragmentation point." | — |
| 10 | The gap **lives between the tables, in the join**; no within-table check can see it (B10) | ✓ | §9: "A name-matching gap can exclude an entire corporate family … without leaving any evidence the missingness check can see." §143. | The film's thesis; directly stated in the chapter. |
| 11 | "Zero missing doesn't mean nothing's missing — nothing's missing **where you looked**." (B11) | ✓ (minor) | Faithful restatement of §9 + §143. | Editorial closing epigram; asserts nothing beyond the chapter. |
| 12 | Card title: "Why a dataset with zero missing values can still be missing your data" (B01) | ✓ | Candidate 04 card title, `vids/video-ideas.md` §49. | — |
| 13 | Endcard attribution: "from The Reallocation Engine — chapter 5" (B11) | ✓ | Source chapter is `05-verifying-the-data.md`. | — |

## Simplifications, labeled (defended)

- **"Labor Department filings" / "immigration approvals"** (B04): the precise terms are
  *DOL Labor Condition Application (LCA) disclosure data* and *USCIS H-1B petition
  approval records*. Shortened for a general audience; the shortening changes nothing
  about the mechanism (two agencies' datasets, joined on employer name). Defended.
- **"orphan bucket" / "a bucket that never joins"** (B07, B08): the chapter says the two
  rows "did not join … appear in the LCA count but not in the approval count." The
  "orphan bucket" is the candidate card's own visual object (§54: "two rows deflected
  into an orphan bucket by a giant comma"). Visual metaphor for "unmatched rows,"
  faithful to the source. Defended.
- **"the gate"** (B05–B10): editorial name for the name-matching/join step. No claim
  rides on the metaphor.

## Numbers appearing on screen (viz)

- B06 / B07 / B08 counts: **10 navy + 2 crimson = 12** — verbatim from §141. ✓
- No percentage, probability, base rate, or approval-rate figure is printed anywhere
  (the film's exclusion list forbids the Bayes material). Confirmed against beat_sheet.json.

**Verdict: all claims hold.** Two minor editorial epigrams (B03, B11) and three labeled
simplifications, each defended above. No WRONG claims. Cleared to render.
