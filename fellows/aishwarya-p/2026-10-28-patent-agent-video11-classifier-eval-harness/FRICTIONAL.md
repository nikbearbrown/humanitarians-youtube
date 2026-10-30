# Frictional Log — patent-agent-video11-classifier-eval-harness (Video 11)

Written 2026-10-29 from this folder's records.

## 2026-10-27 — Measuring the classifier instead of reading outputs

- **Work and expectation:** a way to tell whether "every result is narrow/defensive" comes from the patents or from the prompt.
- **What was done:** Claude wrote `eval_classifier.py`, which reports accuracy, Cohen's kappa, a majority baseline and a collapse check.
  - Without `--yes` it only prints a cost estimate.
  - It was tested offline with mock classifiers first. The constant mock fired both collapse warnings at κ 0.00, and the oracle scored 1.00.
- **Contributions:** Aishwarya set the rule that nothing costing money runs without her approval, and declined to copy the harness into the mycroft repo at that stage.
- **Record:** `eval_classifier.py` (created 2026-10-27), later [mycroft 3bcf1b1](https://github.com/nikbearbrown/mycroft/commit/3bcf1b1cea28265bb89bfea85f4034b6b7da37f0).

## 2026-10-27 — One query instead of sixteen

- **Work and expectation:** about 50 independent claims from 8–10 patents.
- **Where it resisted:** the patents table isn't partitioned, so a query is billed for every byte of each column it touches. One patent costs about as much as 160.
- **What was done:** `pull_eval_claims.py` dry-runs first, then caps the real job at 1.05× the dry-run bytes.
  - One query pulled 160 candidates: 161.8 GB, $0.92 at list price.
  - It ran once, after Aishwarya approved it.
- **Record:** `pull_eval_claims.py`, `eval/claims_pool.jsonl` (both 2026-10-27), `PEDAGOGY.md`.

## 2026-10-27 — The data didn't fit the plan

- **Where it resisted:** the first selection yielded only 36 claims. 147 of the 160 patents have 1–3 independent claims, not the assumed ~5.
- **What was done:** Aishwarya chose to re-select from the cached pool with no new query. The result was 50 claims from 16 patents, 2 per CPC section.
  - HTML entities in the claim text (`&#39;`) were also found and unescaped.
- **Record:** `eval/labeled_claims.csv`, `NARRATION.md` B03.

## 2026-10-27 — Narration that matched the data

- **Where it resisted:**
  - A spot-check count in the draft cold open wasn't consistent with earlier videos.
  - The scan size was given in GiB while everything else used GB.
- **Contributions:**
  - Aishwarya removed the count ("every result came back narrow and defensive").
  - She asked for one sentence explaining kappa.
  - She asked for 16 versus 160 to be made clearer.
  - She asked for one unit, so everything now uses decimal GB (161.8 GB).
- **Record:** `NARRATION.md`, `PEDAGOGY.md`, Friction protected.

## 2026-10-27 — The short

- **Where it resisted:**
  - `shorts.py` auto-dropped B03 and garbled the outro.
  - The channel handle overlay caused an edge-bleed BLOCKER in portrait.
- **Contributions:**
  - Aishwarya chose to drop B00A instead and keep the original outro.
  - She chose to remove `channel_title` from the short's beat sheet only, leaving `compile.py` unchanged.
- **Record:** `short/beat_sheet.json` in the build folder.

## Understood and open

- Labeling was paused for project lead review, so this folder has no accuracy number.
- Requiring 3+ independent claims per patent may skew the set toward broadly drafted patents.

## Process note

The video folder was committed and merged on 28 October ([PR #308](https://github.com/nikbearbrown/humanitarians-youtube/pull/308)). The harness scripts stayed local until the 29 October mycroft commit, [PR #76](https://github.com/nikbearbrown/mycroft/pull/76). This log is late.
