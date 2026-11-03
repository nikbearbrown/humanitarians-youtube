# The Persona File.

**Fellow:** Komal BG
**Date:** 2026-09-25
**Format:** Claude-branded ai-explainer (Brutalist)
**Runtime:** 2:03 · **Master:** 4K 16:9 (3840×2160) + 4K 9:16 (2160×3840)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal
**Greeting:** Bonjour, Liam

## What this video is about

A brand personality used to live in a PDF. An **AI brand persona** is a
runnable character — the house, speaking — with a job, a never-say list,
and proof it always cites. Distinct from sibling reels: *The Owned Face.*
(a minted look) and *The Ruler.* / *Archetype Engine.* (the twelve-seat
wheel). Worked example: **L'Oréal Beauty Genius**, shown at CES 2024.

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
| `description.txt` | Short blurb / caption draft |

The clean 4K master (`claude-liam-brand-personas.mp4`) and 9:16 companion stay
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
