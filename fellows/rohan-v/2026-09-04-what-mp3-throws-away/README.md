# What MP3 Throws Away

A non-technical explainer on lossy audio compression: what an encoder actually
removes, why it is allowed to, and when that removal stops being acceptable.
The STEM half of the week-02 submission; the progress half is
[Unblocking the Team.](../2026-09-04-unblocking-the-team/)

| | |
|---|---|
| **Runtime** | 2:19 |
| **Format** | 16:9 and 9:16, 4K (3840×2160 / 2160×3840), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 7 · 4 purpose-built scenes · 3 chassis components · **no slates** |
| **Presenter** | Rohan Vijaykumar |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## Through-line

**An MP3 is not a smaller copy. It is an edited one.** The encoder models your
ear, finds the parts you cannot hear, and deletes them permanently. That makes
this a sibling to the stem-separation reel: both are about information that is
*gone*, not hidden.

## Every number on screen was measured, not recalled

Before the beat sheet was written, white noise was encoded at 128 and 320 kbps
with ffmpeg + libmp3lame, decoded back, and measured band by band. The script
then described the result. Raw log: [MEASUREMENTS.txt](./MEASUREMENTS.txt);
method and limits: [SOURCES.md](./SOURCES.md).

| Measured | Result |
|---|---|
| 128 kbps cliff | 16 kHz intact (−0.6 dB), **17 kHz down 13.2 dB** |
| 320 kbps cliff | identical to source through 19 kHz; 20 kHz down 3.5 dB |
| Compression | 128 kbps **10.96 : 1** · 320 kbps 4.38 : 1 |
| Generation loss | 12 kHz band: −31.1 dB (1 encode) → **−37.8 dB (11 encodes)** |

The exact cliff frequency belongs to this encoder at these settings, and the
reel says so on screen rather than implying 16 kHz is universal.

## Beat map

| Beat | Act | Dur | Component | What it shows |
|---|---|---|---|---|
| B00 | ASK | 18.60s | `ClaudeComposerAsk` | "Hi, I'm Rohan, for Humanitarians AI" — not compressed, edited |
| B01 | BLUF | 21.72s | `LossySpectrumCut` | White-noise spectrogram; everything above 16 kHz erased mid-beat |
| B02 | MECHANISM | 22.44s | `LossyMaskingCurve` | Masking threshold rises; the quiet tone is swallowed, 0 bits spent |
| B03 | COMPARISON | 23.70s | `LossyBitrateCompare` | 128 / 320 / lossless — each strip cut at its own measured cliff |
| B04 | LIMIT | 21.12s | `LossyGenerationLoss` | Re-encode steps descending, none recovering |
| B05 | APPLY | 22.06s | `ClaudeWindow` | When lossy is fine, when it is malpractice |
| B06 | OUTRO | 10.13s | `ClaudeTitleOutro` | "I'm Rohan Vijaykumar, for Humanitarians AI" |

Total 139.77s. Narration durations are ground truth; every visual is cut to fit
the voice.

## New Remotion components

Four landscape, plus a native portrait sibling for each, registered under
`lossy-audio-explainer`. All four were confirmed genuine library misses with
`./art scenes` before authoring.

| Component | What it does |
|---|---|
| `LossySpectrumCut` | Deterministic white-noise spectrogram; the shelf above the cut frequency is erased, not dimmed |
| `LossyMaskingCurve` | Two tones and a masking skirt; the quiet one greys out as the curve rises over it |
| `LossyBitrateCompare` | Three spectrum strips truncated at their measured cutoffs, with real ratios and byte counts |
| `LossyGenerationLoss` | Descending steps from a source reference line, deficits counting up |

Portrait siblings: `LossySpectrumCut916` · `LossyMaskingCurve916` ·
`LossyBitrateCompare916` · `LossyGenerationLoss916`

## The vertical cut is re-rendered, not cropped

Built through `shorts.py` and THE ONDA CHECK, which rewires each beat to its
`916` sibling. Portrait is the better frame for a spectrogram — the plot gets
taller, so the erased shelf reads as a larger share of the screen than it does
in landscape. See [SHOTLIST.md](./SHOTLIST.md) for each beat's reflow.

## What is in this folder

**Committed to GitHub** — text only, nothing over 25 MB:

```
beat_sheet.json     the reel: beats, narration, visuals, measured durations
MEASUREMENTS.txt    the raw experiment log every on-screen number comes from
README.md           this file
SOURCE-brief.md     what was asked for, and what it was built from
PROMPT.md           the brief and how each constraint was resolved
FEEDBACK.md         reviewer notes — empty until someone reviews it
BUILD-LOG.md        what actually happened
FACTCHECK.md        all 17 claims, 13 of them measured here
SOURCES.md          the experiment's method, results and stated limits
PEDAGOGY.md         narration sign-off — register, vocabulary, what was cut
SHOTLIST.md         beat-by-beat, and how each one reflows for portrait
PROMPTS.md          the design brief behind each visual
description.txt     YouTube description + chapter markers
qc-sheet-16x9.png   contact sheet — landscape visual QC record
qc-sheet-9x16.png   contact sheet — portrait visual QC record
.gitignore          enforces the media rule below
```

**Never committed** — these go to Google Drive:

```
mp4/     finished cuts        media/   per-beat 4K renders
mp3/     narration per beat   clips/   compile intermediates
short/   derived portrait reel
```

## Rebuilding it

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160

python3 runtime/scripts/shorts.py <reel> --no-endcard
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>/short
python3 runtime/scripts/compile.py <reel>/short --height 3840

./art drive <reel>          # docs to GitHub, videos to Drive
```

Audio first, always. The vertical is re-rendered, never cropped.
