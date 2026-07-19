# FACTCHECK — task-brief-validator

Source chapter: `claude-cowork/chapters/04-the-cowork-task-brief.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | The CoWork template has 7 fields: Objective, Allowed Sources, Exclusions, Output Artifact, Decision Rules, Review Checkpoints, Stop Conditions | B01 | ✓ | Chapter defines the 7-field task brief template explicitly. |
| 2 | A missing Exclusions field is an implicit permission slip for the AI | B00, B07 | ✓ | Chapter: missing fields leave AI to decide what the human assumed was decided. |
| 3 | A 4-field brief scores 57% completeness and NOT READY | B04 | ✓ illustrative | Synthetic scenario consistent with the 7-field template math (4/7 ≈ 57%). Labeled as illustrative output. |
| 4 | "Use judgment" in Decision Rules is flagged as specificity failure | B06 | ✓ | Chapter warns that vague delegation language transfers judgment to the AI without a contract. |
| 5 | Completeness checks presence; specificity checks whether the field constrains the AI | B07 | ✓ | Chapter distinguishes between field presence and field quality. |

---

## Illustrative elements

- 4-field brief scenario and 57% score — synthetic, consistent with source chapter math.
- "Use judgment" Decision Rules example — synthetic, consistent with chapter's discussion of vague delegation language.

---

## Exclusions confirmed

- NO discussion of specific task categories beyond the brief template ✓
- NO implementation details beyond the validator scoring loop ✓
