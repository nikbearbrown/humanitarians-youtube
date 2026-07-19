# SOURCE-DISCOVERY.md — nbb-vox-p53-circuit

**Build date:** 2026-07-16
**Builder:** Claude Code (claude-sonnet-4-6)

---

## Source video

| Field | Value |
|---|---|
| SOURCE_VIDEO | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-p53-circuit/vox-p53-circuit-slate.mp4` |
| Duration | 244.668 s |
| Resolution | 1920×1080 |
| FPS | 24 |
| Video codec | h264 |
| Audio codec | aac 44100 Hz mono |
| File size | 4,509,370 bytes |
| SHA-256 | `dda5b9bf5c7b601d6314b6e86813cee4f99e0a75a8fa64cad6c2ca3d173a7ada` |

## Canonical source reel

`/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-p53-circuit/`

**Selection evidence:** Unambiguous — the supplied MP4 (`vox-p53-circuit-slate.mp4`) lives directly in this folder. `beat_sheet.json`, all `clips/B*.mp4` (B01–B17), all `mp3/beat-*.mp3`, `manim/`, `media/`, `FACTCHECK.md`, `PEDAGOGY.md` all present.

## Body beats

Beats B01–B15 are the locked body. B16 and B17 are `act: OUTRO` and are excluded.

| Beat | Act | actual_duration_s | Clip | Audio |
|---|---|---|---|---|
| B01 | COLD OPEN | 10.03 | `clips/B01.mp4` | `mp3/beat-B01.mp3` |
| B02 | COLD OPEN | 12.07 | `clips/B02.mp4` | `mp3/beat-B02.mp3` |
| B03 | THE QUESTION | 16.67 | `clips/B03.mp4` | `mp3/beat-B03.mp3` |
| B04 | THE PROBLEM | 13.09 | `clips/B04.mp4` | `mp3/beat-B04.mp3` |
| B05 | THE PROBLEM | 9.20 | `clips/B05.mp4` | `mp3/beat-B05.mp3` |
| B06 | THE MECHANISM | 16.25 | `clips/B06.mp4` | `mp3/beat-B06.mp3` |
| B07 | THE MECHANISM | 16.61 | `clips/B07.mp4` | `mp3/beat-B07.mp3` |
| B08 | THE MECHANISM | 16.74 | `clips/B08.mp4` | `mp3/beat-B08.mp3` |
| B09 | THE MECHANISM | 17.74 | `clips/B09.mp4` | `mp3/beat-B09.mp3` |
| B10 | THE MECHANISM | 19.12 | `clips/B10.mp4` | `mp3/beat-B10.mp3` |
| B11 | THE IMPLICATION | 16.38 | `clips/B11.mp4` | `mp3/beat-B11.mp3` |
| B12 | THE IMPLICATION | 13.14 | `clips/B12.mp4` | `mp3/beat-B12.mp3` |
| B13 | THE EXAMPLE | 23.85 | `clips/B13.mp4` | `mp3/beat-B13.mp3` |
| B14 | THE EXAMPLE | 23.82 | `clips/B14.mp4` | `mp3/beat-B14.mp3` |
| B15 | RECAP | 16.904 | `clips/B15.mp4` | `mp3/beat-B15.mp3` |

**Body total duration:** 241.614 s

## Outro beats removed

| Beat | Act | Reason |
|---|---|---|
| B16 | OUTRO | Old `OutroSeries` — replaced by NBB wrapper |
| B17 | OUTRO | Old `OutroCTA` — replaced by NBB wrapper |

**Outro start timecode:** 241.614 s

## Body extraction

Stream-copy cut: `ffmpeg -i vox-p53-circuit-slate.mp4 -t 241.614 -c copy body-locked.mp4`

This produces the locked body segment [00:00, 241.614) from SOURCE_VIDEO.
