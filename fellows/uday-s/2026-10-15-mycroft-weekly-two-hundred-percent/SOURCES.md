# SOURCES - Two Hundred Percent

Single-source reel. Everything comes from the `mycroft` repository at `d85106b`
and its companion `a18d1c1`, both on `feat/snickerdoodle-cli`. No web sources.

| On screen | Beat | Where it came from |
|---|---|---|
| the documented snickerdoodle commands | B01 | the Snickerdoodle section every recipe carries |
| 1444 occurrences across 97 recipes | B01, B08 | `git grep -c -E 'snickerdoodle (run\|gate)' d85106b -- recipes/` |
| "the command had never existed" | B01 | commit body of `a18d1c1` |
| 97 recipes / 616 findings / 94 of 97 / 0 clean | B04, B08 | `node scripts/snickerdoodle.mjs check --all`, run read-only |
| 4/97, 4/2, 4/4 | B05 | the checker's summary, plus the commit body for the discarded 4/2 attempt |
| 93 recipes with nothing to compare | B05 | the checker's own footnote |
| the denominator comment | B06 | `git show d85106b:scripts/snickerdoodle.mjs` |
| the five gate refusals | B09 | commit body of `a18d1c1`, and the committed source |
| the cmd.exe gate-test bug | B09 | commit body of `a18d1c1` |
| 99 .md files under recipes/ | B08 | `git ls-tree -r d85106b -- recipes/` |

## Running the checker was itself the verification

Unusually for this series, the artifact under examination is a measuring
instrument, so the honest check was to run it rather than re-implement it. That
is safe here for a specific reason the commit itself argues: `check` parses
`add_argument` out of source instead of executing each script with `--help`,
because "executing a file to learn what it accepts is a side effect a checker
should not need". So running the checker reads files and prints; it does not run
the 582 scripts it inspects, and it does not write.

Episode 7 re-implemented the thing it was measuring because the subject was a
skip rule with two versions to compare. Here there is one version and it is
executable, so the stronger evidence is its own output.

## What the checker could not settle

The 4/2 = 200% denominator was an intermediate version that was never committed.
It cannot be re-run, so it is the commit's account. The arithmetic reconciles
(97 - 94 with a missing script - 1 with no steps = 2), and FACTCHECK.md records
that this reconciliation is mine.

## Claims NOT sourced here, and therefore not made

- Nothing about whether any script is correct - only about whether the recipe
  and the script agree on what exists and what flags are accepted.
- Nothing about CI being gated on `check` today.
- No comparison to any other repository or tool.
