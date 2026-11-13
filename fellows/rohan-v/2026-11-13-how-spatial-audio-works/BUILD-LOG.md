# BUILD-LOG — "How Spatial Audio Works"

What broke, what it cost, and what changed because of it. Built 2026-11-09 to 11-10 for the week of 9–13 Nov,
alongside this week's Netflix reel. B01–B06 are HyperFrames compositions with three.js scenes; B00, B07 and B08 are
the channel's Remotion cards.

## 1 — Evidence: a textbook head small enough to check

Apple hasn't published how its renderer works, so `spatial.py` builds the textbook version and measures it: a rigid
sphere 8.75 cm in radius (the classic radius, fact sheet §1.4), 48 kHz, sound at 343 m/s. Each ear gets Woodworth's
spherical-head timing formula as a fractional delay (a windowed-sinc filter), and the Brown-Duda one-pole/one-zero
head-shadow filter that dims the far ear's highs; an optional outer-ear stand-in cuts some highs for sounds from
behind. The measurements use a one-second broadband noise burst; the listening clips use a Karplus-Strong
plucked-string melody, Western in style per Rohan's standing preference for STEM test material: 16 notes of half a
second on an A minor pentatonic line. Everything is seeded (1113) and in NumPy and SciPy.

What the run measured (`evidence/run.log`):

- **Timing**: 0.000 ms straight ahead rising to 0.661 ms at 90°, from the cross-correlation of the rendered ears;
  the formula gives 0.656 ms.
- **Level** at 90°: 2.3 dB in a 350–700 Hz band, 14.0 dB in a 3–6 kHz band.
- **Front/back**, 30° against 150°: the head alone gives 0.266 vs 0.266 ms and spectra 0.00 dB apart; with the
  outer-ear filter they differ by 2.6 dB.
- **Head tracking**, a 40° turn: without tracking the sound is rendered at 0° from your nose and turns with you;
  with tracking it is rendered at −40° and stays put.
- **Listening**: `circle.wav`, 8.0 s, one turn around the head with the outer-ear filter on (azimuth = 360° ×
  time ÷ 8 s, starting ahead, turning right), plus front/back pairs with and without the outer-ear filter.

Sanity checks on the run:

- **"Exactly the same"** front and back is true *by construction*: a symmetric sphere with ears at opposite points
  can't tell a source from its mirror. The run confirms the code; the narration says "in my model". The 2.6 dB is
  also by construction, from my own stand-in filter, not a measured outer ear.
- **"About two thirds of a millisecond"** is the sphere's 0.661 ms, inside the published 630–763 µs range for real
  heads (§1.5), so the narration doesn't give one exact real-head value.
- **"Fourteen decibels"** is milder than real heads (about 20 dB at 4 kHz, §1.7); the narration says "in my model".
- **Section 4 measures nothing.** It states the geometry of a 40° turn, which B05 draws.
- **The circling clip first had no outer-ear filter**, so its back half gave the ears the same cues as its front
  half: exactly the ambiguity B03 teaches. It is now rendered with the filter on (`use_pinna=True`), so the half
  of the turn behind the ears gets the outer-ear cut and differs from the front half. Re-running `spatial.py`
  left every measured number in `run.log` unchanged; only the LISTENING line now says "outer-ear filter on".
  It is still a textbook model, untested with listeners (FEEDBACK §1).

## 2 — Script

Nine beats, authored by `author_sheet.py` into `beat_sheet.json` and `cues.json`. Every spoken number is the run's
(B01–B03) or from `week-12/_research/facts-spatial.md` (Rayleigh 1907; 710 directions; head tracking in 2020;
Personalized Spatial Audio). Each measured number is introduced with "in my model" or "in my head model". Apple is
credited only with what it has said; the script never says how Apple renders, and the docs never say Apple uses
HRTFs by that name (Apple doesn't use the term, §2.8). The name is spelled phonetically in the narration,
"Row-Haan"; "Rohan V." on screen. The title is plain: "How Spatial Audio Works".

## 3 — Audio, and the stereo listening clip

- **Narration**: Kokoro `af_bella`, nine beats, 0 fallbacks in the word clock (`_audio.log`). B04's narration is
  17.75 s.
- **The listening clip** (`mix_listen.py`, run by `run_audio.sh <reel>` after `align.py` and before `sync_cues.py`):
  B04's mono narration is copied to both channels, then a 0.6 s pause, then `circle.wav` exactly as `spatial.py`
  rendered it, set to the narration's RMS level (+3.7 dB for the outer-ear version; +3.1 dB before it) with 20 ms
  and 30 ms edge fades, then a 0.8 s tail. After the clip was re-rendered, `run_audio.sh` rebuilt
  `beat-B04-listen.mp3`, still 48 kHz stereo, and every beat duration stayed the same (128.22 s in all).
  Stereo throughout, 48 kHz, 192 kbit/s, because the binaural cue lives in the difference between the left and
  right channels: a mono mix would erase it. The mixed file `mp3/beat-B04-listen.mp3` became B04's `audio_file`;
  the beat was re-measured at 27.15 s, and the clip's window (18.349–26.349 s) went into the beat's `listen_clips`
  and `props.listen`, which B04's scene uses to sync the orbit.
- **The compile has to stay stereo** for the same reason: the final cut must keep two channels, or the clip in B04
  turns into a plain melody in the middle of your head.
- **A cue that didn't resolve.** `sync_cues.py` couldn't find the anchor "dummy head": the narration says "dummy
  head's", and the apostrophe broke the match (`_audio.log`: "NOT FOUND -> dummy='dummy head'"). The anchor is now
  "inside a dummy", and the cue resolves (0.0786 of the beat).
- `run_audio.sh` then writes `props.durationSeconds` into every beat, so each scene plays on its measured clock.

## 4 — HyperFrames + three.js build

Rohan chose HyperFrames for both of this week's videos, then asked for three.js and "beautiful motion designs".
Claude recommended three.js for the 3D stage and keeping the HUD in HTML, where text stays sharp and the gates can
read it; Rohan approved downloading three.js 0.187.0 (MIT), vendored in `week-12/_vendor`; it ships inside this folder as
`hyperframes/assets/three.module.min.js` and `three.core.min.js`, with its licence as `three-LICENSE.txt`.

- **One composition per beat and aspect**: `hyperframes/B0x-l.html` (3840×2160) and `B0x-v.html` (2160×3840),
  written by `build_hf.py` with the shared week kit (`hfkit.py`, `kit3.js`, `add_qc.py`, `vertical_strings.py`),
  which ships in this folder as `_kit/`; `build_hf.py` looks there first, then in `week-12/_kit/`. Each page has a WebGL canvas drawn by
  `hyperframes/scenes/B0x.js` through `assets/kit3.js`, and an HTML HUD revealed by a paused GSAP timeline on the
  beat's word-clock cues.
- **Seek-safe**: every three.js frame is drawn from timeline time alone (HyperFrames seeks each frame
  independently): no clocks, no `requestAnimationFrame`, seeded randomness only.
- **Design decisions**: the listener is the textbook spherical head (a glass sphere with two ears and a small
  nose), never a person; sound is amber light, the right ear cyan and the left ear violet throughout, in 3D and in
  the HUD. B04's orbiting source is synced to `circle.wav`: azimuth = 360° × time ÷ 8 s from the clip's start,
  starting ahead, turning right; the dial and "NOW FROM" follow it.
- **Data**: the HUD numbers and the B01 chart come from `evidence/scene.json`; the filter curves in B03 and B04 are
  `spatial.py`'s own filters, evaluated in `build_hf.py` with the same constants.
- Rendered into `media/B0x.mp4` (16:9) and `pantry/B0x-916.mp4` (9:16), where the Brutalist compiler picks them up
  like any beat clip. Temporary frames go to `D:/Rohan/Claude/HyperFrames/tmp`, never C:.

## 5 — Snapshot review fixes

Snapshots of every beat in both aspects (`_snap/`) were looked at before the 4K renders. What they found, and the
fix:

- **Overlapping HUD panels in landscape.** The panels are now laid out as one evenly spaced column, in both aspects.
- **Phone titles wrapping into the 3D stage.** Shorter phone titles ("Your Head's Shadow", "Every Direction") and a
  smaller phone title size.
- **Text running past the right edge.** Shorter labels, and logo tags that wrap.
- **B03's cone-of-confusion camera hid the behind source.** The camera now looks down from above, so both sources
  and the cone read.
- **B06's phone was invisible against the dark ground** during the ear scan. It is now drawn with a lit metal rim
  and a glowing camera lens.

The phone layout follows Rohan's rule from week 11: no overlapping panels or text on the phone; if it doesn't fit,
remove text from the bottom and use the room to space the panels. On the phone, the closing notes of B01, B02, B04
and B06 are dropped.

Gate pre-check (`week-12/hfgate.py`: 4K frames of the rendered clips at 50%, 85% and 97% of each beat, through
Gate V's frame check and GATE T's size, contrast and overlap tests; frames in `_gate/`):

- **The CSS ground gradient counted as ink past the title-safe left edge.** The gradient was re-centred and
  darkened.
- **A few labels were under the 4K size floor.** All HUD type is now at least 0.9× the label size.
- **One phone panel ran past the bottom inset** (B02's "use timing / use loudness" card). That card is dropped on
  the phone; the two panels above already say it.

## 6 — Fact-check fixes in the film

The first fact check flagged four things on screen and in the clip; all four were changed in the film:

- **B06's "3200 POINTS" counter** counted the points in the drawn ear, a number no source supports. Removed; the
  scan card's second line now reads "THE SHAPE OF YOUR EAR".
- **B06's landscape spark line**, "Your ears, measured, make the filters yours.", came close to claiming that Apple
  measures your HRTF (fact sheet §4.7). It now reads "An ear scan builds a profile just for you."
- **B04's chart title**, "ONE FILTER PAIR · 60° RIGHT", didn't say the curves are my model's. It is now "MY
  MODEL'S FILTER PAIR · 60° RIGHT" in both cuts.
- **The circling clip** gained the outer-ear cue for its behind half (§1 and §3 above).

Dolby is named on B07's standard apply card without a mark; the card has no logo slot, so it stays a FEEDBACK
question. GATE F's content check (`runtime/qc/factcheck_check.py`) on this folder: exit 0, 36 rows, every beat
covered.

## Renders and gates

All six body beats were rendered with HyperFrames 0.8.43 (`hfkit.render`: `-q delivery --workers 2`, frame cache on
D:, about 3–4 minutes a clip): `media/B0x.mp4` at 3840×2160 and `pantry/B0x-916.mp4` at 2160×3840. B00, B07 and B08
were rendered by `remotion_scenes.py` in both aspects. `./art vertical` built the phone sheet from the pantry clips;
`_kit/vertical_strings.py` set the phone apply-card strings and `_kit/add_qc.py` wrote the Gate V declarations.
Before the finals, `hfgate.py` checked every clip at 50%, 85% and 97% of its beat (Gate V with the declared
regions, GATE T size/contrast/overlap, and the overlap test again with the 3D stage masked).

**Passes after the first renders (each found by looking at frames, then re-rendered):**
- The phone column was full on seven beats (18 px gaps; two ran past 0.86 H). Per Rohan's phone rule the 3D stage
  shrank to 0.14–0.44 H, the column starts at 0.455 H, and bottom items were dropped on the phone where they did not
  fit (B03's head-only chart — the two cards already say "same"; B06's FRONT ⇄ BEHIND row); B02's phone numbers and B05's phone card lines are smaller. Measured again in a browser: every phone column now has 37–146 px between panels and ends above 0.86 H.
  All twelve phone clips were re-rendered and both vertical finals rebuilt.
- The column layout now re-runs once the web fonts load and on every seek (heights are measured as rendered).
- B04's landscape clip had been rendered from the page before the chart title change ("MY MODEL'S FILTER
  PAIR"); it was deleted and re-rendered before the landscape final.
- The master is 48 kHz stereo and keeps the binaural clip: in B04's clip the right channel leads by ~6 dB
  while the sound passes the right side, then the left leads (measured on the master).

**Finals** (`./art final <reel> --height 2160`, `./art final <reel>/vertical --height 3840`):

| Cut | File | Size | Duration | SHA-256 | Receipt |
|---|---|---|---|---|---|
| 16:9 | `spatial-audio-explainer.mp4` | 64.7 MB | 128.38 s | `1e28a65a4e0fdca79227d4f9a8f74bb50a7cff819b92a33848cd5769bbfbe39b` | ready, 2026-11-10 07:19 UTC |
| 9:16 | `vertical/spatial-audio-explainer-vertical.mp4` | 55.0 MB | 128.38 s | `fdc936eb09b84ffeaf2f3055c1e0f82e9d1c554a7e0ba158ad4657df42ab5d55` | ready, 2026-11-10 08:20 UTC |

GATE F (`factcheck_check.py`): clean. GATE T: PASS on both cuts ([TYPECHECK.md](./TYPECHECK.md)). Gate V: passed
(receipt `ready`), with title + HUD contrast regions declared on B01–B06. QC sheets:
[`qc-sheet-16x9.png`](./qc-sheet-16x9.png), [`qc-sheet-9x16.png`](./qc-sheet-9x16.png).
