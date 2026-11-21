# FACTCHECK — Ep. 18, *counting-craters*

Every number spoken or shown, traced to either a published source or to a line
of `assets/craters.py` that `assets/gen_craters.py` asserts. Nine claims are
asserted at generation time; if any fails, no plate is written.

Full citations in `SOURCES.md`.

---

## F1 — "fourteen craters left, eighty right" (B03)

**Status: DERIVED, asserted (C1, C6).**

The two patches in `surface.png` are synthetic. Their only quantitative claim
is the one the code enforces: the counts stand in the ratio the *real*
chronology function gives for those two ages.

```
N(1) at 1.0 Ga = 8.380e-04 /km^2
N(1) at 3.5 Ga = 4.793e-03 /km^2      ratio 5.72
14 craters x 5.72 = 80                 (C6 asserts len(old)/len(young) == ratio)
```

Crater *sizes* are drawn from a truncated power law (`SFD_SLOPE = 1.8`). That
exponent is a **drawing choice** — it controls how many small craters appear
per large one, i.e. what the patch looks like. No spoken number depends on it,
and `craters.py` says so at the point of definition.

**What the narration does NOT claim:** that these are real patches of ground,
or that a real 1.0 Ga surface carries exactly 14 craters in a frame. The
spoken claim is the *comparison*, and the comparison is real.

## F2 — "one Mars catalogue holds three hundred eighty-four thousand craters, built by hand" (B04)

**Status: PUBLISHED. 384,343.**

Robbins & Hynek (2012), JGR 117 — a global catalogue of Martian craters
"statistically complete for diameters D ≥ 1 km", containing **384,343**
craters with positional, morphologic and morphometric data.

**Care taken.** Two other figures circulate and are *not* interchangeable:
~640,000 is the catalogue's total including sub-kilometre craters, and the
2012 press release's "about 635,000" is that rounded total. Robbins' 2011
thesis gives 378,540 from an earlier version. The narration uses the paper's
own complete-census number and the screen labels it "D ≥ 1 km".

## F3 — "go smaller and the population runs to tens of millions" (B04)

**Status: PUBLISHED, as an estimate, and spoken as one.**

Benedix et al. (2020) motivate automation by noting that the number of Martian
craters from 10 m to 1 km "runs into the tens of millions" — manual counting
cannot reach precise local age analysis across a whole surface at that scale.

The screen shows `~10 million+` against a **log** axis with visible decade
rails, never a precise figure. `gen_craters.py` plots it at 3.0e7.

## F4 — "expert counters ... differ by up to forty-five percent" (B05, and on the B11 artifact)

**Status: PUBLISHED. Up to ~±45%.**

Robbins et al. (2014), *Icarus* 234 — agreement among expert crater analysts
depends on crater diameter, the number of craters per diameter bin, and
terrain, with differences up to ~**±45%**. The same work reports volunteers
showing roughly twice the dispersion of experts, and warns specifically about
craters ≤10 pixels across.

**Care taken.** A conference abstract from the same team reports a different
expert scatter (σ ≈ 21–32% over a stated diameter range). These are different
metrics over different ranges and must not be swapped. The episode uses the
journal abstract's envelope figure, says "up to", and cites the paper on
screen.

**What the simulation does NOT do.** `spread.png`'s synthetic analysts are
drawn so that large craters are unanimous and small ones contested — the
*shape* Robbins reports. The ±45% is **cited, never read off the simulation**,
and `gen_craters.py` asserts nothing numerical about the analyst model.

## F5 — "recovers ninety-two percent ... forty-two percent of what it found was new" (B06)

**Status: PUBLISHED. 92% recall (post-processing); ~42% new.**

Silburt et al. (2019), *Icarus* 317 (arXiv 1803.02192) — the DeepMoon UNet on
LRO digital elevation data reports **92%** recall after post-processing, and
about **42%** of the craters it extracted were not in the input catalogues.
The authors estimate an **11%** false-positive rate among new detections from
inspecting 361 of them.

**Care taken — this is the number most easily misreported.** 92% is the
*post-processed* figure. The raw per-CNN recall is **57% ± 20%** (83% ± 16%
for craters under 15 px radius). The episode puts **57% on screen beside the
92%**, ghosted but legible, so the headline cannot stand alone. The authors
themselves note a human recall of ~75% on re-classification is comparable to
the CNN's small-crater recall.

## F6 — "ninety-six percent of the craters landed in the first six hundred million years" (B07)

**Status: DERIVED from the published chronology function, asserted (C5).**

For a surface that formed 4.1 Ga ago, the share of its D>1 km craters
accumulated before 3.5 Ga:

```
1 - N1(3.5)/N1(4.1) = 0.961
```

4.1 → 3.5 Ga is that surface's first 600 Myr. The screen labels the surface
"4.1 Ga" so the number is never floating free.

## F7 — "sixteen percent" / "ninety percent" (B08)

**Status: DERIVED, asserted (C2, C3, C4).** The central computation of the
episode: a ±45% error in crater *count* pushed through the chronology function
and read back out as an error in *age*.

| surface | ±45% count → age window | width | share of the age |
|---|---|---|---|
| 1.0 Ga | 0.55 – 1.45 Ga | 0.90 Gyr | **90%** |
| 3.5 Ga | 3.05 – 3.61 Ga | 0.56 Gyr | **16%** |

**The honest wrinkle, and why `cost.png` has two panels.** In *absolute* time
the two windows are only 1.6× apart (0.90 vs 0.56 Gyr) — so a plot of the
windows alone reads as "about the same" and teaches the opposite of the beat.
The cost is the window **relative to the age being measured**, which is why
the lower panel draws each window against a bar running 0 → its own age. The
narration says "of the answer" both times, never "wider".

## F8 — the chronology function itself (B02, B07, B08)

**Status: PUBLISHED.**

```
N(1) = 5.44e-14 (exp(6.93 T) - 1) + 8.38e-4 T
```

N(1) = cumulative craters D > 1 km per km², T = age in Ga. Neukum (1983),
restated in Neukum, Ivanov & Hartmann (2001) and in exactly this coefficient
form in Neukum et al., LPSC XXXIII (2002), abstract 1263.

**Care taken.** Published N(1) values derive from two different production
functions (Neukum 1983 and Neukum et al. 2001) and are not interchangeable;
this episode uses one chronology function consistently for every derived
number and never mixes a value from elsewhere into it. The episode also never
claims this function is *correct* — B10 says the opposite.

## F9 — "between one and three billion years, there were none" (B09)

**Status: PUBLISHED, structurally. Asserted for internal consistency (C9).**

The pre-Chang'e-5 calibration record is a cluster of Apollo/Luna sample ages
at the old end, a few young sample-dated craters near the present, and a gap
between them. Li et al. (2021) describe their 2 Ga result as residing
"squarely in the centre of this large gap"; Qiao et al. (2021) frame their
paper as filling the "age gap", placing the Chang'e-5 unit in the ~1–3 Ga
interval between existing calibration points. The 2023 *Reviews in Mineralogy*
chronology chapter lists the calibration sites (Apollo 11, 12, 14, 15, 16, 17;
Luna 16, 24) and notes calibration points are sparse, especially for 1–3 Ga.

**SCHEMATIC IN PLACEMENT — stated plainly.** `anchors.png` draws the anchors
at the conventional Stöffler & Ryder (2001)-era ages (3.92, 3.85, 3.80, 3.75,
3.41, 3.30, 3.22, 3.15 Ga; plus Copernicus ~0.80, Tycho ~0.109, North Ray
~0.053, Cone ~0.026 Ga). Individual dot positions are **illustrative**. What
is load-bearing on screen — and all the narration asserts — is the *shape*:
old cluster, young cluster, empty middle. `gen_craters.py` asserts that no
anchor it plots falls inside 1.0–3.0 Ga.

## F10 — "a window one-point-four billion years wide ... the rock gave eight million" (B10)

**Status: PUBLISHED, both halves. Arithmetic asserted (C7, C8).**

- **Crater counting:** Qiao et al. (2021), GRL — crater counts on the
  Chang'e-5 mare unit give ~**1.3–2.7 Ga** across several chronology models.
  Width **1,400 Myr**.
- **The rock:** Li et al. (2021), *Nature* 600 — a Pb–Pb age of
  **2,030 ± 4 Ma** for Chang'e-5 basalt clasts. Full width **8 Myr**.
- **Ratio:** 1400 / 8 = **175×** (on screen, not spoken).

**Care taken.** The 1.3–2.7 Ga spread is a range *across chronology models*,
not a 1σ statistical uncertainty — the screen labels it "across chronologies".
C8 asserts 2.030 falls inside that window, which is why the narration says
counting was "not wrong, just loose" rather than "wrong".

## F11 — "it moved the curve by at most a quarter-billion years" (B10)

**Status: PUBLISHED. This is the episode's counter-evidence, and it ships.**

The updated lunar cratering chronology fitted with the Chang'e-5 radiometric
age (Yue et al. 2022, *Nature Astronomy*) gives ages older than the Neukum
model for most of lunar history, with a **maximum difference of 0.24 Gyr at
2.55 Ga**.

This weakens the headline and is included for that reason: a 0.24 Gyr shift is
not a demolition of crater counting. What the episode claims is narrower and
survives it — that the shift came from a **returned sample**, and that no
detector improvement has ever produced one.

---

## Claims deliberately NOT made

- **Not claimed: that nobody applies ML to the dating step.** Work exists that
  treats crater age *classification* with transfer learning on Chang'E data.
  The episode's claim is about the **calibration** — the density-to-age curve
  — and no reviewed work moves that curve without a radiometrically dated
  sample. B11 is worded to that scope ("a model trained on crater counts can
  only repeat the curve it was handed").
- **Not claimed: that automated and manual counts are interchangeable.**
  Detectors have their own completeness and bias, especially near the
  resolution limit; Robbins et al. warn about craters ≤10 px regardless of who
  counts them.
- **Not claimed: a specific count of calibration points.** Sources differ on
  which sites and sub-units count as independent anchors, so the episode says
  "rocks somebody flew home and dated" and shows the shape, never a tally.
- **Not claimed: anything about asteroid detection or impact warning.** That is
  Ep. 08. Every crater in this episode is already on the ground.
- **Not dated:** no model version numbers, no "state of the art", no counts
  that drift.
