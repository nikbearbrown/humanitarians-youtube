# How a Canvas Launch Works

Brutalist 4K explainer on the LTI 1.3 launch: why the trust comes from a key
registration done in advance rather than from the launch itself.

| | |
|---|---|
| Master | 3840x2160, 24 fps, 195.4 s (3:15.4) |
| Beats | 11, all filled |
| Voice | Kokoro `am_onyx` |
| Render | `medhavy-lti-verify.mp4`, on Drive |

## What is here

| File | What it is |
|---|---|
| [script.md](script.md) | The narration and art direction, written before the build |
| [script-findings-v1.md](script-findings-v1.md) | Earlier draft that included two security findings, cut for a pure-mechanism framing |
| [beat_sheet.json](beat_sheet.json) | The production contract: 11 beats |
| [SHOTLIST.md](SHOTLIST.md) | Per-beat shot plan |
| [FACTCHECK.md](FACTCHECK.md) | 15 rows. Every on-screen claim traced to a source document |
| [SOURCES.md](SOURCES.md) | Narration provenance and what was deliberately excluded |
| [PEDAGOGY.md](PEDAGOGY.md) | GATE P: the one idea, per-beat comprehension targets, weakest beat |
| [BUILD-LOG.md](BUILD-LOG.md) | Measured durations, deviations, the QC defect and its fix |
| [scenes/render_scenes.py](scenes/render_scenes.py) | The out-of-tree scene renderer, 23 KB |
| [qc-sheet-16x9.png](qc-sheet-16x9.png) | Settled frames on one contact sheet, with [part sheets](qc-sheet-16x9-part1.png) and the [QC report](QC-REPORT.md) |
| [qc-sheet-9x16.png](qc-sheet-9x16.png) | The same settled frames from the native portrait render |
| [beat-sheet-short.json](beat-sheet-short.json) | The 9:16 cut's own beat sheet — the portrait build input |
| [build-state.json](build-state.json) | Build state at completion |

Narration audio and beat clips are renders and live on Drive, per the repo rule.

## Source material

Every claim traces to my own project documents: the Medhavy LTI security and
data-handling review, the FERPA data-flow document, the architecture and hosting
summary, and the implementation guide in `medhavi-hub`. No invented values.

## Frictional log

See [FRICTIONAL.md](FRICTIONAL.md).
