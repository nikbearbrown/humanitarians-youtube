# Week 25 — FACTCHECK

**Film:** *A Weighted Coin* (working title) · angle in `ANGLE.md`
**Primary source:** Sutton, R. S. & Barto, A. G., *Reinforcement Learning: An Introduction*, 2nd ed.
(MIT Press; © 2018, 2020), the authors' free PDF `RLbook2020.pdf` from incompleteideas.net. Page
numbers below are the **printed** book pages. The PDF was read for this audit and then deleted;
anyone can re-fetch it from the authors' site to check.
**Measured source:** `experiment/corridor.py` → `experiment/results.json` (stdlib Python, seeds 0–29).
**Checked:** 2026-10-01

Verdicts: **SUPPORTED** · **QUALIFY** (true with a stated condition or wording fix) ·
**UNSUPPORTED** · **OURS** (our own measurement, so the film must label it as ours)

---

## A. Claims the film will make

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| A1 | The corridor is the book's own worked example: Example 13.1, "Short corridor with switched actions", Chapter 13 *Policy Gradient Methods* | SUPPORTED | p. 323 |
| A2 | Three non-terminal states, two actions (right, left), reward −1 per step; left does nothing in the first state; in the second state the actions are reversed | SUPPORTED | p. 323, Example 13.1 |
| A3 | The learner gets the same features in every state: x(s, right) = [1, 0], x(s, left) = [0, 1] for all s | SUPPORTED | p. 323. The book attributes the difficulty to the states appearing identical under function approximation |
| A4 | An ε-greedy action-value method can only be "mostly right" or "mostly left" (probability 1 − ε/2) | SUPPORTED | p. 323: such a method "is forced to choose between just two policies" |
| A5 | With ε = 0.1 those two policies are worth **−44** and **−82** at the start state | QUALIFY | The book says **less than** −44 and −82 (p. 323). Our exact values are −44.21 and −82.11. Say "about −44 and −82", or use our exact figures labelled as ours |
| A6 | The best policy picks right about 59% of the time and scores about −11.6 | SUPPORTED | p. 323: "about 0.59", "about −11.6" |
| A7 | The exact optimum is 2 − √2 ≈ 0.5858 | SUPPORTED (derived) | The book poses it as **Exercise 13.1** (p. 324) without printing the answer. Our closed form and a 0.0001 grid search both give 0.5858 / −11.657, matching independent worked solutions (minibatchai.com 2022; instrumentalcomplexity.com). Say "works out to two minus root two", not "the book says" **Algebra (MATH-TYPESETTING.md):** setting dv/dp = 0 gives p² − 4p + 2 = 0, so p = 2 ± √2. Only 2 − √2 lies in [0, 1] (2 + √2 ≈ 3.41). Check: (2 − √2)² − 4(2 − √2) + 2 = 6 − 4√2 − 8 + 4√2 + 2 = 0 ✓. On screen it's typeset *p*\* = 2 − √2 ≈ 0.586, with ≈ marking the approximation (B10). |
| A8 | Action-value methods "have no natural way of finding stochastic optimal policies", whereas policy-gradient methods can | SUPPORTED | p. 323 (Sec. 13.1), which points to Example 13.1 as the demonstration |
| A9 | In imperfect-information card games, optimal play often mixes two actions with specific probabilities, e.g. bluffing in poker | SUPPORTED | p. 323 (Sec. 13.1). The book's wording is "two different things", **not** "two very different things", which is a misquote that circulates online |
| A10 | Chapter 13 is a turn in the book: until then, almost all methods were action-value methods | SUPPORTED | p. 321, chapter opening: "In this chapter we consider something new." The book names one exception, gradient bandits (Sec. 2.8), so say **"almost all"**, never "all" |
| A11 | Book layout: Part I tabular methods (Ch. 2–8), Part II approximate methods (Ch. 9–13, ending with Ch. 13), Part III "Looking Deeper" (Ch. 14–17: psychology, neuroscience, applications, frontiers) | SUPPORTED | Contents, pp. vii–xii; Part III opener p. 339 |
| A12 | The book itself runs REINFORCE on the corridor (Figure 13.1) and shows it approaching the optimal start-state value | SUPPORTED | p. 328: step sizes 2⁻¹², 2⁻¹³, 2⁻¹⁴; 1,000 episodes; averaged over 100 runs. The **starting policy isn't stated**, so the film must not claim the book started at "mostly left" |
| A13 | Always-right / always-left never reach the goal | SUPPORTED (derived) | From A2's rules: always-left never leaves state 1; always-right bounces between states 1 and 2. Also `exact_value` → −∞ |
| A14 | A fair coin scores **−12** | OURS (exact) | `results.json` `exact.fair_coin_p0.5` = −12.00. Not in the book's text. Label as our calculation |
| A15 | "A fair coin beats the ε-greedy learner by almost four times" | QUALIFY | 44.21 / 12.00 = **3.68×**. Say "more than three and a half times", or show the two numbers |
| A16 | Sarsa (ε = 0.1, α = 0.01, 1,000 episodes) settled on "mostly right" in **30 / 30** runs | OURS | `results.json` `sarsa`. Our learner, our hyperparameters. Not a claim about every action-value method or every setting |
| A17 | REINFORCE started at P(right) = 0.05 (value −82.11) climbs to mean P(right) **0.586** (range 0.530–0.652), value −11.70 (worst −11.88), in 2,000 episodes | OURS | `results.json` `reinforce_from_mostly_left`. Mean return per 100-episode block: −39, −17, −14, −13, −13, −12… The 30-run **mean** matches 2 − √2; individual runs scatter ±0.07, so don't imply each run lands on 0.586 |
| A18 | The same Sarsa learner, given **one value pair per state**, learns right-left-right: 3 steps, value −3 | OURS | `results.json` `sarsa_sees_state`: 30 / 30 seeds. −3 vs −11.66 is **3.89×**. Say "nearly four times" |
| A19 | The coin helps **because** the learner can't see which square it's on | SUPPORTED + OURS | The book ties the difficulty to identical features (p. 323). A18 shows the advantage disappears when the learner can see the state |

### A20–A25: added for draft 2 (the 12/12 pass), checked 2026-10-01 against a fresh copy of the PDF, deleted after

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| A20 | "Any rule you could pick is really a coin": with the same reading in every square and no memory, every rule is one probability of pressing right | SUPPORTED (derived) | Follows from A3 (same features in every state) plus no memory (A22). It holds **only** with no step-counting, which is why B01 now says so. A blindfolded player who counts could open-loop right-left-right |
| A21 | When the player knows exactly where it is, there's always a fixed (deterministic) rule that's optimal | SUPPORTED | Sec. 17.3, p. 465: with a Markov state there is always a deterministic optimal policy. Also p. 68 (Sec. 3.6): any policy greedy with respect to the optimal value functions is optimal. Say "fixed rule", not "proof" |
| A22 | The corridor's blindfold is partial observability: features that ignore part of the state act as if that part were unobservable, and function approximation alone can't add memory of past observations | SUPPORTED | Ch. 9 opening, p. 197 |
| A23 | Rock-paper-scissors vs. an opponent that plays to beat your most frequent move so far, 30 seeds × 1,000 rounds: always rock **−0.999** per round [−1.000, −0.998]; lean rock 50/30/20 **−0.287** [−0.326, −0.247]; even thirds **+0.008** [−0.035, +0.050] | OURS | `experiment/rps.py` → `rps_results.json`. "Lost essentially every round" fits −0.999. "Broke even" fits ≈ 0. Our opponent design (fictitious play), not a general claim about all opponents |
| A24 | Against an opponent that just plays at random, always rock does as well as anything (≈ 0) | OURS + math | `rps_results.json` `vs_random_opponent_mean`: −0.002 / +0.000 / −0.001. Against a uniformly random opponent every strategy's expected payoff is exactly 0 |
| A25 | The book describes reinforcement learning as learning by trial and error | SUPPORTED | Ch. 1, p. 1: trial-and-error search and delayed reward are its two most important distinguishing features |

**Not claimed, kept as a boundary.** The film's test says "if randomness survives, *look for* someone
who'd exploit a pattern". It's a heuristic, not a theorem. Randomness can survive full information for
other reasons (e.g. constrained problems), so the narration never says "it must be an opponent". The
goalkeeper (B17) is posed as a question only. The film makes no factual claim about real penalty kicks.

## B. Claims in the GitHub source that the film does **not** use (checked anyway)

The review's `SOURCES.md` lists three statistics. Recorded here so the source itself is audited:

| # | Source claim | Verdict | Evidence |
|---|---|---|---|
| B1 | Short corridor: ε-greedy settles for −44 or −82, policy gradient finds 59% right | QUALIFY | Matches A5/A6. The book says "less than −44 and −82" |
| B2 | "Online learning adapted to workload changes, improving performance 19% over best conventional controller and closing 27% of gap to theoretical optimum" | QUALIFY | p. 435 (Sec. 16.4, İpek et al.'s DRAM controller): RL improved over FR-FCFS by 7–33%, **average 19%**, and closed **27%** of the gap to the *Optimistic* upper bound. That bound "ignores all timing and resource constraints", so it is not a "theoretical optimum" a real controller could reach. The 19% is the controller's overall result, not specifically the effect of online adaptation |
| B3 | AlphaGo: 30 million expert moves, policy-gradient RL, value networks and MCTS beat Lee Sedol 4–1 | SUPPORTED | p. 444 "nearly 30 million human expert moves" (SL policy network); p. 442 "winning 4 out of 5 games"; p. 449 "by 4 games to 1" |

The source's beat-sheet fragments ("risk-adjusted betting", "two-ply selective search") correspond to
Sec. 16.3 *Watson's Daily-Double Wagering* and Sec. 16.1 *TD-Gammon*. The film doesn't use them, so
they aren't audited further.

## C. Rights

- The book PDF is licensed **CC BY-NC-ND 2.0** (copyright page). The film is for YouTube, so its
  figures (the Example 13.1 inset graph, Figure 13.1) are **not** reproduced or adapted. Every chart and
  corridor drawing in the film is drawn by us from our own `results.json`.
- Short attributed quotations are fine (e.g. "In this chapter we consider something new"). The
  title and the authors are named on screen.

## D. Wording rules for the beat sheet

1. "About −44 and −82", or our −44.21 / −82.11 labelled as ours. Never present our decimals as the book's.
2. 2 − √2 is "what it works out to" (Exercise 13.1), not something the book prints.
3. "Almost all" of the book before Chapter 13 is action-value learning, never "all".
4. Our runs: "in our 30 runs", "with our settings". No general claims about action-value methods.
5. Ratios: 3.68× ("more than three and a half times") and 3.89× ("nearly four times").
6. Narration avoids "indistinguishable" / "can't tell them apart" (ANGLE.md uniqueness boundary).
   Paraphrase the book's point as "every square gives the learner the same reading".

## E. Open items

- `[VERIFY at Gate P]` Kokoro phonemes: "two minus root two", "Sarsa", "REINFORCE", "epsilon",
  "Sutton", "Barto", years in words ("twenty eighteen").
- None of the film's claims are UNSUPPORTED.
