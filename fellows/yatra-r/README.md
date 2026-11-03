# Yatra R.

**Role:** Social Media Volunteer  
**Project:** _to be filled in_  
**GitHub:** _not on file_

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
| [`2026-09-01-nobody-wrote-this`](2026-09-01-nobody-wrote-this/) | Nobody Wrote This. | 14 | 2:48.9 | 16:9 + 9:16 |
| [`2026-09-03-this-week-gordy`](2026-09-03-this-week-gordy/) | This Week, Gordy. | 12 | 2:24.1 | 16:9 + 9:16 |
| [`2026-09-07-interest-media`](2026-09-07-interest-media/) | Interest Media. | 13 | 2:29.6 | 16:9 + 9:16, both 4K |
| [`2026-10-21-both-sides-of-the-table`](2026-10-21-both-sides-of-the-table/) | Both Sides of the Table. | 14 | 2:48.9 | 16:9 + 9:16 |
| [`2026-10-21-the-mask-slips`](2026-10-21-the-mask-slips/) | The Mask Slips. | 13 | 2:48.3 | 16:9 + 9:16 |
| [`2026-10-29-ads-in-the-picture`](2026-10-29-ads-in-the-picture/) | Ads in the Picture. | 13 | 2:54.0 | 16:9 + 9:16, both 4K |
| [`2026-10-30-no-default-winner`](2026-10-30-no-default-winner/) | No Default Winner. | 13 | 2:42.4 | 16:9 + 9:16, both 4K |

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

## A note on the narrator

Every episode through `2026-09-03-this-week-gordy` is narrated in Yatra's own first person
("Hi, I'm Yatra"). From `2026-09-07-interest-media` onward the voice introduces itself as a
**stand-in** — "Hello, this is Bella, in for Yatra" — and signs off the same way. The voice
is the same Kokoro `af_bella` throughout; what changed is that the episode now says so out
loud, so a viewer is never left guessing whose voice it is. The corner bug stays `@Yatra`
in both cases.

One visible consequence: on stand-in episodes the greeting slot carries the *narrator's*
name (`Vanakkam, Bella`) rather than the channel owner's, which is how the toolkit's
IN-FOR-BEAR LAW handles a substitute voice.

## A note on two folder names

`the-bottleneck-moved` and `the-judgment-is-the-job` were authored before the channel moved
to `@Yatra`, so their internal `slug` fields still read `claude-liam-…`. The folder names
here use the date-plus-title convention instead; the stale slugs inside those two beat
sheets are cosmetic and do not affect a rebuild.

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
