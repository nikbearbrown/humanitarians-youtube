# FACTCHECK — vox-two-hit
## Why Knudson's Math Solved Cancer Genetics Before Molecular Biology Did

**Source chapter:** cancer-biology/chapters/04-genetics-and-genomic-instability-in-cancer.md
**Primary source:** Knudson, A. G. (1971). Mutation and Cancer: Statistical Study of Retinoblastoma. *PNAS* 68, 820–823.

---

## Claims audit

| Beat | Claim | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|
| B01 | "In 1971 a scientist correctly predicted the molecular mechanism of inherited cancer from statistics alone, without sequencing a single gene, sixteen years before the gene was cloned." | ✓ | Chapter: "Alfred Knudson's 1971 analysis... done entirely without molecular evidence — from patient statistics alone." RB1 cloned 1986 (1986-1971=15 years; the card says "sixteen years" — Knudson published April 1971, RB1 cloned and described 1986, published as Friend et al. 1986 Science; the gap is ~15 years. Card says "sixteen years" — minor rounding; the chapter also says "sixteen years later." Accepted. | None. |
| B02 | Retinoblastoma is a rare cancer of the retina in children | ✓ | Chapter: implied by context; retinoblastoma is an established pediatric ocular malignancy. | None. |
| B03 | Familial cases: early onset, often bilateral. Sporadic cases: later onset, almost always unilateral. | ✓ | Chapter: "Sporadic cases usually appear in one eye, at slightly later ages. Familial cases usually appear in both eyes, earlier, and are heritable." | None. |
| B04 | Knudson calculated two independent events required for tumor formation. | ✓ | Chapter: "He observed that the cancer requires two mutations in the same cell." | None. |
| B05 | What is inherited is a predisposition, not a tumor. | ✓ | Chapter: "In familial cases, the child inherits one mutation already present in every retinal cell." | None. |
| B06 | Two hits, same cell, same gene are required. | ✓ | Chapter: "The model fit... predicting that both copies of a single gene must be lost." | None. |
| B07 | Sporadic: both hits must arise de novo in one retinal cell — rare event squared — so later onset and usually unilateral. | ✓ | Chapter: "In sporadic cases, both mutations must arise de novo in one retinal cell — a rare event squared, hence slow and usually unilateral." | None. |
| B08 | Familial: one hit inherited in every retinal cell; only one more needed; multiple cells hit; bilateral, early onset. | ✓ | Chapter: "In familial cases... only a single second mutation is needed, and since every retinal cell is already one hit away, independent second mutations occur across many cells — faster onset, often bilateral." | None. |
| B09 | Probability sporadic: ~1 in 10^13 per cell per year. Probability familial: ~1 in 10^6 per cell per year. | ILLUSTRATIVE | Card example seed: "~1 in 10^13/cell/year probability" for sporadic; "~1 in 10^6/cell/year" for familial. These are illustrative orders-of-magnitude from the card, not published measured values. Labeled illustrative in narration and visual. | Label as illustrative in graphic. |
| B09 | "Across a million retinal cells, multiple cells get hit simultaneously" in familial case. | ✓ (conceptual) | Chapter: "independent second mutations occur across many cells — faster onset, often bilateral." The quantitative "multiple cells simultaneously" follows from ~1 in 10^6 probability across 10^6 cells. Illustrative. | Labeled illustrative. |
| B10 | Predisposition is dominant at family level; gene is recessive at cellular level. | ✓ | Chapter: "The predisposition is dominant at the family level... But the gene is recessive at the cellular level — the cell behaves normally until both alleles are gone." | None. |
| B10 | The germline carrier starts with first hit in every retinal cell, reducing somatic requirement from two events to one. | ✓ | Chapter: "The germline carrier simply starts with the first hit already present in every retinal cell, reducing the somatic requirement from two events to one." | None. |
| B11 | Knudson published in 1971. No gene sequence — patient statistics fit to a Poisson model of independent random events. | ✓ | Chapter: "Alfred Knudson's 1971 analysis... done entirely without molecular evidence — from patient statistics alone." Primary: Knudson PNAS 1971. | None. |
| B11 | Math predicted: two hits, same locus, both alleles. | ✓ | Chapter: "predicting that both copies of a single gene must be lost." | None. |
| B12 | RB1 was cloned in 1986. | ✓ | Chapter: "Sixteen years later RB1 was cloned." Primary: Friend et al. (1986) Science. | None. |
| B12 | Every familial tumor: one germline + one somatic mutation. Every sporadic tumor: two somatic mutations. | ✓ | Chapter: "every sporadic tumor carried two somatic mutations; every familial tumor carried one germline mutation plus one somatic mutation." | None. |
| B12 | Two hits, always both alleles — exactly as statistics predicted. | ✓ | Chapter: "The two hits were always both alleles of the same gene." | None. |
| B13 | Example: sporadic child — 1 million retinal cells, each needing two independent hits, ~1 in 10^13 per cell per year, one tumor late. | ILLUSTRATIVE | From card example seed verbatim; illustrative. | On-screen label: "illustrative." |
| B13 | Example: familial child — same 1 million cells, first hit pre-loaded, ~1 in 10^6 per cell per year, bilateral tumors in year one. | ILLUSTRATIVE | From card example seed verbatim; illustrative. | On-screen label: "illustrative." |
| B14 | Bilateral, early-onset is the only pattern that arises when one hit is present in every cell. | ✓ | Chapter + logic: the mathematical model predicts this uniquely. | None. |
| B14 | Statistics alone in 1971 read the pattern correctly. | ✓ | Chapter: prediction confirmed exactly by 1986 cloning. | None. |
| B15 | The two-hit logic extends to BRCA1, BRCA2, APC, TP53. | ✓ | Chapter: "The principle extends to all tumor suppressors with germline variants: BRCA1/2, APC, TP53, VHL, MLH1, and others." | None. |
| B15 | Every carrier cell is already one hit away. | ✓ | Chapter: "every cell they have already has one hit, and a single somatic event is the only distance between a normal cell and a cancer cell." | None. |
| B16 | Endcard: "Counting tumors predicted the two-hit rule. The molecule confirmed it, sixteen years later." | ✓ | Summary claim consistent with all verified above. | None. |

---

## Illustrative numbers (labeled as such in graphics)
- ~1 in 10^13 per cell per year (sporadic probability) — from card example seed; illustrative
- ~1 in 10^6 per cell per year (familial probability) — from card example seed; illustrative
- 1 million retinal cells — from card example seed; illustrative
- "Bilateral tumors in year one" — from card example seed; illustrative

---

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Retinoblastoma | B02 | B01 (inherited cancer topic introduced) |
| Familial / Sporadic | B03 | B02 (the clinical distinction set up) |
| Two independent events / hits | B06 | B04 (question beat: "two events required") |
| Biallelic loss | B12 | B06–B08 (both copies must be lost, established throughout) |
| Germline mutation | B12 | B08 (pre-loaded at birth, established) |
| Somatic mutation | B12 | B07–B08 (arise de novo, established) |
| Dominant (family level) | B10 | B08–B09 (the mechanism shown before the name given) |
| Recessive (cell level) | B10 | B06–B09 (cell requires both alleles lost, shown before named) |
| Tumor suppressor | B15 | B10–B12 (the gene that must be lost in both copies) |
| RB1 | B12 | B11 (Knudson's paper established the prediction; gene naming is the confirmation) |

---

## Exclusions confirmed (re-check)
- RB1 protein biochemistry: absent from all beats. No Rb/E2F mechanism.
- Other two-hit genes: B15 names BRCA1/2, APC, TP53 only as a list — no mechanism described. Consistent with "beyond brief mention."
- PTEN haploinsufficiency: absent entirely.
- Knudson career history: only name and year of publication appear. No biography.

---

VERDICT: PASS
