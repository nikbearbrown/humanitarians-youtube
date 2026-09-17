# SHOTLIST — "16-bit or 24-bit: What Bit Depth Does"

Seven beats, 127.24s (2:07). Every duration is the measured Kokoro narration
length; the visuals are cut to fit the voice, never the other way round.

**This reel is word-clock choreographed.** `align.py` (faster-whisper) measured
when every word is actually spoken, `cues.json` names an anchor phrase per
reveal, and `sync_cues.py` resolved those phrases into fractions and wrote them
into the beat sheet at `shot.remotion.props.cues`. Nothing below is a guessed
timing — the *cue* column is the fraction of the beat at which that phrase
leaves the narrator's mouth. 30 cues, 30 resolved, 0 unmatched.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.47s | `ClaudeComposerAsk` | chassis |
| B01 | BACKGROUND | 0:18 | 23.62s | `BitSoundToNumbers` | **new** |
| B02 | ANALOGY → IDEA | 0:42 | 19.73s | `BitStaircase` | **new** |
| B03 | MECHANISM | 1:01 | 18.24s | `BitGapIsHiss` | **new** |
| B04 | THE NUMBERS | 1:20 | 19.41s | `BitRoomUnderneath` | **new** |
| B05 | WHAT TO DO | 1:39 | 17.94s | `HaiApplyCard` | library |
| B06 | OUTRO | 1:57 | 9.83s | `HaiTitleOutro` | library |

The shape is deliberate and came out of a correction from Rohan: *"It starts out
very abruptly. what is a person who knows nothing about audio going to
understand?"* The answer was to spend a whole beat (B01) on what sound even is
before the word "bit depth" is used as anything but a name, and a second whole
beat (B02) on an object from a drawer rather than an audio concept. The reel
does not reach its own subject until 1:01.

## Choreography — what happens, and on which word

### B01 `BitSoundToNumbers` — the pipeline, then the fork

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.141 | "air pressure rising" | a wave draws itself left to right, its amplitude wandering on Perlin noise so it reads as a live signal |
| 0.244 | "microphone feels that movement" | a microphone appears mid-chain; its capsule lights |
| 0.401 | "list of numbers" | seven signed decimals land in a row, staggered, sampled from the wave above them |
| 0.581 | "How often should I" | QUESTION 1 card — *How often do I take a measurement?* → SAMPLE RATE |
| 0.742 | "how precisely should I" | QUESTION 2 card — *How precisely do I write each one down?* → BIT DEPTH |
| 0.967 | "the second one" | question 1 dims to 45%; a terracotta bar under question 2 reads THIS IS WHAT THIS VIDEO IS ABOUT |

Naming sample rate and then explicitly setting it aside is the whole job of this
beat. Every beginner conflates the two numbers, and a viewer who leaves thinking
bit depth controls "how often" has learned something false.

### B02 `BitStaircase` — a drawer object, then the same object on a sound

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.000 | "Think of a ruler" | a coarse ruler draws, four markings, captioned *you can only be roughly right* |
| 0.213 | "marked in millimetres" | a fine ruler draws beneath it — same length, sixteen markings, in terracotta |
| 0.512 | "how many markings" | the counter ticks 0 → 256 · MARKINGS AT 8-BIT |
| 0.757 | "land exactly on a marking" | a sound wave appears on the right and the ruler's markings become a ladder across it |
| 0.922 | "pushed to the nearest one" | every sample **snaps** to its nearest rung; the smooth original stays behind at 26% as a ghost |

Both rulers stay on screen while the wave snaps. The analogy is not a stepping
stone to be kicked away — it *is* the explanation, and a viewer who loses the
thread can look left and recover it.

**Honesty note, on screen:** the ladder draws sixteen rungs, not 256. At any
legible height 256 markings are a solid grey block. The frame says so in its own
caption rather than letting the viewer believe 8-bit means sixteen steps.

### B03 `BitGapIsHiss` — the causal chain, in four moves

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.079 | "slightly off" | one sample, its true position, and a terracotta drop to the marking it had to take — OFF BY THIS MUCH |
| 0.287 | "thousands of times every second" | the counter runs to 44,100 · *tiny on its own — not tiny all together* |
| 0.534 | "sound of their own" | the music thins to 30% and a live hiss trace appears beneath it, reseeded every 2 frames so it genuinely moves |
| 0.630 | "faint hiss" | A FAINT HISS, UNDER EVERYTHING |
| 0.788 | "coarser your ruler" | two cards: coarse ruler → louder hiss, fine ruler → quieter hiss, with traces at 4× different amplitudes |

The last stage is what makes the beat pay. It ties the ruler from B02 to the
loudness of the hiss, so "bit depth" and "how much noise" become one idea rather
than two facts.

### B04 `BitRoomUnderneath` — the one place this reel spends numbers

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.110 | "At eight bits" | the 8-bit floor travels down from full volume to −53 dB, live hiss riding it |
| 0.333 | "At sixteen bits" | the 16-bit floor travels to −101 dB; the shaded usable room above it is nearly twice as deep |
| 0.591 | "whisper and a rock concert" | the everyday yardstick lays itself out beside the axis, one row at a time |
| 0.790 | "quieter than the room" | a dashed line crosses the plot: THE ROOM YOU ARE SITTING IN |
| 0.960 | "never hear it" | the verdict lands |

Two numbers, not three. An earlier cut of this beat compared 8/16/24-bit with
per-bit brackets and step sizes in scientific notation, and Rohan cut it: *"These
are too detailed. Keep it high level."* What survived is the pair that carries
the decision, plus the room line — which is the only part a viewer can act on.

### B05 `HaiApplyCard` — the four-step answer

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.009 | "why does twenty-four exist" | the card's eyebrow and lede |
| 0.195 | "every edit rounds" | step 1 |
| 0.383 | "turn its hiss up" | step 2 |
| 0.660 | "record and edit in" | step 3 |
| 0.793 | "Export in sixteen" | the spark line |

### B06 `HaiTitleOutro` — `close` at 0.197

The HAI end card, not `ClaudeTitleOutro`. That component is locked to
@NikBearBrown by `OUTRO-LOCK.md` and silently ignores `handle` and `subline`, so
a reel for @HumanitariansAI that used it would end on the wrong channel.

## Emphasis discipline

Every new component routes its stage weights through `exclusive()` from
`cueKit`: each highlight **retires as the next one arrives**. Without it all five
stages of a beat are lit by its end, and the frame reads as five competing
emphases instead of a walkthrough.

## Continuous motion

No beat holds a still frame. A static graphic held for twenty seconds reads as a
screenshot, and the cheapest honest fix is to give every beat one thing that is
genuinely alive:

| Beat | What is always moving |
|---|---|
| B01 | the wave's amplitude wanders on `noise2D`; the samples re-read it every frame |
| B02 | nothing needs to — the snap is the event, and the rulers hold the frame |
| B03 | the hiss trace, reseeded every 2 frames, at both the music and the two comparison cards |
| B04 | live hiss at both floors, amplitude proportional to the floor |

## 9:16

Native portrait re-render via THE ONDA CHECK — `shorts.py` rewired all seven
beats to their `916` siblings, four of them written for this reel. Never a crop.

What actually changed, rather than shrank:

| Beat | Landscape | Portrait |
|---|---|---|
| B01 | wave → mic → numbers left to right; questions side by side | the chain runs top-down (it is a pipeline, so this reads truer); questions stack |
| B02 | rulers in a left column, the wave plot in a right one | rulers full width at top, plot full width beneath; ladder drops to 12 rungs so the rungs stay rungs |
| B03 | one error beside the rate that multiplies it | the rate sits directly *under* the error it multiplies; coarse/fine stay adjacent because they are a comparison |
| B04 | dB axis, two columns, yardstick in a third column | axis keeps its shape and gains height; the yardstick becomes right-aligned marginal notes inside the plot; the two numbers move to cards below it |

Content is confined to the active band y 230–1440; the top 12% and bottom 25%
belong to platform UI.
