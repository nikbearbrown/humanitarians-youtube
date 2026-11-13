# Week 25 — Angle

**Topic:** `claude-for-education/reinforcement-learning-an-introduction` (see `TOPIC-DECISION.md`)
**Working title:** *A Weighted Coin*
**Decided:** 2026-10-01, pending Tanmay's sign-off

---

## The angle in one line

> In a corridor where the learner sees the same square three times, every fixed rule fails,
> and the best possible policy is a coin weighted to land "right" **2 − √2 ≈ 58.6%** of the time.
> A learner that hunts for the single best *action* can't reach it. A learner that tunes the
> *probability* can, and it finds that exact number on its own.

The surprise to carry: a random choice can be the **optimum**, not a fallback, and the precise
amount of randomness is something you can compute.

## Where it comes from in the GitHub source

The repo folder is an unbuilt auto-conversion, and most of it is boilerplate. The one concrete,
checkable case is in `SOURCES.md`:

> "The short-corridor example (Figure 13.1) proves action-value methods with ε-greedy fail where
> policy gradient succeeds—finding optimal stochastic policy (59% right) versus settling for
> deterministic extremes (-44 or -82)."

The film builds on that line: we reproduce it, then extend it. The other source material
(value functions, optimistic initialization, Sarsa/Expected Sarsa/Tree Backup, Watson-style wagering,
TD-Gammon's two-ply search, the 19% / 27% controller, AlphaGo) is left out on purpose: *one
insight, one case*, as the README's own build loop asks.

## What we measured (`experiment/corridor.py` → `results.json`)

Stdlib Python, seeded, 30 seeds per learner, runs in under a second. The setup follows the book's
example: three non-terminal states, actions reversed in the middle one, reward −1 per step,
γ = 1, and one feature vector shared by all three states.

| Policy | Value of start state | How we got it |
|---|---|---|
| Always right / always left | **never finishes** | exact |
| ε-greedy "mostly right" (P = 0.95) | **−44.21** | exact |
| ε-greedy "mostly left" (P = 0.05) | **−82.11** | exact |
| Fair coin (P = 0.5) | **−12.00** | exact |
| Optimum, P = 2 − √2 = 0.5858 | **−11.66** | exact (closed form + grid search) |
| Sarsa, ε = 0.1, 1,000 episodes | chose "mostly right" in **30 / 30** runs, so −44.21 | learned |
| REINFORCE, started at "mostly left" (−82.11), 2,000 ep | mean P(right) **0.586** [0.530–0.652], value **−11.70** (worst −11.88) | learned |

REINFORCE learning curve, mean return per 100-episode block:
`−39 −17 −14 −13 −13 −12 …` It is near-optimal within about 400 episodes.

Two honest notes, both carried into FACTCHECK:

- From θ = 0, REINFORCE *starts* as a fair coin, which is already worth −12. That run proves
  nothing about learning, so the film uses the "start at mostly-left" run only.
- The source's "59%" is the book's rounding. The exact optimum is 2 − √2 = 0.5858…, i.e. 58.6%.

## The boundary (this is where the film ends)

The coin only helps because the learner **can't see** which square it's in. Give the learner one
feature that marks the switched square and a deterministic rule wins outright: right, left, right,
**3 steps, value −3**, nearly four times better than the best coin (3.89×). Measured: the same Sarsa learner given one value pair per state learns right-left-right in 30 / 30 seeds (`sarsa_sees_state`). Randomness is the best response to
what you can't observe. It is not a substitute for seeing more, and the film says so plainly.

The book's own bridge (Sec. 13.1, p. 323, verified in FACTCHECK A9): in imperfect-information card games,
optimal play is often two different actions with specific probabilities, as with bluffing in poker.
If we use it, it's a one-beat pointer. The poker reason (an opponent) differs from the corridor's
reason (blindness), and the film must not merge the two.

## Structure: the corridor is the film

This isn't a numbered-question framework and it doesn't end with a "your turn" rubric (see W17–W24
structures). The chapters are the policies, tried in order of how sensible they sound, and each one
walks the same four-square corridor on screen:

1. **The corridor.** The rules, the switched square, and the learner's-eye view: one grey square, three times.
2. **Always right.** It loops forever. **Always left.** It never leaves.
3. **The value learner.** Sarsa, 30 runs, all "mostly right": −44.
4. **The turn.** A plain fair coin does −12, more than three and a half times better than the learner (44.21 / 12 = 3.68×).
5. **The dial.** The full curve over P(right); the peak isn't 50%, it's 2 − √2.
6. **The learner that tunes the dial.** REINFORCE from −82 to −12; it lands on 0.586.
7. **The boundary.** Let it see the switched square, and the coin loses to right-left-right.
8. **Close.** One open question, not a rubric: when a system answers "this, 59% of the time,"
   is it being indecisive, or is that the best it can do with what it can see?

**Short (written separately, per the Shorts rule):** one arc, *always-right loops forever → fair
coin escapes → the weighted coin is the optimum*, with its own ending at 2 − √2.

## Uniqueness audit

**Library (`main` @ `5716c413f` + all fellow branches).** No other folder mentions Sutton, Barto,
the short corridor or policy gradient (see `TOPIC-DECISION.md`). Searching every beat sheet for
`stochastic policy | coin flip | mixed strategy | rock-paper-scissors | aliasing` finds 11 folders.
Every "coin flip" there is a byword for **chance-level failure** (Sachin B / Dhrumil S AUC ≈ 0.5,
Sanjana R's P50 dates, `claude-liam-money-hard-stop` "not a coin flip",
`why-two-wellbehaved-agents…` "independent coin flips"). None treats a coin as the **optimal**
policy, which is this film's thesis, so the meaning is reversed.

**Nearest fellow work (boundary):** Kehinde O, `2026-09-08-the-target-that-moved`, a DQN
(value-based, ε-greedy) target-network fix on Lunar Lander. This film doesn't touch training
stability or target networks. It must not frame value-based methods as broken in general:
the failure is specific to a learner that can't distinguish states.

**Our own narration, W15–W24 (44 beat sheets, deduplicated).** No hits for coin, randomness-as-answer,
corridor, reward or stochastic policy. The one W23 "stochastic" (*stochastic parrot*) is unrelated.
The closest prior ideas, kept as lines not to cross:

- **W20 thesis** ("two ideas… became one idea in your build") and **W24's rejected first angle**
  ("two inputs look the same at one check"). Their claim is *conflation causes an error*. This
  film's claim is *calibrated randomness is the optimal response*. So narration must not
  pivot on "they looked the same, so it went wrong."
- **W21 work B10** ("indistinguishable from a busy Tuesday") and **W17 topic B4** ("can't tell them
  apart"). Avoid "indistinguishable" / "can't tell them apart" phrasing; say "it sees one square, three times."

## Checks before any beat sheet (front-loaded)

1. ~~FACTCHECK against the book~~: done, see `FACTCHECK.md` (19 film claims, none unsupported).
2. Phonemes for Kokoro: "two minus root two", "Sarsa", "REINFORCE", "epsilon", "Sutton", "Barto".
3. Decide visuals: the corridor as one reusable Remotion/Manim scene; the value curve as the
   single chart.
