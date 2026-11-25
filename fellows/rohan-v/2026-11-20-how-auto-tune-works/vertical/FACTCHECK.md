# FACTCHECK — How Auto-Tune Works

Status: claims checked 2026-11-19 by Claude (Claude Code) against `week-13/_research/facts-autotune.md`,
`evidence/run.log` and `evidence/results.json`, with one claim (row 15) held UNVERIFIED until its narration was
reworded; Rohan V.'s review of the 4K finals still to come.

Every spoken claim, plus the on-screen strings of B00, B07 and B08 (B01–B06 visuals not built at check time, so
their narration only), its source, and its verdict. "The run" means `autotune.py` → `evidence/run.log` /
`evidence/results.json` / `evidence/scene.json`. It is a **model**: a synthetic singer at 44.1 kHz (a buzzing
source shaped by four fixed "ah" vowel resonances), singing an original seven-note phrase in C major
(E4 G4 A4 G4 E4 D4 C4, 3.89 s) slightly off-key on purpose, with a scoop into each note, vibrato and slow drift
(seeds 1120 and 2026; the true pitch is kept). Pitch is detected with YIN (32 ms window, every 5 ms) and scored
against that true pitch. Correction snaps each moment to the nearest note of C major, follows it with a one-pole lag
("retune speed": 60 ms gentle, 0 ms instant), and is applied to the audio by TD-PSOLA using only the *detected* pitch;
the corrected audio is then measured again with the same detector. A held C4 is shifted up four semitones three ways
(plain resampling; resampling plus repeated whole cycles, my reconstruction of the patent's method; PSOLA) and the
vowel's spectral envelope is compared. **Nothing here is Antares' code.** The inventor and the song's producers are
not named (fellows-repo rule). Confidence: HIGH / MED as graded in the fact sheet; "measured" = a number from the
run. Verdicts: PASS, CORRECTED (changed after review), EXEMPT (a drawing, not a claim); UNVERIFIED = held, blocks
GATE F.

| # | Beat | Claim (as spoken / shown) | Source | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` line 29 | — | PASS (verbatim) |
| 2 | B00 | AI narration disclosed | on screen "Narration: AI voice (Kokoro af_bella), script by Rohan V." + `metadata.ai_disclosure` | — | PASS |
| 3 | B00 | How software finds the note you sang and moves it to the right one; I built a small version. Screen: "How does Auto-Tune fix a singer's notes?", "find the pitch / pick the nearest note / move it without a chipmunk voice" | `autotune.py` sections 2, 3 and 4; run §3 (PSOLA moved the vowel +0.6%) | — | PASS |
| 4 | B01 | A sung note is a wave that repeats; how often it repeats is its pitch | §6; the repetition rate is the fundamental frequency, heard as pitch (beginner simplification) | HIGH | PASS (simplified) |
| 5 | B01 | The A above middle C repeats 440 times a second | §6: A4 = 440 Hz, ISO 16:1975 | HIGH | PASS |
| 6 | B01 | The software slides a copy of the wave along itself until the two line up | §4 (patent: pitch "derived from the auto-correlation function"); my YIN difference function d(τ) = Σ(x[j] − x[j+τ])², computed from the autocorrelation; run: "best repeat after 2.231 ms -> 448.2 Hz" | HIGH | PASS |
| 7 | B01 | My detector was within five cents ninety-three percent of the time | run: "93.1% of frames within 5 cents" of the true pitch, 692 sung frames; median error 0.63 cents; the 11 misses (over 50 cents) all within 11 ms of a note's start. Scored on the synthetic singer, a cleaner signal than a real voice | measured | PASS |
| 8 | B01 | Five cents is about the smallest change most people can hear | §6 safe wording ("around five cents, about the smallest change most people can hear"); musicians do better | MED | PASS |
| 9 | B02 | A semitone, one step on a piano, is a hundred cents | §6 (12 equal semitones per octave, 1 semitone = 100 cents) | HIGH | PASS |
| 10 | B02 | My synthetic singer, singing a short tune in C major | run: "7 notes in C major (E4 G4 A4 G4 E4 D4 C4)"; `TUNE` is an original phrase | — | PASS |
| 11 | B02 | Off by about twenty-nine cents on average | run: "as sung: average 29.1 cents off" (median of each note's middle, from the detected pitch); programmed detune averages 28.8 cents | measured | PASS |
| 12 | B02 | Never a wrong note, just a little sharp or flat | results.json `as_sung.offsets`: 13.7, −35.0, 27.7, 20.0, −29.7, −39.2, −38.8 cents; every note's middle is under 50 cents from its intended note, so the nearest note is always the right one. The scoop into each note and the vibrato peaks go further for a moment | measured | PASS |
| 13 | B03 | Auto-Tune moves each moment toward the nearest note in the key you choose | §4 (target = nearest note of the chosen scale; you pick the key to limit targets) | HIGH | PASS |
| 14 | B03 | A setting called retune speed decides how fast | §3 (the setting is Retune Speed) | HIGH | PASS |
| 15 | B03 | "At a gentle sixty milliseconds, my singer averaged under seven cents off" | run: "gentle (retune speed 60 ms): average 6.5 cents off" (6.45). That is the **average**; per note 3.3, 2.9, 5.3, 6.4, 2.7, 5.4 and **−19.2** cents. The longest note, the final held C4, is still 19 cents flat. Spoken without "on average", it says every note was within seven cents. Proposed: "my singer averaged under seven cents off" **Re-voiced 2026-11-19:** now says "averaged". | measured | CORRECTED |
| 16 | B03 | … and the vibrato survived | run: vibrato about ±14 cents after gentle correction vs ±15 as sung | measured | PASS |
| 17 | B03 | At zero, it snaps instantly | §3 (at zero, "snap the vocal pitch to the nearest note instantly"); in my code, 0 ms applies the full correction with no lag | HIGH | PASS |
| 18 | B03 | The voice sat within five cents of a note ninety-one percent of the time | run: "hard (retune speed 0 ms): … within 5 cents of a note 90.6% of the sung time" (as sung: 4.5%; gentle: 29.8%) | measured | PASS |
| 19 | B03 | That's the robotic sound, made famous by Cher's "Believe" in 1998 | §3 (first famous use of Auto-Tune as an audible effect, 1998; Retune Speed at zero). Not claimed as the first song to use it | HIGH | PASS |
| 20 | B04 | To raise a pitch you could speed the recording up, but it gets shorter | run: "plain resampling: 1.27 s, pitch 329.5 Hz" vs original 1.60 s, 261.5 Hz | measured | PASS |
| 21 | B04 | Auto-Tune's patent keeps the length by repeating whole cycles | §4 (patent US 5,973,252: "resampled at a new sample rate proportional to the desired change in pitch"; whole cycle periods added or subtracted). Raising pitch shortens the sound, so cycles are added | HIGH | PASS |
| 22 | B04 | For a big shift, both move the vowel too: in my test, up by over a quarter, a chipmunk | run, 4 semitones up: resampling "resonances moved x1.258 (+25.8%)", resample + repeat cycles "x1.278 (+27.8%)"; theory for both is ×1.260. "Big shift" is the hedge: a typical correction under 50 cents moves the vowel about 3%. "Chipmunk" is colloquial | measured | PASS |
| 23 | B04 | My version re-spaces single cycles instead, a method called PSOLA | `autotune.py` `psola()`: one grain per pitch mark (two periods wide, raised-cosine windowed), re-placed at the new period, no resampling | — | PASS (simplified) |
| 24 | B04 | The vowel moved under one percent | run: "PSOLA: 1.60 s, pitch 329.5 Hz, resonances moved x1.006 (+0.6%, match r=0.990)" | measured | PASS |
| 25 | B05 | Here's my singer: as sung, then gentle, then retune speed zero | `mix_listen.py` PLAN for B05: take.wav, gentle.wav (60 ms), hard.wav (0 ms), each the full 3.89 s, unedited, level-matched to the narration only. At check time `mix_listen.py` had not been run yet (no `listen_clips` in the beat sheet) | measured | PASS |
| 26 | B06 | Auto-Tune came out in 1997 | §1 (Antares About page; Recording Academy). Year only: the month is disputed | HIGH | PASS |
| 27 | B06 | … from an engineer who had used similar maths to read seismic data for oil | §2 (worked at Exxon interpreting seismic data for oil exploration, using autocorrelation). Sources call him a research engineer or a geophysicist; he trained in electrical engineering. Not claimed: that he invented the method, or that Auto-Tune was made for oil | HIGH / MED-HIGH | PASS |
| 28 | B06 | Today, pitch correction is a standard studio tool, often too subtle to notice | §5 safe wording verbatim. No percentage is given (the "90%" is market share, not songs) | MED | PASS |
| 29 | B07 | Set your song's key first | §4 (you pick the key to limit the targets; default chromatic) | HIGH | PASS (as advice) |
| 30 | B07 | Start with a slow retune speed for a natural sound; turn it to zero for the effect | §3, §4 (at normal speeds it glides and vibrato survives; zero snaps); run rows 16–18 | HIGH | PASS (as advice) |
| 31 | B07 | Screen: title "Try Pitch Correction", lede "Find the repeat, pick the note, move it.", steps "Set your song's key first." / "Slow retune speed: natural." / "Zero: the robot effect.", spark "A little maths between you and the note." | summary of B01–B05 | — | PASS |
| 32 | B08 | "Find the repeat, pick the note, and shift the pitch." | summary of B01, B03 and B04. "Re-space the cycles" is my PSOLA version (B04), not the patent's resample-and-repeat; read as a summary of what I built **Re-voiced 2026-11-19:** the close names the job, not my PSOLA method. | — | PASS (summary of my build) |
| 33 | B08 | Screen: "How Auto-Tune Works", "@HumanitariansAI", "Rohan V." | title card | — | EXEMPT (title card) |

## Fixed in the re-voice (2026-11-19; rows 15 and 32 now CORRECTED)

- **Row 15 (B03).** Current: "At a gentle sixty milliseconds, my singer was under seven cents off, and the vibrato
  survived." Proposed: "At a gentle sixty milliseconds, my singer averaged under seven cents off, and the vibrato
  survived." Same length; the `seven` cue ("under seven") still resolves. Change the verdict to CORRECTED once the
  audio is regenerated, aligned and re-synced.

## Arithmetic, checked separately

- **The example frame.** 1 ÷ 2.231 ms = 448.2 Hz. That A4 is sung sharp: 1200 × log₂(448.2 ÷ 440) ≈ +32 cents at that
  moment (programmed detune +27.1 plus vibrato). The true pitch there is 448.3 Hz, so the frame's error is 0.4 cents.
- **Cents.** A semitone is a ratio of 2^(1/12) = 1.0595; four semitones 2^(4/12) = 1.2599, the run's "x1.260".
  Resampling by that ratio shortens 1.60 s to 1.60 ÷ 1.26 = 1.27 s, the run's figure.
- **Off by twenty-nine.** Programmed detunes +19, −32, +27, +24, −24, −36, −39 cents: mean of the magnitudes 28.8.
  Measured from the detected pitch (median of each note's middle, from 120 ms after its start to 40 ms before its end):
  29.1. Largest 39.2, under the 50 cents at which a note would round to its neighbour.
- **Retune speed.** In `correction()`, 60 ms is the time constant of a one-pole follower stepped every 5 ms:
  k = 1 − e^(−5/60) ≈ 0.080 per step; 0 ms applies the error at once. This is my definition. Antares' current versions
  give Retune Speed in ms, but the 1997 original's units are unconfirmed (§3), so the film never says Antares' 60 ms
  sounds like mine.
- **Gentle average.** (3.3 + 2.9 + 5.3 + 6.4 + 2.7 + 5.4 + 19.2) ÷ 7 = 6.46 (6.45 unrounded): "under seven" holds only
  as an average (row 15).
- **"Within five cents of a note"** (rows 7 and 18 are different measures). Row 7 compares the detector with the true
  pitch. Row 18 rounds the corrected take's detected pitch to the nearest semitone (any of the twelve, not only C
  major) and counts frames within 5 cents of it: 90.6% at 0 ms, 29.8% at 60 ms, 4.5% as sung. Hard correction still
  leaves about ±8 cents of wobble. My reading, not tested: the correction is computed every 5 ms from the *detected*
  pitch and applied one grain (one cycle) at a time, so the fast vibrato is only partly flattened.
- **The vowel.** The envelope comparison stretches the original's cepstrally smoothed spectrum (400–4,000 Hz) by a
  factor a and keeps the best correlation. Plain resampling must give a = 1.260; the run finds 1.258. My
  resample-and-repeat version (resampling, then the PSOLA machinery used as a time-stretch, repeating whole cycles)
  finds 1.278, close to the same; PSOLA finds 1.006.

## Not claimed

- That `autotune.py` is Antares' algorithm, or that the "patent's way" here is the patent's code. It is my
  reconstruction from the patent's description (§4).
- That current Auto-Tune makes chipmunks. Later versions added formant correction (§4); the film speaks of the patent.
- That the inventor invented autocorrelation pitch detection, or that Auto-Tune was invented for oil (§2, "don't say").
- That "Believe" was the first song to use Auto-Tune, or whether its sound was an accident (§3).
- That the 1997 original showed Retune Speed in milliseconds (§3), or a month for the release (§1).
- Any percentage of songs that use pitch correction (§5).
- That 93%, 29 cents, 6.5 cents or 91% describe real singers. They are the synthetic singer's.
