# FACTCHECK — "Multi-Agent Systems"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | 8 agents: supervisor 14 links, mesh 28 (B02) | `python3 agents.py` prints `8  14  28` | VERIFIED BY EXECUTION |
| 2 | 8 agents at 95% each finish 66.3% of the time (B05) | `python3 agents.py` prints `8  66.3%  34` | VERIFIED BY EXECUTION |
| 3 | 34 failures per 100 runs at 8 agents (B05) | same line of the same run | VERIFIED BY EXECUTION |
| 4 | 8 agents must each hit 99.36% to match one at 95% (B06) | `python3 agents.py` prints `8 agents  ->  each must be 99.36%` | VERIFIED BY EXECUTION |
| 5 | The chain arithmetic assumes every step must succeed (B04) | `end_to_end()` is `per_agent ** n`, shown verbatim; the assumption is stated on screen and in narration | ASSUMPTION, LABELLED |
| 6 | If work parallelises or agents vote, this inverts (B09) | stated as the caveat that bounds the whole argument | LIMIT, STATED AS SUCH |

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED
