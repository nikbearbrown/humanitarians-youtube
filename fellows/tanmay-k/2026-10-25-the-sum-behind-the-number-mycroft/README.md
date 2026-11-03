# Week 28 work video — final

*The Sum Behind the Number: Taking Apart a Stress Test.* Tanmay Kulkarni, in for Humanitarians AI.
Publishable set, assembled 2026-10-25. Text and code only. The two masters are uploaded to YouTube.

## The work

A contribution to Mycroft's recipe `scenariostresstestingagent` in
[`nikbearbrown/mycroft`](https://github.com/nikbearbrown/mycroft): pull request
[#74](https://github.com/nikbearbrown/mycroft/pull/74), **merged** (merge commit `5d60312`, 2026-10-26 01:34 UTC).
40 files added, 2 modified (the recipe, and `logs/RUN_LOG.md` appended at the end), 0 removed, 0 renamed. Steps 1, 3 and 5
are closed in sample mode: a provenance check, a data-shape validator that uses the workflow's own rules, and a Python port
of four code nodes checked against the original code (24 of 24 requests identical), with a self-test of 27 checks including
12 deliberate breaks and 22 invented sample portfolios. The recipe stays `DRAFT`, with five items open. The contribution's
own code and README live in the Mycroft repository and are linked here, not copied.

## The films

| | File | | |
|---|---|---|---|
| **Long** | `the-sum-behind-the-number.mp4` | 3840×2160 · 30 fps · 3:28 (208.4 s) | −14.7 LUFS / −1.9 dBFS |
| **Short** | `the-sum-behind-the-number-short.mp4` | 2160×3840 · 30 fps · 1:19 (78.8 s) | −14.6 LUFS / −2.0 dBFS |

Each film carries its captions (`.srt` and `.vtt`) and its YouTube title, description, chapters and tags (`*-youtube.md`).
Narration is Kokoro `am_onyx`.

- **Angle:** *a stress-test percentage is a sum of named shocks, and a sum can be taken apart.* Angle and its audit against
  earlier work videos: `ANGLE.md`.
- **Long, A RUNNING TOTAL:** a block of loss grows one named shock at a time until the workflow's number is rebuilt:
  one holding (−15, −35, −40 make −90, the workflow's own README worked example), the whole book (36 + 27 + 15 = 78), a milder
  scenario with the same rule, my Python copy run beside the original, and the checks that keep the sum honest.
- **Short:** its own script, one continuous scene, for a viewer who never sees the long film; it loops back to the
  opening number, now explained.

## How both were checked

| | Long | Short |
|---|---|---|
| Rubric | `PROOF.md` teaching rubric /12 + production gate | Shorts rubric /12 + 11-point compiled-file gate |
| Result | 12/12, gate PASS (`PROOF-REVIEW-VIDEO.md`, `VIDEO-GATE-LONG.md`) | 12/12, gate 11/11 (`PROOF-REVIEW-SHORT-VIDEO.md`, `VIDEO-GATE-SHORT.md`) |
| Gate P (narration read aloud) | signed 2026-10-25 (`GATE-P-SIGNOFF.md`) | signed 2026-10-25 (`GATE-P-SIGNOFF-SHORT.md`) |

## Links

Add the YouTube URLs once the videos are live.

| | YouTube |
|---|---|
| Long (16:9, 4K) | <!-- YOUTUBE_LINK_LONG --> *(to add)* |
| Short (9:16, 4K) | <!-- YOUTUBE_LINK_SHORT --> *(to add)* |

**Placeholder in the Short's description:** `[FULL VIDEO LINK]`. Swap in the long film's YouTube URL once it is live, and set
the long as the Short's related video in YouTube Studio.

## What the films claim, and what they do not

The full list is in each `*-youtube.md`. In short: every portfolio is invented; the tickers on screen come from the
workflow's own sector list; the numbers are scenario arithmetic, not predictions and not investment advice; every figure is
read from a committed file or the workflow's README; nothing live is ever called.

## Uploading: choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro). Both descriptions say so; whether to tick
   YouTube's "altered or synthetic content" box is your call.
2. **Thumbnail.** The headline number with the stack of three blocks (long film B05) or the opening frame (B01) is the most
   distinctive.
3. **Captions.** Upload the `.srt` as English captions, not YouTube's auto-captions: it shows the figures as written
   (−78%, $10,000, 36 + 27 + 15) where the voice says the words.
