# Whose Failure Is It?

Humanitarians AI · weekly work · Friday 2026-10-16
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> Red means something is wrong. It says nothing about whose, and the three answers call for completely different work.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `Mycroft_AdwaitChangan_2026-10-16.mp4` | 3840×2160 (16:9) | ~3:30 |
| `short/Mycroft_AdwaitChangan_2026-10-16-short.mp4` | 2160×3840 (9:16) | ~2:19 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

A pull request came back red with eleven merge conflicts and nineteen failing checks. The useful skill was not fixing them, it was proving whose they were. Ten of eleven conflicts were another contributor's gateway work, and the base branch version was taken whole and then diffed to prove the result was unchanged rather than assumed. The shared append-only log kept both sides, with ordering verified rather than trusted. The nineteen failing checks reproduce on the base branch, so they were inherited and left alone.

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
