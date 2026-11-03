# FACTCHECK — It Was Still Learning

Every claim with its verdict. Rows citing the script are reproducible by running
`grokking_evidence.py`, which ships here and prints all of them.

| # | Beat | Claim as made | Verdict | Source |
|---|---|---|---|---|
| 1 | B02 | Task is (a+b) mod 23; 529 pairs; 317 train / 212 held out; no overlap | **VERIFIED** | Construction. `int(0.6 × 529) = 317`, remainder 212, split by a single permutation so no pair is on both sides |
| 2 | B02 | Chance is 4.3% | **VERIFIED** | 1/23 = 4.35% |
| 3 | B02 | One hidden layer, 96 units, squared activation, full-batch Adam, weight decay 0.8 | **VERIFIED** | Script constants |
| 4 | B03 | Training accuracy reaches 100% at step 500 and never moves again | **VERIFIED** | Script, all 8 seeds. 97.3% at step 250, 100% from 500 onward |
| 5 | B03 | Held-out accuracy at step 500 is 0.5% | **VERIFIED** | Script, median over seeds |
| 6 | B03 | "Worse than guessing" | **VERIFIED** | 0.5% against a 4.3% chance rate. The memorising solution is actively anti-correlated on held-out pairs, not merely uninformative |
| 7 | B03 | It stays low for another ~1,500 steps | **VERIFIED** | 3.3% at step 1,000; 26.2% at step 2,000. The lift-off is between those two |
| 8 | B03 | Held-out passes 95% by step 6,000 | **VERIFIED** | 95.5% at step 6,000; median crossing at step 6,125 |
| 9 | B03 | "Twelve times later" | **VERIFIED** | 6,125 / 500 = 12.25 |
| 10 | B04 | Weight decay 0.0 / 0.3 / 0.5 / 0.8 gives 0.9% / 10.4% / 86.3% / 99.5% held-out | **VERIFIED** | Script ablation, 3 seeds, 10,000 steps, median. Only the decay differs |
| 11 | B04 | With no decay the network memorises and stays there | **VERIFIED** | Train 100%, held-out 0.9%, 0/3 seeds ever exceeded 95% |
| 12 | B04 | The pressure to shrink weights is what makes a smaller solution win | **VERIFIED (as stated)** | Follows from row 10. Stated as *smaller-weight*, which is what decoupled weight decay directly penalises — NOT as a claim about which algorithm is learned |
| 13 | B05 | Power et al., OpenAI, 2022, named it grokking | **VERIFIED** | arXiv:2201.02177, submitted 6 Jan 2022 |
| 14 | B05 | Both quoted fragments | **VERIFIED VERBATIM** | Read from the arXiv abstract. Shown as two separate ellipsis-led lines because they are not contiguous |
| 15 | README | 8 of 8 seeds generalise; final held-out 99.8% | **VERIFIED** | Script, 8 seeds, 20,000 steps. Not spoken on screen; cited in `README.md` |
| 16 | README | Crossing step ranges 4,750–7,750 across seeds | **VERIFIED** | Script. Not spoken on screen; cited in `README.md`. A draft of the README carried an invented range (5,250–7,000) and was corrected against a re-run before release |

## Claims considered and cut

| Claim | Why it was cut |
|---|---|
| Which algorithm the network learned (e.g. a Fourier/trig construction) | Would require mechanistic analysis not done here. Known from other work, but not *our* evidence |
| Any step count or timing for a large model | Ours describe a 96-unit network on 317 examples |
| "Grokking happens all the time in real training" | Not supported. It is demonstrated on a small algorithmic task, which is the paper's own setting |
| "Never use early stopping" | Overcorrection. The reel's point is to check whether the rule *could* have fired early, which is what the handoff prompt asks |

## Changed during the build

**The first three experiments did not grok, and the claim was not softened to
fit them.**

1. **ReLU, P=31, 12k steps.** Train hit 99% at step 500 but held-out never
   exceeded 90%; at weight decay 1.0 it reached 0.239 and was still climbing.
   Inconclusive, and too slow to iterate on at 88–260 seconds a run.
2. **ReLU, P=23, 200k steps.** Held-out plateaued at **0.53–0.60** and stayed
   there for 170,000 further steps. This is delayed *partial* generalisation —
   real, and genuinely interesting, but it is not grokking. Writing the reel
   around it would have meant describing a 60% plateau as "perfect
   generalisation".
3. **Squared activation.** Modular addition has Fourier structure that a
   quadratic unit can express directly. P=31 groks at step 18,000 but takes ~5
   minutes a run; P=23 with decay 0.8 groks at step 6,000 in about 8 seconds,
   which is what ships.

Only after 8/8 seeds reproduced it was any narration written.

**The weight-decay claim was an assertion before it was a measurement.** The
script's docstring said decay was essential before anything had tested it. The
ablation was then run specifically to check, and it held — but it was written
as a claim first, which is the wrong order and is recorded here for that reason.
