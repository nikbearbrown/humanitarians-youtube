# FACTCHECK — workflow-card-generator

Source chapter: `claude-cowork/chapters/11-building-a-reusable-cowork-workflow.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | The 15-field workflow card format exists to capture task knowledge before it disappears | B01 | ✓ | Chapter defines the 15-field reusable workflow card: Task Type, Trigger, Input Format, Prompt Template, Allowed Sources, Exclusions, Output Artifact, Review Checklist, Stop Conditions, Frequency, Owner, Quality Gate, Archive Destination, Version, Notes. |
| 2 | 12 of 15 fields populated; 3 flagged NEEDS HUMAN REVIEW | B04 | ✓ illustrative | Synthetic scenario consistent with chapter's workflow capture discussion. Chapter notes that Owner and Frequency are commonly missing from initial task briefs. |
| 3 | NEEDS HUMAN REVIEW flags are as valuable as populated fields | B07 | ✓ | Chapter: "The gaps in the workflow card are not failures — they are the explicit record of what the human must supply before the workflow can be run again." |
| 4 | Canonical card from two instances is more reliable than either alone | B06 | ✓ | Chapter: "Each additional run of a workflow produces evidence that can improve the canonical card — resolving ambiguities and surfacing edge cases." |
| 5 | Completed task brief contains everything needed to define a reusable workflow | B01 | ✓ | Chapter: "Every completed CoWork task is a workflow waiting to be extracted." |

---

## Illustrative elements

- 12/15 populated fields with specific gap examples (Frequency, Owner, Archive Destination) — synthetic, consistent with chapter's discussion of common missing fields.
- Two-instance merge scenario — synthetic, illustrates the canonical card refinement process.

---

## Exclusions confirmed

- NO discussion of version control or workflow repository systems ✓
- NO specific tooling beyond the workflow card format ✓
