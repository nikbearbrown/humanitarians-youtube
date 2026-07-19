# FACTCHECK — engineering-partner-loop

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | The verification oracle runs first, then Claude fixes code, then oracle runs again | ✓ | Chapter 04: engineering partner loop described with oracle-first discipline | — |
| B01 | Without the oracle 'Claude fixed the bug' is unverifiable | ✓ | Chapter 04: oracle is the control system for verification | — |
| B01 | Human's job is approving scope, not debugging code | ✓ | Chapter 04: human role in the engineering partner loop — scope approval + plan review | — |
| B03 | Diff is minimal — only the failing function touched, nothing outside auth/ | Illustrative | Chapter 04: scope discipline — minimal edit, scoped task | None needed |
| B07 | Oracle is the control system | ✓ | Chapter 04: near-verbatim — oracle as supervisory mechanism | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| verification oracle | B01 | none — introduced as hook |
| engineering partner loop | B02 | B01 established the oracle concept |
| scope discipline | B03 | B02 showed the command |

## Exclusion Confirmation
- NO full CI/CD pipeline integration: PASS
- NO automated code review systems: PASS
- NO multi-file refactors: PASS

## Illustrative Examples
- B03–B04: auth.py failing test scenario — ILLUSTRATIVE from ch.04 worked walkthrough
- B05–B06: second failing test — ILLUSTRATIVE extension
