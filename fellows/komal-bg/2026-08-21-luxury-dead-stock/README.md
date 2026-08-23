# Dead Stock.

**Fellow:** Komal BG
**Date:** 2026-08-21
**Format:** Claude-branded ai-explainer (Brutalist)
**Runtime:** ~2:22 · **Master:** 4K (3840×2160)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal

## What this video is about

Luxury rarely says **dead stock** out loud. High margins historically paid for
overproduction to avoid stockouts — until EU Ecodesign rules closed destruction
as the brand-protecting exit, and **AI demand forecasting + allocation** became
the upstream fix.

The live rule is **ESPR (Regulation (EU) 2024/1781)**: large companies cannot
destroy unsold clothes, accessories, and footwear from **19 July 2026**.

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Primary sources + corrections log |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line narration review sheet |
| `description.txt` | Short blurb / caption draft |
| `_qc/REPORT.md` | Visual QC notes |
| `_qc/*-frame.png` | Sample late-beat stills |

The clean 4K master (`claude-liam-luxury-dead-stock.mp4`) stays local and is
gitignored. Production source for this cut also lives locally at
`claude-for-branding/youtube/claude-liam-luxury-dead-stock/` and is **not**
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

## Publishing

Not authorized by this package. Master stays local until a human decides to share
or upload.
