# FACTCHECK — The Tails Go First

Every claim with its verdict and source. Rows citing the script are reproducible
by running `collapse_evidence.py`, which ships here and prints all of them.

| # | Beat | Claim as made | Verdict | Source |
|---|---|---|---|---|
| 1 | B02 | The world is a common bulk plus a rare subpopulation worth 5% | **VERIFIED** | Construction of the experiment; `RARE_W = 0.05` |
| 2 | B02 | Generation 0 draws 200 samples and 4.5% land in the rare part | **VERIFIED** | Script, median over 60 seeds. 4.5% not 5% because 200 samples is a finite draw |
| 3 | B03 | After the first step no real data enters again | **VERIFIED** | Construction; each generation resamples only from the previous generation's output |
| 4 | B03 | Nothing adversarial, nothing badly implemented | **VERIFIED** | Construction. The loop is a faithful fit-and-sample each round; the loss comes from finite sampling alone |
| 5 | B04 | Share falls 4.5% → 3.25% at gen 10 → 1.5% at gen 20 → 0% by gen 30 | **VERIFIED** | Script, median over 60 seeds, printed at every fifth generation |
| 6 | B04 | Extinct in 49 of 60 runs | **VERIFIED** | Script |
| 7 | B04 | It never came back in any of those 49 | **VERIFIED** | Script measures this explicitly. It is also structurally true: nothing in the loop can reintroduce a region once no sample occupies it |
| 8 | B05 | At generation 40 the far bump is gone | **VERIFIED** | The on-screen curve is the measured histogram at generation 40, pooled across seeds. Bins beyond x = 4 are all zero |
| 9 | B05 | Mean moved +0.28 → +0.36; std dev 1.60 → 1.67 | **VERIFIED** | Script, generation 0 vs generation 120 |
| 10 | B05 | Summary statistics do not reveal the loss | **VERIFIED (as stated)** | Follows from row 9: both numbers stay in place while 5% of the distribution is permanently absent. Stated about *these* statistics, not about every possible diagnostic |
| 11 | B06 | Shumailov et al. quotation on the card | **VERIFIED VERBATIM** | Nature 631:755–759 (2024), abstract. Extracted from the publisher PDF, not retyped |
| 12 | B06 | Published in Nature, 2024 | **VERIFIED** | Vol 631, pp 755–759, 25 July 2024 |
| 13 | B06 | They tested LLMs, VAEs and Gaussian mixture models | **VERIFIED** | Abstract, verbatim list |
| 14 | B06 | "that last family is the one I just ran" | **VERIFIED** | Our world is a two-component Gaussian mixture |

## Claims considered and cut

| Claim | Why it was cut |
|---|---|
| Any generation count for a language model | Our numbers describe a 200-sample mixture. Transferring them would be inventing a result |
| "Synthetic data is bad" | Not what the paper says and not what the script shows. The finding is about *indiscriminate recursive* training with no real data re-entering |
| "The variance collapses to a point" | The paper describes this as *late* collapse. Our 120-generation run does not reach it — std dev ends at 1.67, slightly **up**. Saying otherwise would be borrowing the paper's result and presenting it as ours |
| "The bulk is unchanged" | Its histogram is slightly flatter by generation 40. The reel claims only what the two displayed statistics show |

## Changed during the build

**The first experiment showed the opposite of model collapse.** With a
Silverman-rule bandwidth the kernel width scales with the current spread, so
each generation *added* variance: standard deviation ran 1.6 → 1563 over 120
generations and the rare share rose to about 50%. That is variance inflation,
not collapse. The model was wrong, not the idea. Fixed by using a fixed
bandwidth so resampling drift dominates.

**The second attempt used a bad metric.** Counting samples beyond x = 3 as "the
rare subpopulation" let ordinary bulk outliers drift across the threshold, so
the subpopulation appeared to come *back* from extinction in 30 of 41 runs —
which is impossible by construction. Replaced with an explicit lineage label
carried through resampling. Recoveries went to 0, as they must.

**An invented curve was caught before rendering.** B04's series was first
written as a hand-made interpolation between the measured points, and it was
also misaligned with the generations it claimed to show. Replaced with the
measured per-generation medians, and the script now prints that exact series so
the beat sheet can be checked against it.

**A fabricated density curve was caught before rendering.** The first version of
the curve exporter generated a fresh N(0,1) sample for the "after" shape instead
of running the loop and measuring it. That would have put an invented figure on
screen in a video about measurement. Replaced with a function that runs the real
loop to the named generation and histograms what is actually there.
