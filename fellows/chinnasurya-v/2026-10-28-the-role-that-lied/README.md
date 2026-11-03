# The Role That Lied

Brutalist 4K explainer on why a substring match is the wrong way to read an LTI
role: the meaning of a role URN lives in its final segment, so "does this contain
Instructor" and "is this role Instructor" are different questions that happen to
agree most of the time.

| | |
|---|---|
| Master 16:9 | 3840x2160, 24 fps, 100.7 s (1:40.7) |
| Master 9:16 | 1216x2160, 24 fps, 100.7 s |
| Beats | 8, all filled |
| Voice | Kokoro `am_onyx` |
| Scripted and rendered | 2026-10-28 |
| Renders | `medhavy-role-matching.mp4` and `medhavy-role-matching-916.mp4`, on Drive |

## What is here

| File | What it is |
|---|---|
| [script.md](script.md) | Narration and art direction |
| [beat_sheet.json](beat_sheet.json) | 8 beats |
| [SHOTLIST.md](SHOTLIST.md) | Per-beat shot plan |
| [FACTCHECK.md](FACTCHECK.md) | 6 rows, plus the threat model stated precisely |
| [SOURCES.md](SOURCES.md) | Narration provenance and exclusions |
| [PEDAGOGY.md](PEDAGOGY.md) | GATE P |
| [BUILD-LOG.md](BUILD-LOG.md) | Durations, QC defects, the single-column decision |
| [scenes/render_scenes.py](scenes/render_scenes.py) | One renderer serving both aspects |
| [qc-sheet-16x9.png](qc-sheet-16x9.png) | All eight settled frames on one contact sheet |
| [qc-sheet-9x16.png](qc-sheet-9x16.png) | The same settled frames from the native portrait render |
| [beat-sheet-short.json](beat-sheet-short.json) | The 9:16 cut's own beat sheet — the portrait build input |

## Why both aspects come from one layout

Every beat is a single stacked column. Nothing is placed side by side and nothing
is placed by a fraction of the frame width, so the 9:16 cut is a genuine render at
portrait dimensions rather than a centre crop of the landscape master.

## Threat model

The `roles` claim arrives inside a platform-signed token, so this is not a reel
about forging a token. What the change fixes is misreading legitimate platform
input. Stated in full in [FACTCHECK.md](FACTCHECK.md). The change and its tests
both shipped, so nothing on camera describes a live unfixed weakness.

## Frictional log

See [FRICTIONAL.md](FRICTIONAL.md).
