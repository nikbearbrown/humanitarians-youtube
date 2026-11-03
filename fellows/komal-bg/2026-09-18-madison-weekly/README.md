# Madison Weekly — Sep 18.

**Fellow:** Komal BG
**Date:** 2026-09-18
**Format:** Narrated weekly (Liam summarizes the brief — clips are not spliced)
**Runtime:** 2:13 · **Master:** 4K 16:9 (3840×2160) + 4K 9:16 (2160×3840)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal
**Greeting:** Hallo, Liam

## What this video is about

Madison weekly. One numbered receipt, three other tracks:

- **Visibility-pilot runner.** 39 unique prompts, shuffled into 117 attempts (×3). Automated runner. Counting rules locked (mention ≠ rec, order ≠ rank, always the denominator). Five local tests passed. **Zero live queries.**
- **Laptop recommendation study** (separate): prompts under test; real responses starting.
- **Loon Conservatory:** API for the metadata annotation tool; demo model and brand deck in progress.
- **Jungian brand-archetype detector:** research started, not built.

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `short/beat_sheet.json` | 9:16 companion plan |
| `README.md` | This file |
| `SOURCES.md` | Brief as source |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line narration review sheet |
| `SHOTLIST.md` | Per-beat visual plan |
| `PROMPTS.md` | Handoff prompt |
| `CHECKS-REPORT.md` | Teaching-arc / SHOW check |
| `description.txt` | Short blurb / caption draft |
| `transcripts/brief.txt` | Source brief |

The clean 4K master (`madison-weekly-sep-18.mp4`) and 9:16 companion stay
local and are gitignored. Pipeline renders (`mp3/`, `media/`, `clips/`,
`vertical/`) stay local.

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
