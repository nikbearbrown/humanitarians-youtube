# SOURCE-brief — "Why Your Track Sounds Thin On A Phone"

## What was asked for

Rohan asked for two more STEM reels for week-04, both audio:

> Great lets plan out 2 more videos for this week. use stem topics for both

and set the production bar:

> I want beautiful animations and nice motion graphics. Take as much time as you
> need. I want everything to be visually appealing. I want to keep the viewer
> hooked. So use as many visuals as you can so that the concepts are very easy
> for the viewer to understand.

Mono fold-down was chosen for three reasons:

1. **It is measurable locally.** numpy can build a stereo signal with a known
   inverted layer, and ffmpeg can measure what the fold-down does to it — so
   every figure on screen is an experiment rather than a recollection.
2. **It can be *predicted* and then measured.** The delay case has a closed-form
   answer (nulls at odd multiples of 1/2d). Writing the prediction down first and
   then landing on it is the strongest form of evidence available at this scale.
3. **The symptom is one most people have actually experienced** — a track that
   sounds fine in headphones and thin on a phone — which gives B00 a real
   question to ask rather than a manufactured one.

The alternatives, and why they lost:

| Candidate | Why not |
|---|---|
| Room modes / standing waves | Needs a room and a mic to measure; not reproducible on this machine |
| Why AI music sounds "off" | Rests on published results rather than anything measurable here |
| Clipping vs limiting | Measurable, but too close to the week-03 loudness reel |

## What it was built from

Two experiments, run before the beat sheet existed. `build_mono_signals.py` in
this folder; raw log [MEASUREMENTS.txt](./MEASUREMENTS.txt); method and limits
[SOURCES.md](./SOURCES.md).

| Claim on screen | Where it came from |
|---|---|
| bass, centre, **unchanged** | measured −13.4 → −13.4 dB |
| vocal, centre, **unchanged** | measured −16.2 → −16.2 dB |
| wide layer, spread, **−49.5 dB** | measured −17.0 → −66.5 dB |
| "only certain frequencies cancel" | predicted nulls at 833/2500 Hz, then measured −10.2 and −9.8 dB there, with peaks intact at 1660 and 3300 |
| "holes, not silence" | the nulls measured ~−10 dB, not −∞, for two stated reasons |
| "most stereo width is one side arriving a fraction late" | the common widener design, and the signal Case 2 models |

## How the audience note shaped the build

The same two corrections that reshaped the sibling reel applied here.

**First — start from the scenario, assume nothing.**

> Do the same for the other video as well. Make sure it is understood by a
> general audience. Explain the scenario where one might encounter such a topic

The original plan opened on two waves being added. It now opens on a lived
symptom (*full in headphones, thin on a phone*) and spends a whole beat on the
fact that recorded music has two sides at all, and that headphones deliver them
separately while a phone cannot. The word "cancel" does no real work until B02.

**Second — but the reel still has to teach.**

> Okay. and dont make the video too high level either. it has to be a good
> balance. at the end of the day the viewer has to learn somthing

So the measured evidence stayed (B03) and the honest caveat stayed (B04). What
went was the detail inside them.

What "too detailed" meant concretely:

| Cut | Why |
|---|---|
| the comb-notch frequency table (400/830/1660/2500/3300 Hz with predictions) | the best result in the reel, and unusable by a beginner. B04's axis now reads LOW NOTES → HIGH NOTES with no numbers |
| per-row live waveforms in B03 | three waveforms plus three bars plus three positions is three things too many |
| a three-column before/after comparison | position and outcome is the whole argument |
| a phase-meter / correlation explainer | a second vocabulary the reel cannot afford |

## What the measurement changed about the reel

**It produced the word "holes".** The prediction was that certain frequencies
would cancel; what the measurement actually showed was nulls at about −10 dB
rather than −∞, for two specific and legitimate reasons (a 120 Hz analysis band,
and a broadband rather than tonal source). That result is what B04's title and
its whole framing come from. A cleaner −∞ would have produced a worse reel,
because "silence" is not the symptom anyone actually hears.

**And it cost a first pass to a tool footgun.** `volumedetect` prints at
ffmpeg's info level, so the first run — written with `-v error` — returned
nothing at all. Recorded in [BUILD-LOG.md](./BUILD-LOG.md) and in
MEASUREMENTS.txt, because it will happen to someone else.

## What was deliberately excluded

- **Mid/side, correlation meters, phase scopes.** The right professional tools,
  and a second vocabulary.
- **Haas effect and precedence.** Why a delay reads as width at all. Its own
  reel.
- **DAW-specific fixes.** The reel names the culprits and stops; plugin settings
  date instantly.
- **Any suggestion that stereo width is bad.** B01 says the difference between
  the sides *is* the width. The point is only that one speaker cannot deliver it.

## Constraints inherited from earlier weeks

| Source | Rule | Applied |
|---|---|---|
| Week-01 review | identical opener/closer across reels | `ClaudeComposerAsk` → `HaiTitleOutro` |
| Week-01 review | name Humanitarians AI in intro and outro | B00 opens with it, B06 closes with it |
| Week-02 review | name phonetic in narration only | `Row-Haan`; on-screen spelling correct |
| Week-02 review | 9:16 native re-render, never a letterbox | four new `916` siblings |
| Week-03 review | no mojibake in portrait cuts | both short beat sheets byte-checked |
| Week-03 build | no personal references in narration | none |
| Toolkit doctrine | library-first | four searches, four genuine misses, all logged |
| Toolkit doctrine | audio-first | Kokoro durations are the master clock throughout |
