# SOURCES — "Why Your Track Sounds Thin On A Phone"

Where every number came from, and what the method cannot tell you.

## Primary: two experiments run for this reel

`build_mono_signals.py`, in this folder. numpy builds the signals, ffmpeg
measures them. No network, no account, no paid API. Rerunnable — the exact
commands are at the bottom of [MEASUREMENTS.txt](./MEASUREMENTS.txt).

```bash
python3 build_mono_signals.py      # writes stereo / mono / left / wide_* wavs
```

### Case 1 — a fully opposite layer (B03)

**Signal.** A 20 s stereo track built with three parts:

| part | frequency | placement |
|---|---|---|
| bass | 110 Hz | identical on both sides (centred) |
| vocal | 440 Hz | identical on both sides (centred) |
| air | 3000 Hz | **inverted on the right** (spread) |

**Method.** For each part, band-pass a 60 Hz-wide window around its frequency
and take `volumedetect`'s mean volume — first on one side alone, then on the same
track summed to a single speaker.

**Results.**

| band | one side | mono sum | change |
|---|---|---|---|
| 110 Hz bass (centred) | −13.4 | −13.4 | **+0.0 dB** |
| 440 Hz vocal (centred) | −16.2 | −16.2 | **+0.0 dB** |
| 3000 Hz air (wide) | −17.0 | −66.5 | **−49.5 dB** |

### Case 2 — a delay-based widener (B04)

**Signal.** Broadband noise, right side delayed by 0.6 ms (28 samples at
48 kHz) — how most stereo wideners work.

**Predicted first.** Summing a signal with a delayed copy cancels at odd
multiples of 1/(2d). For d = 0.6 ms: nulls at **833 Hz, 2500 Hz, 4167 Hz…**,
peaks halfway between at **1667 Hz** and **3333 Hz**.

**Then measured** (120 Hz-wide bands):

| band | one side | mono sum | change | predicted |
|---|---|---|---|---|
| 400 Hz | −39.5 | −42.6 | −3.1 dB | slope |
| 830 Hz | −39.6 | −49.8 | **−10.2 dB** | NULL |
| 1660 Hz | −39.6 | −40.0 | −0.4 dB | peak |
| 2500 Hz | −39.6 | −49.4 | **−9.8 dB** | NULL |
| 3300 Hz | −39.7 | −40.3 | −0.6 dB | peak |

All four predicted positions landed. The prediction was written down before the
measurement was run, which is the only version of this that is worth anything.

### Why the nulls are ~−10 dB and not −∞

1. The analysis band-pass is **120 Hz wide**, so it collects energy from
   neighbouring frequencies that are not cancelling.
2. The delayed layer is **broadband noise, not a pure tone**, so only the
   component exactly at the null frequency cancels completely.

Neither is an error. A narrower filter and a pure tone would drive these toward
−∞, and the wide-band figure is the honest one for a real mix. This is precisely
why the reel says **holes**, not **silence**.

### What these methods do not tell you

- **Nothing about a real mix.** Both signals were *built* for the measurement so
  their placement is known exactly rather than guessed. The mechanism
  generalises; the specific figures belong to these files. B03's on-screen
  footnote says the track was built for this.
- **Nothing about perceived loudness.** These are band-limited mean volumes, not
  loudness measurements. A −49.5 dB band drop is not "the track got 49.5 dB
  quieter".
- **Nothing about a specific phone or speaker.** It measures the arithmetic of
  channel summing, not any device's implementation. A two-driver phone in
  landscape will behave differently from a single-driver one.
- **Nothing about which wideners do this.** Case 2 models the common delay-based
  design. Other designs (all-pass, mid/side gain, true multi-mic capture) fail
  differently or not at all.

### A measurement footgun

The first pass of Case 2 returned nothing at all. `volumedetect` prints its
results at ffmpeg's **info** level, so passing `-v error` suppresses the very
numbers being measured. MEASUREMENTS.txt carries a note about it, because it
will happen again to someone.

## Secondary: established results, used as stated

Not measured here. Standard, and stated in plain language with no invented
figures attached.

| Used for | What is relied on |
|---|---|
| B01 — "that difference is what makes music feel wide" | interaural level and time differences are the primary cues for perceived width and source position |
| B01 — "one speaker has to add them together first" | single-driver playback sums the channels before the driver moves |
| B02 — the door, and "where they agree you get sound" | linear superposition |
| B04 — "most stereo width comes from delaying one side" | the common widener designs are delay-based or all-pass. Hedged as *most*, not *all* |
| B05 — the three usual culprits | wideners, doubled parts and wide reverb on a centred element all introduce inter-channel difference on material that should be centred |

## Toolchain

| Tool | Version / note | Cost |
|---|---|---|
| Kokoro TTS (`af_bella`) | local, `generate_audio_kokoro.py` | **$0.00** |
| faster-whisper (`align.py`) | local word-level alignment | **$0.00** |
| Remotion | 4.0.486 (core, `@remotion/*` pinned to match) | free |
| numpy | signal construction | free |
| ffmpeg / ffprobe | band-pass + `volumedetect`, compile, QC frames | free |
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
