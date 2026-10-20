# FACTCHECK — How Apps Find a Song's Tempo

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-10-17.
"The run" means `tempo.py` → `evidence/run.log` / `evidence/results.json` / `evidence/scene.json`
(SHA-256 in `MEASUREMENTS.txt`). The grooves in the run are **synthetic** Western drum grooves
(`grooves.py`, generated from seeds); no recording is used, measured or played. Outside facts were
verified on 2026-10-17 and are recorded with URLs and confidence levels in
`week-08/_research/facts.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md`, required wording | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure line + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | Apps find the beats from the sound; the hard part is choosing which repeat is the beat | Ellis 2007: a periodic onset signal also correlates at whole multiples of its period, so picking one peak is hard (facts.md §1a, §2) | ✅ |
| 4 | B01 | At 120 BPM a beat lands every half second | 60 s / 120 = 0.5 s | ✅ arithmetic |
| 5 | B01 | Four seconds of a rock groove I generated, beats marked | `grooves.render("rock", 120, seed=2)`, the test set's own clip; marks are `true_beats()` | ✅ |
| 6 | B01 | The listening clip is that groove | `evidence/groove_rock_120.wav`, written by `tempo.py`, appended unedited by `mix_listen.py` (level matched only) | ✅ |
| 7 | B02 | Split into forty frequency bands; how much louder each band just got, added up = the onset curve; called spectral flux | `onset_curve()`: centred STFT, 40 mel bands in dB, positive frame-to-frame increases averaged (librosa documents its own as a "spectral flux onset strength envelope"; Ellis 2007 uses 40 Mel bands) (facts.md §1a, §1b) | ✅ |
| 8 | B02 | A drum hit makes a spike; a held chord adds almost nothing | the example's onset curve: the tallest spikes sit on the drum hits; the sustained pad adds no increases after its attack (visible in the drawn curve) | ✅ shown as the run's data |
| 9 | B03 | Slide the curve against a copy; at some shifts spikes line up; called autocorrelation | `autocorr()`: 8-s Hann-windowed autocorrelation, averaged (librosa's tempogram, `ac_size=8`) (facts.md §1b, §3) | ✅ |
| 10 | B03 | It matches at half a second, and better at one second | run.log EXAMPLE: one beat (0.51 s, the frame nearest 0.5 s) 0.631; two beats (1.00 s) 0.781; asserted in `export_tempo_data.py` | ✅ measured |
| 11 | B03 | 60 / 0.5 s = 120 BPM; 60 / 1.0 s = 60 BPM | arithmetic; typeset with `typeset_math.py` | ✅ |
| 12 | B04 | Forty grooves: rock, funk, house, hip hop, slow ballads, drum and bass, waltzes, jazz swing, five tempos each | `tempo.SET`: 8 styles × 5 tempos chosen by me, 30 s each. The tempos are my choice of each style's usual feel, not a claim about genres | ✅ |
| 13 | B04 | Picking the strongest repeat: right on 13 of 40 | run.log "raw": right 13/40 (within 4% of the true BPM: Accuracy 1, ISMIR 2004) | ✅ measured |
| 14 | B04 | Most misses were exactly half | run.log "raw": 20 half of 27 misses (5 double, 2 other) | ✅ measured |
| 15 | B04 | It locked onto the kick and snare pattern, which repeats every two beats | the example: the two-beat lag (kick + snare + kick + snare) matches at 0.781 vs 0.631 at one beat; in the rock pattern the kick and snare figure repeats every half bar | ✅ measured |
| 16 | B04 | Like librosa, it adds a preference: tempos near 120 count for more | librosa `feature.tempo`: default prior is a Gaussian on log2 BPM centred at `start_bpm=120`, `std_bpm=1.0`; Ellis 2007 weights the autocorrelation the same way (facts.md §3) | ✅ |
| 17 | B04 | Roughly where people tend to tap | Ellis 2007 cites the human bias toward 120 BPM; Moelants 2002 reports a preferred tempo of about 120–130 BPM (facts.md §4; Moelants seen through secondary sources, so "roughly") | ✅ hedged as "roughly" |
| 18 | B04 | With it, the rock grooves come out right, five of five | run.log per-style: rock prior ['right' × 5] | ✅ measured |
| 19 | B05 | Every slow ballad came out double: sixty became a hundred and twenty | run.log: ballads 60/64/68/72/76 → 120.1/128.4/136.0/143.8/152.0, all "double" | ✅ measured |
| 20 | B05 | Every drum and bass groove came out half: 170 became 85 | run.log: 160–178 → 80.3–89.0, all "half" (170 → 85.2) | ✅ measured |
| 21 | B05 | Funk's off-beat kicks pulled it to a different repeat altogether | run.log: funk 96–112 → 128.3, 134.1, 83.3, 143.9, 150.3 (four near 4/3 of the tempo: the kick pattern's three-sixteenth spacing), all "wrong" | ✅ measured; "off-beat kicks" is my reading of the 4/3 ratio |
| 22 | B05 | In all: 17 of 40 exactly right; 33 of 40 right or exactly double or half | run.log "prior": right 17, half 8, double 8, wrong 7 | ✅ measured |
| 23 | B05 | librosa, run on the same forty, gave the same verdict on 34 | run.log cross-check: librosa 0.11.0 `onset.onset_strength` + `feature.tempo` defaults; same class on 34/40 (librosa's own score: 22/40 right, 34/40 right-or-octave) | ✅ measured |
| 24 | B05 | It's called the octave error; the standard tests score it separately | Accuracy 1 vs Accuracy 2 (ISMIR 2004, Gouyon et al. 2006); MIREX scores two tempo candidates (facts.md §2). "Octave error" is the field's term for half/double | ✅ |
| 25 | B06 | Real drummers drift | rekordbox's "Dynamic" analysis mode exists for tracks with tempo changes; Serato advises extra grid markers for live drums (facts.md §6, §7). Qualitative only | ✅ qualitative |
| 26 | B06 | This groove starts at 120 and ends near 123 | the drift function in `tempo.py`: +4% over 30 s plus a ±1.2% wobble; run.log end 123.4 | ✅ (a synthetic drummer, stated as mine in FACTCHECK; not a measurement of real drummers) |
| 27 | B06 | A fixed-tempo grid is more than 50 ms off within six seconds, and up to 140 | run.log DRIFT: grid at 122.4 BPM phase-aligned to the first beat; first > 50 ms at 5.9 s; max 140 ms | ✅ measured |
| 28 | B06 | A beat tracker places each beat on a strong hit while keeping the spacing steady; librosa's method, from a 2007 paper | `track_beats()`: Ellis 2007 dynamic programming (squared log-ratio gap penalty, tightness 100); librosa `beat_track` cites Ellis 2007 (facts.md §1a, §1b) | ✅ |
| 29 | B06 | Half its beats land within six milliseconds | run.log DRIFT: median 6 ms (95% within 15 ms), after correcting the measured −24.8 ms onset-curve latency | ✅ measured |
| 30 | B07 | DJ apps let you halve or double the number, or set a BPM range | Traktor support article on half/double BPM; Serato's analysis "BPM Range" setting (MED, seen via search) (facts.md §7) | ✅ (worded generally, no product named) |
| 31 | B07 | On a live recording, check the beat grid, not just the number | rekordbox Dynamic mode; Serato beatgrid advice (facts.md §7) | ✅ as advice |

## Algebra, checked separately from the typography (MATH-TYPESETTING.md)

- **Autocorrelation.** r(τ) = Σₜ o(t)·o(t+τ), o = the onset curve, τ = the shift in seconds. Shown
  with the sum over frames t; the code normalises by r(0) and averages 8-s windows (stated in PROMPTS).
- **Tempo from a lag.** BPM = 60 / τ (τ in seconds per beat). Worked: 60 / 0.5 = 120; 60 / 1.0 = 60.
  The measured one-beat peak is at 0.511 s (one 23 ms frame from 0.5 s); the screen shows the ideal
  divisions the narration speaks, and the peak marker says 0.5 S.

## Not claimed

- How any named app (Spotify, rekordbox, Serato, Traktor) computes tempo internally: none document it.
- Typical BPM ranges for genres: only practitioner charts exist, and they disagree.
- Any failure rate for swing, triplets or 3/4 beyond my own forty grooves.
- That synthetic grooves behave exactly like recordings: the result is stated as my test, on my grooves.
