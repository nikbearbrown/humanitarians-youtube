# 2026-07-27 - Building the AI Buzz Tracker dashboard

**Week covered:** 2026-07-20 - 2026-07-26

**Video:** [Watch on YouTube](https://www.youtube.com/watch?v=LiJnm8r8ArU)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Hacker News AI Buzz Tracker is a daily automated pipeline that reads what developers are saying on Hacker News about twelve AI companies and turns it into a 0 to 100 attention score for each company, along with a short summary of what commenters actually think.

This week the tracker got a dashboard, so its output can be read in a browser instead of a database table.

- **A live dashboard now shows three things:** a leaderboard ranking the companies by attention, a trend line showing whether each company's attention is rising or fading, and a breakdown of what kind of news (launches, funding, outages, controversy) is driving the week.
- **It runs from the existing automation server at a single web address**, with no separate hosting, and was confirmed working against the real database on 2026-07-21.
- **Six problems had to be fixed to get it running live**, one of them a security issue: the database key first wired into the page gave full read and write access, and anyone viewing the page source could have copied it. It was caught before shipping, revoked, and replaced with a read-only key.
- **Building the comment summaries exposed a parsing failure** that was rejecting every company's result. After changing how the model's output is requested and read, 9 of 12 companies returned a usable summary.
- **One honest limitation was found and kept in the video.** A popular post about a slide-making tool mentioned OpenAI and Anthropic only in passing, yet became the top story for both, so their summaries praised software neither company makes. The fix (the company must be named in the story title) was scheduled for the following week.

---

## The episode

A 20-beat progress showcase: a personal introduction, what the system does, the pipeline walked
through node by node (fetch, score, comments, sector summary), the new dashboard, and the
attribution failure above, closing on the fix planned next.

| Document | What it is |
|---|---|
| `beat_sheet.json` | the narration and visual plan, and the source of truth for the render |
| `BUILD-PROMPT.md` | instructions for rebuilding the reel |
| `BUILD-LOG.md` | build history, including revisions 5 and 6 to the opening |
| `PEDAGOGY.md` | narration structure gate (PASS) |
| `FACTCHECK.md` | 13 claims about the author's private system, listed for the author's own confirmation |
| `SOURCES.md` | asset provenance (all stills are the author's own screenshots) |

## The built reel

Built with **brutalist.art** (`cli-explainer` style), free and local throughout: Kokoro voice
`am_onyx`, Remotion, ffmpeg. 20 beats (5 cards and graphics, 15 screenshot stills), 5:48,
3840x2160.

The rendered video, per-beat narration audio, and per-beat clips are not stored in this folder.
They are large, rebuild from `beat_sheet.json`, and are excluded by this repository's
`.gitignore`. The full original build remains at the source production location.
