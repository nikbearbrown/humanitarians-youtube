# How Kafka Handles Millions of Events

Humanitarians AI / brutalist.art source package for a backend/SWE explainer by Akshay Chavan.

## Deliverables

- Long-form: **3840x2160**, **16:9**, 4K UHD
- Short: **2160x3840**, **9:16**, 4K portrait
- Source QC: ffprobe-based local master validation
- YouTube transcode QC: yt-dlp format inspection; PASS only after a 2160p format is exposed

> Important: the package can enforce and verify a 4K source master. No local build can force YouTube to finish its 4K transcode; `qc/qc_4k.py youtube <URL>` checks when YouTube actually exposes a 2160p rendition.

## Story

A burst of events overwhelms naive direct processing. Kafka absorbs the stream, partitions a topic across brokers, lets consumer groups process partitions in parallel, tracks progress with offsets, rebalances after consumer failure, and protects data with replication.

## Core files

- `beat_sheet.json` — 16:9 long-form authoring spec
- `beat_sheet_short.json` — 9:16 Short authoring spec
- `build_sheet.py` / `build_short.py` — regenerate beat-sheet JSON
- `scenes.py` — 16:9 Manim scenes
- `scenes_short.py` — 9:16 portrait Manim scenes
- `NARRATION.md` — narration copy for both cuts
- `FACTCHECK.md` — technical accuracy notes
- `PEDAGOGY.md` — learning design / beat rationale
- `PROOF-REVIEW.md` — pre-publish review checklist
- `CHECKS-REPORT.md` — expected QC gates
- `qc/qc_4k.py` — validates local resolution and checks YouTube for 2160p
- `render_long.ps1` / `render_short.ps1` — Windows/PowerShell render helpers

## Render assumptions

This package is designed to be placed into the same Humanitarians AI / `brutalist.art` environment used by the reference reels. Remotion pattern names in the beat sheet (`ClaudeComposerAsk`, `ClaudeCodeBeat`, `ClaudeTitleOutro` and portrait equivalents) intentionally follow those conventions.

The Manim sources are self-contained and set their own 4K canvas geometry.

## Render / build flow

1. Regenerate specs if desired:
   - `python build_sheet.py`
   - `python build_short.py`
2. Render Manim long-form:
   - `./render_long.ps1`
3. Render Manim portrait:
   - `./render_short.ps1`
4. Let the brutalist build pipeline render Remotion beats, synthesize narration, and assemble the master.
5. Validate each final local master:
   - `python qc/qc_4k.py local final/kafka-millions-long.mp4 --layout landscape`
   - `python qc/qc_4k.py local final/kafka-millions-short.mp4 --layout portrait`
6. Upload to YouTube and wait for 4K processing.
7. Verify YouTube exposes 2160p:
   - `python qc/qc_4k.py youtube "https://www.youtube.com/watch?v=..."`

## Requirements

- Python 3.12+
- Manim compatible with the brutalist.art environment
- ffprobe / ffmpeg on PATH
- yt-dlp on PATH for YouTube transcode verification

