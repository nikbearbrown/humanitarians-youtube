# The Empty Frame.

**Fellow:** Komal BG
**Date:** 2026-10-23
**Format:** Claude-branded ai-explainer (Brutalist), mixed stills
**Runtime:** 1:59 · **Master:** 4K 16:9 (3840×2160) + 4K 9:16 (2160×3840)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal
**Greeting:** Vanakkam, Liam

## What this video is about

**Conservation AI is not a smarter ranger. It is a filter at scale.** Camera
traps never sleep; most frames are empty. Detect (animal / person / vehicle)
is not classify (species) is not identify (individual — *The Query That
Looks.*, Wildbook). Worked example: **MegaDetector** (Microsoft AI for Good)
— boxes what is there so people stop clicking blanks. A person still reviews.
Always test on your own data.

Body stills break the all-card look: an empty infrared trap frame, a review
queue grid, and a public-domain USFWS trail-camera deer with a teaching
overlay (`animal`, not a species name).

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `short/beat_sheet.json` | 9:16 companion plan |
| `README.md` | This file |
| `SOURCES.md` | Primary sources |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line narration review sheet |
| `SHOTLIST.md` | Per-beat visual plan |
| `PROMPTS.md` | Handoff prompt |
| `CHECKS-REPORT.md` | Teaching-arc / SHOW check |
| `FRICTIONAL.md` | Process log for this cut |
| `description.txt` | Short blurb / caption draft |

The clean 4K master (`claude-liam-empty-frame.mp4`) and 9:16 companion stay
local and are gitignored.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only, no API keys. Full rebuild path is in `BUILD-PROMPT.md`.

## Publishing

Not authorized by this package. Master stays local until a human decides to share
or upload.
