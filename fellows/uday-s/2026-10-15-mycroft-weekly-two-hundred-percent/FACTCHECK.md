# FACTCHECK - Two Hundred Percent

Status: **GATE F SIGNED - 2026-10-15. 14 rows PASS, 1 discrepancy RECONCILED.**

Subject: `mycroft` @ `d85106b` on `feat/snickerdoodle-cli`, with its companion
`a18d1c1`. `git branch -r --contains HEAD` lists
`origin/feat/snickerdoodle-cli` and `git status -sb` reports the branch in sync,
so this is the last pushed commit.

## Method

Two independent routes, neither of which trusts the commit message:

1. **Ran the committed checker, read-only.**
   `node scripts/snickerdoodle.mjs check --all`. The `check` path reads recipe
   files and script sources, prints a summary, and exits; it has no write path,
   and by design it does not execute the scripts it inspects (it parses
   `add_argument` from source). Its own output is reproduced below.
2. **Counted the committed tree.** `git ls-tree -r d85106b` and
   `git grep -c` at that commit.

The working tree has **2108 files showing modified** (the line-ending
renormalisation from episode 7's commit). Nothing was written to the repository.

## The checker's own output, reproduced

```
recipe/script contract check  ·  97 recipes  ·  616 findings

  FINDING                    OF MEASURABLE   READ AS
  script-missing             94/97            97%  one template-wide defect
  documented-not-built       4/4             100%  one template-wide defect
  built-not-documented       4/4             100%  one template-wide defect
  gate-without-test           1/97             1%  individual recipes
  gate-without-capacity       1/97             1%  individual recipes
  no-steps                    1/97             1%  individual recipes

  Flag findings are scored out of the 4 recipe(s) with at least one script on
  disk - the other 93 have nothing to compare against.

  0 recipe(s) with no mismatches.
```

| # | Beat | Claim | Verdict | How checked |
|---|---|---|---|---|
| 1 | B04, B08 | 97 recipes | PASS | checker output, and `git grep -c` finds the contract in exactly 97 files |
| 2 | B04, B08 | 616 findings | PASS | checker output |
| 3 | B04, B08 | 94 of 97 name scripts that do not exist | PASS | checker output, `script-missing 94/97` |
| 4 | B04 | 0 recipes came back clean | PASS | checker output |
| 5 | B05, B08 | flag findings are 4/4 = 100% | PASS | checker output, both flag rows |
| 6 | B05 | 93 recipes have no scripts on disk to compare | PASS | checker's own note; 4 + 93 = 97 |
| 7 | B05 | scoring 4 out of 97 gives 4% | PASS | arithmetic; 4/97 = 4.1% |
| 8 | B05 | the second attempt gave 4/2 = 200% | PASS (author-reported, reconciled below) | commit body of `d85106b` |
| 9 | B01, B08 | the spec is written 1444 times | PASS | `git grep -c -E 'snickerdoodle (run\|gate)' d85106b -- recipes/` sums to 1444 |
| 10 | B01 | across 97 recipes | PASS | the same grep matches in 97 files |
| 11 | B03 | 582 scripts | NOT USED ON SCREEN | spoken in B03's composer panel as the commit's own reasoning; see note below |
| 12 | B09 | gate refuses: failing test, no note, overwrite without --force, no named human, live without --authorize-live | PASS | commit body of `a18d1c1`, and the behaviour is described in the committed source |
| 13 | B09 | gate 3 reported a failure for a test that passes, because Node's `shell:true` uses cmd.exe on Windows | PASS | commit body of `a18d1c1` |
| 14 | B08 | 99 `.md` files under `recipes/` | PASS | `git ls-tree -r d85106b -- recipes/` counts 99 |

## The discrepancy against episode 7, reconciled on screen

Episode 7 said **99 recipes**. This episode says **97**. Both are right and they
count different things:

- `recipes/` contains **99** `.md` files (episode 7's count, and still 99 today).
- **97** of them carry the Snickerdoodle contract section - the same 97 the
  checker walks, and the same 97 the 1444 occurrences are spread across.

B08 shows this rather than quietly switching numbers. Had the reel used 97
without explanation, a viewer who watched episode 7 would have been right to
distrust both.

## Why 200% is reported but not independently reproduced

The 4/2 denominator belongs to a **discarded intermediate version** of the
summary that was never committed, so it cannot be re-run. It is the commit's own
account and is attributed as such in narration.

It does reconcile arithmetically, which is why it is used: 97 recipes, minus the
94 with at least one missing script, minus the 1 with no steps at all, leaves
**2** recipes with no missing scripts - the denominator that produced 4/2. The
reel states the number; FACTCHECK records that the reconciliation is mine, not
the commit's.

## Figures deliberately kept off screen

- **582 scripts** appears only inside B03's composer panel as the reasoning for
  parsing source instead of running `--help`. A raw count of `.py` under
  `scripts/` at this commit is 642, and 521 excluding the quarantined
  `scripts/mycroft-main/` import - neither is 582, because 582 counts the
  scripts the recipes actually name. Since no single `git` command reproduces
  it, no figure for it appears as evidence anywhere in the reel.

## Precision notes

- **"4%" is 4.1%** and is spoken as "four percent", matching the commit.
- **The three denominators are three attempts at one summary**, not three
  different findings. B05 makes that explicit.
- **"One template defect" is the checker's reading, not a repair.** The reel
  does not claim the template has been fixed - only that 94 instances share one
  cause.
- **`check` exits 1 on findings.** The reel does not claim CI is gated on it;
  the commit says it *can* be, once the template defect is closed.

## Claims deliberately NOT made

- **No claim that the repository is broken.** 616 findings are contract
  mismatches between documentation and code, not runtime failures.
- **No claim that the CLI is finished or verified.** Episode 6's verdict on the
  market-sentiment recipe stands untouched.
- **No performance, security or quality claim** about any script.

## Repo hygiene

Reads only: `git show`, `git ls-tree`, `git grep`, `git rev-parse`,
`git branch -r --contains`, and one read-only run of the committed checker.
No writes, no checkouts, no renormalisation.
