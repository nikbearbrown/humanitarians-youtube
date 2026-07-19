# SOURCE-DISCOVERY.md

## Input

`SOURCE_VIDEO = /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-hpylori-cancer/vox-hpylori-cancer-cut.mp4`

## Derived Slug

Filename `vox-hpylori-cancer-cut.mp4`  
Remove `-cut` suffix → `vox-hpylori-cancer`

## Search Strategy

1. Checked the MP4's immediate parent: `/cancer-biology/youtube/vox-hpylori-cancer/`
2. Found `beat_sheet.json` in the same directory with `metadata.slug = "vox-hpylori-cancer"` — exact match.
3. Found `clips/`, `mp3/`, `media/`, `manim/`, `pantry/` all present.
4. Found `vox-hpylori-cancer-slate.mp4` in `mp4/` and `clips/concat.txt` listing all 15 beats.
5. `clips/concat.txt` references `clips/B01.mp4` … `clips/B15.mp4` — all 15 conformed clips present.

## Candidates Considered

| Candidate | Evidence |
|---|---|
| `/cancer-biology/youtube/vox-hpylori-cancer/` | **SELECTED** — contains `beat_sheet.json` with matching slug, SOURCE_VIDEO is the direct sibling `-cut.mp4`, all clips/audio/media present |
| No other candidates found | Search found no duplicate reels for this slug elsewhere in the workspace |

## Selection Evidence

- SOURCE_VIDEO lives at `vox-hpylori-cancer/vox-hpylori-cancer-cut.mp4`
- `beat_sheet.json` `metadata.slug = "vox-hpylori-cancer"` — exact match
- `beat_sheet.json` `metadata.total_estimated_duration_seconds = 182.73` matches SOURCE_VIDEO duration 182.160s
- `clips/concat.txt` lists B01–B15 in order; sum of `actual_duration_s` = 182.682s ≈ SOURCE_VIDEO 182.160s
- 15 conformed clips, 15 mp3 beats, all present

## Canonical SOURCE_REEL

`/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-hpylori-cancer/`

## Body / Outro Identification

Beat sheet identifies OUTRO beats by `act: "OUTRO"`:
- **B14** — `act: "OUTRO"`, `OutroSeries` Remotion scene, duration 2.04s
- **B15** — `act: "OUTRO"`, `OutroCTA` Remotion scene, duration 1.49s

**Body beats: B01–B13** (cumulative 0.000–179.152s from beat durations)
**Outro beats removed: B14, B15** (179.152–182.682s)

Note: SOURCE_VIDEO is 182.16s. The beat-sheet sum gives 182.682s. Small discrepancy (~0.5s) is within normal encode rounding. The body cut will use the source video directly (stream-copy up to the B13 endpoint).
