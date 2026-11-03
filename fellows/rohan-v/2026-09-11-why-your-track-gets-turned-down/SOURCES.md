# SOURCES — "Why Your Track Gets Turned Down"

## Primary source: an experiment run for this reel

Every number on screen was measured on this machine on 2026-09-10, **before**
the beat sheet was written. Raw log: [MEASUREMENTS.txt](./MEASUREMENTS.txt).

### Method

```bash
# 1. a source with real crest factor: a sustained chord bed, a decaying low hit
#    and a short high tick every beat, plus a quieter passage from 10s to 18s
ffmpeg -filter_complex "sine=f=110:d=30,volume=0.22[b]; ... \
  sine=f=180:d=30,volume='0.80*exp(-22*mod(t,1))':eval=frame[hit]; ... \
  amix=inputs=5:normalize=0,volume='if(between(t,10,18),0.25,1.0)':eval=frame" src.wav

# 2. version A — gain only, brought up until the loudest moment nears the ceiling
ffmpeg -i src.wav -af "volume=18.0dB,alimiter=limit=0.891" A_dynamic.wav

# 3. version B — compressed hard, then driven into a limiter
ffmpeg -i src.wav -af "volume=12.5dB,\
  acompressor=threshold=0.02:ratio=20:attack=0.3:release=50:makeup=18,\
  volume=5dB,alimiter=limit=0.82" B_loud.wav

# 4. measure
ffmpeg -i <file> -filter_complex ebur128=peak=true -f null -
```

**Why a synthetic signal.** A real song's crest factor and quiet passages are
unknown quantities; here both are known exactly, so the difference between the
two versions is attributable entirely to the processing. The mechanism
generalises; the specific numbers belong to this file, and the reel says so on
screen.

**Why both versions come from one source.** Otherwise the comparison would be
between two different pieces of music rather than between two treatments.

### Results used on screen

| Where | Figure | Measured |
|---|---|---|
| B01 tallest-point readouts | −1.0 / −0.2 dBFS | true peak, both versions |
| B01 loudness readouts | −15.3 / −6.6 LUFS | integrated loudness |
| B03 gains | +1.3 dB / −7.4 dB | arithmetic to a −14 target from the measured values |
| B03 markers | both arrive −14.0 | confirmed by rendering B at −7.4 dB and re-measuring |
| B04 spans | 12.0 / 0.7 LU | EBU R128 loudness range |
| B04 proof row "loudness" | −6.6→−14.0 · −15.3→−22.7 | measured after an identical −7.4 dB on both |
| B04 proof row "the gap" | 0.7→0.7 · 12.0→12.0 | measured after the same gain — unchanged |

### The claim this method is strongest on

Row four of the log. Applying **the same** gain to both files moves both
loudness figures and leaves both LRA figures bit-identical. That is a direct
demonstration that a volume change cannot restore range, rather than an appeal
to how compressors work.

### Stated limits

- **Synthetic, not commercial.** Said on screen in B01's footnote.
- **−14 LUFS is a stand-in, not a spec.** It is the most commonly published
  streaming figure. Platforms differ, change their targets, and some apply a
  limiter when raising quiet tracks. B03's footnote says targets differ; the
  narration says "around minus fourteen".
- **LRA is not crest factor.** The reel calls it "the gap between the quietest
  and loudest moments", which is what LRA describes, and never equates it with
  peak-to-average ratio.
- **Turning tracks *up* is simplified.** The reel shows +1.3 dB on the quiet
  version. Real platforms cap or limit upward gain rather than clipping. The
  reel's argument only depends on the downward case, which is universal.

## Established results used as explanation, not measured here

| Claim | Status |
|---|---|
| Loudness perception is better modelled by a time-averaged, frequency-weighted measure than by peak | The basis of EBU R128; presented in plain language, no numbers attached |
| Platforms normalise playback loudness to a target | Standard behaviour; the reel claims the behaviour, hedges the number |
| Leaving ~1 dB under the ceiling is sound practice on export | Standard practice, and what version A does |

## Toolkit

| Source | Used for |
|---|---|
| `ffmpeg` + `ebur128` filter | the whole experiment |
| `runtime/remotion/src/tokens/claude.ts` | palette for all five new components |
| `runtime/scripts/shorts.py` | THE ONDA CHECK — portrait rewiring |
| `runtime/qc/final_frame_check.py` | Gate V — caught the B04 contrast and B05 underfill defects |
| `docs/OUTRO-LOCK.md` | why the outro is `HaiTitleOutro`, not `ClaudeTitleOutro` |

## Not used

- No external web sources. Every figure came from a command run locally.
- No commercial recordings, and no audio from any platform.
- No screen recordings; every plot is drawn in code.
- No AI-generated audio beyond Kokoro narration.
