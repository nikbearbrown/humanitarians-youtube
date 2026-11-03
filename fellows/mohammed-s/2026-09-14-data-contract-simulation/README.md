# Prove The Number Changed.

A `cli-explainer` build reel about the data contract agent in
[`mdhussainshariff/Mycroft`](https://github.com/mdhussainshariff/Mycroft) →
`Data_Quality_Agent/`, and the metric-impact simulation added to it on branch
`feature/metric-impact-simulation` (commit `4469968`).

**The one insight:** a schema change can compile, run, pass every test, and still
return a number that is wrong — and the only honest way to warn about it is to
rebuild the marts and measure.

| | |
|---|---|
| Skill | `cli-explainer` (prompt → real code → moving output) |
| Voice | Kokoro `am_onyx` ("Onyx"), Teardown register |
| Narrator | Hussain, first person — no channel persona |
| Runtime | 2:06 · 11 beats |
| Masters | `data-contract-simulation.mp4` (3840×2160) · `916/data-contract-simulation-916.mp4` (2160×3840) |

## Spine

| Beat | Act | Scene | s |
|---|---|---|---|
| B00 | INTRO | `ClaudeComposerAsk` | 12.9 |
| B01 | PROBLEM | `SimSilentBreak` | 14.2 |
| B02 | CLI | `ClaudeComposerAsk` | 10.5 |
| B03 | CODE | `ClaudeCodeBeat` | 14.1 |
| B04 | OUTPUT | `SimLoudHalf` | 11.2 |
| B05 | CHANGE | `ClaudeComposerAsk` | 13.1 |
| B06 | CODE | `ClaudeCodeBeat` | 14.4 |
| B07 | OUTPUT | `SimMoneyShot` | 9.9 |
| B08 | SUMMARY | `SimThreeLayers` | 12.9 |
| B09 | NEXT STEPS | `ClaudeComposerAsk` | 10.9 |
| B10 | OUTRO | `ClaudeTitleOutro` | 2.1 |

B02–B04 are cycle 1; B05–B07 are the revision cycle the REVISION LAW requires.
The revision is not a contrivance — it is the actual design problem the feature
had to solve (see `PEDAGOGY.md`).

## The 9:16 is a reflow, not a crop

Each bespoke scene is ONE component in
`brutalist.art/runtime/remotion/src/scenes/SimImpactIllus.tsx`, registered twice in
`Root.tsx` — `<Name>` at 1920×1080 and `<Name>916` at 1080×1920 — and it branches
internally on `portrait`. Sizes are fractions of the content box, so the same
authored number reads *larger* on a phone, and `--scale=2` gives true 4K in both
aspects with no layout change. `make_916.py`'s ONDA CHECK refuses to build the
vertical cut unless a real portrait composition exists for every beat.

`./art shorts` is deliberately **not** used: it builds a *Short* (drops beats for
the 3:00 cap, rewrites the outro, centre-cuts). This is the same video in two
geometries, every beat intact.

## Rebuild

```bash
TOOLKIT=../../../brutalist.art
python build_sheet.py                                   # author the beat sheet
$TOOLKIT/venv/Scripts/python.exe $TOOLKIT/runtime/scripts/generate_audio_kokoro.py .
python sync_durations.py .                              # audio → durationSeconds
ART_CONCURRENCY=4 $TOOLKIT/venv/Scripts/python.exe \
    $TOOLKIT/runtime/scripts/remotion_scenes.py .
python make_916.py --force && python sync_durations.py 916
ART_CONCURRENCY=4 $TOOLKIT/venv/Scripts/python.exe \
    $TOOLKIT/runtime/scripts/remotion_scenes.py ./916
```

Prefix every toolkit script with `PYTHONIOENCODING=utf-8` on Windows — the sheet
carries em dashes and arrows, and the cp1252 console will kill a long run midway.

## Paperwork

- `PEDAGOGY.md` — GATE P, with the claim ledger
- `build_sheet.py` — the beat sheet's single source of truth
- `_qc/` — sampled frames for the visual QC pass
