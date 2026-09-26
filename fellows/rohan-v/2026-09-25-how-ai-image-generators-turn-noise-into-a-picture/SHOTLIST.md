# SHOTLIST — "How AI Image Generators Turn Noise Into a Picture"

8 beats, 147.82s (2:27). Every duration is the measured Kokoro narration length; the visuals are cut to fit the voice, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 36 cues authored, 36 resolved, 0 unmatched. New components size themselves from `props.durationSeconds` (the measured narration), so a cue fraction lands on its word exactly.

The reel reaches its one equation at B03 on purpose: B01 (where images start) and B02 (an analogy) come first, so the equation arrives as a summary of something the viewer has already watched happen. Every picture in B01–B05 is recorded output of the toy model (see MEASUREMENTS.txt).

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.54s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:18 | 19.58s | `DiffuseSeedStatic` | **new** |
| B02 | ANALOGY | 0:38 | 19.90s | `DiffuseRainForward` | **new** |
| B03 | MECHANISM | 0:58 | 21.16s | `DiffuseMixEquation` | **new** |
| B04 | MEASURED | 1:19 | 21.40s | `DiffuseReverseRun` | **new** |
| B05 | SEED AND PROMPT | 1:40 | 17.28s | `DiffuseSeedPrompt` | **new** |
| B06 | WHAT TO DO | 1:57 | 21.55s | `HaiApplyCard` | library |
| B07 | OUTRO | 2:19 | 8.41s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how AI image generators like Midjourney turn random noise into a picture. You type a prompt, and moments later there are four images that never existed before. Nothing was searched for, and nothing was pasted together. Every one of them started as static.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `prompt` | “You type a prompt” | 0.417 | 7.73s |
| `four` | “four images that never existed” | 0.550 | 10.20s |
| `notsearched` | “Nothing was searched for” | 0.716 | 13.27s |
| `static` | “started as static” | 0.937 | 17.37s |

### B01 — BACKGROUND · `DiffuseSeedStatic`

> Midjourney's own guide says it plainly: every image begins as random noise, like the static on an old TV. That starting noise comes from a number called a seed. From there, the model does one thing, over and over. It looks at the static, and removes a little of the noise. Do that enough times, and a picture is left.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `guide` | “own guide says it plainly” | 0.027 | 0.53s |
| `tv` | “static on an old TV” | 0.264 | 5.17s |
| `seed` | “called a seed” | 0.458 | 8.97s |
| `remove` | “removes a little of the noise” | 0.763 | 14.93s |
| `left` | “a picture is left” | 0.938 | 18.37s |

### B02 — ANALOGY · `DiffuseRainForward`

> Think of a photo left out in the rain. Each drop smudges it a little more, until all that's left is grey speckle. Ruining a picture like that is easy, and you can do it with simple arithmetic. The hard part is going backwards. So that's what the model is trained to do: shown a smudged picture, guess what it looked like one drop earlier.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `rain` | “left out in the rain” | 0.034 | 0.67s |
| `speckle` | “grey speckle” | 0.281 | 5.60s |
| `arithmetic` | “simple arithmetic” | 0.509 | 10.13s |
| `backwards` | “going backwards” | 0.636 | 12.67s |
| `earlier` | “one drop earlier” | 0.933 | 18.57s |

### B03 — MECHANISM · `DiffuseMixEquation`

> Here is the rule for adding the noise. The noisy picture is part picture, plus part noise. At every step, the picture's share shrinks, and the noise's share grows. By step one thousand, less than one percent of the picture is left. Training shows the model millions of these mixes, and asks it just one question: which part of this is the noise?

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `rule` | “rule for adding the noise” | 0.024 | 0.50s |
| `parts` | “part picture, plus part noise” | 0.165 | 3.50s |
| `shrinks` | “picture's share shrinks” | 0.328 | 6.93s |
| `thousand` | “By step one thousand” | 0.507 | 10.73s |
| `question` | “just one question” | 0.857 | 18.13s |

### B04 — MEASURED · `DiffuseReverseRun`

> So I trained one myself. A tiny model, on my laptop, with no graphics card. Twelve thousand little pictures of hearts and music notes, each sixteen pixels across, and about half an hour of training. Then I gave it pure static, asked for a heart, and let it take a thousand small steps. At first it's only guessing. By the last step, there's a heart.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `trained` | “trained one myself” | 0.011 | 0.23s |
| `laptop` | “no graphics card” | 0.179 | 3.83s |
| `pictures` | “Twelve thousand little pictures” | 0.248 | 5.30s |
| `static` | “gave it pure static” | 0.592 | 12.67s |
| `guessing` | “only guessing” | 0.865 | 18.50s |
| `heart` | “there's a heart” | 0.967 | 20.70s |

### B05 — SEED AND PROMPT · `DiffuseSeedPrompt`

> Now watch what the seed does. Keep the same static, but change the prompt to a music note, and the same noise becomes a note. Keep the prompt, change the seed, and you get a different heart every time. That's why Midjourney shows you four pictures. One prompt, four different starting points.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `same` | “Keep the same static” | 0.121 | 2.10s |
| `note` | “becomes a note” | 0.363 | 6.27s |
| `change` | “change the seed” | 0.505 | 8.73s |
| `every` | “different heart every time” | 0.594 | 10.27s |
| `four` | “four different starting points” | 0.910 | 15.73s |

### B06 — WHAT TO DO · `HaiApplyCard`

> So here's how to use this. When you're testing a change to your prompt, lock the seed. Midjourney's guide calls it a control in an experiment: now the only thing that changed is your words. But don't use a seed to keep a style or a character. It only sets the starting static, and Midjourney says it has the least effect of anything. For that, use style references.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `lock` | “lock the seed” | 0.170 | 3.67s |
| `control` | “control in an experiment” | 0.294 | 6.33s |
| `dont` | “don't use a seed” | 0.518 | 11.17s |
| `least` | “least effect of anything” | 0.815 | 17.57s |
| `refs` | “use style references” | 0.936 | 20.17s |

### B07 — OUTRO · `HaiTitleOutro`

> Every picture starts as noise. Lock the seed when you want to see what your words are really doing. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “Lock the seed when you want” | 0.266 | 2.23s |

<a id="916"></a>
## 9:16

`shorts.py` rewires the portrait sheet (`short/beat_sheet.json`) to each beat's `<Pattern>916` composition (THE ONDA CHECK). Every beat has a native portrait variant — no letterbox, no centre crop. The new components re-lay themselves for a 1080×1920 frame inside the y 230–1440 safe band; what moves where is described in each component's header comment.
