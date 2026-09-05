# SOURCES — "What MP3 Throws Away"

## Primary source: an experiment run for this reel

Every number on screen was measured on this machine on 2026-09-04, **before**
the beat sheet was written, so the script describes the result rather than the
result being fitted to the script. Raw log:
[MEASUREMENTS.txt](./MEASUREMENTS.txt).

### Method

```bash
# 1. a source with a known, flat spectrum
ffmpeg -f lavfi -i "anoisesrc=d=10:c=white:r=44100:a=0.5" -ac 2 -c:a pcm_s16le src.wav

# 2. encode and decode back
ffmpeg -i src.wav -c:a libmp3lame -b:a 128k enc_128.mp3
ffmpeg -i enc_128.mp3 -c:a pcm_s16le dec_128.wav      # and the same at 320k

# 3. measure surviving energy in 500 Hz-wide bands
ffmpeg -i dec_128.wav -af "bandpass=f=17000:width_type=h:w=500,volumedetect" -f null -
```

**Why white noise.** A flat source spectrum makes the encoder's decisions
directly legible: anything missing afterwards was removed by the encoder, not
absent from the input. With music you cannot separate "the encoder discarded
this" from "the song never had it."

**Why decode before measuring.** Measuring the `.mp3` would measure the
bitstream. Decoding back to PCM measures what a listener actually receives.

### Results used on screen

| Where | Figure | Measured |
|---|---|---|
| B01 cliff | 16 kHz | 16 kHz at −0.6 dB, 17 kHz at −13.2 dB |
| B01 drop label | −13.2 dB at 17 kHz | source −34.0, 128 kbps −47.2 |
| B03 ratios | 11 : 1 · 4.4 : 1 · 1 : 1 | 1,764,078 ÷ 160,958 = 10.96; ÷ 402,329 = 4.38 |
| B03 byte counts | 160,958 / 402,329 / 1,764,078 | file sizes on disk |
| B03 320k cliff | 20 kHz | identical to source through 19 kHz; 20 kHz −3.5 dB |
| B04 steps | −31.1 / −33.3 / −34.7 / −37.8 dB | 12 kHz band at 1 / 4 / 6 / 11 encodes |
| B04 total | −7.0 dB | source −30.8 → 11 encodes −37.8 |

### Generation-loss procedure

The decoded 128 kbps file was re-encoded at 128 kbps and decoded again, ten
more times, measuring the 12, 14 and 15 kHz bands at generations 1, 4, 6 and
11. All three bands degrade monotonically and by similar amounts, so the reel
reports one band and says so on screen (`12 kHz band`).

### Stated limits of the experiment

- **One encoder, one mode.** libmp3lame at constant bitrate, as shipped with
  the ffmpeg on this machine. Other encoders and VBR modes pick different
  lowpass points. The B03 footnote states this on screen.
- **Noise is not music.** A real bit allocator behaves differently on tonal
  material. The lowpass shelf is stable across content; the fine structure is
  not, and the reel makes no claim about it.
- **Band levels, not perceptual difference.** The measurements show what
  survives, not how audible its absence is. That distinction is exactly why
  B05 concedes 320 kbps is transparent for almost everyone.

## Established results used as explanation, not measured here

| Claim | Status |
|---|---|
| Simultaneous masking: a loud tone raises the threshold near it | Standard psychoacoustics; the mechanism every perceptual codec is built on |
| Masking spreads further upward in frequency than downward | Standard asymmetry — drawn qualitatively in B02, no axis values claimed |
| High-bitrate MP3 is transparent for most listeners | Widely reported listening-test result; stated as "almost everyone", not universal |

These are presented as explanation. No invented figures are attached to any of
them, and the B02 masking curve deliberately carries no numeric axis so it
cannot be read as measured data.

## Toolkit

| Source | Used for |
|---|---|
| `RohanClaudeHAIbrutalist.art/runtime/remotion/src/tokens/claude.ts` | palette values for all eight new components |
| `RohanClaudeHAIbrutalist.art/runtime/scripts/shorts.py` | THE ONDA CHECK — portrait rewiring for the 9:16 cut |
| ffmpeg / libmp3lame | the experiment above, and every render |

## Not used

- No external web sources. The reel's numbers come from an experiment anyone
  can re-run with the four commands above.
- No screen recordings. Every visual is a deterministic Remotion render.
- No AI-generated video or audio beyond Kokoro narration.
