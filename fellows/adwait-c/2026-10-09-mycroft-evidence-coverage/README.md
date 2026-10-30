# Citations Nobody Checks

Humanitarians AI · weekly work · Friday 2026-10-09
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> Findings had carried evidence references for weeks, which looked like proof. Nothing had ever opened the files to check.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `Mycroft_AdwaitChangan_2026-10-09.mp4` | 3840×2160 (16:9) | ~3:36 |
| `short/Mycroft_AdwaitChangan_2026-10-09-short.mp4` | 2160×3840 (9:16) | ~2:31 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

The word *unsourced* hides three different failures, and only the first is visible by reading: no citation at all, a citation to a file that is not in the pack, and a citation to a row that is not there. Each is now reported separately, and a reference that cannot even be parsed raises rather than being skipped quietly. Run against the real February investigation, all twenty one references across four findings resolve. The honest closing point is that resolving proves the row exists, and proves nothing about whether it supports the claim.

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
