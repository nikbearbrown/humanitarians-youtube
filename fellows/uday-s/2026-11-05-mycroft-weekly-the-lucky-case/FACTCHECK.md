# FACTCHECK — The Lucky Case

Status: **GATE F SIGNED — 2026-11-05. 12 rows PASS, including one mechanism
REPRODUCED STANDALONE rather than quoted.**

Subject: `mycroft` @ `0358ab9` on `chore/recipe-lifecycle-frontmatter`.
`git branch -r --contains HEAD` lists `origin/chore/recipe-lifecycle-frontmatter`
and `git status -sb` reports the branch in sync, so this is the last pushed
commit.

**Note on history:** the branch was rebased since last week. Episode 10's subject
commit is now `6f10055` (was `6428457`); same content, new hash. Nothing in this
episode depends on the old hash.

## Method

Three read-only routes:

1. **Ran the committed checker** — `node scripts/snickerdoodle.mjs check --all`
   and `check gru`. `check` reads and prints; it has no write path. (`gate`
   writes a record and has not been run since episode 9.)
2. **Counted the committed tree** — `git show`, `git ls-tree`, `git grep`.
3. **Reproduced the argparse mechanism in a standalone interpreter**, with
   nothing from the repository imported or executed.

## Verified claims

| # | Beat | Claim | Verdict | How checked |
|---|---|---|---|---|
| 1 | B01 | the Flags column is consumed by `snickerdoodle run`, not just read by people | PASS | commit body, and the runner's behaviour described in the committed source |
| 2 | B04 | `run scenariostresstestingagent --step validate-data-shape --sample` fails with `error: argument --sample-dir: expected one argument` | PASS | commit body — and the error text is reproduced independently, below |
| 3 | B05 | passing `--sample` alone makes argparse prefix-match `--sample-dir` and demand its value | **PASS — reproduced standalone** | a two-argument `ArgumentParser` in a fresh interpreter produced exactly `error: argument --sample-dir: expected one argument` |
| 4 | B05 | passing `--sample` followed by a non-flag token makes argparse silently absorb that token as the flag's value | **PASS — reproduced standalone** | `parse_args(["--sample", "data/real.json"])` gave `sample_dir='data/real.json'`, `input=None` — no error raised |
| 5 | B06 | all six built recipes carried the same `--sample --no-write` boilerplate | PASS | commit body; the six recipes are the six touched by the diff |
| 6 | B06 | 24 table rows reconciled, one for one | PASS | `git show --unified=0 0358ab9 -- recipes/` — 24 lines matching `^+\|` and 24 matching `^-\|` |
| 7 | B06 | unbuilt steps were left alone | PASS | commit body; the diff touches only the six built recipes |
| 8 | B07 | the 6 built recipes name 82 scripts, of which 70 exist on disk | PASS | parsed the `scripts/...py` paths from the six recipes at this commit and tested each against `git ls-tree` |
| 9 | B07 | none of those 70 imports a network library | PASS | searched each of the 70 for `import`/`from` of requests, urllib, urllib3, httpx, aiohttp, socket, http.client, websockets — zero hits |
| 10 | B07 | a repo-wide search finds 9 scripts that do, none among the 70 | PASS | same pattern over `scripts/`, excluding the quarantined `mycroft-main` tree — 9 hits, all under `scripts/ingest/`, none in the 70-script set |
| 11 | B08 | the attestation is voided, version bumped to 0.2.1, record kept with the voiding appended | PASS | recipe frontmatter reads `attestation: null  # v0.2.0 record voided by the v0.2.1 flag-table correction` and `recipe_version: 0.2.1`; the diff appends a "Voided — 2026-11-05" section to the v0.2.0 file rather than deleting it |
| 12 | B09 | 5 defects remain, all in `recipes/gru.md`; 96 of 97 recipes clean | PASS | `check --all` reports 97 recipes, 5 defects, 96 clean; `check gru` lists exactly 5 |

## The one figure I checked against the wrong list first

Searching `scripts/` repo-wide for network imports returns **9** files, all
under `scripts/ingest/`. That number is real but answers a different question
than the commit's claim, which is about the **70 scripts the six built recipes
actually name**. Parsing those 70 and checking each gives **0**.

This is the same distinction that went wrong in episode 10, where my own `grep`
over `recipes/` returned 98 against the checker's 97. B07 shows both numbers and
says which question each answers, rather than quietly using the one that agrees.

## Figures from the commit that are NOT independently reproduced

- **"85 defects"** before the change. The pre-change state cannot be re-measured
  without reverting the commit, so this is the commit's own figure. The **5**
  after is reproduced. B09 shows both and the citation strip names the command
  that produces the second.
- **The two external endpoints "rendered as approval-required handoffs and never
  called"** — stated in the commit body and not independently traced. It does
  not appear on screen; only the 0-of-70 result does.

## Precision notes

- **B05's two cases are not the same severity and the beat says so.** Case A is
  a crash. Case B requires the next token to be non-flag-like — argparse refuses
  to consume something beginning with `-` as a value — and the reel's example
  uses a path, which is the realistic shape.
- **"24 rows" counts table lines changed**, and the 1:1 ratio (24 added, 24
  removed) is what establishes that rows were corrected rather than added or
  dropped.
- **"70 built scripts" is scripts that exist**, out of 82 named. The 12
  difference are named-but-absent, which is the `script-missing` class from
  earlier episodes and is not a defect at DRAFT.
- **The attestation's point 5 was shown in episode 6.** The quotation in B08 is
  the rule as the attestation states it, which is why the voiding is on schedule
  rather than a surprise.

## Claims deliberately NOT made

- **No claim that the recipes are now correct**, only that the Flags column
  matches the implementations for built steps.
- **No claim about `gru.md` being bad.** Its five findings are reported as they
  are: a recipe with no steps and two under-specified gates.
- **No claim that anything was ever run live.** The 0-of-70 result is the
  evidence that it could not have been.

## Repo hygiene

Reads only, plus one standalone Python process that imported nothing from the
repository. No command that writes a record was executed. Nothing was written to
the repository.
