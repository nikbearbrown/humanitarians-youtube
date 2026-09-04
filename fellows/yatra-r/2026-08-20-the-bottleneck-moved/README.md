# The Bottleneck Moved.

**AI · MARKETING** · 10 beats · 2:46.1 · narrated by Yatra
(Kokoro `af_bella`, local and free) · `@Yatra`

## What this folder is

The **source** of the video, not the video. `beat_sheet.json` is the single source of
truth: every beat's narration, its measured audio duration, the Remotion composition that
renders it, and a `show` block describing what the viewer watches. Given the toolkit, this
folder rebuilds the episode from scratch — audio, frames and all.

Media (mp4/mp3/png) is deliberately not committed.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 source of truth — narration, measured durations, scene + props per beat |

| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds this episode end to end |
| `CHECKS-REPORT.md` | PROOF GATE record — per-beat classification and the teaching-arc checklist |
| `FACTCHECK.md` | Claim-by-claim ledger: what is asserted, on whose authority, and what is deliberately not claimed |
| `PROMPTS.md` | Every prompt shown on screen, verbatim |
| `QC-LOG.md` | Frame-level visual QC — defects found, fixed, and deliberately accepted |
| `SHOTLIST.md` | Typed work order — measured durations, frame counts, composition per beat |

## How to read it

Start with `FACTCHECK.md`. It states what the episode claims and — more usefully — what it
refuses to claim and why. The beat sheet is the machine's copy; the fact-check is the
argument's.

## Rebuild

Free and local: Kokoro TTS, Remotion, ffmpeg. No API keys.

```bash
python3 runtime/scripts/generate_audio_kokoro.py <this-folder>   # audio is the master clock
python3 runtime/scripts/remotion_scenes.py <this-folder>          # render each beat
./art final <this-folder>                                         # compile the master
```

Regenerating audio changes the measured durations, so each composition's
`durationInFrames` must be retargeted to match, or progress-mapped animations get trimmed.
