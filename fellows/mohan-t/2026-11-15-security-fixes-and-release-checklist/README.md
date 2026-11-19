# Timesheet Redesign – Week 3: Security Fixes and the Release Checklist

Test the ways an admin could misuse their own power, not just the happy path.

| | |
|---|---|
| **Runtime** | 2:29.83 (149.83 s) |
| **Format** | 24 fps · 16:9 (1920×1080) and 9:16 (1080×1920) |
| **Voice** | Kokoro `am_michael` — AI narration of my script, disclosed in the first beat |
| **Beats** | 9 · `ai-explainer` spine |
| **Brand** | `claude-hai` · `@HumanitariansAI` |
| **Presenter** | Mohan T. |
| **Status** | Built · frame QC and type gate passed · fact-checked · **not published** |
| **Renders** | [Google Drive](https://drive.google.com/drive/folders/1IDkPJ5rz7ClIZRHDSdUFdfAW-KsQm0BB?usp=sharing) — `landscape/TimesheetRedesignWeek3_MohanT.mp4`, `vertical/TimesheetRedesignWeek3_MohanT.mp4` |

## Evidence of the work

- [PR #16](https://github.com/nikbearbrown/humanitarians_html/pull/16) 'Second review (Nov 17)'
- Commits `76b6f21`, `406398e`, `106680f`, `e23ef74`, `d093582`
- CI run [44384744932](https://github.com/nikbearbrown/humanitarians_html/actions/runs/44384744932): success

## Beats

| Beat | Act | Opens with | Measured |
|---|---|---|---:|
| B00 | INTRO | Hi, I am Mohan and this video is about week three of the timesheet redesign: security fixe | 12.27 s |
| B01 | BLUF | In week three, I fixed the findings from the second review, including two security issues, | 9.13 s |
| B02 | BODY | The first was a security bug: an admin could get around the rule that you can't change you | 26.13 s |
| B03 | BODY | Two reliability fixes | 15.70 s |
| B04 | BODY | I wrote one release checklist: staging first, then production | 20.07 s |
| B05 | LIMITS | Stated plainly: pull request sixteen is not merged, and nothing new is live | 19.43 s |
| BVDT | VERDICT | To recap week three | 16.21 s |
| BHTF | YOUR_TURN | Your turn | 24.19 s |
| BOUT | OUTRO | Timesheet redesign, week three | 6.70 s |

## Fact-check

8 claims verified against code or GitHub; 1 from my own notes with no public record to
check. See [`FACTCHECK.md`](FACTCHECK.md).

## What is in this folder

```
README.md                  this file
FRICTIONAL.md              the process log for this work
beat_sheet.json            every beat: narration, shot, measured duration (16:9)
vertical/beat_sheet.json   the 9:16 cut
FACTCHECK.md               each on-screen claim and its evidence
SOURCES.md · SHOTLIST.md · PROMPTS.md · TYPECHECK.md
```

Videos and audio are not committed; the rendered masters are on Drive.
