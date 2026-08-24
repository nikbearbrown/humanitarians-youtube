# Weekly Report: What's Komal Building? — Loon Conservatory, Week 1

**Fellow:** Komal BG
**Date:** 2026-07-24
**Format:** Fellows sandwich — house setup (Bella) → unedited fellow report → your turn → outro
**Runtime:** ~6:09 · **Master:** 1080p review cut
**Narrator:** Bella (`af_bella`) on house beats; B04 is Komal's own recording audio
**Channel chip / handle on cut:** `@HumanitariansAI`

Advisor feedback is omitted from this cut (provided separately).

## What this video is about

Komal's first weekly report on building a free/legal image repository for a
loon metadata-annotation tool: sourcing from Unsplash, Pexels, and U.S. Fish
& Wildlife Service; tracking provenance in a spreadsheet; writing the research
brief before the schema; and the National Loon Center Foundation (Minnesota)
as the hoped-for beneficiary.

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Recording + named entities |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line house-narration review sheet |
| `description.txt` | Short blurb / caption draft |
| `BUILD-LOG.md` | Dated build notes |
| `qc-sheet.png` | Visual QC contact sheet |

The review master (`Komal_weekly-report-slate.mp4`) stays local and is
gitignored. Production source for this cut also lives locally at
`loon-book/youtube/weekly-report/` and is **not** part of this PR.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only, no API keys. Full rebuild path is in `BUILD-PROMPT.md`.
House voice: `af_bella`. Report beat keeps source audio.

## Publishing

Not authorized by this package. Master stays local until a human decides to share
or upload.
