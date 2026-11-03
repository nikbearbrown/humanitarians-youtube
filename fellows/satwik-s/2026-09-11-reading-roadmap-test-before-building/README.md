# Weekly Research Report: Test Before You Advance

**Fellow:** Satwik Reddy Sripathi
**Week ending:** September 11, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** The single frozen source `source/test_to_advance_gate.tex` (+ rendered `.pdf`), the technical write-up "Dependency-Aware Test-to-Advance Gating — the assessment layer of the personalized reading roadmap." Every on-screen figure traces to it, and it was produced by the running engine (`scripts/run_assessment.py`).
**Source status:** The **engine numbers are real** (a six-file model + deterministic grader + top-down/prune/descend engine, run on a 22-concept / 26-edge slice seeded from Chapter 27). What is **draft**: the hard/soft edge typing and the six seed assessment items are auto-proposed, marked `needs_review = yes` — **no row is faculty-approved**. Grading is deterministic offline answer-key matching; open-ended (LLM-as-judge) grading is a **separate, phase-two proposal**. **No learning-outcome claim** is made — the gate proves *readiness*, not learning gains.

This weekly research video answers the question Prof. Nik set after the "Robot Tutor" discussion — *start with what everyone does: a sequence to be learned in order, and a test before you move forward:*

**Ordering a curriculum by dependency is not enough — ordering never checks that a learner actually holds a prerequisite before advancing. How do you test readiness, cheaply and honestly, without quizzing the whole chain behind the goal?**

The video answers with a **reusable framework — a test-to-advance gate in three moves:** **(1) test the edge**, not just the nodes — a *connection item* asks "how is B built on A?" and catches the learner who knows two topics as isolated facts but not how one rests on the other; **(2) prune + descend** — direct prerequisites only, skip the known, descend only on failure, so cost tracks the gap near the goal, not the length of the chain; **(3) hard edges gate, soft edges only diagnose.** It then walks two learners through the gate on one real goal, and marks exactly what is running versus what is still a draft.

The final beat sheet contains **10 beats**. The complete video was generated locally using the free Brutalist toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4 lives in the reel folder and is distributed separately.

## How this connects to the series (and to Prof. Nik's note)

Prof. Nik's guidance was to **start with the standard baseline everyone builds** — "a sequence needs to be learned before this, and let's test you before you move forward first" — and only then layer on the richer learner model from the *Robot Tutor* video and the outcome-over-engagement angle from the OBER (week-06) video. This film is that baseline. It reuses the dependency graph (weeks 00–05) as the **assessment substrate** and lands OBER's "outcomes + assessment items" idea as a running artifact. The key honest move is the **connection item**: adaptive tutors typically know a student only through right/wrong on isolated topics; testing the *edge* is the first step past that thin model.

## Production state

- Premise / reusable-framework gate (PROOF Phase 1): completed (`PREMISE.md`)
- Plan and beat structure: completed (derived from `test_to_advance_gate.tex`)
- Narration generation: completed (Kokoro `af_bella`, run under `PYTHONUTF8=1`)
- Audio timing: completed (measured durations are the clock; total ≈ 4:14)
- Visual beats: 10 of 10 filled (16:9 `TestToAdvanceGate.tsx` for B01–B06 + shared claude scenes for B00/B07/B08/B09)
- Local compilation: completed — **4K 16:9 (3840×2160)** via stream-copy assembly
- Full-video review + PROOF production gate: completed (teaching 12/12; gate PASS; `_qc/REPORT.md`)
- **Audio verified present** (`volumedetect` mean ≈ **−21.5 dB**, not the −91 dB silence bug)
- Formal claim-level fact-check: figures traced to `SOURCES.md`; requires final human sign-off before publication
- YouTube publishing: handled separately through the Humanitarians AI review process

## Deliverables

| File (`outputs/test-to-advance-gate/`) | Aspect | Resolution | Duration | Audio |
|---|---|---|---|---|
| `week7_test-to-advance-gate_sep11.mp4` | 16:9 | 3840×2160 (4K) | 4:14 | −21.5 dB ✓ |

A ≤1-min **4K 9:16 Short** (B01 framework + B05 two-learners + B09) can be added on request via portrait `916` components.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## What this video is about

**Topic:** The assessment layer of the reading roadmap — a dependency-aware gate that checks a learner *holds* a prerequisite before advancing.

For six films the roadmap ordered *what* to read. Ordering, though, never verifies readiness: a learner can be sequenced to a concept they aren't prepared for. This week adds the **test-to-advance gate** — and does it the honest, cheap way, then shows exactly the two-learner case where a naive (node-only) quiz would get it wrong.

The result is a **reusable framework** a viewer can apply to any prerequisite-gated curriculum: test the edge, prune + descend, and let only hard edges block.

## Central question

> Ordering says what comes next. How do you prove a learner is *ready* for it — testing the dependency itself, cheaply, without quizzing the entire chain?

The proposed answer: test the **edge** (a connection item verifies the dependency, not just the two endpoints); keep it short by **pruning** the known and **descending only on failure**; and let **hard** edges gate while **soft** edges only diagnose.

## Main ideas presented (10 beats)

1. **The ask (hook).** Ordering never checks that a learner *holds* a prerequisite before advancing. How do you test readiness without quizzing the whole chain?
2. **The framework (framework-first).** A test-to-advance gate in three moves — **test the edge · prune + descend · hard gates, soft diagnose** — shown before any file, item, or learner.
3. **The six-file model.** Four authored CSVs (`concepts`, `dependencies`, `items`, `students`) → engine → two derived CSVs (`responses`, `gate_result`). Every file is a spreadsheet faculty can open and correct.
4. **Move 1 · test the edge.** A *concept item* asks "do you know this node?"; a *connection item* asks "how is the target built on this prerequisite?" A learner can ace both endpoint quizzes and still fail the connection — only the edge question catches it.
5. **Move 2 · prune + descend.** Test only the direct prerequisites (depth 1); skip the known; descend only when a prerequisite fails (a pass implies its subtree — the surmise relation, Knowledge Space Theory). Questions track the gap near the goal, not the chain length.
6. **The two learners (worked example · falsifiability).** Goal `CH27-S01-SS02`. **STU001** passes both prerequisite *nodes* but fails *connection e1* → because e1 is hard, **GATE HOLD → remediate to CH16-S05** (5 tested, 0 pruned). **STU002** had one prerequisite already placed → **pruned** (4 tested, 1 pruned) → **GATE OPEN → advance**. A node-only quiz would have advanced STU001.
7. **The honest boundary.** What's real (engine runs; deterministic offline grading) vs draft (hard/soft typing + six items, `needs_review`, none faculty-approved). **Question format:** multiple-choice first (approved pool, answer-key grade); open-ended → LLM-as-judge is phase-two, only once it agrees with humans on a gold set. A working baseline, not a finished system.
8. **Verdict.** Order + gate; test the link; stay short; hard-only gates; drafts pending faculty — the standard prerequisite gate, built to be corrected.
9. **Your turn (CTA).** One target → its direct hard prerequisites → one connection item each → mark hard/soft → run (skip known, test direct, descend on fail). Watch the tests audit the graph: a "hard" edge nobody ever fails probably isn't hard.
10. **Outro.** Order tells you what to read next; a test tells you you're ready.

## Current implementation boundary

The video establishes a **running assessment gate** and a reusable way to design one. It does **not** claim the gate improves learning outcomes, and it does **not** treat the draft edges/items as authoritative.

- The gate proves **readiness** (holds the prerequisite + understands the link), not learning gains;
- the hard/soft typing (threshold `conf ≥ 0.67`) and the six items are **auto-proposed drafts**, `needs_review = yes`, **no faculty approval**;
- in the worked example, grading is **simulated** (an item passes iff its concept/edge is in the learner's `knows` set); the **control flow, pruning, and decisions are real**. Production = deterministic answer-key matching;
- open-ended grading (LLM-as-judge) is a **separate proposal**, decided against a held-out gold set.

Future work: author + faculty-review items for the full Chapter-27 chain; replace the simulated grader with real answer-key matching on submitted responses; add a **placement mode** (find where a learner should *start*); use accumulated connection-item outcomes to validate — and where warranted re-type — the dependency edges themselves.

## The reusable framework (apply it to a new case)

Build a test-to-advance gate for any prerequisite-gated curriculum:

1. **Test the edge** — for each hard prerequisite, write a *connection item* ("why does the target depend on this?"), not just a node quiz on each endpoint.
2. **Prune + descend** — test only the target's *direct* prerequisites; skip what the learner already knows; descend into a prerequisite's own prerequisites only when it fails.
3. **Hard gates, soft diagnose** — type each edge: hard edges block advancement; soft edges are reported but never block.

Decision rule: a gate should be **short and honest**. Good result = it localises the exact gap and holds only on real (hard) failures; bad result = a node-only quiz that advances a learner who can't connect the pieces, or a whole-chain quiz that tests what the learner already knows.

## How faculty review is used

Faculty review resolves the one expert-judgment step the gate deliberately leaves open: whether each **auto-proposed edge type** (hard vs soft) and each **draft item** is authoritative. The `conf ≥ 0.67 → hard` threshold is a defensible default *surfaced for review*, not hidden. A useful by-product: accumulated **connection-item outcomes audit the graph** — a "hard" edge whose connection nobody ever fails is probably not hard, and a hard edge whose failure predicts failure at the target is confirmed. Until faculty sign off, every authored row is a **draft**, and the video says so on screen.

## Research prompt

Use the following prompt before substantially rewriting this film:

> Research the "Test Before You Advance" dependency-aware test-to-advance gate. Begin with `source/test_to_advance_gate.tex`, then `SOURCES.md`, `PREMISE.md`, and `beat_sheet.json`. Identify the three moves (test the edge / prune + descend / hard-gate soft-diagnose); the six-file model (4 authored + 2 derived); the two edge types and two item types; the top-down/prune/descend logic (surmise relation, KST); the slice (22 concepts, 26 edges; 11 hard / 15 soft; threshold 0.67); and the two-learner worked example (STU001 gate-hold on connection e1, 5 tested / 0 pruned; STU002 gate-open with one pruned, 4 tested / 1 pruned; closure 3). Return a claim table: claim, exact source line, evidence, confidence, and what still requires verification. Do not invent numbers. Never present the draft edges/items as faculty-approved, and never claim a learning-outcome improvement.

## Fact-check prompt

Run the following prompt after any narration or beat-sheet change:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and capability claim and compare each with `source/test_to_advance_gate.tex` and `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Pay particular attention to: the six-file model; 22/26 and 11/15 and the 0.67 threshold; the STU001/STU002 decisions and tested/pruned/closure counts; the "passes both nodes, fails the connection" fact; the deterministic-grading claim; and the MC-first / open-ended-phase-two framing. Flag any framing that treats drafts as approved, any learning-outcome claim, and any number not in the source. Do not silently rewrite narration; list corrections for human review.

## Typical commands

Run from the Brutalist toolkit root. On Windows, prefix Python with `PYTHONUTF8=1` so on-screen middots / arrows / ≠ / ✓ / ✕ do not corrupt, and use the toolkit venv Python for Kokoro.

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/test-to-advance-gate"
# 4K beats — redirect temp to D: if C: is low on space (see build note):
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=3 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/test-to-advance-gate"
# top up any transient Chrome-launch timeout at concurrency 1:
... python runtime/scripts/remotion_scenes.py "/abs/path/to/test-to-advance-gate" --only B05
```

**Audio assembly (binding Windows fix).** Build the master audio with the concat **FILTER**, not the demuxer — the demuxer yields a **silent** track (−91 dB) from 24 kHz-mono Kokoro mp3s on this ffmpeg build:

```bash
ffmpeg -i b00.mp3 … -filter_complex "[0:a][1:a]…concat=n=N:v=0:a=1[a]" -map "[a]" -c:a aac -b:a 192k _a.m4a
ffmpeg -f concat -safe 0 -i _v.txt -c copy -fflags +genpts _v.mp4          # stream-copy video
ffmpeg -i _v.mp4 -i _a.m4a -map 0:v:0 -map 1:a:0 -c copy -shortest -movflags +faststart OUT.mp4
ffmpeg -i OUT.mp4 -af volumedetect -f null -                               # VERIFY mean ≈ −20 dB, not −91
```

## Beat-sheet and visual rules

- Treat `beat_sheet.json` as the source of truth; audio duration is the timing clock (`durationInFrames = round(actual_duration_s × 30)`).
- Show the three moves **before** any file/item/learner (framework-first).
- Every claim beat shows its real figure legibly at the moment of the claim; B05's two learners are **side-by-side**, the failed connection and the pruned node both visible, held ≥2s.
- **CRIMSON = gate-hold / a failed connection / remediate; TEAL = advance/pass; GOLD = the connection-item insight; SAGE = soft/diagnostic; SLATE = the six-file substrate.**
- Never frame the draft edges/items as faculty-approved; keep `needs_review` and "none faculty-approved" wherever the topic arises. No learning-outcome claim.

## Voice and narration

Kokoro `af_bella` ("Bella"), recorded in `beat_sheet.json`; register **pragmatist / skeptical-explainer**; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration on the animated slate before generating audio; regenerate + remeasure whenever narration changes; on Windows always run audio/render/compile under `PYTHONUTF8=1`.

## Useful project files

- `outputs/test-to-advance-gate/PREMISE.md` — the three-move framework + falsifiability + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must be qualified; what must not be claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric (teaching 12/12)
- `VISUAL-PLAN.md` — per-beat visual treatment + legibility contract + the audio-assembly fix
- `beat_sheet.json` — narration, timing, props, build state
- `remotion-src`/`TestToAdvanceGate.tsx` (in the toolkit `runtime/remotion/src/`) — reel-local B01–B06 components
- `source/test_to_advance_gate.tex` (+ `.pdf`) — the frozen story source (schema, algorithm, flow, worked example, results)
- `_qc/` — frame-level QC + PROOF production-gate result (`REPORT.md`)
- final `.mp4` — the 4K 16:9 master

## Build result for this report

The reviewed local build produced:

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 4:14), stream-copy assembled;
- **audio verified present** (`volumedetect` mean ≈ −21.5 dB) via the concat **filter**;
- a complete end-to-end human review plus a PROOF pass (teaching 12/12; production gate PASS).

Build notes: the first 4K render failed with **ENOSPC — the C: drive was 100% full** (Remotion writes temp frames to C:). Fixed by redirecting `TMPDIR/TEMP/TMP` to `d:/_remotion_tmp` (D: has ~416 GB free); all 10 beats then rendered cleanly at concurrency 3. C: disk space is a standing environment issue, not specific to this reel. Duration (4:14) runs a little long because Bella reads the dense technical script slower than estimated — consistent with prior weeks (week-04 was 3:52).

## Current limitations

- the hard/soft edge typing and the six items are **draft** (`needs_review = yes`); **no faculty approval**;
- the `0.67` confidence threshold is a **defensible default**, not a validated cutoff;
- worked-example grading is **simulated** (control flow/pruning/decisions real); production uses answer-key matching;
- **no learning-outcome / retention claim** — the gate proves readiness, not learning;
- single Chapter-27 slice (22 concepts / 26 edges); no extrapolation to the full book.

## Future work

- author + faculty-review items for the full Chapter-27 chain; replace the simulated grader with real answer-key matching;
- add a **placement mode** that finds where a learner should *start* and returns a trimmed roadmap;
- use accumulated connection-item outcomes to validate — and where warranted re-type — the dependency edges;
- (phase two) open-ended items graded by an LLM-as-judge, calibrated against a human gold set;
- (later) layer the richer learner model (interests, project, background) from the *Robot Tutor* discussion on top of this baseline.

## Final human checklist

- Can a new viewer state the three moves and apply them to a new prerequisite-gated curriculum?
- Does B01 land the three moves **before** any file/item/learner?
- Is B05 the two-learner split (STU001 hold vs STU002 advance), with the failed connection and pruned node both on screen and the tested/pruned counts shown?
- Does B06 show real-vs-draft, `needs_review`, "none faculty-approved", and MC-first vs open-ended?
- Is every number traceable to `test_to_advance_gate.tex`, with no learning-outcome claim?
- Is **audio present** on the master (`volumedetect` ≈ −21 dB, not −91)?
- Did a human watch the complete output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it (16:9 long; and any vertical Short) to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
