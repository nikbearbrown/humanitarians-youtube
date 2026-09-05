# SHOTLIST — "What MP3 Throws Away"

Seven beats, 139.77s. Every duration is the measured Kokoro narration length;
the visuals were cut to fit these.

| Beat | Act | In | Dur | Component | Lane | On screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.60s | `ClaudeComposerAsk` | chassis | Composer card; the question typed in; three output lines resolve |
| B01 | BLUF | 0:18 | 21.72s | `LossySpectrumCut` | **new** | White-noise spectrogram, evenly lit; at 42% the shelf above 16 kHz erases to bare page, terracotta cliff rule, measured drop appears in the void |
| B02 | MECHANISM | 0:40 | 22.44s | `LossyMaskingCurve` | **new** | Loud tone, quiet tone; masking skirt sweeps up out of the loud one; the quiet tone greys out and is stamped MASKED — 0 BITS SPENT |
| B03 | COMPARISON | 1:02 | 23.70s | `LossyBitrateCompare` | **new** | Three spectrum strips, each truncated at its measured cliff, with ratio and real byte count; the discarded remainder greyed |
| B04 | LIMIT | 1:26 | 21.12s | `LossyGenerationLoss` | **new** | Source reference line; four rungs descending, each deficit counting up; total block lands last |
| B05 | APPLY | 1:47 | 22.06s | `ClaudeWindow` | library | Artifact card — fine / not fine / keep the master / never edit the thinned file |
| B06 | OUTRO | 2:09 | 10.13s | `ClaudeTitleOutro` | chassis | Title, `@HumanitariansAI`, `Rohan Vijaykumar` |

## Visual rhythm

No two consecutive body beats share a shape. B01 is a dense field that loses
part of itself. B02 is a sparse two-object plot with a curve. B03 is a stacked
comparison. B04 is a descending stair. B05 is text. The opener and outro are the
shared chassis, unchanged across every reel on the channel.

## Motion budget

Each new scene has exactly one thing that *happens*:

| Beat | The event | When |
|---|---|---|
| B01 | The lowpass lands; the shelf is erased | `durationInFrames × 0.42` |
| B02 | The masking curve rises and swallows the quiet tone | `durationInFrames × 0.40` |
| B03 | Three strips land in sequence, each shorter than the last | staggered, settles ~frame 150 |
| B04 | Rungs descend one at a time, never recovering | staggered, settles ~frame 150 |

B01 and B02 key their event off `durationInFrames`, so re-recorded narration
cannot push the reveal past the end of the beat. B03 and B04 settle early and
hold.

## Why the noise texture is deterministic

`LossySpectrumCut` and `LossyBitrateCompare` generate their spectrogram cells
from a fixed hash of position, not a random number. Two consequences: the render
is reproducible frame to frame (no shimmer), and re-running the build produces
an identical picture, so a QC sheet can be compared across builds.

## 9:16 — a native portrait re-render, not a crop

Per THE ONDA CHECK (`shorts.py`), every beat is rewired to a `916` sibling
registered at 1080×1920 and re-rendered.

| Beat | Landscape | Portrait |
|---|---|---|
| B00 | `ClaudeComposerAsk` | `ClaudeComposerAsk916` (library) |
| B01 | `LossySpectrumCut` | `LossySpectrumCut916` **(new)** |
| B02 | `LossyMaskingCurve` | `LossyMaskingCurve916` **(new)** |
| B03 | `LossyBitrateCompare` | `LossyBitrateCompare916` **(new)** |
| B04 | `LossyGenerationLoss` | `LossyGenerationLoss916` **(new)** |
| B05 | `ClaudeWindow` | `ClaudeWindow916` (library) |
| B06 | `ClaudeTitleOutro` | `ClaudeTitleOutro916` (library) |

Each sibling re-exports the landscape schema, so props are identical.

### How each beat reflows

| Beat | Landscape | Portrait |
|---|---|---|
| B01 | wide, short spectrogram | **taller** plot — portrait gives height, which is the axis a spectrogram wants, so the erased shelf occupies a larger share of frame |
| B02 | curve label beside the plot, verdict stamp inline | plot squarer, tones fatter, verdict moves to a **card below the plot** where portrait has room |
| B03 | label / strip / stats in three columns | each encode becomes a **card**: label + ratio on top, full-width strip beneath, cliff + bytes on the footer |
| B04 | steps descend left to right | steps descend **straight down**, each indented further — gravity does the explaining |

### Portrait safe area

Content sits in the active band **y 230–1440, x 54–1026**; the top 12% and
bottom 25% of the 1080×1920 frame are reserved for platform UI. Font sizes
derive from `height`, not inherited from landscape.
