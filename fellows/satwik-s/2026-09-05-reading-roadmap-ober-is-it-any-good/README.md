# Weekly Research Report: How Would We Know It's Any Good?

**Fellow:** Satwik Reddy Sripathi
**Week ending:** September 5, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** The single frozen source `sources/ober_roadmap_detailed_report.md` (Parts 0/A–F), plus the reel ledger `output/reading-roadmap-ober/SOURCES.md`. Every on-screen figure traces to the report; the report itself is grounded in Askarbekuly et al. 2025, **OBER**, arXiv:2509.18186v1 (NamazApp).
**Source status:** This is a **step-back / idea-reconsideration** film, not a new experimental result. It reports the OBER preprint's numbers honestly (a deployed A/B on a prayer app, **~5,700 learners, 2 weeks, no significance tests**) and states plainly that **we have run no learning study of our own**. Every claim is framed as *direction, blueprint, instrument, or positioning* — **never as proof**.

This weekly research video answers the question we were asked to step back and confront:

**One recent study has become the whole justification for this project. How much weight can one study bear — and how would we actually know a personalized reading roadmap is any good?**

The video answers with a **reusable framework**: a single study can do **four honest jobs — evidence, blueprint, instrument, positioning — and one it can't: proof.** It then walks OBER through all five, job by job: the engagement recommender won engagement but the fixed, structured path won mastery (direction); structure-first-then-personalize is the blueprint, and OBER's own authors name the open problem — marry expert structure with personalization — which *is* the roadmap; mastery-read-from-logs is a cheap instrument we can borrow (plus the delayed check OBER missed); and the caveats (preprint, prayer app, no stats, in-app quizzes) are the reason it can **position** but never **prove**.

The final beat sheet contains **10 beats**. The complete video was generated locally using Brutalist, delivered as a **4K 16:9 master** plus a **≤1-minute 4K 9:16 Short**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4s live in the reel folder and are distributed separately.

## Note on series position (possible pivot)

This film steps back from *building the system* (weeks 00–05) to *justifying the idea*. If the project pivots to an **evaluation-first** framing — "how would we know roadmaps are any good?" as the organizing question — **this becomes Week 1 of that new project**, and the subsequent weeks renumber from here. Filed under `week-06-idea-reconsideration` for continuity; treat it as a hinge, not just a sixth episode.

## Production state

- Premise / reusable-framework gate (PROOF Phase 1): completed (`PREMISE.md`)
- Plan and beat structure: completed (re-derived from `ober_roadmap_detailed_report.md`)
- Narration generation: completed (Kokoro `af_bella`, run under `PYTHONUTF8=1`)
- Audio timing: completed (measured durations are the clock; total ≈ 3:18)
- Visual beats: 10 of 10 filled (16:9 `ReadingRoadmapsOber.tsx` + portrait `ReadingRoadmapsOber916.tsx` + shared claude scenes)
- Local compilation: completed — **4K 16:9 (3840×2160)** + **4K 9:16 (2160×3840)** via stream-copy assembly
- Vertical Short: one ≤60s 4K cut (framework-led: B01 framework + B03 evidence + B09 outro)
- Full-video review + PROOF production gate: completed (teaching 12/12; gate PASS; `_qc/REPORT.md`)
- **Audio verified present** on both masters (`volumedetect` mean ≈ **−21.2 dB**, not the −91 dB silence bug)
- Formal claim-level fact-check: figures traced to `SOURCES.md`; requires final human sign-off before publication
- YouTube publishing: handled separately through the Humanitarians AI review process

## Deliverables

| File (`output/reading-roadmap-ober/`) | Aspect | Resolution | Duration | Audio |
|---|---|---|---|---|
| `week6_reading-roadmap-ober_sep06.mp4` | 16:9 | 3840×2160 (4K) | 3:18 | −21.2 dB ✓ |
| `week6_reading-roadmap-ober_short_9x16_sep06.mp4` | 9:16 Short | 2160×3840 (4K) | 0:55 | −21.2 dB ✓ |

The Short is a **true re-layout** (the `916` components), not a center-crop.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## What this video is about

**Topic:** Reading one study honestly — the four jobs a single paper can do for a research bet, and the one it can't.

For five films the reading-roadmap pipeline was built and demonstrated. Asked to step back, we confront the uncomfortable fact that the whole project leans on **one preprint** — OBER, a deployed recommender A/B on a *prayer app* — with **no significance tests**. Rather than over-claim or discard it, the film builds a rubric for how much weight one study can bear, and applies it to OBER in the open.

The result is a **reusable framework** a viewer can apply to any "the literature supports my idea" moment: pin the one study to four jobs (evidence / blueprint / instrument / positioning), then name the job it can't do (proof) and add what it lacks.

## Central question

> One study has become the whole justification for a project. How much weight can it bear — and how would you know the thing it justifies is any good?

The proposed answer: a single study can honestly do four jobs — test the **direction** of your bet (not its magnitude), hand you a **blueprint** plus the open problem to fill, give you a cheap **instrument** to measure, and **position** you against alternatives — but it can never be **proof**. Name all five and you have used the paper honestly.

## Main ideas presented (10 beats)

1. **The ask (hook).** One study justifies the whole project — but it's a preprint, on a prayer app, with no significance tests. How much weight can it bear, and how would we know a roadmap is any good?
2. **The framework (framework-first).** A single study does four honest jobs — **evidence, blueprint, instrument, positioning** — and one it can't: **proof.** Shown as a structure *before* any OBER detail.
3. **What OBER is.** Deployed, randomized: **~5,700 learners, 2 weeks, 3 ways to recommend the same lessons** — a fixed expert-ordered path, an engagement ("people-like-you") recommender, and a knowledge-based one. Same learners, same content, three orders.
4. **Job 1 · Evidence.** The engagement recommender won **engagement** (retention 6.16); the **fixed, structured path won mastery** (0.46 vs 0.39); **click-through was flat (~0.30) for all three**. The clicking winner ≠ the learning winner. Direction: **structure > engagement** — that's the direction our bet rides on (not the magnitude).
5. **Job 2 · Blueprint.** Structure first, then personalize inside it. The **gift**: OBER's winning order was fixed and one-size-for-all, and *both* personalized arms lost — so its authors name the open problem, **marry expert structure with personalization**. That hybrid *is* the roadmap: keep the dependency graph, add project-level ordering.
6. **Job 3 · Instrument.** OBER measures learning without a separate study — put outcomes and quiz items in the data, read **mastery straight from the logs**. Our three arms (chapter order / plain search / the roadmap) get scored on the same signal — with one fix OBER missed: a **delayed check** days later, so we measure learning that lasts.
7. **The job it can't do · Proof (falsifiability).** One preprint, a prayer app, no significance tests, and "mastery" = in-app quizzes, not lasting learning. **SAFE:** the engagement winner wasn't the learning winner. **OVER-REACH:** "it proves our system works." We've run no learning study of our own — **yet.**
8. **Verdict.** Used honestly, one study does four jobs — direction, blueprint, instrument, positioning — and never proves us right. That's the next study.
9. **Your turn (CTA).** Next time the literature "supports" your idea, pin the one study to four jobs, then name the one it can't do (proof) and add what it lacks. One paper is a foundation, never a verdict.
10. **Outro.** One study, four jobs — and the humility to know the fifth.

## Current implementation boundary

The video establishes a **way to reason about evidence**, and reports OBER's real findings. It does **not** claim our reading-roadmap system improves learning, and it does **not** treat OBER as proof of anything about our system.

The result should be understood as follows:

- OBER gives us the **direction** of the bet (structure beat engagement on mastery), not its magnitude for our setting;
- the **hybrid** (expert structure + personalization) is an open problem OBER's authors name — we adopt it as the design, not as a validated outcome;
- the **instrument** (mastery-from-logs + a delayed check) is a method we can reuse; we have not yet run it;
- **no learning or engagement claim** is made for our own system.

The following remain future work: our own learning study across projects; the delayed-retention measurement; any outcome/engagement claim for the roadmap.

## The reusable framework (apply it to a new case)

Pin any one study that "supports your idea" to five jobs:

1. **Evidence** — does it test the **direction** of your bet (not just its magnitude)?
2. **Blueprint** — does it hand you a design principle **and** the open problem you get to fill?
3. **Instrument** — does it give you a cheap way to **measure** (ideally from data you already have)?
4. **Positioning** — does it place you **against the alternatives**?
5. **Proof** — the one it can't do. Name it, then add what's missing (usually: your own study).

Decision rule: a paper is a **foundation, never a verdict**. A good use names the four jobs and refuses the fifth; a bad use leans on one study's magnitude, or calls direction "proof."

## How faculty review is used

This film rests on published/derived figures, not on the project's draft prerequisite graph, so it does not itself need faculty sign-off to be honest. It does, however, motivate the study faculty review would eventually gate: the **hybrid roadmap** (dependency graph + project-level ordering) is exactly what needs an authoritative prerequisite graph before a real learning study can run. Until then, the film claims direction and method, not proof.

## Research prompt

Use the following prompt before substantially rewriting this film:

> Research the "How Would We Know It's Any Good?" idea-reconsideration explainer. Begin with `sources/ober_roadmap_detailed_report.md` (Parts 0/A–F), then `SOURCES.md`, `PREMISE.md`, and `beat_sheet.json`. Identify the four honest jobs a single study can do (evidence/blueprint/instrument/positioning) and the one it can't (proof); OBER's setup (~5,700 learners, 2 weeks, 3 arms: Fixed/CF/KB); the results (retention CF 6.16 / Fixed 5.63 / KB 5.02; CTR flat ~0.30; mastery Fixed 0.46 > CF 0.39); the authors' open problem (marry expert structure + personalization); the mastery-from-logs instrument; and the caveats (preprint, prayer app, no significance tests, in-app quizzes). Return a claim table: claim, exact source (report part), pinpoint evidence, confidence, and what still requires verification. Do not invent numbers or significance. Never present OBER as proof our system works, and never claim durable learning from in-app quizzes.

## Fact-check prompt

Run the following prompt after any narration or beat-sheet change:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and capability claim and compare each with `sources/ober_roadmap_detailed_report.md` and `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Pay particular attention to: ~5,700 learners / 2 weeks / 3 arms; retention 6.16/5.63/5.02; CTR flat ~0.30; mastery 0.46 vs 0.39; "engagement winner ≠ learning winner"; the authors' open problem; the four-jobs framing; and the caveats. Flag any framing that treats OBER as proof, any durable-learning claim from in-app quizzes, any significance claim, and any learning/engagement claim for our own system. Do not silently rewrite narration; list corrections for human review.

## Typical commands

Run from the Brutalist toolkit root. On Windows, prefix Python with `PYTHONUTF8=1` so on-screen em-dashes / middots / arrows / ≠ / ✗ do not corrupt, and use the toolkit venv Python for Kokoro.

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/reading-roadmap-ober"
PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=4 python runtime/scripts/remotion_scenes.py "/abs/path/to/reading-roadmap-ober"   # 4K beats
# top up any transient Chrome-launch timeout at concurrency 1:
PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=1 python runtime/scripts/remotion_scenes.py "/abs/path/to/reading-roadmap-ober" --only B05
# 9:16 Short: render the portrait 916 compositions directly, then assemble:
PYTHONUTF8=1 npx remotion render src/index.ts FourJobsFramework916 out.mp4 --props=p.json --scale=2 --image-format=png --crf=16
```

**Audio assembly (binding Windows fix).** Build the master audio with the concat **FILTER**, not the demuxer — the concat *demuxer* (`-f concat -c:a aac`) yields a **silent** track (−91 dB) from 24 kHz-mono Kokoro mp3s on this ffmpeg build:

```bash
ffmpeg -i b00.mp3 … -filter_complex "[0:a][1:a]…concat=n=N:v=0:a=1[a]" -map "[a]" -c:a aac -b:a 192k _a.m4a
ffmpeg -f concat -safe 0 -i _v.txt -c copy -fflags +genpts _v.mp4          # stream-copy video
ffmpeg -i _v.mp4 -i _a.m4a -map 0:v:0 -map 1:a:0 -c copy -shortest -movflags +faststart OUT.mp4
ffmpeg -i OUT.mp4 -af volumedetect -f null -                               # VERIFY mean ≈ −20 dB, not −91
```

## Beat-sheet and visual rules

- Treat `beat_sheet.json` as the source of truth; audio duration is the timing clock (`durationInFrames = round(actual_duration_s × 30)`).
- Show the four-jobs framework (+ the PROOF ✗ fifth) **before** any OBER detail (framework-first).
- Every claim beat shows its real number legibly at the moment the claim is made; B03's retention/CTR/mastery are **side-by-side**, flat-CTR beside separating mastery, held ≥2s.
- **CRIMSON is reserved for falsifiability** — the PROOF ✗ strip (B01), B06, and the B04 "gift" (OBER's weakness). GOLD = engagement, TEAL = mastery, SAGE = the delayed-check.
- Never frame OBER as proof; never claim durable learning from in-app quizzes; keep "no learning study of our own — yet" wherever the topic arises.
- Portrait (9:16) is a true re-layout via the `916` components, never a center-crop.

## Voice and narration

Kokoro `af_bella` ("Bella"), recorded in `beat_sheet.json`; register **pragmatist / skeptical-explainer**; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration on the animated slate before generating audio; regenerate + remeasure whenever narration changes; on Windows always run audio/render/compile under `PYTHONUTF8=1`.

## Useful project files

- `output/reading-roadmap-ober/PREMISE.md` — the four-jobs framework + falsifiability + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must not be claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric (teaching 12/12)
- `VISUAL-PLAN.md` — per-beat visual treatment + legibility contract + the audio-assembly fix
- `beat_sheet.json` — narration, timing, props, build state
- `remotion-src/ReadingRoadmapsOber.tsx` (16:9) + `…Ober916.tsx` (portrait) — reel-local components
- `sources/ober_roadmap_detailed_report.md` — the frozen story source (Parts 0/A–F)
- `_qc/` — frame-level QC + PROOF production-gate result (`REPORT.md`)
- final `.mp4` files — the 4K 16:9 master + the 4K 9:16 Short

## Build result for this report

The reviewed local build produced:

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 3:18) and a **≤1-min 4K 9:16 Short** (2160×3840, 0:55), stream-copy assembled;
- **audio verified present on both masters** (`volumedetect` mean ≈ −21.2 dB) — this rebuild specifically fixed the earlier silent-audio defect by switching to the concat **filter**;
- a complete end-to-end human review plus a PROOF pass (teaching 12/12; production gate PASS).

Build notes: this reel was **recreated from scratch** — the prior "any-good" cut was removed and the story re-derived directly from `ober_roadmap_detailed_report.md` (the four jobs). Several beats hit transient Chrome-launch timeouts during the 4K render (the machine was running low on free RAM, ~1.8 GB) and were topped up individually at concurrency 1. The portrait Short beats (B01/B03/B09) were rendered directly from the `916` compositions and assembled with the same verified concat-filter audio path.

## Current limitations

- OBER is a **preprint**, not peer-reviewed; it is a deployed A/B on a **prayer app** (non-STEM, procedural content), with **no significance tests**;
- its "mastery" is **in-app quizzes**, not durable learning; the direction is trustworthy, the magnitude is not portable;
- the **best arm was not personalized** (fixed, one-size-for-all) — the hybrid we adopt is an *open problem*, not a validated design;
- **we have run no learning study of our own** — no outcome or engagement claim is made for the reading-roadmap system.

## Future work

- run our own learning study (three arms: chapter order / plain search / the roadmap) scored on mastery-from-logs;
- add the **delayed retention check** OBER missed, so we measure learning that lasts;
- activate the authoritative prerequisite graph (faculty review) so the hybrid roadmap can be evaluated as designed;
- position the result against the literature's alternatives once we have our own evidence.

## Final human checklist

- Can a new viewer state the four jobs (+ the one it can't) and apply them to a new "the literature supports my idea" case?
- Does B01 land the framework (+ PROOF ✗) **before** any OBER detail?
- Is B03 the engagement/mastery split with the **flat-CTR** column, side-by-side and legible?
- Does B06 show the four caveats + SAFE/OVER-REACH + "no learning study of our own — yet"?
- Is OBER named exactly (Askarbekuly et al. 2025, arXiv:2509.18186v1; NamazApp), with direction cited and magnitude not leaned on?
- Is **audio present** on both masters (`volumedetect` ≈ −21 dB, not −91)?
- Is the Short a true re-layout (not a crop), and both cuts genuinely 4K?
- Did a human watch the complete output, and has an authorized reviewer approved publication?

## Publication note

The final MP4s live in the reel folder and are shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload them (16:9 long + vertical Short) to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
