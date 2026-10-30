# FACTCHECK — "Guardrails and Evals"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | Reviewing one run takes about 90 seconds (B01) | `SECONDS_PER_REVIEW = 90` in `evals.py`; stated as the author's assumption, not a measurement of anyone's system | ASSUMPTION, LABELLED |
| 2 | 1000 runs/day is 25 human hours (B02) | `python3 evals.py` prints `1000  25.0` | VERIFIED BY EXECUTION |
| 3 | 5% of a 2% failure rate leaves 19 unseen per day at 1000 runs (B04) | `python3 evals.py` prints `1000  20  1.0  19.0` | VERIFIED BY EXECUTION |
| 4 | A bigger sample does not fix it (B06) | `python3 evals.py` prints 5%→19.0 unseen/1.2h, 25%→15.0/6.2h, 50%→10.0/12.5h, 100%→0.0/25.0h | VERIFIED BY EXECUTION |
| 5 | The arithmetic is three lines (B05) | `undetected_failures()` is three lines, shown verbatim from the shipped file | VERIFIED BY COUNT |
| 6 | An eval never finds the failure you did not imagine (B09) | argued, not measured; stated as the limit of the whole approach | LIMIT, STATED AS SUCH |

## Corrections made before this master shipped

1. B05's code card filled about a fifth of its panel. Fixed in the toolkit rather than by padding the beat: `ClaudeCodeBeat` now sizes its type and its card to the content. The narration says "the arithmetic is three lines", so the three lines are correct and the panel was the defect.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- B05's code card filled about a fifth of its panel. Fixed in the toolkit rather than by padding the beat: `ClaudeCodeBeat` now sizes its type and its card to the content. The narration says "the arithmetic is three lines", so the three lines are correct and the panel was the defect.
