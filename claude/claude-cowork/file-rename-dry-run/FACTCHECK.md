# FACTCHECK — file-rename-dry-run

Source chapter: `claude-cowork/chapters/08-organizing-and-renaming-files.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | Rename operations are CoWork-tier: multi-step, requires human review, irreversible on execution | B01 | ✓ | Chapter places file organization in the CoWork tier explicitly: "any task whose execution is irreversible requires human review before execution." |
| 2 | A tool without a mandatory dry-run skips the only review moment | B01 | ✓ | Chapter: "The manifest is the review moment. Without it, the rename happens before the human can evaluate whether it should." |
| 3 | 12-rename manifest with 1 conflict and 1 ambiguous case | B04 | ✓ illustrative | Synthetic scenario consistent with chapter's dry-run discussion. |
| 4 | Q1_final.pdf and Q1_draft.pdf conflict to q1-report.pdf | B05, B06 | ✓ illustrative | Synthetic conflict example illustrating duplicate-target detection described in chapter. |
| 5 | Manifest-first is "plan before execute" applied to the filesystem | B07 | ✓ | Chapter: "Generate the manifest first. Review it. Only then execute." |

---

## Illustrative elements

- 12-rename manifest with specific conflict — synthetic, consistent with chapter's discussion of batch rename risks.
- Q1_final/Q1_draft conflict example — synthetic, illustrates duplicate-target detection.

---

## Exclusions confirmed

- NO discussion of batch reversibility beyond the manifest pattern ✓
- NO specific OS or file system API details ✓
