# BUILD-LOG — "How Auto-Tune Works"

What broke, what it cost, and what changed because of it. Built 2026-11-19 for the week of 16–20 Nov, alongside
this week's Bluetooth audio reel. Rohan V. chose the topic, chose HyperFrames + three.js again for both of the
week's videos, and gave 20 hours for the week. B01–B06 are HyperFrames compositions with three.js scenes; B00, B07
and B08 are the channel's Remotion cards.

## 1 — Evidence: a small pitch corrector, built from the textbook parts

Antares' code isn't public, so `autotune.py` builds each part and measures it. A synthetic singer at 44.1 kHz (a
buzzing source shaped by four fixed "ah" vowel resonances) sings an original seven-note phrase in C major (E4 G4 A4
G4 E4 D4 C4, 3.89 s), Western in style per Rohan's standing preference for STEM test material, off-key on purpose:
each note detuned (+19, −32, +27, +24, −24, −36, −39 cents), a scoop into each note, vibrato and slow drift. The
true pitch is kept for scoring. Pitch is detected with YIN (32 ms window, every 5 ms). Correction pulls each moment
toward the nearest note of C major through a one-pole follower (my "retune speed": 60 ms gentle, 0 ms instant) and
is applied to the audio with TD-PSOLA using only the *detected* pitch; the corrected audio is then measured again
with the same detector. A held C4 is shifted up four semitones three ways. Seeded (1120 for the tune, 2026 for the
singer's wobble); NumPy and SciPy.

What the run measured (`evidence/run.log`):

- **Detection**: 692 sung frames; median error 0.63 cents, 95th percentile 9.03; 93.1% of frames within 5 cents of
  the true pitch. Example frame at 1.26 s (the A4): best repeat after 2.231 ms → 448.2 Hz (true 448.3 Hz).
- **As sung**: 29.1 cents off on average (programmed detune 28.8), vibrato about ±15 cents; within 5 cents of a
  note 4.5% of the sung time.
- **Gentle (60 ms)**: 6.5 cents off on average, vibrato about ±14 cents; within 5 cents of a note 29.8% of the time.
- **Retune speed zero**: 0.4 cents off on average, vibrato about ±8 cents; within 5 cents of a note 90.6% of the time.
- **Shifting a held C4 up 4 semitones (×1.260)**: plain resampling 1.27 s long (was 1.60), vowel moved +25.8%; the
  patent's way (resample, then repeat whole cycles) 1.60 s, +27.8%; PSOLA 1.60 s, +0.6%. All three land at 329.5 Hz.

Sanity checks on the run, and what they changed:

- **A metric that measured the wrong thing.** The first correction score was how quickly the pitch reached each new
  note. It was unreliable: the scoop into each note and the note's own detune moved it as much as the correction
  did. It was replaced by the share of sung time within 5 cents of a note (4.5% as sung, 29.8% gentle, 90.6% at
  zero), which B03 and B05 use.
- **A vowel measure that gave nonsense.** The first formant measure picked peaks from the long-term average
  spectrum and reported +14% and −8%, numbers that made no sense (plain resampling must move every resonance by
  ×1.260): the first two resonances of "ah" sit close together and merge, so picking peaks was unreliable. It was replaced by a
  stretch fit on the cepstrally smoothed spectral envelope (the stretch that best maps the original's envelope onto
  the shifted one, 400–4,000 Hz). Plain resampling must give ×1.260; the fit finds ×1.258 (+25.8%), and PSOLA
  +0.6%.
- **Detector misses are reported, not hidden.** 11 frames are more than 50 cents off, all within 11 ms of a note's
  start, where the old note fades and the new one begins. They stay in every number above; only the drawing drops
  them (§5).
- **A click at the edge.** PSOLA's output had a click of 0.26 (full scale 1.0) at its edge. The
  grains now fade in and out over 10 ms where the output starts and stops.
- **The patent's method was added.** Research showed that Auto-Tune's patent shifts pitch by resampling and then
  adds or drops whole cycles to keep the length (fact sheet §4). The run first compared only plain resampling and
  PSOLA; it now includes that method too (my reconstruction from the patent's text, built from the PSOLA machinery
  used as a time-stretch): +27.8%, so it keeps the length but moves the vowel about as much as plain resampling.
  B04 shows all three.
- **The gentle average hides one note.** Per note, gentle correction leaves 3.3, 2.9, 5.3, 6.4, 2.7 and 5.4 cents,
  and the final held C4 still 19.2 cents flat. Found by the fact check (§2); the narration now says "averaged".

## 2 — Script

Nine beats, authored by `author_sheet.py` into `beat_sheet.json` and `cues.json`; later edits went into the sheet.
Every spoken number is the run's (B01–B04) or from `week-13/_research/facts-autotune.md` (440 Hz; five cents; 1997;
"Believe", 1998). Each measured number is introduced with "my detector", "my singer", "in my test" or "my version".
Antares is credited only with the release and the patent's method; the inventor and the song's producers are not
named (fellows-repo rule). The name is spelled phonetically in the narration, "Row-Haan"; "Rohan V." on screen. The
title is plain: "How Auto-Tune Works"; the handoff name is `AutoTune_RohanV`.

The fact-check pass (an independent Claude agent, against the fact sheet and `evidence/`; FACTCHECK) held two
claims in this reel; both were re-voiced on 2026-11-19:

- **B03.** "At a gentle sixty milliseconds, my singer was under seven cents off" said every note was within seven
  cents; one is 19 cents flat. Now "my singer **averaged** under seven cents off". Same length; the `seven` cue
  ("under seven") still resolves.
- **B08.** The close described my PSOLA method as if it were Auto-Tune's. It now names the job: "Find the repeat,
  pick the note, and shift the pitch."

## 3 — Audio, and the listening takes

- **Narration**: Kokoro `af_bella`, nine beats, all aligned by `align.py` with 0 fallbacks (`_audio.log`); all 51
  cue anchors in `cues.json` resolved. B05's narration is 4.27 s.
- **The listening takes** (`mix_listen.py`, run by `bash ../run_audio.sh <reel>` after `align.py` and before
  `sync_cues.py`): B05's narration, then a 0.6 s pause, then `take.wav`, `gentle.wav` and `hard.wav` exactly as
  `autotune.py` rendered them (3.89 s each, 0.7 s apart), each set to the narration's RMS level (−9.5, −9.4 and
  −9.4 dB), then a 0.8 s tail. Stereo, 48 kHz, 192 kbit/s like the rest of the series; the mono takes play in both
  ears. The mixed file `mp3/beat-B05-listen.mp3` became B05's `audio_file`; the beat was re-measured at 18.74 s, and
  the three windows (4.867–8.757, 9.457–13.347, 14.047–17.937 s) went into the beat's `listen_clips` and
  `props.listen`, which B05's scene uses to sweep the playhead in real time.
- `run_audio.sh` then writes `props.durationSeconds` into every beat, so each scene plays on its measured clock.
  Nine beats, 137.27 s in all.

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
- **New in the kit this week**: `pianoRoll` (the lanes of C major, the tune's notes, pitch tracks as tubes that draw
  on progressively), with `tubeN` / `drawTube`, `slab`, `grid`, `glowBox`, `ribbon`, `canvasTex` and `pathTube`.
- **Design decisions**: "the vocal booth at night" (near-black plum); the singer is a wave and a pitch track, never
  a person; as sung coral, gentle gold, zero cyan and the notes of C major lilac throughout, in 3D and in the HUD.
  B03's tracks are the pitch measured on the corrected audio, not the targets. B06's seismic traces are an
  illustration (synthetic, seeded); its voice is the run's A4 frame.
- **Data**: the HUD numbers come from `evidence/scene.json` and `results.json`; B04's vowel curves are
  `autotune.py`'s own `envelope()` evaluated in `build_hf.py` on the run's held-note files.
- Rendered by `build_hf.py --render` into `media/B0x.mp4` (16:9) and `pantry/B0x-916.mp4` (9:16), where the
  Brutalist compiler picks them up like any beat clip. Temporary frames go to `D:/Rohan/Claude/HyperFrames/tmp`,
  never C:.

## 5 — Snapshot review fixes

Snapshots of every beat in both aspects (`_snap/`, `../snap.sh`) were looked at before the 4K renders. What they
found, and the fix:

- **Spikes in the drawn pitch tracks.** The detector's few onset misses (octave slips where one note fades into the
  next) drew as tall spikes. The drawing now drops points more than half a semitone from the median of their nine
  neighbours (`track()` in `build_hf.py`); every number on screen still comes from `results.json`, misses included.
- **Tracks washed to white.** With additive blending, overlapping glowing tracks added up to white where they
  crossed. The core tubes of the piano roll now use normal blending (`kit3.js` `pianoRoll`); the glow sprites stay additive.
- **B04's 3D stage was blank.** The vowel chart's panel had the id `env`, which clashed with the page's `env` data
  script (both are found by id), and the 3D stage came up blank. The panel is now `envp`.
- **3D labels outside the stage.** Labels pinned to 3D points could show over the HUD when their point left the
  stage. `kit3.js` `pin` now hides a label whose point is outside the stage (both reels).
- **E4 and F4 lane labels collided.** Only the tune's own notes are labelled now (C4, D4, E4, G4, A4).
- **Phone label overlaps.** B04's grain-row labels (ORIGINAL, SPED UP, PSOLA) overlapped on the phone; they are now anchored
  above their rows.
- **Long bar labels** were shortened.

The phone layout follows Rohan's rule from week 11: no overlapping panels or text on the phone; if it doesn't fit,
remove text from the bottom and use the room to space the panels. On the phone, B01's closing note and B03's
"Believe" card are dropped (the narration still names the song).

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
- B01 phone: the "MATCH" caption was set on one line and ran past the right title-safe edge (Gate V edge-bleed);
  it now wraps, and the "one repeat" label moved inward.
- B03 phone: the two result cards sat side by side and the right one ran off the frame; on the phone they now stack,
  and the colour key ("THE TRACKS") was dropped there so the column ends inside the safe area (the card heads already
  name the colours).
- B02 phone: at Gate V's 50% sample the "29 cents" stat had not appeared yet (low contrast in the HUD region); it now
  appears on "synthetic singer" and counts up on "twenty-nine".
- The first Auto-Tune phone final was refused by Gate V for exactly these (B02 low contrast, B03 bottom edge-bleed);
  after the re-renders the phone final passed with no BLOCKER or MAJOR.
- In the final mix the three listening takes were measured again with the run's own detector: 4.4%, 29.2% and 89.1% of
  the time within 5 cents of a note (the run: 4.5%, 29.8%, 90.6%; the small differences are the AAC encode).

**Finals** (`./art final <reel> --height 2160`, `./art final <reel>/vertical --height 3840`):

| Cut | File | Size | Duration | SHA-256 | Receipt |
|---|---|---|---|---|---|
| 16:9 | `auto-tune-explainer.mp4` | 65.6 MB | 137.50 s | `2ea5e085efd2b8c845c160c07a25e23f5c9b1d83a9a641b9539c0ffc63137240` | ready, 2026-11-20 05:47 UTC |
| 9:16 | `vertical/auto-tune-explainer-vertical.mp4` | 57.4 MB | 137.50 s | `f755892426629e176f27c8e77baa92047d45def972ffb2c3522d18597ce8b3e2` | ready, 2026-11-20 06:35 UTC |

GATE F (`factcheck_check.py`): clean. GATE T: PASS on both cuts ([TYPECHECK.md](./TYPECHECK.md)). Gate V: passed
(receipt `ready`), with title + HUD contrast regions declared on B01–B06. QC sheets:
[`qc-sheet-16x9.png`](./qc-sheet-16x9.png), [`qc-sheet-9x16.png`](./qc-sheet-9x16.png).
