# Process notes — The Queue Is A Query (both cuts)

**Status:** built · awaiting Rishabh's review
**Channel:** claude-hai · **Resolution:** 3840×2160 (16:9) / 2160×3840 (9:16)
**Last updated:** 2026-10-16
**Drive:** https://drive.google.com/drive/folders/1rca04Q1xJCdidYSC3QelYdoodXrX9G1H

Build log for `research-assistant-part-5` (16:9) and `research-assistant-part-5-short` (9:16).
Chronological; append-only — add dated entries, don't rewrite history.

## 2026-10-16 — beat sheet → both cuts at true 4K

**Source.** The Stage 2 doc (Part 2B) and the eight Oct 12–15 commits. Build-log framing, first
person; no course or reference mentioned on screen; no credit line. The parser choice is stated
as it is: no local benchmark run, comparison script ready. Omitted for length: the YAML volume typo
and `docker compose cp` permissions. Greeting "Hola" (slug pick); outro `HaiTitleOutro`.

**GATE L.** Every beat maps to an existing composition: `AgenticPatternDiagram` (×7),
`ClaudeCodeFile` (×5) and the bookends. No new components.

**LOGO LAW.** Docling's official mark added to `icons/logos/docling/` (from docling-project/docling);
arXiv, Postgres, Airflow and FastAPI from the library.

**Executable evidence.** Code on screen is the real file; trims are labelled (`…`, "docstring
dropped", "comments trimmed"). Results (BERT parse, image sizes, the two DAG runs) are the numbers
recorded in the Stage 2 log.

**Audio.** Kokoro `af_sarah`; 1.0 s hold per beat. B06 re-ordered and regenerated so its highlight
cue lands inside the 10 s composition.

**Gates.** F: FACTCHECK (19 claims: 18 PASS, 1 EXEMPT editorial), SHOTLIST, PROMPTS. T: PASS first time
(the Part 4 typography fixes carried over). V: one underfill on the outro — "The Queue Is A Query" fit
one 16:9 line — fixed by letting `titleSize` apply in landscape (230 pt, two lines).

**Short.** Purpose-authored 9:16 sheet (9 beats), every beat a registered `916` composition, all
diagrams; outro title at 195 pt. Gate V on the clean cut: 0/0.

**Final specs:**

| Cut | Resolution | Duration | Gate V | Gate T |
|---|---|---|---|---|
| 16:9 | 3840×2160 | 4:51 (290.9s) | 0 blockers · 0 majors | PASS |
| 9:16 | 2160×3840 | 1:20 (80.4s) | 0 blockers · 0 majors | — |

**Non-blocking lint (accepted, as on Parts 1–4):** OUTRO LAW wants `ClaudeTitleOutro` — no, it
hardcodes @NikBearBrown; `remotion` carries 100% of beats — the cap is archival guidance.
