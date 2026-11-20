# BUILD-LOG — "How Bluetooth Audio Works"

What broke, what it cost, and what changed because of it. Built 2026-11-19 for the week of 16–20 Nov, alongside
this week's Auto-Tune reel. Rohan V. chose the topic, chose HyperFrames + three.js again for both of the week's
videos, and gave 20 hours for the week. B01–B06 are HyperFrames compositions with three.js scenes; B00, B07 and
B08 are the channel's Remotion cards.

## 1 — Evidence: real encoders, a simulated link

No company's Bluetooth stack is available to measure, so `bluetooth.py` does two things. Part 1 uses real
encoders: a synthetic pop track (drums, bass, piano chords, a lead, with human timing; 60 s, 44.1 kHz, 16-bit
stereo), Western in style per Rohan's standing preference for STEM test material, encoded with ffmpeg's SBC (the
High Quality setting, 328k), aptX, aptX HD and AAC (ffmpeg's own encoder at 256k, not Apple's), with each data rate
measured from the encoded bytes. Parts 2 and 3 are a simulation of an A2DP link, not a measurement of any radio:
120 s; packets of 14.5 ms of music (5 SBC frames); one try every 3.75 ms (a 5-slot packet and its 1-slot reply),
each on a new channel of 79; a Wi-Fi network on channels 24–46 (23 of 79), busy 55% of the time in bursts; 16
body-blocking moments of 60–320 ms (a phone in a pocket as you turn); a 1% random error elsewhere; failed tries
re-sent until the packet is too late to play; the headphones play each packet a fixed buffer time after its music
began. Seeded (1119 and 77 for the track, 2402 for the radio); NumPy, SciPy and ffmpeg.

What the run measured (`evidence/run.log`):

- **Too much data**: CD quality = 44,100 × 16 bits × 2 channels = 1,411.2 kbit/s. SBC 330.7 kbit/s (1/4.3 of CD),
  aptX 352.8 (1/4.0), aptX HD 529.2 (1/2.7), AAC 272.1 (1/5.2; ffmpeg's encoder set to 256k).
- **The radio**: 267 tries/s for 69 packets/s. Without adaptive hopping 22.1% of tries lost (17.4% outside the
  body-blocking moments); with adaptive hopping 7.6% (0.9% outside them).
- **The buffer** (adaptive hopping on, 120 s): 20 ms 103 glitches (3,643 ms of music missing); 50 ms 30 (1,553 ms);
  100 ms 19 (755 ms); 150 ms 9 (261 ms); 200 ms 3 (44 ms); 300 ms 0.
- **Listening**: window 2.0–8.0 s of the track; `small_buffer.wav` (50 ms buffer) 2 glitches, `large_buffer.wav`
  (200 ms) none: the same moments, 200 ms later.

Sanity checks on the run, and what they changed:

- **A quality column that ranked the codecs unfairly.** The first table scored each codec by waveform SNR against
  the original. A waveform match punishes codecs built around hearing (they discard what you can't hear, which a
  waveform match counts as error), and aligning aptX's output with the original for the comparison failed. With no
  listening test to replace it, the column was dropped; `run.log` says why, and the film makes no quality ranking.
- **A cutoff column that didn't discriminate.** The highest frequency each codec kept was measured too; it didn't
  separate the codecs, so it was dropped.
- **The listening window was picked as typical, not dramatic**: the 6 s whose 50 ms glitch count is closest to that
  buffer's average rate (2 glitches against 1.5 expected). `mix_listen.py` plays 1.5–5.5 s of it, where the two
  glitches (0.13 s apart, inside one body-blocking moment) are heard as one stutter about 2.1 s in.
- **Where the failures come from** (found by the fact check, §2): 26% of the failed tries without adaptive hopping,
  and 90% with it, fall inside the body-blocking moments. Wi-Fi alone predicts 23/79 × 55% ≈ 16%, plus the 1%
  random error ≈ 17%; the run gives 17.4% outside body blocking, and 0.9% (the random error) once hopping skips the
  Wi-Fi channels. So B02 uses the Wi-Fi-only figures.

## 2 — Script

Nine beats, authored by `author_sheet.py` into `beat_sheet.json` and `cues.json`; later edits went into the sheet.
Every spoken number is the run's (B01, B02, B04) or from `week-13/_research/facts-bluetooth.md` (79 channels, up to
1,600 hops, aptX about 350, LDAC up to 990, a couple of hundred milliseconds, LC3 at half the bit rate). The run's
numbers are introduced with "my test track" and "my simulation"; company claims are attributed. The name is spelled
phonetically in the narration, "Row-Haan"; "Rohan V." on screen. The title is plain: "How Bluetooth Audio Works";
the handoff name is `BluetoothAudio_RohanV`.

The fact-check pass (an independent Claude agent, against the fact sheet, `evidence/` and a web check of four
claims; FACTCHECK) held three claims in this reel; all were re-voiced on 2026-11-19, with other lines reworded in
the same pass:

- **B02.** "…twenty-two percent of tries failed … under eight percent" included the body-blocking moments, which
  B02 never mentions. Now the Wi-Fi-only figures: "a busy Wi-Fi network made seventeen percent of tries fail.
  Adaptive hopping skips the busy channels: about one percent." The HUD draws the same figures (`loss_quiet`: 17%,
  0.9%); the cues now anchor on "seventeen" and "about one".
- **B03.** "Apple's devices use AAC" said they always do; they fall back to SBC when the headphones lack AAC. Now
  "Apple's devices **prefer** AAC"; the HUD tag reads "APPLE DEVICES PREFER AAC".
- **B06.** "The newest version, LE Audio" made LE Audio a version of Bluetooth; it isn't. Now the SIG's own framing:
  "Bluetooth's next generation, LE Audio, brings a new codec called LC3."
- Also reworded: **B01** "under a quarter" (SBC is 23% of CD); **B04** "Lost packets, from Wi-Fi or your own body,
  get sent again", so B02's Wi-Fi-only numbers and B04's glitches agree, and "That reserve is **the main reason**
  Bluetooth lags" (not the only one); **B04** and **B05** trimmed for length ("Listen: small, then big.").

## 3 — Audio, and the listening clips

- **Narration**: Kokoro `af_bella`, nine beats, all aligned by `align.py` with 0 fallbacks (`_audio.log`); all 53
  cue anchors in `cues.json` resolved. B04's narration is 20.39 s.
- **The listening clips** (`mix_listen.py`, run by `bash ../run_audio.sh <reel>` after `align.py` and before
  `sync_cues.py`): B04's narration, then a 0.6 s pause, then 4 s of `small_buffer.wav` and 4 s of
  `large_buffer.wav` (both from 1.5 s into the 6 s window, 0.7 s apart), exactly as `bluetooth.py` rendered them,
  each set to the narration's RMS level (−1.8 dB), then a 0.8 s tail. Stereo, 48 kHz, 192 kbit/s. The mixed file
  `mp3/beat-B04-listen.mp3` became B04's `audio_file`; the beat was re-measured at 30.49 s, and the two windows
  (20.995–24.995 and 25.695–29.695 s) went into the beat's `listen_clips` and `props.listen`, which B04's scene uses
  to drain the two reservoirs in real time during each clip.
- `run_audio.sh` then writes `props.durationSeconds` into every beat, so each scene plays on its measured clock.
  Nine beats, 146.30 s in all (about 2:26).

## 4 — HyperFrames + three.js build

Rohan chose HyperFrames with three.js again for both of this week's videos. three.js 0.187.0 (MIT; the version
approved in week 12) is vendored in `week-13/_vendor` and ships inside this folder as
`hyperframes/assets/three.module.min.js` and `three.core.min.js`, with its licence as `three-LICENSE.txt`.

- **One composition per beat and aspect**: `hyperframes/B0x-l.html` (3840×2160) and `B0x-v.html` (2160×3840),
  written by `build_hf.py` with the shared week kit (`week-13/_kit/`: `hfkit.py`, `kit3.js`, `add_qc.py`,
  `vertical_strings.py`); `build_hf.py` looks for `_kit/` in this folder first, then in `week-13/_kit/`, and copies
  `kit3.js` into `hyperframes/assets/` only when it has changed (file times drive re-renders). Each page has a WebGL
  canvas drawn by `hyperframes/scenes/B0x.js` through `assets/kit3.js`, and an HTML HUD revealed by a paused GSAP
  timeline on the beat's word-clock cues.
- **Seek-safe**: every three.js frame is drawn from timeline time alone: no clocks, no `requestAnimationFrame`,
  seeded randomness only.
- **Design decisions**: "the radio sky" (near-black blue); music violet, the link blue, Wi-Fi orange, a try that
  gets through green and a lost one red throughout, in 3D and in the HUD. B02's hops are the simulation's own tries
  (the first 160 of the listening window, with and without adaptive hopping); B04's reservoir levels are the run's
  own, every 10 ms of the same 6 s window the clips come from, at half speed during the narration and in real time
  during each clip. B05 and B06 are illustrations: B05's delay is drawn at 250 ms, inside the 170–370 ms of the two
  published tests on its HUD; B06's broadcast rings are seeded, with no data.
- **Logos** (LOGO LAW): Apple, Android and ffmpeg marks from the toolkit's `icons/logos/` (B01's ffmpeg tag, B03's
  Apple and Android tags). The toolkit has no Bluetooth SIG, Qualcomm or Sony mark, and none was downloaded
  (FEEDBACK §3).
- Rendered by `build_hf.py --render` into `media/B0x.mp4` (16:9) and `pantry/B0x-916.mp4` (9:16), where the
  Brutalist compiler picks them up like any beat clip. Temporary frames go to `D:/Rohan/Claude/HyperFrames/tmp`,
  never C:.

## 5 — Snapshot review fixes

Snapshots of every beat in both aspects (`_snap/`, `../snap.sh`) were looked at before the 4K renders. What they
found, and the fix:

- **3D labels outside the stage.** Labels pinned to 3D points could show over the HUD when their point left the
  stage. `kit3.js` `pin` now hides a label whose point is outside the stage (both reels).
- **B04's tank labels overlapped on the phone** ("50 ms", "200 ms", "GAP"); fixed so they no longer collide.
- **Long bar labels** were shortened.

The phone layout follows Rohan's rule from week 11: no overlapping panels or text on the phone; if it doesn't fit,
remove text from the bottom and use the room to space the panels. On the phone, B01's CD sum, B03's measurement
note and B04's closing note are dropped.

## Renders and gates

All six body beats were rendered with HyperFrames 0.8.43 (`hfkit.render`: `-q delivery --workers 2`, frame cache on
D:, about 3–4 minutes a clip): `media/B0x.mp4` at 3840×2160 and `pantry/B0x-916.mp4` at 2160×3840. B00, B07 and B08
were rendered by `remotion_scenes.py` in both aspects. `./art vertical` built the phone sheet from the pantry clips;
`_kit/vertical_strings.py` set the phone apply-card strings and `_kit/add_qc.py` wrote the Gate V declarations.
Every clip was pre-checked by `week-13/hfgate.py` at 50%, 85% and 97% of its beat as it landed (Gate V, GATE T
size / contrast / overlap).

**Render passes.** The first render attempt (launched through the hidden-window helper) was cancelled by HyperFrames
(`render_cancelled_parent_exited`) on the first clip of each reel; renders were re-launched from the background shell.
Clips whose pages changed after the pre-check were re-rendered; a clip whose page was edited while it was rendering was
deleted and rendered again (its mtime would otherwise have looked up to date).

**Fixes found by the pre-check and the QC sheets (each re-rendered):**
- B02 landscape: the "2402 MHz" label projected past the left title-safe edge (edge-bleed); both frequency labels
  were dropped and the loss label shortened ("OF TRIES FAILED · BUSY WI-FI").
- B05 landscape: the delay label ("BEHIND THE PICTURE · TWO PUBLISHED TESTS") ran past the right edge; shortened to
  "BEHIND · TWO PUBLISHED TESTS".
- B01 phone: the "SBC" and "BLUETOOTH LINK" labels overlapped and the 50% frame underfilled (51%, under Gate V's 55%);
  the link label moved below the pipe and the CD arithmetic note now shows on the phone too. The first phone final was
  then refused for the "CD QUALITY" label crossing the left edge; on the QC sheet it also touched "SBC", so on the phone
  that label was dropped (the stat says CD quality).
- B03 phone: a note that the kbit/s come from ffmpeg's encoders (and LDAC from Sony) was added, as on landscape.
- B05/B06 phone: the "BEHIND" and "ONE PHONE OR TV" labels sat over 3D blocks and dots; both moved up. B07 phone: two
  apply-card steps wrapped; shortened ("Phone close by", "Pick a better codec", "Use game mode").
- In the final mix the small-buffer clip has about 0.14 s of extra silence around 2.1 s in (the dropout); the big-buffer
  clip has none (measured on the master).

**Finals** (`./art final <reel> --height 2160`, `./art final <reel>/vertical --height 3840`):

| Cut | File | Size | Duration | SHA-256 | Receipt |
|---|---|---|---|---|---|
| 16:9 | `bluetooth-audio-explainer.mp4` | 69.5 MB | 146.50 s | `d2f4de37b39bfbcd7254db6fcdfbe80fc7686838d565d9a5eaf6f67bc627bb72` | ready, 2026-11-20 06:14 UTC |
| 9:16 | `vertical/bluetooth-audio-explainer-vertical.mp4` | 57.3 MB | 146.50 s | `81a6d4b25552f451a9977fb77011c6c8a4386584344d8dbce76103fee56d7887` | ready, 2026-11-20 07:03 UTC |

GATE F (`factcheck_check.py`): clean. GATE T: PASS on both cuts ([TYPECHECK.md](./TYPECHECK.md)). Gate V: passed
(receipt `ready`), with title + HUD contrast regions declared on B01–B06. QC sheets:
[`qc-sheet-16x9.png`](./qc-sheet-16x9.png), [`qc-sheet-9x16.png`](./qc-sheet-9x16.png).
