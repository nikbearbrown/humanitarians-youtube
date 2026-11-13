# Where the Improvement Came From

**Type:** Project update (re-analysis of saved pilot runs — no new experiment)
**Fellow:** Maitri P. · **Voice:** Kokoro `af_bella` (Bella), a synthetic narrator — disclosed on the outro card.

## This week's contribution
**Question:** where did the pilot's average improvement actually come from?
**Prediction:** the average suggested procedural memory helped broadly.
**What I did:** a task-by-task **re-analysis of the saved pilot runs** — no new Pi runs. Compared six unseen questions under none / procedural / metacognitive / both on tool calls, errors and evidence validity.
**Observed:** procedural used fewer calls on 4/6 (equal 1, more 1); metacognitive 3 fewer / 3 more; both 2 fewer / 1 equal / 3 more. One task drove much of the average: no memory 12 calls and 2 KeyErrors, against 3 calls and 0 errors with the metacognitive lesson. Without that task the procedural gap shrinks from 1.67 to 0.40 calls per task. All numeric answers were correct; one combined-memory run failed the evidence check.
**Learned:** storing a lesson is only part of the problem — it has to be retrieved when it fits the task; always injecting both memories sometimes added work.
**Next experiment:** repeat with the same frozen memories; then selective retrieval and outdated/conflicting lessons. No general claim yet.

## Human and AI work
**My decisions and verification:** did the task-by-task analysis and wrote the update; approved the narration and the without-outlier comparison.
**AI tools and what they generated:** Claude Code (Anthropic) re-derived every number from the saved run records (read-only), wrote the beat sheet and rendered; it proposed the without-outlier arithmetic (4.80 vs 4.40). Kokoro produced the narration. No Pi run and no API call were made for the film.
**What I rejected or corrected:** see `FRICTIONAL.md`.
**What remains unverified or failed:** see `FACTCHECK.md` — one repetition per condition.

## Reproduce
- **Brutalist toolkit:** commit `6fc9987` **plus local uncommitted changes** (scenes in `scenes/`, Windows fixes). Not yet upstream.
- **Evidence:** `evidence.json` — per-task numbers recomputed from saved runs (no paths, logs or credentials).
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16 native layouts).
- **Checks:** `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`. GATE V: 0 blockers on both aspects.

## Watch and review
- **Landscape** — `PiMemoryTaskReview_MaitriP.mp4` — [Drive Link](https://drive.google.com/file/d/1zxl7Krfp6hWkd0CC0VtDfpQD1Gp-zOPT/view?usp=sharing)
