# FACTCHECK — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · the series finale
Every on-screen claim, with its status and its source. Checked 2026-10-31.

Two categories, kept strictly apart on screen and in the voice:

- **PUBLISHED** — from the literature. Carries a visible `PUBLISHED` chip and
  a citation line.
- **COMPUTED IN THIS REEL** — produced by `assets/gen_conj.py` on seed 1515.
  Carries a `computed in this reel` citation. It is an illustration of a
  mechanism, never a measurement of any real catalogue or operator.

---

## Beat by beat

### B00 — cold open (ask)
| Claim | Status | Source |
|---|---|---|
| Operators screen close approaches and act on a probability threshold | PUBLISHED, uncontroversial | Standard conjunction-assessment practice; ESA's challenge is built around exactly this decision |
| "it is not P(collision) — it is P(collision given your covariance)" | PUBLISHED | Definitional: Pc is the Gaussian mass over the hard-body disk *given a covariance* |
| the three result lines | COMPUTED | `gen_conj.py` |

### B01 — presenter
No factual claim. "Fifteen episodes" is this series' own count; this is the
fifteenth and last.

### B02 — the whole idea
| Claim | Status | Source |
|---|---|---|
| Pc is not the chance two satellites hit, but the chance given your uncertainty | PUBLISHED, definitional | Foster's method computes exactly this integral |
| "make your uncertainty bigger and the number gets smaller" | PUBLISHED | Balch, Martin & Ferson 2019: probability dilution. Verbatim: *"it results in a severe and persistent underestimate of collision risk exposure"* |

This beat makes no computed claim. It restates what the quantity is.

### B03 — the benchmark
| Claim | Status | Source |
|---|---|---|
| 15,321 close approaches | PUBLISHED | Uriot et al. 2020 |
| 199,082 warning messages, ≈13 per approach | PUBLISHED | Uriot et al. 2020 |
| 30 were ever genuinely dangerous | PUBLISHED | Uriot et al. 2020: 30 events at risk ≥ 1e-4 |
| "collected over four years" | PUBLISHED | The dataset spans 2015–2019 |
| **the isotype's scale** | HONEST BY CONSTRUCTION | One mark = 10 close approaches throughout. 1,532 marks, of which 3 are terracotta. The caption states the rate; the ratio is the picture, not a caption on it. |

**"Genuinely dangerous" is the reel's wording, not ESA's.** The published fact
is "30 events reached a final risk of 1e-4 or above". 1e-4 is the threshold
most often quoted for considering a manoeuvre, so the paraphrase is fair, but
it is a paraphrase.

### B04 — what the number is
| Claim | Status | Source |
|---|---|---|
| Pc is the share of the position-error distribution landing on the hard-body disk | PUBLISHED, definitional | Foster's method |
| Same probability, wider spread, less on the disk | COMPUTED, and arithmetically necessary | The plate's three panels share ONE density scale |
| disk twenty metres across | COMPUTED, illustrative | `HBR = 20.0`; operators use 5–50 m. The effect depends on R/d, not on R. |

**The three panels share one density scale.** An earlier version normalised
each panel to its own maximum, which rendered the worst-tracked panel as
solid ink — reading as "certain everywhere", the exact opposite of the truth.
A display gamma of 0.25 is applied so the thinnest field is still visible;
without it the third panel is blank at 1e-4 of the first.

### B05 — the curve has a summit
| Claim | Status | Source |
|---|---|---|
| Track badly → Pc tiny | COMPUTED | 8.0e-6 at σ = 5 km |
| Track perfectly → Pc tiny again, because they miss | COMPUTED | →0 as σ→0 for d > R |
| In between it peaks | COMPUTED | Peak **1.635e-3** at **σ = 212.1 m** |
| the peak sits at d/√2 | COMPUTED, and analytically predicted | 300/√2 = 212.1 m. The small-R approximation gives σ* = d/√2; the measured peak matches to better than 0.05 %. |

### B06 — the flip
| Claim | Status | Source |
|---|---|---|
| Tracked well: above the action threshold | COMPUTED | 1.635e-3 > 1e-4 |
| Uncertainty 7× larger: below it | COMPUTED | Pc crosses 1e-4 at σ = 1397.7 m, i.e. **6.6×** the peak σ |
| "the alert quietly goes away" | COMPUTED | At σ = 5 km, Pc = 8.0e-6, 12× below threshold |

**"Seven times" is rounded from 6.6×**, the measured crossing. The plate's
terracotta bar is drawn at σ = 5 km (23.6× the peak), which is further out
than the crossing — so the bar is *below* the threshold rather than *at* it.
Stated here because the narration says "seven times" and the picture shows
more.

**Nothing in this beat suggests anyone degrades tracking deliberately.** It is
a property of the metric, stated as a property.

### B07 — what the forecast is for
| Claim | Status | Source |
|---|---|---|
| Almost every alert decays as tracking improves | COMPUTED | As σ shrinks below d, Pc falls |
| The few that matter climb from the start | COMPUTED | All three drawn climbers begin exactly on the 1e-6 floor |
| "they announce themselves early" | COMPUTED | **Zero** events in 120,000 are quiet at the −2-day cutoff and dangerous at closest approach |

**This plate was redrawn after being measured.** The first version was drawn
to show alerts *breaking late* — quiet until the last message, then jumping.
The population contains **no such events**, and that is not an artefact of
the simulation: once the covariance shrinks below the miss distance, Pc
falls. The plate now shows what is actually there. Logged because it is
exactly the failure the series keeps warning about — drawing the picture you
expected instead of the one you measured.

### B08 — the reversal
| Claim | Status | Source |
|---|---|---|
| Trained model beats "assume nothing changes" 4× on all events | COMPUTED | MSE 0.0152 vs 0.0609 on 40,000 test events |
| It is 3× worse on the notified events | COMPUTED | MSE 4.130 vs 1.275 on the 124 that ever left the floor |
| "same model, opposite verdict" | COMPUTED | Same predictions, two scoring sets |

**The model is a ridge regression, not a competitive architecture.** It is
chosen to make one structural point — that a loss dominated by 99.7 % quiet
events prefers a forecaster that is wrong on the loud ones — not to represent
the state of the art. Saying it beats a baseline "4×" is a statement about
this simulation only.

**"The hundred-odd events anyone was warned about"** = 124 of 40,000 test
events that ended above the 1e-6 notification floor.

### B09 — ninety-seven teams
| Claim | Status | Source |
|---|---|---|
| 97 teams | PUBLISHED | Uriot et al. 2020 |
| only 12 beat the naive forecast | PUBLISHED | Uriot et al. 2020 |
| "surprisingly effective" | PUBLISHED, verbatim | The organisers' own words for the baseline |

The baseline is the **Latest Risk Prediction**, *"the clipped naive
forecast"*: predict the most recent reported risk. The reel's phrase "assume
nothing changes" is a plain-English gloss on that, and the citation line
names the source.

**Not said:** that the teams failed. The top three did beat it (0.556, 0.571,
0.585 against 0.694). The published point the reel uses is the *margin* and
*how few* managed it — *"the scores do not improve much below the LRP
baseline"*.

### B10 — the tell
| Claim | Status | Source |
|---|---|---|
| Giving the model the geometry moved the error three percent | COMPUTED | σ/d as a feature: notified MSE 4.130 → 4.020, **−2.7 %** |
| "the problem was never the features" | COMPUTED, inference | Reweighting the loss moved it 2.4×; a feature moved it 2.7 % |
| max-Pc and Pc give opposite decisions at the same uncertainty | COMPUTED | At σ = 5 km: Pc = 8.0e-6 (no action), max-Pc = 1.635e-3 (act) |
| the bound "stops depending on how hard you looked" | PUBLISHED + true by construction | max-Pc depends only on d and R. Alfano's maximum-probability construction (US7383153B2) |

**max-Pc being scale-free is a property, not a discovery.** It is the whole
purpose of the construction. The reel presents it as a property.

**It is not presented as a solution.** Maximum probability is conservative by
design and would trigger more manoeuvres than operators can fly; the reel
says only that it answers a question that does not depend on your tracking.

### B11 — verdict · B12 — handoff · B13 — outro
Five artefact lines, each traceable above. B12 is a prompt. B13 is title,
handle and series position.

---

## Claims considered and REFUSED

| Candidate | Why it was dropped |
|---|---|
| **"Persistence beats the trained model."** The ORIGINAL hypothesis. | **The measurement refused it.** Persistence is 4× *worse* overall. The claim was rewritten to what was actually measured — the ranking *reverses* between the two scoring sets — which is a sharper point than the one I set out to make. Standing rule from Eps. 11 and 13: when a measurement refuses a claim, rewrite the claim, never tune the experiment. |
| "Alerts break late, so you get no warning" | Drawn, then measured: **zero** such events in 120,000. The plate was redrawn to show the real structure. |
| "σ/d as a feature fixes the tail" | Measured at −2.7 %. Reported as a failed fix, not a fix. |
| "Reweighting fixes it" | 2.4× better on the tail, 15× worse overall, still loses to persistence. Too equivocal to claim; it is in SOURCES.md and the generator output. |
| "Operators are under-reacting to real risk" | Not supported by anything here, and not what the simulation shows. The reel measures its own simulation only. |
| "Probability dilution means Pc is wrong" | The integral is correct. The episode says what it is a probability *of*. |
| Current debris counts, Starlink conjunction rates, Iridium–Cosmos | Verified, deliberately unused — see SOURCES.md. |

---

## Numerical reproducibility

`assets/gen_conj.py` on **seed 1515** prints every figure above and
**asserts all four central claims**, writing no plate if any fails:

```
.venv/Scripts/python.exe -I assets/gen_conj.py
```

Verified reproducing identically on 2026-10-31:

```
  Pc peaks at sigma 212.1 m  (d/sqrt(2) = 212.1)   Pc = 1.635e-03
  Pc crosses 1e-04 at sigma 1397.7 m on the dilution branch
  degraded sigma 5000.0 m -> Pc 7.986e-06
  max-Pc (scale-free)     -> 1.635e-03
  final risk >= 1e-4 : 180 of 120,000 (0.15%)
                        all MSE   notified MSE
  persistence            0.0609          1.275
  ridge                  0.0152          4.130
  ridge_geom             0.0149          4.020
  ridge_weighted         0.2231          1.729
  -> all four hold. writing plates.
```

The constants printed on screen live in `scenes.py` as named values
(`P_GOOD`, `P_BAD`, `INFLATE`, `FACTOR_ALL`, `FACTOR_HI`, `GEOM_MOVE`,
`N_TEAMS`, `N_BEAT`, …) so a changed experiment cannot silently disagree
with a label.
