# FACTCHECK — plan-approval-gate

Source chapter: `claude-cowork/chapters/05-plans-approvals-and-redirection.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | Plans fail in predictable ways: scope, sources, exclusions, output, stop conditions | B01 | ✓ | Chapter defines these five failure modes explicitly and builds the 5-question gate around them. |
| 2 | Approving without review is abdication — looks like oversight but provides none | B01 | ✓ | Chapter: "Rubber-stamping a plan is not oversight — it's abdication dressed as process." |
| 3 | Q5 fail on "when done" stop condition | B04 | ✓ illustrative | Synthetic scenario. Chapter: "'When done' is not a stop condition — it delegates the definition of done to the AI." |
| 4 | Binary and testable revision: `wc -l < 100 returns true` | B04, B06 | ✓ | Chapter: "A stop condition is binary if a machine can evaluate it without human interpretation." The wc example is illustrative but consistent with chapter's definition. |
| 5 | Gate guarantees reviewability, not plan quality | B07 | ✓ | Chapter: "The gate is minimum viable oversight — it guarantees the plan can be reviewed, not that it's correct." |

---

## Illustrative elements

- Q3 operations scope, internal-only sources, single markdown under 2 pages — synthetic, consistent with chapter's plan approval examples.
- `wc -l < 100` as binary stop condition example — synthetic, consistent with chapter's definition of a binary and testable stop condition.

---

## Exclusions confirmed

- NO discussion of plan versioning or plan history ✓
- NO specific task categories for the plan reviewed ✓
