# FACTCHECK - It Looked Complete

Status: **GATE F SIGNED - 2026-10-22. 10 rows PASS, 1 figure NOT REPRODUCED and
therefore NOT SHOWN.**

Subject: `mycroft` @ `93485c4` on `feat/gate-records`.
`git branch -r --contains HEAD` lists `origin/feat/gate-records` and
`git status -sb` reports the branch in sync, so this is the last pushed commit.
It is the only non-merge commit on the branch.

## Method, and one deliberate restriction

Everything was read from the committed tree with `git show` and `git ls-tree`.

**The `gate` command was NOT run.** Unlike last episode -- where `check` only
reads and prints, so running it was the strongest evidence available -- `gate`
**writes a decision record into the repository**. Running it to confirm a figure
would have put a file in the subject repo for the sake of a video. So the
reel's figures come from counting the tree, and anything that could only be
obtained by running the writer is absent from the frames.

The working tree is now essentially clean (one modified file, `.gitignore`); last
week's 2100-file renormalisation has been resolved upstream.

| # | Beat | Claim | Verdict | How checked |
|---|---|---|---|---|
| 1 | B01 | five fields were absent: evidence_files, evidence_observed, mode, run_log, scope | PASS | commit body, and the field names appear in the diff |
| 2 | B01 | residual_risk was present but a generic default | PASS | commit body |
| 3 | B04 | the evidence list is derived from the gate's own test | PASS | commit body, and the committed source |
| 4 | B04 | gate 3's test names `data/raw/<slug>` and `data/verified/<slug>` | PASS | `git show 93485c4:recipes/market-sentiment-analysis-part-1.md` line 65 |
| 5 | B04 | those two trees hold **26 JSON files** | PASS | `git ls-tree -r 93485c4` - 14 under data/raw, 12 under data/verified, 26 total |
| 6 | B04 | stopping at depth 1 missed them | PASS | the same listing shows 3 and 1 top-level entries; the JSON sits two levels down |
| 7 | B06 | gate 4's test is a `for s in tools/verify-provenance ...` loop, so those tokens are loop values | PASS | commit body |
| 8 | B06 | gate 6's test names a `[DATE]` template | PASS | commit body |
| 9 | B07 | +147 / -3 in `scripts/snickerdoodle.mjs` | PASS | `git show --stat 93485c4` |
| 10 | B08 | `toISOString()` returns UTC and recorded 2026-10-23 for a decision made on the 22nd | PASS | commit body; the commit's own author date is 2026-10-22 22:28 -0400, which is 2026-10-23 02:28 UTC - the offset reproduces exactly |

## The figure that is NOT on screen

The commit says gate 3's evidence went from **2 evidence files to 32**.

- The **2** is clear: the test names two directory paths.
- The **32** does not reproduce. Counting every file under those two trees gives
  **31** - 26 `.json`, 3 `.md`, 2 `.broken` - both in the committed tree and on
  disk. I cannot identify the 32nd item without running `gate`, which writes.

The difference is almost certainly benign (an off-by-one in how the two named
directories themselves are counted). It is **not** presented as an error in the
commit, and it is **not** shown in any frame. B04 uses 26 instead, which is the
figure the commit itself calls out as the point ("missed all 26 JSON files the
gate exists to check") and which reproduces exactly.

This is the difference between last episode and this one: there, an unreproduced
figure was a real, large error and became the falsifiability beat. Here it is a
one-item discrepancy I cannot resolve without writing to the repo, so the honest
move is to use the figure I verified and record the one I did not.

## Figures attributed to the commit, not independently reproduced

B09's post-change checks - all six gates producing distinct evidence sets, the
four refusal paths still holding, `run` and `check` unaffected, `npm run verify`
passing - are the commit's own verification. Confirming them requires running
the writer. They are spoken as the commit's account and the citation strip on
B09 says "the gate writer was not run here".

## Precision notes

- **"Five fields" is five named fields**, not five lines of diff.
- **The date bug is reconstructed, not just quoted.** The commit's author
  timestamp is `2026-10-22 22:28:21 -0400`. In UTC that is `2026-10-23 02:28`.
  A UTC-formatted date field would therefore have written the 23rd, exactly as
  the commit says.
- **26 is JSON files only.** The two trees hold 31 files in total; the gate's
  test selects `-name "*.json"`, so 26 is the number the gate is about.

## Claims deliberately NOT made

- **No claim that the records are now complete** - only that five named fields
  were added and three became observations rather than assertions.
- **No claim that any gate decision changed.** Nothing in this commit re-decides
  anything; episode 6's verdict on the market-sentiment recipe stands.
- **No security claim.** A thin audit record is an evidence problem here, not a
  vulnerability, and the reel does not dress it as one.

## Repo hygiene

Reads only: `git show`, `git ls-tree`, `git rev-parse`, `git status`,
`git branch -r --contains`, and a `find` over two directories. **No command that
writes a record was executed.** Nothing was written to the repository.
