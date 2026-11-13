# Weekly Research Report: Three Tiers, One Plan

**Fellow:** Satwik Reddy Sripathi
**Week ending:** October 10, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` — `weekly_report_2026-10-10.md`, `prerequisites_README.md`, `topic_reading_order.csv`, `chapter_reading_order.csv`, `question_coverage.csv`, `student_roadmap_app.html`, `demo_roadmap_3tier.png`. Every on-screen figure traces to these.
**Source status:** The three-tier graph is **committed and consistent** — 1,283 section-level links sorted into required / recommended / curious, 302 chapter-level links derived, and **0 cycles** (every prerequisite comes earlier in the book). The question bank is **mapped** onto the sections. What is **draft**: *every* prerequisite link (`approve` blank, `provenance = llm_proposed / derived`, `needs_review = yes`); the questions are **borrowed** from the collaborators' bank and **5 titles** still need reconciling. **No learning-outcome claim** is made — the structure is done and consistent, not yet *verified*.

This weekly research video follows directly from the review cycle: faculty looked at the prerequisite graph and raised two points — a broadly useful chapter like Introduction to Cancer should appear in far more plans, and a single required-versus-helpful split was not enough. So this week —

**the prerequisites were rebuilt around three tiers, and the real question bank was attached so every step comes with its questions.**

The answer is one framework in three tiers: **required** (*you have to know this* — the target can't be understood without it, so these gate advancement, kept strict and small); **recommended** (*you better know this* — strongly helps and you'll likely struggle without it, but never blocks, and this is where broadly foundational chapters live); and **curious** (*aren't you curious about this* — related and enriching, not needed, the lateral and synthesis links). Required gates, recommended helps, curious invites.

The final beat sheet contains **10 beats**. The complete video was generated locally with the free Brutalist toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4 lives in the reel folder and is distributed separately.

## What was built this week

- **A three-tier prerequisite graph** (committed). 1,283 section-level links = **298 required + 575 recommended + 410 curious**; 302 chapter-level links derived from them. Every prerequisite comes earlier in the book, so the reading order is acyclic (**0 cycles**). Appendices excluded entirely (reference material, never a step).
- **Plain-language reading-order files** for faculty (`topic_reading_order.csv`, `chapter_reading_order.csv`) with tiers shown as *Read this first / Better to know / Curious extra*, each row carrying a reason and an `approve` column.
- **The question bank, integrated.** The collaborators' bank was mapped onto our sections by chapter and title: **1,544 of 1,584 questions matched (97.5%)**, about 8 per section across **193 sections**; only 5 titles didn't line up (reconciled by hand). Questions are keyed to sections, so the plan chains: a goal → its prerequisites → the sections → the questions.
- **The demo app, updated** to run on the three tiers and the real questions: pick a goal, optionally mark what you know, get a bounded plan (the required backbone in order plus recommended and curious alongside, each linked to its chapter and section with a reason and a tier), and take a quick check from the real questions.

The upgrade over week 10: the binary required-vs-helpful split could not express "broadly foundational but not required." The middle tier fixes that — **Chapter 2 (Introduction to Cancer) is now a prerequisite for 109 topics**, almost all of them recommended.

## How this connects to the series

Weeks 00–06 built and justified the roadmap; **week 07** designed the test-to-advance gate; **week 08** built the first prerequisite graph; **week 09** ran the evaluation pipeline; **week 10** wrote a real question for every step; **week 11 re-tiers the prerequisites** on faculty feedback and **attaches the question bank** so the whole plan is driven by one connected structure. It is the piece that turns the graph into a right-sized, question-backed reading plan — and the last structural step before faculty verification.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> How do you turn a prerequisite graph into a reading plan that is right-sized — strict where it has to be, generous where it helps — with a real question behind every step?

The proposed answer: sort every prerequisite into three tiers (required gates, recommended helps, curious invites), keep required strict so it can gate, and attach the questions to the same sections so every step comes with a check.

## Main ideas presented (10 beats)

1. **The ask (hook).** Faculty feedback: a broadly useful chapter should appear in more plans, and two tiers weren't enough. So: rebuild into three tiers and attach the question bank.
2. **The framework (framework-first).** The three tiers — required (gates) / recommended (helps) / curious (invites) — before any count.
3. **The tiers at scale.** 1,283 section links = 298 required + 575 recommended + 410 curious; 302 chapter links derived; 0 cycles; appendices excluded.
4. **Why three, not two.** Genetics (Ch4) requires Ch1 (can't be understood without cell biology) but only recommends Ch2 (broadly foundational, not blocking). The binary split had nowhere for "broadly foundational." Result: Chapter 2 is now a prerequisite for 109 topics, almost all recommended.
5. **Questions attach to the prerequisites.** The chain: a goal → its prerequisites → the sections → the questions. 1,544 of 1,584 matched (97.5%), ~8 per section over 193 sections; 5 titles unmatched.
6. **The demo.** Goal = immune checkpoint inhibitors (Ch25) → 8 required + 8 recommended + 3 curious, in reading order, each linked to chapter/section with a reason and a tier; a quick check from the real questions; bounded to ~15 readings.
7. **The honest boundary.** Committed and acyclic, but every link is a draft (llm_proposed/derived, needs_review=yes); the questions are borrowed, 5 titles unmatched; the tiers (especially what counts as required) and the questions need faculty.
8. **Verdict.** Three tiers over 1,283 links with 0 cycles; a middle tier that fits the broadly foundational; the bank attached (97.5%); a bounded tiered plan. Committed and consistent — verification is the faculty's part.
9. **Your turn (CTA).** Don't settle for required-vs-helpful; add a middle tier and a light one; keep required strict so it can gate; attach assessments to the same nodes; leave an approve column.
10. **Outro.** The roadmap, the gate, the questions, and now three tiers that say what to read first, what helps, and what's just interesting.

## Current implementation boundary

The three-tier graph is **committed and consistent**; it is **not** verified, and makes **no** claim about tier correctness or learning outcomes:

- **Structure + acyclicity** are checked (1,283 links sorted into tiers; every prerequisite earlier in the book; 0 cycles; appendices excluded).
- **Every link is a draft** — `approve` blank, `provenance = llm_proposed / derived`, `needs_review = yes`. Nothing is approved.
- **Questions are borrowed** from the collaborators' bank and mapped by chapter/title; **5 titles unmatched**, reconciled by hand.
- **Tier correctness** (is this link really required vs recommended vs curious?) and **question correctness** are exactly what faculty verification decides.

## The reusable framework (apply it to a new reading plan)

1. **Three tiers, not two** — required (gates), recommended (helps, where broadly foundational chapters live), curious (invites).
2. **Keep required strict** — so it can actually gate advancement; let recommended and curious guide without blocking.
3. **Attach assessments to the same nodes** — so a goal pulls its prerequisites, the prerequisites pull the sections, and each section pulls its questions; leave an approve column for the expert.

Decision rule: take the required chain in full; attach recommended and curious to the goal and its backbone rather than expanding them deep, so a plan stays bounded (~15 readings, not dozens).

## Research grounding

Textbook-structure prerequisite extraction (what must be understood first, read from chapter/section order and shared concepts); the three-tier softening of a strict dependency graph (required / recommended / curious) to fit broadly-foundational material; question-bank alignment keyed to sections so assessment and prerequisites share one structure.

## Research prompt

> Research the "Three Tiers, One Plan" explainer. Begin with `sources/weekly_report_2026-10-11.md`, `prerequisites_README.md`, `topic_reading_order.csv`, `chapter_reading_order.csv`, `question_coverage.csv`, and `beat_sheet.json`. Identify the three tiers (required/recommended/curious) and what each does; the counts (1,283 = 298 + 575 + 410; 302 chapter links; 0 cycles; appendices excluded); why three not two (Ch4 requires Ch1, recommends Ch2; Ch2 → 109 topics); the question integration (goal → prereqs → sections → questions; 1,544/1,584 = 97.5%, ~8/section, 193 sections, 5 unmatched); and the demo (immune checkpoint inhibitors → 8 required / 8 recommended / 3 curious, bounded ~15 readings). Return a claim table with exact source lines. Do not invent numbers. Never present a draft link as approved, and never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each factual/numerical/capability claim: beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: the three tier definitions; 1,283 = 298 + 575 + 410; 302 chapter links; 0 cycles; appendices excluded; the Ch4→Ch1(required)/Ch2(recommended) example; Ch2 → 109 topics; 1,544/1,584 (97.5%), ~8/section, 193 sections, 5 unmatched; the demo counts (8/8/3) and ~15 readings; "every link a draft (llm_proposed/derived, needs_review=yes)"; "questions borrowed." Flag any framing that treats a draft as approved, consistency as verification, or asserts a learning gain.

## Typical commands

Run from the toolkit root, under `PYTHONUTF8=1`, `.venv` Python for Kokoro, **temp on D:** (C: near-full):

```bash
PYTHONUTF8=1 ".venv/Scripts/python.exe" runtime/scripts/generate_audio_kokoro.py "/abs/path/to/three-tier-plan"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/three-tier-plan"
# stubborn beat (repeated Chrome cold-start timeout): re-run --only BXX at concurrency 1,
# or render direct with a longer browser window:
npx remotion render src/index.ts <CompId> media/BXX.mp4 --props=p.json --scale=2 --crf=16 --timeout=120000
```

**Assembly (binding):** both video and audio via the concat **FILTER** (beats span sessions → stream-copy `-c copy` concat silently truncates; demuxer re-encode balloons duration). Verify the **video-stream** duration, not just the format duration, plus `volumedetect` ≈ −20 dB.

## Beat-sheet and visual rules

- `beat_sheet.json` is the source of truth; audio duration is the clock (`durationInFrames = round(actual_duration_s × 30)`).
- Show the framework (three tiers) **before** any count (framework-first).
- Every claim beat shows its real figure legibly; B03 is the one-target-two-tiers contrast; B06 is committed-vs-draft side by side; each held ≥2s.
- **TEAL = required / gates, GOLD = recommended / the key example, SLATE = curious / scale, SAGE = done / committed, CRIMSON = draft / caveats.** Tier colors stay consistent across all body beats.
- Never frame a draft link as approved, consistency as faculty verification, or assert a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration on the animated slate before audio; regenerate + remeasure on any change; run under `PYTHONUTF8=1`.

## Useful project files

- `output/three-tier-plan/PREMISE.md` — the framework + worked spine + falsifiability + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must be qualified / not claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric
- `VISUAL-PLAN.md` — per-beat treatment + legibility contract + render/assembly fixes
- `beat_sheet.json` — narration, timing, props, build state
- `Week11Tiers.tsx` (in the toolkit `runtime/remotion/src/`) — reel-local B01–B06 components
- `sources/` — the frozen story source (weekly report, prereq README, reading-order + coverage CSVs, demo HTML + PNG)
- `_qc/` — frame-level QC + PROOF production-gate result (`REPORT.md`)
- final `.mp4` — the 4K 16:9 master

## Build result for this report

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 4:28 — video stream 268.0s, verified full length);
- **audio verified present** (`volumedetect` mean ≈ −21.5 dB) via the concat filter;
- a complete end-to-end frame-level QC plus a PROOF pass (production gate PASS; `_qc/REPORT.md`).

Build notes: eight beats rendered on the first 4K pass; B07 and B09 (both shared claude scenes) each hit the low-RAM 25s Chrome cold-start timeout once and rendered cleanly on a `--only` retry at concurrency 1. Assembly used the concat filter for both streams; the video-stream duration was verified full length (268.0s).

## Current limitations

- **every prerequisite link is a draft** (approve blank, llm_proposed/derived, needs_review=yes) — none approved;
- the **questions are borrowed** from the collaborators' bank; 5 titles unmatched;
- the graph is **consistent (0 cycles) but not verified** — tier correctness is what faculty decide;
- **no learning-outcome claim** — the plan is structured and bounded, not shown to teach.

## Future work

- faculty verification of the tiers (especially what counts as *required*) and the questions;
- reconcile the 5 unmatched question titles;
- decide whether the question text (from the collaborators' bank) is committed to the repo or kept local;
- wire the verified tiers + questions into the week-09 gate so it runs on the real structure.

## Final human checklist

- Can a viewer name the three tiers and what each does (gate / help / invite)?
- Does B02 show the counts (1,283 = 298 + 575 + 410) and 0 cycles, after the framework?
- Does B03 make the case for a middle tier (Ch1 required vs Ch2 recommended; Ch2 → 109)?
- Does B04 show the chain (goal → prereqs → sections → questions) with real coverage (97.5%)?
- Does B06 show committed-and-acyclic vs still-a-draft, with the "needs faculty" stamp?
- Is every figure traceable to `sources/`, with no draft framed as approved and no learning-outcome claim?
- Is **audio present** and the **video stream full length** on the master?
- Did a human watch the complete output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
