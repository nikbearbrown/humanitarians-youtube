# When the Reviewer Disagrees

Humanitarians AI · weekly work · Friday 2026-10-02
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> A reviewer who disagrees with the engine needs somewhere to say so that does not quietly overwrite what the engine said.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `Mycroft_AdwaitChangan_2026-10-02.mp4` | 3840×2160 (16:9) | ~3:34 |
| `short/Mycroft_AdwaitChangan_2026-10-02-short.mp4` | 2160×3840 (9:16) | ~2:22 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Agreement was recordable and disagreement was not, so the only way to dissent was to change the number. This week's work keeps both sides verbatim: the engine's value is copied from the run rather than restated by the reviewer, the reviewer's position is named and dated, and nothing is reconciled. The log resolves nothing on purpose. Its job is to make a disagreement visible to whoever reads the report, not to decide who was right.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| — | The work itself lives in `mycroft/projects/Mycroft-Finance-Investigator/`; this folder documents it. |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
