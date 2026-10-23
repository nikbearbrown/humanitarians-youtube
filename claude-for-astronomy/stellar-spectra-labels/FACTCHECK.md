# FACTCHECK — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels` · AI in Astronomy & Space Science
Every on-screen claim, with its status and its source. Checked 2026-10-23.

The reel keeps two categories strictly apart, on screen and in the voice:

- **PUBLISHED** — a result from the literature or a survey's own documentation.
  Carries a visible `PUBLISHED` chip and a citation line.
- **COMPUTED IN THIS REEL** — produced by `assets/gen_stars.py` on seed 1414.
  Carries a `computed in this reel` citation line. It is an illustration of a
  mechanism, never a measurement of any real catalogue.

---

## Beat by beat

### B00 — cold open (ask)
| Claim | Status | Source |
|---|---|---|
| Data-driven models read spectra and return Teff / log g / composition faster than fitting physics | PUBLISHED | Ness et al. 2015 abstract; the Cannon is ~10³ faster than full spectral fitting and this is its stated motivation |
| "it has no physics in it — only the labels it was given" | PUBLISHED | *"Beyond the reference labels, The Cannon makes no use of stellar models nor any line-list"* |
| 0.03 / 0.13 dex, the Teff line | COMPUTED | `gen_stars.py` |

The composer output lines are the reel's own three findings, not quotations.

### B01 — presenter
No factual claim. "Thirteen episodes" is this series' own count; Ep. 14 is the
fourteenth, so thirteen precede it.

### B02 — the whole idea
| Claim | Status | Source |
|---|---|---|
| "nobody measures a star directly — the labels come from a physics model" | PUBLISHED | DR14: *"we have trained the Cannon on the ASPCAP stellar parameters and abundances"*; ASPCAP is a synthetic-spectrum fitting pipeline |
| "the AI learns the labels and nothing else" | PUBLISHED | Ness et al., as above |
| "so it predicts the model, not the star" | PUBLISHED, in the survey's words | DR14: *"the Cannon results are not an independent determination of these"* |

This beat makes no computed claim. It is a restatement of what the method's
authors and the survey's documentation both say plainly, which is why it can
be asserted this early and this flatly.

### B03 — the method
| Claim | Status | Source |
|---|---|---|
| 542 reference stars | PUBLISHED | *"only 542 stars in 19 clusters as reference objects"* |
| 56,000 stars labelled | PUBLISHED | Ness et al. 2015, applied to APOGEE DR10 |
| no stellar models, no line list | PUBLISHED, verbatim | Ness et al. 2015 abstract |
| **the isotype's scale** | HONEST BY CONSTRUCTION | One mark = 100 stars in *both* blocks: 5 marks against 560. The caption states the rate. The picture is the ratio, not a decoration of it. |

### B04 — what it reads
| Claim | Status | Source |
|---|---|---|
| Same Teff and log g, three metallicities; more metal, deeper lines | COMPUTED, and standard physics | `spectra.py` builds absorption depth as a monotone function of [Fe/H] at fixed Teff/log g. The direction is textbook; the magnitudes are illustrative. |
| The guide marks one line that deepens down the stack | COMPUTED, MEASURED | Pixel 47 of 160 is the most metal-sensitive line in the frozen bank: normalised flux 0.365 at [Fe/H] = −0.90 against 0.020 at +0.35, a depth gain of 0.345. The guide's x-position is that measurement, not an eyeball. |
| "it never learns why" | PUBLISHED | Ness et al.: no models, no line list |

### B05 — the chain
| Claim | Status | Source |
|---|---|---|
| star → spectrum → physics model → data-driven model | PUBLISHED | This is the literal training path described by DR14 |
| "only the first one is nature" | EDITORIAL, and defensible | Links 2–4 are an instrument, a code and a fit. The claim is about where the information enters, not a disparagement of any of them. |

### B06 — it agrees with its teacher
| Claim | Status | Source |
|---|---|---|
| rms against its training labels = **0.033 dex** | COMPUTED | `gen_stars.py`, 400 test stars |
| "this is the plot a paper shows" | EDITORIAL | Agreement-with-labels is the standard validation figure. The reel does not claim any specific paper shows only this. |

### B07 — and against the truth
| Claim | Status | Source |
|---|---|---|
| rms against truth = **0.128 dex**, on the same stars and the same fit | COMPUTED | `gen_stars.py` |
| "four times worse than it looked" | COMPUTED | 0.128 / 0.033 = 3.9× |
| "nothing about the model changed" | TRUE BY CONSTRUCTION | B06 and B07 plot the *same* `pred` array; only the x-axis differs |

**Why a simulation is the honest instrument here.** The claim is a gap between
agreement-with-labels and agreement-with-truth. Measuring it requires knowing
the truth. For real stars nobody does — that is the whole problem. So the gap
can only be demonstrated where truth exists by construction, and the reel says
so on screen every time.

### B08 — precision is not accuracy
| Claim | Status | Source |
|---|---|---|
| repeat-measurement scatter = **0.008 dex** | COMPUTED | 120 stars × 3 fresh noise draws, same fitted model |
| the real error is **15×** that | COMPUTED | 0.1280 / 0.0083 = 15.3× |
| "the error bars describe neither" | COMPUTED | 0.008 describes neither 0.033 nor 0.128 |
| the thesis itself | PUBLISHED | DR14: *"this precision may not reflect higher accuracy, if the correlations are not present over the entire data set"* |

### B09 — the error has a shape
| Claim | Status | Source |
|---|---|---|
| correlation with Teff = **0.995**, slope **+0.18 dex per 1000 K** | COMPUTED | `gen_stars.py` |
| "a bias shaped like astrophysics, which survives every check that compares averages" | EDITORIAL, and arithmetically true | A zero-mean trend has, by definition, no mean offset to detect. The teacher's bias here is zero-mean by construction about the pivot. |

**Disclosed plainly:** the trend is in the simulation *because it was put
there*. `teacher_labels(bias=0.18)` is the injected systematic. The reel never
claims ASPCAP has a 0.18 dex/kK metallicity trend. The claim is the weaker and
true one: *if* a label source carries a trend, a data-driven student
reproduces it while reporting a precision that cannot see it.

### B10 — the tell
| Claim | Status | Source |
|---|---|---|
| control, unbiased teacher = **0.013 dex**, correlation −0.131 | COMPUTED | `gen_stars.py` |
| 120 independent anchor stars = **0.032 dex**, correlation −0.139 | COMPUTED | `gen_stars.py` |
| "four times fewer, four times more accurate" | COMPUTED | 500/120 = 4.2× fewer; 0.1280/0.0318 = 4.0× more accurate |
| asteroseismic anchors are more independent than spectroscopic ones | PUBLISHED | APOKASC (arXiv:1410.2503); gravities from oscillation frequencies do not come from the atmosphere model |
| **the anchor is not perfect either** | PUBLISHED, and said on screen in B11 | TESS-vs-APOGEE (arXiv:2307.13853): agreement <5%, largest offsets for clump stars, quoted uncertainties underestimated by ~2×; and arXiv:2310.19872, a real calibration error on the asteroseismic scale |

### B11 — verdict (artefact)
Five lines, each traceable above. Line 5 is the anchored result; line 4 the
trend; line 3 the three numbers; lines 1–2 the published inheritance.

### B12 — handoff
A prompt. No claim.

### B13 — outro
Title, handle, series position.

---

## Claims considered and REFUSED

| Candidate | Why it was dropped |
|---|---|
| "The Cannon's published abundances are wrong by ~0.1 dex" | Not supported by anything measured here, and not what the simulation shows. The reel measures its own simulation only. |
| "Data-driven stellar models are unreliable" | Contradicts the sources. The method does exactly what its authors claim, including the caveat. The episode's point is about label provenance, not method quality. |
| "Asteroseismology is ground truth" | The sources say otherwise — offsets by evolutionary state, mass-dependent discrepancies, underestimated uncertainties, and one real calibration bug. The reel says "more independent", never "independent". |
| "AI can determine stellar distances faster than manual analysis" | In the brief's one-liner, but distance runs through parallax and a different inference chain. Claiming it on this reel's evidence would be unsupported. Logged in SOURCES.md as deliberately not used. |
| A fourth plate of fitted per-pixel coefficients | True and pretty, but it supported no beat. Cut. |

---

## Numerical reproducibility

`assets/gen_stars.py` on **seed 1414** prints every figure above and
**asserts all three central claims**, writing no plate if any fails. Re-run:

```
.venv/Scripts/python.exe -I assets/gen_stars.py
```

Verified reproducing identically on 2026-10-23:

```
  precision (repeat measurement) 0.0083 dex
  vs teacher labels  rms 0.0329
  vs truth           rms 0.1280  bias +0.0263
  teacher vs truth   rms 0.1348
  error vs Teff: correlation 0.995  slope +0.178 dex/kK
  control  (unbiased teacher) 0.0129  corr -0.131
  anchored (120 stars)        0.0318  corr -0.139
  -> all three hold. writing plates.
```

The constants printed on screen live in `scenes.py` as named values
(`PRECISION`, `VS_LABELS`, `VS_TRUTH`, `CORR`, `SLOPE`, `CONTROL`,
`ANCHORED`) so a changed experiment cannot silently disagree with a label.
