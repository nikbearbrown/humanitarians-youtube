# Madison Weekly — Sep 4.

**Fellow:** Komal BG
**Date:** 2026-09-04
**Format:** Narrated weekly (Liam summarizes team videos — clips are not spliced)
**Runtime:** ~2:52 · **Master:** 4K (3840×2160) + 9:16 short
**Narrator:** Liam (`am_onyx`), in for Komal
**Channel chip / handle on cut:** Komal

## What this video is about

Madison weekly, three tracks:

- **Sai** closed the annotation set: about 136 quality-checked common-loon images, every box by hand. Nothing trained yet. First YOLO run next week.
- **Karishma** designed a persona-aware LLM visibility study (who a model recommends brands *to*, not only which brands).
- **Komal** wrote the strategic plan for a Jungian brand-archetype detector (evidence, hybrid tension, applied brief).

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `short/beat_sheet.json` | 9:16 companion plan |
| `README.md` | This file |
| `SOURCES.md` | Clips + plan |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line narration review sheet |
| `description.txt` | Short blurb / caption draft |
| `transcripts/` | Extracted source text |

The clean 4K master (`madison-weekly-sep-4.mp4`) and 9:16 short stay local
and are gitignored. Production source for this cut also lives locally at
`Sept 4 - Brutalist Updates/2026-09-04-madison-weekly-sep-4/` and is **not**
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
Team videos are source only — do not splice them into the cut.

## Publishing

Not authorized by this package. Master stays local until a human decides to share
or upload.
