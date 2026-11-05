# Who Approves the Threshold?

Humanitarians AI · weekly work · Friday 2026-09-18
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> The agent can compute a materiality threshold. It cannot approve one. The approval is a named human's, or it does not exist.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `Mycroft_AdwaitChangan_2026-09-18.mp4` | 3840×2160 (16:9) | ~3:32 |
| `short/Mycroft_AdwaitChangan_2026-09-18-short.mp4` | 2160×3840 (9:16) | ~2:24 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

The threshold that decides which variances are worth reporting is a judgement, and the engine was making it silently. This week's work splits the two halves: the engine prepares a request, and a named human signs it. Four attempts are run. The agent signing is refused by name. A human signing with a placeholder reason is refused. A named person with a stated basis is recorded. Signing again is refused, because an approval you can quietly replace is not evidence of anything.

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
