# SHOTLIST — "Why Your Track Gets Turned Down"

Seven beats, 121.54s. Every duration is the measured Kokoro narration length;
the visuals were cut to fit these.

| Beat | Act | In | Dur | Component | Lane | On screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 17.71s | `ClaudeComposerAsk` | chassis | Composer card; the question typed in; three output lines resolve |
| B01 | BLUF | 0:17 | 20.22s | `LoudPeakVsLoudness` | **new** | Two waveform rows — one dynamic, one filled solid — sharing one dashed ceiling; paired readouts show −1.0/−0.2 against −15.3/−6.6 |
| B02 | MECHANISM | 0:37 | 18.99s | `LoudLufsWindow` | **new** | One waveform read twice: a marker locks onto the single tallest bar, then a window sweeps the whole track accumulating an average |
| B03 | THE CATCH | 0:56 | 18.35s | `LoudNormalizeGain` | **new** | Vertical loudness axis with a target line; both markers slide onto it, gains shown as they travel |
| B04 | THE COST | 1:15 | 18.03s | `LoudRangeLost` | **new** | Two vertical spans, 12.0 collapsing to 0.7, plus a MOVED / DID NOT BUDGE proof table |
| B05 | APPLY | 1:33 | 16.83s | `ClaudeWindow` | library | Artifact card — four things to do on export |
| B06 | OUTRO | 1:50 | 11.41s | `HaiTitleOutro` | library | Title, `@HumanitariansAI`, `Rohan Vijaykumar` |

## Visual rhythm

No two consecutive body beats share a shape. B01 is two stacked waveforms. B02
is one waveform with two readings moving across it. B03 is a vertical axis with
travelling markers. B04 is two vertical spans plus a table. B05 is text.

## Motion budget

Each new scene has exactly one thing that *happens*:

| Beat | The event | When |
|---|---|---|
| B01 | The shared ceiling rule draws across both waveforms | frame 62 |
| B02 | The peak marker locks, then the averaging window sweeps | frame 46, then `durationInFrames × 0.40` |
| B03 | Both markers slide onto the target and finish level | `durationInFrames × 0.44` |
| B04 | The second span lands at a fraction of the first; the proof rows follow | frames 52 and 104+ |

B02 and B03 key their events off `durationInFrames`, so a re-recorded
narration cannot push the reveal past the end of the beat.

## The one frame that carries the reel

B03's last second: two markers, level with each other, one of which travelled
7.4 dB down to get there. If a viewer only sees one frame, that is the one that
should land.

## Why B06 is `HaiTitleOutro`, not `ClaudeTitleOutro`

`OUTRO-LOCK.md` scopes `ClaudeTitleOutro` to claude-liam / @NikBearBrown reels
only; it now hardcodes that handle and drops the subline entirely. Visual QC
caught it rendering `@NikBearBrown` with a bear mascot on the first pass. See
[BUILD-LOG.md](./BUILD-LOG.md).

## 9:16 — a native portrait re-render, not a crop

Per THE ONDA CHECK (`shorts.py`), every beat is rewired to a `916` sibling
registered at 1080×1920 and re-rendered. Each sibling re-exports the landscape
schema, so props are identical.

| Beat | Landscape | Portrait |
|---|---|---|
| B00 | `ClaudeComposerAsk` | `ClaudeComposerAsk916` (library) |
| B01 | `LoudPeakVsLoudness` | `LoudPeakVsLoudness916` **(new)** |
| B02 | `LoudLufsWindow` | `LoudLufsWindow916` **(new)** |
| B03 | `LoudNormalizeGain` | `LoudNormalizeGain916` **(new)** |
| B04 | `LoudRangeLost` | `LoudRangeLost916` **(new)** |
| B05 | `ClaudeWindow` | `ClaudeWindow916` (library) |
| B06 | `HaiTitleOutro` | `HaiTitleOutro916` **(new)** |

`HaiTitleOutro916` did not exist and had to be authored — without it the only
916 outro available was the @NikBearBrown-locked one, so the vertical would
have shipped the wrong channel's attribution.

### How each beat reflows

| Beat | Landscape | Portrait |
|---|---|---|
| B01 | readouts in a right-hand column beside each waveform | each version becomes a **block**: label, full-width waveform, then the two readouts side by side beneath. The shared ceiling still crosses both |
| B02 | the two reading cards sit side by side | cards **stack**, which lets each explanatory line sit on one line instead of wrapping |
| B03 | vertical axis, markers side by side | **portrait is the better frame** — the axis is already vertical, so the plot gets taller and the 7.4 dB drop is longer |
| B04 | spans side by side, proof detail inline | spans stay vertical and taller; each proof row puts its detail on a **second line** so nothing truncates |

### Portrait safe area

Content sits in the active band **y 230–1440** of 1080×1920; the top 12% and
bottom 25% are reserved for platform UI. Font sizes derive from `height`.
`HaiTitleOutro916` centres its card **within that band**, not the full frame —
a frame-centred outro would put the handle behind the platform's own UI.
