# SOURCES — Look at the Frames

**Film:** `hai-look-at-the-frames` · ai-explainer · `claude-hai` (`@HumanitariansAI`) · `af_bella`
**Built:** 2026-10-29, locally with the brutalist.art toolkit

## Primary sources

| # | Source | Used for |
|---|---|---|
| S1 | The fellow's framing of the topic — AI Fluency as the skill, Brutalist as the receipt | the series' argument |
| S2 | [`SERIES-PLAN.md`](../2026-10-29-fluent-isnt-finished/SERIES-PLAN.md) | audience, outcome, spine |
| S3 | [`SERIES-BUILD-LOG.md`](../2026-10-30-show-what-broke/SERIES-BUILD-LOG.md) | every failure, count and fix named on camera |
| S4 | brutalist.art `HOW-TO.md`, `CLAUDE.md`, ai-explainer skill | how the toolkit and its gates behave |
| S5 | this folder's `beat_sheet.json` | what is on screen and said, beat by beat |

## Held out of the narration

The original framing credited AI fluency to "Stanford HAI" and said it is taught through
"Botspeak". Neither is said on camera until a source is supplied.

## Toolchain

Kokoro TTS (`af_bella`, local, no API keys) · Remotion 4.0.535 scenes via
`runtime/scripts/remotion_scenes.py` at `--scale=2` (4K) · ffmpeg conform · `./art run`
(review cut). Gates: F (fact-check), L (beat lint), V (frame QC), T (typecheck).
