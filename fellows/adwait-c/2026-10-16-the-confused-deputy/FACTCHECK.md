# FACTCHECK — "The Confused Deputy"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | Operator text and fetched text are not distinguishable (B04) | `python3 deputy.py` prints `operator text and fetched text are distinguishable: False` | VERIFIED BY EXECUTION |
| 2 | The injected instruction reaches a real tool (B04) | `python3 deputy.py` prints `disable_2fa -> granted` | VERIFIED BY EXECUTION |
| 3 | A tool outside the grant is refused (B04) | same run prints `delete_account -> refused` | VERIFIED BY EXECUTION |
| 4 | Narrowing the tools changes what it can reach, not whether it arrives (B06) | `python3 deputy.py` prints `disable_2fa -> refused` and `the injection still arrives. It just has less to reach.` | VERIFIED BY EXECUTION |
| 5 | 'Ignore injected instructions' is itself an instruction (B08) | argued, not measured; offered as a reason the phrasing defence is weak | ARGUED, NOT MEASURED |
| 6 | This is not solved (B09) | no reliable way today to separate instructions from content in one context; stated on screen | LIMIT, STATED AS SUCH |

## Corrections made before this master shipped

1. **An em dash survived in the narration of B01 and BVDT.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.

## Safety note

`deputy.py` is defensive only. Its entire import list is `from __future__ import annotations` — it makes no network call and touches nothing outside the process. The 'injection' is a harmless fixture string, and the 'tools' set booleans in a dictionary. It demonstrates why a permission boundary is needed; it attacks nothing and cannot be pointed at anything.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- **An em dash survived in the narration of B01 and BVDT.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.
