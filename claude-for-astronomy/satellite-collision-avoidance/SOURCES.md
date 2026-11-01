# SOURCES — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · AI in Astronomy & Space Science
**The series finale.** Checked from primary sources on **2026-10-31**.

---

## Published — the effect

**Balch, Martin & Ferson (2019), "Satellite conjunction analysis and the
false confidence theorem", *Proceedings of the Royal Society A* **475**,
20180565** (arXiv:1706.08565).

Verbatim:

> "A counterintuitive phenomenon has emerged in the conjunction analysis
> literature, namely, probability dilution"

> "In satellite conjunction analysis, it results in a severe and persistent
> underestimate of collision risk exposure."

The authors argue dilution is a symptom of a broader problem they call **false
confidence**, propose the Martin–Liu validity criterion as a benchmark for
avoiding it, and show that uncertainty ellipsoids satisfy that criterion — so
manoeuvre decisions taken on ellipsoid overlap keep risk within a stated
limit.

**This episode does not adopt their remedy or their framing of the
foundations.** It uses only the uncontroversial part: that Pc falls as the
covariance grows, and that this is a property of the quantity rather than of
the sky. The confidence-distribution and false-confidence debate is live, and
the reel stays out of it.

**Alfano**, in the patent covering maximum conjunction probability
(US7383153B2), makes the operational version of the same point: a very large
positional uncertainty produces a low computed conjunction probability which
is *mathematically correct* but "may give a false sense of confidence that a
conjunction is not likely to occur". That construction — asking how bad the
encounter could look over all covariance scales — is what B10 draws.

---

## Published — the benchmark

**Uriot, Izzo, Simões, Abay, Einecke, Rebhan, Martinez-Heras, Letizia,
Siminski & Merz (2020), "Spacecraft Collision Avoidance Challenge: design and
results of a machine learning competition"** (arXiv:2008.03069; also
*Astrodynamics*, 2021).

| Fact | Value |
|---|---|
| Conjunction events released | **15,321** |
| Conjunction data messages | **199,082** (≈13 per event) |
| Events with final risk ≥ 1e-4 | **30** |
| Events with final risk ≥ 1e-5 | 131 |
| Events with final risk ≥ 1e-6 | 515 |
| Competition notification threshold | 1e-6 |
| Teams | **97** |
| Teams that beat the naive baseline | **12** |
| Naive baseline score | L = 0.694 |
| Top three scores | 0.556, 0.571, 0.585 |

The naive baseline is the **"Latest Risk Prediction"**, described by the
authors as *"the clipped naive forecast"*: predict the risk reported in the
most recent message, or −6.001 if that is below −6.

Verbatim, on how hard it was to beat:

> "all the top teams managed to beat the LRP baseline"

> "it took most of the teams around 20 days to do so"

> "the scores do not improve much below the LRP baseline"

The authors describe the baseline as **"surprisingly effective"**, which is
the phrase B09 quotes.

The competition chose 1e-6 rather than the more common operational 1e-5 in
order to *"have a higher number of high-risk events while keeping its value
close to the more frequently used operational value"* — i.e. the class
imbalance was severe enough to need managing before the problem was even
posable.

---

## Computed in this reel

`assets/conj.py` — the probability, and the population.
`assets/gen_conj.py` — the experiment, the self-check and all six plates.

**Seed 1515**, logged here, used for every figure.

**The integral is the real one.** For a short encounter the relative motion is
projected into the plane perpendicular to the relative velocity, and Pc is the
Gaussian mass inside a disk of radius R at the predicted miss distance:

```
Pc = ∫₀^R (r/σ²) exp(-(r - d)²/(2σ²)) · i₀ₑ(r d / σ²) dr
```

That is Foster's method in its numerically stable form — writing
I₀(x) = i₀ₑ(x)·e^{|x|} and folding the exponentials together, so nothing is
ever exponentiated to a large positive argument. The naive form overflows for
d/σ ≳ 30, which is exactly the well-tracked regime the episode is about.

| | |
|---|---|
| Combined hard-body radius | 20 m |
| Worked-example miss distance | 300 m |
| Action threshold drawn | 1e-4 |
| Population | 120,000 conjunctions, 7 messages each |
| Screening box | 8 km |
| Final covariance | 25–200 m |
| Total covariance shrink | 20–300× |

**Why the miss distance is drawn uniform in AREA.** Conjunctions are screened
inside a box, and for encounters arriving from random directions the number
with miss distance below *d* grows like *d²*. Drawing *d* log-uniformly — the
first thing I tried — made 41 % of events high-risk. Drawing it uniform in
area gives **0.15 % above 1e-4**, the same order as ESA's 30 in 15,321. The
rarity is a consequence of the geometry, not a parameter.

---

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Current debris population counts (ESA's quarterly numbers, Starlink conjunction rates) | True, and the obvious way to open the episode, but the reel's argument is about a quantity, not a census. Numbers that age badly add nothing to it. |
| The 2009 Iridium–Cosmos collision | The standard anecdote. It illustrates that collisions happen; it says nothing about what Pc is. The episode does not need it. |
| The Martin–Liu validity criterion and the false-confidence theorem | The foundations debate is live and the reel takes no position in it. The dilution effect itself is not in dispute. |
| Specific winning architectures from the challenge (Siamese networks, gradient-boosted trees) | Quoting them would imply this reel reproduced them. It did not — it trained a ridge regression to make one structural point about the loss. |
| Covariance realism and its own literature | A real and serious problem, but a second mechanism. One followed properly beats three named. |

---

## Measured here, and deliberately NOT claimed as a fix

Both of these are reported in FACTCHECK.md and in the generator's own output.
Neither is presented on screen as something that worked.

- **Giving the model σ/d** — where the conjunction sits on the dilution
  curve — moved the notified-event error by **−2.7 %**. That is nothing. B10
  says so out loud, because "the fix I tried did not work" is the honest
  shape of that beat.
- **Reweighting the tail 300×** improved the notified error **2.4×**, cost
  **15×** on the aggregate, and **still lost to "assume nothing changes" by
  1.4×**.

---

## Softened on purpose

- **The simulation is never presented as a model of any real catalogue,
  operator or conjunction.** Every computed beat carries "computed in this
  reel". The orbital dynamics are not modelled at all — there is no
  propagator here. What is real is the Pc integral and the shape of its
  dependence on σ, and those are the only things claimed.
- **The reel does not say operators are getting this wrong.** Maximum
  probability, covariance realism and dilution are all well known inside the
  conjunction-assessment community; Alfano patented the remedy in 2008. The
  claim is about what the *quantity* is, not about anyone's competence.
- **"Degrade your tracking to clear the alert" is not an accusation.** It is
  a property of the metric, stated as a property. Nothing in the reel
  suggests anybody does this deliberately.
- **The ESA challenge is not described as a failure.** The top teams did beat
  the baseline. The point is the margin and how few managed it, which is the
  organisers' own published observation.
