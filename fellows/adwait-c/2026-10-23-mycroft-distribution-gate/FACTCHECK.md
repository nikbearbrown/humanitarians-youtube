# FACTCHECK — "May This Leave the System?"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | Called with nothing, four conditions refuse and one clears (B03) | `cli distribution-gate --output …` with no artifacts prints four BLOCKED lines and `CLEARED no_open_disagreements`. **The earlier cut showed only the four refusals and called them 'four conditions', which miscounted and dropped the asymmetry the video is about**; corrected, and B03's narration was rewritten and its audio regenerated | CORRECTED — see corrections |
| 2 | Against the real artifacts: three cleared, two blocking (B05) | `cli distribution-gate --freshness … --coverage-report …` prints exactly that | VERIFIED BY EXECUTION |
| 3 | STALE clears, EXPIRED does not (B07) | `FRESHNESS_ALLOWED = {"FRESH", "STALE"}` in `distribution.py` | VERIFIED BY SOURCE |
| 4 | No disagreement log clears; an entry blocks (B07) | the real run prints `no disagreement log; nobody dissented` | VERIFIED BY EXECUTION |
| 5 | The materiality approver is a fixture (B05) | labelled `(fixture)` on screen; no real approval is recorded anywhere | FIXTURE, LABELLED ON SCREEN |
| 6 | 13 tests cover this module | `grep -cE '^\s*def test_' tests/test_distribution.py` returns 13 | VERIFIED BY COUNT |
| 7 | It cannot actually stop anybody (B09) | it sends nothing and blocks no file; what it produces is a record. Stated on screen | LIMIT, STATED AS SUCH |

## Corrections made before this master shipped

1. **B03 miscounted the gate and dropped its own point.** It showed four BLOCKED lines under the heading "Four conditions, four refusals". The gate has five conditions, and called with nothing the fifth **clears**, because no disagreement log means nobody dissented. That asymmetry is the subject of B07, so omitting it here contradicted the video. All five lines are now shown, the heading reads "Four refuse. One clears on nothing.", and the narration was rewritten and its audio regenerated.

2. **A named approver was shown without saying it is a fixture.** B05 displayed `approved by Dana Whitfield, Controller` with no qualifier, in a beat a viewer reads as a real approval record. Now labelled `(fixture)` on screen. The same label was added to the materiality video's four-attempt beat.

3. B07's two cards overlapped: a two-line sub pushed one card past its slot. Subs shortened to one line each.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- **B03 miscounted the gate and dropped its own point.** It showed four BLOCKED lines under the heading "Four conditions, four refusals". The gate has five conditions, and called with nothing the fifth **clears**, because no disagreement log means nobody dissented. That asymmetry is the subject of B07, so omitting it here contradicted the video. All five lines are now shown, the heading reads "Four refuse. One clears on nothing.", and the narration was rewritten and its audio regenerated.

- **A named approver was shown without saying it is a fixture.** B05 displayed `approved by Dana Whitfield, Controller` with no qualifier, in a beat a viewer reads as a real approval record. Now labelled `(fixture)` on screen. The same label was added to the materiality video's four-attempt beat.

- B07's two cards overlapped: a two-line sub pushed one card past its slot. Subs shortened to one line each.
