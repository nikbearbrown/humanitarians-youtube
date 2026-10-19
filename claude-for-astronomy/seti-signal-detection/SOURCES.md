# SOURCES — *The Signal We Imagined.*

Ep. 13 · `seti-signal-detection` · AI in Astronomy & Space Science
Checked from primary sources on **2026-10-16**, during this build.

---

## Published — the thesis, in the field's own words

**Brzycki, Siemion, de Pater, Croft, Hoang, Ng, Price, Sheikh & Zheng (2022),
"Setigen: Simulating Radio Technosignatures for SETI", *The Astronomical
Journal*** (arXiv:2203.09668, doi 10.3847/1538-3881/ac5e3d).

Verbatim:

> "Given that we have not yet detected a radio SETI signal, we must make
> assumptions about their form"

> "The lack of positive detections also makes it difficult to test these
> algorithms' inherent efficacy."

This is the episode. `setigen` exists because the positive class does not:
it is a library for **generating artificial narrowband signals and injecting
them into Breakthrough Listen data products**, so that search algorithms have
something to be tested against. The tool is excellent and the authors are
explicit about why it is needed. The reel's argument is not a criticism of
it — it is a reading of the sentence above.

---

## Published — the one candidate that got through

**Sheikh et al. (2021), "Analysis of the Breakthrough Listen signal of
interest blc1 with a technosignature verification framework", *Nature
Astronomy* 5, 1153–1162.**

- The signal was recorded on **2019 April 29** with the **Parkes** telescope,
  near **982 MHz**, while observing **Proxima Centauri**, and was labelled
  **BLC1** — Breakthrough Listen Candidate 1.
- The analysis concluded it was an **intermodulation product of local,
  time-varying interferers** that happened to line up with the observing
  pattern. Verbatim: *"we find that blc1 is not an extraterrestrial
  technosignature"*.
- What killed it was a **population argument**, not a classifier. Verbatim:
  *"We find dozens of instances of radio interference with similar
  morphologies to blc1"*, at frequencies harmonically related to common clock
  oscillators. Several similar 982 MHz signals were found on other days, and
  **some appeared in off-source observations**.

That last clause is the fix beat: a signal that shows up when the telescope
is pointed *away* from the target is not coming from the target.

---

## Published — AI in the search

**Ma, Ng, Rizk, Croft, Siemion, Brzycki, Czech, Drew, Gajjar, Hoang,
Isaacson, Lebofsky, MacMahon, de Pater, Price, Sheikh & Worden (2023),
"A deep-learning search for technosignatures of 820 nearby stars", *Nature
Astronomy*** (arXiv:2301.12670, doi 10.1038/s41550-022-01872-z).

Verbatim from the abstract:

> "The search comprises 820 unique targets observed with the Robert C. Byrd
> Green Bank Telescope"

> "totaling over 480 hr of on-sky data"

> "We implement a novel beta-Convolutional Variational Autoencoder"

> "returning 8 promising ETI signals of interest for re-observation"

**What this reel does NOT say about it.** The abstract does not report
whether the eight candidates recurred on re-observation, so the reel does not
claim they were ruled out, and does not claim they were not. It uses the
paper for one fact only: a modern deep-learning search over 480 hours
returned eight things worth looking at again.

---

## Computed in this reel

`assets/seti.py` — the dynamic spectrum, the interference, and the two tests.
`assets/gen_seti.py` — the experiment, the self-check and all six plates.

**Seed 1313**, logged here, used for every figure.

**The detector is the real algorithm, not a stand-in.** `dedoppler()` computes
the statistic a radio technosignature search actually computes: sum the
dynamic spectrum along a straight time-frequency track, once per trial drift
rate, and keep the best signal-to-noise. That is what turboSETI and its
relatives do. Using it matters, because the episode's subject — the
assumption — is then a single visible number: **the range of drift rates the
search is told to try.** A signal outside that range is not hard to find. It
is not looked for.

| | |
|---|---|
| Dynamic spectrum | 16 time rows × 512 frequency channels, 1 Hz and 1 s per cell |
| Interference | 6 narrowband lines at **zero drift**, plus 10 broadband blips |
| Injected signal | narrowband, SNR 2.2, under three hypotheses |
| Hypothesis A | drifting at 0.15–0.60 Hz/s, continuous — *what searches assume* |
| Hypothesis B | **drift-corrected** — a transmitter that cancels its own Doppler, which is what humans do for spacecraft |
| Hypothesis C | pulsed (45% duty), drifting |
| Thresholds | calibrated per search range to a 5% false-alarm rate on interference-only fields, as a real pipeline does |

**Why zero drift is the knife-edge.** A transmitter bolted to the same
rotating planet as the telescope has no relative acceleration, so its signal
is a straight vertical line in the dynamic spectrum. That is why real
pipelines exclude zero drift — and it is also exactly where a *drift-
corrected* transmitter would sit. The exclusion is not laziness; it is forced
by the interference population. The reel measures what it costs.

---

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| The Wow! signal (1977) | A single unrepeated detection with no cadence information — it cannot illustrate a verification framework, which is the episode's point. |
| The Drake equation, Fermi paradox | The episode is about detection method, not about how many civilisations there are. |
| Specific turboSETI drift-rate limits used by Breakthrough Listen | I could not verify a current published value from a primary source in this session, so the reel uses its own stated range and says it is illustrative. |
| Whether Ma et al.'s eight candidates recurred | Not in the abstract; not claimed either way. |
| BLC1's exact drift rate and bandwidth | Reported in the paper but not needed; the reel's BLC1 beat is about *how it was ruled out*, not its parameters. |
| Breakthrough Listen's total data volume / "largest SETI survey" claims | Drifts with time, and the episode does not need a scale figure. |

---

## Softened on purpose

- **"We have never detected one"** is the literal statement of the setigen
  paper and is the reel's foundation. It is stated as of this build.
- **The experiment is never presented as a model of Breakthrough Listen,
  Parkes, or Green Bank.** The parameters are illustrative; only the
  direction and rough size of the effect are claimed, and every computed beat
  carries "computed in this reel".
- **The reel does not say SETI searches are wrong or badly built.** It says
  the positive class is hypothetical, that the field says so itself, and that
  the test which settles a candidate is a provenance test rather than a
  morphology test — which is also what the field does.
- **Hypothesis B is not a prediction.** A drift-corrected transmitter is one
  plausible choice among many, chosen because it is the one *we* would make.
  The reel does not claim aliens would do this.
- **No claim that any published search missed a real signal.** The
  demonstration is in simulation.
