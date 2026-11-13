# SOURCES — Ep. 17, *scheduling-the-night*

Everything the narration asserts traces to one of these, or to
`assets/gen_sched.py`, which re-derives its own numbers and refuses to write
a plate if a claim fails.

---

## S1 — ZTF: the Integer Linear Programming scheduler

Bellm, E. C., Kulkarni, S. R., Barlow, T., Feindt, U., Graham, M. J.,
Goobar, A., Kupfer, T., Ngeow, C.-C., Nugent, P., Ofek, E., Prince, T. A.,
Riddle, R., Walters, R., & Ye, Q.-Z. (2019).
**"The Zwicky Transient Facility: Surveys and Scheduler."**
*PASP* 131, 068003. arXiv:1905.02209.

Used for:

- **The method.** "We use Integer Linear Programming (ILP) techniques to solve
  this problem." Blocks of time; `Y[r,t,f] = 1` if request set `r` is scheduled
  in block `t` with filter `f`; "Filter changes only occur at the block
  boundaries."
- **The request-set definition this episode's simulation copies.** "the number
  of visits and filter set for observations requested within a night (e.g.,
  *two nightly visits, one in g-band and one in r-band*)." This is why a
  request set in `sched.py` is a **g+r pair** and not two visits in one band —
  the pairing is theirs, not a convenience of mine.
- **The decisive measurement, and its name.** §: "The importance of the
  lookahead provided by the ILP algorithm is most clearly demonstrated by the
  **sequence completion fraction** — the fraction of observed fields for which
  the scheduler obtains all of the desired nightly observations. Including the
  effects of weather losses, the greedy algorithm completed an average of
  **64%** of the MSIP Northern Sky Survey observations, **79%** of the MSIP
  Galactic Plane Survey observations, and **72%** of the collaboration
  Extragalactic High-Cadence observations. In contrast, the ILP scheduler
  completed **81%** of the requested observations for each of the same
  surveys."
- **That throughput was NOT the difference.** "Both approaches yielded
  comparable numbers of exposures per hour." The ILP gained 9% on the summed
  metric and observed closer to zenith — "a median airmass of **1.11**
  compared to **1.20** for the greedy approach."
- **The counterweight I am required to say out loud.** "Perhaps surprisingly,
  the greedy scheduler yielded **fewer filter changes**, averaging **2.0** per
  night compared to **3.6** per night." The ILP penalises filter changes
  explicitly and still made more of them.
- **That the ILP is not run unbounded.** Their recomputation scheme is
  deliberately limited: "at each block boundary, the best un-observed requests
  from earlier in the evening are reassigned to any unused time in the current
  block."

## S2 — Rubin: the Feature-Based Scheduler as actually deployed

Jones, R. L., Yoachim, P., Neilsen, E. H. Jr., Ribeiro, T., Dennihy, E., &
MacBride, S. P. **"Scheduling the LSST: Commissioning the Rubin Feature Based
Scheduler."** SMTN-020 / SPIE proceedings.

Used for:

- **The cadence of the decision.** "From twilight to twilight, except during
  bad weather or maintenance, the Simonyi Telescope will **select a new target
  every 30 seconds**." Mount "slews between pointings in under 5 s."
- **The mechanism.** `BasisFunction` objects "calculate the reward value of
  potential observations given the current Conditions… Combining multiple
  BasisFunction instances with different weights yields a **total reward**."
- **That it is tiered and greedy within a tier.** "A higher-tier survey always
  takes priority over a lower-tier survey: lower tiers execute only when no
  survey in any higher tier has a feasible observation to request. Within each
  tier, surveys are ranked by their current reward values… the survey with the
  **highest reward** will request observations."
- **That it is real.** Commissioning May–Sept 2025 drove "over 20,000 science
  visits"; early operations from Oct 2025 "almost 50,000 additional visits."

**Negative result, deliberately checked:** the strings `reinforcement`,
`machine learning`, and `neural` appear **zero times** in S2. The scheduler
Rubin actually runs is a weighted sum of hand-built basis functions, chosen
greedily within priority tiers. See FACTCHECK F6.

## S3 — where the "reinforcement learning" in the topic line comes from

Naghib, E., Yoachim, P., Vanderbei, R. J., Connolly, A. J., & Jones, R. L.
(2019). **"A Framework for Telescope Schedulers: With Applications to the
Large Synoptic Survey Telescope."** *AJ* 157, 151.

S1 describes it precisely, and this is the phrasing the episode follows:
Naghib et al. "casts the scheduling problem of the Large Synoptic Survey
Telescope (LSST) as a **memoryless Markov Decision Process**, using
**hand-designed features** to reduce the dimensionality of the state space and
**optimizing the feature weights** with a simple throughput-based objective
function."

So: learning appears, offline, to tune a handful of weights. It does not drive
the telescope. Saying "reinforcement learning schedules Rubin" would be wrong.

## S4 — the airmass model

Kasten, F., & Young, A. T. (1989). "Revised optical air mass tables and
approximation formula." *Applied Optics* 28, 4735.

`sched.py: airmass()` implements the Kasten–Young formula rather than
`sec(z)`, which diverges badly near the horizon — precisely the regime where
scheduling decisions are made.

---

## What is MINE, not theirs

`assets/sched.py` is a **toy** built to isolate one mechanism. It is not ZTF,
not Rubin, and not calibrated to either. Specifically mine, and labelled as
such in FACTCHECK:

- one 8-hour night, 16 half-hour blocks, two bands, a −30° site;
- fields on a Fibonacci sphere, not real ZTF/Rubin field grids;
- a trapezoidal alt-az slew model with invented axis rates;
- `scipy.optimize.milp` (HiGHS) in place of Gurobi;
- the `finish_bonus` knob, which is **not in any paper** — it is the
  falsifiability test this episode runs on its own claim.
