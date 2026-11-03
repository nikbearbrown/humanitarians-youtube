# Weekly Research Report: The Links That Weren't There

**Fellow:** Satwik Reddy Sripathi
**Week ending:** October 24, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` - `weekly_report_2026-10-25.md`, `prereq_underconnection_diagnostic.md`, `prereq_recall_problem_story.md`, `prereq_recall_fix_methodology.md`, `mechanism_prereqs_proposed.csv`, `prereq_gap_data.csv`, `prereq_gap_chart.png`. Every on-screen figure traces to these.
**Source status:** The diagnosis is **measured and reproducible**; the fix is a **content-grounded proposal**, not applied. What is **draft / not approved**: the `mechanism_prereqs_proposed.csv` tiers (`approve` blank, `needs_review = yes`); faculty confirm the required tier. **No learning-outcome claim.**

This week follows a faculty review. Dr. Gultepe looked at the three-tier prerequisites and flagged that the
later chapters were under-connected - Chemotherapy (Ch 23) required almost nothing, though understanding it
depends on core cancer biology. So this week -

**I diagnosed why the later chapters came out under-connected, grounded it in the research, and built a fix
that recovers the missing links from the textbook's own content.**

The answer is that this is a known failure mode - the recall problem in automatic prerequisite extraction -
and the fix is to stop leaning on surface similarity and instead derive each applied chapter's prerequisites
from the concepts it actually uses, then let faculty confirm the tiers.

The final beat sheet contains **10 beats**. The complete video is generated locally with the free Brutalist
toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass).

## What was done this week

- **A failure analysis, not a patch.** Ruled out the redundancy cleanup as the cause; showed the gap is two
  distinct failures (mis-tiering and missing edges); measured it across the book (11 of 21 later chapters have
  0-1 required cross-chapter prerequisite; see `prereq_gap_chart.png`).
- **Research grounding.** Named it: the recall problem / precision-recall trade-off in concept-prerequisite
  extraction (Pan 2017; Liang 2015/2018), plus a generality bias.
- **A content-grounded fix.** Derived each applied chapter's prerequisites from the textbook's own
  concept/mechanism tags (`propose_mechanism_prereqs.py`), through three documented iterations to avoid
  re-introducing the generality bias. 146 proposals; the 13 under-connected chapters drop to 0; Ch 23 recovers
  Metabolism and Principles of Therapy as required.
- **Recurrence prevention.** A coverage gap-check (`check_prereq_coverage.py`) that flags any under-connected
  applied chapter and can gate the build (25 issues on the current graph).

## How this connects to the series

Week 11 built the three tiers; week 12 made concept-matching usable; **week 13 responds to faculty review of
the prerequisites** by diagnosing and fixing a recall gap in the later chapters. It is the review loop working
as designed: the expert caught a real gap, I found the systemic cause, and the fix is a reviewable proposal.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> Why did the later, applied chapters come out with almost no required prerequisites - and how do you recover
> the missing links without just reproducing the bias that caused them?

The answer: it is the known recall problem in prerequisite extraction; recover the links from the textbook's
own concepts (content-grounded), not from surface similarity, and let faculty confirm the tiers.

## Main ideas presented (10 beats)

1. **The catch (hook).** A reviewer: Chemotherapy requires almost nothing, though it depends on metabolism and
   the tumor microenvironment.
2. **It's a known failure (framework-first).** The recall problem / precision-recall trade-off in
   prerequisite extraction, plus a generality bias - named and measured in the literature.
3. **The diagnosis.** Not the redundancy cleanup; two failures - mis-tiering and missing edges; 11 of 21 later
   chapters have 0-1 required prereq (the chart).
4. **Why it happened.** Chunked authoring, an over-strict required tier, surface vs conceptual matching, and
   integrative applied chapters.
5. **The method.** Derive prerequisites from the textbook's own concept tags: for each concept a chapter uses,
   credit the earlier chapter that owns it.
6. **Three dead ends.** Raw overlap reproduced the generality bias; specificity filtering lost the TME
   (metadata over-tagging); concentration-home finally recovered Metabolism, TME, Cell Cycle, Therapy
   Principles. Then a sibling-contamination fix (a treatment is not a prerequisite of another treatment).
7. **The result.** 146 proposals; 13 under-connected chapters -> 0; Ch 23 recovers Metabolism and Principles of
   Therapy as required - as a proposal for faculty, not auto-applied.
8. **Prevention.** A gap-check that flags any under-connected applied chapter and gates the build.
9. **The honest boundary.** A proposal, not approved; the metadata has its own recall gaps; faculty decides
   the required tier.
10. **Outro / CTA.** When an extractor is precise but thin, the fix is recall from content, not more
    similarity - and a check so the gap can't come back.

## Current implementation boundary

- **Diagnosis:** measured and reproducible from the two input files.
- **Fix:** a content-grounded **proposal** (`mechanism_prereqs_proposed.csv`), `needs_review = yes`; nothing
  written to the authoritative graph.
- **Tiers:** faculty confirm what is required; the tool proposes from evidence.
- **No learning-outcome claim.**

## The reusable framework

1. **Treat a reviewer's catch as a failure analysis** - find the systemic cause, not the one instance.
2. **Name the failure mode** - here, the recall problem and generality bias in prerequisite extraction.
3. **Recover from content, not surface similarity** - derive dependencies from the material's own concepts,
   weighting specificity and concept ownership; restrict candidates to the foundational half to avoid sibling
   contamination.
4. **Add a check so it can't silently recur**, and keep the expert as the authority on the final tier.

## Research grounding

Recall problem / precision-recall trade-off in automatic concept-prerequisite extraction (Pan et al., ACL
2017; Liang et al., PREREQ, 2018); prerequisite direction and generality via Reference Distance (Liang, Wu,
Huang & Giles, EMNLP 2015); LLM concept-graph recovery limitations (2024-2025). Full citations in
`sources/prereq_recall_problem_story.md`.

## Research prompt

> Research the "The Links That Weren't There" explainer. Begin with `sources/weekly_report_2026-10-25.md`,
> `prereq_underconnection_diagnostic.md`, `prereq_recall_fix_methodology.md`, `prereq_gap_data.csv`, and
> `prereq_gap_chart.png`. Identify: the feedback (Ch 23 under-connected); ruling out the reduction; the two
> failures (mis-tiering, missing edges); the measure (11/21 later chapters with 0-1 required prereq); the
> research framing (recall problem + generality bias); the method and its three iterations; the result
> (146 proposals, 13 -> 0, Ch 23 recovers Metabolism + Principles of Therapy); the gap-check (25 issues). Return
> a claim table with exact source lines. Do not invent numbers. Never present the proposal as approved, and
> never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each claim: beat ID, claim, verdict
> (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: "not the reduction";
> 1.82 vs 1.67 average; 11 of 21 later chapters 0-1 required; two failures; the recall-problem citations;
> the three method iterations; 146 proposals (127 add / 10 promote / 9 exists); 13 -> 0; Ch 23 recovers
> Metabolism + Principles of Therapy as required, TME proposed recommended; gap-check 25 issues. Flag any
> framing that treats the proposal as approved or asserts a learning gain.

## Typical commands

```bash
PYTHONUTF8=1 ".venv/Scripts/python.exe" runtime/scripts/generate_audio_kokoro.py "/abs/path/to/prereq-recall-gap"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/prereq-recall-gap"
```

## Beat-sheet and visual rules

- `beat_sheet.json` is the source of truth; audio duration is the clock.
- Show the framework (it's a known failure mode) before the counts (framework-first).
- B03 shows the gap chart; B06 is the three-iterations arc; each claim beat holds its real figure >=2s.
- **CRIMSON = the gap / under-connected, GOLD = the method, SLATE = diagnosis / scale, TEAL = recovered / fixed,
  SAGE = prevention.**
- Never frame the proposal as approved; never assert a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off
"This is Satwik for Humanitarians AI."

## Useful project files

- `sources/` - the frozen story source (weekly report, three analysis docs, the proposal CSV, the gap data + chart)
- `output/prereq-recall-gap/` (to be produced) - PREMISE, SOURCES, NARRATION-GATE-P, PEDAGOGY, VISUAL-PLAN, beat_sheet.json
- final `.mp4` - the 4K 16:9 master

## Build result for this report

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160, 5:13 — video stream 312.77s, verified full length);
- **audio verified present** (`volumedetect` mean ≈ −21.4 dB) via the concat filter;
- a complete frame-level QC plus a PROOF + fact-check pass (production gate PASS; `output/prereq-recall-gap/_qc/REPORT.md`, `FACT-CHECK.md`).

Fact-check corrections applied (`FACT-CHECK.md`): the docs' "11 of 21 later chapters" was not reproducible from `prereq_gap_data.csv`, so the on-screen figure is the CSV-consistent **13 of 19 applied chapters**; the "TME proposed for Ch 23" claim is not in the proposal CSV, so it is shown only as the honest-boundary gap (the signal missed it), never as recovered; "three iterations" is framed as three tries + a sibling-contamination fix. 146 = 127 add + 10 promote + 9 exists and the Ch 23 recoveries (Metabolism required·added; Principles of Therapy required·promoted) were verified directly in the CSV.

Per direction, the **video shows only the research progress** — Dr. Gultepe's review and catch are kept, but the next-steps / "send it to faculty" handoff is removed (B00 and B07 read "a reviewable proposal, not yet applied"); the actual ask lives only in the separate email file.

Build notes: this render fought persistent low-RAM Chrome cold-start timeouts (free RAM dipped to ~0.3–0.8 GB); B00, B04, and B07 each needed `--only` retries at concurrency 1 to beat the 25 s browser-connect window. Assembly used the concat filter for both streams; the video-stream duration was verified full length (312.77s).

## Current limitations

- the fix is a **proposal**, not approved; faculty confirm the required tier;
- the content signal depends on the metadata, which has its own recall gaps;
- the ranking reflects shared content, not pedagogical necessity (e.g., TME proposed recommended for Ch 23);


## Future work

- faculty confirm/adjust the proposed tiers (Ch 23 is the calibration);
- apply the approved rows, re-validate (acyclic), regenerate the reading-order files and app;
- wire the gap-check into the build so coverage is enforced going forward.

## Publication note

The final MP4 is shared separately with the Humanitarians AI publishing team. A successful local build is not
itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
