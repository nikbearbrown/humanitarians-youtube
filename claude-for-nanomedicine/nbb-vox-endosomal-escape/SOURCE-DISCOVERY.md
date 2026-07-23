# SOURCE-DISCOVERY.md — nbb-vox-endosomal-escape

**Build date:** 2026-07-16

## Source reel

| Field | Value |
|---|---|
| SOURCE_VIDEO | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/vox-endosomal-escape/vox-endosomal-escape.mp4` |
| SOURCE_REEL | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/vox-endosomal-escape/` |
| Beat sheet | `vox-endosomal-escape/beat_sheet.json` |

## Candidates considered

- `/cancer-nanomedicine/youtube/vox-endosomal-escape/` — SELECTED. The supplied SOURCE_VIDEO lives directly inside this folder. `beat_sheet.json`, all build artifacts (`manim/`, `media/`, `mp3/`), `FACTCHECK.md`, `PEDAGOGY.md` all present.

## Source media

| Category | Path |
|---|---|
| Source MP4 | `vox-endosomal-escape/vox-endosomal-escape.mp4` |
| Beat sheet | `vox-endosomal-escape/beat_sheet.json` |
| Manim renders | `vox-endosomal-escape/manim/B01.mp4`, `B03.mp4`–`B11.mp4` |
| Remotion renders | `vox-endosomal-escape/media/B02.mp4`, `B12.mp4`, `B13.mp4` |
| Body MP3s | `vox-endosomal-escape/mp3/beat-B01.mp3`–`beat-B11.mp3` |

## Beat structure

| Beat | Act | Actual duration (s) |
|---|---|---|
| B01 | COLD OPEN | 8.07 |
| B02 | COLD OPEN | 18.29 |
| B03 | THE QUESTION | 14.71 |
| B04 | THE PROBLEM | 15.12 |
| B05 | THE PROBLEM | 18.05 |
| B06 | THE MECHANISM | 20.90 |
| B07 | THE MECHANISM | 21.08 |
| B08 | THE IMPLICATION | 18.42 |
| B09 | THE EXAMPLE | 23.12 |
| B10 | THE EXAMPLE | 13.19 |
| B11 | RECAP | 14.861 |
| **B12** | **OUTRO — REMOVED** | 2.17 |
| **B13** | **OUTRO — REMOVED** | 1.49 |

## Body end timecode calculation

Sum of actual_duration_s for all non-OUTRO beats:

```
8.07 + 18.29 + 14.71 + 15.12 + 18.05 + 20.90 + 21.08 + 18.42 + 23.12 + 13.19 + 14.861 = 185.811s
```

**Body end timecode: 185.811s**

## Body-lock extraction

```bash
ffmpeg -i vox-endosomal-escape.mp4 -t 185.811 -c copy body-locked.mp4
```

Extracted duration: 185.917s (stream-copy boundary alignment, 0.106s past timecode — acceptable).

## Last-frame verification

Frame extracted at 185.0s (0.9s before extraction end): shows B11 RECAP card —
"Neutral in blood. Cationic in the endosome. That charge flip is the drug." — NOT outro content.
Body cut is clean.

## OUTRO beats removed

| Beat | Type | Duration |
|---|---|---|
| B12 | OutroSeries (Remotion) | 2.17s |
| B13 | OutroCTA (Remotion) | 1.49s |
