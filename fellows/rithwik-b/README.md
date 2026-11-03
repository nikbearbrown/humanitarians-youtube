# Rithwik B.

**Role:** AI Software Engineer
**Project:** AI Fluency × Brutalist — explainer series, and the Medhavy bio-art figure audit
**GitHub:** [@rithwikbanala](https://github.com/rithwikbanala)

Humanitarians AI fellow. I make explainer films with the Brutalist toolkit about what
AI fluency means in practice — knowing which steps of an AI-assisted build the machine
owns and which stay yours — and I audit AI-generated teaching media against its own
inputs. Video projects live in one dated lowercase-kebab folder per reel,
`YYYY-MM-DD-slug/`. The folder date is the day the reel was built; research and
scripting for each reel ran over the two weeks listed in [HOURS.md](HOURS.md).

**Renewal:** [RENEWAL.md](RENEWAL.md) · **Hours:** [HOURS.md](HOURS.md) ·
**Weekly records:** [weekly-hours/](weekly-hours/README.md)

## Weekly progress reports

One folder per week — `README.md` (report and evidence), `SCRIPT.md` (progress narration),
`FRICTIONAL.md` — with that week's hours record in [weekly-hours/](weekly-hours/README.md).

| Week | Dates | Report | Hours | Focus |
|---|---|---|---:|---|
| 1 | 3–7 Aug | [progress-week-1](2026-08-03-progress-week-1/README.md) | [20](weekly-hours/2026-08-03-weekly-hours.md) | Bio-art onboarding · film 1 research |
| 2 | 10–14 Aug | [progress-week-2](2026-08-10-progress-week-2/README.md) | [20](weekly-hours/2026-08-10-weekly-hours.md) | Audit rubric · film 1 script |
| 3 | 17–21 Aug | [progress-week-3](2026-08-17-progress-week-3/README.md) | [20](weekly-hours/2026-08-17-weekly-hours.md) | Audit figures 1–25 · film 2 research |
| 4 | 24–28 Aug | [progress-week-4](2026-08-24-progress-week-4/README.md) | [21](weekly-hours/2026-08-24-weekly-hours.md) | Audit write-up · film 2 script |
| 5 | 31 Aug – 4 Sep | [progress-week-5](2026-08-31-progress-week-5/README.md) | [21](weekly-hours/2026-08-31-weekly-hours.md) | Structure check · film 3 research |
| 6 | 7–11 Sep | [progress-week-6](2026-09-07-progress-week-6/README.md) | [20](weekly-hours/2026-09-07-weekly-hours.md) | Viewer blank page · film 3 script |
| 7 | 14–18 Sep | [progress-week-7](2026-09-14-progress-week-7/README.md) | [21](weekly-hours/2026-09-14-weekly-hours.md) | Viewer fix · film 4 research |
| 8 | 21–25 Sep | [progress-week-8](2026-09-21-progress-week-8/README.md) | [22](weekly-hours/2026-09-21-weekly-hours.md) | Session reel built · film 4 script |
| 9 | 28 Sep – 2 Oct | [progress-week-9](2026-09-28-progress-week-9/README.md) | [20](weekly-hours/2026-09-28-weekly-hours.md) | Viewer build · film 5 research |
| 10 | 5–9 Oct | [progress-week-10](2026-10-05-progress-week-10/README.md) | [20](weekly-hours/2026-10-05-weekly-hours.md) | Toolkit study · film 5 script |
| 11 | 12–16 Oct | [progress-week-11](2026-10-12-progress-week-11/README.md) | [21](weekly-hours/2026-10-12-weekly-hours.md) | Series plan · film 6 research |
| 12 | 19–23 Oct | [progress-week-12](2026-10-19-progress-week-12/README.md) | [20](weekly-hours/2026-10-19-weekly-hours.md) | Generator script · film 6 script |
| 13 | 26–30 Oct | [progress-week-13](2026-10-26-progress-week-13/README.md) | [22](weekly-hours/2026-10-26-weekly-hours.md) | Six films built, checked, fixed |
| | | | **268** | |

## What's in this folder

- [2026-09-21-a-blank-page-and-49-ai-figures](2026-09-21-a-blank-page-and-49-ai-figures/) — session replay: the bio-art viewer's blank page, and the 49-figure audit
- [2026-10-29-fluent-isnt-finished](2026-10-29-fluent-isnt-finished/) — film 1: Claude builds, can't watch; fluency is knowing which calls stay yours
- [2026-10-29-the-beat-sheet-is-the-prompt](2026-10-29-the-beat-sheet-is-the-prompt/) — film 2: one file is the whole prompt; audio first
- [2026-10-29-look-at-the-frames](2026-10-29-look-at-the-frames/) — film 3: a passing gate is not a finished film
- [2026-10-29-trust-then-verify](2026-10-29-trust-then-verify/) — film 4: which claims need a source, and who signs
- [2026-10-30-show-what-broke](2026-10-30-show-what-broke/) — film 5: a failure log as evidence
- [2026-10-30-the-workflow-is-the-lesson](2026-10-30-the-workflow-is-the-lesson/) — film 6: the machine runs the steps, you stand at the checks

## Voice choice

**Series voice:** Bella (`af_bella`) — the `hai` persona.
**Register:** Plain — one idea per film, said directly.

Recorded as `metadata.voice_kokoro` in every beat sheet of the AI Fluency series.

**The outlier:** the 2026-09-21 bio-art session replay is Onyx (`am_onyx`). It was built
before the series voice was chosen and stays that way on disk. If it publishes alongside
the series it gets re-voiced — audio is the clock, so that means new narration and a
re-cut.

## House style

| Reel | Format | Brand | Spine |
|---|---|---|---|
| A Blank Page and 49 AI Figures | CLI explainer | `claude` palette | cold open → problem → ask → code → output → change → summary → next steps → outro |
| AI Fluency films 1–6 | `ai-explainer` | `claude` · `@HumanitariansAI` | composer cold open → hesitant-writer BLUF → body → verdict → your turn → outro |

All six series films use stock toolkit compositions only (`ClaudeComposerAsk`,
`BrutalistHesitantWriter`, `ShowTellCard`, `ClaudeCodeBeat`); the toolkit stays read-only.
One deliberate departure: the outro is a `ShowTellCard` layout, not `ClaudeTitleOutro`,
because that composition hardcodes another channel's handle.

## Reports

| Date | Title | Subject | Runtime | Status |
|---|---|---|---|---|
| 2026-10-30 | [The Workflow Is the Lesson](2026-10-30-the-workflow-is-the-lesson/) | The build loop — author, audio, render, check, sign — and where a person must stand | 2:55 | Built · QC'd · fact-check drafted · not published |
| 2026-10-30 | [Show What Broke](2026-10-30-show-what-broke/) | The series' own 11 failures as evidence; who caught them | 2:48 | Built · QC'd · fact-check drafted · not published |
| 2026-10-29 | [Trust, Then Verify](2026-10-29-trust-then-verify/) | GATE F — the final cut refuses to compile until a person signs | 2:47 | Built · QC'd · fact-check drafted · not published |
| 2026-10-29 | [Look at the Frames](2026-10-29-look-at-the-frames/) | Reading a QC report and contact sheet; blocker, major or fine | 2:48 | Built · QC'd · fact-check drafted · not published |
| 2026-10-29 | [The Beat Sheet Is the Prompt](2026-10-29-the-beat-sheet-is-the-prompt/) | Narration, show, scene — and why audio comes first | 2:50 | Built · QC'd · fact-check drafted · not published |
| 2026-10-29 | [Fluent Isn't Finished](2026-10-29-fluent-isnt-finished/) | Claude builds but can't watch; sorting steps into Claude-owned and human-owned | 2:52 | Built · QC'd · fact-check drafted · not published |
| 2026-09-21 | [A Blank Page and 49 AI Figures](2026-09-21-a-blank-page-and-49-ai-figures/) | The viewer crash, its fix, and 31 of 49 figures on five templates | 3:05 | Built · fact-checked · one beat needs a re-cut · not published |

The through-line across both projects: **an automatic check passing is not the output
being right.** The figure generator returned an image for every prompt while ignoring most
of them; the video gates passed films that still had visible defects. Frame review caught
7 of the 11 series defects; the gates caught 4.

## Media policy

Per `fellows/README.md` (rule of 2026-09-18): **renders go to Drive, build inputs and
source stay here.** Each reel's `.gitignore` excludes `mp3/`, `media/`, `clips/`, `mp4/`
and `*-slate.mp4` by location. Committed: beat sheets, `timings.json`, fact-checks,
sources, QC reports and contact sheets, build prompts, generator scripts, the audit and
the viewer diff.

Rebuild with the free local toolkit ([brutalist.art](https://github.com/nikbearbrown/brutalist.art)) —
each reel's `BUILD-PROMPT.md` has the commands.

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
