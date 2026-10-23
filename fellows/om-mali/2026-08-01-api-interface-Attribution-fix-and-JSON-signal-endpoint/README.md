# 2026-08-01 - Attribution fix and JSON signal endpoint

**Week covered:** 2026-07-27 - 2026-08-02

**Video:** [Watch on YouTube](https://www.youtube.com/watch?v=LiJnm8r8ArU)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Hacker News AI Buzz Tracker is a daily automated pipeline that reads what developers are saying on Hacker News about twelve AI companies and turns it into a 0 to 100 attention score for each company, along with a short summary of what commenters actually think.

This week made that output more correct, usable by other software, and clear about its limits.

- **Stories are now attributed to the right company.** Previously, each company's top story was simply its most popular match, so a slide-tool post that mentioned OpenAI and Anthropic in passing (1,018 points) became the top story for both. Now a story only counts if the company is named in its title. After the fix, OpenAI's top stories are about OpenAI, and the slide-tool post no longer appears for either company. Eight automated tests cover the rule, including that exact post.
- **The fix has a stated limit.** A title can name a product without being about the company: Anthropic's top stories are now real, but they are third-party tools built for Claude, not news about Anthropic itself.
- **Other systems can now request the signal directly.** A new web address returns the latest run as a versioned, documented JSON record with each company's score, momentum, sentiment, and warning flags.
- **Gaps are flagged, not hidden.** In the run shown in the video, only three of the twelve companies had enough comments for a sentiment reading. The other nine are returned with a "degraded" flag rather than being dropped or filled in.
- **Also shipped:** a richer email digest and a separate alert that emails when the pipeline itself fails.

---

## The episode

A 7-beat progress update: a personal introduction, the three questions the week asked (is the
output right, can other systems use it, is it honest about its limits), the attribution fix
shown before and after on one screenshot, its remaining limit, the endpoint's raw payload and
the same data read as one row per company, and a close on what was built and verified.

| Document | What it is |
|---|---|
| `beat_sheet.json` | the narration and visual plan, and the source of truth for the render |
| `PEDAGOGY.md` | narration structure gate (PASS) |
| `mp3/timings.json` | measured narration timings per beat |

The narration is the author's own wording, confirmed before audio was generated.

## The built reel

Built with **brutalist.art**, free and local throughout: Kokoro voice `am_onyx`, Remotion,
ffmpeg. 7 beats, about 1:51, 3840x2160 (rebuilt from the source beats at 4K on 2026-08-04, not
upscaled from the earlier 1440p cut).

The rendered video and per-beat audio are not stored in this folder. They are excluded by this
repository's `.gitignore` and rebuild from `beat_sheet.json`.
