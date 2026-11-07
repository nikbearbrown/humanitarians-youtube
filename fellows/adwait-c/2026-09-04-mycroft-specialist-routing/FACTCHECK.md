# FACTCHECK — "One Agent, or a Team?"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | Gaps ranked revenue 200000, cogs 100000, opex 36000 (B05, BVDT) | `cli orchestrate` emits the routing report with exactly these figures | VERIFIED BY EXECUTION |
| 2 | Four recorded handoffs (BVDT) | `cli orchestrate` prints `delegations: 4 / 4` | VERIFIED BY EXECUTION |
| 3 | Three specialist tasks | `cli orchestrate` prints `specialist tasks: 3` | VERIFIED BY EXECUTION |
| 4 | Every ranked gap is blocked on a human (B09, BVDT) | every row in the routing report carries `EVIDENCE_COLLECTED_PENDING_OWNER` and `OWNER_CAUSAL_EXPLANATION` | VERIFIED BY EXECUTION |
| 5 | 8 tests cover this module | `grep -cE '^\s*def test_' tests/test_orchestration.py` returns 8 | VERIFIED BY COUNT |
| 6 | More specialists does not mean more gets closed (B09) | argued from the run: the queue is fully routed and fully blocked | ARGUED FROM THE RUN |

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED
