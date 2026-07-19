# FACTCHECK — vox-format-credibility

Source chapter: `claude-cowork/chapters/06-extracting-data-from-documents.md`  
Date: 2026-07-08

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | 47 receipts extracted to a 47-row spreadsheet in ~3 minutes | B01, B11 | ✓ illustrative | Chapter p.1: "forty-seven receipts … produces a clean table in about three minutes." Used as the running example throughout ch06. Labeled illustrative in narration (B11) and scenes. |
| 2 | Row 23 reads $342.00; source receipt says $34.20 | B04, B11 | ✓ illustrative | Chapter p.1: "The total reads $342.00 … the actual receipt … $34.20. The decimal point moved." Exact figures from the chapter. Labeled illustrative in narration B11. |
| 3 | One smudged photo yields "Unknown Merchant" copied to 3 other rows | B08 | ✓ illustrative | Chapter p.1: "Row 31 has a vendor listed as 'Unknown Merchant' … Cowork quietly copied that name to three other rows without flagging that it guessed." Figures from the chapter. Labeled illustrative. |
| 4 | Extraction has two separate steps: reading the document and writing the table | B05, B07 | ✓ | Chapter section "Extraction vs. Summarization": extraction produces specific values claimed to represent source document contents — this is the two-step characterization in the film. |
| 5 | "Structure confers credibility" | B09 | ✓ | Chapter, verbatim: "structure confers credibility. A well-formatted table with column headers looks authoritative whether the values came from a clean digital invoice or from a model's confident guess." |
| 6 | The formatting step does not know if the reading step succeeded | B07 | ✓ | Follows directly from the chapter's core framing: "The spreadsheet is a claim about what those documents said. The two are not the same thing." |
| 7 | 3 errors found in a few minutes of checking | B11, B12 | ✓ illustrative | Chapter: "Three errors found in a few minutes of checking." Exact quote from the chapter. Labeled illustrative. |
| 8 | Format is evidence that formatting ran, not that the reading was correct | B09, B10 | ✓ | Chapter: "Clean-looking output is not the same as correct output." The film's interpretation is a faithful restatement. |
| 9 | Spot-check 5 rows of 47 (10% or 5 rows, whichever is larger) | B12 | ✓ illustrative | Chapter "Numeric spot-check" section: "Pick a sample of rows — at minimum 10% or five rows, whichever is larger." 5 rows of 47 = 10.6%, consistent. Labeled illustrative. |

---

## Illustrative numbers (labeled in narration and/or scenes)

- 47 receipts, 47 rows — illustrative (from chapter example)
- $342.00 / $34.20 — illustrative (from chapter example)
- "Unknown Merchant" / 3 additional rows — illustrative (from chapter example)
- "3 errors in a few minutes" — illustrative (from chapter example)
- "5 rows spot-checked, 2 errors, 42 unchecked" — illustrative (derived from chapter guidance)

---

## Exclusions confirmed

- NO OCR or vision-model architecture explanation appears anywhere ✓
- NO schema-design template or field-definition walkthrough ✓
- NO full verification-checklist enumeration (row count, source-file column, exception log, etc.) ✓
- NO second example type (invoices) ✓
- NO hallucination-vs-granularity error taxonomy ✓

---

## Terms table

| Term | Debut beat | Need created by |
|------|-----------|-----------------|
| extraction | B01 (implicit) / B05 (named) | B02: the spreadsheet exists and came from somewhere — the viewer now wants a name for what produced it |
| formatting step | B05 | B04: two cells look the same but have different values — the viewer now wants a name for what made them look identical |
| reading step | B05 | B04: same — the viewer wants a name for what produced the wrong value |
| structure confers credibility | B09 | B07–B08: viewer has seen the read fail and the format still succeed — they want a name for the mechanism |

All terms debut after the beat that creates the need for them. No term appears before its motivating context.
