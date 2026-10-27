# FACTCHECK — "When Not to Build an Agent"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | Two of six tasks pass all three conditions (B04) | `python3 decide.py` prints the table and `2 of 6 pass all three.` | VERIFIED BY EXECUTION |
| 2 | Each condition fails exactly twice (B06) | `python3 decide.py` prints `doing fails 2 of 6`, `undoable fails 2 of 6`, `checkable fails 2 of 6` | VERIFIED BY EXECUTION |
| 3 | The verdict is a conjunction, with no averaging (B02) | `return "AGENT" if (doing and undoable and checkable) else "NOT YET"`, shown verbatim from the shipped file | VERIFIED BY SOURCE |
| 4 | The six tasks are representative of what people automate (B03) | chosen by the author; no survey is claimed and none is cited | AUTHOR'S CHOICE, LABELLED |
| 5 | The scores are judgements, not measurements (B09) | stated on screen and in narration: the conditions were chosen and the tasks scored by hand, and the viewer is invited to score them differently | LIMIT, STATED AS SUCH |

## Corrections made before this master shipped

1. **An em dash survived in the narration of B03.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- **An em dash survived in the narration of B03.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.
