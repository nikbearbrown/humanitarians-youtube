# FACTCHECK — handoff-condition-protocol

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B03 | subprocess.run for handoff condition execution | ✓ | Python stdlib subprocess docs |
| B03 | Exit code 0 = PASS, non-zero = FAIL | ✓ | Unix/POSIX exit code standard |
| B07 | "Claude is done" is not machine-checkable | ✓ | Subjective — no test file, no exit code, no observable artifact |

## Illustrative / Synthetic

All validator examples and Boondoggle Score JSON examples are synthetic.

## Exclusions Confirmed

- No CI/CD pipeline tutorial ✓
- No make/shell scripting tutorial ✓
