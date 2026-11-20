# FACTCHECK — "Grounding and Retrieval"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | Two of four citations check out automatically (B03) | `python3 grounding.py` prints `citations that check out automatically : 2 of 4` | VERIFIED BY EXECUTION |
| 2 | One of those two is still false (B05) | `python3 grounding.py` prints `of those, claims that are still FALSE  : 1` | VERIFIED BY EXECUTION |
| 3 | The falsifying case: 14 days claimed, 30 days quoted (B05) | `python3 grounding.py` prints both the claim and the real quote side by side | VERIFIED BY EXECUTION |
| 4 | Three distinct failure modes are distinguished (B03) | `CITATION_CHECKS_OUT`, `QUOTE_NOT_IN_SOURCE`, `MISSING_SOURCE` in the shipped file | VERIFIED BY SOURCE |
| 5 | The documents are invented for the example | an expense policy written for this video; no real organisation's policy is quoted | FIXTURE, LABELLED |

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED
