# Weekly Research Report: Evaluate, Then Advance

**Fellow:** Satwik Reddy Sripathi
**Week ending:** September 25, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` — `weekly_report_2026-09-27.md`, `evaluation_pipeline.md`, `evaluation_example.md`, `example_checkpoint_gate_result.csv`, `topic_graph_run_gate_result.csv`, `evaluate_gate.py`, `build_item_bank.py`. Every on-screen figure traces to these.
**Source status:** The **engine is real and running** (`evaluate_gate.py`): it grades a learner, prunes on a pass, descends on a fail, and returns advance/remediate with the exact gap. **MCQ grading is live** (offline exact-match). What is **draft**: the item text at scale is template **stubs** (real questions are next: LLM-draft + faculty-approve); **open-ended grading is a seam** (off until a gold set); and the whole gate **depends on faculty-approved edges**, still pending. **No learning-outcome claim** is made — the gate decides *readiness*, not learning gains.

This weekly research video is the payoff to the last two weeks: week 07 designed the test-to-advance gate, week 08 built the prerequisite graph it runs on, and this week —

**the pipeline runs end to end: grade a learner, decide advance or send back, and name the exact gap — without wasting questions or assuming what they already know.**

The answer is one rule in three moves: **evaluate, never assume** (every prerequisite is tested; nothing is trusted up front); **a pass earns a prune, a fail makes you descend** (a passing answer skips the whole subtree; a failure digs deeper to localise the gap); and **hard prerequisites gate while soft ones only diagnose** (and it tests the *connection*, not just the concept). Cost tracks the size of the gap near the goal, not the length of the chain.

The final beat sheet contains **10 beats**. The complete video was generated locally with the free Brutalist toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4 lives in the reel folder and is distributed separately.

## What was built this week

- `evaluate_gate.py` — the engine: grade → prune-on-pass → descend-on-fail → advance/remediate + gap.
- `build_item_bank.py` — turns a reviewed prerequisite CSV into a runnable dataset so the gate runs on the real graph.
- Three runnable examples, each writing `gate_result.csv` + `responses.csv`:
  - **STU-A** (goal: immune checkpoint inhibitors) → **remediate → "The basics of cancer treatment"**; 6 items administered, 2 subtrees pruned, closure 6.
  - **STU-B** → **advance**; 5 items administered, 3 subtrees pruned, closure 6.
  - **STU-SIM** on the **real topic graph** (220 concepts, 248 edges, 536-item pool) → **remediate → "Mutations"**; saw **5 of 536 items**, closure 8.

The upgrade over the week-07 demo: it no longer prunes against a pre-declared "knows" list. Nothing is assumed now — every skip is earned by a passing answer.

## How this connects to the series

Weeks 00–06 built and justified the roadmap; **week 07** designed the gate; **week 08** built the dependency graph; **week 09 runs the evaluation** on that graph, at scale. It is the direct successor to both, and the last piece before real question authoring and faculty sign-off.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> How do you evaluate a learner against a prerequisite structure — deciding advance or remediate, and naming the exact gap — without wasting questions, and without assuming what they already know?

The proposed answer: evaluate every prerequisite (never assume), prune on a pass and descend on a fail, and let only hard edges gate. The number of questions then tracks the gap near the goal, not the length of the chain.

## Main ideas presented (10 beats)

1. **The ask (hook).** Gate designed, graph built; now it runs. How to evaluate without waste or assumption?
2. **The rule (framework-first).** Three moves — evaluate never assume · pass → prune, fail → descend · hard gates, soft diagnose (test the connection) — before any example.
3. **The loop.** Top down from the goal: grade node → grade connection → pass → prune subtree; node fail → descend; soft = diagnostics; advance iff every hard prereq satisfied. Cost ∝ the gap near the goal.
4. **Evaluate, don't assume (the upgrade).** Earlier demo pruned against a declared knows-list; now every skip is earned by a passing answer.
5. **Item pools, one per learner.** Several questions per concept/edge; the engine samples one item per learner, deterministically — no two identical tests, from one approved pool. MCQ graded offline; open-ended a seam.
6. **The worked example.** Goal = immune checkpoint inhibitors. STU-A: immunology passes (prune), treatment basics fails (descend) → gap = basics of cancer treatment; 6 items, 2 pruned. STU-B: both hard branches pass (prune) → advance; 5 items, 3 pruned. Foundations never tested — the topics above passed.
7. **At scale + the honest boundary.** Real graph: 220 concepts, 248 edges, 536-item pool; a learner saw 5 items, gap pinned to Mutations. MCQ grading is done; item text at scale is stubs; open-ended is off until a gold set; edges pending faculty.
8. **Verdict.** Runs end to end; nothing assumed; descend on fail; measures the gap (5 of 536); MCQ live, the rest next.
9. **Your turn (CTA).** Test before you trust; prune on a pass, descend on a fail; pull from one approved pool; measure the gap.
10. **Outro.** Design the gate, build the graph, then let it run.

## Current implementation boundary

The engine is **real and running**; the demonstrations use real MCQ grading (STU-A/STU-B) and a real-scale run (STU-SIM). It does **not** claim a learning gain, and the scale run is **not** a claim about question quality:

- **MCQ grading** is finished (offline exact-match, free, reproducible).
- **Scale item text** is **template stubs** — real questions are the next step (LLM-draft, faculty-approve).
- **Open-ended grading** is a **seam** (`--open-grader defer|keywords|llm`), off until a small human-graded gold set calibrates the judge.
- The gate **depends on faculty-approved edges** (hard/soft typing), still pending.

## The reusable framework (apply it to a new assessment)

1. **Evaluate, never assume** — test every prerequisite; earn every skip with a passing answer.
2. **Pass → prune, fail → descend** — a pass trusts the subtree; a fail localises the gap.
3. **Hard gates, soft diagnose** — block only on hard links; test the *connection*, not just the concept.

Decision rule: advance iff every hard prerequisite is satisfied; else hold and remediate to the gap. Cost tracks the gap near the goal, not chain length.

## Research grounding

Knowledge Space Theory (Doignon & Falmagne, 1985) for minimal testing under a prerequisite structure (the prune-and-descend basis); Bayesian Knowledge Tracing (Corbett & Anderson, 1995) and the mastery-threshold study (Zhang et al., EDM 2025) for the confidence bar; SINKT (2024) for the LLM-plus-graph direction; the curriculum-grounded LLM-as-judge (Xu et al., 2026) for open-ended grading.

## Research prompt

> Research the "Evaluate, Then Advance" evaluation-pipeline explainer. Begin with `sources/weekly_report_2026-09-27.md`, `evaluation_pipeline.md`, the two gate_result CSVs, and `beat_sheet.json`. Identify the rule (evaluate-never-assume / pass-prune, fail-descend / hard-gate, soft-diagnose); the loop; item pools with one-item-per-learner sampling; the worked example (STU-A remediate→basics of cancer treatment, 6/2/closure 6; STU-B advance, 5/3/closure 6); and the scale run (220 concepts, 248 edges, 536 pool; STU-SIM 5 items, gap Mutations, closure 8). Return a claim table with exact source lines. Do not invent numbers. Never present the scale item text as real/approved, never claim open-ended grading is running, and never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each factual/numerical/capability claim: beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: the STU-A/STU-B/STU-SIM counts; 220/248/536; 5-of-536; "nothing assumed / earned pruning"; MCQ-live vs open-ended-seam; item-stubs; edges-pending-faculty. Flag any framing that treats stubs as real, open-ended as running, or asserts a learning gain.

## Typical commands

Run from the toolkit root, under `PYTHONUTF8=1`, venv Python for Kokoro, **temp on D:** (C: near-full):

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/evaluation-pipeline"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/evaluation-pipeline"
# stubborn beat (repeated Chrome cold-start timeout): render direct with a longer browser window:
npx remotion render src/index.ts <CompId> media/BXX.mp4 --props=p.json --scale=2 --crf=16 --timeout=120000
```

**Assembly (binding):** both video and audio via the concat **FILTER** (beats span sessions → stream-copy `-c copy` concat silently truncates; demuxer re-encode balloons duration). Verify the **video-stream** duration, not just the format duration:

```bash
ffmpeg -i b00.mp4 … -filter_complex "[0:v]…concat=n=N:v=1:a=0[v]" -map "[v]" -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p -r 30 v.mp4
ffmpeg -i b00.mp3 … -filter_complex "[0:a]…concat=n=N:v=0:a=1[a]" -map "[a]" -c:a aac -b:a 192k a.m4a
ffmpeg -i v.mp4 -i a.m4a -map 0:v:0 -map 1:a:0 -c copy -shortest -movflags +faststart OUT.mp4
ffprobe -select_streams v:0 -show_entries stream=duration OUT.mp4   # must be full length
ffmpeg -i OUT.mp4 -af volumedetect -f null -                       # mean ≈ −20 dB
```

## Beat-sheet and visual rules

- `beat_sheet.json` is the source of truth; audio duration is the clock (`durationInFrames = round(actual_duration_s × 30)`).
- Show the rule (three moves) **before** any example (framework-first).
- Every claim beat shows its real figure legibly; B05's two learners are side-by-side with counts; held ≥2s.
- **TEAL = pass/advance/prune, CRIMSON = fail/hold/remediate + draft, GOLD = the upgrade + hard emphasis, SAGE = soft/diagnostic, SLATE = pipeline/scale.**
- Never frame the scale stubs as real questions, open-ended as running, or assert a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration on the animated slate before audio; regenerate + remeasure on any change; run under `PYTHONUTF8=1`.

## Useful project files

- `output/evaluation-pipeline/PREMISE.md` — the rule + worked example + falsifiability + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must be qualified / not claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric (teaching 12/12)
- `VISUAL-PLAN.md` — per-beat treatment + legibility contract + render/assembly fixes
- `beat_sheet.json` — narration, timing, props, build state
- `remotion-src/EvaluationPipeline.tsx` (in the toolkit `runtime/remotion/src/`) — reel-local B01–B06 components
- `sources/` — the frozen story source (report, pipeline/example docs, the two gate_result CSVs, the two scripts)
- `_qc/` — frame-level QC + PROOF production-gate result (`REPORT.md`)
- final `.mp4` — the 4K 16:9 master

## Build result for this report

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 4:04), video stream verified full length;
- **audio verified present** (`volumedetect` mean ≈ −21.3 dB) via the concat filter;
- a complete end-to-end human review plus a PROOF pass (teaching 12/12; production gate PASS).

Build notes: the render fought persistent low-RAM Chrome cold-start timeouts (orphaned at several session boundaries, topped up across relaunches). One beat (B03) failed 7× on the default 25 s browser timeout and finally rendered via a direct `npx remotion render … --timeout=120000`. Assembly used the concat filter for both streams; the video-stream duration was verified full (244.4s), ruling out the stream-copy truncation seen previously.

## Current limitations

- scale item text is **template stubs**; open-ended grading is **off** (a seam); edges **pending faculty**;
- MCQ grading is real but the scale run proves the *pipeline*, not question quality;
- **no learning-outcome claim** — the gate decides readiness, not learning.

## Future work

- author real questions (LLM-draft a pool per prerequisite, faculty-approve once);
- turn on open-ended grading via the LLM-as-judge once a human-graded gold set exists;
- faculty approval of the prerequisite edges the gate depends on;
- wire real submitted answers through the live grader across more learners and goals.

## Final human checklist

- Can a viewer state the rule (evaluate / pass-prune, fail-descend / hard-gate, soft-diagnose) and apply it?
- Does B01 land the rule **before** any example?
- Is B05 the two-learner split (STU-A hold vs STU-B advance) with real counts, side-by-side?
- Does B06 show real-vs-draft (MCQ live / item stubs / open-ended off / faculty pending)?
- Is every figure traceable to `sources/`, with no learning-outcome claim?
- Is **audio present** and the **video stream full length** on the master?
- Did a human watch the complete output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
