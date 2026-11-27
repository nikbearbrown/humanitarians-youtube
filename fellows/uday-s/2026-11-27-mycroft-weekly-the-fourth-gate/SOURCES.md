# SOURCES — The Fourth Gate

Two places only: the mycroft repository at a named commit, and a scratch folder
outside it where every gate test was re-run against planted defects.

## Primary — the repository (read-only)

| # | Source | Access | Used for |
|---|---|---|---|
| 1 | `D:\Projects\mycroft` @ `20795b2`, branch `chore/promote-scenariostresstestingagent` | local, read-only (`git show`, `git ls-tree`) | the whole reel |
| 2 | `recipes/scenariostresstestingagent.md` @ `20795b2` | `git show` | B04 gate tests verbatim; B06 gate 4; the `[TODO: DEV]` counts |
| 3 | the commit message of `20795b2` | `git log -1` | B01 the self-reported weaknesses; B07 the claim being corrected |
| 4 | `logs/RUN_LOG.md` entry for 2026-11-27 | `git show` | B01, B07, B09 |
| 5 | `data/verified/scenariostresstestingagent/{clean,defective}/validated.json` | `git show` | B08 the two corpora |
| 6 | `logs/scenariostresstestingagent/*-results.json` (4 files) | `git show` | B08 self-test totals; B07 the skipped-count difference |
| 7 | status frontmatter of all 99 `recipes/*.md` @ `20795b2` | `git show` per file | B08 the 94 / 3 / 97 count |
| 8 | `session-handoff.md`, `status.md` diffs | `git show` | B09 the changed next action |
| 9 | `scripts/snickerdoodle.mjs` @ `20795b2` | `git show` | established that the CLI does not execute gate tests (recorded, not shown) |

## Reproduction — a scratch folder, outside the repository

| # | What | Used for |
|---|---|---|
| 10 | gate 1's shape (`test -f … && grep … \|\| true`) against three cases: pattern present, pattern absent, file missing | B05 |
| 11 | gate 3's shape (`find … -exec python -m json.tool`) over a folder holding one deliberately invalid JSON file | B05 |
| 12 | gate 6's shape (`test -f …-[DATE].json`) beside a real dated file | B05, B07 |
| 13 | gate 4's shape against a file containing **only** the gate definition line, with no script on disk and no real TODO entries | B06 |

Fixtures were written to the session scratchpad. Nothing was written into
`D:\Projects\mycroft`.

## Not run, on purpose

- `snickerdoodle gate` — writes a decision record.
- `snickerdoodle run` — writes outputs.
- `npm run verify` / `conformance.mjs` — compiles Python, leaves `__pycache__`.

This is why the reel reproduces the gate *shapes* in a scratch folder rather
than executing the repository's own gates.

## Not used

No external source. This is a work report about one commit in one repository.
