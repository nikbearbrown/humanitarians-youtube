# FACTCHECK — spec-prompt-audit

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B03 | csv.reader with encoding='utf-8-sig' handles UTF-8 BOM correctly | ✓ | Python stdlib docs: utf-8-sig codec strips BOM on read |
| B03 | Empty cells require explicit check in csv reader | ✓ | csv.DictReader returns '' for empty cells; None requires `or None` check |
| B03 | pandas is not stdlib | ✓ | pandas is a third-party package not in Python stdlib |
| B04 | pytest exit code 0 = all tests pass | ✓ | pytest standard exit code semantics |
| B06 | Vague prompt produces openpyxl or pandas non-deterministically | ✓ illustrative | Training data contains multiple CSV-reading approaches |

## Illustrative / Synthetic

All code examples are synthetic illustrations for pedagogical purposes.

## Exclusions Confirmed

- No pandas tutorial ✓
- No full CSV parsing specification ✓
- No pytest tutorial ✓
