# BUILD-LOG — "What MP3 Throws Away"

Built 2026-09-04 as the STEM half of the week-02 submission. What actually
happened, in order.

## 1 — Topic selection

Rohan asked for an audio/music topic and then asked for suggestions. Three were
proposed: lossy compression, why AI music sounds "off", and loudness
normalisation. He picked lossy compression.

It was the recommended one for a reason that shaped the whole build: **it is
the only one of the three whose every claim can be measured locally in
minutes.** The other two would have rested on recalled facts.

## 2 — The experiment, before the script

Rather than write the beat sheet and then look for numbers to support it, the
measurements were taken first.

```bash
ffmpeg -f lavfi -i "anoisesrc=d=10:c=white:r=44100:a=0.5" -ac 2 -c:a pcm_s16le src.wav
ffmpeg -i src.wav -c:a libmp3lame -b:a 128k enc_128.mp3     # and 320k
ffmpeg -i enc_128.mp3 -c:a pcm_s16le dec_128.wav
ffmpeg -i dec_128.wav -af "bandpass=f=17000:width_type=h:w=500,volumedetect" -f null -
```

White noise because a flat source spectrum makes the encoder's decisions
legible — anything missing afterwards was removed, not absent. Decoded before
measuring, because measuring the bitstream would not describe what a listener
receives.

**Results** (full log in [MEASUREMENTS.txt](./MEASUREMENTS.txt)):

| | source | 128 kbps | 320 kbps |
|---|---|---|---|
| 16 kHz | −33.1 | −33.7 | −33.1 |
| 17 kHz | −34.0 | **−47.2** | −34.0 |
| 19 kHz | −36.4 | −58.7 | −36.4 |
| 20 kHz | −38.3 | −63.5 | −41.8 |

128 kbps has a hard cliff at 16 kHz. 320 kbps is identical to source through
19 kHz. Compression: 10.96 : 1 and 4.38 : 1 from real byte counts.

**Generation loss**, measured by re-encoding the decoded 128 kbps file ten more
times: the 12 kHz band goes −31.1 → −33.3 → −34.7 → −37.8 dB at 1 / 4 / 6 / 11
encodes. Monotonic. Nothing recovers.

### One line did not survive the data

A drafted B03 said 320 kbps "keeps everything." The measurement showed 20 kHz is
3.5 dB down, so it became "survives intact all the way to nineteen" — which is
what was observed. This is the whole argument for measuring first.

## 3 — Library-first gate

`./art scenes` run for both visual needs before authoring. Closest candidates
and why they failed are in [PROMPTS.md](./PROMPTS.md); both genuine punts.

Also checked the week-00 reel "What a Spectrogram Shows" for anything
inheritable — it used **reel-local Manim scenes**, not shared Remotion
components, so there was nothing in the library. Built in Remotion anyway, which
keeps the portrait path exact: `shorts.py` re-lays-out Manim beats, whereas a
`916` sibling gives full control.

## 4 — Eight components authored

Four landscape under folder `lossy-audio-explainer`, plus a native portrait
sibling for each. Every sibling re-exports the landscape schema
(`export const fooBar916Schema = fooBarSchema`) so props are identical and the
beat sheet carries no format-specific content — standing rule #4, and the
lesson from the `items`-undefined failure in the previous reel.

Spectrogram cells come from a deterministic hash of position rather than a
random number: no frame-to-frame shimmer, and re-running the build produces an
identical picture so QC sheets can be compared across builds.

## 5 — Audio (the master clock)

```
B00 18.60   B01 21.72   B02 22.44   B03 23.70
B04 21.12   B05 22.06   B06 10.13
```

Total **139.77s = 2:19**, against the 2:21 stem-separation sibling. Cost $0.00.
No beat was re-recorded — the per-beat word budget held on the first pass.

Name spelled phonetically in `narration_text` (`Row-Haan VeeJayKooMaar`); every
on-screen string keeps the correct spelling.

## 6 — Visual QC caught three fill defects

Rendered, compiled a review cut, read the QC sheet, then pulled
full-resolution frames of each new scene. Three defects, all the same class and
all invisible to a probe:

| Beat | Defect | Fix |
|---|---|---|
| B01 | Plot occupied 27–71% of frame height; ~160px dead between caption and spark line | `PLOT_H` 0.44 → 0.505, `PLOT_Y` 0.27 → 0.255 |
| B02 | Plot floated in the upper two thirds; the loud tone did not reach the top of its own plot area | `PLOT_H` 0.45 → 0.555, tone heights 0.78 → 0.86 |
| B04 | Step labels hang ~110px below the lowest rung, leaving ~200px dead at the bottom | `PLOT_H` 0.40 → 0.465 |

All three are FILL-THE-CANVAS violations: *"accidental dead space under
undersized content is the defect this law kills."* None would have been caught
by checking dimensions or duration — only by looking at a frame.

## 7 — The vertical cut

`shorts.py --no-endcard`, which rewired all seven beats to their `916` siblings
on the first run — the ONDA CHECK bug fixed during the previous reel is holding.
`--no-endcard` because B06 is already a branded outro and skipping the silent
card keeps both cuts the same length.

Portrait is genuinely the better frame for two of these beats: the spectrogram
gets height, which is the axis it wants, and the generation-loss steps descend
vertically so gravity does the explaining.

## 8 — Delivery

Docs and both QC sheets to GitHub; the two mp4s to Drive via `./art drive`,
which is now a standing step in every build.

## Outputs

```
2026-09-04_what_mp3_throws_away_16x9.mp4   3840×2160   139.77s
2026-09-04_what_mp3_throws_away_9x16.mp4   2160×3840   139.77s
```

## Toolkit changes

None. Every bug fixed during the previous reel — five cp1252 encoding faults and
the swallowed-exception in `shorts.py` that silently disabled the ONDA CHECK —
held for this build. `scene_search.py`, `build_scene_index.py`, `compile.py --review`
and `shorts.py` all ran clean on the first attempt, which is the first time that
has happened on this machine.
