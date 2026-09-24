# 16-bit or 24-bit: What Bit Depth Does

A non-technical explainer on bit depth: what the 16-or-24 question in an export
box actually controls, and which one to pick. One of the two week-04 STEM reels;
the other is
[Why Your Track Sounds Thin On A Phone.](../2026-09-18-why-tracks-sound-thin-on-a-phone/)

| | |
|---|---|
| **Runtime** | 2:07 |
| **Format** | 16:9 and 9:16, 4K (3840×2160 / 2160×3840), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 7 · 4 purpose-built scenes · 3 chassis/library · **no slates** |
| **Presenter** | Rohan V. |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## Through-line

**Bit depth is room to work in, not quality.** Keep it while you edit, spend it
when you ship. The number in the export box does not make your recording sound
better — it sets how quiet a sound can get before the file's own hiss takes over,
and at 16 bits that floor is already below the room you are sitting in.

## Written for someone who has never opened an audio editor

The first plan for this reel opened straight into the export dialog, and Rohan
stopped the build:

> I checked out the bit depth video. It starts out very abruptly. what is a
> person who knows nothing about audio going to understand? I want you to give
> some background. Explain it as if the viewer is new to the topic completely.

The reel was rebuilt around that. It now spends its first two body beats before
the subject:

- **B01** — what sound is (movement), how a computer stores it (a list of
  numbers), and the fact that doing so answers *two* separate questions. Sample
  rate is named and then explicitly set aside, because every beginner conflates
  the two and a viewer who leaves thinking bit depth controls "how often" has
  learned something false.
- **B02** — a ruler. Not a waveform, not a decibel: an object from a drawer. Only
  once "more markings means more precision" is obvious does the ruler get laid on
  a sound wave.

The reel does not reach its own subject until 1:01 of 2:07. That is deliberate.

Then a second correction, after the first rewrite went too far the other way:

> Okay. and dont make the video too high level either. it has to be a good
> balance. at the end of the day the viewer has to learn somthing

So the mechanism is kept in full (B03: the leftover gap *is* a hiss, and a
coarser ruler makes it louder) and exactly **one** pair of hard numbers survives
(B04). Full vocabulary and sequencing decisions in [PEDAGOGY.md](./PEDAGOGY.md).

## Every number measured

The experiment ran **before** the script was written. Raw log:
[MEASUREMENTS.txt](./MEASUREMENTS.txt); script: `measure_bitdepth.py` (numpy
only — no ffmpeg, no network).

| depth | measured noise floor | step size | dynamic range |
|---|---|---|---|
| 8-bit | **−53.14 dBFS** | 7.812e-03 | 53.1 dB |
| 16-bit | **−100.75 dBFS** | 3.052e-05 | 100.8 dB |
| 24-bit | −149.56 dBFS | 1.192e-07 | 149.6 dB |

Two things this bought the reel:

1. **The pair of numbers in B04 is measured, not recalled.** −53 and −101, from a
   20-second 440 Hz sine at −6 dBFS peak, quantised by mid-tread rounding with no
   dither, error taken in float64 against the unquantised original.
2. **"About six decibels per bit" is confirmed, not assumed** — 5.95 dB/bit from
   8→16 and 6.10 dB/bit from 16→24. It did not make the final cut (too much
   detail for this audience) but it is why the 8-vs-16 comparison is honest.

The 24-bit row is real and is *not claimed on screen*: comparing three depths was
cut as more detail than the audience needs. See
[FACTCHECK.md](./FACTCHECK.md) for all 19 claims and their verdicts.

**ffmpeg cannot do this measurement.** Its filter graph is 32-bit float
internally, so a 24-bit round trip is lossless to it and it reports `-inf`. That
is a tool limit, not a property of the format; float64 numpy has the headroom.

## Word-clock choreography

Every reveal in this reel is timed to a **measured** spoken word, not a guessed
fraction of the beat:

```
narration mp3 → align.py (faster-whisper) → mp3/words.json
              → cues.json (hand-authored: cue name → anchor phrase)
              → sync_cues.py → beat_sheet.json props.cues
```

30 cues authored, 30 resolved, 0 unmatched. Per-beat table in
[SHOTLIST.md](./SHOTLIST.md).

## 9:16 is a different render, not a crop

Four portrait siblings were written for this reel — `BitSoundToNumbers916`,
`BitStaircase916`, `BitGapIsHiss916`, `BitRoomUnderneath916` — and `shorts.py`
rewires the short's own beat sheet to them (THE ONDA CHECK). Each one re-lays the
beat out for a tall frame rather than scaling the wide one down; what changed and
why is in [SHOTLIST.md](./SHOTLIST.md#916).

## Files

| | |
|---|---|
| `beat_sheet.json` | the build contract — 7 beats, durations, components, props, cues |
| `cues.json` | cue name → anchor phrase, hand-authored |
| `mp3/` | Kokoro narration per beat + `words.json` word timings |
| `media/`, `clips/` | rendered 4K beats and their normalised clips |
| `short/` | the portrait beat sheet and its own `media/` |
| `_qc/` | Gate V frames and report |
| `measure_bitdepth.py` | the measurement, rerunnable |
| `MEASUREMENTS.txt` | its raw output |
| `qc-sheet-16x9.png`, `qc-sheet-9x16.png` | contact sheets, both orientations |

The two 4K masters are **not** in git — they are in
[Google Drive](https://drive.google.com/drive/folders/1B5jcU0Cg2OAyYncwYzVYQklvRqUus5bA)
under `2026-09-18/`. Only the docs and the build contract are committed.

## Rebuilding

```bash
./art final path/to/2026-09-18-what-bit-depth-does
```

Everything is deterministic: no randomness at render time, so a rebuild produces
identical frames and the QC sheets stay comparable across builds.
