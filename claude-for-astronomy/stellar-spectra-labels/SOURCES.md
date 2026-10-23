# SOURCES — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels` · AI in Astronomy & Space Science
Checked from primary sources on **2026-10-23**, during this build.

---

## Published — the method

**Ness, Hogg, Rix, Ho & Zasowski (2015), "The Cannon: A data-driven approach
to stellar label determination", *The Astrophysical Journal* 808, 16**
(arXiv:1501.07604).

Verbatim from the abstract:

> "only 542 stars in 19 clusters as reference objects"

> "Beyond the reference labels, The Cannon makes no use of stellar models nor
> any line-list"

The labels are **Teff, log g and [Fe/H]**; the trained model was applied to
spectra of **56,000 stars from APOGEE DR10**, and the rms differences against
the APOGEE pipeline's own labels are "basically identical to the stated
ASPCAP uncertainties". A stated aim is "to bring different spectroscopic
surveys onto a consistent scale of stellar labels".

That second quote is the episode. A data-driven model has no physics in it.
Everything it knows about stars arrives through its reference labels, and
nothing else.

---

## Published — the thesis, in the survey's own documentation

**SDSS DR14, "The Cannon" data-release page** (`sdss4.org/dr14/irspec/the-cannon/`).

Verbatim:

> "we have trained the Cannon on the ASPCAP stellar parameters and
> abundances"

> "the Cannon results are not an independent determination of these"

> "all the issues and caveats associated with ASPCAP apply to the Cannon
> results, since the latter depend on the former"

And, on precision against accuracy:

> "without censoring, such correlations can lead to abundances that appear to
> be of higher precision"

> "but this precision may not reflect higher accuracy, if the correlations
> are not present over the entire data set"

This is not my inference about a possible weakness. It is the survey telling
its own users that the data-driven labels inherit the physics pipeline's
systematics and that apparent precision is not accuracy. The reel's
contribution is to **measure how far apart those two can get**, on a case
where the truth is known by construction.

The training labels are specifically "the calibrated ASPCAP Teff, log g,
[M/H], [alpha/M], and [X/H] for 20 different species".

---

## Published — the model-independent anchor, and its own limits

Spectroscopic gravities are calibrated against **asteroseismology**, which
does not come from the same atmosphere model, so it does not carry the same
systematic. The APOKASC catalogue
(Pinsonneault et al., arXiv:1410.2503) is the joint asteroseismic and
spectroscopic sample this rests on.

**The anchor is more independent, not perfectly independent**, and the reel
says so:

- APOKASC reports a mean offset near zero across the full sample but a clear
  split between **red clump and red giant branch** stars.
- The discrepancy at the base of the red giant branch depends on **stellar
  mass**, linked by the authors to CN cycling
  (A&A 2017, doi 10.1051/0004-6361/201629938).
- A TESS-versus-APOGEE comparison (arXiv:2307.13853) found agreement to
  better than 5%, with the largest offsets for clump stars and **quoted
  uncertainties apparently underestimated by about a factor of two**.
- One APOGEE release carried a calibration error on the asteroseismic scale
  that produced a systematic red-clump gravity offset (arXiv:2310.19872).

That last bullet is worth keeping in view: the anchor had a bug too. The
episode's recommendation is to tie the scale to something not derived from
the same model — not to believe the anchor uncritically.

---

## Computed in this reel

`assets/spectra.py` — nature, the teacher, and the student.
`assets/gen_stars.py` — the experiment, the self-check and all six plates.

**Seed 1414**, logged here, used for every figure.

**The student is the real algorithm.** `Cannon` fits a quadratic polynomial
in the labels at every wavelength pixel and then inverts it at test time by
Gauss-Newton to read labels off a new spectrum. It contains no physics; its
only contact with the world is the labels it was handed. Using the real
method matters because the episode's subject — what the model is actually
fitting — is then visible rather than asserted.

| | |
|---|---|
| Spectrum | 160 pixels, continuum-normalised, 26 absorption lines |
| Line sensitivities | drawn once from a fixed seed and frozen, so "nature" is the same function on every run |
| Labels | Teff 4000–6500 K · log g 1.5–4.5 · [Fe/H] −1.0 to +0.4 |
| Noise | S/N 100 per pixel |
| **The teacher's error** | a **temperature-dependent** metallicity bias of 0.18 dex per 1000 K, plus 0.03 dex of random scatter |
| The anchor | unbiased labels, 0.08 dex scatter in [Fe/H], far fewer stars |

**Why the bias is a trend and not an offset.** A constant offset would be
caught by any comparison of means. The shape a real missing-opacity or
microturbulence error takes is a trend across the sample — it looks like
astrophysics, and it survives every check that compares averages.

---

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Casey et al. (2016), *The Cannon 2*, and its note that high-S/N stacked spectra are "advantageously dominated by systematic uncertainties" | A good corroboration, but the DR14 documentation says the same thing more directly and is the survey's own voice. |
| APOGEE/ASPCAP's specific calibration relations and their published offsets | Real numbers, but quoting them would imply this reel measured something about APOGEE. It did not. |
| Gaia parallaxes and the distance half of the brief's one-liner | The brief says "composition/age/distance". The episode takes composition, because that is where the label-inheritance problem is cleanest and best documented. Distance would need a second, unrelated mechanism. |
| Spectral type classification (OBAFGKM) as a framing | Decorative here; the episode is about parameter estimation, not taxonomy. |
| Specific neural-network spectral models (e.g. Payne-style) | A different implementation of the same dependency. One method, followed properly, is worth more than three named. |

---

## Softened on purpose

- **The experiment is never presented as a model of APOGEE, the Cannon, or
  any survey.** Every computed beat carries "computed in this reel". The line
  bank, the label ranges and the bias are illustrative; only the direction
  and rough size of the effect are claimed.
- **The reel does not say the Cannon is wrong or badly built.** It says a
  data-driven model inherits its labels' systematics, which the method's own
  authors and the survey's own documentation both state plainly. The method
  does what it says.
- **"The teacher is wrong" is a property of my simulation**, introduced
  deliberately so the gap can be measured. It is not a claim that ASPCAP has
  a 0.18 dex/1000 K metallicity trend.
- **The anchor is not called a solution.** It is called more independent, and
  the reel notes the anchor's own offsets and underestimated uncertainties.
- **No claim that any published catalogue's labels are inaccurate by a
  specific amount.**
