# Yatra R.

Weekly video work for Humanitarians AI, built with the `brutalist.art` toolkit —
Claude-bookended explainers, narrated with Kokoro (`af_bella`, local and free), rendered
with Remotion. Channel handle `@Yatra`.

**This folder holds sources, not videos.** Each episode directory contains its beat sheet
and its paperwork; the rendered mp4s are not committed.

## Episodes

| Folder | Title | Beats | Length | Formats |
|---|---|---|---|---|
| [`2026-08-20-the-bottleneck-moved`](2026-08-20-the-bottleneck-moved/) | The Bottleneck Moved. | 10 | 2:46.1 | 16:9 |
| [`2026-08-21-assisted-not-automated`](2026-08-21-assisted-not-automated/) | Assisted, Not Automated. | 24 | 5:27.6 | 16:9 + 9:16 |
| [`2026-08-21-every-tool-every-week`](2026-08-21-every-tool-every-week/) | Every Tool, Every Week. | 10 | 2:26.8 | 16:9 + 9:16 |
| [`2026-08-21-the-judgment-is-the-job`](2026-08-21-the-judgment-is-the-job/) | The Judgment Is the Job. | 10 | 2:40.2 | 16:9 + 9:16 |
| [`2026-08-30-one-tool-a-week-brandy`](2026-08-30-one-tool-a-week-brandy/) | One Tool a Week. | 10 | 2:25.8 | 16:9 + 9:16 |

## What a beat sheet is

One JSON file per episode, and it is the whole film: every beat carries its narration, the
**measured** duration of that narration's audio, the Remotion composition and props that
render it, and a `show` block naming what the viewer actually watches at each moment.
Audio is the master clock — durations are measured from generated mp3s, never estimated,
and never hand-tuned.

## The house rules these episodes follow

- **Audio-first.** Narration is generated and measured before any visual work; every
  composition's frame count derives from a real mp3.
- **Show, don't tell.** A beat that could be exported as a static slide is a defect. Every
  beat carries a `show` block written before its narration.
- **Say what isn't known.** Each episode's `FACTCHECK.md` lists not only what is claimed but
  what is deliberately *not* claimed. Where an episode had no data, it uses ordinal or
  descriptive language rather than inventing a figure — and where figures were supplied,
  every one is cited on screen.
- **Never publish from the pipeline.** Masters stay local; publishing is a human step.

## A note on two folder names

`the-bottleneck-moved` and `the-judgment-is-the-job` were authored before the channel moved
to `@Yatra`, so their internal `slug` fields still read `claude-liam-…`. The folder names
here use the date-plus-title convention instead; the stale slugs inside those two beat
sheets are cosmetic and do not affect a rebuild.
