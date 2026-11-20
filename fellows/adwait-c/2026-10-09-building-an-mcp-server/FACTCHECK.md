# FACTCHECK — "Building a Tool Server"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | The client is told nothing in advance (B02) | `python3 server.py` step 1 prints both tools from the registry; no list is configured anywhere | VERIFIED BY EXECUTION |
| 2 | Descriptions come from docstrings, not a second config (B04) | `describe()` calls `inspect.getdoc(fn)`, shown verbatim from the shipped file | VERIFIED BY SOURCE |
| 3 | The contract is name, description, input schema (B05) | `python3 server.py` step 2 prints exactly that JSON | VERIFIED BY EXECUTION |
| 4 | row_count('sales.csv') returns 3 (B07) | `python3 server.py` step 3 prints `row_count(path='sales.csv')  ->  3` | VERIFIED BY EXECUTION |
| 5 | An unknown tool is refused by name (B07) | `python3 server.py` step 4 prints `'no such tool: delete_everything'` | VERIFIED BY EXECUTION |
| 6 | This is not a production server (B09) | no transport, no session, no auth, no error semantics; stated on screen | LIMIT, STATED AS SUCH |

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED
