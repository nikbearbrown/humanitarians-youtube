# Weekly Research Report: A Question for Every Step

**Fellow:** Satwik Reddy Sripathi
**Week ending:** October 2, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` — `weekly_report_2026-10-04.md`, `mcq_bank_README.md`, `mcq_bank_for_review.csv`, `student_roadmap_app.html`, and the three demo screenshots. Every on-screen figure traces to these.
**Source status:** The bank is **complete and mechanically validated** — 315 questions covering every concept and every hard prerequisite link, each with four options, an answer key, a one-line reason, a difficulty, and an exact chapter/section reference. What is **draft**: *every* question (the `approve` column is blank on all 315 rows; `llm_proposed`; `needs_review = yes`) — nothing is confirmed until a faculty member signs off. A few sections came through with **empty body text**, so those questions are anchored to the section title plus standard textbook facts rather than the exact wording — precisely the rows the review should catch. **No learning-outcome claim** is made — the bank is built and validated, not yet *verified*.

This weekly research video is the direct successor to the last two weeks: week 08 built the prerequisite graph, week 09 ran the evaluation gate on it (but on placeholder questions), and this week —

**an actual question exists for every part of the roadmap, and a working demo shows what a student sees — all drafted, validated, and ready for faculty to check.**

The answer is one rule in three moves: **cover everything** (one question for every topic, one for every hard prerequisite link — no gaps); **carry the receipts** (every question ships with four options, the answer, a one-line reason, a difficulty, and the exact chapter and section); and **ship it as a draft** (an empty approve column on every row — nothing trusted until a faculty member signs it off). A complete, sourced draft is what makes a review fast, and a review is what makes it real.

The final beat sheet contains **10 beats**. The complete video was generated locally with the free Brutalist toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4 lives in the reel folder and is distributed separately.

## What was built this week

- `mcq_bank_for_review.csv` — the bank: **315 questions = 219 topic (node) + 96 connection**. Columns: `approve`, `item_id`, `tests_type`, `tests_id`, `section_ref`, `question`, `options`, `answer_key`, `rationale`, `difficulty`, `provenance`, `needs_review`.
  - **219 topic questions** — one for every concept in the roadmap ("do you know this topic?").
  - **96 connection questions** — one for every hard prerequisite link ("how does one topic support the next?"), grounded in that prerequisite's own reason.
- `student_roadmap_app.html` — a working, offline student demo: pick a goal → build the roadmap (each step linked to its chapter and section, with a reason) → a quick check from the real questions (pass skips the topic and what it builds on; miss keeps it) → the roadmap from where the student actually is (done / start here / upcoming).
- `mcq_bank_README.md` + three demo screenshots documenting the bank and the flow.

Mechanical validation that passed: every concept and every hard edge has a question; every question has four options; every answer key matches one of its options; difficulty set (1 to 3) on every row.

The upgrade over week 09: the gate no longer runs on template stubs. There is now a real, sourced question for every node and every hard edge — a complete draft a reviewer can act on row by row.

## How this connects to the series

Weeks 00–06 built and justified the roadmap; **week 07** designed the test-to-advance gate; **week 08** built the prerequisite graph; **week 09** ran the evaluation pipeline on that graph (on placeholder items); **week 10 writes the real questions** the gate needs and shows the student-facing demo. It is the last piece before faculty verification turns the draft bank into an approved one.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> How do you make a whole curriculum's questions something a faculty reviewer can actually verify — covering every topic and every link, with the evidence on each row, and nothing trusted until it's signed off?

The proposed answer: cover everything (a question per topic and per hard link), carry the receipts (options, answer, reason, difficulty, exact section on every row), and ship as a draft (an empty approve column — complete and validated, but not verified until faculty sign off).

## Main ideas presented (10 beats)

1. **The ask (hook).** The gate ran last week, but on placeholder questions. The real next step: a real question for every part of the roadmap, plus a student demo, made so faculty can verify it.
2. **The rule (framework-first).** Three moves — cover everything · carry the receipts · ship as a draft — before any count.
3. **The bank at scale.** 315 questions = 219 topic + 96 connection; validated: every concept and hard edge covered, every question four options, every answer key matches one.
4. **Anatomy of a question.** One real MCQ in full — Ch1 Normal Cell Biology, "which molecule is most abundant in cells, 70%+ of total mass?" → Water (options Water/Protein/DNA/Lipid), a one-line reason tied to the section, difficulty 1/3, the exact section ref — everything a reviewer needs in one row.
5. **Node vs connection.** A topic question asks "do you know this?"; a connection question asks "how does one topic support the next?" — e.g. "how do mutations support how oncogenes get activated?" → "oncogene activation is caused by specific mutation types, so you need mutations first." The connection question tests the link, not just the facts.
6. **The demo.** The student experience end to end, offline in a browser: pick a goal → the roadmap (steps + chapter/section + why) → a quick check → where you are (done / start here / upcoming).
7. **The honest boundary.** Every question a draft (approve blank, llm_proposed, needs_review=yes); a few empty-body sections anchored to title + standard facts; complete and validated, but not yet verified → needs faculty.
8. **Verdict.** A question for every topic and hard link (315), each with its receipts, all drafts; a working demo; built and validated — what's left is the part only faculty can do: verify it.
9. **Your turn (CTA).** Cover every node and link; make every question carry its answer, reason, and exact source; leave an approve column for the expert.
10. **Outro.** The roadmap, the gate, and now the questions — drafted, and ready to check.

## Current implementation boundary

The bank is **complete and mechanically validated**; it is **not** verified, and makes **no** claim about question quality or learning outcomes:

- **Coverage + structure** are checked (every concept and hard edge has a question; four options each; answer key matches an option; difficulty set).
- **Every question is a draft** — `approve` blank, `llm_proposed`, `needs_review = yes`. Nothing is approved.
- **Empty-body sections** are anchored to the section title + standard textbook facts, not the exact wording — flagged for the review to catch.
- **Correctness of each question** (does the answer and reason actually fit the section?) is exactly what faculty verification decides.

## The reusable framework (apply it to a new question bank)

1. **Cover everything** — one question per concept and one per hard prerequisite link; no gaps.
2. **Carry the receipts** — every row ships its options, answer, a one-line reason, a difficulty, and the exact source section.
3. **Ship as a draft** — leave an approve column empty; a complete, sourced draft is what makes a faculty review fast, and the review is what makes it real.

## Research grounding

Automatic question generation from course text (the LLM-draft, human-approve pattern); the prerequisite structure from weeks 08–09 (which topic depends on which) as the backbone the questions are generated against; the curriculum-grounded reviewer loop (faculty sign-off as the source of truth, not the generator).

## Research prompt

> Research the "A Question for Every Step" MCQ-bank explainer. Begin with `sources/weekly_report_2026-10-04.md`, `mcq_bank_README.md`, `mcq_bank_for_review.csv`, `student_roadmap_app.html`, and `beat_sheet.json`. Identify the rule (cover everything / carry the receipts / ship as a draft); the counts (315 = 219 topic + 96 connection); the real example question (Ch1, most-abundant-molecule → Water) and the real connection example (mutations → oncogene activation); the demo flow (pick a goal → roadmap → quick check → where you are); and the honest boundary (every question a draft, empty-body sections, validated but not verified). Return a claim table with exact source lines. Do not invent numbers. Never present a draft question as approved, and never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each factual/numerical/capability claim: beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: 315 = 219 + 96; "one per concept / one per hard link"; the Water example and its options; the mutations→oncogenes example and its answer; the four-options / answer-matches validation; "every question a draft (approve blank, llm_proposed, needs_review=yes)"; the empty-body-sections caveat; "complete and validated but not verified." Flag any framing that treats a draft as approved, the validation as verification, or asserts a learning gain.

## Typical commands

Run from the toolkit root, under `PYTHONUTF8=1`, venv Python for Kokoro, **temp on D:** (C: near-full):

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/mcq-bank-demo"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/mcq-bank-demo"
# stubborn beat (repeated Chrome cold-start timeout): re-run --only BXX at concurrency 1,
# or render direct with a longer browser window:
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
- Show the rule (three moves) **before** any count (framework-first).
- Every claim beat shows its real figure legibly; B03 is one real MCQ in full with Water highlighted; B04 is topic-vs-connection side by side; B06 is done-vs-draft side by side; each held ≥2s.
- **TEAL = correct/covered/primary, GOLD = the key example/receipts emphasis, SAGE = pass/validated, CRIMSON = the draft/falsifiability caveats, SLATE = the bank/scale substrate.**
- Never frame a draft question as approved, the mechanical validation as faculty verification, or assert a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration on the animated slate before audio; regenerate + remeasure on any change; run under `PYTHONUTF8=1`.

## Useful project files

- `output/mcq-bank-demo/PREMISE.md` — the rule + worked example + falsifiability + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must be qualified / not claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric
- `VISUAL-PLAN.md` — per-beat treatment + legibility contract + render/assembly fixes
- `beat_sheet.json` — narration, timing, props, build state
- `McqBankDemo.tsx` (in the toolkit `runtime/remotion/src/`) — reel-local B01–B06 components
- `sources/` — the frozen story source (weekly report, bank CSV + README, the demo HTML + screenshots)
- `_qc/` — frame-level QC + PROOF production-gate result (`REPORT.md`)
- final `.mp4` — the 4K 16:9 master

## Build result for this report

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 3:47 — video stream 226.67s, verified full length);
- **audio verified present** (`volumedetect` mean ≈ −21.3 dB) via the concat filter;
- a complete end-to-end frame-level QC plus a PROOF pass (production gate PASS; `_qc/REPORT.md`).

Build notes: all ten beats rendered at `--scale=2` (true 3840×2160). Nine rendered on the first pass; B08 hit the low-RAM 25 s Chrome cold-start timeout once and rendered cleanly on a `--only B08` retry at concurrency 1. Assembly used the concat filter for both streams; the video-stream duration was verified full length, ruling out the stream-copy truncation seen previously.

## Current limitations

- **every question is a draft** (approve blank, llm_proposed, needs_review=yes) — none approved;
- a few **empty-body sections** are anchored to title + standard facts, not exact wording;
- the bank is **validated but not verified** — correctness per row is what faculty decide;
- **no learning-outcome claim** — the bank is built and checked, not shown to teach.

## Future work

- faculty verification of `mcq_bank_for_review.csv` row by row (set `approve`, fix, note);
- prioritise the 96 connection questions (they test the links the roadmap depends on);
- wire the approved bank into the week-09 gate so it runs on real, verified questions;
- fill the empty-body sections from the exact source text once available.

## Final human checklist

- Can a viewer state the rule (cover everything / carry the receipts / ship as a draft) and apply it?
- Does B01 land the rule **before** any count?
- Does B03 show one real MCQ in full with the correct answer highlighted and its section ref?
- Is B04 the topic-vs-connection split with the real mutations→oncogenes example?
- Does B06 show complete-and-validated vs still-a-draft, with the empty-body caveat and the "needs faculty" stamp?
- Is every figure traceable to `sources/`, with no draft framed as approved and no learning-outcome claim?
- Is **audio present** and the **video stream full length** on the master?
- Did a human watch the complete output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
