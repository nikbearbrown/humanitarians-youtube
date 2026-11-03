# SHOTLIST — "Testing AI Video Editors, and a Setup Guide for New Fellows"

8 beats, 140.57s (2:20). Every duration is the measured Kokoro narration length; the visuals are cut to fit the voice, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 34 cues authored, 34 resolved, 0 unmatched. New components size themselves from `props.durationSeconds` (the measured narration), so a cue fraction lands on its word exactly.

Two threads, one cause (B01). The research beat (B02) surveys four tools without ranking them; the test beat (B03) shows the agent's real output; B04/B05 report what resisted and what the one test can and cannot show; B06 states the guide's real status: in progress.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 11.58s | `ClaudeComposerAsk` | library |
| B01 | WHY | 0:11 | 17.19s | `HaiProgressTwoFronts` | **new** |
| B02 | THE FIELD | 0:28 | 25.88s | `HaiToolField` | **new** |
| B03 | THE TEST | 0:54 | 16.96s | `HaiFootageShowcase` | **new** |
| B04 | WHERE IT RESISTED | 1:11 | 21.63s | `HaiProgressOverturned` | library |
| B05 | WHAT IT SHOWED | 1:33 | 18.92s | `HaiVerdictSplit` | **new** |
| B06 | THE GUIDE | 1:52 | 21.99s | `HaiProgressSignupChain` | library |
| B07 | OUTRO | 2:14 | 6.42s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about two things I worked on this week: testing whether an AI agent can edit our videos, and starting a setup guide for new Lyrical Literacy fellows.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `testing` | “testing whether an AI agent” | 0.417 | 4.83s |
| `guide` | “starting a setup guide” | 0.711 | 8.23s |

### B01 — WHY · `HaiProgressTwoFronts`

> Both come from the same problem, which is time. Every tutorial I make is built scene by scene, by hand. And every new fellow has to ask around just to get into the tools. If an agent could take on the editing, and a guide could take on the setup, the whole team moves faster.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `time` | “which is time” | 0.107 | 1.83s |
| `editing` | “built scene by scene” | 0.285 | 4.90s |
| `onboarding` | “ask around” | 0.527 | 9.07s |
| `agent` | “an agent could take on the editing” | 0.681 | 11.70s |
| `faster` | “whole team moves faster” | 0.906 | 15.57s |

### B02 — THE FIELD · `HaiToolField`

> I looked at four tools. Remotion, which Brutalist is built on, where a video is written as code. HyperFrames, from HeyGen, where a video is written as a web page, and it's built for agents. OpenReel, an open-source editor that runs in the browser, and whose desktop app connects to Claude. And DaVinci Resolve, through community connectors that let an agent drive a professional editor, though they work best with the paid Studio version.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `four` | “looked at four tools” | 0.005 | 0.13s |
| `remotion` | “Remotion, which Brutalist” | 0.067 | 1.73s |
| `hyperframes` | “HyperFrames, from HeyGen” | 0.246 | 6.37s |
| `openreel` | “OpenReel, an open-source editor” | 0.461 | 11.93s |
| `resolve` | “And DaVinci Resolve” | 0.701 | 18.13s |
| `studio` | “paid Studio version” | 0.949 | 24.57s |

### B03 — THE TEST · `HaiFootageShowcase`

> Then I tested one properly. I gave HyperFrames the finished footage and narration from Suno part one, and asked for captions that light up word by word, and a new intro. It came back with a four-minute cut: ninety-four caption lines, and none of them overlapping.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `tested` | “tested one properly” | 0.020 | 0.33s |
| `footage` | “finished footage and narration” | 0.210 | 3.57s |
| `captions` | “captions that light up” | 0.440 | 7.47s |
| `back` | “came back with” | 0.686 | 11.63s |
| `overlap` | “none of them overlapping” | 0.922 | 15.63s |

### B04 — WHERE IT RESISTED · `HaiProgressOverturned`

> It didn't go smoothly. The glass look I asked for disappeared against our cream backgrounds, so the footage had to move onto a dark stage. The captions copied the phonetic spelling of my name from the voice script, until that was fixed. The render needed about sixty gigabytes of scratch space, and filled my main drive. And the file came out at ten-eighty p, not four K.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `r0` | “glass look I asked for” | 0.077 | 1.67s |
| `r1` | “captions copied the phonetic” | 0.378 | 8.17s |
| `r2` | “sixty gigabytes” | 0.670 | 14.50s |
| `r3` | “ten-eighty p” | 0.923 | 19.97s |

### B05 — WHAT IT SHOWED · `HaiVerdictSplit`

> So here's what the test showed. The agent was good at packaging footage that already exists: captions, titles, an intro. It didn't add new teaching visuals; those still came from our own scenes. It didn't reach our four K standard. And OpenReel and DaVinci Resolve haven't had a hands-on test yet.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `showed` | “what the test showed” | 0.030 | 0.57s |
| `good` | “good at packaging” | 0.150 | 2.83s |
| `visuals` | “didn't add new teaching visuals” | 0.435 | 8.23s |
| `fourk` | “didn't reach our four K” | 0.673 | 12.73s |
| `pending` | “OpenReel and DaVinci Resolve” | 0.819 | 15.50s |

### B06 — THE GUIDE · `HaiProgressSignupChain`

> The second piece is the setup guide, and it's still in progress. It covers everything a new fellow needs before they can make anything. Discord comes first, because everything else hangs off it. Suno, which you sign into with Discord. Midjourney, through the Humanitarians AI Discord. And Canva. For each one: how to get access to the account, and how to use the tool.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `guide` | “setup guide” | 0.047 | 1.03s |
| `discord` | “Discord comes first” | 0.344 | 7.57s |
| `suno` | “Suno, which you sign” | 0.502 | 11.03s |
| `midjourney` | “Midjourney, through” | 0.620 | 13.63s |
| `canva` | “And Canva” | 0.752 | 16.53s |
| `each` | “For each one” | 0.823 | 18.10s |

### B07 — OUTRO · `HaiTitleOutro`

> Four tools looked at, one tested, and a guide on the way. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “Four tools looked at” | 0.000 | 0.00s |

<a id="916"></a>
## 9:16

`shorts.py` rewires the portrait sheet (`short/beat_sheet.json`) to each beat's `<Pattern>916` composition (THE ONDA CHECK). Every beat has a native portrait variant — no letterbox, no centre crop. The new components re-lay themselves for a 1080×1920 frame inside the y 230–1440 safe band; what moves where is described in each component's header comment.
