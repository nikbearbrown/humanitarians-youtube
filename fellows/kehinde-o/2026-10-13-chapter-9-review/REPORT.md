# Project update — Fact-Checking Chapter 9

**Week:** 13 Oct 2026
**Type:** Project update

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1QAjFH3y4w_j7DfTFjUmGsy05ZVqJIv0r?usp=drive_link (`Medhavy_Kehinde/Fact Check/Chapter 9/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

Chapter 9 of the Medhavy textbook, on cell cycle control. The chapter runs to 292
sentences. The pipeline flagged 145 of them for human verification, and 30 of those
were assertions I could actually rule on: 20 need revision, 10 approved. A further
28 editorial findings came out of the same pass.

Four findings carry the reel:

- The chapter says "the 100,000 genes" of the human genome. That is a pre-genome-project
  estimate. NCBI records 19,116 known protein-coding genes, with consensus near 20,000.
  The number did not become wrong recently. It was superseded more than twenty years ago.
- The chapter attributes double-strand breaks to ultraviolet light. UV produces
  pyrimidine dimers and 6-4 photoproducts. Double-strand breaks are the signature
  lesion of ionising radiation. Right damage, wrong agent.
- The chapter has CDKN1C imprinting backwards. Only the maternal allele is expressed.
- Trilaciclib: this one corrects **my own** earlier finding, not the textbook's. I had
  recorded the approval wrongly. FDA NDA 214200 approved it in February 2021 for small
  cell lung cancer, to protect bone marrow during chemotherapy. The chapter was right
  and I was not.

The last one is the reason the video exists in the shape it does. An audit that never
catches itself is not an audit.

## Why this topic, this week

Chapter 9 was audited on 24 September and its corrections went into PR #46 with
Chapter 6's. Neither had a video or any record in the fellows repo, which means that
as far as anyone reviewing the work is concerned, it did not happen. This closes that
gap for Chapter 9. Chapter 6 shipped in the previous batch.

## Limits

- 30 assertions is what was **in scope**, not the whole chapter. 115 of the 145 flagged
  sentences were definitional, or were hedged claims with no checkable assertion, or
  repeated a claim already ruled on. They are listed in the workbook but not re-litigated.
- The 20 text edits span 6 files and are text only. Chapter 9 had no character-encoding
  damage, unlike Chapters 23, 25 and 30.
- A verdict of "approved" means the claim matches its source. It does not mean the
  source is the best available one.
- One item is reported unresolved: the workbook says the dinaciclib trial was terminated
  for futility, and ClinicalTrials.gov says COMPLETED. The reel reports the discrepancy
  rather than resolving it, because I have not established which record is right.
