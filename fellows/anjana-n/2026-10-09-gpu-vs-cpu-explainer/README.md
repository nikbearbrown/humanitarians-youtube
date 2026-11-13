# Why GPUs Beat CPUs for AI

## Series
STEM AI/Data Science Explainers

## Summary
Explains why GPUs are the preferred hardware for AI training and inference. Starts with the core computational cost — neural networks are dominated by matrix multiplication — then contrasts CPU sequential processing with GPU massively parallel SIMD execution. Covers memory bandwidth as the sustained throughput limiter, introduces tensor cores as dedicated matrix acceleration hardware, and closes with the complementary relationship between CPUs (orchestration, control, preprocessing) and GPUs (dense numerical compute).

## Beat structure
| Beat | Title                  | Duration |
|------|------------------------|----------|
| B01  | The Bottleneck         | 13s      |
| B02  | One Fast vs Many Wide  | 13s      |
| B03  | Memory Bandwidth       | 13s      |
| B04  | Tensor Cores           | 13s      |
| B05  | The Full Picture       | 13s      |

## Palette
- CPU blue: #4A90D9
- GPU green: #27AE60
- Matrix gold: #F1C40F
- Tensor purple: #9B59B6
- Muted grey: #95A5A6
- Background: #1A1A2E
- Text: #EAEAEA

---

# As built

The sections above are the authored brief. What follows is what the build
actually produced.

## Beats as rendered

The five authored beats are the body. Four beats were added around
them per the `ai-explainer` structure — a cold-open ask, a verdict, a handoff
and a title outro. Durations are measured from the Kokoro MP3s, which are the
master clock; nothing here was timed by hand.

| Beat | Pattern                | Title                 | Audio   |
|------|------------------------|-----------------------|---------|
| B00  | `ClaudeComposerAsk`    | The Ask (cold open)   | 15.31s  |
| B01  | `GpuBottleneck`        | The Bottleneck        | 31.32s  |
| B02  | `GpuSimd`              | One Fast vs Many Wide | 38.33s  |
| B03  | `GpuBandwidth`         | Memory Bandwidth      | 35.38s  |
| B04  | `GpuTensor`            | Tensor Cores          | 42.86s  |
| B05  | `GpuFullPicture`       | The Full Picture      | 38.71s  |
| B06  | `ClaudeVerdictArtifact`| Verdict               | 36.26s  |
| B07  | `ClaudeComposerAsk`    | Your Turn             | 20.86s  |
| B08  | `ClaudeTitleOutro`     | Title outro           | 2.16s   |
|      |                        | **total**             | **261.19s (4:21)** |

## Voice

Kokoro TTS, `af_bella` — the narrator is Anjana. `beats.json` specifies
`am_onyx`; it is overridden at build time. No channel handle or brand chip
appears on this build.

## Palette

The hex values listed above are used exactly as written, with no role remapped
and no value substituted. Three values the brief implies but does not list were
added for chip outlines (`#2C3E50`) and tube interiors (`#1E1E2E`). The four
Claude-fidelity UI beats (B00, B06, B07, B08) keep the cream/ink house palette;
the five body beats are entirely the brief's.

`GpuBottleneck.tsx` is the palette module — every other component imports its
colours from there, so a change to a hex propagates to all ten compositions.

## Delivery

Both orientations at 4K:

| Cut   | Composition | Master                                   |
|-------|-------------|------------------------------------------|
| 16:9  | 3840×2160   | `gpu-vs-cpu-explainer.mp4`               |
| 9:16  | 2160×3840   | `short/gpu-vs-cpu-explainer-short.mp4`   |

## Rebuild

From this folder, with the toolkit root as the working directory:

```sh
python3 runtime/scripts/generate_audio_kokoro.py /gpu-vs-cpu-explainer
python3 runtime/scripts/remotion_scenes.py      /gpu-vs-cpu-explainer 
./art final /gpu-vs-cpu-explainer
```

## Source files

| Path              | What it is                                        |
|-------------------|---------------------------------------------------|
| `narration/*.txt` | Authored narration, B01–B05, verbatim             |
| `visuals/*.md`    | Authored visual direction, B01–B05                |
| `script.md`       | Full script — authored body plus beats   |
| `beats.json`      | Authored beat spec                                |
| `beat_sheet.json` | Build beat sheet, all nine beats                  |
| `PEDAGOGY.md`     | GATE P record — signed before audio was generated |
| `mp3/`            | Narration and `timings.json` (the master clock)   |
