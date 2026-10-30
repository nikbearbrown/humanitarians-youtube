# Frictional Log — patent-agent-video12-baseline-results (Video 12)

**Written on 2026-10-29**, the same day as the work, with Claude, from that day's Claude Code session and this folder's records. It was written after the work rather than during it. Awaiting Aishwarya's review. Each entry names the record it comes from.

## 2026-10-29 — Labels the harness couldn't read

- **Work and expectation:** the harness reads the 50 hand labels and estimates the cost.
- **Where it resisted:** six posture cells had an explanation typed after "defensive". The harness only accepts the three labels.
- **What was done:**
  - Aishwarya approved setting those six cells to `defensive` and moving each explanation into `label_notes`.
  - A backup copy of the file was kept.
- **Record:** `eval/labeled_claims.csv`.

## 2026-10-29 — The baseline, and a set that can't measure posture

- **Work and expectation:** a first accuracy number, after a $0.32 upper-bound estimate that Aishwarya approved.
- **Result:**
  - Breadth: accuracy 0.66, κ 0.08.
  - Posture: accuracy 0.60, κ 0.00.
  - Both fall below the always-most-common-answer baseline.
- **Where it resisted:** the labels are 46 narrow / 4 broad and 50 defensive. A model that always says "defensive" would score 100%, so this set can't measure posture agreement.
- **Understood and open:** the classifier leans broad/offensive on functional claim wording, the opposite of the earlier suspicion. The set needs offensive and broad examples.
- **Record:** `eval/runs/baseline_report.md`, [mycroft 3bcf1b1](https://github.com/nikbearbrown/mycroft/commit/3bcf1b1cea28265bb89bfea85f4034b6b7da37f0).

## 2026-10-29 — A wrong guess about the bug

- **Where it resisted:** two claims on one grinding-process patent returned cut-off JSON.
  - Claude guessed the 500-token limit was the cause. Aishwarya approved raising it, and the retry failed earlier than before.
  - Claude then guessed thinking tokens. That was also wrong.
- **What was done:** Aishwarya approved one diagnostic call, about $0.003. It showed `stop_reason: "refusal"` partway through the answer, at 155 of 1000 tokens, with no thinking.
  - The code had only handled empty refusals.
  - It now treats any refusal as declined, and `max_tokens` is back at 500.
  - The two cached errors were re-scored offline with no new calls.
- **Understood and open:**
  - The refusal is handled, but its cause on that patent isn't known.
  - Claim 5's refusal is inferred from the matching failure, not tested directly.
- **Record:** `claim_classifier.py` diff in [mycroft 3bcf1b1](https://github.com/nikbearbrown/mycroft/commit/3bcf1b1cea28265bb89bfea85f4034b6b7da37f0).

## 2026-10-29 — Committing to mycroft

- **Where it resisted:** `git pull` aborted because of an uncommitted local `.gitignore` edit, so the new branch was first cut from a `main` 48 commits behind.
- **What was done:**
  - The edit was set aside and the branch recreated on the current `origin/main`.
  - The edit was restored, with upstream's lines kept.
  - Aishwarya reviewed the commit command before it ran.
- **Record:** [PR #76](https://github.com/nikbearbrown/mycroft/pull/76).

## 2026-10-29 — The video

- **Contributions:**
  - The brief gave the cost as $0.32. The narration says "at most thirty-two cents", because actual usage wasn't recorded.
  - Aishwarya approved keeping the all-defensive caveat on screen.
  - A card overlap in portrait B03 was found by frame check and re-spaced.
- **Record:** `NARRATION.md`, `PEDAGOGY.md`, [humanitarians-youtube 7c165d76](https://github.com/nikbearbrown/humanitarians-youtube/commit/7c165d76550648aecfaf4e411ee6d1c1bf7260cf).

## Process note

The eval code, labels and baseline results were committed to mycroft on the day of this work (PR #76). The video folder was committed and merged the same day ([PR #319](https://github.com/nikbearbrown/humanitarians-youtube/pull/319)).
