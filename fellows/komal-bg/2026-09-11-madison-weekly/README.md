# Madison Weekly — Sep 11.

**Fellow:** Komal BG
**Date:** 2026-09-11
**Format:** Narrated weekly (Liam summarizes team videos — clips are not spliced)
**Runtime:** ~1:58 · **Master:** 4K (3840×2160) + 9:16 short
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal

## What this video is about

Madison weekly, two receipts with numbers:

- **LoonNet first detector.** 106 train / 26 held-out. Common loon vs non-loon. Web, shore, drone, phone. 19 of 26 held-out frames clean (hand count, not a validation run). Misses split: merge setting vs reeds/fog.
- **Persona-aware prompt dataset.** 39 laptop prompts. Three generic baselines plus four branches (CS student, developer, creative, enterprise IT buyer). Intent → persona → constraints, three matched wordings. CSV + JSON; validator passed. No model queries yet.

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `short/beat_sheet.json` | 9:16 companion plan |
| `README.md` | This file |
| `SOURCES.md` | Clips + transcripts |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line narration review sheet |
| `description.txt` | Short blurb / caption draft |
| `transcripts/` | Extracted source text |

The clean 4K master (`madison-weekly-sep-11.mp4`) and 9:16 short stay local
and are gitignored. Production source for this cut also lives locally at
`Sept 11 - Brutalist Updates/2026-09-11-madison-weekly/` and is **not**
part of this PR.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only, no API keys. Full rebuild path is in `BUILD-PROMPT.md`.
Team videos are source only — do not splice them into the cut.

## Publishing

Not authorized by this package. Master stays local until a human decides to share
or upload.
