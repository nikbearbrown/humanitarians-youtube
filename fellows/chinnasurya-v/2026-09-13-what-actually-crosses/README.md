# What Actually Crosses

Brutalist 4K explainer: what moves between Canvas and the Medhavy Hub, and what
deliberately does not. The point of the reel is the negative space. The tool
requests no Assignment and Grade Services scopes and no Names and Role
Provisioning scopes, so the gradebook and the roster never cross.

| | |
|---|---|
| Master | 3840x2160, 24 fps, 129.1 s (2:09.1) |
| Beats | 9, all filled |
| Voice | Kokoro `am_onyx` |
| Script written | 2026-09-13 |
| Rendered | 2026-10-28 |
| Render | `medhavy-canvas-sync.mp4`, on Drive |

## What is here

| File | What it is |
|---|---|
| [script.md](script.md) | The narration and art direction, unchanged since 13 September |
| [beat_sheet.json](beat_sheet.json) | The production contract: 9 beats |
| [SHOTLIST.md](SHOTLIST.md) | Per-beat shot plan |
| [FACTCHECK.md](FACTCHECK.md) | 9 rows, every claim traced to a source file. Plus two code findings kept off camera |
| [SOURCES.md](SOURCES.md) | Narration provenance and exclusions |
| [PEDAGOGY.md](PEDAGOGY.md) | GATE P: the one idea, per-beat targets, weakest beat |
| [BUILD-LOG.md](BUILD-LOG.md) | Environment rebuild, measured durations, four QC defects and their fixes |
| [scenes/render_scenes.py](scenes/render_scenes.py) | The out-of-tree scene renderer. Core reused verbatim from the September reel; the nine scene functions are new |
| [qc-sheet-16x9.png](qc-sheet-16x9.png) | All nine settled frames on one contact sheet |
| [qc-sheet-9x16.png](qc-sheet-9x16.png) | The same settled frames from the native portrait render |
| [beat-sheet-short.json](beat-sheet-short.json) | The 9:16 cut's own beat sheet — the portrait build input |

## Research

Done against the code rather than against the project's own documents, which is
why the fact-check cites source files and line numbers: `lib/lti-utils.ts`,
`app/api/lti/callback/route.ts`, `lib/quiz/grading.ts`,
`app/api/quizzes/[id]/submit/route.ts`, and the LTI migrations.

That approach turned up two defects the documents did not describe, both recorded
in [FACTCHECK.md](FACTCHECK.md) and deliberately kept off camera: a dormant
second Canvas-config generator that still lists all four AGS and NRPS scopes, and
two advertised placements pointing at a `/api/lti/deep-linking` route that does
not exist.

## Frictional log

See [FRICTIONAL.md](FRICTIONAL.md).
