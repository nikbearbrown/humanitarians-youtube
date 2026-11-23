# FRICTIONAL — It Tested Clean

A dated record of the process behind this piece of work, kept beside the
evidence it describes. Append; never rewrite an earlier entry.

---

## 2026-11-23 — the experiment that nearly proved the wrong thing

**What I tried and expected.** Training-serving skew came off the registry's
open list. I expected a straightforward build: fit a model, break a feature at
serving, show the damage. I also expected a specific angle — *the skews a
drift check misses are the ones that hurt most* — and I had the beat planned
before the numbers existed.

**Where it resisted.**

**1. The first model was badly fit, and the tell was that it made skew look
harmless.** I fitted logistic regression on unstandardised features with too
few epochs. It reached AUC 0.61, overflowed `exp`, and — the part that
mattered — two of the four skews *improved* the score. Multiplying one feature
by 7/30 was raising AUC.

That is not a finding about skew. It is a finding about a fit that was
over-weighting one feature, and if I had taken it at face value the reel would
have been a demonstration of a broken model wearing the costume of a
demonstration of skew. What caught it was the direction being *wrong*: damage
that helps is a symptom, not a result. Fixed by standardising on train
statistics, clipping the logit, and fitting to convergence.

**2. The angle I had planned is false in this data.** With the model fitted
properly, the two skews a PSI check sails past cost 0.5 and 1.4 accuracy
points. The two that trip the alarm cost 9.2 and 31.9. Drift checking, pointed
at the values the model actually received, works — which is the opposite of
the story I had in my head.

I had a choice: find a framing that preserved the planned beat, or throw the
beat away. Throwing it away produced a better reel. The real finding was one
line further down in my own output — PSI against the warehouse reads 0.001 for
all four, because the warehouse never saw the problem. The failure is not
sensitivity, it is **where the check is pointed**, and that is both truer and
more actionable than the beat I had planned.

This is the second time in three reels that the interesting result was the one
that contradicted my setup. The peeking reel had the same shape: a comparison
rigged in favour of the conclusion I expected, and a better finding underneath
it once the comparison was made fair.

**3. No sklearn, deliberately.** The toolkit's dependency floor is numpy plus
scipy, and adding a dependency for one reel is not a good trade when the
needed maths is thirty lines. Writing the fit by hand also made failure 1
visible — an imported `LogisticRegression` would have standardised internally,
converged quietly, and hidden the fact that my first setup was wrong in a way
I should have caught by reasoning rather than by accident.

**What Claude contributed and what I accepted.** Claude chose the topic from
the open list, built the evidence, caught both problems above mid-build, and
authored both reels. I supplied the brief and the pipeline report.

**What is now understood.** The failure mode I keep writing down has a second
half. The first half is that gates read geometry and type, not meaning. The
second half, visible here, is that **a result which confirms the plan gets
less scrutiny than one that contradicts it.** Both of this build's problems
were found by noticing that a number pointed the wrong way — not by a gate,
not by a check, but by the result being surprising enough to re-read.

The practical version: when a measurement agrees with the beat you already
wrote, that is the moment to go back and ask whether the measurement could be
agreeing for the wrong reason.

**What is still open.** The simulation sweeps one skew at a time. Real
pipelines skew several features at once, and the interactions are not
necessarily additive. That is a bigger piece of work and would need its own
reel.

---

## 2026-11-23 — a week with no punt

GATE L found nothing for "two pipelines computing the same value differently",
which in a previous week would have meant building something. It did not,
because `PairedBars` — built the week before for Simpson's paradox — already
does the shape this reel needed: two series, N rows, optional aggregate. Here
it runs with `total: null` and four independent comparisons.

That is three weeks running where a component built against a punt has carried
an argument it was not designed for: `StageRail` (10-09 → 10-30), `ThresholdWalk`
(11-06 → reused in the report), `PairedBars` (11-13 → here, and in this week's
report too).

Zero new components this reel, and the library is at 647 renderable scenes.
The punts are compounding in the right direction.
