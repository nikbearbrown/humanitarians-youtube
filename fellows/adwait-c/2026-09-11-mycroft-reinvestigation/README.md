# Checking Its Own Work

Humanitarians AI · weekly work · Friday 2026-09-11
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> A reviewer can send work back. Three follow-up requests went in, three different answers came out, and only one of them was yes.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `Mycroft_AdwaitChangan_2026-09-11.mp4` | 3840×2160 (16:9) | ~3:48 |
| `short/Mycroft_AdwaitChangan_2026-09-11-short.mp4` | 2160×3840 (9:16) | ~2:38 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Builds the loop that runs after a reviewer questions an investigation. Each follow-up is bound by hash to the exact investigation it questions, and every specialist result is regenerated from scratch and compared by fingerprint rather than trusted. The three outcomes are the point: one verified by exact replay, one causal claim rejected as unsupported, and one left open because the operational evidence does not exist. The replay matched exactly and closure is still blocked, because verified means the evidence replayed, not that anyone established a cause.

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
