# Madison Weekly — Nov 27.

**Fellow:** Komal BG
**Date:** 2026-11-27
**Format:** Narrated weekly (Liam summarizes the brief — clips are not spliced)
**Runtime:** 2:11 · **Master:** 4K 16:9 (3840×2160) + 4K 9:16 (2160×3840)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal
**Greeting:** Namaste, Liam

## What this video is about

Madison weekly. One track from the project brief:

- **Intelligence Agents layer.** Madison is **building** a machine-learning
  capability that detects inauthentic Instagram engagement (bots, fake
  followers, fake likes and comments). It returns two explainable risks:
  how likely the **account** is fake, and separately how likely the
  **likes and comments on a given post** are fake.
- **Who it is for.** Smaller brands, independent creators, and nonprofits
  cannot easily buy the proprietary desks large companies use.
- **How it differs (their competitive reading).** Reviewed tools
  (HypeAuditor, Modash, CreatorIQ) score the account with rules. Madison
  trains on TwiBot-20 so performance can be measured, and adds a second
  layer on the post. **A Twitter benchmark is not Instagram ground truth.
  Appear is not a census. Building is not shipped.**

No teammate names on the cut. Body plates are drawn cards, not photographs.

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
| `transcripts/brief.txt` | Source brief |
| `assets/render_plates.py` | Teaching plates (16:9 + 9:16) |

The clean 4K master (`madison-weekly-nov-27.mp4`) and 9:16 companion stay
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
Do not splice team videos into the cut.

## Publishing

Not authorized by this package. Master stays local until a human decides to share
or upload.
