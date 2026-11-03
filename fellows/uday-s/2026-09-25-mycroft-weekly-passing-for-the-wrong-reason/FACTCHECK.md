# FACTCHECK — Passing For The Wrong Reason

Status: **GATE F SIGNED — 2026-09-25. 14 rows PASS.**

Subject: `D:/Projects/mycroft`, branch `feature/market-sentiment-human-report`,
commit **`4157a8e`** ("give gates 4 and 5 real failure paths", 2026-09-25),
with companion commit `7987a4e` ("promote recipe to RUNNABLE-SAMPLE").
Episode 5.

Every figure was produced by running the gate tests live. The three break-test
cases were reproduced in a scratch tree, so the subject repo was never written
to — confirmed clean afterwards.

| # | Beat | Claim | Verdict | Derivation |
|---|---|---|---|---|
| 1 | B01 | Episode 4 closed by asking what makes a green indicator go red | ✓ PASS | Previous episode's B11 narration |
| 2 | B04 | The old gate-5 test passed if an approval record existed **or** `[TODO: APPROVE]` was in the recipe | ✓ PASS | `git show 968470a:recipes/…` — shown verbatim |
| 3 | B04 | That marker is always present | ✓ PASS | `grep -c "\[TODO: APPROVE\]"` on the current recipe = **1**; it is template text |
| 4 | **B05** | **The old test, run today, passes — on the marker alone** | ✓ PASS | Ran the old test verbatim against the current tree: **PASS**, with no approval file anywhere |
| 5 | B05 | `logs/gate-decisions/` holds gates 1–4 and no gate 5 | ✓ PASS | Directory listing: `gate-1.json`, `gate-2.json`, `gate-3.json`, `gate-4.json`. No gate-5 |
| 6 | B05 | So the test reported a clearance that never happened | ✓ PASS | Follows from rows 4 and 5; the commit states the same |
| 7 | B07 | The new gate-5 test reads the run's artifacts | ✓ PASS | Current recipe line 68, shown verbatim: `test -f …gate-5.json \|\| ! grep -rqs '"live_call_performed": true' logs/… data/raw/…/runs/` |
| 8 | B08 | No live call, no approval → PASS | ✓ PASS | Break-test case A, reproduced |
| 9 | B08 | Live call, no approval → **FAIL** | ✓ PASS | Break-test case B, reproduced — the path that did not exist before |
| 10 | B08 | Live call with approval → PASS | ✓ PASS | Break-test case C, reproduced |
| 11 | B09 | Gate 5 still passes today, because no live call is possible | ✓ PASS | Ran the new test against the real tree: PASS, and the approval file does not exist — so it passes on the second clause |
| 12 | B10 | status RUNNABLE-SAMPLE · version 0.2.0 · todos_open 2 · attestation null | ✓ PASS | Recipe frontmatter, verbatim |
| 13 | B10 | Step 3 gained `type_errors` | ✓ PASS | 11 references in `validate-data-shape.py`; the gap this series flagged in episode 3 |
| 14 | B10 | Gate 4 now requires all six scripts to compile | ✓ PASS | Current recipe line 66: a `for` loop running `python3 -m py_compile` over all six, `|| exit 1`. Ran it: all six compile |

## What makes B05 stronger than the commit message

The commit says creating `logs/gate-decisions/` made the old gate "actively
misleading". That is an assertion about a past state. The reel does better: it
**runs the old test against today's tree and shows it still passing**, beside
the directory listing that has four real records and no gate-5. That is not a
claim about what used to happen — it is a demonstration of what still would.

## Claims deliberately NOT made

- **No claim that gate 5 is now meaningful.** It is capable of failing; it has
  not yet had the opportunity. B09 exists to say exactly that.
- **No claim the pipeline is production-ready.** The frontmatter declines
  RUNNABLE-LIVE and the reel repeats that.
- **No claim that any live, external or model call has run.** None has.
- **No accuracy figure.** `logs/RUN_LOG.md` records that none exists (P3).

## Repo hygiene

The break test was run entirely in the session scratchpad using a replica of
the gate's shell logic. `git status` on mycroft was clean before and after; no
file in the subject repo was created, modified or deleted.
