# FACTCHECK — *The Cell Next Door*

Every factual, numerical, and attributional claim the script makes, with its verdict, the
beat that consumes it, and the evidence. Per the source README's fact-check protocol: nothing
is silently repaired, and gaps are marked `[VERIFY: …]` rather than filled by guessing.

**This table exists to be consumed.** The inherited `source/nbb-hot-cold-excluded-tumors/
FACTCHECK.md` is 138 bytes long, has zero claim rows, and ends `VERDICT: PASS` — a gate that
did not run. A `PASS` with nothing under it is the defect this file is written against.

Two evidence bases:

- **Primary literature**, fetched during the research pass — see [`RESEARCH.md`](RESEARCH.md).
  Every PMID below was resolved, not remembered.
- **Our own computation**, [`experiment/tmb_orr_audit.py`](experiment/tmb_orr_audit.py),
  reproducible on a stock `python3` with no dependencies. Saved output:
  [`experiment/RESULTS.txt`](experiment/RESULTS.txt).

Confidence grades: **A** = primary source fetched and the figure read from it this pass;
**B⁺** = the primary source is closed, but the figure is reported consistently by three or
more independent authoritative secondary sources; **B** = primary source fetched, figure
derived or taken from one authoritative secondary summary; **C** = not verified to a primary
text — **may not be spoken.**

---

## Part 1 — C1–C16, the research claim table, as the script uses it

Row **C1a** is a claim the script originally made and no longer does. It is listed rather than
deleted, because a cut claim is evidence about the gate.

| ID | Beat | Claim | Verdict | Evidence / required correction | Conf |
|---|---|---|---|---|---|
| **C1** | B01, B03, B04 | Pembrolizumab 5-year OS in advanced melanoma is 38.7%, not "above 50%"; the fact-check's "~43%" is the first-line subgroup (43.2%) | **SUPPORTED** | Robert 2019, KEYNOTE-006 5-year post-hoc: 834 enrolled, median follow-up 57.7 mo, median OS **32.7 vs 15.9 mo**, HR 0.73, p=0.00049 — all read from the abstract. **Lancet Oncol** 20(9):1239–51, [PMID 31345627](https://pubmed.ncbi.nlm.nih.gov/31345627/). **5-year OS 38.7% vs 31.0%** and **first-line 5-year 43.2% vs 33.0%** are corroborated across three independent ASCO Post reports of the trial (see §4). **Correction applied:** the source cites this to *NEJM*; it is *Lancet Oncology*. On-screen citation must say so. | A (n, follow-up, median OS, HR) / B⁺ (the two OS rates, triple-corroborated) |
| **C1a** | **CUT** | "Above 50%" is specifically the 24-month OS figure (55.2%) | **UNVERIFIED — provenance claim, not a finding** | The 24/36/48-month grid (55.2 / 48.1 / 42.3) appears in only **one** secondary source and in none of the three that agree on the 5-year figures. It is a plausible account of where "above 50%" came from, and plausible is not the standard here. **Correction applied:** B03 no longer asserts it. The beat now says only that "above fifty" is not the five-year row — which C1 establishes outright and which is all the argument requires | **C — cut** |
| **C2** | B05 | Pancreatic checkpoint response is near zero | **SUPPORTED** | O'Reilly 2019: ORR **3.1%** durvalumab+tremelimumab; **no responders** on durvalumab monotherapy; part B not opened because the 10% continuation threshold was unmet. **JAMA Oncol** 5(10):1431–8, [PMID 31318392](https://pubmed.ncbi.nlm.nih.gov/31318392/) | B |
| **C3** | B05 | MSS/pMMR colorectal: the regression predicts ~9%, the trial saw zero | **SUPPORTED — and the source understated it** | Le 2015: **0 of 18** pMMR colorectal patients had an immune-related objective response; 20-week irPFS 11%. Source reel said "<3% ORR"; the observed value is 0%. **NEJM** 372(26):2509–20, [PMID 26028255](https://pubmed.ncbi.nlm.nih.gov/26028255/) | A |
| **C4** | B05 | MSI-H / dMMR is the clearest hot-tumour biomarker | **SUPPORTED** | Le 2015: dMMR CRC irORR **40% (4/10)**; pMMR CRC **0% (0/18)**; dMMR non-CRC **71% (5/7)**. Mean 1,782 somatic mutations/tumour in dMMR vs **73** in pMMR (p=0.007); high mutation load associated with prolonged PFS (p=0.02). Same source as C3 | A |
| **C5** | B07 | Hot / inflamed = T cells inside the tumour parenchyma | **SUPPORTED** | Chen & Mellman 2017, *Nature* 541:321–330 — trichotomy defined on spatial CD8⁺ distribution relative to parenchyma and stroma | B |
| **C6** | B07 | Cold / desert = no lymphocytes in parenchyma **or** periphery | **SUPPORTED** | Chen & Mellman 2017, as above | B |
| **C7** | B07 | Excluded = immune cells abundant but confined to stroma, not penetrating parenchyma | **SUPPORTED** | Chen & Mellman 2017, as above | B |
| **C8** | — | Four PD-L1 IHC assays exist with different cutoffs | **SUPPORTED — but RETIRED from the script** | Hirsch 2017 Blueprint: 22C3/28-8/SP263 aligned on tumour-cell staining, **SP142 consistently lower**; **14 of 38 cases (37%)** would be classified differently depending on assay/cutoff. **J Thorac Oncol** 12(2):208–22, [PMID 27913228](https://pubmed.ncbi.nlm.nih.gov/27913228/). Verified and strengthened, then cut — see §3 | A |
| **C9** | — | The Tumor Inflammation Signature is an 18-gene panel | **QUALIFY — RETIRED from the script** | The T cell–inflamed GEP is a weighted sum of 18 genes; the count is right. But Ayers 2017's own abstract never states "18," and "Tumor Inflammation Signature" names the commercial assay derived from the profile, not the paper. **J Clin Invest** 127(8):2930–40, [PMID 28650338](https://pubmed.ncbi.nlm.nih.gov/28650338/). Cut — see §3 | B |
| **C10** | B09, B10, B12 | CXCR4 blockade increases T-cell trafficking into excluded tumours — mechanism confirmed, clinical benefit not | **SUPPORTED, with the split stated** | Bockorny 2020, COMBAT cohort 1: 37 enrolled, **29 evaluable**, BL-8040 + pembrolizumab, no chemo. **ORR 3.4% (1 PR)**, DCR 34.5% (9 SD), median OS 3.3 mo. Paper reports BL-8040 **increased CD8⁺ effector T-cell tumour infiltration**, decreased MDSCs, decreased circulating Tregs. **Nat Med** 26(6):878–85, [PMID 32451495](https://pubmed.ncbi.nlm.nih.gov/32451495/). Preclinical basis: Feig 2013, **PNAS** 110(50):20212–7, [PMID 24277834](https://pubmed.ncbi.nlm.nih.gov/24277834/) — **mouse; must be labelled as such on screen** | A |
| **C11** | B08, B10 | STING agonists activate innate immunity in cold tumours | **OUTDATED as the source states it — CORRECTED** | Meric-Bernstam 2022, ADU-S100/MIW815 phase I: n=**47**, **one confirmed PR** (+2 unconfirmed: parotid, myxofibrosarcoma); lesion stable or decreased in 94% of evaluable injected lesions. Paired biopsies showed **no significant on-treatment change in RNA expression or immune infiltration**; systemic activation *was* seen (inflammatory cytokines, peripheral T-cell clonal expansion). **Clin Cancer Res** 28(4):677–88, [PMID 34716197](https://pubmed.ncbi.nlm.nih.gov/34716197/). **Correction applied:** the source presents STING agonists as a live conversion strategy; the script states the opposite and shows both measurements | A |
| **C12** | B05, B11 | TMB correlates with response across cancer types at r=0.74 (r²=0.55), so 45% is unexplained | **SUPPORTED, then QUALIFIED BY US** | Yarchoan 2017: 27 tumour types, **r=0.74**, P<0.001, TMB from Foundation Medicine; formula **ORR = 10.8·ln(X) − 0.7**. **NEJM** 377(25):2500–1, [PMID 29262275](https://pubmed.ncbi.nlm.nih.gov/29262275/), full text PMC6549688. **Our qualification (C20):** 45% is the naive 1−r² reading; modelling small-trial attenuation puts it nearer 40%. B11 makes this correction out loud | A |
| **C13** | **CUT** | "Historical median of 9 months" in metastatic melanoma | **UNSUPPORTED — MUST NOT BE SPOKEN** | No citation exists in any source variant. The field benchmark is Korn 2008, **J Clin Oncol** 26(4):527–34, [PMID 18235113](https://pubmed.ncbi.nlm.nih.gov/18235113/) — 42 trials, 2,100 patients, median OS 6.2 mo. **But that figure is not in the abstract**, which reports prognostic factors only; it comes from secondary summaries. `[VERIFY: open Korn 2008 full text before this number is ever used]`. **Correction applied:** B04 uses KEYNOTE-006's own ipilimumab arm (median OS 15.9 mo, grade A) instead | **C — cut** |
| **C14** | B06, B12 | Radiation before immunotherapy converts cold tumours ("in situ vaccination") | **QUALIFY — and the script's first draft got the thresholds wrong** | Theelen 2019 PEMBRO-RT: 92 enrolled, **76 randomised** (40 control / 36 experimental). ORR at 12 wk **18% vs 36%, P=0.07**. Median PFS 1.9 vs 6.6 mo (HR 0.71, P=0.19); median OS 7.6 vs 15.9 mo (HR 0.66, P=0.16). Largest benefit in **PD-L1-negative** tumours. Paper's conclusion: criteria for meaningful clinical benefit not met. **JAMA Oncol** 5(9):1276–82, [PMID 31294749](https://pubmed.ncbi.nlm.nih.gov/31294749/). **REQUIRED CORRECTION, APPLIED:** the prespecified endpoint was *two* conditions — ORR rising from 20% to **50%**, at **P<0.10**. The trial **cleared the p-condition (0.07) and missed the ORR target (36%)**. An earlier draft of B06 stated "p=0.07" immediately after "it missed," which invites the reader to hear the p-value as the failure. B06 now names both bars and marks them pass/fail independently, and the frame is specified to do the same | A |
| **C15** | B13 | PDAC is not a single immune phenotype; hot/cold/excluded describes a sample, not a tumour type | **SUPPORTED** | Sivakumar 2025: single-cell multi-omics of matched tumour-infiltrating CD45⁺ cells and blood, **12 patients** plus two published datasets. Patients are **myeloid-enriched or adaptive-enriched**. In APACT trial patients, myeloid enrichment associated with **shorter OS** than adaptive enrichment. **Nat Commun** 16(1):1397, [PMID 39915477](https://pubmed.ncbi.nlm.nih.gov/39915477/) | A |
| **C16** | **CUT** | "<15% of cells in a pancreatic tumour are actually cancer" | **UNVERIFIED — MUST NOT BE SPOKEN** | Inherited from the source reel's B08 teaser for a different video. Not researched this pass, no citation located. `[VERIFY]` before it appears anywhere | **C — cut** |

---

## Part 2 — C17–C24, claims this script introduces

The research table enumerated the source's claims. The new script makes eight of its own,
mostly from our computation. A table covering only C1–C16 would leave the film's most
distinctive assertions unchecked — which is the failure mode this document exists to avoid.

| ID | Beat | Claim | Verdict | Evidence | Conf |
|---|---|---|---|---|---|
| **C17** | B05 | The published Yarchoan formula reproduces one of the letter's own worked predictions to 0.02 points and misses the other by 0.85 | **SUPPORTED, computed** | `tmb_orr_audit.py` §1. Sarcomatoid lung: stated 20.6%, recomputed **20.62%**. Basal-cell: stated 40.1%, recomputed **40.95%**; the formula needs TMB 43.7, not the 47.3 printed beside it. Both input pairs are quoted from the letter | A |
| **C18** | B05 | Residuals: the regression predicts pancreatic failure within ~0.6 pts, dMMR CRC within ~3.4, and over-predicts MSS CRC by ~8.9 | **SUPPORTED, computed — with one stated assumption** | `tmb_orr_audit.py` §2. Le 2015 whole-exome counts converted at **30 Mb**; sensitivity across 25–40 Mb is printed by the script and the dMMR conclusion holds throughout. Pancreatic TMB taken as **1.5/Mb**, a stated midpoint of the 1–2/Mb literature range — Chalmers 2017 ([PMID 28420421](https://pubmed.ncbi.nlm.nih.gov/28420421/)) supplementary table was not retrievable through any open route this pass. **REQUIREMENT: no specific pancreatic TMB number may be spoken or shown.** The claim the beat needs is comparative, and is | B |
| **C19** | B05 | Within Merkel-cell carcinoma, virus-positive (lower-burden) tumours responded at 62% vs 44% for virus-negative | **SUPPORTED as an ILLUSTRATION, never as a result** | Nghiem 2016: 26 patients dosed, 25 evaluable. MCPyV-positive **62% (10/16)**; virus-negative **44% (4/9)**. Overall ORR 56% (95% CI 35–76). **NEJM** 374(26):2542–52, [PMID 27093365](https://pubmed.ncbi.nlm.nih.gov/27093365/). **n=16 and n=9; intervals overlap heavily; not significant and not claimed to be.** Script says "an illustration and not a result" and the label is burned into the frame for the full beat | A |
| **C20** | B11 | Correcting for small-trial attenuation, the TMB-independent share is nearer 40% than 45% | **SUPPORTED as an ILLUSTRATIVE MODEL — not an empirical result** | `tmb_orr_audit.py` §4. Stated model: phenotype = a·ln(TMB) + TMB-independent term; ORR linear in phenotype; observed ORR = Binomial(nᵢ, ORRᵢ)/nᵢ with nᵢ log-uniform on 15–200. 400 reps/point, seeded. Sweep matches published r=0.74 at **40%** vs the naive 1−r² reading of 45%. **The trial-size distribution is our assumption, not a published one**, and the result is sensitive to it. `[VERIFY: the per-tumour-type n values in Yarchoan's supplementary appendix would replace this assumption with data; NEJM supplementary returned HTTP 403 this pass]`. **[ILLUSTRATIVE MODEL] must be burned into the frame** | B |
| **C21** | B08 | The one confirmed responder in the STING trial had Merkel-cell carcinoma — a tumour that was never cold | **SUPPORTED** | Meric-Bernstam 2022 names the PR as Merkel cell (see C11). That MCC is virus-antigen-driven and an above-the-line responder is Yarchoan 2017's own named example (C12). **This is a juxtaposition of two sourced facts, not a finding**, and the script presents it as a footnote | A |
| **C22** | B07, B10 | The six-link chain — mutations → antigens → priming → trafficking → infiltration → killing — and the claim that STING broke at link 4 while CXCR4 broke at link 6 | **SUPPORTED as an INTERPRETATION the evidence constrains** | The chain is a standard restatement of the cancer-immunity cycle (Chen & Mellman 2013/2017), not a novel model, and B07 presents it as vocabulary. The two break-points are read directly off measured endpoints: STING showed systemic activation with **no infiltration change** (C11); CXCR4 showed **infiltration increase** with 3.4% ORR (C10). Both are the papers' own measurements. The *labelling* of which link broke is our reading, and B10 states it as a reading | A (measurements) / B (link assignment) |
| **C23** | B03 | The same trial reports **38.7 percent** (5-year OS, all patients) and **38.7 months** (median OS, first-line subgroup) — same digits, different quantities | **SUPPORTED** | Corroborated independently across three ASCO Post reports of the trial: 5-year OS 38.7% vs 31.0%; first-line median OS **38.7 vs 17.1 months**. Overall median OS 32.7 vs 15.9 mo is grade A from the paper's abstract. **This is a coincidence of the data, not a claim about anyone's reasoning** — the script says people read a table with cells that look alike, and does not assert that this specific pair caused the error | B⁺ |
| **C24** | B04 | 10-year OS is 34.0% for pembrolizumab vs 23.6% for ipilimumab | **SUPPORTED** | Long 2024, KEYNOTE-006 10-year follow-up, read directly from the abstract: 834 randomised (pembro 556 / ipi 278); median OS 32.7 vs 15.9 mo, HR 0.71; **10-year OS 34.0% and 23.6%**; median melanoma-specific survival 51.9 vs 17.2 mo, HR 0.66. **Ann Oncol** 35(12):1191–99, [PMID 39306585](https://pubmed.ncbi.nlm.nih.gov/39306585/). Note the HR is 0.71 here vs 0.73 in the 5-year paper — updated follow-up, not a discrepancy; do not mix the two on one frame | A |

---

## Part 3 — Claims verified and then deliberately dropped

Both were checked, both hold up, and neither is in the film. Recording this so the work is
not silently lost and so nobody re-adds them without knowing what they cost.

- **C8, the four PD-L1 assays.** The strongest version of this claim is better than the
  source's: 37% of cases change classification depending on which assay is used. It is a
  genuinely good fact. It belongs to a *different* film — one about biomarker measurement —
  and in this one it would sit in Act I as a fourth "cell next door" instance, which is one
  too many. Act I already escalates three times.
- **C9, the 18-gene signature.** Same reason, plus it needs a wording fix (see C9) that costs
  a sentence the film does not have room for.

If either returns, C8's phrasing is *"37% of cases would be classified differently depending
on the assay"* — not *"four assays with different cutoffs,"* which asserts less than the
evidence supports.

---

## Part 4 — What must still be verified

### The KEYNOTE-006 grid — RESOLVED, by removing the dependency

**What was blocking:** B03 originally walked a four-row OS-by-timepoint grid (55.2 / 48.1 /
42.3 / 38.7) taken from a single secondary summary. A film about reading the actual table
cannot rest its central beat on a summary of the actual table.

**What was tried, and failed.** The paper is genuinely closed, and this was checked rather
than assumed:

| Route | Result |
|---|---|
| Publisher full text (thelancet.com) | HTTP 403 |
| Europe PMC | `isOpenAccess: N`, subscription-only |
| PMC | no PMCID exists for this article |
| OpenAlex | `oa_status: closed`, `any_repository_has_fulltext: false` |
| Unpaywall | `is_oa: false`, zero OA locations |
| Institutional repositories (Manchester, VUB) | metadata records only, no manuscript |
| ClinicalTrials.gov NCT01866319 posted results | **12-month OS only** — the registry does not carry the 5-year rates |

**How it was resolved.** Three ways, none of them "trust the summary":

1. **Corroboration.** The 5-year figures (38.7% / 31.0%, first-line 43.2% / 33.0%) and the
   first-line median OS (38.7 vs 17.1 months) are reported consistently across **three
   independent ASCO Post articles**. The 24/36/48-month values appear in only **one**. That
   asymmetry is itself the finding: the corroborated numbers were kept, the single-sourced
   ones cut (**C1a**).
2. **The dependency was removed.** The argument never needed the 24-month value. "Above 50%"
   being wrong follows from the 5-year figure alone. B03 now asserts only what three sources
   agree on, and offers no theory about which cell was misread.
3. **A better, grade-A anchor was found.** The **10-year follow-up** (Long 2024, *Ann Oncol*
   35(12):1191–99, [PMID 39306585](https://pubmed.ncbi.nlm.nih.gov/39306585/)) **is** indexed
   with a full abstract, and gives **10-year OS 34.0% vs 23.6%** plus median OS 32.7 vs 15.9
   months and HR 0.71 — all read directly from a primary source. B04 now closes on that
   instead of on a secondary figure (**C24**).

**What the film gained.** Chasing the grid surfaced **C23**: the same trial reports *38.7
percent* (5-year OS, all patients) and *38.7 months* (median OS, first-line). Same digits,
different quantities, a few lines apart — corroborated three times, and a far better beat than
the 24-month provenance story it replaced.

**Residual exposure, stated:** C1's two OS *rates* remain **B⁺** — triple-corroborated
secondary reporting of a closed paper. Everything else in B03/B04 is grade A. If Northeastern
library access to *Lancet Oncology* 20(9):1239–51 is available, opening it would upgrade C1 to
A in one step; nothing in the current cut depends on it.

### Remaining verifications — none blocking

| Item | Status | Blocking? |
|---|---|---|
| Korn 2008 pooled median OS (6.2 mo) | Secondary summaries only | No — the claim is **cut** (C13) |
| Chalmers 2017 per-tumour-type median TMB | Supplementary not retrievable | No — assumption stated and sensitivity reported (C18); no number spoken |
| Yarchoan supplementary per-type trial sizes | NEJM supplement returned HTTP 403 | No — but it would upgrade C20 from model to measurement |
| C1 OS rates at grade A | Requires institutional access to a closed paper | No — triple-corroborated, and the beat is built so nothing rests on a single source |

---

## Part 5 — Standing requirements on the frames

Derived from PROOF and from BEATS.md defect 1. These are visual obligations, not narration
notes, and each is checkable against the built beat sheet.

1. **Illustrative labels burned in, for the full beat, not flashed:** `n=16 / n=9 —
   illustration, not result` (B05, C19); `[ILLUSTRATIVE MODEL]` (B11, C20); `mouse` on any
   Feig 2013 visual (B09, C10).
2. **No frame may assert more than its claim.** Specifically: any STING response count reads
   *1 confirmed / 2 unconfirmed* (C11); the PEMBRO-RT frame marks the ORR bar and the
   p-condition **pass/fail independently** (C14); no pancreatic TMB value appears (C18).
3. **Citations legible at the moment of assertion**, not in an end card — C1's frame carries
   *Lancet Oncology*, not NEJM; C24's carries *Annals of Oncology* 2024.
4. **B04 shows reported points, not a fitted curve.** The script's artifact line originally
   asked for "both survival curves." We do not have the Kaplan-Meier data — the paper is
   closed (§4) and only the reported timepoints are corroborated. Drawing a smooth curve
   would mean inventing the shape of evidence we could not obtain, in a film about exactly
   that. The slate plots 38.7 / 31.0 / 34.0 / 23.6 as bars and says so in its own kicker.
5. **Units are load-bearing in B03.** The two 38.7s (C23) must be readable *as* a percent and
   *as* months. A viewer who can read the digits but not the unit has been shown the film's
   own error rather than the trial's.
6. **Never place the 5-year HR (0.73) and the 10-year HR (0.71) on the same frame** (C1, C24).
   Different follow-up, not a discrepancy — but adjacent on screen they read as one.

---
7. **No bar, curve or axis may imply a magnitude the source does not report.** B04 shows
   reported points because the Kaplan–Meier data is unobtainable; B08 shows direction only,
   labelled *no magnitudes reported*, because Meric-Bernstam 2022 reports both findings
   qualitatively. A bar is a quantitative assertion whether or not its axis is labelled — the
   first version of B08 drew four numbers that appear in no source, and PROOF failed the
   production gate on it.
8. **Every slate carrying claims carries a citation.** Enforced by `render_beats.py`, which
   refuses to render otherwise. B07 and B10 shipped sixteen renders without one.
9. **No rendered text contains `[` … `]`.** Verify with `audit_source.py` §6 against the new
   beat sheet before Gate P. The source reel shipped an unfilled placeholder on screen.

## Part 6 — Claims deliberately NOT made

- **No claim that anyone was dishonest.** Every error documented here — the source reel's, the
  field's, and ours — is consistent with ordinary misreading. `SOURCE-ANALYSIS.md` records
  what the artifacts contain; motive is not evidence, and the film says so by putting itself
  on the same list.
- **No claim that checkpoint inhibitors don't work.** C1 is the opposite: 38.7% five-year
  survival against a 15.9-month comparator is one of modern oncology's great results, and B04
  says exactly that.
- **No claim that conversion strategies have failed as an idea.** C11 and C14 are specific
  agents in specific trials. C14's PD-L1-negative subgroup cuts the other way and B12 reports
  it against the film's own argument.
- **No patient-level prediction from any figure here.** C12's r is a correlation of 27 *group
  averages*; the letter's own prediction interval for one cancer type is 19.4 points wide.
  Nothing in this film tells anyone what will happen to a person.
- **No mouse result is presented as a human result.** C10's preclinical basis is labelled.

---

## Keeping this table honest

If a beat changes, its row changes in the same commit. If a row cannot be filled, the beat is
cut — C13 and C16 are both cut claims, and they are listed here rather than deleted so that
the absence is on the record.

Re-run the computational evidence at any time:

```bash
python3 "Week 21/topic-video/experiment/tmb_orr_audit.py"
```
