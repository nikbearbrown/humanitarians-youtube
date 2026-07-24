# SOURCE-DISCOVERY.md

## Task
NBB-wrap `vox-vhl-hif-slate.mp4` — add Kore cold open, Bear verdict, Bear "Your turn" handoff, and Claude title outro.

## Input
`SOURCE_VIDEO = /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-vhl-hif/vox-vhl-hif-slate.mp4`

## Step 1 — Resolve and verify

ffprobe confirmed the file exists:
- Duration: 293.059 s
- Dimensions: 1920×1080 (16:9)
- Streams: video h264, audio aac 44100 Hz
- Size: 5,188,869 bytes
- SHA-256: `4fc61d9cfe2efbcc56c7fe14d4b376e0fb97ee4d7ffd215cddd662b80b68f9d7`

## Step 2 — Derive slug

Filename: `vox-vhl-hif-slate.mp4`  
Remove known output suffix `-slate` → slug = `vox-vhl-hif`

## Step 3–5 — Search and ranking

| Candidate | Evidence |
|---|---|
| `/Users/bear/.../cancer-biology/youtube/vox-vhl-hif/` | **STRONGEST**: contains `vox-vhl-hif-slate.mp4` (the supplied SOURCE_VIDEO itself, not a copy), plus `beat_sheet.json`, `clips/B01–B17.mp4`, `mp3/beat-B01–B17.mp3`, `manim/B01–B15.mp4`, `media/B02,B12,B16,B17.mp4`, `qc-sheet.png`, `PEDAGOGY.md`, `FACTCHECK.md` |

No other candidate found. The supplied MP4 lives directly inside its production reel.

## Step 6 — Selection

**Selected canonical SOURCE_REEL:**  
`/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-vhl-hif/`

Evidence is unambiguous: the supplied SOURCE_VIDEO is the production reel's own `vox-vhl-hif-slate.mp4` output file.

## Step 7 — Version

Single version. No detached copies found in TMP or Downloads.

## Step 8–11 — Source assets

See SOURCE-MEDIA-LOCK.md for complete ledger.
