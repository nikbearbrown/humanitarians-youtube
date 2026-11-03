# SHOTLIST — "Writing the Lyrical Literacy Fellows Handbook"

8 beats, 135.84s (2:15). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 36 cues authored, 36 resolved.

A progress report has one deliverable to show, so B01 shows it: crops of the real handbook, never a mock-up. B02–B04 are the three things worth knowing about it (the part fellows ask about most, what review changed, what it has not done yet); B05 puts it on the renewal plan; B06 tells a new fellow what to do.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 15.02s | `ClaudeComposerAsk` | library |
| B01 | THE HANDBOOK | 0:15 | 21.72s | `HaiDocPages` | **new** |
| B02 | ACCESS | 0:36 | 16.45s | `HaiProgressSignupChain` | library |
| B03 | WHAT REVIEW CHANGED | 0:53 | 22.70s | `HaiProgressOverturned` | library |
| B04 | WHAT IT DOES | 1:15 | 18.65s | `HaiVerdictSplit` | library |
| B05 | NEXT | 1:34 | 19.09s | `HaiProgressRoadmap` | library |
| B06 | WHAT TO DO | 1:53 | 16.58s | `HaiApplyCard` | library |
| B07 | OUTRO | 2:10 | 5.63s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about the handbook I wrote for new Lyrical Literacy fellows. Until now, getting started meant asking around: which account, which link, who approves what. This week, all of it went into one document.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `asking` | “meant asking around” | 0.502 | 7.53s |
| `one` | “into one document” | 0.917 | 13.77s |

### B01 — THE HANDBOOK · `HaiDocPages`

> Here it is: forty-six pages in twelve sections. Claude drafted it from the program's own pages and from our nine tutorials, and I reviewed and corrected it. It covers getting into every tool, full guides to Suno and Midjourney, the weekly reporting rules, the whole video workflow, and how renewals work. And it opens with a first-week checklist.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `here` | “Here it is” | 0.000 | 0.00s |
| `pages` | “forty-six pages” | 0.043 | 0.93s |
| `drafted` | “Claude drafted it” | 0.178 | 3.87s |
| `reviewed` | “I reviewed” | 0.381 | 8.27s |
| `tools` | “getting into every tool” | 0.493 | 10.70s |
| `guides` | “full guides to Suno” | 0.569 | 12.37s |
| `mj` | “and Midjourney” | 0.629 | 13.67s |
| `reporting` | “weekly reporting rules” | 0.683 | 14.83s |
| `workflow` | “whole video workflow” | 0.758 | 16.47s |
| `renewals` | “how renewals work” | 0.821 | 17.83s |
| `checklist` | “first-week checklist” | 0.953 | 20.70s |

### B02 — ACCESS · `HaiProgressSignupChain`

> The part new fellows ask about most is access. Discord comes first, because Suno and Midjourney both sign in through it. Then Canva for design, and Adobe for editing. A month ago, this chain lived in people's heads. Now each link is a numbered set of steps.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `doc` | “ask about most is access” | 0.051 | 0.83s |
| `t0` | “Discord comes first” | 0.191 | 3.13s |
| `t1` | “because Suno” | 0.259 | 4.27s |
| `t2` | “Midjourney both sign in” | 0.348 | 5.73s |
| `t3` | “Then Canva” | 0.472 | 7.77s |
| `t4` | “Adobe for editing” | 0.582 | 9.57s |
| `each` | “numbered set of steps” | 0.928 | 15.27s |

### B03 — WHAT REVIEW CHANGED · `HaiProgressOverturned`

> It didn't come out right first time. The first draft followed a navy and cream palette that looked heavy, so it was rebuilt to match our website. My review comments in Word removed a step nobody needs, and handed the hours and logs to Claude. And when the program's rules changed mid-week, the handbook changed with them: build files on GitHub, and every video to one reviewer.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `r0` | “navy and cream” | 0.153 | 3.47s |
| `r1` | “removed a step” | 0.420 | 9.53s |
| `r2` | “handed the hours” | 0.517 | 11.73s |
| `r3` | “build files on GitHub” | 0.839 | 19.03s |
| `r4` | “every video to one reviewer” | 0.922 | 20.93s |

### B04 — WHAT IT DOES · `HaiVerdictSplit`

> What it does now: one place for access, tools, reporting and renewals, in an editable Word file with a version history, so whoever runs onboarding next can keep it current. What it hasn't done yet is meet a new fellow. The real test is someone following it from page one, without asking anyone.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `showed` | “What it does now” | 0.000 | 0.00s |
| `good` | “one place for access” | 0.061 | 1.13s |
| `visuals` | “hasn't done yet” | 0.618 | 11.53s |
| `pending` | “The real test” | 0.710 | 13.23s |

### B05 — NEXT · `HaiProgressRoadmap`

> It also closes the first item on my renewal plan, which has now been approved, almost a month ahead of the thirty October target. Next is automating our video editing: testing two more tools on the same footage in November, then building the best one into a pipeline for Lyrical Literacy by mid-December.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `plan` | “first item on my renewal plan” | 0.059 | 1.13s |
| `next` | “Next is automating” | 0.451 | 8.60s |

### B06 — WHAT TO DO · `HaiApplyCard`

> If you're joining Lyrical Literacy: ask your project manager for the handbook, start with the first-week checklist, and come to the team meeting on Wednesdays at twelve, Eastern time. If anything in it is unclear or out of date, tell me, and it goes into the next version.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `ask` | “ask your project manager” | 0.135 | 2.23s |
| `checklist` | “first-week checklist” | 0.342 | 5.67s |
| `meeting` | “the team meeting” | 0.444 | 7.37s |
| `tell` | “tell me” | 0.854 | 14.17s |

### B07 — OUTRO · `HaiTitleOutro`

> One handbook, so nobody has to ask twice. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “nobody has to ask twice” | 0.190 | 1.07s |

