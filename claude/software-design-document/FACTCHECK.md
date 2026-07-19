# FACTCHECK — software-design-document

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Principle Collision Test: two principles must conflict under at least one realistic scenario to be real principles | ✓ | Chapter 07: SDD specification |
| B01 | User Need testability: stopwatch-and-laptop measurable | ✓ | Chapter 07: done-condition specification |
| B03 | Non-component list makes scope explicit and prevents scope creep | ✓ | Chapter 07: non-component list rationale |
| B06 | Collision Test fires on local-only vs. sync conflict | ✓ illustrative | Chapter 07: collision test example |

## Illustrative / Synthetic

All SDD examples (local timeline editor, multi-user sync conflict) are synthetic illustrations.

## Key Terms

| Term | Definition |
|------|-----------|
| Principle Collision Test | Two principles must conflict under at least one realistic scenario |
| Non-component list | Explicit list of what is OUT of scope |
| Done-condition | One measurable statement of when the SDD goal is achieved |

## Exclusions Confirmed

- No full SDD methodology tutorial ✓
- No architectural patterns deep-dive ✓
- No project management methodology ✓
