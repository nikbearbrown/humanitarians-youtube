# Madison Weekly — Scope Locked.

**Fellow:** Komal BG
**Date:** 2026-08-21
**Format:** Claude-branded narrated weekly (Brutalist) — no Zoom sandwich
**Runtime:** ~2:26 · **Master:** 4K (3840×2160) + 9:16 short
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal

## What this video is about

Komal's Madison weekly: the team locked scope and milestones with Nina, chose
**CVAT** over building annotation from scratch, lined up three weeks of build
work, kept collecting free-licensed images, and opened a second track on brand
frameworks for Madison tools.

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `short/beat_sheet.json` | 9:16 companion plan |
| `README.md` | This file |
| `SOURCES.md` | Written brief (only source of claims) |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line narration review sheet |
| `description.txt` | Short blurb / caption draft |

The clean 4K master (`madison-weekly-scope-cvat.mp4`) and 9:16 short stay local
and are gitignored. Production source for this cut also lives locally at
`loon-book/youtube/madison-weekly-scope-cvat/` and is **not** part of this PR.

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
