# A Blank Page and 49 AI Figures

A session replay. One git clone, a viewer that opened to a blank white page, and — once
it rendered — an audit of every molecule and drug figure in the Medhavy bio-art library.
The crash was one property read. The bigger finding was that 31 of 49 figures are one of
five recycled templates.

| | |
|---|---|
| **Runtime** | 3:05 (184.79 s) |
| **Format** | 30 fps · 16:9 |
| **Voice** | Kokoro `am_onyx` — before the series voice was chosen (see the fellow README) |
| **Beats** | 10 (B00–B09) · CLI-explainer spine, direct compile |
| **Register** | Teardown |
| **Presenter** | Rithwik B. |
| **Repository** | [Medhavy/bio-art](https://github.com/Medhavy/bio-art) |
| **Built** | 2026-09-21 · project work Weeks 3–8 (see [HOURS.md](../HOURS.md)) |
| **Status** | Built (10/10 beats) · fact-checked · **one claim needs a re-cut** · **not published** |
| **Renders** | beat clips local in `bio-art/video/bio-art-session/clips/`; master goes to the shared Drive after the re-cut |

## Through-line

The loader assumed every catalog entry looked like the first one; the figure generator
assumed every prompt could be drawn with five shapes.

## Beats

| Beat | Act | Opens with | Measured |
|---|---|---|---:|
| B00 | INTRO | Hola, this is Liam, in for Bear | 6.40 s |
| B01 | PROBLEM — why care | GitHub killed password auth years ago, so the clone bounced off a… | 27.71 s |
| B02 | ASK | Into Claude: the viewer's index point html is a Vite React app, it… | 11.24 s |
| B03 | CODE | The crash was one property read | 18.69 s |
| B04 | OUTPUT — run | Here's the blast radius | 17.28 s |
| B05 | CHANGE — check & revise | The fix: normalize both shapes into one, and while we're in the dev… | 16.62 s |
| B06 | OUTPUT — revised | The viewer came back | 32.00 s |
| B07 | SUMMARY | Zero of the two-hundred-forty-five figures in this repo attempt an… | 31.94 s |
| B08 | NEXT STEPS | Your move: point Claude at your own repo's asset pipeline and ask it… | 14.61 s |
| B09 | OUTRO | From a failed clone to a blank page to a five-template duplication… | 8.30 s |

## Fact-check — seven claims, five pass, two partial

See [`FACTCHECK.md`](FACTCHECK.md). Re-checked 2026-11-02 against `index.json`, the
annotations and the figure PNGs themselves. **B06 overstates:** the figures are visually
near-identical, not pixel-identical, and a fresh clustering does not reproduce the 16 / 15
group sizes. The 63% headline stands as the audit's judgment; the "pixel-identical" word
does not.

## What is in this folder

```
beat_sheet.json                every beat: narration, shot, measured duration
timings.json                   the measured clock, per beat
README.md                      this file
FACTCHECK.md                   every claim, its source, its verdict
SOURCES.md                     provenance and toolchain
audit-molecule-drug-figures.md the 49-figure audit the reel reports
viewer-fix.diff                the catalog.js + vite.config.js fix shown in B03–B05
qc-B04-fixed.png               frame check of the fixed B04
FRICTIONAL.md                  the process log for this piece of work
description.txt                YouTube description + validated chapters
.gitignore                     renders out, build inputs in
```

## Open before publication

1. **Re-cut B06** — say "near-identical", and recount the template groups with the
   perceptual check in `FACTCHECK.md`.
2. **B01 says "four separate bugs" and names three** after the clone. Name the fourth or
   say three.
3. Re-voice to `af_bella` if it publishes as part of the series.
4. Commit `viewer-fix.diff` to Medhavy/bio-art — the fix is still uncommitted in the clone.
