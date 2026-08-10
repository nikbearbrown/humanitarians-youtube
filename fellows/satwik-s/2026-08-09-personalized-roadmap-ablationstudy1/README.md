# Weekly Research Report: Does the Fancy Part Earn It? — A Tagging Ablation

**Fellow:** Satwik Reddy Sripathi
**Week ending:** August 9, 2026
**Research project:** Personalized Project-Driven Reading Roadmaps
**Research sources:** See `SOURCES.md`, the ablation study (`ablation_study_tagging.md`), the raw results table (`tagger_comparison.md`), the cluster reproduction runbook (`cluster_run_study2.md`), and the per-run data in `analysis/`.
**Source status:** This video reports a completed ablation study on the Stage-2 metadata tagger. Its strongest single number rests on a small sample (n≈4) and is presented as **provisional pending a denser re-run**; the denser run and any learning-outcome evaluation are presented as future work, not completed results.

This weekly research video asks:

**When a cheap, deterministic component and a fancier language-model component are both available, how do you decide — honestly — whether the fancy one earns its place?**

The video answers with a **reusable, five-check ablation method**, then walks the tagger ablation through it: hold everything fixed and toggle exactly one component (a deterministic rule-based tagger vs. a pinned open model), test run-to-run stability, compare where the two agree, weight the field that actually drives the downstream decision, and check the denominator behind the headline number. The conclusion — ship the deterministic default, keep the pinned model as a named option — is delivered with its limits shown, not hidden.

The video also explains how the places the two backends **disagree** (the fuzzy interpretive fields, the difficulty score) are not failures but the **agenda for faculty review** — the human step where uncertain tags are resolved.

The final beat sheet contains **10 beats**. The complete video was generated locally using Brutalist, compiled at 1080p, reviewed end to end (including a PROOF skeptical-explainer pass), and prepared separately for submission. The MP4 and generated media files are intentionally excluded from this repository.

## Production state

- Premise / reusable-framework gate (PROOF Phase 1): completed
- Plan and beat structure: completed
- Beat-sheet lint: passed
- Narration generation: completed (Kokoro `af_bella`, run under `PYTHONUTF8=1`)
- Audio timing: completed (measured durations are the clock)
- Visual beats: 10 of 10 filled
- Local compilation: completed (1080p)
- Full-video review + PROOF production gate: completed (teaching 12/12; gate PASS)
- Formal claim-level fact-check: figures traced to `SOURCES.md`; requires final human sign-off before publication
- YouTube publishing: handled separately through the Humanitarians AI review process
- MP4 and generated media: excluded from Git as instructed

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Weekly Research Report: Does the Fancy Part Earn It? — A Tagging Ablation

## What this video is about

**Topic:** Deterministic vs. pinned open-model metadata tagging — an ablation study.

The reading-roadmap pipeline tags each textbook section with structured metadata (concepts, mechanisms, techniques, materials, assays, disease contexts) drawn from a controlled vocabulary. The default tagger is a **deterministic, rule-based lexicon matcher**; a **language-model tagger** (a pinned, self-hosted open model) is available behind the same interface.

The project's method paper raised a standard worry: language-model tagging is stochastic — run it twice and you may get different tags — which threatens reproducibility. Rather than argue the point, this week ran an ablation to answer it with evidence.

An ablation isolates the effect of one component by holding everything else fixed and toggling only that component. This video turns the ablation into a **reusable method** a viewer can apply to any "simple vs. fancy" engineering choice.

The video can represent:

- the reusable five-check ablation rubric;
- the control vs. treatment setup (one variable changed);
- run-to-run stability, per metadata field;
- cross-backend agreement, per metadata field;
- the load-bearing field that drives the downstream decision;
- the denominator (sample size `n`) behind each headline number;
- approved / verified numbers vs. provisional ones;
- the decision the evidence supports;
- where human (faculty) review adds the most value;
- what remains future work.

The current project contains **10 beats**. Its timing is derived from the measured narration and beat durations recorded in `beat_sheet.json`.

## Central question

The project is organized around the following question:

> When a cheap deterministic component and a fancier model-based component are both available, how do you decide — honestly, with the sample size in view — whether the fancy one earns its place?

The proposed answer is to run a controlled ablation and read it through five checks, keeping the simple default unless the fancy component earns its cost on the checks that actually matter.

## Main ideas presented

The video introduces the following ideas:

1. A method paper's worry ("the model is stochastic, so can you trust it?") should be tested with an ablation, not settled by assertion.
2. An ablation changes exactly one component and holds everything else fixed, so any difference is attributable to that component.
3. Stability (run-to-run self-agreement) measures whether a backend gives the same answer twice.
4. The deterministic backend is exactly reproducible (1.000, byte-identical); the pinned model is only near-exact (~0.991) even at temperature 0, because of GPU floating-point non-associativity — not sampling.
5. Agreement (per field) shows where the two backends differ; on the fuzzy interpretive fields the model tags more liberally (1–2 extra terms), with overlap near 0.4.
6. You should weight the field that drives the downstream decision, not average all fields equally — here that field is `materials`, which sets a section's `core` role.
7. Agreement is highest exactly on that load-bearing field (Jaccard ≈ 0.89).
8. A headline number can be padded by trivial cases (empty-vs-empty agreement); you must report the denominator `n`.
9. Restricted to sections that actually carry a tag, `materials` stability drops from 0.996 to 0.933 on just four sections — so the strongest number is provisional pending a denser re-run.
10. Where the two backends disagree is not a failure; it is the agenda for faculty review, and dynamic adaptation / learning-outcome evaluation remain future work.

## Current implementation boundary

The study establishes a **reproducibility and agreement result** for the tagging step. It does not claim the model-based tagger is "worse," and it does not claim any improvement in learning outcomes.

The result should be understood as follows:

- the deterministic backend is *exactly* reproducible and is a genuine control (stays 1.000 even under the stricter, non-empty test);
- the pinned open model is *named and near-reproducible* (temperature 0, fixed seed, recorded digest), not exactly reproducible;
- on the load-bearing field the two agree strongly, but on a small sample;
- neither backend is a gold standard — agreement is measured against the rule-based reference, not against faculty-verified truth.

The following require additional evaluation or remain future work:

- the denser `--chapters 19-27` re-run that turns the `materials` agreement into a claim with defensible `n`;
- adjudication of the model's extra tags on interpretive fields (faculty review);
- calibration of the 1–5 difficulty heuristic (weak agreement: 35% exact, MAE 0.88);
- validation across more than one open model and one 60-section sample;
- any claim about improved learning or engagement.

## How to read the ablation tables

The tables should be read carefully; the honest reading is different from the headline.

### Stability (run-to-run)

For each field, stability is the mean pairwise overlap of the tag set across K=3 runs. The rule-based backend is **1.000** everywhere. The model is **0.987–0.996**. Plain stability counts "no tags in any run" as agreement, so sparse fields read high for a trivial reason.

### Non-empty stability (with `n`)

Restricting to sections that actually carry a tag — and reporting how many sections that is — shows where the headline is padded. The model holds 0.98–0.99 on most fields but drops to **0.933 on `materials`, over just 4 non-empty sections**. The deterministic control stays exactly **1.000** under this stricter test.

### Agreement (per field)

`Jaccard` = set overlap; `recall` = fraction of rule-based tags the model reproduced; `extra` = tags the model added per section. Agreement is highest on `materials` (0.887) and moderate (0.35–0.46) on the fuzzy fields, where the model adds 1–2 extra terms.

### Difficulty

The two backends agree on the 1–5 difficulty level only 35% of the time (MAE 0.88) — the weakest signal, and a faculty-calibration item, not a score to rely on as-is.

An on-screen number is not trustworthy merely because it is large; its meaning depends on the denominator behind it.

## How faculty review is used

Faculty review resolves the places the two backends disagree, rather than replacing the tables with a single score.

A faculty review may help determine:

- whether a model's extra tag on an interpretive field is signal or noise;
- whether a `materials`/`concepts`/`mechanisms` tag is accurate;
- whether the difficulty level of a section is reasonable;
- whether two tags should be merged or separated;
- whether a proposed prerequisite relationship is authoritative;
- whether a relationship should be approved or remain provisional;
- whether additional evidence or a denser sample is required.

Where reviewers disagree, that uncertainty should be preserved, not silently collapsed into certainty.

## Sample and per-run data

The study's inputs and outputs are reproducible artifacts, not verified ground truth.

They include:

- a seeded, chapter-stratified sample of 60 sections (`analysis/tagger_sample.json`);
- per-run tag sets for each backend (`analysis/tagger_runs.json`);
- the raw results table (`tagger_comparison.md`);
- the metrics implementation (pure functions with unit tests, in the project repo).

Sample data is provided to make the study reproducible and to show how stability and agreement are computed — not to assert a validated production result. Before any number is used as a claim it should be checked for sample size, empty-vs-empty padding, single-model bias, and the absence of a gold standard.

## The reusable method (apply it to a new case)

A viewer can run the same five checks on any "simple vs. fancy" decision:

1. **ISOLATE** — change exactly one component; hold the rest fixed.
2. **STABILITY** — run it K≥3 times; is the answer the same?
3. **AGREEMENT** — does the fancy option differ from the simple one, and where?
4. **WEIGHT** — judge the field/metric that drives your downstream decision, not the average.
5. **DENOMINATOR** — restrict to non-trivial cases and report `n`.

Decision rule: keep the simple default unless the fancy part earns its cost on the checks that matter. A good result is a decision you can defend with the denominator visible; a bad result is a headline number whose `n` you cannot state.

## Make your own version

Download the local Brutalist toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist uses the beat sheet as the source of truth.

Each beat records information such as:

- narration;
- timing;
- visual intent;
- motion language;
- scene type;
- source references;
- build state;
- implementation notes.

For this project, begin with:

```text
beat_sheet.json
```

Preserve the reviewed version before experimenting. Create a copy or a new dated project folder rather than overwriting the completed project.

This project uses a compact, framework-first explainer structure (per the PROOF protocol) rather than a long documentary. The ten beats move from the reproducibility worry, through the five-check rubric, the isolate/stability/agreement/weight checks, the honest denominator check, and the decision, to the scaffolded viewer task.

## Research prompt

Use the following prompt before substantially rewriting the project:

> Research the tagging ablation "Does the Fancy Part Earn It?" for an educational explainer. Begin with `ablation_study_tagging.md`, the raw results `tagger_comparison.md`, the cluster runbook `cluster_run_study2.md`, `SOURCES.md`, `beat_sheet.json`, and the per-run data in `analysis/`. Identify the research question, the control vs. treatment setup, the stability and agreement metrics, why `materials` is the load-bearing field, how empty-vs-empty padding inflates sparse-field numbers, what the non-empty `n` reveals, and what remains future work (the denser re-run, difficulty calibration, learning-outcome evaluation). Return a claim table containing: claim, exact source or citation, pinpoint evidence, confidence, and what still requires verification. Do not invent experimental results, sample sizes, model identifiers, performance metrics, or deployed capabilities. Never state a small-sample number without its `n`.

## Fact-check prompt

Run the following prompt after any narration or beat-sheet change:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and capability claim. Compare each with `ablation_study_tagging.md`, `tagger_comparison.md`, and `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Pay particular attention to: stability figures (1.000 vs 0.991), the non-empty `materials` figure (0.996 → 0.933) and its `n`=4, agreement per field, the difficulty numbers, the model identifier/digest, and the boundary between what was measured and what is planned (the `--chapters 19-27` re-run). Flag any on-screen number shown without its `n`, and any framing that reads as "the model is worse" rather than a precision/recall trade-off. Do not silently rewrite the narration. List every proposed correction for human review.

## Build and review loop

The human remains responsible for research judgment, factual approval, narrative quality, and publishing decisions. Brutalist performs the structured local build.

1. **Research and scope** — define the specific question and identify the study, raw results, runbook, and data.
2. **Lock the reusable method (PROOF Phase 1)** — write the framework and falsifiability case to `PREMISE.md` and gate it before scripting.
3. **Create the project folder** — a separate dated folder for the weekly report.
4. **Write the narration** — framework-first: the five checks land before any result.
5. **Create the beat sheet** — one explanatory purpose per beat; every claim beat names its on-screen artifact.
6. **Define the visual plan** — decide what the viewer sees during each segment; specify the legibility contract (side-by-side, `n` shown, held ≥2s).
7. **Separate measured results from future work** — the denser re-run and any learning claim are future work.
8. **Run the fact-check review** — create or update `FACTCHECK.md`; mark unresolved claims with `[VERIFY: ...]`.
9. **Complete Gate P narration review** — read every line aloud; record the decision in `PEDAGOGY.md` / `NARRATION-GATE-P.md`.
10. **Generate local narration audio** — only after review; run under `PYTHONUTF8=1`; measured durations become the timing clock.
11. **Generate visual beats** — implement each beat as a native Remotion scene.
12. **Run build checks** — validate beat structure, branding, timing, metadata.
13. **Compile the review cut** — render the scenes and combine with measured narration (run under `PYTHONUTF8=1`).
14. **Watch the complete video + PROOF pass** — check pacing, sync, legibility, side-by-side comparisons, and that every number shows its `n`.
15. **Refine and rebuild** — update only the beats that require correction.
16. **Create the clean final output** — produce the final MP4 separately and keep it outside Git.
17. **Publish only after human approval** — successful compilation does not authorize publication.

## Typical commands

Run these from the Brutalist toolkit root. On Windows, prefix Python with `PYTHONUTF8=1` (or `set PYTHONUTF8=1`) so on-screen em-dashes / middots / arrows do not corrupt.

```bash
# Inspect the available workflow
./art --help

# Generate or verify narration audio after approval
PYTHONUTF8=1 python3 runtime/scripts/generate_audio_kokoro.py "/absolute/path/to/this/project"

# Render the Remotion beats
PYTHONUTF8=1 python3 runtime/scripts/remotion_scenes.py "/absolute/path/to/this/project"

# Compile at 1080p
PYTHONUTF8=1 python3 runtime/scripts/compile.py "/absolute/path/to/this/project" --height 1080

# Inspect remaining work
./art todo "/absolute/path/to/this/project"
```

The exact supported commands may depend on the checked-out Brutalist version. Check each command's `--help` before adding new arguments.

## Beat-sheet and visual rules

- Treat `beat_sheet.json` as the source of truth.
- Audio duration is the timing clock; regenerate and remeasure audio whenever narration changes.
- Show the reusable framework before any result (framework-first).
- Keep each beat focused on one explanatory purpose.
- Every claim beat shows its real table/number, legibly, at the moment the claim is made.
- Put comparisons side-by-side (rule-based vs. model), held ≥2s.
- Never show a small-sample number without its `n`.
- Do not frame the result as "the model is worse" — it is a precision/recall trade-off with no gold standard.
- Present the denser re-run and any learning-outcome claim as future work, never as a result.
- Keep important labels readable at normal viewing size; avoid overcrowding a beat.
- Use motion to show comparison, progression, or the denominator strip-away — not decoration.
- Run project lint / quality checks after structural edits.
- Treat the first successful compile as a review cut; preserve the reviewed project before a new version.
- Keep final MP4 files and generated media outside Git.

## Voice and narration

The narration voice and production metadata are recorded in `beat_sheet.json` and the generated audio artifacts.

For future weekly reports:

- choose one consistent local Kokoro voice (this project: `af_bella`);
- record the voice selection in the beat sheet;
- review narration before generating audio;
- preserve pronunciation consistency for technical terms and model identifiers;
- regenerate audio when narration changes;
- do not manually stretch visual timing to hide narration changes;
- verify synchronization after every narration revision;
- on Windows, always run the audio/render/compile scripts with `PYTHONUTF8=1`.

## Useful project files

- `README.md` — this weekly report + rebuild guide
- `PREMISE.md` — the reusable ablation framework, falsifiability case, and CTA (PROOF Phase 1)
- `beat_sheet.json` — narration, timing, beat structure, on-screen props, and build state
- `NARRATION-GATE-P.md` — the spoken lines + narration gate (GATE P: VERDICT PASS)
- `PEDAGOGY.md` — teaching strategy, act structure, and PROOF rubric mapping
- `SOURCES.md` — the no-source-no-verdict ledger (verified figures with `n`; what must not be claimed)
- `VISUAL-PLAN.md` — visual treatment, per-beat design, and legibility contract
- `remotion-src/` — reel-local Remotion scene implementations (portable copy)
- `_qc/REPORT.md` — frame-level QC + PROOF production-gate result
- `FACTCHECK.md` — claim-level evidence and required corrections, when present
- `mp3/`, `media/`, `clips/` — generated narration audio and derived render assets; excluded from this submission
- final `.mp4` files — excluded from Git and distributed separately

## Build result for this report

The reviewed local build produced:

- 10 of 10 filled beats;
- successful beat-mix lint;
- measured per-beat narration (Kokoro `af_bella`, generated under `PYTHONUTF8=1`);
- synchronized audio and visual compilation;
- a 1080p output, total runtime ≈ 3:27;
- a complete end-to-end human review plus a PROOF pass (teaching 12/12; production gate PASS);
- no MP4 committed to this project folder.

The build emitted a motion-distribution warning because the `illustrate` motion language carried 6 of 10 beats — above the recommended balance. This warning did not prevent compilation and is expected for a six-body-beat explainer; future revisions may diversify the motion language where that improves comprehension rather than adding variation for its own sake.

## Current limitations

This video reports one ablation on one open model and one 60-section sample. It does not establish a gold standard, and it does not claim improved learning outcomes.

Important limitations include:

- field sparsity + small `n`: `materials` stability/agreement rests on only ~4–5 non-empty sections;
- plain metrics count empty-vs-empty as agreement, inflating sparse-field headlines (reported non-empty with `n` to make this visible);
- single model (`qwen2.5-coder:7b`) and single sample — agreement numbers would shift with a different model or larger sample;
- no gold standard — agreement is measured against the rule-based reference, not faculty-verified truth;
- the ~1% model drift is hardware/runtime dependent (the architectural point holds; the exact figure is not portable);
- the difficulty heuristic is uncalibrated (35% exact agreement);
- the denser `--chapters 19-27` re-run is planned, not completed;
- visual simplifications of the tables should not be mistaken for the full data.

## Future work

Potential future work includes:

- the denser `--chapters 19-27` re-run (materials density ~17%) to give the load-bearing field defensible `n`;
- evaluation across additional open models and larger samples;
- faculty adjudication of the model's extra tags on interpretive fields;
- calibration of the difficulty heuristic against faculty judgment;
- a gold-standard set of faculty-verified tags to measure accuracy, not just agreement;
- the companion Selection-vs-Retrieval ablation (deferred until the faculty prerequisite CSV is returned);
- explicit representation of reviewer disagreement and per-tag provenance.

These items should be presented as proposed directions unless implementation and evaluation evidence is available.

## Final human checklist

- Can a new viewer state the five checks and apply them to a new "simple vs. fancy" case?
- Is the control-vs-treatment setup clear (one variable changed)?
- Is stability distinguished from agreement, and both from difficulty?
- Is every on-screen number shown with its `n` where the sample is small?
- Is the `materials` 0.996 → 0.933 (n=4) shown honestly, with the control holding at 1.000?
- Is the result framed as a precision/recall trade-off, not "the model is worse"?
- Are measured results clearly separated from the planned denser re-run and future work?
- Does any visual imply more certainty than the evidence supports?
- Does the narration remain synchronized with the visuals?
- Is all text readable at ordinary playback size?
- Did a human watch the complete output and complete at least one refinement pass?
- Was the model identifier/digest recorded accurately?
- Is the MP4 excluded from Git, and generated clips/audio excluded?
- Has an authorized human reviewer approved publication?

## Publication note

The final MP4 is not stored in this repository.

The video is intended to be shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it as an unlisted video and add it to the appropriate Humanitarians AI playlist.

A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
 
