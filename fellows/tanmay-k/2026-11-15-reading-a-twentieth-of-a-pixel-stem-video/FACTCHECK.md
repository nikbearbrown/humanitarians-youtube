# FACTCHECK — Reading a Twentieth of a Pixel (Week 31), pass 1 on draft 1 scripts

Verdicts: SUPPORTED / QUALIFY (true with a label the film must show) / OUR OWN (from our simulation, reproducible).
Checked 2026-11-16. Public values were looked up by web search; secondary pages are named, primary papers where found.

## Public values
| Claim (where) | Verdict | Evidence |
|---|---|---|
| H-alpha rest wavelength 656.28 nm in air (B02) | SUPPORTED | 656.28 nm air / 656.46 nm vacuum in standard references (Wikipedia "Hydrogen-alpha", EPFL concept page, LibreTexts Tatum "The Hydrogen Spectrum"); those cite NIST ASD. **NIST ASD itself opened 2026-11-17** (Lines form, H I, 600 to 700 nm; page states wavelengths are air between 200 and 2000 nm): H-alpha observed 656.279 nm (air), Ritz 656.2819 nm (air); the film's 656.28 nm is that value rounded. Film says "in the lab ... six hundred fifty-six point two eight" (air). |
| Shift = (v/c) x rest wavelength (B02, slow speeds) | SUPPORTED | Non-relativistic Doppler; valid at 300 km/s (v/c = 0.001). |
| Andromeda approaches at about 300 km/s measured from the Sun (B02, B08) | SUPPORTED | -301 km/s (van der Marel & Guhathakurta 2008; Chemin et al. 2009), -300 +/- 4 km/s (McConnachie 2012). |
| Galactic-frame approach about 109 km/s (B08) | SUPPORTED | -109.3 +/- 4.4 km/s, van der Marel et al. 2012, "The M31 velocity vector II" (arXiv:1205.6864). A 2018 M31 globular-cluster paper (arXiv:1810.10719) states -301 heliocentric corresponds to -109 +/- 4 Galactocentric. |
| "Most of that three hundred is us" (B08) | SUPPORTED, computed | 301 - 109 = about 192 km/s is the Sun's own motion projected toward Andromeda: 64% of the Sun-frame figure. Sun's speed itself is about 232 to 246 km/s depending on definition (IAU 232; 239 +/- 9; 245.6 total / 233.4 LSR from GRAVITY note); the film does NOT quote it. |
| Andromeda shift about 0.66 nm (B02) | OUR OWN arithmetic | 656.28 x 300 / 299,792.458 = 0.657 nm; 13.1 pixels of 0.05 nm. |
| 1 km/s = 0.0022 nm at H-alpha (B00) | OUR OWN arithmetic | 656.28 / 299,792.458 = 0.00219 nm. |

## Our measurements (`experiment/photon_precision.py`, numpy, seed 31)
| Claim | Verdict | Evidence |
|---|---|---|
| Ten photons: off by about fifteen km/s, most of a pixel (B04) | OUR OWN | RMS 14.6 km/s = 64% of a 22.84 km/s pixel. |
| A hundred: four point six; a thousand: one point four; six percent of a pixel (B05, S03) | OUR OWN | 4.60, 1.45 km/s; 6.3% of a pixel (2,000 trials each). |
| Rule: error = width / sqrt(photons), held to within about eight percent from ten to a hundred thousand (B06) | OUR OWN | Ratio measured/theory 1.06 to 1.09 over 10 to 100,000 photons; theory uses line sigma = 100/2.3548 = 42.47 km/s. |
| Price list: 4.6 at 100, 0.46 at 10,000, 0.14 at 100,000 (B07) | OUR OWN | 4.60, 0.46, 0.14 (rounded 0.142). Each x100 in light = x10 in precision (check: 4.60 to 0.46 to 0.142 is x10, x3.2 per further x10 in light because the last step is x10 in light; narration says "tenfold gain costs hundredfold light", which holds for 100 -> 10,000 and 1,000 -> 100,000). |
| Exercise: 5 km/s needs (42.5/5)^2 = about 72, closer to 85 with pixels (B11) | OUR OWN | Sim RMS at 72 photons = 5.3 km/s; at 85 = 5.05 km/s (4,000 trials). |
| Sky glow: ten times as many glow photons as line photons took the error at 1,000 line photons from 1.4 to 3.4 km/s (B10, S06 "more than doubles") | OUR OWN | `experiment/sky_glow.py` (seed 31, 2,000 trials each): 1,000 line + 0 glow = 1.44; + 1,000 glow = 1.67 (1.24x the rule); + 10,000 glow = 3.37 (2.5x the rule). Same estimator, no background subtraction, glow flat over the +/-600 km/s window. At 100 line photons + 1,000 glow: 7.31 vs 4.69. Real pipelines subtract background; the film says only what this simulation did. |
| Toy disk: edge bars ten times centre bars (B09) | OUR OWN, toy | `rotation_bars.py`: exponential disk, scale length 3 kpc (assumed), centre ring 100,000 photons, error 0.17 km/s at 1 kpc to 1.77 at 15 kpc = 10.4x. Must be labelled "toy disk, assumed" on screen. |

## Qualifications the film must carry
1. **The pixel is ours.** 0.05 nm (22.8 km/s) is the simulation's choice; real spectrograph pixels vary. Label on screen. B00's "can be more than twenty times wider" is true of this pixel only.
2. **Width 100 km/s is our choice** for the line; real lines differ.
3. **Mostly ideal case.** Sky glow was tested (B10, S06); blended lines and calibration error were not, and the film says so.
4. **No telescope data.** Nothing here was measured on an instrument (B10).
5. **The toy disk is not a measured galaxy** and the film does not argue the dark-matter case.
6. **Quoted precision of real surveys is not claimed.** The film asks why precise speeds need many photons; it does not state how real catalogues achieve their errors.

## Pending before sign-off
- Phonemes: check Kokoro reads "v over c", "nanometres", "hydrogen-alpha", "Andromeda" (no years or acronyms in the script).
- ~~Open NIST ASD to confirm 656.28 directly~~ Done 2026-11-17 (see row above).
- Confirm Earth/Sun motion wording is not used on screen beyond the values above.
