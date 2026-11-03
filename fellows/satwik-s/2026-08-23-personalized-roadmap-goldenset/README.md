# Weekly Research Report: Which One Is Right? Scoring Taggers Against a Gold Set

**Fellow:** Satwik Reddy Sripathi
**Week ending:** August 22, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** See `output/reading-roadmap-gold-verdict/SOURCES.md`, the frozen sources `sources/week4_video_numbers.md`, `sources/gold_scoring.md`, `sources/week4_gold_set.md`, and `sources/week4_tagging_results.md`.
**Source status:** This video reports the gold-set tagger verdict as **provisional — grader 1 only**; a second independent blind grading and reconciliation are pending. The ordering/dependency step remains **dormant** (0 authoritative prerequisite edges). Any learning-outcome evaluation is future work, not a completed result.

This weekly research video asks:

**When agreement can tell you a component choice *matters* but not which option is *correct*, how do you actually decide — honestly — which one is right?**

The video answers with a **reusable, four-step scoring method**, then walks the tagging gold set through it: build a **blind** gold set (a human grades each tag against the text, blind to which tagger produced it), score **precision and recall** per field, **read the split** rather than the combined F1, and **trace where each tag came from**. The conclusion — provisionally, the deterministic dictionary is the more correct tagger — is delivered with its limits shown: it rests on **one grader**, and the "hybrid" expectation is **rejected**, not confirmed.

The final beat sheet contains **10 beats**. The complete video was generated locally using Brutalist, compiled at 1080p, reviewed end to end (including a PROOF skeptical-explainer pass), and prepared separately for submission.

## Production state

- Premise / reusable-framework gate (PROOF Phase 1): completed (`PREMISE.md`)
- Plan and beat structure: completed
- Narration generation: completed (Kokoro `af_bella`, run under `PYTHONUTF8=1`)
- Audio timing: completed (measured durations are the clock; total ≈ 3:52)
- Visual beats: 10 of 10 filled (`ReadingRoadmapsGoldVerdict.tsx`)
- Local compilation: completed (1080p)
- Full-video review + PROOF production gate: completed (teaching 12/12; gate PASS)
- Formal claim-level fact-check: figures traced to `SOURCES.md`; requires final human sign-off before publication
- YouTube publishing: handled separately through the Humanitarians AI review process

## Deliverables

| File (`output/reading-roadmap-gold-verdict/`) | Aspect | Resolution | Duration |
|---|---|---|---|
| `week4_reading-roadmap-gold-verdict_aug23.mp4` | 16:9 | 1920×1080 | 3:52 |

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## What this video is about

**Topic:** Choosing the metadata tagger with a human-graded gold set — precision, recall, and provenance.

Week-03 established the **ceiling** of an ablation: reproducibility and agreement only compare the two taggers to each other, so they cannot say which is *correct*; that requires ground truth. This week that ground truth is in. A **gold set** — sections graded by hand against the text — lets both taggers (the deterministic **dictionary** vs. a pinned open **model**) be scored on precision and recall, and turns "which is right?" into a method a viewer can reuse.

## Central question

> Agreement proves the tagger choice *matters*; only a blind gold set says which is *correct*. How do you build and read that gold set — with the grader count and the precision/recall split in view — so the winner is defensible?

The proposed answer is to grade blind, score precision and recall (not just F1), read the split to name the failure mode, and trace which system's unique outputs are actually correct — reporting how many graders stood behind the result.

## Main ideas presented (10 beats)

1. Last week's ceiling: an ablation can't say which tagger is correct; that needs ground truth.
2. The four-step method: build a **blind gold set** · score **precision & recall** · **read the split** · **trace provenance** — shown before any result (framework-first).
3. The gold set: **20** content-bearing sections, **333** tags to grade (materials, techniques, mechanisms); **191** literally present in the text, **142** model-inferred; graded blind; a second grader grades independently.
4. Field-by-field F1 (rule vs model): materials **1.00 vs 0.27**, techniques **0.92 vs 0.37**, mechanisms **0.80 vs 0.37**.
5. Overall: dictionary **F1 0.89** (P 0.87 / R 0.91) vs model **F1 0.35** (P 0.34 / R 0.36) — the dictionary wins every field.
6. Read the split: the going-in hypothesis was "dictionary = precision, model = recall → a hybrid wins."
7. Ground truth rejects it — the model loses **recall too** (0.36 vs 0.91), so there is no recall advantage to harvest; this round, the hybrid idea is dead.
8. Trace provenance: where both taggers agreed, tags were correct **94%** (50/53); rule-only tags **85%** (117/138); model-only tags **12%** (17/142).
9. The model isn't surfacing real tags the lexicon missed — it is mostly adding wrong ones; that single row *is* the verdict.
10. The honest catch: this is **one grader**. The verdict is provisional until a second blind grading reconciles; and the ordering step is still pending (0 edges, one faculty sign-off away).

## Current implementation boundary

The study establishes a **precision/recall verdict** for the tagging step against a human-graded sample. It is **provisional (grader 1)** and does not yet claim a final, reconciled result; it makes no learning-outcome claim.

The result should be understood as follows:

- the winner (dictionary) is decided on **one grader's** blind grading; a second grader is pending;
- the "hybrid" outcome is **rejected this round**, not adopted — the model wins neither precision nor recall;
- the two "333" splits are distinct axes: **191 literal / 142 inferred** (present-in-text vs inferred) ≠ **184 kept / 149 rejected** (grader yes/no);
- the ordering/dependency step is **dormant** (0 prerequisite edges).

The following require additional evaluation or remain future work: the second independent grading + reconciliation → final tagger verdict; faculty approval of the prerequisite links; validation across more sections/models; any learning/engagement claim.

## The reusable method (apply it to a new case)

A viewer can run the same four steps on any "which option is more correct?" question:

1. **Build a blind gold set** — grade against the source; hide which system produced each item.
2. **Precision & recall** — per category, not just the combined F1.
3. **Read the split** — precision ↔ recall names the failure mode (over-tagging vs missing) and tests your hypothesis.
4. **Trace provenance** — which system's unique outputs are actually correct?

Decision rule: agreement can't crown a winner; a blind gold set can — and report the grader count. A good result is a winner backed by ground truth with its failure mode named; a bad result is crowning a winner from F1 alone, or from a single grader stated as final.

## How faculty review is used

Faculty (and a second independent grader) resolve what one grader cannot finalize: the blind grading is reconciled between two graders before the verdict is called final. Separately, faculty approval of the proposed prerequisite links remains the step that would switch the ordering on (still 0 edges this week).

## Research prompt

> Research "Which One Is Right? Scoring Taggers Against a Gold Set." Begin with `sources/week4_video_numbers.md`, `sources/gold_scoring.md`, `sources/week4_gold_set.md`, `SOURCES.md`, and `beat_sheet.json`. Identify the blind gold set (20 sections, 333 tags; 191 literal / 142 inferred), the per-field and overall F1 (0.89 vs 0.35), the precision/recall split (0.87/0.91 vs 0.34/0.36), the provenance breakdown (94/85/12), why the "hybrid" hypothesis is rejected, and the provisional (one grader) status. Return a claim table: claim, exact source, pinpoint evidence, confidence, and what still requires verification. Do not invent scores, precision/recall/F1 numbers, or a final verdict. Never present the verdict as final while it rests on one grader, and never adopt "hybrid" as the outcome.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `gold_scoring.md`, `week4_video_numbers.md`, and `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and correction. Pay attention to: the F1 figures (0.89 vs 0.35 and per field), the P/R split, the provenance 94/85/12, the two distinct 333 splits (191/142 vs 184/149), the "hybrid rejected" framing, and the provisional-one-grader label wherever F1 appears. Flag any figure shown as final, any use of F1 without the split, and any adoption of "hybrid" as a conclusion. List corrections for human review.

## Typical commands

Run from the Brutalist toolkit root. On Windows, prefix Python with `PYTHONUTF8=1`; use the toolkit venv Python for Kokoro.

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/gold-verdict"
PYTHONUTF8=1 python runtime/scripts/remotion_scenes.py "/abs/path/to/gold-verdict"
PYTHONUTF8=1 python runtime/scripts/compile.py "/abs/path/to/gold-verdict" --height 1080
```

## Beat-sheet and visual rules

- Treat `beat_sheet.json` as the source of truth; audio duration is the timing clock.
- Show the four-step framework **before** any result (framework-first).
- Show **precision and recall with F1** — never F1 alone; the split is the teach. Put comparisons side-by-side, held ≥2s.
- Mark the verdict **provisional (grader 1)** wherever the F1 appears; render the gold set / ordering as in-progress, never as a final result.
- Do not conflate the two 333 splits; do not adopt "hybrid" as the outcome.

## Voice and narration

Kokoro `af_bella` ("Bella"), recorded in `beat_sheet.json`; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration before generating audio; regenerate + remeasure whenever narration changes; on Windows always run audio/render/compile under `PYTHONUTF8=1`.

## Useful project files

- `PREMISE.md` — the 4-step scoring framework + falsifiability (hybrid rejected) + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must not be claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric (teaching 12/12)
- `VISUAL-PLAN.md` — per-beat visual treatment + legibility contract
- `beat_sheet.json` — narration, timing, props, build state
- `remotion-src/ReadingRoadmapsGoldVerdict.tsx` — reel-local components
- `_qc/REPORT.md` — frame-level QC + PROOF production-gate result
- final `.mp4` — the 1080p master

## Build result for this report

The reviewed local build produced 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`); a synchronized 1080p compilation, runtime ≈ 3:52; and a complete end-to-end human review plus a PROOF pass (teaching 12/12; production gate PASS). The build emitted the expected `illustrate` motion-distribution warning (6 of 10 beats) — acceptable for a six-body-beat explainer.

## Current limitations

- the verdict is **provisional (grader 1)**; a second independent grading + reconciliation is pending;
- one gold sample (20 sections, 333 tags) and one model (`qwen2.5-coder:7b`, temp 0);
- the "hybrid" hypothesis is rejected *this round* — not a permanent finding across models/samples;
- agreement/provenance are measured on the graded sample, not the whole book;
- no learning/engagement claim; ordering still dormant (0 edges).

## Future work

- second independent blind grading + reconciliation → final, non-provisional tagger verdict;
- faculty approval of prerequisite links → activate ordering;
- validation across more sections and additional open models;
- an outcome/engagement study (out of scope this week).

## Final human checklist

- Can a new viewer state the four steps and apply them to a new "which is more correct?" case?
- Is precision/recall shown *with* F1, and the split read (not just the combined score)?
- Is the verdict marked **provisional (grader 1)** everywhere it appears?
- Is "hybrid" shown as a *rejected hypothesis*, not adopted as the outcome?
- Are the two 333 splits kept distinct (191/142 vs 184/149)?
- Did a human watch the complete output and complete at least one refinement pass?
- Has an authorized human reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it as an unlisted video and add it to the appropriate playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
