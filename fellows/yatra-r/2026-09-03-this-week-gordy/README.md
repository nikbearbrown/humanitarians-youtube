# This Week, Gordy.

**HUMANITARIANS AI · WEEKLY** · 12 beats · 2:23.6 · narrated by Yatra
(Kokoro `af_bella`, local and free) · `@Yatra`

## What this folder is

The **source** of the video, not the video. `beat_sheet.json` is the single source of
truth: every beat's narration, its measured audio duration, the Remotion composition that
renders it, and a `show` block describing what the viewer watches. Given the toolkit, this
folder rebuilds the episode from scratch — audio, frames and all.

Media (mp4/mp3/png) is deliberately not committed.

## What the episode reports

The weekly one-tool recap for **Gordy**. What actually happened this week: Gordy used,
graphics made for the Humanitarians AI LinkedIn page, and two articles written and sent to
Nina for review.

The episode's subject is that the week **ends mid-pipeline**. Four of five stages closed;
publish stays open, because that one is not the narrator's to close. That is what
distinguishes it from the previous episode in the series, which ended with three things
shipped.

## The constraint this episode is built around

The two articles are **in review, not published**, and nothing about their content is
known. That is enforced structurally, not by memory:

- `WkReview`'s `slots` are typed `{label: string}[]` — there is **no** title, summary,
  excerpt or content prop, so an article's contents cannot reach the screen even by
  accident. The slots render as dashed empty cards under a withheld band, and the Substack
  node stays hollow.
- `WkPipeline` has **no per-stage `state` field**, so the framework beat cannot leak the
  status board that the next beat reveals.
- `WkShip` draws **no artwork**. Inventing graphics and presenting them as the week's
  deliverable would be a fabricated artifact. Its chip reads `MADE`, never `LIVE` — the
  graphics were *created for* the page, and that is all that is claimed.

Gordy's description renders **verbatim** from its tool page, in quotation marks, with its
citation. The page says "two-mode" but never names the modes, so the modes are not named
anywhere in this episode — and the reel says on screen that one line is the whole public
description.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 source of truth — narration, measured durations, scene + props per beat |
| `beat_sheet.short.json` | The 9:16 derivative, with each beat rewired to its portrait composition |
| `FACTCHECK.md` | Claim ledger, and the full list of what is deliberately not claimed |
| `SOURCES.md` | The tool page, the first-person account, and the DOUBLE-CHECK rewrite log |
| `PROMPTS.md` | Every prompt shown on screen, verbatim |
| `SHOTLIST.md` | Typed work order — measured durations, composition per beat |
| `CHECKS-REPORT.md` | PROOF GATE: per-beat classification and the teaching-arc checklist |
| `QC-LOG.md` | Frame-level visual QC, GATE V verdicts, and the render-environment diagnosis |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds the episode end to end |
| `YOUTUBE.md` | Title, description, computed chapter timings, tags |

## How to read it

Start with `FACTCHECK.md`. For a first-person recap the failure mode is not a bad statistic
— it is claiming that unfinished work is finished. The fact-check is the list of things
this episode refuses to say.

## Source

- Gordy tool page — `humanitarians.ai/ai1/tools/gordy-tool` (description quoted verbatim)

## Rebuild

Free and local: Kokoro TTS, Remotion, ffmpeg. No API keys.

```bash
python3 runtime/scripts/generate_audio_kokoro.py <this-folder>   # audio is the master clock
python3 runtime/scripts/remotion_scenes.py <this-folder>          # render each beat
./art final <this-folder>                                         # compile the master
```

Regenerating audio changes the measured durations, so each composition's
`durationInFrames` must be retargeted to match, or progress-mapped animations get trimmed.

Scenes for this episode: `../scenes/WeekGordy.tsx` and `WeekGordy916.tsx`.
