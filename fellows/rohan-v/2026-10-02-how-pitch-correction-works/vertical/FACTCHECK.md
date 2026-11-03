# FACTCHECK — How Pitch Correction Works

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-10-05.
"The run" means `pitch_demo.py` → `evidence/run.log` / `evidence/pitch_demo.json`
(SHA-256 recorded in `MEASUREMENTS.txt`). The voice in the run is a **synthesised test
signal**, labelled as such on screen; no real singer is measured or claimed.

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md`, required wording | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure line + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | Every singer drifts a little, even good ones | general statement about live singing; not measured here | ✅ as framing; no number attached |
| 4 | B01 | A sung note is a vibration that repeats; faster repeats = higher note | physics of periodic sound (pitch ≈ fundamental frequency) | ✅ |
| 5 | B01 | The A above middle C is 440 Hz | ISO 16 standard tuning, A4 = 440 Hz | ✅ |
| 6 | B01 | Double the frequency, an octave higher | octave = 2:1 frequency ratio | ✅ |
| 7 | B01 | 100 cents between neighbouring piano keys; 1200 to the octave | cent definition (Ellis 1885), equal temperament: semitone = 2^(1/12) = 100 cents | ✅ |
| 8 | B02 | The detector slides a copy of the sound along itself; the difference drops almost to zero at one period | the run: YIN cumulative-mean-normalised difference at the worked frame (t = 2.56 s) is 0.01 at 51.27 samples (`worked_example.cmnd`) | ✅ measured, shown as the run's own curve |
| 9 | B02 | Here the period is 2.33 ms, so the note is 430 Hz | 51.27 samples ÷ 22,050 Hz = 2.325 ms; 1 / 2.325 ms = 430.08 Hz | ✅ measured |
| 10 | B02 | The first Auto-Tune found pitch with the same idea, autocorrelation | Wikipedia, "AutoTune": Hildebrand's "method for detecting pitch involved autocorrelation"; released by Antares, September 1997 | ✅ — our detector is YIN (de Cheveigné & Kawahara 2002), a difference-function refinement of autocorrelation: d(τ) = r(0) + r_τ(0) − 2r(τ). The chip says "the idea behind", not "the same algorithm" |
| 11 | B03 | 430 Hz is just below A (440) | nearest equal-tempered note to 430.08 Hz is A4 | ✅ |
| 12 | B03 | Cents = 1200 × log₂ of the ratio; this note is −39.5 cents | 1200 · log₂(430.08 / 440.0) = −39.49, computed by `export_pitch_data.py` and asserted against the run | ✅ computed; typeset with `typeset_math.py` |
| 13 | B03 | So the target is A, a raise of almost forty cents | +39.5 cents | ✅ |
| 14 | B04 | Seven sung notes, each a little off, a scoop into each, vibrato on the long ones | `pitch_demo.py` MELODY: detunes −28…+22 and −75 cents; 90-cent scoop over 70 ms; 5.5 Hz ±22-cent vibrato from 0.18 s | ✅ (synthesised, labelled TEST SIGNAL) |
| 15 | B04 | On average forty cents out | run.log: "before correction: mean 39.9 cents off the nearest C-major note" | ✅ measured |
| 16 | B04 | Measured every six milliseconds | hop 128 samples ÷ 22,050 Hz = 5.8 ms (on screen: 5.8 ms) | ✅ rounded in speech |
| 17 | B04 | Measured again afterwards, under three cents out | run.log: instant / C major, re-measured mean 2.8 cents from target | ✅ measured on the corrected audio, not assumed |
| 18 | B04 | The listening clips are the melody as sung, then corrected | `evidence/sung.wav`, `evidence/corrected_instant.wav`, appended unedited by `mix_listen.py` (level matched only) | ✅ |
| 19 | B05 | Instant correction removes the slides and vibrato, leaving flat steps | the run's re-measured instant curve on the held note (B05 left panel) | ✅ measured |
| 20 | B05 | That robotic sound was made famous by Cher's "Believe" in 1998 | Wikipedia, "AutoTune": "Cher's 1998 song 'Believe' popularized the use of AutoTune to deliberately distort vocals … known as the 'Cher effect'" | ✅ |
| 21 | B05 | Pull slowly, over a quarter of a second, and the vibrato survives | glide time constant 250 ms; vibrato visible in the re-measured curve (B05 right panel) | ✅ measured |
| 22 | B05 | Nineteen cents from perfect | run.log: natural (250 ms), re-measured mean 19.2 cents | ✅ measured |
| 23 | B05 | "Instant, then slow" clips | `corrected_instant.wav`, `corrected_natural.wav` | ✅ |
| 24 | B06 | The last note is 75 cents below G, closer to F♯ | MELODY last note G4 at −75 cents → 25 cents above F♯4 | ✅ |
| 25 | B06 | Allowed every note, it lands on F♯, in tune and wrong | run: chromatic, last note re-measured on F♯4 (100% of held frames, midi 65.95–66.04) | ✅ measured |
| 26 | B06 | In C major F♯ isn't allowed, so it goes to G | C major = C D E F G A B; run: C-major last note re-measured on G4 (100% of held frames) | ✅ measured |
| 27 | B07 | Set the key and scale first; slow speed for a natural voice; listen | advice that follows from B05 and B06; key/scale and speed controls are standard in pitch correctors (Wikipedia, "AutoTune": "If you've assigned it a key …") | ✅ as advice |

## Algebra, checked separately from the typography (MATH-TYPESETTING.md)

- **Rule.** c = 1200 · log₂(f / f_note). Free variables: the measured frequency f and the
  reference note frequency f_note; c is in cents. Positive c = sharp, negative = flat.
- **Worked case.** f = 22,050 / 51.27 = 430.08 Hz; f_note = 440.0 Hz (A4):
  1200 · log₂(0.97745) = 1200 × (−0.032908) = −39.49 ≈ −39.5. Computed twice independently
  (`pitch_demo.py` from the unrounded detector output; `export_pitch_data.py` from the
  rounded period, asserted to agree within 0.06 cents) and drawn by the tuner needle.
- **Approximation vs equality.** "≈ −39.5" is rounded and typeset with ≈.
- **Renderer.** Both rows are outlined SVG from `runtime/scripts/typeset_math.py`
  (matplotlib MathText, STIX); no raw-text fallback.

## What the reel does not claim

- That Auto-Tune today uses YIN, this snap rule or TD-PSOLA. The run is a small, labelled
  model of the idea; commercial internals are not published.
- That the synthetic voice is a person, or that its numbers describe real singers.
- Any listening-test result ("sounds human"): B05 says the vibrato *survives*, which is
  measured; "still moves like a voice" refers to that movement.

## One correction made during the build

The last note was first written 62 cents flat. At that depth the vibrato's peaks crossed
the halfway point (66.5), so the chromatic result flickered between F♯4 and G4: a real
behaviour, but not what B06 says. The note was moved to 75 cents flat, the run repeated,
and every number spoken in B04–B06 re-checked and re-voiced (40, 19, 75). See BUILD-LOG.
