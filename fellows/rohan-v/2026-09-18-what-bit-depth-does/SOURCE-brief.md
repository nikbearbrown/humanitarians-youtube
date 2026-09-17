# SOURCE-brief — "16-bit or 24-bit: What Bit Depth Does"

## What was asked for

Rohan asked for two more STEM reels for week-04, both audio:

> Great lets plan out 2 more videos for this week. use stem topics for both

and set the production bar:

> I want beautiful animations and nice motion graphics. Take as much time as you
> need. I want everything to be visually appealing. I want to keep the viewer
> hooked. So use as many visuals as you can so that the concepts are very easy
> for the viewer to understand.

Bit depth was chosen over three alternatives for one reason above all: **it is
measurable locally with no account and no network.** numpy can quantise a signal
and measure the error exactly, which means every number on screen could be
produced by experiment rather than recalled — the same discipline as the week-02
MP3 reel and the week-03 loudness reel.

The alternatives, and why they lost:

| Candidate | Why not |
|---|---|
| Sample rate / Nyquist | The interesting part is aliasing, which needs an audio demo the reel cannot play |
| Why AI music sounds "off" | Rests on published results rather than anything measurable here |
| Latency and buffer size | Measurable, but the payoff is a settings tweak, not an idea |

## What it was built from

An experiment run before the beat sheet existed. `measure_bitdepth.py` in this
folder; raw log [MEASUREMENTS.txt](./MEASUREMENTS.txt); method and limits
[SOURCES.md](./SOURCES.md).

| Claim on screen | Where it came from |
|---|---|
| −53 dB at 8-bit | measured error RMS, float64 numpy, undithered |
| −101 dB at 16-bit | measured error RMS, float64 numpy, undithered |
| 256 markings at 8-bit | 2⁸ |
| 44,100 times every second | the sample rate used in the measurement |
| coarser ruler → louder hiss | measured: a 256× coarser step raises the floor 47.6 dB |
| "roughly the gap between a whisper and a rock concert" | published everyday SPL tables, hedged in both narration and label |
| "quieter than the room you are sitting in" | a quiet domestic room at ~30 dB SPL against a normal playback level |
| 16-bit is a third smaller | 16 ÷ 24 |

## How the audience note shaped the build

Two corrections from Rohan did more to this reel than any design decision.

**First — the reel started too far in.**

> It starts out very abruptly. what is a person who knows nothing about audio
> going to understand? I want you to give some background. Explain it as if the
> viewer is new to the topic completely.

The original plan was ASK → BLUF → MECHANISM → COMPARISON → LIMIT → APPLY →
OUTRO: six beats that all assumed the viewer records audio. It was replaced with
BACKGROUND and ANALOGY beats, and the subject of the video now arrives at 1:01 of
2:07. Two whole beats — 43 seconds, a third of the runtime — are spent before
"bit depth" means anything more than a name.

**Second — the rewrite over-corrected.**

> Okay. and dont make the video too high level either. it has to be a good
> balance. at the end of the day the viewer has to learn somthing

The high-level rewrite had dropped the mechanism entirely and would have left a
viewer able to repeat "24 to work in, 16 to ship" without knowing why. B03 (the
leftover gap *is* a hiss) and one hard pair of numbers (B04) went back in.

What "too detailed" meant concretely, from the same review:

> These are too detailed. Keep it high level. Use details only where necessary.

| Cut | Why |
|---|---|
| a three-depth comparison with per-bit brackets (+47.7 / +48.8 dB) | three columns is a table; two is a decision |
| step sizes in scientific notation (7.81e-03 …) | true, logged, and meaningless to this audience |
| a log-scale gap-size chart | needed a paragraph to explain its own axis |
| a fade-out demo beat | a fifth beat making the same point B03 and B04 already make |

## What the measurement changed about the reel

The first attempt measured with `ffmpeg` + `volumedetect` and reported `-inf`
for 24-bit. That looked like a spectacular result and was a tool artefact:
ffmpeg's filter graph is 32-bit float internally, so a 24-bit round trip is
lossless *to ffmpeg*. Rewriting the measurement in float64 numpy produced a real
number (−149.56 dBFS) — and then that number was cut from the reel anyway for
being one comparison too many. It is in the log, not on screen.

The second thing the measurement changed: it confirmed **5.95 and 6.10 dB per
bit**, which is how the 8-vs-16 comparison could be made without hand-waving. The
per-bit figure itself was also cut as too much detail.

## What was deliberately excluded

- **Dither.** A second mechanism on top of the first, and a viewer who has just
  met rounding cannot hold "and now we add deliberate noise to improve it".
- **Sample rate beyond naming it.** Named once, set aside deliberately, deserves
  its own reel.
- **32-bit float.** A better answer to B05's question than 24-bit, and needs its
  own five minutes.
- **Any claim that 24-bit sounds better to a listener.** It does not, and B05
  says so.

## Constraints inherited from earlier weeks

| Source | Rule | Applied |
|---|---|---|
| Week-01 review | identical opener/closer across reels | `ClaudeComposerAsk` → `HaiTitleOutro` |
| Week-01 review | name Humanitarians AI in intro and outro | B00 opens with it, B06 closes with it |
| Week-02 review | name phonetic in narration only | `Row-Haan VeeJayKooMaar`; on-screen spelling correct |
| Week-02 review | 9:16 native re-render, never a letterbox | four new `916` siblings |
| Week-03 build | no personal references in narration | none |
| Toolkit doctrine | library-first | four searches, four genuine misses, all logged |
| Toolkit doctrine | audio-first | Kokoro durations are the master clock throughout |
