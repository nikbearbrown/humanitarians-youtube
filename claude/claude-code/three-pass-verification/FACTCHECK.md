# FACTCHECK — three-pass-verification

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Three-pass protocol: functional, edge-case, SDD needs | ✓ | Chapter 13: Verification |
| B01 | Pass 3 requires reading user needs literally, not test descriptions | ✓ | Chapter 13: Pass 3 definition |
| B05 | Amending the SDD to remove a need is a valid resolution for Pass 3 failure | ✓ | Chapter 13: done is relative to the spec |
| B07 | Pass 3 cannot be automated — requires human reading SDD aloud against running build | ✓ | Chapter 13: human judgment requirement |

## Illustrative / Synthetic

All verification examples (app tracker, empty state bug, at-a-glance failure) are synthetic.

## Key Terms

| Term | Definition |
|------|-----------|
| Pass 1 | Functional: does the happy path run? |
| Pass 2 | Edge cases: do boundaries named in the SDD handle correctly? |
| Pass 3 | SDD needs: read each user-need sentence aloud against the running build |

## Exclusions Confirmed

- No formal software testing methodology ✓
- No test coverage metrics ✓
- No TDD tutorial ✓
