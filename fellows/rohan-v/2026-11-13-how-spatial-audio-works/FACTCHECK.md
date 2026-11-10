# FACTCHECK — How Spatial Audio Works

Status: claims checked 2026-11-10 by Claude (Claude Code) against `week-12/_research/facts-spatial.md` and
`evidence/run.log`, after the B04 and B06 fixes below; Rohan V.'s review of the 4K finals still to come.

Every spoken and on-screen claim, its source, and its verdict. "The run" means `spatial.py` →
`evidence/run.log` / `evidence/results.json` / `evidence/scene.json`. It is a **model**: a textbook spherical head,
8.75 cm in radius, at 48 kHz with sound at 343 m/s; timing from Woodworth's spherical-head formula, applied as a
fractional delay; the head's shadow as the Brown-Duda one-pole/one-zero filter per ear; a simple outer-ear
stand-in (a gentle high cut for sounds from behind); a broadband noise burst for the measurements and a
Karplus-Strong plucked-string melody for listening (seed 1113). **Nothing here is Apple's code or Apple's
method.** Apple describes its renderer only as "directional audio filters" and never uses the term HRTF
(facts-spatial §2.8). Facts about hearing, HRTFs, Apple and Dolby, with URLs, dates and confidence levels:
`week-12/_research/facts-spatial.md` (summarised in SOURCES.md). B01–B06 are HyperFrames compositions with
three.js scenes, written by `build_hf.py` from the run's files. Confidence: HIGH / MED / LOW as graded in the fact
sheet; "measured" = a number from the run. Verdicts: PASS, CORRECTED (changed in the film after review), EXEMPT
(a drawing, not a claim).

| # | Beat | Claim | Source | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` | — | PASS (verbatim) |
| 2 | B00 | AI narration disclosed | on screen "Narration: AI voice (Kokoro af_bella), script by Rohan V." + `metadata.ai_disclosure` | — | PASS |
| 3 | B00 | I built a small version to see how; screen "time the gap between your ears / shade the far ear / keep the sound still when you turn" | `spatial.py` sections 1, 2 and 4 | — | PASS |
| 4 | B01 | Your brain finds a sound with two ears; a sound on your right reaches your right ear first | §1.1, §1.4 | HIGH | PASS |
| 5 | B01 | In my head model, straight out to one side, the gap is about two thirds of a millisecond | run: "maximum (90 deg, straight to one side): 0.661 ms" (formula 0.656 ms); screen "0.66 ms · GAP BETWEEN YOUR EARS", "SOUND AT 90° RIGHT". Published range for real heads ~630–763 µs (§1.5) | measured; §1.5 MED/HIGH | PASS |
| 6 | B01 | … and it shrinks to nothing as the sound moves in front of you | run: "0 deg: measured 0.000 ms"; screen "SOUND STRAIGHT AHEAD"; landscape note "Straight ahead, the gap is zero." | measured | PASS |
| 7 | B01 | On screen: "GAP vs DIRECTION · MY HEAD MODEL", seven points from "AHEAD 0°" to "SIDE 90°" | run rows 0, 15, 30 … 90 deg: 0.000, 0.133, 0.266, 0.388, 0.500, 0.586, 0.661 ms. The live readout interpolates between them as the source glides | measured | PASS |
| 8 | B01 | On screen: wavefronts, a straight cyan path to the near ear, a violet path wrapping round the head to the far ear | `scenes/B01.js`: waves slowed about 100,000× so they can be seen; the wrap follows the same formula's geometry | — | EXEMPT (illustration) |
| 9 | B02 | Your head casts a shadow; high sounds can't bend around it, so the far ear hears them quieter | §1.7 | HIGH | PASS |
| 10 | B02 | Fourteen decibels quieter in my model | run: "high band (3-6 kHz) 14.0 dB"; screen "HIGH SOUNDS · 3–6 kHz · 14.0 dB QUIETER IN THE FAR EAR". Real heads: about 20 dB at 4 kHz (§1.7), so my model is milder; the narration says "in my model" | measured | PASS |
| 11 | B02 | Low sounds bend around, so only two | run: "low band (350-700 Hz) 2.3 dB"; screen "LOW SOUNDS · 350–700 Hz · 2.3". Spoken "two" rounds 2.3. Below about 1 kHz ILDs are negligible (§1.7) | measured | PASS |
| 12 | B02 | Timing for low sounds, loudness for high ones; Lord Rayleigh worked that out in 1907 | §1.1 ("On our perception of sound direction", *Philosophical Magazine*, Feb 1907); landscape screen "LOW SOUNDS use timing / HIGH SOUNDS use loudness", "Lord Rayleigh, 1907: the “duplex” theory." No cutoff frequency is stated (the crossover is gradual, §1.3) | HIGH | PASS |
| 13 | B03 | A sound in front of you and its mirror behind you give your ears the same timing and the same loudness | §1.8 (cone of confusion) | HIGH | PASS |
| 14 | B03 | In my model, exactly the same | run: "head only: ITD 0.266 vs 0.266 ms; spectra differ by 0.00 dB on average"; screen "IN FRONT · 30°" and "BEHIND · 150°", each "0.266 ms GAP · SAME LOUDNESS"; chart "HEAD ONLY · 0.0 dB APART". True by construction of a symmetric sphere (below) | measured | PASS |
| 15 | B03 | Your outer ears break the tie: their folds change the high notes depending on where a sound comes from | §1.9 (pinna peaks and notches, about 4 kHz and up; main cue for front/back) | HIGH | PASS |
| 16 | B03 | On screen: "WITH OUTER EARS · 2.6 dB APART" | run: "with the outer-ear filter: spectra differ by 2.6 dB". My stand-in (a high cut for sounds from behind), not a measured outer ear; it has no peaks or notches | measured | PASS (model) |
| 17 | B04 | Researchers measure all of this with microphones inside a dummy head's ears | §2.2 (microphones in the ear canals, test sounds from many directions); §2.4 (KEMAR, a manikin, MIT 1994) | HIGH | PASS |
| 18 | B04 | … from more than seven hundred directions; screen "710 DIRECTIONS MEASURED" | §2.4: 710 directions, −40° to +90° elevation, 1.4 m loudspeaker, anechoic chamber, May 1994. The 710 dots on screen are laid out evenly on a sphere from −40° up, a schematic, not KEMAR's actual grid (5° at ear level, coarser above) | HIGH | PASS |
| 19 | B04 | Those measurements are called head-related transfer functions | §2.1 (a pair of filters per direction, one per ear) | HIGH | PASS |
| 20 | B04 | Run a sound through the pair for one direction, and headphones play it from there | §2.3 (convolution with one direction's left and right filters). The general method, not a description of Apple's renderer | HIGH (general method) | PASS |
| 21 | B04 | On screen: "MY MODEL'S FILTER PAIR · 60° RIGHT", a cyan and a violet curve | `spatial.py`'s own head-shadow filters for a source at 60° right, evaluated by `build_hf.py` with the same constants; a model pair, not a measured HRTF. The title said "ONE FILTER PAIR" until review; it now says "MY MODEL'S" in both cuts | — | CORRECTED |
| 22 | B04 | "Put your headphones on, and listen": the melody makes one turn around your head | `evidence/circle.wav`; run: "LISTENING: circle.wav (8.0 s, one turn around the head, outer-ear filter on)"; beat sheet `listen_clips`: 18.349–26.349 s into the beat, +3.7 dB. Rendered by my head model: timing, shadow, and the outer-ear filter on the behind half, so the back half of the turn differs from the front half. Still a textbook model, untested with listeners. Landscape note "One turn around your head, rendered by my model." The dial and "NOW FROM: AHEAD / AHEAD-RIGHT / RIGHT …" follow the clip: azimuth = 360° × time ÷ 8 s, starting ahead, turning right | measured | CORRECTED (outer-ear cue added after review) |
| 23 | B05 | Turn your head, and an ordinary headphone mix turns with you | §3.2 (sources that move with the head); §3.8 ("Fixed" = Spatial Audio without head tracking); run §4: "without tracking: … it ends up 40 deg right of where it was"; screen "TRACKING OFF · The sound turns with you." | HIGH | PASS |
| 24 | B05 | Spatial audio uses motion sensors to turn the sound the other way, so it stays put in the room | §3.6 (gyroscope and accelerometer in the headphones and the iPhone or iPad; the sound field kept anchored to the device; Apple-primary for AirPods Max, 8 Dec 2020); run §4: "with tracking: rendered at -40 deg from your nose, so it stays where it was in the room"; screen "TRACKING ON · Motion sensors turn it back: it stays put." Apple anchors the sound to the device; "in the room" is the same thing while the device stays still | HIGH | PASS (simplified) |
| 25 | B05 | On screen: "HEAD 40°", "SOUND 40°" (off) and "SOUND 0°" (on) | run §4, a 40° turn (`turn_deg` 40). The run states this geometry; it measures nothing here | — | PASS |
| 26 | B05 | Apple added this to AirPods in 2020; tag "AirPods · head tracking · 2020" with Apple's mark | §3.5: announced 22 Jun 2020, shipped with iOS 14 on 16 Sep 2020, for AirPods Pro | HIGH | PASS ("AirPods" = AirPods Pro then) |
| 27 | B06 | Everyone's ears are different; screen "EVERY EAR IS DIFFERENT" | §2.6 ("small variations can produce large changes in the HRTF"); §4.3 | HIGH | PASS |
| 28 | B06 | So filters from a dummy head can mix up front and back; screen "Filters from a dummy head can flip front and back.", "FRONT ⇄ BEHIND" | §6.1 (another person's HRTFs: frequent front-back confusions), §6.2, §6.3; §6.5 (generic HRTFs, often from a KEMAR) | HIGH | PASS |
| 29 | B06 | Apple's Personalized Spatial Audio scans your ears with the iPhone's camera to build a profile for you; screen "iPHONE CAMERA EAR SCAN", tag "Personalized Spatial Audio · iOS 16" with Apple's mark | §4.1 (TrueDepth camera, personal profile, 6 Jun 2022), §4.2 (released 12 Sep 2022), §4.4 (a front view, then the right ear and the left ear), §4.5 (processed on the device) | HIGH | PASS |
| 30 | B06 | Scan card, second line: "THE SHAPE OF YOUR EAR" | §4.3 (Apple: sound is perceived by "the size and shape of their head and ears"), §4.4. Until review the card counted up to "3200 POINTS", the size of the drawn ear, which no source supports; the counter is removed | HIGH | CORRECTED |
| 31 | B06 | Landscape spark line "An ear scan builds a profile just for you." | §4.1, §4.4 (a camera scan builds a personal profile). Until review it read "Your ears, measured, make the filters yours.", close to the fact sheet's "do not say" (§4.7); it no longer claims a measurement or filters | HIGH | CORRECTED |
| 32 | B07 | Use headphones with head tracking | §3.8, §3.9 (model list dated 2026-11-09, so models aren't named); §5.6 | HIGH | PASS (as advice) |
| 33 | B07 | Set up the personalized profile | §4.4, §4.5 | HIGH | PASS (as advice) |
| 34 | B07 | Pick music mixed in Dolby Atmos | §5.4, §5.5 (Apple Music, June 2021), §5.6 (only select songs) | HIGH | PASS (as advice) |
| 35 | B07 | Lede "Timing, shadow and your ears, rebuilt in your headphones."; spark "Two ears, and a little maths." | summary of B01–B06 | — | PASS |
| 36 | B08 | "A tiny delay, a shadow, and the shape of your ears." | summary of B01–B03 | — | PASS |

## The listener and the scenes are drawn, not captured

The listener in every 3D scene is the textbook spherical head that `spatial.py` measures: a glass sphere with two
ears (right cyan, left violet) and a small nose. It is never a person. The three ears in B06 are seeded point clouds
(rim, inner fold, bowl, lobe), the phone and its scan line are drawn, and the room in B05 is a floor grid with four
posts. None of it is a scan, a screenshot or Apple artwork, except Apple's mark beside its name (LOGO LAW,
`hyperframes/assets/apple-01.svg`).

## Arithmetic, checked separately

- **Timing.** Woodworth's formula is ITD = (a/c)(θ + sin θ). At θ = 90°: 0.0875 ÷ 343 × (π/2 + 1) = 0.656 ms, the
  run's "formula 0.656 ms". The fact sheet's 654 µs (§1.5) uses c = 344 m/s. The run *measures* 0.661 ms from the
  cross-correlation peak of the two rendered ears (8× upsampled). My reading of the small difference (0.005 ms at
  90°, 0.012 ms at 60°): the two ears' head-shadow filters add a little phase difference of their own. Either way,
  "about two thirds of a millisecond".
- **Shadow.** Each ear's Brown-Duda filter is H(s) = (1 + α s/2ω₀) ÷ (1 + s/2ω₀), with ω₀ = c/a, so its corner is
  2c/a ≈ 7,840 rad/s ≈ 1.25 kHz. α = 2.0 for the near ear at 90°; for the far ear α = 1.05 + 0.95 × cos(180°/150° ×
  π) ≈ 0.28. At very high frequencies they differ by 20 log₁₀(2.0 ÷ 0.28) ≈ 17 dB; the run's 3–6 kHz band gives
  14.0 dB and its 350–700 Hz band 2.3 dB, consistent with that shape.
- **Front and back.** The timing uses the lateral angle (arcsin of sin θ), and 30° and 150° share it; each source
  is 60° from the right ear's axis and 120° from the left's. So the head alone gives the two ears the same thing
  for both, **by construction**: the run confirms the code, it isn't a discovery. A real head isn't front/back
  symmetric, which is why the outer ear matters (§1.9).
- **Outer-ear stand-in.** For a source behind: 0.45 × the sound + 0.55 × the sound low-passed at 3.5 kHz, a cut that
  levels off near 20 log₁₀ 0.45 ≈ −6.9 dB. The run's 2.6 dB is the mean absolute difference over twelve log-spaced
  bands from 1 to 12 kHz (the larger of the two ears). Also by construction.
- **The circling clip.** 16 notes × 0.5 s = 8.0 s. Rendered in 4,096-sample blocks with a 2,048-sample hop (42.7 ms
  at 48 kHz), one direction per block: about 1.9° per hop. Blocks whose direction is behind the ear axis (90° to
  270°, the middle half of the clip) get the outer-ear filter. In B04's audio the clip starts at 17.75 s of
  narration + 0.6 s pause = 18.349 s and ends at 26.349 s; a 0.8 s tail makes the beat 27.15 s. The reel totals
  128.22 s.

## Not claimed

- That `spatial.py` is Apple's method, or how Apple renders (§2.8, "do not say"); that Apple uses HRTFs by that
  name; how the camera scan becomes a profile (§4.7).
- That 0.66 ms, 14 dB, 2.3 dB or 2.6 dB are real-head numbers. They are the textbook sphere's; real heads give
  about 630–763 µs (§1.5) and about 20 dB at 4 kHz (§1.7).
- A hard crossover frequency between timing and loudness (§1.3, "do not say").
- That the circling clip is heard behind you. Its behind half carries my outer-ear stand-in, a simple high cut, not
  a real ear's peaks and notches, and it hasn't been tested with listeners; the picture says where it is.
- Any AirPods head-tracking latency, accuracy in degrees, or size of improvement from personalisation (§3.4, §6.7).
- Any list of current AirPods models (§3.9, §4.6 are dated).
- That the 710 dots are KEMAR's real grid, or that the drawn ear or phone are Apple's scan.
