# BUILD-REPORT — nbb-vox-hpylori-cancer

Built: 2026-07-16

## Source

| Item | Value |
|---|---|
| SOURCE_VIDEO | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-hpylori-cancer/vox-hpylori-cancer-cut.mp4` |
| SOURCE_REEL | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-hpylori-cancer/` |
| SOURCE-DISCOVERY.md | `nbb-vox-hpylori-cancer/SOURCE-DISCOVERY.md` |

## Discovery Summary

The SOURCE_VIDEO lives in its canonical production reel directory. Evidence:
- `beat_sheet.json` in same directory, `metadata.slug = "vox-hpylori-cancer"` — exact slug match
- `metadata.total_estimated_duration_seconds = 182.73` matches video 182.160s
- All 15 conformed clips present in `clips/`, 15 MP3s in `mp3/`, Manim/media renders in `manim/` and `media/`
- No other candidates found elsewhere in the workspace
- Selection: unambiguous single candidate

## Discovered Source Assets

| Asset | Role |
|---|---|
| `../vox-hpylori-cancer/beat_sheet.json` | Beat sheet (15 beats, B01–B15) |
| `../vox-hpylori-cancer/clips/B01.mp4–B13.mp4` | Conformed body clips (locked) |
| `../vox-hpylori-cancer/clips/B14.mp4, B15.mp4` | Outro clips (removed in NBB) |
| `../vox-hpylori-cancer/mp3/beat-B01.mp3–beat-B13.mp3` | Body audio (locked) |
| `../vox-hpylori-cancer/manim/B01.mp4–B13.mp4` | Manim graphics for body beats |
| `../vox-hpylori-cancer/media/B02.mp4` | SlateCard Remotion render |
| `../vox-hpylori-cancer/FACTCHECK.md` | Source fact-check record |
| `../vox-hpylori-cancer/PEDAGOGY.md` | Source pedagogy record |

## Old Outro Removal

| Beat | Act | Duration | Timecode onset |
|---|---|---|---|
| B14 | OUTRO (OutroSeries) | 2.04s | 179.152s |
| B15 | OUTRO (OutroCTA) | 1.49s | 181.192s |

Old outro removed by stream-copying SOURCE_VIDEO from 0 to 179.152s (body only).

## Locked Body

| Property | Value |
|---|---|
| Duration | 179.152s (B01–B13 actual_duration_s sum) |
| Actual extracted duration | 179.240s (ffprobe on body.mp4 — within encode rounding) |
| Dimensions | 1280×720, H.264, 24fps |
| Audio | AAC mono 44100Hz |
| Body beats | B01, B02, B03, B04, B05, B06, B07, B08, B09, B10, B11, B12, B13 |

Body clips reused: `../vox-hpylori-cancer/clips/B*.mp4` referenced in beat_sheet.nbb.json (locked=true). Assembly extracted body from SOURCE_VIDEO via stream-copy.

## Source SHA-256 Verification

| File | Expected SHA-256 | Verified SHA-256 | Status |
|---|---|---|---|
| `vox-hpylori-cancer-cut.mp4` | `7c619ae57ce4ece76b927b0fa26f4b8ba0a03219f735facd531db1fb40b6e627` | `7c619ae57ce4ece76b927b0fa26f4b8ba0a03219f735facd531db1fb40b6e627` | PASS |

## New Wrapper Beats

### Cold Open (NBB00)

| Property | Value |
|---|---|
| Greeting | "Selam, Kore" (Amharic hello) |
| Question | "Why does a stomach bacterium cause cancer after 30 to 50 years?" |
| End sentence | "Can you explain it, Bear?" |
| Audio path | `mp3/beat-NBB00.mp3` |
| Duration | 8.38s |
| Visual | ClaudeComposerAsk @ 1920x1080 → scaled to 1280x720 |

### Verdict (NBB01)

| Property | Value |
|---|---|
| Narration summary | Mechanism: chronic inflammation → ROS/RNS → Correa cascade. Trade-off: probabilistic threshold, 35% reduction with antibiotics |
| Audio path | `mp3/beat-NBB01.mp3` |
| Duration | 29.42s |
| Visual | ClaudeVerdictArtifact @ 1920x1080 → scaled to 1280x720, frozen last frame to cover audio |

### Your Turn (NBB02)

| Property | Value |
|---|---|
| Paste-ready prompt | Traces inflammation-first mechanism for viewer's own infection-linked cancer using H. pylori as template, with 5 specific elements |
| Audio path | `mp3/beat-NBB02.mp3` |
| Duration | 7.81s |
| Visual | ClaudeComposerAsk @ 1920x1080 → scaled to 1280x720 |

### Outro (NBB03)

| Property | Value |
|---|---|
| Title | "Why Ulcer Bacteria Also Cause Cancer" |
| Handle | @HumanitariansAI |
| Subline | "inflammation is the engine, antibiotics are the off switch" |
| Duration | 6.0s (silence) |
| Visual | ClaudeTitleOutro @ 1920x1080 → scaled to 1280x720 |

## Final Video

| Property | Value |
|---|---|
| Path | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-hpylori-cancer/vox-hpylori-cancer-nbb.mp4` |
| Duration | 230.89s |
| Dimensions | 1280×720 |
| Video codec | H.264, 24fps |
| Audio codec | AAC mono 44100Hz |
| File size | 5,442,034 bytes (5.19 MB) |
| Expected duration | 8.38 + 179.25 + 29.42 + 7.81 + 6.0 = 230.86s (match within rounding) |

## Assembly Notes

- Remotion scenes rendered at 1920x1080 (composition default), scaled down to 1280x720 via `scale=1280:720:flags=lanczos` to match body canvas
- `ClaudeVerdictArtifact` composition is 180 frames (12s) at 24fps — extended to 29.42s using `tpad=stop_mode=clone` (freeze last frame) to cover verdict narration duration
- Body extracted from SOURCE_VIDEO via stream-copy (`ffmpeg -t 179.152 -c copy`)
- All segments normalized to yuv420p, 44100Hz, 1ch before concat
- One final encode applied to entire assembly (unavoidable for format normalization)
- No body beats re-encoded individually — body extracted as one stream-copy then re-encoded once in final concat

## Pedagogy and Factcheck

| Check | Verdict |
|---|---|
| PEDAGOGY.md | PASS |
| FACTCHECK.md | PASS |

## QC Sheet

`nbb-vox-hpylori-cancer/QC-sheet.png` — 3×3 grid: cold open, B01, B04, B09, B12, B13, verdict, your turn, outro

## Ready to Review

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-hpylori-cancer/vox-hpylori-cancer-nbb.mp4
```
