# May This Leave the System?

Humanitarians AI · weekly work · Friday 2026-10-23
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> Four checks each produced a careful artifact and then stopped. Nothing stood between a finished report and somebody acting on it.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `Mycroft_AdwaitChangan_2026-10-23.mp4` | 3840×2160 (16:9) | ~3:35 |
| `short/Mycroft_AdwaitChangan_2026-10-23-short.mp4` | 2160×3840 (9:16) | ~2:28 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

The gate blocks by default and clears only when every condition is demonstrated by an artifact on disk, because a check nobody ran is invisible on the finished report. It reports every reason at once rather than one per round, since a gate that reveals failures one at a time gets routed around. Two judgements are stated as judgements rather than hidden in code: STALE clears and EXPIRED does not, and a missing disagreement log clears while an open entry blocks. The closing point is that it cannot actually stop anyone.

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
