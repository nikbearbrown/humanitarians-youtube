# Madison Weekly — Oct 9.

**Fellow:** Komal BG
**Date:** 2026-10-09
**Format:** Narrated weekly (Liam summarizes the brief — clips are not spliced)
**Runtime:** 2:23 · **Master:** 4K 16:9 (3840×2160) + 4K 9:16 (2160×3840)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal
**Greeting:** Olá, Liam

## What this video is about

Madison weekly. Three tracks:

- **SurveyMind.** Tried the paper's method again; it failed. Four papers on
  synthetic personas, then a plan to build their own fake-data generator:
  **80% to build, 20% held out.** Sent for review. A literature plan is not
  a generator.
- **Laptop recommendation study:** 39-prompt set finalized (baseline, student,
  developer, creative, enterprise). Collected in Claude Opus 5.5 (medium, web
  search), mapped to prompt IDs, tracker and coding sheet, initial brand
  comparison, draft findings. **Collected is not a ranking.**
- **Loon Conservatory:** app is built; testing is underway. **Built is not
  tested.** Repo is source-only — not spoken or shown.

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
| `FRICTIONAL.md` | Process log for this cut |
| `description.txt` | Short blurb / caption draft |
| `transcripts/brief.txt` | Source brief |

The clean 4K master (`madison-weekly-oct-9.mp4`) and 9:16 companion stay
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
