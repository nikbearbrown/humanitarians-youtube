# Weekly Research Report: Read the Book, Draft the Graph

**Fellow:** Satwik Reddy Sripathi
**Week ending:** September 18, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` — the two prerequisite CSVs (`chapter_prerequisites.csv`, `topic_prerequisites.csv`), the two research reports (`report_prerequisite_construction.md`, `report_evaluation_testing.md`), and `prerequisites_README.md`. Every on-screen figure traces to these files.
**Source status:** The **counts are real** — the prerequisite edges were constructed for the whole *Cancer Biology and Therapeutics* textbook (38 chapters + Appendices A–D). What is **draft**: every edge's hard/soft typing and confidence is a drafting judgment, each row has a blank `approve` column, and **no row is faculty-approved**. Reading order is a strong *signal*, not proof; each edge carries a rationale precisely so a reviewer can reject it. **No learning-outcome claim** is made — this is the dependency structure the roadmap and the test-to-advance gate consume, offered for expert review.

This weekly research video answers the question that has hung over the project since week 05 — every film said *"the dependency graph has 0 authoritative edges, pending faculty."*

**This week the graph is built. So: how do you draft a dependency graph for an entire textbook that domain experts can actually trust?**

The video answers with a **reusable framework — draft a dependency graph in three moves:** **(1) read it from the book** — let the textbook's own chapter/section order and first-mention propose the edges, every one pointing to a real in-book unit; **(2) type each edge hard or soft** — hard = must-know-first (a strict ordering constraint), soft = helpful but never blocking, each with a confidence; **(3) ship it as a draft, not a verdict** — every edge carries a rationale and an empty approval box, because faculty are the source of truth. It then walks the real opening chain of the book (Module 0 → Ch 1 → Ch 2 → Ch 4) and marks plainly what is grounded versus what still needs review.

The final beat sheet contains **10 beats**. The complete video was generated locally using the free Brutalist toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4 lives in the reel folder and is distributed separately.

## What was built this week

Two faculty-review CSVs for *Cancer Biology and Therapeutics* (38 chapters + Appendices A–D = **42 units**, **1,340 sections**, **213 topics**):

| File | "X needs Y" | Edges | Hard | Soft |
|---|---|---|---|---|
| `chapter_prerequisites.csv` | this **chapter** needs this | **102** | 41 | 61 |
| `topic_prerequisites.csv` | this **topic** (section-level) needs this | **248** | 96 | 152 |

`Module 0` (course foundations: intro biology, basic chemistry/biochemistry, fundamental genetics) is the **only external prerequisite** — every other edge is in-book. Columns: `edge_id, approve, target_id, target_title, prereq_id, prereq_title, prereq_type, confidence, rationale, faculty_notes`. Confidence: hard ~0.7–1.0, soft ~0.4–0.6. A validation step confirmed every edge points to a real section (no dangling links). Introduction / Summary / Conclusion sections carry no prerequisites.

## How this connects to the series

Weeks 00–05 built and interrogated the roadmap; week 06 justified the idea (OBER); week 07 added the test-to-advance gate — all on a dependency graph that was still a promise. **Week 08 fills the graph** — the artifact the ordering and the gate both consume. It is the direct answer to the standing "pending faculty" caveat, and it hands faculty a concrete, reviewable object.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> Order says what comes next; a prerequisite says what must come *first*. How do you draft that dependency structure for a whole textbook so that a domain expert can approve, edit, or reject it — grounded, not guessed?

The proposed answer: read the edges from the book's own structure (order + first-mention), type each hard or soft with a confidence and a one-line rationale, and leave approval to faculty. Reading order is a signal, not proof — so it ships as a draft, corroborated next by a deterministic RefD score and an optional LLM pass.

## Main ideas presented (10 beats)

1. **The ask (hook).** The graph was a promise — 0 approved edges, pending faculty. This week it's built for the whole textbook. How do you draft one experts can trust?
2. **The framework (framework-first).** Three moves — **read it from the book · type hard/soft · ship as a draft** — shown before any count.
3. **What was built.** One book (42 units, 1,340 sections, 213 topics) → two graphs: chapter (102 = 41 hard / 61 soft) and topic (248 = 96 hard / 152 soft). Every edge one reviewable row.
4. **Move 1 · read it from the book.** Chapter/section order + first-mention propose the edges; every edge references a real in-book unit by stable ID; Module 0 is the only external prerequisite; validated — no dangling links. (Grounded in concept-maps-from-textbooks, Wang et al. 1816.)
5. **Move 2 · hard vs soft.** Hard = the target directly assumes it, must come first (a strict ordering constraint, conf ~0.7–1.0); soft = helpful, the target reads fine without it (nudges order, never blocks, conf ~0.4–0.6). The editable strong/weak weight is the published model for faculty prerequisite review (PREAP/PRAT).
6. **The worked chain.** CH01 (Normal Cell Biology) ← MOD0 (hard 1.00); CH02 (What Cancer Is) ← CH01 (hard 0.90); CH04 (Genomic Instability) ← CH01 (hard 0.90) and ← CH02 (soft 0.50). Same book, hard and soft, each with a reason you can read.
7. **Draft, not verdict (falsifiability).** Every edge is a draft — `approve` blank, none faculty-confirmed. Reading order is a signal, not proof; each row carries a rationale to reject. Next: a deterministic reference-distance (RefD) score, then an optional LLM pass, then faculty.
8. **Verdict.** 102 chapter + 248 topic edges, read from the book, typed, each with a confidence and a reason; grounded in the prerequisite-relation literature; entirely a draft, built for faculty to approve, edit, or reject.
9. **Your turn (CTA).** For any book: read edges from its structure → type each hard/soft with a confidence → write a one-line rationale → leave the approval box for the expert. A prerequisite is a hypothesis until someone who knows the field signs off.
10. **Outro.** Week after week we pointed at an empty graph; now it's drawn — in pencil, for faculty.

## Current implementation boundary

The video establishes a **built, grounded, reviewable** prerequisite graph and a reusable method for making one. It does **not** claim any edge is authoritative, and it does **not** claim a learning-outcome effect.

- The counts (102 / 248, and the hard/soft splits) are real; the **typing and confidence of each edge are drafting judgments** carried into review.
- **No row is faculty-approved** (`approve` is blank on every edge).
- Reading order is a **signal, not proof** — a book can introduce a topic before its true prerequisite; the rationale column exists so faculty can reject an edge.
- RefD corroboration and the optional LLM pass are **next steps**, not yet run.

## The reusable framework (apply it to a new book)

1. **Read it from the book** — use chapter/section order + first-mention; make every edge point to a real in-book unit (validate — no dangling links).
2. **Type each edge hard or soft** — hard = strict order (must-first); soft = helpful nudge (never blocks); attach a confidence.
3. **Ship as a draft** — one-line rationale per edge, `approve` left blank for the expert.

Decision rule: a prerequisite is a **hypothesis until an expert signs off.** A good result is a grounded, reviewable draft that respects real dependencies; a bad result is treating raw chapter order as truth, or shipping edges nobody can reject.

## How faculty review it

Open either CSV (UTF-8, Excel-safe). For each row: set `approve` = yes/no, adjust `prereq_type` or `confidence` if needed, and add `faculty_notes`. Approved **hard** edges become the strict reading-order constraints; **soft** edges only influence ordering. A useful by-product downstream: accumulated test outcomes (from the week-07 gate) can audit the graph — a "hard" edge whose connection nobody ever fails is probably not hard.

## Research grounding

- **Concept maps from textbooks** — Wang et al., CIKM 1816 (first-mention + chapter/section order as prerequisite features). The most on-point prior work for the from-the-book method.
- **RefD (Reference Distance)** — Liang et al., EMNLP 1815. A deterministic asymmetry score for "is A a prerequisite of B" — a natural hard/soft dial and a corroborating signal (no model needed).
- **PREAP / PRAT** — Alzetta & Torre, JASIST 1825. Annotate prerequisites as the text presents them, with an editable strong/weak weight — the published model for a faculty-reviewable hard/soft attribute.
- **LLMs predict prerequisites** — Le & Abel, arXiv:2507.18479, 1825. Zero-shot LLM prediction aligns with experts — support for an optional LLM-proposed pass on top of the manual draft.
- **Survey** — *Prerequisite Relation Learning: A Survey and Outlook*, ACM Computing Surveys, 1825.

## Research prompt

> Research the "Read the Book, Draft the Graph" prerequisite-construction explainer. Begin with `sources/report_prerequisite_construction.md`, `prerequisites_README.md`, the two CSVs, and `beat_sheet.json`. Identify the three moves (read from book / type hard-soft / ship as draft); the counts (42 units, 1,340 sections, 213 topics; chapter 102 = 41/61; topic 248 = 96/152); MOD0 as the only external prerequisite; the confidence bands (hard ~0.7–1.0, soft ~0.4–0.6); and the worked chain (CH01←MOD0 hard 1.00, CH02←CH01 hard 0.90, CH04←CH01 hard 0.90, CH04←CH02 soft 0.50). Return a claim table: claim, exact source line, evidence, confidence, and what still requires verification. Do not invent numbers. Never present a draft edge as faculty-approved, and never claim a learning-outcome effect.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each factual/numerical/capability claim produce: beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, required correction. Pay attention to: 42 units / 1,340 sections / 213 topics; 102 (41/61) and 248 (96/152); MOD0 as only external; the four worked-chain rows and their confidences; and the "every edge is a draft, none approved" framing. Flag any framing that treats an edge as approved/authoritative, any learning claim, and any number not in the source.

## Typical commands

Run from the Brutalist toolkit root, under `PYTHONUTF8=1`, venv Python for Kokoro. **Render with temp on D:** (C: is near-full — Remotion writes temp there):

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/prerequisite-graph"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/prerequisite-graph"
# top up transient Chrome-launch timeouts serially (re-runs only missing beats):
... ART_REMOTION_CONCURRENCY=1 python runtime/scripts/remotion_scenes.py "/abs/path/to/prerequisite-graph"
```

**Audio assembly (binding Windows fix):** concat **FILTER**, not the demuxer (which yields a silent −91 dB track here):

```bash
ffmpeg -i b00.mp3 … -filter_complex "[0:a][1:a]…concat=n=N:v=0:a=1[a]" -map "[a]" -c:a aac -b:a 192k _a.m4a
ffmpeg -f concat -safe 0 -i _v.txt -c copy -fflags +genpts _v.mp4
ffmpeg -i _v.mp4 -i _a.m4a -map 0:v:0 -map 1:a:0 -c copy -shortest -movflags +faststart OUT.mp4
ffmpeg -i OUT.mp4 -af volumedetect -f null -    # VERIFY mean ≈ −18 dB, not −91
```

## Beat-sheet and visual rules

- Treat `beat_sheet.json` as the source of truth; audio duration is the clock (`durationInFrames = round(actual_duration_s × 30)`).
- Show the three moves **before** any count (framework-first).
- Every claim beat shows its real number/edge legibly at the moment of the claim; B05's chain shows **hard (solid) vs soft (dashed)** together with confidences + rationales, held ≥2s.
- **TEAL = hard/ordering, GOLD = key insight/hard emphasis, SAGE = soft/non-blocking, SLATE = the book, CRIMSON = the draft/falsifiability.**
- Never frame an edge as approved/authoritative; keep `approve = blank` / "none faculty-approved" wherever the topic arises. No learning-outcome claim.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration on the animated slate before generating audio; regenerate + remeasure whenever narration changes; on Windows run audio/render/compile under `PYTHONUTF8=1`.

## Useful project files

- `output/prerequisite-graph/PREMISE.md` — the three-move framework + falsifiability + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must be qualified; what must not be claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric (teaching 12/12)
- `VISUAL-PLAN.md` — per-beat visual treatment + legibility contract + render/audio fixes
- `beat_sheet.json` — narration, timing, props, build state
- `remotion-src/PrereqGraph.tsx` (in the toolkit `runtime/remotion/src/`) — reel-local B01–B06 components
- `sources/` — the two CSVs + two reports + README (the frozen story source)
- `_qc/` — frame-level QC + PROOF production-gate result (`REPORT.md`)
- final `.mp4` — the 4K 16:9 master

## Build result for this report

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 4:23), stream-copy assembled;
- **audio verified present** (`volumedetect` mean ≈ −21.4 dB) via the concat filter;
- a complete end-to-end human review plus a PROOF pass (teaching 12/12; production gate PASS).

Build notes: the render hit low-RAM Chrome-launch timeouts again (~0.9–1.1 GB free); rendered at concurrency 2, then topped up transient failures serially at concurrency 1. A session boundary interrupted the final beat mid-render — no partial/corrupt files were left (verified), and the one missing beat was re-rendered. Temp was redirected to `d:/_remotion_tmp` throughout.

## Current limitations

- every edge is a **draft** (`approve` blank; none faculty-approved); typing + confidence are drafting judgments;
- reading order is a **signal, not proof**; RefD corroboration and the LLM pass are next steps, not yet run;
- **no learning-outcome claim**; single textbook slice; subsection-level prerequisites not yet built.

## Future work

- corroborate hard edges with a deterministic RefD score from the book's cross-references + order;
- an optional LLM-proposed pass to surface edges the manual draft missed (flagged `needs_review`);
- subsection-level prerequisites, selectively, where a subsection has a distinct cross-topic dependency;
- feed approved edges into the roadmap ordering and the test-to-advance gate.

## Final human checklist

- Can a new viewer state the three moves and apply them to a new textbook?
- Does B01 land the three moves **before** any count?
- Is B05 the real chain with hard (solid) vs soft (dashed), confidences, and rationales visible?
- Does B06 mark every edge a draft (0 approved), order≠proof, corroboration next?
- Is every count/edge traceable to `sources/`, with no authoritative or learning-outcome claim?
- Is **audio present** on the master (`volumedetect` ≈ −21 dB, not −91)?
- Did a human watch the complete output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 lives in the reel folder and is shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
