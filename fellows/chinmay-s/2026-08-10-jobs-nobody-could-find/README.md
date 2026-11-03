# The Jobs Nobody Could Find

A 12-week ship log for a job board: a five-tier visa classifier and the SEO stack that made 23,000 listings findable.

| | |
|---|---|
| **Runtime** | 6:08 · 26 beats · 1920x1080 |
| **Voice** | Kokoro Bella (`af_bella`) |
| **Channel** | @HumanitariansAI |
| **Built** | 2026-08-10 |
| **Cost** | $0.00 — no paid APIs |

## What is here

The master MP4 is **not** committed: this repository keeps large distribution media out
of Git. `beat_sheet.json` is the source of truth — narration, timing, scene routing and
measured per-beat durations — and the reel rebuilds from it.

- `PEDAGOGY.md`
- `SHOPPING.md`
- `SOURCES.md`
- `beat_sheet.json`

## Scenes used

- `ClaudeCodeBeat`
- `ClaudeComposerAsk`
- `ClaudeTitleOutro`
- `ClaudeVerdictArtifact`
- `SlateCard`

## Rebuild

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>   # audio durations are the clock
python3 runtime/scripts/remotion_scenes.py     <reel>
python3 runtime/scripts/compile.py             <reel> --height 1080
```

Audio durations *are* the timeline, so any narration edit re-renders the beats it moves.
Verify every beat carries a video stream before compiling — a failed render can still
write an audio-only MP4 that the toolkit counts as a successful fill.
