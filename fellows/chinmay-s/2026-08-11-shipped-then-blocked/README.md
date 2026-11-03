# Shipped, Then Blocked

The same 12-week sprint cut to 3 minutes, ending on the week it stopped for a permission.

| | |
|---|---|
| **Runtime** | 2:58 · 14 beats · 1920x1080 |
| **Voice** | Kokoro Bella (`af_bella`) |
| **Channel** | @HumanitariansAI |
| **Built** | 2026-08-11 |
| **Cost** | $0.00 — no paid APIs |

## What is here

The master MP4 is **not** committed: this repository keeps large distribution media out
of Git. `beat_sheet.json` is the source of truth — narration, timing, scene routing and
measured per-beat durations — and the reel rebuilds from it.

- `IndexedOrInvisible.tsx`
- `PEDAGOGY.md`
- `beat_sheet.json`

## Scenes used

- `ClaudeComposerAsk`
- `ClaudeTitleOutro`
- `ClaudeVerdictArtifact`
- `IdxBatchFlow`
- `IdxBlocked`
- `IdxFaqVariation`
- `IdxMatrix`
- `IdxOutcomes`
- `IdxPipelineFlow`
- `IdxSplitPane`
- `IdxStatement`

## Rebuild

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>   # audio durations are the clock
python3 runtime/scripts/remotion_scenes.py     <reel>
python3 runtime/scripts/compile.py             <reel> --height 1080
```

Audio durations *are* the timeline, so any narration edit re-renders the beats it moves.
Verify every beat carries a video stream before compiling — a failed render can still
write an audio-only MP4 that the toolkit counts as a successful fill.
