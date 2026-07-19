# FACTCHECK — vox-bypass-track
# Why Blocking the Accelerator Perfectly Can Still Fail
# Source chapter: cancer-biology/chapters/05-oncogenes.md

---

## TERMS TABLE

| Term | Debut beat | Earlier beat creating the need |
|---|---|---|
| EGFR | B02 (named as "a receptor on the cell surface that tells the cell to grow") | B01 hook establishes: drug targets oncogene precisely |
| osimertinib | B03 (named as "a drug designed to block that EGFR mutation specifically") | B02 establishes the EGFR mutation as the target |
| oncogene addiction | B05 (explained as "concentrated all of its survival wiring through that one point") | B03-B04 demonstrate the dramatic response then failure — viewer needs a name for why the response was so complete |
| MET amplification | B08 (explained as "a completely different receptor" that "can activate the same downstream survival signals") | B07 establishes that the tumor population contains rare variants; viewer needs a name for what the CRIMSON minority has |
| bypass track | B08 (named implicitly via the visual trace; B10 section card names the mechanism) | B08 shows MET routing around EGFR; viewer needs the concept name |
| RAS / PI3K | B08 (named as "the same downstream survival signals") | B08 is where they matter — no earlier mention; introduced at the exact moment of need |
| clonal selection | B11 (explained: "winner of a natural selection event that the drug ran") | B09-B10 establish that MET cells survive the drug kill; viewer needs the evolutionary framing |

---

## CLAIMS AND VERDICTS

| Beat | Claim | Verdict | Source / Derivation |
|---|---|---|---|
| B01 | A targeted cancer drug can produce dramatic tumor shrinkage and then fail with tumor regrowth even though the drug still blocks its target | PASS | Chapter p.73: "Eighteen months later, imaging shows new growth... the drug is still blocking that target — but now the cancer has also amplified MET" |
| B02 | Never-smoker with lung adenocarcinoma; sequencing finds EGFR exon-19 deletion | PASS | Chapter p.69: "A 55-year-old never-smoker is diagnosed with lung adenocarcinoma. Tumor sequencing shows an EGFR exon-19 deletion" |
| B02 | EGFR deletion "locks EGFR in a constitutively active, ligand-independent state" | PASS | Chapter p.69 verbatim |
| B03 | Osimertinib is a third-generation EGFR inhibitor; produces dramatic response within three months | PASS | Chapter p.69: "She starts osimertinib, a third-generation EGFR inhibitor, and within three months her tumors have shrunk dramatically" |
| B04 | At relapse, the EGFR deletion is still present and still being blocked; tumor now carries MET amplification | PASS | Chapter p.73: "Resequencing of the resistant tumor finds the original EGFR deletion still present — the drug is still blocking that target — but now the cancer has also amplified MET" |
| B04 | MET activates RAS/MAPK and PI3K/AKT independently of EGFR | PASS | Chapter p.73: "MET can activate RAS/MAPK and PI3K/AKT independently of EGFR" |
| B05 | Oncogene-addicted cancers depend on continuous output from one signal; blocking it leaves cells with no alternative | PASS | Chapter p.69: "The tumor is oncogene-addicted: its proliferation and survival depend on continuous EGFR output, and when that output is blocked, the cells have no alternative" |
| B06 | The dramatic response reflects oncogene addiction — the tumor concentrated its dependency on one signal | PASS | Chapter p.80: "The lesson from CML is that oncogene addiction creates a genuine vulnerability — the cancer has, in effect, concentrated its dependency onto one signal" |
| B07 | A tumor of 10 billion cells is a population with rare pre-existing variants | PASS (concept); ILLUSTRATIVE (number) | Chapter p.80 implies large populations with selection; the "10 billion cells" figure is standard oncology context (a 1 cm tumor contains ~10^8 cells; a clinically detected tumor ~10^9-10^10) — used as an illustrative order-of-magnitude |
| B07 | MET-amplified cells existed before treatment started | PASS | Chapter p.73 (the bypass track mechanism); Chapter p.80: "it has billions of cells, continuous mutation, and time to search" |
| B08 | MET is a receptor tyrosine kinase that signals through RAS/MAPK and PI3K/AKT | PASS | Chapter p.73: "MET, a different receptor tyrosine kinase. MET can activate RAS/MAPK and PI3K/AKT independently of EGFR" |
| B09 | Osimertinib has no effect on MET signaling; MET-amplified cells survive drug treatment | PASS | Chapter p.73: the drug "is still blocking that target" (EGFR) while MET-amplified clone grows — drug cannot block MET |
| B10 | "Resistance is selected, not created" | PASS | Chapter p.80: "the drug is the selection pressure. Whatever the pre-existing resistant minority turns out to be, it will expand." — the concept of pre-existing clones selected by drug is canonical resistance biology |
| B11 | The relapse tumor is the winner of a selection event run by the drug | PASS | Chapter p.80: "cancer is a population under selection, and the drug is the selection pressure" |
| B12 | 10 billion cells in the tumor at treatment start | ILLUSTRATIVE | Standard estimate for a clinically detectable solid tumor (10^9-10^10); labeled illustrative. Chapter states "billions of cells" generally |
| B12 | 1 in 1,000,000 cells carry MET amplification before treatment (example seed from card) | ILLUSTRATIVE | The card specifies "one-in-a-million MET-amplified cells" as the example seed; labeled illustrative in this film |
| B12 | ~10,000 MET-amplified cells before first pill (10^10 / 10^6 = 10^4) | ILLUSTRATIVE | Arithmetic from the illustrative numbers above: 10,000,000,000 / 1,000,000 = 10,000. Correct arithmetic. Labeled illustrative. |
| B13 | Osimertinib kills ~99.99% of EGFR-addicted cells in the example | ILLUSTRATIVE | The "99.99%" figure is from the card's example seed; labeled illustrative. Real response rates vary; the concept (near-total kill of the sensitive majority) is accurate |
| B13 | After 99.99% kill of 10B cells, ~1M sensitive cells remain; all ~10K MET cells survive | ILLUSTRATIVE | Arithmetic: 10^10 x 0.0001 = 10^6 survivors; 10K MET cells unaffected. Correct arithmetic. Labeled illustrative. |
| B14 | The bypass track (MET amplification) was present before treatment; drug revealed it | PASS | Chapter p.73-74 and p.80 |

## EXCLUSION AUDIT
| Excluded topic | Appears in film? | Verdict |
|---|---|---|
| Full EGFR biochemistry (kinase domain details) | NO — exon-19 deletion named but not detailed | PASS |
| T790M gatekeeper mutation | NO — not mentioned | PASS |
| Phenotypic switching | NO | PASS |
| Pharmacokinetics | NO | PASS |
| Comparison of EGFR inhibitor generations | NO — osimertinib named as "third-generation" only in passing | PASS |

## ILLUSTRATIVE NUMBERS DECLARATION
The following numbers in B12 and B13 are explicitly illustrative (from the card's example seed), not claimed as precise clinical measurements:
- 10,000,000,000 (10 billion) tumor cells
- 1 in 1,000,000 pre-treatment MET-amplification frequency
- ~10,000 pre-existing MET-amplified cells
- 99.99% kill rate
- ~1,000,000 surviving sensitive cells
- All ~10,000 MET cells surviving

These numbers are used to demonstrate the mechanism (selection mathematics) and are labeled illustrative in narration.

---

VERDICT: PASS
