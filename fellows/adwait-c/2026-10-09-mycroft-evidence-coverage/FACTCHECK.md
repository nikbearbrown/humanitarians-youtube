# FACTCHECK — "Citations Nobody Checks"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | 21 of 21 references resolve across 4 claims (B05, B07, BVDT) | `cli coverage --verified-dir …` prints `coverage: 21/21 references resolved across 4 claims` | VERIFIED BY EXECUTION |
| 2 | Per claim: revenue 6, opex 9, cogs 3, payroll 3 (B05, B07) | `per_claim` in the emitted coverage report. **The earlier cut showed 6/5/5/5, which summed to the right total and was wrong per claim.** Corrected before the master was re-rendered | CORRECTED — see corrections |
| 3 | An unparseable reference raises rather than being skipped (B02) | `parse_reference()` raises `CoverageError`, shown verbatim from the shipped file | VERIFIED BY SOURCE |
| 4 | Eleven cases, each built to break it (B07) | `grep -cE '^\s*def test_' tests/test_coverage.py` returns 11 | VERIFIED BY COUNT |
| 5 | It reports and does not gate (B09) | the module emits a report; the distribution gate consumes it. Stated on screen | LIMIT, STATED AS SUCH |
| 6 | Resolving does not prove support (B08, BVDT) | argued: the wrong account can resolve perfectly. Three checks, none about meaning | ARGUED, NOT MEASURED |

## Corrections made before this master shipped

1. **The per-claim split was fabricated.** B05 and B07 showed revenue 6, cogs 5, opex 5, payroll 5. The real run is revenue 6, opex 9, cogs 3, payroll 3. Both sum to 21, which is exactly why it survived the first pass: the headline figure was right and the breakdown was not. Caught by re-running `cli coverage` and reading `per_claim` rather than trusting the beat sheet. Both beats re-rendered.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- **The per-claim split was fabricated.** B05 and B07 showed revenue 6, cogs 5, opex 5, payroll 5. The real run is revenue 6, opex 9, cogs 3, payroll 3. Both sum to 21, which is exactly why it survived the first pass: the headline figure was right and the breakdown was not. Caught by re-running `cli coverage` and reading `per_claim` rather than trusting the beat sheet. Both beats re-rendered.
