# FACTCHECK — vox-exposure-gate

Source chapter: `claude-cowork/chapters/10-what-not-to-delegate.md`  
Date: 2026-07-08

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | Reviewing the output before acting doesn't catch the problem — exposure already occurred | B03, B05 | ✓ | Chapter: "data exposure happens when the information enters the session, not when the output is shared." |
| 2 | For sensitive data, the hazard is the processing, not the destination | B07 | ✓ | Chapter: "Cowork processes information to produce the output; the processing is the risk, not just the destination of the file." |
| 3 | "Exposure occurs at ingestion. A review placed at the end sits downstream of the event it was meant to prevent." | B08 | ✓ | Chapter: "Feeding a student's disability documentation into Cowork has already occurred before any output exists. Reviewing the summary does not undo that." |
| 4 | Thirty student accommodation records scenario | B01, B11, B12 | ✓ illustrative | Chapter opening scene: "a folder of student accommodation files — disability documentation, medical letters, academic adjustment notes for thirty students." Labeled illustrative. |
| 5 | Files processed at 2:00, summary at 2:04, review at 2:06 — moving review changes nothing about 2:00 | B11, B12 | ✓ illustrative | Chapter: "Feeding a student's disability documentation into Cowork has already occurred before any output exists." Time-stamps are illustrative, pattern is from the chapter. Labeled illustrative. |
| 6 | Human review must be meaningful, not nominal | B09 | ✓ | Chapter: "human oversight must be meaningful, not nominal." NIST AI RMF framing used in chapter. |
| 7 | The effective gate position is before ingestion (before the file goes in) | B09, B12, B14 | ✓ | Chapter: "The right answer is not a better prompt. It is refusal, followed by a redesign conversation." / "developing the discipline to stop before the folder is opened." |

---

## Illustrative elements (labeled in narration or scenes)

- "Thirty accommodation PDFs" / "2:00 PM" / "2:04" / "2:06" — illustrative (time-stamps invented; scenario structure from chapter opening scene)

---

## Exclusions confirmed

- NO HIPAA/FERPA regulatory enumeration ✓
- NO seven-nondelegation-categories list ✓
- NO three-redesign-moves (reduce data / reduce action / increase governance) ✓
- NO data-retention-policy specifics ✓
- NO prompt-injection tangent ✓

---

## Terms table

| Term | Debut beat | Need created by |
|------|-----------|-----------------|
| ingestion | B05 (implicit — "the moment the file enters the session") | B04: viewer has seen the pipeline; they need a name for the first step |
| gate position | B09 (explicit — "two gate positions") | B05–B08: viewer has seen the exposure at ingestion and the key claim; they need a name for where to place the check |

All terms debut after the beat that creates the need for them. ✓
