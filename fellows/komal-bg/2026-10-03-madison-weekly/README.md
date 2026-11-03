# Madison Weekly — Oct 3.

**Fellow:** Komal BG
**Date:** 2026-10-03
**Format:** Narrated weekly (Liam summarizes the brief — clips are not spliced)
**Runtime:** 2:32 · **Master:** 4K 16:9 (3840×2160) + 4K 9:16 (2160×3840)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal
**Greeting:** Vanakkam, Liam

## What this video is about

Madison weekly. Two tracks:

- **Loon Conservatory.** Backend moved from Python to Rust. Memory about
  80 MB down to about 40 MB. Batch processing up to 25 files, including zip
  folders. Updates inject automatically from how many they push and download.
  **macOS confidence is not a Windows test — Windows is next.**
- **Laptop recommendation study** (separate): moved from preparation into
  actual model testing. Same 13-prompt mini-pilot twice in separate Claude
  chats (Opus 5.5, medium effort, web search on) = 26 real responses. Apple
  in all 26; Lenovo and Dell same frequency both rounds; reasoning changed
  with user context. **26 replies is not the 39-prompt analysis.**

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

The clean 4K master (`madison-weekly-oct-3.mp4`) and 9:16 companion stay
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
