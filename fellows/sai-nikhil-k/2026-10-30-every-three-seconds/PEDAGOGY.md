# PEDAGOGY — Every Three Seconds

**Reel** `weekly_updates/2026-10-30-every-three-seconds/` · **slug** `claude-sai-every-three-seconds`
**Subject** Gavia 0.4.0's Check an audio (loon-call detection) · **week of** 2026-10-30 (built 2026-11-09, backlog)
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + two image plates (real Gavia 0.5.0 screenshots), no Manim, nothing paid

---

## The ONE idea

> Gavia can listen now: it cuts a recording into three-second windows and gives
> each one P(loon call), from BirdNET 2.4's embedding and a logistic regression,
> all offline. Its perfect validation score is easy by construction; under our
> drone's noise at 5 dB it catches about two loon windows in three, and invents none.

Sai's brief (2026-11-09): "Create 2 new videos explaining one feature each for
the following changes pushed to the Gavya app: audio detection model of the loon
call; invasive vegetation detection." Dates: this one is October 30. His repo
link is the content. He picked the angle "Every Three Seconds" (explain the
pipeline, then the honest test) and "nothing to leave out".

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Gavia only looked at photos; now it listens. How does it hear, and through a drone? |
| B01 | CHECK AN AUDIO | image plate · 3 screenshots | The real screen: a Maine recording, 3 s bars, two calls; the new question; any format. |
| B02 | HOW IT HEARS | `ClaudeScienceChipGrid` | Six steps: decode, mono 48 kHz, 3 s windows, BirdNET 2.4, 1,024 numbers, one probability. |
| B03 | ONE WINDOW, ONE NUMBER | `TypesetMath` | n = 3 s × 48 kHz = 144,000; z = ((x − μ)/σ)·w + b; P = σ(z) ≥ 0.5 ⇔ z ≥ 0. |
| B04 | A PERFECT SCORE | `BinaryBranch` | 1.000 on val is easy by construction (windows picked by BirdNET's score); drone noise is the real test. |
| B05 | UNDER THE DRONE | `ExecutedData` | Gavia's Rust code on loonet's drone test: 28 → 24 → 19 → 13 of 28; 0 of 37 false alarms. |
| B06 | ONE RECORDING, TWO WAYS | image plate · 2 screenshots | The same Maine recording in the app: 4 of 8 bars at 88% clean; 2 of 8 at 77% under the drone. |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B08 | HANDOFF | `ClaudeComposerAsk` | Record a minute near water; ask what windows, embeddings and thresholds do to it; check in Gavia. |
| B09 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B08 and the verdict only. Body beats:
`images → ChipGrid → TypesetMath → BinaryBranch → ExecutedData → images`.
No repeats; every beat has an ordered `show` block.

## 9:16

Every Remotion pattern has a `*916` sibling; the two image plates have
re-composed portrait plates in `pantry/`. Portrait-only edits: none planned.

## Evidence and honesty

- **Executed locally, Gavia's own code:** `evidence/noise_check.rs` (a companion to
  Gavia's `tests/call_parity.rs`, built at tag v0.5.0, `5dd8471`; looncall_v1.onnx
  sha256 `b47f45d1…`, unchanged since 0.4.0) scores the 325 clips that
  `evidence/drone_mix.py` rebuilt from loonet's notebook (65 val windows × clean,
  10, 5, 0, −5 dB; same order, RNG and gain). Loon windows caught: 28, 24, 19, 13,
  4 of 28; false alarms 0 of 37 at every level.
- **The formula is the model:** `drone_mix.py` applies loonet's README formula to
  BirdNET 2.4 TFLite embeddings with `weights.npz` and gets the identical table;
  Rust and Python agree to 0.000004 on every clip (0 on the other side of 0.5).
- **Gavia's own parity test passes:** `call_parity.out`: 147 windows, worst
  |P − Python| = 0.0031, 0 flipped; `calls` 3/3.
- **Screenshots are real:** Gavia 0.5.0 from /Applications, launched with
  `GAVIA_DATA_DIR` pointing at a scratch folder (Sai's own history untouched),
  driven by accessibility + synthetic mouse, captured with `screencapture -R`.
  The audio code is unchanged between 0.4.0 and 0.5.0 (`git diff v0.4.0 v0.5.0`
  touches nothing under `src/calls/` or the audio UI), so the screen is the 0.4.0
  feature; captions say 0.5.0 because that is what was running.
- **The B06 drone recording is ours:** `demo_mix.py` mixes the drone noise into a
  CC0 val recording (Mount Desert, Maine) at 5 dB per window, the way loonet's test
  does. `listen.out` shows the same windows the app drew (4 vs 2 at or above 0.5).
- **"About two in three"** = 19/28 = 0.679 at 5 dB, loon *windows*, not calls. In
  B06 both calls survive; only their quieter windows drop. The narration says so.
- **"Invents none"** = 0 false alarms on the 37 non-loon val windows at every SNR
  (185 noisy clips). The drone's own windows were in training as not-loon, which
  loonet's README flags; the reel doesn't claim more than this test.
- **Not claimed:** call types. Gavia's ROADMAP item 3 asked for wail, tremolo,
  yodel and hoot; looncall 1.0 is loon / not loon. The verdict says it can't tell
  them apart yet.

## QC changes made after the first render (2026-11-09)

- **Data beat → table mode.** In `mode: "probability"`, four bar rows pushed the
  provenance note below the frame (GATE V: edge-bleed at 50% and 85%). The beat
  now shows the same counts as a table, and the note is on screen.
- **`qc.sparse` declared on B02 (ChipGrid)**, with the reason in the sheet: at the 50% sample only 4 of 6 chips are lit, so the portrait ink box is 34% (floor 35%).
  Looked at the frames first; the 85% frames are full. Carried in `build_beats.py`,
  so `shorts.py --vertical` copies it on a re-derive.

## Corrections Sai may want in the repo (not in the video)

- `ROADMAP.md` at v0.4.0 and v0.5.0 still lists **3. Acoustic Common Loon call
  classifier — ⚪ Not started**, though 0.4.0 shipped it.
- README "How accurate is it?" has no audio section; the only call-model numbers
  are in `looncall_v1.json` (P = R = AP = 1.0 on clean val, recall 0.679 at 5 dB).

## Attribution

Hosted by Sai; Gavia and loonet are his projects. Every commit in the window
(`e5ac987`, `1b2ef35`, `7909a76`) is Sai's. BirdNET 2.4 is the K. Lisa Yang
Center for Conservation Bioacoustics' (Cornell Lab of Ornithology), CC BY-NC-SA
4.0 — said on the verdict card. The Maine recording is CC0 (iNaturalist).

## Pronunciation (narration only)

- `BirdNET` → "BirdNet" (raw spells N-E-T) · `loonet` → "Loon Net" ·
  `Mount Desert` → "Mount Dessert" (the local pronunciation).

## Expected build noise (not bugs)

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Is "about two loon windows in three at 5 dB" the headline you want public?
- [ ] OK to show your drone noise mixed into a public CC0 recording (B06)?
- [ ] B07: OK to say on screen that the call model is non-commercial?
- [ ] Fix the ROADMAP status for item 3 (separately, in the Gavia repo)?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 12.5s measured (47 words)

> Until now, Gavia only looked at photos. This is Sai. This week it learned to
> listen: open a recording, and it marks every three seconds where a loon calls.
> So how does it hear? And how well does it hear through the noise of our own
> drone?

### B01 · CHECK AN AUDIO — `image plate · hero+2` · 16.7s measured (63 words)

> Here's the new screen, on a recording from Mount Dessert, Maine. Each bar is
> three seconds of sound, and the red ones hold a loon call: four stretches, two
> calls. Click one to hear it, or save every stretch as a spreadsheet. The front
> page now asks: is that a loon? And it takes almost any recording, even the
> sound of a video.

### B02 · HOW IT HEARS — `ClaudeScienceChipGrid` · 20.3s measured (64 words)

> Under the hood, it's six steps. Decode the file, whatever the format. Mix it
> down to one channel at forty-eight thousand samples a second. Cut it into
> three-second windows, back to back. Pass each window through BirdNet two point
> four, the bird-sound model from the Cornell Lab of Ornithology. Out come one
> thousand twenty-four numbers, and a small classifier turns them into one
> probability.

### B03 · ONE WINDOW, ONE NUMBER — `TypesetMath` · 19.0s measured (63 words)

> Each window is three seconds at forty-eight thousand samples a second: a
> hundred and forty-four thousand numbers. BirdNet turns them into x, the
> embedding. The classifier scales x, weighs it, and sums it into one score, z.
> The logistic curve turns z into a probability, and Gavia calls it a loon at
> one half or more: exactly when z is zero or more.

### B04 · A PERFECT SCORE — `BinaryBranch` · 19.9s measured (65 words)

> On Loon Net's validation set, the classifier scores a perfect one point zero.
> Don't celebrate yet. Those windows were picked by BirdNet's own score: loon
> windows above zero point four, the rest below zero point zero two. Easy by
> construction, and the model card says so. The harder question is the one our
> field recordings will ask: does a call still register under the drone?

### B05 · UNDER THE DRONE — `ExecutedData` · 19.2s measured (61 words)

> So we ran that test again, through Gavia's own Rust code. Clean, it catches
> all twenty-eight loon windows. At ten decibels of drone noise, twenty-four. At
> five, nineteen. At zero, where the propeller is as loud as the recording,
> thirteen. And it never once called a loon among the thirty-seven other
> windows. Loon Net's own Python agrees to within four millionths.

### B06 · ONE RECORDING, TWO WAYS — `image plate · pair` · 16.4s measured (54 words)

> Here's what that looks like in the app. The Maine recording, clean: a loon in
> four of eight stretches, the strongest call eighty-eight percent. The same
> recording with the drone mixed in at five decibels: two of eight, the
> strongest seventy-seven. Both calls are still found, but their quieter halves
> fall below the line.

### B07 · VERDICT — `ClaudeVerdictArtifact` · 15.9s measured (51 words)

> So: Gavia can listen now, entirely offline, three seconds at a time, with
> BirdNet's ears and a small classifier. Its perfect score means little. Under
> our drone at five decibels, it catches about two loon windows in three, and
> invents none. And it can't yet tell a wail from a tremolo.

### B08 · HANDOFF — `ClaudeComposerAsk` · 13.7s measured (50 words)

> Your turn. Record a minute of sound near water on your phone, and ask an
> assistant what a three-second window, an embedding, and a one-half threshold
> would each do to it, and what would make a call slip through. Then open it in
> Gavia, and see which bars turn red.

### B09 · OUTRO — `LogoOutro` · 2.4s measured (4 words)

> Every three seconds. Sai.

**Total: 522 words** → 155.8s measured (2:35). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: PASS   — reviewer: SAI NIKHIL KUNAPAREDDY date: 11/09/2026
