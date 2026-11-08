# PEDAGOGY — *Aim Where It's Going.*

Ep. 16 · `predictive-adaptive-optics` · **GATE P**

> **This gate binds.** A human signs below with `VERDICT: PASS` before any
> audio is generated. It is a quality gate, not a cost gate — Kokoro is free
> and local. What is being signed off is the **teaching**, not the budget.

---

## The one idea

**A correction that arrives late is a correction aimed at the wrong place.**

Under Taylor frozen flow the atmosphere does not change, it *travels*. So a
delay of 1.7 milliseconds is not really a duration — it is **1.7 centimetres
of sideways slide**. And that reframing is the whole episode, because a
displacement has a future you can read off its past, where a random change
does not.

The pivot line: **prediction doesn't make the loop faster, it makes the
mirror aim ahead.**

## Why this topic, here

`ideas.md` Astronomy topic 16. Its Notes fence it explicitly:

> *Ep. 16 is about real-time instrument control (moving a mirror), not
> cleaning up images afterward.*

That separates it from Ep. 09 (`denoising-deep-space`), which is post-facto
reconstruction. This episode never repairs an image. Every correction in it
happens **before the photons reach the detector**, and B02's closing line says
exactly that so the boundary is audible, not just structural.

## The teaching arc

| Stage | Beat | What it does |
|---|---|---|
| **Framework** | B02 | measure → bend → two milliseconds → the air moved. Stated before any number. |
| **Reframe** | B03 | the delay, converted into a distance. 1.7 ms × 10 m/s = 1.7 cm, against a 15 cm coherence cell. |
| **Worked law** | B04 | the lag error *is* the structure function walked that far; exponent 5/3 recovered, and only 16% of it is reachable. |
| **Mechanism** | B05 | what the predictor actually is: 24 frames, one linear filter, no physics. |
| **Decomposition** | B06 | where the gain comes from — back in time, not across the pupil. |
| **Falsifiability** | B07 | the gain collapses with sensor noise. The claim has a condition, and the condition is measured. |
| **Reconciliation** | B08 | why a 11× cut in the lag term shows up as a published 20% in the total. |
| **Honest record** | B09 | two dated results from the same predictor that say different things. |
| **The tell** | B10 | the expectation that was refused, named out loud. |
| **Scaffolded task** | B12 | the viewer separates reachable error from untouchable error in a loop of their own. |

## What a viewer should be able to do afterwards

1. **Convert a control delay into a displacement** and ask whether that
   displacement is small compared to the system's correlation length. This is
   the transferable move, and it is not specific to telescopes.
2. **Ask what fraction of an error budget a method can even touch** before
   being impressed by its headline improvement. B08 is the reusable piece of
   arithmetic: crush a fifth, move a fifth.
3. **Distinguish "the model is weak" from "the measurement is noisy."** The
   episode's answer is that the second was the binding constraint all along.

## The honesty load

Four places where the episode reports against its own interest:

1. **B10 — the refused expectation.** I expected more atmospheric layers to
   break the predictor. In clean air three layers still gave 183×, because a
   sum of frozen translations is still a linear process. The hypothesis was
   wrong and the beat says so rather than quietly dropping it.
2. **B09 — the complicating result.** The 2021 coronagraphic contrast gain is
   the flattering number. The 2026 on-sky test, same predictor, reports
   comparable Strehl and contrast. Both are on screen, both dated.
3. **B06 — a near-zero reported as near zero.** Spatial-only prediction
   measured 1.2×. It is drawn as a bar that barely clears the baseline rather
   than being omitted or rounded up.
4. **B08 — the deflationary reading of my own result.** 11.2× sounds large;
   the beat immediately explains why the real-world number is 20%.

## Register check — Pragmatist, for STUDENTS

The HAI channel's audience is people learning when to use AI and when not to.
This episode's version of that question is pointed: **the "AI" here is ridge
regression with 1,440 parameters, and it works for a reason you can state in
one sentence** — the pattern is sliding. B05 refuses to dress it up. The
lesson is that knowing *why* a method can work tells you where it will stop
working, and B07 then shows exactly where.

## What is NOT claimed

- No Strehl number from the simulation (it would describe a 60-mode toy).
- No comparison to Doelman's 1.77× theoretical ceiling (different quantity).
- No claim that r₀ = 15 cm and v = 10 m/s describe Mauna Kea (stated
  parameters, cited as such on screen).
- No claim that prediction beats shortening the loop — checked, and false
  here by 4× against 11×, so the verdict line was rewritten.

## Runtime

428 words. Against Ep. 15's measured 0.3731 s/word that predicts **2:38.6**,
inside the 3:00 cap with ~21 s of margin. The words-only model has been noisy
by ±5–10% with no consistent sign across Eps. 06–15, so the margin is real but
not large.

---

## Pre-audio gate status

| Gate | Result |
|---|---|
| **F** paperwork | PASS |
| **L** beat lint | PASS — clean, 14 beats |
| **A** render-free pre-flight | PASS — 10/10, first pass |
| **W** WCAG + margins | PASS — 10/10, first pass |
| **B** pixel layout, landscape | PASS — 10/10 |
| **B** pixel layout, portrait | PASS — 10/10 after 2 fixes |
| **visual pre-flight** | 20 frames read; **5 defects found and fixed** |

Detail in `CHECKS-REPORT.md`.

---

## SIGNATURE

Audio is generated only after this reads `VERDICT: PASS`.

```
VERDICT: PASS
SIGNED: Om Mali
DATE: 11/06/2026
```
