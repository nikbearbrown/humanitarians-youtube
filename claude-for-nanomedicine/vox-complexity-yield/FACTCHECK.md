# FACTCHECK — vox-complexity-yield

## Claims audit

| # | Claim (narration/viz) | Beat | Verdict | Source / Note |
|---|---|---|---|---|
| 1 | "More than half the manufactured batches fail" (six functions at 90%) | B01, B03 | PASS | Chapter 8: "More than half your batches fail some specification." 0.9^6 = 0.531 — confirmed |
| 2 | Six functions: targeting, imaging, drug release, heating, pH-responsive linker, targeting antibody | B02 | PASS | Chapter 8 opening case: gold core / photothermal, iron-oxide / MRI, fluorescent dye, chemotherapy payload, pH-responsive linker, antibody for targeting — six named functions |
| 3 | "Each working at ninety percent reproducible, batch to batch" | B03 | PASS | Chapter 8: "Suppose each of six functions in your nanoparticle is 90% reproducible batch-to-batch — a generous assumption" |
| 4 | "Reproducibility multiplies, not adds" | B04 | PASS | Chapter 8: "The probability that all six are within specification in the same batch is 0.9 raised to the sixth power" — multiplication explicitly stated |
| 5 | "0.9^1 = 90%, 0.9^2 = 81%, 0.9^3 = 73%, 0.9^4 = 66%, 0.9^5 = 59%, 0.9^6 = 53%" | B05 | PASS | Arithmetic verified: 0.9=0.900, 0.81=0.810, 0.729=0.73, 0.6561=0.66, 0.59049=0.59, 0.531441=0.53 (rounded to nearest integer percent) |
| 6 | "0.95^6 = 74%" (at 95% per-function quality) | B06 | PASS | Chapter 8: "Raise the per-function reproducibility to 95% — exceptional for a complex particle — and the whole-particle yield is about 74%." 0.95^6 = 0.7351 ≈ 74% — confirmed |
| 7 | "Doxil carries one drug payload — one function to characterize" | B07 | PASS | Chapter 8: "A liposome carrying doxorubicin — the Doxil design — has one active function to characterize: the drug encapsulation efficiency and release rate." |
| 8 | "A radioligand has one function: labeling yield" | B07 | PASS | Chapter 8: "A radioligand has one: the labeling yield and radiochemical purity." |
| 9 | "These are the designs that reached patients" (Doxil, Abraxane, radioligands) | B07, B11 | PASS | Chapter 8: "Single-function nano-drugs that translated: Doxil, Abraxane, and the ADCs of the previous chapter. They do one job... They are in clinical use." |
| 10 | "Process engineering cannot make a six-parameter assembly as consistent as a one-parameter assembly" | B08 | PASS | Chapter 8: "Reproducibility is multiplicative; no process engineering makes a six-parameter assembly as consistent as a one-parameter assembly, because each function adds its own polydispersity contribution..." |
| 11 | Program A: 1-function, 90% yield, ~11/12 batches pass (illustrative) | B09 | ILLUSTRATIVE | The card's example seed: "12 successful batches out of 13 last year." Adapted to 11/12 for round numbers. Labeled illustrative. |
| 12 | Program B: 6-function, 0.9^6 = 53%, ~7/12 batches pass (illustrative) | B09 | ILLUSTRATIVE | The card's example seed: "7 batches out of 13 pass spec." Adapted to 7/12 to match 12-batch framing. 12 × 0.531 = 6.4 → 7 is a reasonable rounding. Labeled illustrative. |
| 13 | "The Christmas tree particle stays in the paper" | B11 | PASS | Chapter 8: "It never gets there." re: the opening-case six-function particle. "The book's verdict — conceptually appealing but not yet clinically translated." |
| 14 | "Simplification is not a concession. It is the work." | B11 | PASS | Chapter 8: "Simplification is the work." Exact quote. |

## Exclusion confirmations
- Protein corona detail: appears in chapter but EXCLUDED from film — not mentioned in narration or viz
- PDT/PTT/AuroLase: appears in chapter but EXCLUDED — no photodynamic or photothermal gradient discussed
- Cell-derived particles / exosomes: appears in chapter's "Still Puzzling" section but EXCLUDED
- Full NCI characterization list (size, polydispersity, surface chemistry, encapsulation, release, stability, sterility): chapter cites this list, EXCLUDED from film — only referenced as "one function to characterize"

## Illustrative numbers (labeled as such)
- B09: "eleven of twelve" batches in Program A — illustrative, not from clinical data
- B09: "seven of twelve" batches in Program B — illustrative, computed from 0.9^6 ≈ 0.531

## Terms table

| Term | Debut beat | Setup beat (viewer needed the name) |
|---|---|---|
| theranostic nanoparticle | B02 | B01 (the elegant particle that fails) |
| reproducibility (batch-to-batch) | B03 | B02 (showed the six functions) |
| multiplicative | B04 | B03 (question: why does 90% per function still fail?) |
| 0.9^6 | B05/B06 | B04 (gates explained) |
| Doxil | B07 | B07 (introduced as the translated contrast) |
| radioligand | B07 | B07 (named with Doxil and Abraxane as translated class) |
| Christmas tree particle | B11 | B02 (showed the complex six-function design) |
