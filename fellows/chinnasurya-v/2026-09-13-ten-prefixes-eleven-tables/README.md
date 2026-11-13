# Ten Prefixes, Eleven Tables

Brutalist 4K explainer on the database schema behind a Canvas integration: the
three jobs it does, and a table count that looked like a mistake and was not.

| | |
|---|---|
| Master | 3840x2160, 24 fps, 114.5 s (1:54.5) |
| Beats | 8, all filled |
| Voice | Kokoro `am_onyx` |
| Script written | 2026-09-13 |
| Rendered | 2026-10-28 |
| Render | `medhavy-lti-tables.mp4`, on Drive |

## What is here

| File | What it is |
|---|---|
| [script.md](script.md) | The narration and art direction, unchanged since 13 September |
| [beat_sheet.json](beat_sheet.json) | The production contract: 8 beats |
| [SHOTLIST.md](SHOTLIST.md) | Per-beat shot plan |
| [FACTCHECK.md](FACTCHECK.md) | 8 rows against the migration files, one carrying an explicit note that the claim is contested |
| [SOURCES.md](SOURCES.md) | Narration provenance and exclusions |
| [PEDAGOGY.md](PEDAGOGY.md) | GATE P: the one idea, per-beat targets, weakest beat |
| [BUILD-LOG.md](BUILD-LOG.md) | Measured durations, three QC defects and their fixes |
| [scenes/render_scenes.py](scenes/render_scenes.py) | The out-of-tree scene renderer. Core reused verbatim across all three reels; the eight scene functions and `tcard()` are new |
| [qc-sheet-16x9.png](qc-sheet-16x9.png) | All eight settled frames on one contact sheet |
| [qc-sheet-9x16.png](qc-sheet-9x16.png) | The same settled frames from the native portrait render |
| [beat-sheet-short.json](beat-sheet-short.json) | The 9:16 cut's own beat sheet — the portrait build input |

## The count

The reel exists because of a discrepancy. Working notes said ten LTI tables; the
security review said eleven. Both were right. Ten carry the `lti_` prefix. Eleven
have row level security enabled: those ten plus `institutions`, which belongs to
the same schema but is not prefixed. The arithmetic is shown in
[FACTCHECK.md](FACTCHECK.md) row 7.

## One claim is contested, on purpose

B04 states launch audit retention as one hour, which is what the schema's column
default says. A later audit of the same codebase found the published privacy
policy says twelve months and the purge job is not actually scheduled. Rather
than drop the claim or quietly change the number, the discrepancy is written up
in [FACTCHECK.md](FACTCHECK.md) with a note that the figure must be re-measured
before any rebuild. Reconciling it is in the project's
[research plan](../research-plan.md).

## Frictional log

See [FRICTIONAL.md](FRICTIONAL.md).
