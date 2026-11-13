# FACTCHECK — Ep. 17, *scheduling-the-night*

Every spoken number, traced. Sources are keyed to `SOURCES.md` (S1 ZTF /
Bellm+ 2019, S2 Rubin / SMTN-020, S3 Naghib+ 2019, S4 Kasten–Young).
Measured numbers come from `assets/gen_sched.py`, which **asserts** each one
and writes no plate if an assertion fails.

---

### F1 — "more than ten to the two-thousandth ways" (B04) — **OK, and deliberately understated**

`log10(1000!) = 2567.6`, asserted in `gen_sched.py` (`claim: orderings`).
The narration says "more than ten to the two-thousandth," which is true and
easier to say than the exact exponent. The Remotion cold-open chrome shows the
precise figure, `10^2567`.

### F2 — "every atom in the universe is ten to the eightieth" (B04) — **OK, standard figure**

The conventional estimate for baryonic atoms in the observable universe is
~10⁸⁰ (quoted ranges run 10⁷⁸–10⁸²). Used only as a scale anchor; the
comparison survives anywhere in that range, since the gap is ~2,487 orders of
magnitude either way.

### F3 — "every thirty seconds" (B05) — **OK, verbatim S2**

"From twilight to twilight… the Simonyi Telescope will **select a new target
every 30 seconds**."

### F4 — "scores the whole sky… adds them up with weights, and takes the highest" (B05) — **OK, verbatim S2**

BasisFunctions "calculate the reward value of potential observations…
Combining multiple BasisFunction instances with different weights yields a
total reward," and within a tier "the survey with the **highest reward** will
request observations." Calling it *greedy* is my word, but it is what
selecting the current maximum with no lookahead means.

### F5 — "sixteen blocks, one filter each… an integer program" (B06) — **mine, modelled on S1**

S1 establishes the method and that "Filter changes only occur at the block
boundaries." The **sixteen** half-hour blocks is **my** simulation's night
(8 h / 30 min), not a ZTF constant — ZTF's block count varies with night
length. Narration is phrased as a description of my own run.

### F6 — "a request is a pair: one green exposure and one red" (B07) — **OK, S1's own example**

S1: "the number of visits and filter set for observations requested within a
night (e.g., **two nightly visits, one in g-band and one in r-band**)."
"Green/red" is a plain-language gloss of g/r for a student audience.

### F7 — "may decline a field entirely… may not take half a pair" (B07) — **OK, my implementation of S1's Eq. 4**

`sched.py`: `sum_t Y[r,t,f] = n_req[r,f] * Z[r]`. An equality, not `<=`.

### F8 — "401 started, 78 unfinished; 360 started, none" (B08) — **measured**

`gen_sched.py`, seed 1717, n_sets 450: greedy started 401, completed 323,
stranded 78 → completion **0.805**. Planner started 360, completed 360 →
**1.000**. Asserted.

### F9 — "ninety point five exposures an hour against ninety" (B10) — **measured**

greedy 724 visits = 90.5/h; planner 720 = 90.0/h. Asserted as <10% apart.
Matches S1's finding in kind: "Both approaches yielded **comparable numbers of
exposures per hour**."

### F10 — "depth it never asked for… 1.71 against 1.29" (B10 plate labels) — **measured, with known jitter**

Median airmass, greedy **1.709**, planner **1.281–1.288** depending on run.
See F13. Plate labels say **1.7** and **1.3** (one decimal, so the jitter cannot move them); narration says only "depth it
never asked for," which is robust to the jitter. S1 found the same direction
at smaller magnitude (1.20 → 1.11).

### F11 — "ZTF's planner made more filter changes" (B10) — **OK, verbatim S1, and a counterweight against my own thesis**

"Perhaps surprisingly, the greedy scheduler yielded **fewer filter changes**,
averaging **2.0** per night compared to **3.6** per night." The ILP penalises
filter changes explicitly and still made more. This is in the episode because
leaving it out would make the result look cleaner than it is.

### F12 — "it climbs to ninety-eight percent, but by starting fewer fields and giving up rate. It never reaches the line." (B09) — **measured; this is the falsification test**

finish_bonus sweep, same night: 0.0 → 0.805 (401 started, 90.5/h);
2.0 → 0.927; 5.0 → 0.950; **20.0 → 0.975 (358 started, 88.4/h)**. Asserted
jointly: completion > 0.95 **and** started < baseline **and** rate < baseline.
Narration rounds 0.975 to "ninety-eight percent."

The honest reading, stated on screen: greedy **can** largely buy sequence
completion. It does so by becoming *less* greedy — starting 43 fewer fields —
and it still does not reach 1.000 while giving up 2.3% of its exposure rate.
The planner reaches 1.000 at 90.0/h. The `finish_bonus` knob appears in **no**
paper; it is mine, and exists so this episode's central claim can be attacked.

### F13 — the ILP does **not** prove optimality, and this is said nowhere misleadingly — **known limitation**

HiGHS returns `Time limit reached` at the 120 s budget used for the build.
Incumbent quality improves with budget (60 s → 540 visits; 120 s → 720), and
because the solve stops on **wall clock**, re-running shifts the planner's
median airmass slightly (1.281 vs 1.288 across two runs). Completion stays
exactly 1.000 because it is a **constraint**, not an objective — which is the
episode's actual point. No narration line claims the plan is optimal.

### F14 — "both solved that without machine learning" (B00) and "no network, no reward learned from experience" (B11) — **OK, and carefully scoped**

Scoped to **the pointing decision**, not to either observatory's wider
software (Rubin certainly uses ML downstream, e.g. alert classification —
which is Ep. 10's territory, not this one).

- S2, the document describing the scheduler Rubin **actually runs**, contains
  **zero** occurrences of `reinforcement`, `machine learning`, or `neural`
  (checked directly).
- ZTF's scheduler is Integer Linear Programming (S1). No learned component.
- S3 (Naghib+ 2019) is where learning enters: a memoryless MDP "using
  **hand-designed features**… **optimizing the feature weights** with a simple
  throughput-based objective function" (quoted in S1). Offline weight tuning,
  not an operational policy.

**Correction carried into the build:** `ideas.md`'s one-line topic blurb for
Astronomy 17 names "optimization and reinforcement learning." The optimization
half is right; the RL half is not true of either deployed system, and the
episode says so instead of repeating it. An earlier draft of B11 said learning
tunes "five weights" — **no source states a count**, so that number was cut
before any audio was generated.

### F15 — airmass model (not spoken, but underlies every m5 and seeing number)

Kasten–Young (S4), not `sec(z)`. Relevant because the two schedulers differ
precisely in how low they are willing to work.

---

## What is simulated, and therefore NOT a claim about ZTF or Rubin

`assets/sched.py` is a toy: one 8-hour night, 16 half-hour blocks, two bands,
a −30° site, fields on a Fibonacci sphere, invented axis rates, HiGHS in place
of Gurobi, and **no weather**. It reproduces the *direction* of S1's published
comparison; it is not a replication of it, and nothing in the narration says
these numbers are ZTF's. The two ZTF figures that ARE quoted as ZTF's — the
completion percentages and the filter-change counts — are flagged as theirs
in the beats that use them.
