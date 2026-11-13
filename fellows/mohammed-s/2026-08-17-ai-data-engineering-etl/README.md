# ETL, Simplified

- **Status:** built & QC-passed — not published (nothing here publishes)
- **YouTube:** _(blank — nothing here publishes)_
- **Channel / persona:** Mohammed Hussain (no channel identity claimed)
- **Skill:** `ai-explainer` · **Register:** Teardown · **Voice:** Kokoro `am_onyx` ("Onyx")
- **Runtime:** 1:59.99 · 10 beats
- **Resolutions:** 3840×2160 (16:9) **and** 2160×3840 (9:16)
- **Last updated:** 2026-08-31

## What it argues

AI collapses the *glue* in ETL, not the *judgment*. Schema mapping, connector
boilerplate, tests and docs stop being handwritten — but deciding what a mismatch
**means** does not move, and the new failure mode is a pipeline that runs green
while the values are quietly wrong.

## The two masters

| Cut | File | Frame | Notes |
|---|---|---|---|
| 16:9 | `ai-data-engineering-etl.mp4` | 3840×2160 | the desktop master |
| 9:16 | `916/ai-data-engineering-etl-916.mp4` | 2160×3840 | **native portrait**, not a crop |

Both are also copied into `mp4/`.

**The 9:16 cut is a re-layout, not a centre-cut.** Every beat renders from its own
portrait composition, and the components reflow: the glue stack runs down a
vertical spine instead of across a pipe; the schema diff becomes one full-width
card per mapping instead of two facing panels; the good-at/cannot-do split turns
from two columns into two stacked blocks. Portrait type is **larger** than
landscape type, because the frame is narrower — nothing is shrunk to fit.

## Beats

| # | Act | Composition | Audio |
|---|---|---|---|
| B00 | INTRO | `ClaudeComposerAsk` | 15.59s |
| B01 | PROBLEM | `EtlGlueTax` | 14.21s |
| B02 | ASK | `ClaudeComposerAsk` | 10.41s |
| B03 | RESULT | `EtlSchemaMapping` | 15.40s |
| B04 | CODE | `ClaudeCodeBeat` | 10.24s |
| B05 | JUDGMENT | `EtlWhereAiHelps` | 12.71s |
| B06 | RISK | `EtlSilentFailure` | 11.03s |
| B07 | SUMMARY | `ClaudeVerdictArtifact` | 11.97s |
| B08 | NEXT STEPS | `ClaudeComposerAsk` | 13.76s |
| B09 | OUTRO | `ClaudeTitleOutro` | 4.67s |

Every slot is machine-rendered. No slates, no pantry drops, no stock imagery —
REBUILD LAW is satisfied by construction.

## Paperwork

| File | What |
|---|---|
| `PEDAGOGY.md` | GATE P — the signed narration review, plus the shortening amendment |
| `FACTCHECK.md` | every claim, verdicted, with the corrections applied |
| `SOURCES.md` | what the technical claims rest on; determinism notes |
| `SHOTLIST.md` | the typed work order and the aspect-ratio contract |
| `PROMPTS.md` | the on-screen prompts (content) and the scene build prompts |
| `BUILD-PROMPT.md` | paste-ready rebuild, end to end |
| `_build_sheet.py` | authors `beat_sheet.json` — **edit this, never the JSON** |
| `_build_916.py` | derives the portrait sibling from the signed sheet |
| `_qc/` | frame-level visual QC evidence for each cut |

## QC

Gate V: **0 BLOCKERs** in both cuts. Remaining flags are all the automated
`underfill` heuristic and were adjudicated by eye — see `_qc/REPORT-final.md`.
Three real defects were found and fixed on the second pass: a header collision in
the portrait schema beat, a title-safe breach in the spark line across four
scenes, and undersized type on the landscape split.

## Change notes

- **2026-08-31** — QC pass 2: fixed the portrait B03 header collision, the
  `EtlSpark` title-safe breach (8 BLOCKERs across 4 scenes, both aspects), and
  landscape B05 underfill. Re-rendered 8 beats, recompiled both masters. Gate V
  now reports 0 BLOCKERs on both. Masters staged in `mp4/`.
- **2026-08-30** — built. GATE P signed PASS with a shortening: a standalone
  E/T/L mechanism beat was cut to bring the runtime under 2:00, and its one
  load-bearing line was folded into B01. Five new Remotion illustrations were
  authored for this reel (`EtlGlueTax`, `EtlStages`, `EtlSchemaMapping`,
  `EtlWhereAiHelps`, `EtlSilentFailure`), each registered twice — 16:9 and 9:16.
  `EtlStages` was the beat that got cut; it stays in the library.
