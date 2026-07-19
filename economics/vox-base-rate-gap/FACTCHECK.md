# FACTCHECK — vox-base-rate-gap
## The Base Rate Problem: Why 0.68 Is Not 68%

Source chapter: `the-reallocation-engine/chapters/05-verifying-the-data.md`

---

## Claims table

| Beat | Claim | Verdict | Source / Derivation | Fix |
|------|-------|---------|---------------------|-----|
| B01 | Score comes back 0.68 | ✓ | Chapter 5, worked example: "The Sponsorship Scorer returns 0.68" | — |
| B01 | Actual probability closer to 40 | ✓ (minor) | Chapter 5: "posterior approximately 0.38–0.45 depending on assumptions" — 40% is within range | Narration says "closer to 40" not "exactly 40" — acceptable |
| B02 | Cambridge biotech | ✓ | Chapter 5: "Take a mid-sized Cambridge biotech" | — |
| B02 | 12 LCA filings over three years | ✓ | Chapter 5: "twelve LCA filings over three years" | — |
| B02 | 80% H-1B approval rate | ✓ | Chapter 5: "80% H-1B approval rate" | — |
| B02 | Score 0.68 | ✓ | Chapter 5: "The Sponsorship Scorer returns 0.68" | — |
| B03 | 12 filings, 80% approval, 0.68 score | ✓ | Chapter 5 worked example verbatim | — |
| B04 | 0.68 means closer to 0.40 | ✓ | Chapter 5: "posterior approximately 0.38–0.45" — 0.40 within range | — |
| B05 | Pharmaceutical/medicine manufacturing SIC code | ✓ | Chapter 5: "In this SIC code (pharmaceutical and medicine manufacturing)" | — |
| B05 | Only 8% of employers have ever filed an LCA | ✓ | Chapter 5: "the three-year LCA filing rate among employers in the DOL's universe is approximately 8%" | — |
| B05 | Nine out of ten never sponsor | ✓ | Derivation: if 8% file, then 92% never file; "nine out of ten" = 92% rounds to ~90%. Chapter says "92%". Narration says "nine out of ten" as a rounding. | Minor: exact figure is 92% (chapter). "Nine out of ten" is a slight understatement. Acceptable simplification for narration. |
| B06 | Prior is 8% before any signal | ✓ | Chapter 5: "Working through the Bayes update: prior 0.08" | — |
| B06 | Most companies here are not sponsors | ✓ | 92% never filed — correct | — |
| B07 | Score 0.68 working in right direction | ✓ | Chapter 5: the signal is real (12 filings, 80% approval) | — |
| B07 | Prior is 8 not 50 | ✓ | Chapter 5: prior 0.08 (8%) | — |
| B08 | Correction lands around 40% | ✓ | Chapter 5: "posterior approximately 0.38–0.45" — 40% is within range | — |
| B08 | Raw score overstates by 50 to 75 percent | ✓ | Chapter 5: "The 0.68 overstates the posterior probability by somewhere between 50% and 75%." Verbatim. | — |
| B09 | 92% of employers never sponsor | ✓ | Chapter 5: SIC base rate 8%, so 92% never filed | — |
| B10 | 0.68 didn't know it was working against a 0.08 prior | ✓ | Chapter 5: "The math is Bayes' theorem, and it produces a result that consistently surprises people" — captures the mechanism | — |
| B11 | 1,000 companies in this SIC code — illustrative | ILLUSTRATIVE | Card content: "Example seed: Imagine 1,000 companies in this SIC code" | Labeled illustrative in narration context; not a real data claim |
| B11 | 80 have ever filed an LCA — illustrative | ILLUSTRATIVE | Derived: 1,000 × 0.08 = 80. Consistent with chapter's 8% base rate. | Illustrative derivation from chapter's real 8% figure |
| B12 | Scorer flags 100 as likely sponsors — illustrative | ILLUSTRATIVE | Card content example seed verbatim | Labeled illustrative |
| B12 | 80% precision → 64 genuine, 36 false positives — illustrative | ILLUSTRATIVE | Card content: "Even at 80% precision, only 64 are genuine — and the remaining 36 are false positives." Verbatim from card. | Labeled illustrative |
| B13 | 0.68 means closer to 0.40 | ✓ | Chapter 5: posterior 0.38–0.45 | — |
| B13 | Base rate pulls it back | ✓ | Chapter 5: "Working through the Bayes update: prior 0.08...posterior approximately 0.38–0.45" | — |

---

## Terms table

| Term | Debut beat | Earlier beat creating need |
|------|-----------|--------------------------|
| LCA (Labor Condition Application) | B02 | B01 (score, filing context) |
| SIC code | B05 | B02–B03 (company context established) |
| Prior / base rate | B06 | B05 (8% filing rate = the prior) |
| Sponsorship score / 0.68 | B01 | — (hook, opens film) |
| Posterior | B08 | B07 (mechanism of signal + prior combined) |
| False positives | B12 | B11 (1,000 companies example, 100 flags) |

---

## Exclusion audit

- **No Bayes theorem formula on screen:** confirmed. No formula appears anywhere. Mechanism carried by axis visual and counts.
- **No odds-form calculation:** confirmed. No odds ratios appear.
- **No calibration curve detail:** confirmed. Calibration curve not mentioned.
- **No four diagnostic questions as a list:** confirmed. Only the base-rate question is illustrated; the other three (calibration, cost distribution, freshness) are not named or listed.
- **Illustrative numbers labeled:** B11 and B12 are the example act. Numbers (1,000 / 80 / 100 / 64 / 36) are from the card's example seed and are illustrative — not claimed as real data. They are consistent with the chapter's real 8% base rate figure.

---

## Editorial simplifications

- "Nine out of ten never sponsor" (B05): chapter says 92%. "Nine out of ten" = 90%. Minor simplification for narration rhythm. Not a factual error.
- "Around 40 percent" (B08): chapter says 0.38–0.45. 40% is a reasonable single-number summary. The narration uses "around" and "closer to" throughout.
- "50 to 75 percent overstatement" (B08): verbatim from chapter.

---

## Verdict

All factual claims trace to the source chapter. Illustrative numbers are from the card's example seed, are internally consistent with the real 8% base rate, and will be understood as illustrative in the example act. No exclusion is violated.
