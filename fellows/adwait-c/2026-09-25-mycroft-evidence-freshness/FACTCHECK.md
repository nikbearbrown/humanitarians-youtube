# FACTCHECK — "How Old Is the Evidence?"

Claim-by-claim audit. Every figure on screen is either printed by a real run or labelled on
this page as an assumption, a judgement, or a fixture. Nothing is asserted from memory.

| # | Claim on screen | How it was checked | Verdict |
|---|---|---|---|
| 1 | This project's own pack: lag 148 days, age 92 days, verdict STALE (B02) | `cli freshness --as-of 2026-10-26 --max-lag-days 10 --max-age-days 120` prints `freshness: STALE (lag 148d, age 92d)`. **The supplied limits are now shown on screen**, because the verdict is not reproducible without them: at a 45 day age limit the same pack returns EXPIRED | VERIFIED BY EXECUTION — see corrections |
| 2 | A pack created before its period ended is refused (B05) | `FreshnessError` naming both dates; the same guard fired in this build when an `--as-of` earlier than `created_on` was passed by mistake | VERIFIED BY EXECUTION |
| 3 | A pack with no provenance is refused rather than assumed fresh (B06) | covered by `tests/test_freshness.py` | VERIFIED BY TESTS |
| 4 | 14 tests cover this module | `grep -cE '^\s*def test_' tests/test_freshness.py` returns 14 | VERIFIED BY COUNT |
| 5 | 148 days is routine for one report and disqualifying for another (B07) | argued; it is the reason the module reports rather than blocks | ARGUED, NOT MEASURED |
| 6 | The limits are supplied, never derived (B07, B09) | `max_lag_days` and `max_age_days` are required arguments with no defaults | VERIFIED BY SOURCE |

## Corrections made before this master shipped

1. **The verdict was not reproducible from what was on screen.** B02 showed `verdict STALE` with no limits. Re-running the engine at the obvious limits (lag 10, age 45) returns **EXPIRED**, not STALE, because 92 days is past a 45 day age limit. The narration's "the engine calls it stale" is true only under supplied limits of lag 10 and age 120, which the screen never showed. Fixed by putting `limits supplied   lag 10 days, age 120 days` on the artifact, so the verdict can be reproduced. Numbers unchanged; they were already right.

## What is deliberately not claimed

No model, vendor, product, benchmark or price is named. No real person's approval, review
or dissent is reproduced anywhere in this reel or in the repository it describes. Where a
named approver appears on screen it is a test fixture and the screen says so.

> FACT GATE: CLEARED

## Corrections applied 2026-10-26

- **The verdict was not reproducible from what was on screen.** B02 showed `verdict STALE` with no limits. Re-running the engine at the obvious limits (lag 10, age 45) returns **EXPIRED**, not STALE, because 92 days is past a 45 day age limit. The narration's "the engine calls it stale" is true only under supplied limits of lag 10 and age 120, which the screen never showed. Fixed by putting `limits supplied   lag 10 days, age 120 days` on the artifact, so the verdict can be reproduced. Numbers unchanged; they were already right.
