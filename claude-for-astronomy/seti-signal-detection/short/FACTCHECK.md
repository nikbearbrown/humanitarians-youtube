# FACTCHECK — *The Signal We Imagined.*

Ep. 13 · `seti-signal-detection` · checked from primary sources on
**2026-10-16**, during this build.

**Two kinds of number appear and they are never mixed.** *Published* figures
come from the cited papers and carry a source line. *Computed here* figures
come out of `assets/gen_seti.py`, which runs the real de-Doppler search and
asserts three claims. B03 is published and says so on screen; B04–B10 are
computed here and say so.

**And one distinction this episode needs more than most.** The *diagnosis* —
that we must assume a form because nothing has ever been detected — is not
my observation. It is the stated motivation of the field's own simulation
toolkit, quoted verbatim below. What this reel adds is a measurement of what
that assumption costs on one concrete, fully-known case.

## Claims on screen or in the narration

| # | Claim | Where | Verdict | Source |
|---|---|---|---|---|
| 1 | No radio technosignature has ever been detected | B00, B02, B11 | ✅ | Brzycki et al. 2022 (AJ), verbatim: *"Given that we have not yet detected a radio SETI signal, we must make assumptions about their form"*. |
| 2 | Because of that, algorithms are hard to test | B02 (implied), paperwork | ✅ | Same paper, verbatim: *"The lack of positive detections also makes it difficult to test these algorithms' inherent efficacy."* `setigen` exists to inject synthetic signals precisely to fill that gap. |
| 3 | A signal was recorded at Parkes, 29 April 2019, observing Proxima Centauri, near 982 MHz, named BLC1 | B03 | ✅ | Sheikh et al. 2021, *Nature Astronomy* 5, 1153–1162. |
| 4 | It was ruled out as human interference | B03 | ✅ | Same, verbatim: *"we find that blc1 is not an extraterrestrial technosignature"*; an intermodulation product of local, time-varying interferers. |
| 5 | **Dozens of look-alikes** were found in the interference | B03 counter + narration | ✅ | Same, verbatim: *"We find dozens of instances of radio interference with similar morphologies to blc1"*, at frequencies harmonically related to common clock oscillators. |
| 6 | Interference stands vertical in the dynamic spectrum; a sky source drifts | B04 | ✅ | Standard radio-astronomy geometry: a transmitter fixed to the rotating Earth has no relative line-of-sight acceleration with respect to the telescope, so no Doppler drift. This is the premise of drift-rate searches. |
| 7 | The search sweeps trial drift rates and keeps the best | B05 | ✅ | This is the de-Doppler statistic computed by turboSETI and its relatives, and is implemented here directly rather than approximated. |
| 8 | A signal outside the swept range is not searched for | B05, B07, B11 | ✅ | True by construction of the algorithm, and demonstrated by the control sweep. |

## Computed in this reel (`assets/gen_seti.py`, seed 1313)

32 time rows × 512 frequency channels; 4 interference lines at zero drift
plus 10 broadband blips; one injected narrowband signal at SNR 1.6 per cell.
Threshold fixed at the 95th percentile of the map maximum on **noise-only**
fields. 80 trials per hypothesis.

| Quantity | Value |
|---|---|
| Hypothesis A — drifting 0.6–2.0 Hz/s, continuous (*what searches assume*) | recall **1.00** |
| Hypothesis B — **drift-corrected** (zero drift), continuous | recall **0.00** |
| Hypothesis B, with zero drift included in the sweep | recall **1.00** |
| Hypothesis C — pulsed, 45% duty, drifting | recall **0.70** |
| Where the blind spot begins | recall falls 1.00 → 0.00 between **0.06 and 0.12 Hz/s** |
| Cadence test — A · B · C | **0.98 · 0.76 · 0.70** |

**The self-check asserts three things and the script writes nothing if any
fails**: the drift-corrected signal is a clean blind spot (≤0.02 → ≥0.95);
the assumed signal is reliably found (≥0.90), since the comparison means
nothing if the search fails on its own hypothesis; and the cadence test
recovers the signal the morphology search scores zero on, while being
insensitive to the drift hypothesis.

### A claim I measured and then cut

An earlier version argued that zero drift is **too crowded with interference
to search** — the reason, I assumed, that pipelines exclude it. The
measurement does not support it: the median number of look-alikes sharing a
candidate's drift rate is **6 for a drifting candidate and 5 for a stationary
one**. No difference.

The real flood of zero-drift interference is a property of actual spectrum
occupancy, which four simulated lines do not reproduce. Raising the line
count until the claim came true would be tuning the experiment to the
conclusion. So the claim went, the function stayed (`seti.lookalikes`, still
run, still reported), and **BLC1's look-alike argument appears in the reel as
a published result only** — which it is.

### Three simulators discarded before this one, all my errors

1. **A statistic that could not work.** The first detector took a single
   maximum over the whole field. The interference is brighter than the
   signal, so the maximum was always an interference line and the injected
   signal never moved it — every recall came out at 0.03–0.10. A pipeline
   returns a *hit list*; the question is whether the real signal is on it.
2. **A threshold set by the interference.** Calibrating on fields containing
   interference made the threshold track the brightest line (22.6), so
   nothing could ever exceed it. The interference is not supposed to be under
   the threshold — it is the pile of hits a human sifts. Now calibrated on
   noise-only fields.
3. **An under-resolved regime.** At 16 rows and 0.15–0.60 Hz/s a signal
   drifts only 2–10 channels across the integration, against a 1–2 channel
   linewidth, so de-Doppler could not separate a drifting signal from a
   stationary one at all and look-alike counts came out identical by
   construction. Real surveys integrate for minutes and sweep several Hz/s.
   Now 32 rows at 0.6–2.0 Hz/s.
4. A fourth, smaller: drift was drawn with a random **sign** while the search
   ranges covered only positive rates, so half of every "assumed" signal was
   never searched for. It showed up as recall 0.45 on the one hypothesis that
   was supposed to work.

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Ma et al. 2023 (*Nature Astronomy*): β-VAE search, **820 targets, >480 hr, 8 signals of interest** | Verified and quotable, but the reel's argument is about what a search is trained to recognise, and adding a second system's numbers would blur the one case being measured. Kept in SOURCES. |
| Whether those 8 candidates recurred on re-observation | **Not stated in the abstract.** Not claimed either way. |
| The Wow! signal (1977) | A single unrepeated detection with no cadence information — it cannot illustrate a verification framework, which is the episode's point. |
| Specific drift-rate limits used operationally by Breakthrough Listen | Could not verify a current figure from a primary source in this session. The reel uses its own stated range and says it is illustrative. |
| BLC1's exact drift rate and bandwidth | In the paper, but the reel's BLC1 beat is about *how it was ruled out*. |
| Drake equation, Fermi paradox | The episode is about detection method, not abundance. |

## Softened on purpose

- **"We have never detected one"** is the literal statement of the setigen
  paper, stated as of this build.
- **The experiment is never presented as a model of Breakthrough Listen,
  Parkes or Green Bank.** Only the direction and rough size of the effect are
  claimed, and every computed beat carries "computed in this reel".
- **Hypothesis B is not a prediction.** A drift-corrected transmitter is one
  plausible choice among many, chosen because it is the one *we* make for our
  own spacecraft. The reel does not claim aliens would do this.
- **The reel does not say SETI searches are wrong or badly built.** It says
  the positive class is hypothetical, that the field says so itself, and that
  the test which settles a candidate is a provenance test — which is also
  what the field does, and what settled BLC1.
- **"0 of 80" is a measured count**, not a rhetorical zero, and the plate
  draws it as a visible zero-height bar rather than as an absent bar.
- **No claim that any published search missed a real signal.**

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is that the positive class does not exist**, which is new to
   this series. There is no training set to be biased, no objective to
   under-specify, no test set to leak — nobody has ever observed the thing.
2. **The detector is the real algorithm**, not a black box, so the assumption
   is visible as one number rather than buried in weights.
3. **The control beat is what makes it an experiment.** B08 sweeps the
   search's lower edge and locates the blind spot exactly where the parameter
   crosses zero. Without it the episode is an anecdote.
4. **The fix is given as much room as the problem**, and it is the fix the
   field actually uses.
5. **Published and computed-here are separated**, and so are *diagnosis* and
   *measurement*.
6. **No real telescope imagery, no reproduced figures, no redrawn plots.**
   BLC1 is an isotype of tones on a frequency axis, never a spectrogram
   lifted from the paper.
7. **A claim that failed its own test was removed, not weakened.**
