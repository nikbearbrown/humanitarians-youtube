# FACTCHECK — weekly-operations-packet

Source chapter: `claude-cowork/chapters/12-capstone-the-weekly-operations-packet.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | Weekly ops packet fails as Claude Code task because source documents change weekly | B01 | ✓ | Chapter: "The weekly ops packet is a CoWork task, not a Claude Code task, because the source documents are not stable — their format, structure, and content change every week." |
| 2 | CoWork tier requires human review of source conflicts before finalization | B01 | ✓ | Chapter: "The human's role in the weekly packet assembly is conflict resolution — not assembly." |
| 3 | 23 data points across 4 sections, all tagged with source | B04 | ✓ illustrative | Synthetic scenario consistent with chapter's capstone demonstration. |
| 4 | Without traceability, model would silently choose between conflicting sources | B06 | ✓ | Chapter: "Without source tags, the model has no way to surface the conflict — it resolves it silently, and the human never knows the conflict existed." |
| 5 | CONFLICTING SOURCES flag causes assembly to pause | B06, B07 | ✓ | Chapter describes the conflict detection mechanism: "When two sources disagree on the same data point, the assembly must stop and present both versions to the human." |

---

## Illustrative elements

- 4 source documents with specific claim counts per source — synthetic, consistent with chapter's capstone scenario.
- Approved/pending conflict between status.md and email_digest.md — synthetic, illustrates the conflict detection mechanism described in chapter.

---

## Exclusions confirmed

- NO discussion of specific project management tools ✓
- NO step-by-step guide to building the full packet (capstone overview only) ✓
