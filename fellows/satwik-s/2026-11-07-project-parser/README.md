# Weekly Research Report: Reading the Student (Stage 4a Project Parser)

**Fellow:** Satwik Reddy Sripathi
**Week ending:** November 7, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` - `weekly_report_2026-11-07.md`, `project_parser_upgrade.md`, `project_parse_quality.md`, `project_parse_quality.json`, `project_parse_gold.json`, and `projects/` (the six project descriptions). Every on-screen number traces to these.
**Source status:** The evaluation is **measured and reproducible** (`scripts/evaluate_project_parser.py`) against a hand-annotated gold standard. The reported numbers are the **offline rule-based backend**. The LLM backend is **code-complete behind the same interface but not yet measured here** (no local model is running in this environment); its benefit is stated as a prediction, not a result. This makes **no learning-outcome claim**.

This is the pipeline stage where the system first reads the student: a free-text project description becomes
structured fields in the same controlled vocabulary as the textbook metadata. If that reading is wrong,
everything downstream inherits the error. So this week -

**I made Stage 4a measurable: I built a gold standard, scored the parser, and found its one real weakness - it
reads concrete nouns perfectly but misses abstract concepts a student paraphrases - then built a swappable
second backend designed to close exactly that gap, with a hard "never guess" guarantee that the audit confirms.**

The final beat sheet contains **10 beats**. The complete video is generated locally with the free Brutalist
toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass).

## What was done this week

- **Refactored the project parser into one interface with two backends** (same config-driven pattern as the
  embedding layer): `RuleBasedProjectParser` (offline default) and `LLMProjectParser` (strict JSON over the
  controlled vocabulary, auto-fallback when no local model is reachable).
- **Built a hand-annotated gold standard** over six projects (two demos plus CAR-T, polymeric chemotherapy,
  iron-oxide MRI, CRISPR) and an evaluation script reporting per-field precision/recall/F1 and a never-guessed
  audit.
- **Measured, rule-based backend:** overall precision **0.97**, recall **0.89**, F1 **0.93**; concrete fields
  (materials, techniques, assays, disease) at **1.0 / 1.0**; abstract fields at **0.69 / 0.71** recall, with all
  eight misses being paraphrase. Never-guessed audit: **0** invented terms, **67/67** grounded, **4** fields
  correctly left empty.
- **Added tests** (`tests/test_project_parser.py`) locking in the never-guessed contract, the vocabulary
  filter, and the fallback.

## How this connects to the series

This is the first episode of the **pipeline component series** (`docs/pipeline_work_plan.md`): one pipeline
stage per week, each producing a measurable artifact, each a video. The series walks the pipeline front to
back - build the textbook model, **read the student (this week)**, select, make it reproducible, prove it
personalizes.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> When a student describes their project in their own words, can the system turn it into structured intent
> without guessing - and where does plain keyword matching fall short?

The answer: concrete, named things (materials, techniques, assays, disease) are read perfectly; abstract
concepts and mechanisms hit a paraphrase recall ceiling; and the parser never invents a term or fills a field
it cannot support. Measured against a gold standard, with a swappable LLM backend built to close the gap.

## Main ideas presented (10 beats)

1. **The challenge (hook).** The system has to read the student first. A free-text paragraph in, structured
   fields out. Misread it and every later stage inherits the mistake.
2. **The setup (framework-first).** Two guarantees before any number: never guess (an empty field beats a wrong
   one), and never miss (recognize the idea even in the student's own words). The fields use the same
   vocabulary as the textbook, which is what makes matching possible.
3. **Two backends, one interface.** Offline rule-based keyword extraction (default) and an optional LLM
   constrained to strict JSON over the controlled vocabulary. Swap by config, like the embedder.
4. **The test.** A hand-annotated gold standard over six projects; per-field precision, recall, F1, plus a
   never-guessed audit - named before any result.
5. **Concrete fields are solved.** Materials, techniques, assays, disease contexts: precision and recall 1.0.
   Students name these plainly and the lexicon catches them all.
6. **The recall ceiling.** Concepts 0.69, mechanisms 0.71. All eight misses are paraphrase: "new blood vessels"
   for angiogenesis, "spread to the bone" for metastasis, "stop responding to the drug" for drug resistance.
   (The figure: concrete bars at 1.0, abstract bars short.)
7. **Never-guessed holds.** 0 invented terms, every term grounded in the text, 4 fields correctly left empty;
   overall precision 0.97. The parser refuses to make things up.
8. **The precision slips are polysemy, not invention.** "checkpoint" (immune, not cell-cycle) and "tissue"
   (tumor tissue): a backend that reads meaning avoids both.
9. **The fix, and the honest boundary.** The LLM backend maps paraphrase onto the canonical term, with
   vocabulary membership stopping hallucination. It is code-complete but not measured here (no local model), so
   the rule-based numbers are the result and the LLM gain is a prediction.
10. **Verdict / CTA.** Structured intent without guessing. The way to trust a parser is to measure it against a
    gold standard and audit what it refuses to fill.

## Current implementation boundary

- **Measured and reproducible** against a six-project hand-annotated gold standard.
- Reported numbers are the **offline rule-based backend**.
- The **LLM backend is code-complete** behind the interface but **not yet evaluated** (no local model here).
- **No learning-outcome claim.**

## The reusable framework

1. **Measure the reading before trusting it** - a parser that feeds everything downstream earns a gold standard
   and a score, not an assumption.
2. **Separate the two failure modes** - precision (guessing) and recall (missing) are different problems with
   different fixes; report them apart.
3. **Make abstention a measured property** - the parser must prefer an empty field to a wrong one, and the audit
   has to prove it.
4. **Put the fix behind the same interface** - a second backend that closes the gap should be a config swap,
   not a rewrite.

## Research grounding

Dictionary- and ontology-based concept extraction in biomedical text (the tradition behind MetaMap and cTAKES)
is reliably high-precision but limited on paraphrase and synonymy - exactly the trade-off the measurement
reproduces. The LLM backend is schema-constrained structured extraction (JSON over a fixed label set) with
vocabulary membership as the anti-hallucination guard. Precision, recall, and F1 are the standard
information-extraction evaluation; the never-guessed audit is an abstention check. Citations in
`sources/project_parser_upgrade.md`.

## Research prompt

> Research the "Reading the Student" explainer. Begin with `sources/weekly_report_2026-11-07.md`,
> `project_parser_upgrade.md`, `project_parse_quality.json`, and `project_parse_gold.json`. Identify: the two
> guarantees (never guess, never miss); the two backends; the six-project gold standard; overall precision 0.97,
> recall 0.89, F1 0.93; concrete fields at 1.0/1.0 and abstract fields at 0.69/0.71 recall; all eight misses
> being paraphrase; never-guessed audit (0 invented, 67/67 grounded, 4 empty); the two polysemy precision slips.
> Return a claim table with exact source lines. Do not invent numbers. Never present the LLM backend as
> measured, and never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each claim: beat ID, claim, verdict
> (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: precision 0.97,
> recall 0.89, F1 0.93; concrete fields 1.0/1.0; concepts 0.69, mechanisms 0.71; 8 paraphrase misses; 0 invented
> terms, 67/67 grounded, 4 empty fields; the "checkpoint"/"tissue" polysemy slips; LLM backend code-complete but
> not measured; no learning claim.

## Typical commands

```bash
PYTHONUTF8=1 ".venv/Scripts/python.exe" runtime/scripts/generate_audio_kokoro.py "/abs/path/to/reading-the-student"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/reading-the-student"
```

## Beat-sheet and visual rules

- `beat_sheet.json` is the source of truth; audio duration is the clock.
- Show the framework (two guarantees + the two backends) before any number.
- B05/B06 are the per-field figure (concrete bars at 1.0, abstract bars short); B07 is the never-guessed audit;
  each claim beat holds its figure >=2s.
- **CRIMSON = recall misses / paraphrase gap, TEAL = never-guessed / precision, SLATE = fields / scale,
  GOLD = the recall-ceiling finding, SAGE = the LLM fix.**
- Never present the LLM backend as measured; never claim a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off
"This is Satwik for Humanitarians AI."

## Useful project files

- `sources/` - frozen story source (weekly report, the upgrade writeup, the quality md+json, the gold json, and
  the six project descriptions under `projects/`)
- `output/reading-the-student/` (to be produced) - PREMISE, SOURCES, NARRATION-GATE-P, PEDAGOGY, VISUAL-PLAN,
  beat_sheet.json
- final `.mp4` - the 4K 16:9 master

## Build result for this report

- **Built.** `output/reading-the-student/week15_reading-the-student_nov07.mp4` — **4K 16:9** (3840×2160),
  **4:30** (video stream 269.97 s), 30 fps, AAC 192 kbps, volumedetect mean **-21.5 dB**.
- **10 beats, all present and 4K**, each clip extended to its measured narration (via `remotion_scenes.py`):
  B00 30.7 s · B01 25.6 s · B02 29.4 s · B03 27.1 s · B04 22.9 s · B05 26.8 s · B06 25.9 s · B07 30.8 s ·
  B08 36.0 s · B09 14.8 s.
- **PROOF gate:** PEDAGOGY `VERDICT: PASS`; GATE P (NARRATION-GATE-P) passed; `FACT-CHECK.md` `VERDICT: PASS`
  with 1 correction (polysemy-slip example terms reconciled to `project_parse_quality.json`: the two false
  positives are `cell cycle regulation` and `tissue organization`, not the README's earlier "checkpoint"/"tissue").
- **Numbers verified on the rendered master:** overall precision 0.97 / recall 0.89 / F1 0.93 (B06); concrete
  fields 1.0 — materials 8/8, techniques 16/16, assays 6/6, disease 16/16 (B04); recall ceiling concepts 0.69,
  mechanisms 0.71 (B05); never-guessed 0 invented / 67/67 grounded / 4 empty (B06).
- **QC:** `output/reading-the-student/_qc/REPORT.md` (per-beat frames + specs) — **PASS**.
- Video content is pure research progress; the explainer email to Prof. Nik is the separate deliverable
  (`output/reading-the-student/email_week15_reading_the_student.md`).

## Current limitations

- reported numbers are the offline rule-based backend;
- the LLM backend is code-complete but not yet measured (no local model in this environment);
- the gold standard is six projects annotated by one author, not a held-out benchmark;
- **no learning-outcome claim.**

## Future work

- run the LLM backend against the same gold standard once a local model is available, to measure the predicted
  recall gain at equal precision;
- grow the gold standard and have a second annotator check it;
- feed the parsed projects through the full pipeline for the personalization-at-scale week.

## Final human checklist

- Does the video state the two guarantees and the two backends before any number?
- Do B05/B06 show the concrete-vs-abstract split, and B07 the never-guessed audit?
- Is the LLM backend clearly marked code-complete-but-not-measured, with the rule-based numbers as the result?
- Every figure traceable to `sources/`?
- No learning-outcome claim?
- Did a human watch the full output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 is shared separately with the Humanitarians AI publishing team. A successful local build is not
itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
