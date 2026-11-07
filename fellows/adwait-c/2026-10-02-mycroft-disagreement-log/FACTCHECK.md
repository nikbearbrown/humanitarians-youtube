# FACTCHECK — "When the Reviewer Disagrees"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | A reviewer may not restate the engine's number (B04) | `if "engine_value" in record: raise DisagreementError`, shown verbatim | VERIFIED BY SOURCE |
| 2 | The engine's value is read from the run, not the record (B04) | `engine_findings()` keys off `observation.category_bridge[].key` in the run log | VERIFIED BY SOURCE |
| 3 | A disagreement against a category the engine never mentioned is refused (B06) | covered by `tests/test_disagreement.py` | VERIFIED BY TESTS |
| 4 | The reviewer is a test fixture (B05) | 'Dana Whitfield, Controller' is the same fixture value used across this series; no real person's dissent is recorded anywhere in the repository | FIXTURE, LABELLED |
| 5 | 13 tests cover this module | `grep -cE '^\s*def test_' tests/test_disagreement.py` returns 13 | VERIFIED BY COUNT |
| 6 | It resolves nothing (B09) | stated on screen: an open entry stays open, and the gate treats it as blocking | LIMIT, STATED AS SUCH |

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED
