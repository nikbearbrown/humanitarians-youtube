# FACTCHECK — "What Is MCP?"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | 5 apps × 10 tools is 50 direct connectors, 15 through a protocol (B02) | `python3 integrations.py` prints `5  10  50  15` | VERIFIED BY EXECUTION |
| 2 | 10 apps × 20 tools is 200 versus 30 (B02) | same run prints `10  20  200  30` | VERIFIED BY EXECUTION |
| 3 | One more tool costs 1 connector regardless of how many apps (B05) | `python3 integrations.py` prints 3→1, 5→1, 10→1, 50→1 | VERIFIED BY EXECUTION |
| 4 | At small scale direct wins (B06) | `python3 integrations.py` prints 1 app 1 tool: direct 1, protocol 2 → DIRECT; 1×3: 3 vs 4 → DIRECT; 2×2: 4 vs 4 → tie | VERIFIED BY EXECUTION |
| 5 | The protocol adds no capability (B03) | argued from the arithmetic: both columns call the same tools | ARGUED, NOT MEASURED |
| 6 | A bad tool is bad in any protocol (B09) | stated as the limit; nothing in the count addresses description quality | LIMIT, STATED AS SUCH |

## Corrections made before this master shipped

1. **An em dash survived in the narration of BVDT.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- **An em dash survived in the narration of BVDT.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.
