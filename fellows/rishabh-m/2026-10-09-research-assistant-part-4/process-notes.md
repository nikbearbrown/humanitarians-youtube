# Process notes — Design From Real Data (both cuts)

**Status:** built · awaiting Rishabh's review · not yet staged to Drive
**Channel:** claude-hai · **Resolution:** 3840×2160 (16:9) / 2160×3840 (9:16)
**Last updated:** 2026-10-09
**Drive:** https://drive.google.com/drive/folders/1TcLfQncfg-LSAnTao7RW7xvedUpr2oOB

Build log for `research-assistant-part-4` (16:9) and `research-assistant-part-4-short` (9:16).
Chronological; append-only — add dated entries, don't rewrite history.

## 2026-10-09 — beat sheet → both cuts at true 4K

**Source.** The Stage 2 doc (Part 2A) and the nine Oct 5–8 commits. Build-log framing, first
person; no course or reference mentioned; no credit line. Omitted for length: the
sync-vs-async decision. Greeting "Greetings" (slug pick, HOUSE-RULES); outro `HaiTitleOutro`.

**GATE L.** Every beat maps to an existing composition: `AgenticPatternDiagram` (×7),
`ClaudeCodeFile` (×6) and the bookends (`ClaudeComposerAsk` ×2, `BrutalistHesitantWriter`,
`ClaudeVerdictArtifact`, `HaiTitleOutro`). No new components.

**LOGO LAW.** Tool nodes carry their marks: arXiv and Airflow were added to `icons/logos/`
from their official marks (arXiv wordmark recoloured to arXiv red for the cream stage);
Postgres and FastAPI from the library. `AgenticPatternDiagram` gained an optional per-node `logo`.

**Executable evidence.** Code on screen is the real file, with every trim labelled
(`…`, "one line wrapped"). B10's results are the numbers recorded in the Stage 2 log
(243 papers, 3 requests, 6.5 s, 2.79 s gap), labelled as recorded — not a screen capture.

**Audio.** Kokoro `af_sarah`; every beat padded with a 1.0 s hold (`pad_beats.local.py`).
B03 re-ordered and regenerated so its highlight cue lands inside the 10 s composition.

**Gates.**
- **F (paperwork):** FACTCHECK (22 claims: 21 PASS, 1 EXEMPT editorial), SHOTLIST, PROMPTS.
- **V (frames):** fixed underfill on B01 (type 162→175), B15 (longer verdict lines + channel
  label), B17 (outro spacing without a credit line); then a mean-contrast fail from the accent
  tint, fixed by lightening it to ≤14%.
- **T (typography):** accent cards no longer use cream text on terracotta (2.7:1) — now a
  tint with a deeper terracotta rule and ink text; diagram sub-lines and labels raised above
  the 1.9% floor; code-card floor raised; two notes cut to ≤12 words; B12 excerpt trimmed.

**Short.** Purpose-authored 9:16 sheet (9 beats), every beat a registered `916` composition.
The config code card became a diagram (portrait is width-bound); the outro title set to
210 pt so it wraps to three lines and stays inside SAFE916. Gate V on the clean cut: 0/0.

**Final specs:**

| Cut | Resolution | Duration | Gate V | Gate T |
|---|---|---|---|---|
| 16:9 | 3840×2160 | 5:37 (336.7s) | 0 blockers · 0 majors | PASS |
| 9:16 | 2160×3840 | 1:23 (83.0s) | 0 blockers · 0 majors | — |

**Non-blocking lint (accepted, as on Parts 1–3):** OUTRO LAW wants `ClaudeTitleOutro` — no,
it hardcodes @NikBearBrown; `remotion` carries 100% of beats — the cap is archival guidance.
