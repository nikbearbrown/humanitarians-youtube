# FACTCHECK — receipt-extraction-pipeline

Source chapter: `claude-cowork/chapters/06-extracting-data-from-documents.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | Schema-less extraction produces date format inconsistencies and silent total/subtotal confusion | B01, B04 | ✓ | Chapter: "Without a schema, the model makes formatting decisions you did not specify — date formats, numeric precision, field naming — and those decisions are invisible to you." |
| 2 | Schema-driven extraction raises exception flags for ambiguous fields | B02, B04 | ✓ | Chapter: "The schema forces the model to surface ambiguity rather than resolve it silently." |
| 3 | 5-receipt comparison: 0 exception flags (no-schema) vs 3 exception flags (schema) | B04 | ✓ illustrative | Synthetic scenario consistent with chapter's schema-vs-no-schema demonstration. |
| 4 | High-value threshold ($500) routes to human approval queue | B05, B06 | ✓ | Chapter: "Threshold rules are exception rules — they define when the AI should stop and wait for a human." |
| 5 | AI flags and stops; does not approve high-value receipts | B06 | ✓ | Chapter: "The AI's role in an exception workflow is to detect the exception and route it — not to resolve it." |

---

## Illustrative elements

- 5-receipt dataset with 3 exception flags — synthetic, consistent with chapter's extraction demonstration.
- $500 threshold flag example — synthetic, illustrates threshold-based routing described in chapter.
- Specific exception types (foreign currency, handwritten total, ambiguous line item) — synthetic, consistent with chapter examples.

---

## Exclusions confirmed

- NO specific AI model comparison for extraction accuracy ✓
- NO discussion of OCR tooling or document scanning ✓
