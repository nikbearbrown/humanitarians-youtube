# FACTCHECK — three-pass-verification

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | Most builds stop at Pass 1; failures Pass 1 misses surface six days later | ✓ | Ch14: "Most builds stop at Pass 1. The failures Pass 1 misses are the ones that surface six days later in production." Verbatim. | — |
| B01 | Pass 1 = does it run; Pass 2 = boundary conditions; Pass 3 = user needs tested as users encounter them | ✓ | Ch14: The three-pass structure is defined verbatim. | — |
| B01 | Pass 3 failures (phone readability, load-time, accessibility) invisible to automated tests | ✓ | Ch14: "Pass 3 failures... require human judgment to define and verify." Verbatim in spirit. | — |
| B04 | 18-item checklist: Pass 1 six items, Pass 2 seven items, Pass 3 five items | Illustrative | Synthetic checklist count illustrating the three-pass structure from Ch14. | Marked synthetic. |
| B04 | Manual Pass 3 items: iPhone-preset portrait, 120% browser zoom, throttled 3G load time | Illustrative | Synthetic Pass 3 items consistent with Ch14's examples of user-need verification. | Marked synthetic. |
| B06 | 6-column table requires horizontal scroll on iPhone portrait; no automated test catches this | Illustrative | Illustrates Ch14's specific example of a Pass 3 failure. | Marked synthetic. |
| B06 | Failure goes into AGENTS.md: 'tables with >4 columns need responsive collapse for mobile' | Illustrative | Illustrates the learning-loop from Ch14 → AGENTS.md. | Marked synthetic. |

## Illustrative Scenarios
- B04: 18-item checklist with specific pass/fail counts — SYNTHETIC. Illustrates the three-pass structure from Ch14.
- B06: 6-column table phone-scroll failure — SYNTHETIC. Consistent with Ch14's mobile readability example.
- All code outputs are synthetic demonstrations.
