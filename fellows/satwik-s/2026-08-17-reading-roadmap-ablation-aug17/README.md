# Weekly Research Report: What an Ablation Can (and Can't) Decide — Full-Book Tagging

**Fellow:** Satwik Reddy Sripathi
**Week ending:** August 16, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** See `output/reading-roadmap-ablation-fullbook/SOURCES.md`, and the frozen sources `sources/week3_progress_report.md`, `sources/week3_tagging_results.md` (PRIMARY), `sources/week3_gold_set.md`, and `sources/week3_prerequisites.md`.
**Source status:** This video reports a completed **full-book** tagging ablation (all 1,340 sections). It does **not** name a "correct" tagger — the gold set is **being built and graded, not yet scored**. The prerequisite ordering is **dormant** (0 edges). The gold-set score and any learning-outcome evaluation are future work, not completed results.

This weekly research video asks:

**What can an ablation actually decide — and what can't it?**

The video answers with a **reusable, four-question framework**, then walks the full-book tagging ablation through it: is each option reproducible? does the choice *matter*, measured downstream? where do the two differ, per field, with the sample size in view? and — the ceiling — which one is *correct*? The conclusion is delivered with its limit shown: an ablation can prove the choice is reproducible, that it matters, and where the options differ, but it **cannot** say which is correct; that needs ground truth.

The final beat sheet contains **10 beats**. The complete video was generated locally using Brutalist, compiled at 1080p, reviewed end to end (including a PROOF skeptical-explainer pass), and prepared separately for submission.

## Production state

- Premise / reusable-framework gate (PROOF Phase 1): completed (`PREMISE.md`)
- Plan and beat structure: completed
- Narration generation: completed (Kokoro `af_bella`, run under `PYTHONUTF8=1`)
- Audio timing: completed (measured durations are the clock; total ≈ 3:22)
- Visual beats: 10 of 10 filled (`ReadingRoadmapsAblation2.tsx`)
- Local compilation: completed (1080p)
- Full-video review + PROOF production gate: completed (teaching 12/12; gate PASS)
- Formal claim-level fact-check: figures traced to `SOURCES.md`; requires final human sign-off before publication
- YouTube publishing: handled separately through the Humanitarians AI review process

## Deliverables

| File (`output/reading-roadmap-ablation-fullbook/`) | Aspect | Resolution | Duration |
|---|---|---|---|
| `reading-roadmap-ablation-fullbook.mp4` | 16:9 | 1920×1080 | 3:22 |

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## What this video is about

**Topic:** The tagging ablation, run on the full 1,340-section book — and the honest ceiling of the method.

Week-02 ran the tagger ablation on a 60-section sample; its strongest number rested on **n≈4** and promised a denser re-run. This week delivers that re-run on the **whole book** (materials agreement now **0.919 on n=102**), adds the **downstream** effect on the actual roadmap, and — crucially — names what an ablation **cannot** decide.

## Central question

> An ablation isolates one component. What questions can it honestly answer — reproducibility, whether the choice matters, and where two options differ — and which question (which is *correct*?) can it not answer without ground truth?

The proposed answer is the four-question framework, with the fourth question explicitly flagged as the ceiling.

## Main ideas presented (10 beats)

1. Last week's strongest number rested on four sections; this week runs the ablation on the whole 1,340-section book.
2. The four questions — reproducible? / does it matter (downstream)? / where do they differ (per field, with n)? / which is correct? — shown before any result; the fourth is flagged unanswerable by ablation.
3. Reproducible? The dictionary is exact (**1.000**); the open model near-exact (**~0.99**) at temperature 0. On the full book the dictionary tags all sections in ~12 s (free, offline) vs ~5 h 27 min on a GPU — roughly **1,600×** faster.
4. Does it matter? Measured **downstream**, not at the tagger: swapping the tagger changes **~74%** of a student's reading list (roadmap Jaccard **0.257**); the model promotes far more sections to `core` (LNP 13 → 23).
5. Where do they differ? Field by field, with **n**: materials **0.919 (n=102)** — up from last week's n=4 — down to concepts 0.296 (n=755); the model over-tags the fuzzy fields.
6. Which is correct? The ceiling: reproducibility and agreement only compare the two backends to each other; agreeing at 0.92 doesn't make either right.
7. To say which is more correct you need ground truth the ablation doesn't have.
8. So a gold set is being built — 20 sections, 333 tags (191 literally present, 142 model-inferred), graded blind by two independent graders — to decide dictionary / model / hybrid.
9. It is **still being graded** — no winner yet.
10. Alongside it, one human step remains: faculty approving the read-A-before-B links (26 proposed, 0 edges today) that would switch ordering on.

## Current implementation boundary

The study establishes **reproducibility, a downstream effect, and per-field agreement** for the full-book tagging step. It does **not** name a correct tagger, and it makes no learning-outcome claim.

The result should be understood as follows:

- the dictionary is *exactly* reproducible and far cheaper/faster; the model is *near*-reproducible;
- the tagger choice **matters** — 74% of the reading list turns over — but that is divergence, not accuracy;
- agreement is highest on the load-bearing field (materials, n=102), yet agreement ≠ correctness;
- the gold set is **in progress**; the ordering is **dormant** (0 edges; 26 proposed links awaiting faculty).

Future work: the gold-set score (to name a correct tagger); faculty approval of the prerequisite links; any learning/engagement claim.

## The reusable method (apply it to a new case)

For any "simple vs. fancy" component choice, ask four questions — and stop at the ceiling:

1. **Reproducible?** run it K times; is the answer stable?
2. **Does it matter?** measure the effect *downstream*, not at the component you swapped.
3. **Where do they differ?** per field/metric, always with the sample size `n`.
4. **Which is correct?** — you can't answer this from the ablation; build a gold set.

Decision rule: an ablation tells you *whether to care* and *where to look*; it does not crown a winner. Keep the cheap default while the ablation runs; use a gold set to actually pick.

## How faculty review is used

Faculty grade the gold set (with a second independent grader) to establish the ground truth the ablation lacks, and approve the proposed prerequisite links that would activate ordering. Both are in progress this week; the video renders them as pending, never as results.

## Research prompt

> Research "What an Ablation Can (and Can't) Decide — Full-Book Tagging." Begin with `sources/week3_tagging_results.md` (PRIMARY), `sources/week3_progress_report.md`, `sources/week3_gold_set.md`, `sources/week3_prerequisites.md`, `SOURCES.md`, and `beat_sheet.json`. Identify the four-question framework, reproducibility (1.000 vs ~0.99; ~1,600×), the downstream 74% (roadmap Jaccard 0.257), the per-field agreement with n (materials 0.919, n=102 … concepts 0.296, n=755), the ceiling (agreement ≠ correctness), and the in-progress gold set + dormant ordering. Return a claim table: claim, exact source, evidence, confidence, what still requires verification. Do not name a correct tagger, do not report any precision/recall/F1, and never show an agreement number without its n.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `week3_tagging_results.md` and `SOURCES.md`. Produce a verdict table (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED) with evidence, source, and correction. Pay attention to: 1.000 vs ~0.99, the ~12 s vs ~5 h 27 min / ~1,600× figures, the 74% downstream (0.257), every per-field agreement with its n, and the "ceiling" framing. Flag any agreement number shown without n, any claim naming a correct tagger or citing precision/recall/F1, and any framing of divergence as "the model is wrong." List corrections for human review.

## Typical commands

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/ablation-fullbook"
PYTHONUTF8=1 python runtime/scripts/remotion_scenes.py "/abs/path/to/ablation-fullbook"
PYTHONUTF8=1 python runtime/scripts/compile.py "/abs/path/to/ablation-fullbook" --height 1080
```

## Beat-sheet and visual rules

- Treat `beat_sheet.json` as the source of truth; audio duration is the timing clock.
- Show the four-question framework **before** any result; flag question four as the ceiling.
- **Show n** with every agreement number; put comparisons side-by-side, held ≥2s.
- Render the gold set and prerequisite review as **in-progress / pending**, never as results.
- Frame divergence as "the choice matters" (74% downstream), not "the model is wrong."

## Voice and narration

Kokoro `af_bella` ("Bella"); greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration before generating audio; regenerate + remeasure whenever narration changes; on Windows run audio/render/compile under `PYTHONUTF8=1`.

## Useful project files

- `PREMISE.md` — the four-question framework + falsifiability (the ceiling) + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures with n; what must not be claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric (teaching 12/12)
- `VISUAL-PLAN.md` — per-beat visual treatment + legibility contract
- `beat_sheet.json` — narration, timing, props, build state
- `remotion-src/ReadingRoadmapsAblation2.tsx` — reel-local components
- `_qc/REPORT.md` — frame-level QC + PROOF production-gate result
- final `.mp4` — the 1080p master

## Build result for this report

The reviewed local build produced 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`); a synchronized 1080p compilation, runtime ≈ 3:22; and a complete human review plus a PROOF pass (teaching 12/12; production gate PASS). The expected `illustrate` motion-distribution warning (6 of 10 beats) is acceptable for a six-body-beat explainer.

## Current limitations

- the ablation compares the two backends only to each other — **no gold standard**, so no correctness claim;
- agreement numbers depend on field density; small-n fields are less robust (n shown throughout);
- the ~1% model drift is hardware/runtime dependent (the architectural point holds; the figure is not portable);
- single model (`qwen2.5-coder:7b`, temp 0); ordering dormant (0 edges); no learning/engagement claim.

## Future work

- the gold-set score → name a correct tagger (delivered the following week);
- faculty approval of the 26 prerequisite links → activate ordering;
- broader validation across models and samples; an outcome/engagement study.

## Final human checklist

- Can a new viewer state the four questions and apply them, stopping at the ceiling?
- Does every agreement number show its **n** (materials 0.919 · n=102, etc.)?
- Is "does it matter?" measured **downstream** (74% / 0.257), not at the tagger?
- Is question four shown as unanswerable by ablation (needs ground truth)?
- Are the gold set and ordering shown as in-progress, never as results?
- Did a human watch the complete output and complete at least one refinement pass?
- Has an authorized human reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it as an unlisted video and add it to the appropriate playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
