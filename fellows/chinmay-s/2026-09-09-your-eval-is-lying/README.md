# Your Eval Is Lying to You

An LLM evaluation notebook that reports 0.0 for everything — and why that is the harness, not the model.

| | |
|---|---|
| **Runtime** | 5:57 · 26 beats · 1920x1080 |
| **Voice** | Kokoro Bella (`af_bella`) |
| **Channel** | @HumanitariansAI |
| **Built** | 2026-09-09 |
| **Cost** | $0.00 — no paid APIs |

## What is here

The master MP4 is **not** committed: this repository keeps large distribution media out
of Git. `beat_sheet.json` is the source of truth — narration, timing, scene routing and
measured per-beat durations — and the reel rebuilds from it.

- `EvalCartoon.tsx`
- `EvalHarness.tsx`
- `PEDAGOGY.md`
- `beat_sheet.json`
- `build_beat_sheet.py`

## Scenes used

- `ClaudeComposerAsk`
- `ClaudeTitleOutro`
- `ClaudeVerdictArtifact`
- `EvalBeforeAfter`
- `EvalGoldenTest`
- `EvalGraderStamp`
- `EvalNormalizer`
- `EvalPipeline`
- `EvalPromptDiff`
- `EvalRegexMiss`
- `EvalScoreboard`
- `EvalSilentCatch`
- `EvalTokenOverlap`
- `EvalTwinZeros`
- `EvalZeroChart`
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
