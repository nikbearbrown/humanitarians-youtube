# BUILD-LOG — "Why Your Track Gets Turned Down"

Built 2026-09-10 as the STEM half of the week-03 submission.

## 1 — Topic selection

Two audio topics were offered: loudness normalisation, and why AI music sounds
"off". Rohan picked loudness, with one condition:

> keep in mind that a lot of people are not audio professionals. so they might
> not understand what a master or a squeezed mix is so keep that in mind

Loudness was the recommended one for a specific reason: **ffmpeg ships an EBU
R128 scanner**, so every claim could be produced by experiment rather than
recalled. The AI-artifacts topic would have rested mostly on established
results with no way to measure locally.

## 2 — The experiment, before the script

### First attempt failed, and the failure was instructive

Built a 30s signal from sustained tones, then a "squeezed" version via
compressor + limiter. Measured:

```
A_dynamic.wav   -7.9 LUFS   LRA 15.9   peak -1.0
B_loud.wav     -11.4 LUFS   LRA  0.9   peak -0.6
```

**The squeezed version measured 3.5 LU quieter** — the opposite of the point.
Cause: a steady tremolo tone has almost no crest factor, so there are no peaks
for a limiter to trade away. Compression buys loudness only when there is
transient headroom to exploit.

Rebuilt the source with decaying hits and a high tick on every beat:

```
src.wav   -37.6 LUFS   LRA 13.1   peak -18.5    → 19.1 dB crest factor
```

Then the comparison behaved like music does:

| file | LUFS | LRA | true peak |
|---|---|---|---|
| A — left alone | **−15.3** | **12.0** | −1.0 |
| B — squeezed louder | **−6.6** | **0.7** | −0.2 |
| B at the −14 target | −14.0 | 0.7 | −7.6 |
| A, same −7.4 dB applied | −22.7 | **12.0** | −8.4 |

Full log: [MEASUREMENTS.txt](./MEASUREMENTS.txt).

### The result worth the whole reel

Row four. Applying **the same** gain to both files moves both loudness figures
and leaves both LRA figures **identical**. That is a direct demonstration that
a volume change cannot restore range — not an appeal to how compressors work.
It became B04's proof table verbatim.

## 3 — Library-first gate

Four searches, four genuine misses — closest candidates were a Suno song-card
panel, a tax-season spike, a cost/latency bar chart and a career-verb bar
chart, all scoring 5.5–7.5. Recorded in PROMPTS.md.

## 4 — Components authored

Four landscape + four portrait siblings under
`loudness-normalization-explainer`:

`LoudPeakVsLoudness` · `LoudLufsWindow` · `LoudNormalizeGain` ·
`LoudRangeLost`, each with a `916` sibling re-exporting the landscape schema.

**Every label was written for a non-professional.** No "master", "mix",
"dynamics", "compression", "limiter" or "headroom" anywhere in the components.
"Peak" became `TALLEST SINGLE MOMENT`; LUFS became `HOW LOUD IT ACTUALLY
SOUNDS`; LRA became `GAP BETWEEN THE QUIETEST AND LOUDEST MOMENTS`.

## 5 — Audio, and a length trim

First pass: 145.95s = 2:26, well over the 2:00 brief. Trimmed beat by beat
rather than dropping an act — the loudness-war history had already been cut in
drafting to make room for B04.

```
B00 17.71   B01 20.22   B02 18.99   B03 18.35
B04 18.03   B05 16.83   B06 11.41
```

Total **121.54s = 2:02**. Cost $0.00.

## 6 — The factcheck caught two narration errors

Running FACTCHECK as a real gate rather than a write-up found two problems:

| Draft | Problem | Corrected to |
|---|---|---|
| "half a decibel apart" | measured difference is 0.8 dB | "under a decibel apart" |
| "sounds nearly nine times louder" | **8.7 LU is a difference on a logarithmic scale, not a ratio** — this overstates the perceptual effect by a wide margin | "sits nearly nine points higher on the loudness scale" |

The second is a real error, not a rounding. B01's audio was regenerated.
Recorded as FACTCHECK notes 1 and 2.

**And a duration bug from that fix.** Regenerating B01 stamped 20.22s, but a
later script that rewrote the beat sheet clobbered it back to the stale 19.37s,
so B01 rendered 0.85s short of its own audio. Caught by probing the mp3 against
the sheet; all durations were then re-stamped from the actual files and B01
re-rendered.

## 7 — Gate V blocked the final twice, both times correctly

| Finding | Fix |
|---|---|
| **B04 `low-contrast`** — ink/background separation 0.25 against a 0.30 floor. The measurement spans were drawn at 0.16 opacity, too faint on cream | span fill to 0.38, caps 4px → 7px |
| **B05 `underfill`** — the library's `ClaudeWindow` artifact card fills **21% of the safe area against a 55% floor** | built `HaiApplyCard` + `HaiApplyCard916` |

The underfill is a library-wide finding, not a mistake in this reel:
`ClaudeWindow` in artifact view is simply too sparse to pass a final. It is the
same class of problem `HaiTitleOutro`'s header records about the old HAI end
card — sparse cards being waved through as "the known exemption" when no
exemption existed. `HaiApplyCard` carries the same numbered-instruction content
as full-width rows that actually occupy the frame.

### One false alarm, worth recording

An early manual gate run reported **14 BLOCKER `edge-bleed`** on every beat,
including untouched library components. Cause: I ran it against the
`-slate.mp4` review cut, whose burn-in timecode legitimately crosses
title-safe. **Run Gate V against the clean candidate, never the slate.**

After both fixes: **0 BLOCKER, 0 MAJOR — clean.**

## 8 — The outro was the wrong channel's

Same defect as the sibling reel: `ClaudeTitleOutro` is locked to
@NikBearBrown per `OUTRO-LOCK.md` and silently ignores `handle` and `subline`.
Switched B06 to `HaiTitleOutro`, and authored the missing `HaiTitleOutro916`
so the vertical had a correct portrait outro to rewire to. Details in the
sibling reel's BUILD-LOG.

## 9 — Portrait

`shorts.py --no-endcard` rewired all seven beats to `916` siblings on the first
run. B03 is genuinely better in portrait: the loudness axis is already
vertical, so the plot gets taller and the 7.4 dB drop onto the target reads
longer.

## Outputs

```
2026-09-11_why_your_track_gets_turned_down_16x9.mp4   3840×2160   121.5s
2026-09-11_why_your_track_gets_turned_down_9x16.mp4   2160×3840   121.5s
```

## Toolkit changes made in this build

| File | Change |
|---|---|
| `runtime/remotion/src/scenes/HaiApplyCard.tsx` + `916` | **new** — filled HAI apply card; `ClaudeWindow` fails Gate V underfill at 21% |
| `runtime/remotion/src/scenes/HaiTitleOutro916.tsx` | **new** — HAI portrait end card |
| `runtime/remotion/src/scenes/Loud*.tsx` + `916` | **new** — 8 components |
| `runtime/scripts/compile.py` | UTF-8 change-guard read; channel-scoped OUTRO LAW lint |
| `runtime/remotion/src/Root.tsx` | registrations |

## What this build says about the gates

Three separate checks each caught something the others could not:

- **the factcheck** caught a false claim in the narration
- **Gate V** caught two visual defects invisible to any probe
- **looking at a frame** caught the wrong channel's logo on the end card

None of the three is redundant, and a duration-and-dimensions check would have
passed all four defects.
