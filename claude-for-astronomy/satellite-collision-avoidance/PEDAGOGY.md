# PEDAGOGY — *Safer By Not Looking.*

**GATE P** · Ep. 15 · `satellite-collision-avoidance` · **the series finale**

> This gate binds. Narration audio is **not generated** until a human writes
> `VERDICT: PASS` at the bottom of this file. It is a quality gate, not a cost
> gate — the audio here is free (Kokoro `af_bella`, local, $0.00).

---

## What this episode teaches

**The collision probability is not the chance two satellites hit. It is the
chance they hit *given your uncertainty* — so past a certain point, knowing
less makes the number smaller.**

And the second half: **a score dominated by the 99.7 % of nights when nothing
was ever going to happen will prefer the forecaster that is wrong on the
0.3 % that matter.**

Topic 15 of the brief is "AI predicting and preventing space debris
collisions in increasingly crowded orbits". The crowding is real and the
reel says so. But the episode goes after the quantity every downstream model
is trained to predict, because that is where the interesting thing is.

## Why this is the right finale

Fourteen episodes asked *where did this answer come from*. They found the
limit in the data, the objective, the evaluation, the class definition, the
labels. **Ep. 15 finds a quantity whose answer is partly "from you."**

Probability dilution is not a modelling mistake. The integral is correct.
Every step is defensible. And yet the number can be lowered by tracking an
object less carefully — which means the thing on the dashboard is a joint
statement about the sky *and* about the observer, and nobody downstream can
tell which part moved.

That closes the series' loop better than any other topic in the list: it is
the case where asking "where did this come from?" returns, in part, *you*.

## The spine, in five moves

1. **B02 — the claim, before any evidence.** Pc is computed *given* a
   covariance. Make the covariance bigger and the number gets smaller. This
   is definitional, not an inference, so it can be stated flatly up front.
2. **B03–B05 — why that is structurally true.** The published benchmark
   (15,321 approaches, 30 ever dangerous). What the integral actually
   measures — the share of your error that lands on a twenty-metre disk. And
   the curve: tiny when you know everything, tiny when you know nothing, with
   a summit in between.
3. **B06 — the consequence, measured.** The same conjunction, the same two
   objects. Tracked well it is above the action threshold; with the
   uncertainty seven times larger the alert is gone.
4. **B07–B09 — the forecasting problem this creates.** Alerts almost always
   decay as tracking improves, and the dangerous ones announce themselves
   early. So a trained model beats "assume nothing changes" four times over
   on all 40,000 events — and loses to it three times over on the 124 anyone
   was warned about. ESA saw the same shape for real: of 97 teams, 12 beat
   the naive forecast.
5. **B10 — the tell, including the fix that failed.** Giving the model the
   dilution geometry moved the error 2.7 %. The problem was never the
   features. Ask instead how bad the encounter could possibly look, and the
   answer stops depending on how hard you looked.

## What a viewer should be able to do afterwards

Ask, of any risk number they act on: **can I make this number better without
making anything safer?** And: **is my score dominated by the cases I don't
care about?** That is exactly the B12 handoff, and its three grading lines
are the skill.

## The honesty constraints this reel accepted

- **The simulation is never presented as a model of any real catalogue or
  operator.** There is no propagator here. What is real is the Pc integral
  and the shape of its dependence on σ — and those are the only things
  claimed. Every computed beat carries "computed in this reel".
- **The reel does not say anybody is getting this wrong.** Dilution, maximum
  probability and covariance realism are well known inside the
  conjunction-assessment community; Alfano patented the remedy in 2008. The
  claim is about what the quantity *is*.
- **"Degrade your tracking to clear the alert" is not an accusation.** It is
  a property of the metric, stated as a property.
- **The ESA challenge is not called a failure.** The top teams did beat the
  baseline. The published point used here is the margin, and how few managed
  it — the organisers' own observation.
- **max-Pc is not called a solution.** It is conservative by design and would
  trigger more manoeuvres than anyone can fly. The reel says only that it
  answers a question that does not depend on your tracking.
- **The reel takes no position in the false-confidence debate.** Balch,
  Martin & Ferson argue dilution reveals a foundational flaw in probabilistic
  inference. That argument is live. The dilution effect itself is not in
  dispute, and only the effect is used.

## Two places the work corrected itself

These are the reason the gate is worth signing, so they are stated plainly.

- **The central claim was refused by the measurement and rewritten.** The
  hypothesis was that persistence would beat the trained model. It does not —
  it is 4× *worse* overall. What is true is sharper: the ranking *reverses*
  between the aggregate score and the notified events. The claim changed; the
  experiment did not.
- **A plate was drawn to show something that does not exist.** `shrink.png`
  originally showed alerts breaking late. The population contains **zero**
  such events, and not by accident — once the covariance shrinks below the
  miss distance, Pc falls. The plate was redrawn to show the real structure.

Both are logged in FACTCHECK.md rather than quietly fixed.

## Register and tier

Pragmatist register, Humanitarians AI. **Fellow Tier throughout**: Kokoro
`af_bella` for narration, Manim and Remotion for picture, no API keys, no
paid service, **$0.00**. No image-generation prompts at all.

## Runtime

426 words. Predicted **2:31** against Ep. 14's measured 0.3548 s/word,
leaving ~29 s of margin against the under-3:00 requirement. The words-only
model has been noise of ±5–10 % with no consistent sign across Eps. 06–14,
so the margin is real. Final runtime is set by the **measured** MP3
durations, not this estimate.

## Pre-audio gate status

| Gate | What it checks | Result |
|---|---|---|
| **F** | paperwork complete | PASS |
| **L** | beat mix / ledger | PASS — 14 beats, 10 Manim + 4 Remotion |
| **A** | render-free scene pre-flight | PASS — 10/10 after 1 fix |
| **W** | WCAG contrast + margins | PASS — 10/10 |
| **B** | pixel layout, both aspects | see CHECKS-REPORT.md |
| pre-flight | 20 frames read by eye | see CHECKS-REPORT.md |

Audio, pacing, render, GATE V and the 9:16 derivative all come **after** this
signature.

---

## Verdict

Reviewed by: Om Mali  Date: 10/30/2026

```
VERDICT: PASS
```

*(Write `VERDICT: PASS` to release audio generation. Anything else holds it.)*
