# Madison Weekly — Nov 6.

**Fellow:** Komal BG
**Date:** 2026-11-06
**Format:** Narrated weekly (Liam summarizes the brief — clips are not spliced)
**Runtime:** 2:08 · **Master:** 4K 16:9 (3840×2160) + 4K 9:16 (2160×3840)
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal
**Greeting:** Ciao, Liam

## What this video is about

Madison weekly. Three tracks:

- **Intelligence Agents.** Detecting inauthentic social engagement (bots, fake
  followers) as a capability. Exploring datasets and baselines. Discussed with
  Nina on Tuesday. **Exploring is not a detector shipped.**
- **CatBot / DogBot + LoonNet.** Reviewing the proposal and planning
  (requirements, features, approach). Outreach is identifying loon, eagle, and
  swan conservation organizations. **A proposal is not a product. Identifying
  is not a partner signed.**
- **Gavia.** Last feature: invasive vegetation detection. Expected to implement
  and deploy by end of this week; demo at next week's meeting. **Expected is
  not deployed. A planned demo is not a demo given.**

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

The clean 4K master (`madison-weekly-nov-6.mp4`) and 9:16 companion stay
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
