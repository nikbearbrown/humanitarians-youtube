# How Old Is the Evidence?

Humanitarians AI · weekly work · Friday 2026-09-25
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> A financial report carries two ages that never appear in any figure: how long the data took to arrive, and how long it then sat before anyone read it.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `Mycroft_AdwaitChangan_2026-09-25.mp4` | 3840×2160 (16:9) | ~3:26 |
| `short/Mycroft_AdwaitChangan_2026-09-25-short.mp4` | 2160×3840 (9:16) | ~2:21 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Two gaps, measured separately, because they are different problems. Arrival lag is the time between a period closing and the data about it being produced. Shelf age is the time between production and use. Pointed at this project's own shipped pack the answer was not flattering, and it was left as it was rather than regenerated to look better. Two cases are refused rather than measured: a pack with no provenance at all, and a pack created before its own period had ended.

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
