# FACTCHECK — "Whose Failure Is It?"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | 11 conflicts, 10 in another contributor's files (B02) | counted from the conflict list before anything was resolved; `scripts/gateway/` 10 files, `logs/RUN_LOG.md` 1 | VERIFIED BY COUNT |
| 2 | My commits touched none of those files (B02) | `git log` over the conflicted paths returns no commit of mine | VERIFIED BY REPOSITORY |
| 3 | The base branch fails without me (B06) | `verify` on main, last five runs, all failure | VERIFIED BY CI HISTORY |
| 4 | The cause is a file-type map that includes Python (B07) | `KIND` in `mycroft/scripts/conformance.mjs` maps `'.py': 'py'`, shown verbatim. **The earlier cut showed invented Python under this JavaScript filename**; corrected to the real source before the master was re-rendered | CORRECTED — see corrections |
| 5 | Nineteen failing checks are inherited, not caused | they reproduce on the base branch across five consecutive runs | VERIFIED BY CI HISTORY |
| 6 | A fix nobody asked for, in an unrelated pull request, is a second problem (B08) | argued; the one-line fix is real and was deliberately not made here | ARGUED, NOT MEASURED |

## Corrections made before this master shipped

1. **B07 showed invented Python attributed to a real JavaScript file.** The beat was titled `conformance.mjs` and the language badge read PYTHON, while the code was Python-shaped text that does not exist in that file. Replaced with lines 45 to 59 of `mycroft/scripts/conformance.mjs`, verbatim, which actually contain the `'.py': 'py'` mapping the narration describes. This also required two toolkit fixes, below.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- **B07 showed invented Python attributed to a real JavaScript file.** The beat was titled `conformance.mjs` and the language badge read PYTHON, while the code was Python-shaped text that does not exist in that file. Replaced with lines 45 to 59 of `mycroft/scripts/conformance.mjs`, verbatim, which actually contain the `'.py': 'py'` mapping the narration describes. This also required two toolkit fixes, below.
