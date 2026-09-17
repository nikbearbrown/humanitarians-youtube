# SOURCES — "16-bit or 24-bit: What Bit Depth Does"

Where every number came from, and what the method cannot tell you.

## Primary: an experiment run for this reel

`measure_bitdepth.py`, in this folder. numpy only — no ffmpeg, no network, no
account. Rerunnable:

```bash
python3 measure_bitdepth.py
```

Raw output: [MEASUREMENTS.txt](./MEASUREMENTS.txt).

### Method

1. Generate 20 s of a 440 Hz sine at −6 dBFS peak in **float64**.
2. Quantise a copy to 8-, 16- and 24-bit by **mid-tread rounding**, with **no
   dither**: `round(x / step) * step`, `step = 2 / 2^bits` over a −1..+1 scale.
3. Take the error signal — quantised minus original — and measure its **RMS in
   dBFS** relative to full scale.
4. Report the error level, the step size, and the implied dynamic range.

### Results

| depth | error RMS (dBFS) | `6.02b + 1.76` | offset | step size |
|---|---|---|---|---|
| 8-bit | **−53.14** | −49.9 | −3.2 | 7.812e-03 |
| 16-bit | **−100.75** | −98.1 | −2.7 | 3.052e-05 |
| 24-bit | −149.56 | −146.2 | −3.3 | 1.192e-07 |

Signal RMS −9.03 dBFS, peak −6.0 dBFS. Derived: **5.95 dB/bit** across 8→16 and
**6.10 dB/bit** across 16→24.

### What this method does not tell you

- **Nothing about audibility.** It measures a level in dBFS. Whether that level
  is audible depends on the playback gain and the room, which is exactly why B04
  draws a room line instead of asserting a threshold.
- **Nothing about dithered audio.** Real 16-bit masters are usually dithered,
  which trades a slightly higher but far less correlated noise floor for the
  absence of quantisation distortion at low levels. The measured figures are the
  **undithered** case, which is the simpler claim and the one the reel makes.
- **Nothing about a specific encoder or DAW.** It measures the arithmetic of
  fixed-point storage, not any product's implementation.
- **Nothing about perceived quality.** No listening test was run, and the reel
  makes no perceptual claim beyond "below the room you are sitting in".

### The ~3 dB offset, stated plainly

Every measured floor sits about 3 dB below the textbook formula. The formula
assumes a full-scale sine and an idealised uniform error distribution; this
signal peaks at −6 dBFS and is rounded rather than dithered. The offset is
consistent across all three depths — the signature of a systematic difference in
assumptions, not of a mistake. **The reel reports the measured values** and names
the method on screen.

### Why not ffmpeg

The first attempt used `ffmpeg` + `volumedetect`. ffmpeg's filter graph is
32-bit float internally, which carries a 24-bit mantissa, so a 24-bit round trip
is *lossless to ffmpeg* and it reports an error of `-inf`. That is a limit of the
tool, not a property of 24-bit audio. float64 has the headroom to measure all
three depths. Recorded in [BUILD-LOG.md](./BUILD-LOG.md).

## Secondary: established results, used as stated

These are not measured here. They are standard, and the reel states them in
plain language with no invented figures attached.

| Used for | What is relied on |
|---|---|
| B02 — "every measurement has to land on a marking" | the definition of uniform (mid-tread) quantisation |
| B03 — "all those small errors together are a sound" | undithered quantisation error of a complex signal is noise-like and broadband |
| B03 — "coarser ruler, louder hiss" | error is bounded by ±½ step, so its RMS scales with step size — and this reel's own measurement confirms it |
| B04 — the whisper-to-rock-concert anchor | published everyday SPL tables. These disagree by ~30 dB at both ends: a whisper is given as 20–30 dB SPL and a rock concert as 100–120, so the gap is 70–100 dB. The reel says *roughly* and the label says *≈*, and the on-screen ladder is drawn relative to full volume rather than in absolute SPL |
| B05 — "every edit rounds all over again" | fixed-point processing re-quantises after each gain stage; gain applied to a signal applies to its noise floor too |
| B05 — 16-bit is a third smaller | 16 ÷ 24 = 0.667, at the same sample rate and length |

## Toolchain

| Tool | Version / note | Cost |
|---|---|---|
| Kokoro TTS (`af_bella`) | local, `generate_audio_kokoro.py` | **$0.00** |
| faster-whisper (`align.py`) | local word-level alignment | **$0.00** |
| Remotion | 4.0.486 (core, `@remotion/*` pinned to match) | free |
| numpy | float64 measurement | free |
| ffmpeg / ffprobe | compile, concat, QC frame extraction | free |
| `remotion-bits`, `@remotion/shapes`, `@remotion/paths`, `@remotion/noise`, `@remotion/motion-blur`, `@remotion/layout-utils`, `@remotion/google-fonts` | motion/typography libraries | free |

No paid API was called at any point. Fellow Tier cost: **$0.00**.

## Licence diligence on the motion research

Two template collections were read while researching the animation upgrade:

- [`reactvideoeditor/remotion-templates`](https://github.com/reactvideoeditor/remotion-templates)
  — **MIT.** Patterns adapted where useful.
- [`ali-abassi/remotion-templates`](https://github.com/ali-abassi/remotion-templates)
  — **no licence declared.** Read for conventions only; **no code copied.**

The spring constants used across this reel (`damping 12–14, mass 0.5–0.6,
stiffness 80–100`) are the convention observed across 81 professionally built
Remotion templates, not a copied snippet.
