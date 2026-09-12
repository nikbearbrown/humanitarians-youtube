# Why Your Track Gets Turned Down

A non-technical explainer on loudness normalisation: why making a track louder
buys nothing, and what it permanently costs. The STEM half of the week-03
submission; the progress half is
[Use the Tool First.](../2026-09-11-use-the-tool-first/)

| | |
|---|---|
| **Runtime** | 2:01 |
| **Format** | 16:9 and 9:16, 4K (3840×2160 / 2160×3840), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 7 · 4 purpose-built scenes · 3 chassis/library · **no slates** |
| **Presenter** | Rohan Vijaykumar |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## Through-line

**Loudness is borrowed. The gap is spent.** The platform turns every track to
the same playback level, so the loudness you fought for is removed before
anyone hears it — but the space you crushed between your quiet and loud parts
does not come back.

Sibling to the week-02 MP3 reel: that one was what happens *inside* your file,
this is what happens *after you upload it*.

## Written for people who have never opened a DAW

Explicit instruction from Rohan when picking the topic:

> keep in mind that a lot of people are not audio professionals. so they might
> not understand what a master or a squeezed mix is so keep that in mind

So the script never uses **master**, **mix**, **dynamics**, **limiter**,
**compression** or **headroom**. The two things being measured are called *the
tallest point* and *how loud it actually sounds*. The thing you lose is called
*the gap*. LUFS appears once, in an on-screen footnote that says you do not
need the acronym. Full vocabulary table in [PEDAGOGY.md](./PEDAGOGY.md).

## Every number measured

The experiment ran **before** the script was written. Raw log:
[MEASUREMENTS.txt](./MEASUREMENTS.txt).

| file | LUFS | gap (LRA) | tallest point |
|---|---|---|---|
| left alone | −15.3 | **12.0** | −1.0 |
| squeezed louder | −6.6 | **0.7** | −0.2 |
| squeezed, at the −14 target | −14.0 | 0.7 | −7.6 |
| left alone, same gain applied | −22.7 | **12.0** | −8.4 |

Three results carry the reel:

1. **A peak meter cannot see loudness.** The two files' tallest points are
   0.8 dB apart; their loudness is 8.7 LU apart.
2. **Squeezing costs 94% of the gap** — 12.0 LU down to 0.7 LU.
3. **Gain moves loudness but never restores the gap.** The last row is the
   proof: same −7.4 dB applied, loudness moved, LRA did not budge.

## Beat map

| Beat | Act | In | Dur | Component | What it shows |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 17.71s | `ClaudeComposerAsk` | "Hi, I'm Rohan, for Humanitarians AI" — you turned it up, they turned it down |
| B01 | BLUF | 0:17 | 19.37s | `LoudPeakVsLoudness` | Two waveforms at the same ceiling, wildly different loudness readouts |
| B02 | MECHANISM | 0:37 | 18.99s | `LoudLufsWindow` | One waveform read two ways: a marker on one instant, a window over everything |
| B03 | THE CATCH | 0:56 | 18.35s | `LoudNormalizeGain` | Both tracks slide onto the same playback target |
| B04 | THE COST | 1:14 | 18.03s | `LoudRangeLost` | The gap collapses 12.0 → 0.7, and a proof table shows gain cannot undo it |
| B05 | APPLY | 1:32 | 16.83s | `ClaudeWindow` | What to do on export |
| B06 | OUTRO | 1:49 | 11.41s | `ClaudeTitleOutro` | "I'm Rohan Vijaykumar, for Humanitarians AI" |

Total 120.69s. Narration durations are ground truth.

## New components

Four landscape, each with a native portrait sibling, registered under
`loudness-normalization-explainer`. All four were genuine library misses,
confirmed with `./art scenes` before authoring.

| Component | What it does |
|---|---|
| `LoudPeakVsLoudness` | Two waveform rows sharing one dashed ceiling, with paired readouts |
| `LoudLufsWindow` | A peak marker that locks on one bar, then an averaging window that sweeps the whole track |
| `LoudNormalizeGain` | A vertical loudness axis with a target line both markers slide onto |
| `LoudRangeLost` | Two vertical spans, the second collapsed, plus a moved/did-not-budge proof table |

Portrait siblings: `LoudPeakVsLoudness916` · `LoudLufsWindow916` ·
`LoudNormalizeGain916` · `LoudRangeLost916`

## The vertical cut is re-rendered, not cropped

Built through `shorts.py` and THE ONDA CHECK. B03 is genuinely better in
portrait — the loudness axis is vertical, so the drop from the loud track down
to the target is longer and the two markers finishing level is unmissable. See
[SHOTLIST.md](./SHOTLIST.md).

## What is in this folder

**Committed to GitHub** — text and QC sheets only:

```
beat_sheet.json     the reel: beats, narration, visuals, measured durations
MEASUREMENTS.txt    the raw experiment log every on-screen number comes from
README.md           this file
SOURCE-brief.md     what was asked for, and what it was built from
PROMPT.md           the brief and how each constraint was resolved
FEEDBACK.md         reviewer notes — empty until someone reviews it
BUILD-LOG.md        what actually happened
FACTCHECK.md        every claim, its source, its verdict
SOURCES.md          the experiment's method, results and stated limits
PEDAGOGY.md         narration sign-off — register, vocabulary, what was cut
SHOTLIST.md         beat-by-beat, and how each one reflows for portrait
PROMPTS.md          the design brief behind each visual
description.txt     YouTube description + chapter markers
qc-sheet-16x9.png   contact sheet — landscape visual QC record
qc-sheet-9x16.png   contact sheet — portrait visual QC record
.gitignore          enforces the media rule below
```

**Never committed** — these go to Google Drive via `./art drive`:

```
mp4/  finished cuts     media/  per-beat 4K renders
mp3/  narration         clips/  compile intermediates
short/  derived portrait reel
```

## Rebuilding it

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160

python3 runtime/scripts/shorts.py <reel> --no-endcard
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>/short
python3 runtime/scripts/compile.py <reel>/short --height 3840

./art drive <reel>
```

Audio first, always. The vertical is re-rendered, never cropped.
