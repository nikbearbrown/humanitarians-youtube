# Weekly Research Report: Match It, Prove It, Skip It

**Fellow:** Satwik Reddy Sripathi
**Week ending:** October 17, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` — `weekly_report_2026-10-18.md`, `matching_scorer.py`, `question_coverage.csv`, `matching_malformed.csv`, `matching_recovered.csv`, `student_roadmap_app.html`, `demo_matching_check.png`, `demo_matching_miss.png`. Every on-screen figure traces to these.
**Source status:** The matching **scorer, importer, gate branch, and app self-check are built and tested** (62 tests pass; 178 well-formed matching items live; app renders with 0 skipped, verified). What is **draft / not verified**: the **0.75 pass bar** is a chosen, documented default (configurable, faculty to review); the **questions are borrowed** from the collaborators' bank and **held from the repo**; the **8 recovered items** need Evin's confirmation; **1 Chapter-2 title** is still unmatched. **No learning-outcome claim** is made — the check works and is consistent, not yet shown to teach.

This weekly research video follows last week directly. Week 11 attached the question bank to the three-tier prerequisites, but one whole question type — **concept-matching** ("Match each X to its Y") — was being dropped, because its answer is a *mapping*, not a single letter. 186 of them were skipped. So this week —

**the matching questions were made gradable, and turned into an optional "check your knowledge" step that can let a student skip a prerequisite — without ever being a graded test.**

The answer is one small, careful piece: score each prompt->option pair independently (relational partial credit), pass at a bar well above chance, and treat the result as **formative** — opt-in, informative, and able to advance a student, but never recorded as a grade.

The final beat sheet contains **10 beats**. The complete video is generated locally with the free Brutalist toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4 lives in the reel folder and is distributed separately.

## What was built this week

- **A matching scorer** (`matching_scorer.py`, 12 tests). Relational per-pair partial credit: `s = correct pairs / prompts`. The raw `s` is kept so the stronger partial-credit knowledge-tracing path (Wang, Heffernan & Beck 2010) stays open. It knows bijective from distractor items and flags malformed ones instead of grading them.
- **A re-runnable importer** (`build_question_map.py`). It preserves the full matching structure (prompts, options, the mapping) instead of flattening every question to the MCQ shape. **178 well-formed matching items** now carry full structure; **8 malformed** are routed to a flag file.
- **Gate integration** (`evaluate_gate.py`). A `concept_matching` item can satisfy a prerequisite (prune-after-evaluate), recorded as `assessment_mode = knowledge_check`, never a grade. Verified end to end: **4/4 -> advance, 2/4 -> remediate, opted-out -> hold**.
- **The demo app** (`student_roadmap_app.html`). An opt-in matching self-check: a dropdown per prompt, per-pair feedback, the explanation, and a Continue button regardless of score. **0 skipped now** (was 186).
- **A recovery of the 8 malformed items** into a *separate* review file (`matching_recovered.csv` / `.json`), kept out of the live pipeline until faculty confirm them.

The upgrade over week 11: last week the question bank was attached but matching questions were unusable. This week they work, and they do something the MCQs cannot do cleanly — let a student *demonstrate* a mapping and have it count, while staying explicitly formative.

## How this connects to the series

Weeks 00–06 built and justified the roadmap; **week 07** designed the test-to-advance gate; **week 08** built the prerequisite graph; **week 09** ran the evaluation pipeline; **week 10** wrote a real question per step; **week 11** re-tiered the prerequisites and attached the question bank; **week 12 makes the matching questions usable** as an optional, formative knowledge-check that can advance a student. It is the piece that turns a dropped question type into a working, non-punitive way to skip what you already know.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> How do you let a student prove they already know a prerequisite with a matching question — and let that count toward skipping ahead — without turning a formative check into a graded test?

The proposed answer: score each prompt->option pair independently (relational partial credit), pass at a bar well above chance, and keep the whole thing opt-in and informative — a pass can prune a prerequisite, but it is never a grade.

## Main ideas presented (10 beats)

1. **The dropped question type (hook).** Concept-matching answers are mappings, not letters, so the gate skipped all of them — 186 dropped last week. A whole question type, unused.
2. **The framework (framework-first).** A formative knowledge-check: opt-in (you get the roadmap anyway), can advance you (a pass prunes a prerequisite), but never graded. Three properties before any number.
3. **The scoring method.** Relational / per-pair partial credit (McClure, Sonak & Suen), the same as per-option partial credit with no negative marking. `s = correct pairs / prompts`. Pass bar 0.75, above the ~4% chance of a lucky 4x4 match.
4. **The bijection subtlety.** 157 items are 4x4 bijections (can't miss exactly one, so 0.75 means perfect); 22 have a spare distractor and can earn genuine partial credit like 2/3. Shown honestly.
5. **In the gate.** 4/4 -> advance (prune), 2/4 -> remediate, opted-out -> hold; recorded as `knowledge_check`, never a grade. The prune-after-evaluate rule, now with matching.
6. **The demo.** Pick a goal, mark a topic known, opt into the check: a dropdown per prompt, per-pair green/red, the explanation, Continue either way. Pass "I will skip this and what it builds on"; miss "No problem, I will keep this in your plan." 0 skipped (was 186).
7. **The 8 malformed items.** A bank defect, not a textbook issue (re-cloning can't fix it). Content is sound; the mapping is recoverable (Ch5 spells it out; Ch35 is parallel-order, confirmed by explanations). Recovered into a separate review file, kept out of the pipeline.
8. **The honest boundary.** Built and tested, but the 0.75 bar is a chosen default; questions are borrowed and held from the repo; the 8 recovered need faculty; 1 Ch2 title unmatched; no learning-outcome claim.
9. **Your turn (CTA).** Score matching by relational partial credit; make the check opt-in and formative; let a pass prune but never grade; recover malformed data instead of discarding it, and keep the recovery separate until verified.
10. **Outro.** The roadmap, the tiers, the questions, and now a matching check that lets a student prove what they know and skip ahead — without a grade.

## Current implementation boundary

The matching check is **built, tested, and consistent**; it is **not** verified and makes **no** learning claim:

- **Works and is tested** — 62 tests pass (12 for the scorer); 178 items live; the gate and app verified end to end; the app renders with 0 skipped.
- **The 0.75 pass bar is a default** — defensible (above chance), documented, configurable; faculty may change it.
- **Questions are borrowed** from the collaborators' bank and **held from the repo**; **1 Chapter-2 title unmatched**.
- **The 8 recovered items are drafts** (`needs_review = yes`), kept separate; Evin confirms (mainly the Ch35 ordering).
- **No learning-outcome claim** — the check works and is consistent, not shown to teach.

## The reusable framework (apply it to any mastery check)

1. **Score structured answers by their parts** — relational / per-pair partial credit, not all-or-nothing; keep the raw fraction so a richer model can use it later.
2. **Separate the signal from the stakes** — a check can *inform advancement* (prune what a student proves) while being explicitly *formative* (opt-in, never a grade).
3. **Recover, don't discard** — malformed source data whose content is sound should be reconstructed into a separate, reviewable file, not dropped; keep it out of the live pipeline until an expert confirms.

Decision rule: pass the check if the per-pair score clears a bar set well above chance; on a pass, prune the prerequisite and what it builds on; on a miss or an opt-out, simply keep it in the plan.

## Research grounding

Relational concept-map scoring (McClure, Sonak & Suen) and its edge over similarity/structure scoring in validity studies; per-option partial credit with no negative marking for matching items (polytomous scoring); partial-credit knowledge tracing (Wang, Heffernan & Beck 2010) as the documented path for using the raw fraction; mastery-threshold framing (BKT ~0.95 context) for why a pass bar must sit above chance.

## Research prompt

> Research the "Match It, Prove It, Skip It" explainer. Begin with `sources/weekly_report_2026-10-18.md`, `matching_scorer.py`, `question_coverage.csv`, `matching_malformed.csv`, and `matching_recovered.csv`. Identify: the problem (matching answers are mappings, 186 skipped); the method (relational per-pair partial credit = per-option partial credit no negative marking; `s = correct/prompts`; bar 0.75 above ~4% chance); the bijection subtlety (157 4x4 bijections vs 22 distractor items); the three formative properties (opt-in, can advance, never graded); the gate behavior (4/4 advance, 2/4 remediate, opt-out hold; recorded as knowledge_check); the demo (0 skipped, was 186); and the 8 malformed items (bank defect, recovered into a separate review file, 2 high + 6 medium, kept out of the pipeline). Return a claim table with exact source lines. Do not invent numbers. Never present a draft as approved, and never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each factual/numerical/capability claim: beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: 186 skipped before, 0 skipped after; 178 well-formed live, 8 malformed; 157 bijective + 22 distractor; relational per-pair partial credit; bar 0.75 and the ~4% chance figure; the gate outcomes (4/4 advance, 2/4 remediate, opt-out hold) and `assessment_mode = knowledge_check`; "can advance but never graded"; "opt-in"; the 8 recovered (2 high + 6 medium, kept separate, needs_review); 62 tests pass; "questions borrowed and held"; "1 Ch2 title unmatched." Flag any framing that treats a draft as approved, a formative check as a grade, consistency as verification, or asserts a learning gain.

## Typical commands

Run from the toolkit root, under `PYTHONUTF8=1`, `.venv` Python for Kokoro, **temp on D:** (C: near-full):

```bash
PYTHONUTF8=1 ".venv/Scripts/python.exe" runtime/scripts/generate_audio_kokoro.py "/abs/path/to/concept-matching"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/concept-matching"
# stubborn beat (Chrome cold-start timeout): re-run --only BXX at concurrency 1, or render direct:
npx remotion render src/index.ts <CompId> media/BXX.mp4 --props=p.json --scale=2 --crf=16 --timeout=120000
```

**Assembly (binding):** both video and audio via the concat **FILTER** (beats span sessions; stream-copy concat can truncate). Verify the **video-stream** duration and `volumedetect` ≈ −20 dB.

## Beat-sheet and visual rules

- `beat_sheet.json` is the source of truth; audio duration is the clock (`durationInFrames = round(actual_duration_s × 30)`).
- Show the framework (opt-in / can-advance / never-graded) **before** any count (framework-first).
- Every claim beat shows its real figure legibly; B06 is the pass-vs-miss contrast (the two demo screenshots); B07 is bank-defect-vs-recovered; each held ≥2s.
- **TEAL = pass / advance, GOLD = the scoring method, SLATE = scale / counts, SAGE = built / live, CRIMSON = draft / caveats / malformed.** Colors stay consistent across body beats.
- Never frame a formative check as a grade, a draft as approved, or assert a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration on the animated slate before audio; regenerate + remeasure on any change; run under `PYTHONUTF8=1`.

## Useful project files (to be produced by the build)

- `output/concept-matching/PREMISE.md` — framework + worked spine + falsifiability + CTA
- `output/concept-matching/SOURCES.md` — no-source-no-verdict ledger
- `output/concept-matching/NARRATION-GATE-P.md` — spoken lines + GATE P
- `output/concept-matching/PEDAGOGY.md` — act structure + PROOF rubric
- `output/concept-matching/VISUAL-PLAN.md` — per-beat treatment + legibility contract
- `output/concept-matching/beat_sheet.json` — narration, timing, props, build state
- `sources/` — the frozen story source (weekly report, scorer, coverage + malformed + recovered CSVs, demo HTML, two demo PNGs)
- `_qc/` — frame-level QC + PROOF production-gate result
- final `.mp4` — the 4K 16:9 master

## Build result for this report

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 4:31 — video stream 270.77s, verified full length);
- **audio verified present** (`volumedetect` mean ≈ −21.4 dB) via the concat filter;
- a complete end-to-end frame-level QC plus a PROOF pass (production gate PASS; `output/concept-matching/_qc/REPORT.md`).

Build notes: this render fought persistent low-RAM Chrome cold-start timeouts (free RAM dipped to ~0.2–0.8 GB), so the 10 beats were completed across several top-up passes (first run, a concurrency-1 resume, direct `npx remotion render` for the stubborn beats, and a temp-dir clear before B08 finally landed). B08 (the shared `ClaudeComposerAsk`, registered at 900 frames) rendered at its 30 s composition length via the direct path, which skips the extend/trim step, so it was trimmed to its 26.24 s audio afterward (the composer settles by ~frame 115, so only the static hold was removed — verified in the master). Assembly used the concat filter for both streams; the video-stream duration was verified full length (270.77s).

## Current limitations

- the **0.75 pass bar** is a chosen default, not faculty-verified;
- the **questions are borrowed** from the collaborators' bank and **held from the repo**;
- the **8 recovered items** are drafts awaiting Evin (mainly the Ch35 ordering);
- **1 Chapter-2 question title** is unmatched;
- the check is **consistent and tested but not verified** — **no learning-outcome claim**.

## Future work

- faculty review of the 0.75 pass bar and confirmation of the 8 recovered items;
- reconcile the 1 Chapter-2 title; decide on the ~187 that only fit a matching gate;
- decide whether the question text is committed to the repo or kept local;
- consider the partial-credit knowledge-tracing path for the stored raw score.

## Final human checklist

- Can a viewer state the three properties (opt-in / can-advance / never-graded)?
- Does B03 show the method (per-pair partial credit, `s = correct/prompts`, bar 0.75 above ~4% chance)?
- Does B05 show the gate outcomes (4/4 advance, 2/4 remediate, opt-out hold) as a knowledge-check, not a grade?
- Does B06 contrast pass vs miss with the two real screenshots, and state 0 skipped (was 186)?
- Does B07 show the bank defect vs the separate recovery, with "needs faculty"?
- Is every figure traceable to `sources/`, with no formative check framed as a grade and no learning claim?
- Is **audio present** and the **video stream full length** on the master?
- Did a human watch the complete output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
