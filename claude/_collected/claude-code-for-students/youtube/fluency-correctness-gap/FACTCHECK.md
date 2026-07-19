# FACTCHECK — fluency-correctness-gap

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Claude's output arrives as System 1 — fluent, plausible, completed-feeling | ✓ | Kahneman 2011 System 1/2 framework applied to LLM outputs |
| B04 | 100% pass rate on self-generated tests is not evidence of correctness | ✓ | Tests only verify code against tests, not against user needs |
| B05 | Claude self-audit may not catch the bug it generated | ✓ | Pearce et al. 2022 "Asleep at the Keyboard" |
| B07 | Verification requires adding the test case Claude did not generate | ✓ | Chapter 02: Division of Labor |

## Illustrative / Synthetic

- gpa_test.py with 5 passing tests and no tie case — synthetic illustration
- Claude self-audit response — synthetic illustration

## Sources

- Kahneman 2011 "Thinking, Fast and Slow" — System 1/System 2
- Pearce et al. 2022 "Asleep at the Keyboard" — GitHub Copilot self-audit limitation
- Chapter 02: Division of Labor — claude-code-for-students

## Exclusions Confirmed

- No formal cognitive science deep-dive ✓
- No LLM benchmark comparison ✓
