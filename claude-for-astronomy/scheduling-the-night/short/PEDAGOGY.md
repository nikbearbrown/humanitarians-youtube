# PEDAGOGY — Ep. 17, *scheduling-the-night*

**GATE P. A human signs this before any audio is generated.**
Audio here is free (Kokoro, local). This is a quality gate, not a cost gate.

---

## The one thing a student should leave with

**Some problems look like AI's job because they're enormous, and aren't.**
A telescope's night has 10²⁵⁶⁷ possible orderings. That number *feels* like it
demands a learned policy. It demands the opposite: because the objective and
the constraints are both already written down, the right move is to **encode
the structure and solve it**, not to learn it from experience.

The series spine is *when to use AI and when not to*. This episode is a
clean "not" — and the evidence is that the two biggest sky surveys on Earth
both independently landed there.

## The second thing, which is the harder one

**Optimise the thing that only counts when it's finished, not the thing that's
easy to count.** Exposures per hour is easy to count. But a g-exposure with no
matching r-exposure is not half a detection — it's zero, because nothing can be
compared against nothing. ZTF's measured result is the whole lesson: the two
schedulers had *comparable* exposure rates, and completely different
completion fractions.

Students will recognise this immediately outside astronomy: a sprint that ships
nine half-features, a week of study that opens six topics and closes none.

## Why this isn't Ep. 10

`ideas.md` Notes: *"Ep. 17 is about planning the survey's own observing
schedule, not deciding which transients deserve follow-up (Ep. 10)."*

Every decision in this episode is made **before any photon arrives**, about
where to point. Nothing ranks an alert, scores a candidate, or decides what's
worth chasing. B02 states the boundary out loud ("where to point, decided
before any photon arrives"). No plate, number, or source is shared with Ep. 10
or with Ep. 16.

## The arc

| beat | does what | why it's there |
|---|---|---|
| B00–B02 | pose it; name the hinge | "you cannot search those orders, so both schedulers change what a *move* is" |
| B03 | the board | shows the constraint before any decision exists — a student must see the game board before the game |
| B04 | the number | the combinatorics, with the atom-count anchor |
| B05 | Rubin's move → "now" | greedy, on purpose, every 30 s |
| B06 | ZTF's move → "which block" | makes exact solution possible; teaches the colour map |
| B07 | **the equals sign** | the load-bearing beat: one constraint, not a preference |
| B08 | what it bought | 78 holes vs none |
| B09 | **the attack on my own claim** | pay greedy to care — it gets most of the way |
| B10 | the tell + the counterweight | not speed; and ZTF's ILP made *more* filter changes |
| B11–B13 | verdict, handoff, outro | names the "when not to learn it" rule; hands the student a schedule of their own |

## What I deliberately did NOT do

- **Did not claim reinforcement learning schedules Rubin.** `ideas.md`'s topic
  line says "optimization and reinforcement learning." The deployed scheduler
  (SMTN-020) never mentions RL, ML, or neural networks. Repeating the blurb
  would have been the easy path and would have been wrong. See FACTCHECK F14.
- **Did not claim a weight count.** An earlier B11 draft said learning tunes
  "five weights." No source states a number, so it was cut.
- **Did not hide the counterweight.** ZTF's ILP made *more* filter changes
  (3.6 vs 2.0/night) despite penalising them. That's in B10.
- **Did not assert the plan is optimal.** The solver hits its time limit. Said
  in FACTCHECK F13; no narration line claims optimality.
- **Did not let greedy be a strawman.** B09 pays greedy to want completion and
  reports that it climbs to 0.975. If this episode's claim is wrong, B09 is
  where a viewer gets to see it.

## Honest risks in this cut

1. **B09 complicates the story.** Greedy reaching 0.975 is *close* to the
   planner's 1.000, and a sharp student may conclude the planner isn't worth
   it. I think that reading is correct and worth having — the distinction I
   draw is that greedy got there by *starting fewer fields*, i.e. by emulating
   lookahead it does not have, and still paid 2.3% of its rate. If the signer
   thinks B09 undercuts rather than strengthens the episode, say so now, not
   after audio.
2. **"Without machine learning" is a strong opener.** It is scoped to the
   pointing decision only (FACTCHECK F14). If that scoping doesn't survive a
   first listen of B00, it needs rewording.
3. **The simulation is a toy** and the gap it shows (1.71 vs 1.29 airmass) is
   wider than ZTF's real one (1.20 vs 1.11). The narration never calls my
   numbers ZTF's, but a viewer could conflate them.

## Checks before signing

- [x] Spine question answered (when NOT to use AI), explicitly, in B11
- [x] Ep. 10 boundary respected and stated on screen
- [x] Every spoken number traced in FACTCHECK
- [x] All measured numbers asserted in `gen_sched.py` (build fails otherwise)
- [x] Published counter-evidence included rather than omitted
- [x] A falsification test ships *as a beat*, not as a footnote
- [x] 430 words → 2:40 predicted, 2:57 worst case — under 3:00
- [x] Plates carry imagery only; all labels placed by `scenes.py`

---

## VERDICT

```
VERDICT: PASS
signed:  Om Mali
date:    11/13/2026
```

