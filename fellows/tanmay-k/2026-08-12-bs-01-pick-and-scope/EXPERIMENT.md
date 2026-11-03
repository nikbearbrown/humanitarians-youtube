# EXPERIMENT — can a model run the adjacent-profession test?

Primary source for any number this film puts on screen. Append-only; dated entries.

**Question.** The source draft's CTA (`claude-liam-bs-01-pick-and-scope`, beat B07) tells
students to paste a role statement into Claude and have it run the adjacent-profession
test. Nobody measured whether a model can run that test. This measures it.

| | |
|---|---|
| Claimed cause | the verdict tracks exclusion of adjacent roles |
| Rival | the verdict tracks word count / density of domain jargon |
| Isolating arm | `swapped` — matched to `full` on words **and** domain terms, but not identifying |
| Q3 falsifier | `stripped` — if removing the load-bearing phrase doesn't flip the verdict, the phrase wasn't load-bearing |
| Q4 guarantee | `full` (expect PASS) and `generic` (expect FAIL) anchors, so the run can't silently collect no signal |

Harness: [experiment/neighbour_bench.py](experiment/neighbour_bench.py). Items:
[experiment/items.py](experiment/items.py), 6 bases × 4 variants across healthcare,
finance, and engineering. The `full`↔`swapped` match is verified in code — **0 word
delta and 0 domain-term delta on all six pairs.**

---

## Revision 1 — 2026-08-18 — PILOT FAILED THE GATE

48 calls (24 items × 1 repeat × 2 models), **$0.0757**. Results:
`experiment/results-20260818T040606Z.json`.

### PASS rate by variant

| Model | full | swapped | stripped | generic |
|---|---:|---:|---:|---:|
| `claude-haiku-4-5` | 83% | 33% | 67% | **0%** |
| `claude-sonnet-5` | 33% | 17% | 33% | **0%** |

Ground truth: `full`=PASS, everything else=FAIL.

### The gate

`generic` FAILed **100% of the time on both models** — the fail anchor is solid.
The *pass* anchor is what broke: Sonnet 5 rejected 4 of 6 statements designated PASS,
giving anchor separation of only +33% and failing the gate.

### Why — the neighbour choice swamps everything else

Reading the per-trial `nearest_neighbour` field explains the whole divergence. **The
verdict is dominated by how near a neighbour the model happens to pick**, not by the
statement under test:

| Item | Haiku's neighbour → verdict | Sonnet 5's neighbour → verdict |
|---|---|---|
| H1 pharmacist | *Hospital pharmacist* → FAIL | *Discharge/floor nurse* → PASS |
| F1 credit analyst | *Commercial loan officer* → PASS | *Commercial loan underwriter* → FAIL |
| F2 crime investigator | *Compliance analyst* → PASS | *AML/KYC analyst on transaction monitoring* → FAIL |
| E1 backend engineer | *DevOps engineer* → PASS | *Backend engineer on the fraud-detection team* → FAIL |

Three distinct failure modes, all of them about neighbour selection:

1. **Same-profession neighbour.** On H1, Haiku picked "hospital pharmacist" — not an
   adjacent profession, the *same* one. It then correctly reasoned that a hospital
   pharmacist could claim the statement, so the item trivially FAILs. Nothing about the
   statement was tested.
2. **Far neighbour → trivial pass.** For a backend engineer on the payments team, Haiku
   picked "DevOps engineer." A far neighbour is easy to exclude, so the item trivially
   PASSes. Again, the statement wasn't tested.
3. **Near neighbour → honest fail.** Sonnet 5 picked "backend engineer on the adjacent
   fraud-detection team" and "commercial loan underwriter at the same bank" — genuinely
   nearest neighbours, who genuinely could claim these statements.

**Sonnet 5's verdicts are arguably the better analysis.** Its FAILs are not errors — a
commercial loan underwriter at the same bank really could write F1's statement. That
means my ground truth was the weak link: *"`full` should PASS" is not well-defined until
the neighbour is fixed*, and I left the model to choose it.

**Haiku passed the gate for the wrong reason.** Its +83% separation came from picking
lenient, distant neighbours — not from the instrument working. A gate that only checked
Haiku would have waved through a broken design.

### What this already establishes

This is framework question 2 — *who is the nearest neighbour?* — firing on live data.
The framework predicted that the test is only as strong as the closest neighbour you
pick, and that a far neighbour passes trivially. Both happened, on both models.

**Consequence for the draft:** its CTA hands the neighbour choice to the model and never
constrains it. The variance above is inherited directly by any student who follows beat
B07. That is a real, measured defect in the draft's advice — not a hypothesis.

### Not established

Nothing yet about specificity vs. length. `swapped` (33% / 17% PASS) and `stripped`
(67% / 33% PASS) are both confounded by the same uncontrolled neighbour choice, so
those rates measure nothing attributable. **Do not put them on screen.**

### Revision 2 — the fix

Split the neighbour into a controlled variable instead of leaving it free:

- **Arm P (pinned):** supply the human-designated nearest neighbour in the prompt. The
  verdict then measures *exclusion given a fixed neighbour* — the clean arm where
  specificity-vs-length becomes measurable and ground truth is well-defined.
- **Arm F (free):** the model picks its own neighbour, as the draft's CTA has it. This
  measures neighbour-choice variance and agreement with the human designation — which is
  the finding revision 1 stumbled into, now measured deliberately.

6 bases × 4 variants × 2 arms = 48 items. Pilot at 1 repeat × 2 models = 96 calls,
≈ $0.15.

**Cost of learning this: 7.6 cents, before writing 24 more statements or running a
powered pass.** Film 4 discovered its Q4 problem the expensive way, after a full build;
this one was caught by a gate designed for exactly that purpose.

---

## Revision 2 — 2026-08-18 — PILOT FAILED THE GATE AGAIN. Root cause: my items.

96 calls (24 items × 2 arms × 1 repeat × 2 models), **$0.1530**. Results:
`experiment/results-20260818T041433Z.json`.

Pinning the neighbour worked as a mechanism — free-arm verdicts changed in 33% (Haiku)
and 17% (Sonnet 5) of items once the neighbour was fixed, confirming revision 1's
diagnosis. But the gate failed again.

### PASS rate, pinned arm (ground truth well-defined)

| Model | full | swapped | stripped | generic |
|---|---:|---:|---:|---:|
| `claude-haiku-4-5` | 67% | 17% | 33% | **0%** |
| `claude-sonnet-5` | **50%** | **50%** | 33% | **0%** |

### The root cause is my ground truth, not the models

Sonnet 5 failed three of my six `full` designations in the pinned arm. Its stated
reasons are **correct**, and they indict the items:

| Item | Pinned neighbour | Sonnet 5's reason (verbatim, trimmed) |
|---|---|---|
| E1 | platform engineer, same payments team | "could plausibly review a pull request touching the fraud-detection service, since the statement contains no phrase distinguishing…" |
| E2 | on-call platform engineer | "performs essentially the same duty of deciding canary rollbacks during incidents, so the statement does not exclude them" |
| F2 | AML compliance officer | "routinely performs sanctions-screening alert clearance on correspondent-bank wire traffic…" |

These are right. A platform engineer on the same payments team really could review that
PR. An on-call platform engineer really does make canary rollback calls. **Three of my
six "identifying" statements do not identify**, and in revision 1 my designated
*neighbours* were wrong too (the nearest neighbour of a credit analyst who re-underwrites
covenant breaches is an underwriter, not a relationship manager — which is exactly the
neighbour Sonnet 5 picked unprompted).

**The wall:** the correctness framing requires me to be right about which statements
exclude which neighbours. Two revisions have now failed, both traceable to that same
component. I am the broken instrument, and no sample size or prompt fix reaches it.

Also note `F1/full` and `F1/swapped` both PASS on both models, and `H1`/`H2` `swapped`
PASS on Sonnet 5. `swapped` is the length- and jargon-matched **non**-identifying
control, so a model passing it at the same rate as `full` is the length confound
appearing — but at n=6 per cell that is a hint, not a measurement. **Not for screen.**

### What survives without any ground truth from me

Reliability needs no adjudication of who is right:

| Measure | Pinned | Free |
|---|---:|---:|
| Cross-model disagreement on identical items | **12%** | **21%** |
| Verdicts changed by pinning the neighbour | — | 33% Haiku / 17% Sonnet 5 |
| Degenerate same-title "neighbour" chosen | — | 12% both models |

`generic` FAILed 100% in the pinned arm on both models — the one anchor that has held
across both revisions.

### Recommended revision 3 — drop correctness, measure reliability

Reframe the question from *"does the model get it right?"* (needs my judgment) to
**"is the answer stable?"** (needs none). A student following beat B07 cares about the
second question, and it is answerable with the items we already have:

- **within-model stability** — same item, same arm, N repeats: does the verdict flip?
- **cross-model agreement** — Haiku vs Sonnet 5 on identical items
- **arm effect** — how often pinning the neighbour changes the answer
- **degenerate-neighbour rate** — how often the model picks the same profession

If the same statement gets different verdicts depending on which model you ask, which
neighbour got picked, or which run it was, then *"paste it into Claude and run the
adjacent-profession test"* is unreliable advice **regardless of who is correct**. That is
a defensible on-screen claim with a bounded number, and it needs no item rewrite.

Cost: 24 items × 2 arms × 5 repeats × 2 models = 480 calls ≈ **$0.75**.

**Spend to date: ~$0.23** across two failed revisions and a smoke test.

---

## Revision 3 — 2026-08-18 — MEASURED. Reliability framing works.

480 calls (24 items × 2 arms × 5 repeats × 2 models), **0 errors, $0.7640**. Results:
`experiment/results-20260818T042<…>.json`, `experiment/run-rev3.log`.

Correctness was abandoned as the primary measure (see revision 2 — the author's ground
truth was the broken component). Every number below is a **disagreement rate** and none
depends on anyone being right about which statements pass.

### Headline — the model does not pick the same neighbour twice

Same statement, same question, five runs:

| Model | Mean distinct neighbours named / item | Items given >1 different neighbour | Degenerate same-title choices |
|---|---:|---:|---:|
| `claude-haiku-4-5` | **2.25** | **19/24 = 79%** | 18/120 = 15% |
| `claude-sonnet-5` | **2.46** | **17/24 = 71%** | 11/120 = 9% |

Ask five times, get roughly two and a half different answers to *"who is your nearest
neighbour?"* — for about three in four statements. The adjacent-profession test's verdict
is downstream of that choice, so the verdict inherits the churn.

### Verdict stability — and the fix

| Model | Arm | Items that flipped PASS↔FAIL across 5 runs |
|---|---|---:|
| `claude-haiku-4-5` | free | **10/24 = 42%** |
| `claude-haiku-4-5` | pinned | 4/24 = **17%** |
| `claude-sonnet-5` | free | 4/24 = **17%** |
| `claude-sonnet-5` | pinned | 2/24 = **8%** |

**Pinning the neighbour cuts the flip rate by about 2.5× on both models.** On Haiku's free
arm, 42% of statements got *both* PASS and FAIL from the same model with nothing changed
but the run — coin-flip territory.

### Cross-model agreement and arm effect

| Measure | Free | Pinned |
|---|---:|---:|
| Haiku vs Sonnet 5 disagree (modal verdict) | **33%** | **12%** |
| Verdict changed by pinning | Haiku 39% of trials, Sonnet 5 13% | — |

### Screen-eligible vs not

**Screen-eligible** (no ground truth required): every figure above.

**NOT for screen:** the `full`/`swapped`/`stripped` correctness rates. Revision 2 showed
three of six `full` statements don't exclude their designated neighbour, so those cells
measure the author's item-writing, not the models.

**Borderline, supporting only:** in the pinned arm at n=30/cell, Haiku separated `full`
from the length-and-jargon-matched `swapped` control sharply (70% vs 13%), while Sonnet 5
did not (50% vs 47% — a one-item difference). Read narrowly, Sonnet 5 passed a control
that is non-identifying *by construction* on 14 of 30 trials. That is consistent with the
length/jargon rival, but `full`'s baseline is contaminated, so it stays a supporting
observation with the caveat stated — never a headline.

`generic` FAILed **0% PASS** in the pinned arm on both models, across all three revisions.

### What this establishes for the film

1. **Framework question 2 is now measured, not asserted.** "Who is the nearest neighbour?"
   was the axis the framework said would dominate. It does, on both models, at 71–79%.
2. **The draft's CTA has a named, measured defect.** Beat B07 tells students to let the
   model pick the neighbour. That choice is unstable ~3 times in 4.
3. **There is a fix, and it is one sentence.** *Tell the model who the neighbour is
   instead of asking it.* Measured effect: ~2.5× fewer verdict flips, cross-model
   disagreement 33% → 12%.
4. **The draft's advice survives; its method changes.** The adjacent-profession test is
   sound. Handing the neighbour choice to a model is what breaks it.

B10 is live. Falsifiability rises from 1 to 2 — the framework predicted an effect and the
effect was measured.

**Total experiment spend across all three revisions: $0.996.**
