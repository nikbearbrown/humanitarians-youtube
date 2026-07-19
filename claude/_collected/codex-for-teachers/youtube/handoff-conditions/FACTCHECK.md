# FACTCHECK — handoff-conditions
**Build Handoff Conditions with Claude: Why 'Looks Good' Fails Every Time**
Source: `codex-for-teachers/chapters/05-handoff-conditions.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B00 | "Looks good" is a feeling; feelings don't catch broken links that appear three days after the build | ✓ | Chapter: subjective review is insufficient for build verification; specific testable conditions are required. |
| 2 | B01 | A handoff condition must be specific, testable, and binary (pass or fail — no "mostly") | ✓ | Chapter names these three properties explicitly as the required criteria for a valid handoff condition. |
| 3 | B01 | Weak versions fail the binary test; strong versions have a bash one-liner | ✓ | Chapter contrasts weak ("the page looks right") with strong (machine-executable check). |
| 4 | B04 | Bash check script runs green on the correct build: all 3 PASS | SYNTHETIC | Illustrative output. The script logic is correct for the described conditions; the specific PASS/FAIL output is a synthetic representation of expected behavior. |
| 5 | B06 | Condition 2 FAIL: an unexpected file was modified | SYNTHETIC | Illustrative failure scenario. The deliberate broken nav link scenario is consistent with the chapter's discussion of how weak conditions miss changes to unexpected files. |
| 6 | B06 | The script caught what a visual review would not have caught in 3 days of normal use | ✓ | Chapter: automated checks catch time-delayed failures (broken links that appear under specific navigation conditions) that visual review misses. |
| 7 | B07 | The bash check script is the artifact — it makes the condition executable, not just declarative | ✓ | Chapter: the executable check is the deliverable, not the prose description of the condition. |

---

## Exclusions confirmed
- No discussion of handoff conditions for multi-environment deployments
- No discussion of CI/CD integration
- No performance or load testing conditions

## Synthetic scenarios
Build outputs, PASS/FAIL results, and specific file modification scenarios are illustrative examples consistent with the source chapter. Not transcripts of actual Claude sessions.
