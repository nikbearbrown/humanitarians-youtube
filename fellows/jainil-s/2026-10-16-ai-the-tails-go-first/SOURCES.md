# SOURCES — The Tails Go First

## Primary evidence (ships in this folder)

**`collapse_evidence.py`** — pure numpy, no scikit-learn, no download, runs in
seconds. **Every number and both density curves in the reel are printed by this
file.** 60 seeds, n = 200 samples per generation, 120 generations, medians over
seeds.

What it does: recursive generative training. Generation 0 draws real samples
from a mixture — a common bulk at N(0,1) plus a rare subpopulation worth 5% at
N(6, 0.6). Every later generation is a fixed-bandwidth kernel density model
fitted to the previous generation's output. Real data is never seen again.

Each point carries a lineage label recording whether it descends from the rare
subpopulation. The label is never used by the model; it exists so the script can
state exactly when the rare subpopulation is gone instead of inferring it from a
threshold that bulk outliers can wander across. The script prints the lineage
share next to the observable "fraction beyond x = 4" so the two can be compared —
they track each other, which is what shows the finding is in the data and not in
the bookkeeping.

| Quantity | Value |
|---|---|
| True weight of the rare subpopulation | 5% |
| Observed at generation 0 | 4.5% |
| Generation 10 / 20 / 30 | 3.25% / 1.5% / 0% |
| Runs where it went extinct | **49 / 60** |
| Median generation of extinction | 20 (earliest 3, latest 108) |
| Runs where it returned after extinction | **0 of 49** |
| Still alive at generation 120 | 11 / 60 |
| Mean, generation 0 → 120 | +0.28 → +0.36 |
| Std dev, generation 0 → 120 | 1.60 → 1.67 |

## Published source

**Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R. & Gal, Y.
(2024).** *AI models collapse when trained on recursively generated data.*
Nature **631**, 755–759. Published 25 July 2024.
doi:[10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y) ·
open copy via the
[Edinburgh Research Explorer](https://www.research.ed.ac.uk/en/publications/792c0742-46bd-4d3d-b5d4-6a5bdfee2646)

- Quoted verbatim on B06, from the abstract:
  *"We find that indiscriminate use of model-generated content in training
  causes irreversible defects in the resulting models, in which tails of the
  original content distribution disappear."*
- Also from the paper, supporting the shape of our curve: *"At first, the tails
  (low-probability events) begin to disappear as a result of the low probability
  of sampling them and, over time, support of the distribution shrinks."*
- **Why this matters for our setup:** the paper demonstrates collapse in LLMs,
  variational autoencoders, **and Gaussian mixture models**. Our world is a
  Gaussian mixture, so this is a reproduction inside one of the paper's own
  families rather than an analogy to it.

## Deliberate omissions

1. **No numeric claim about LLMs.** "Generation 20", "49 of 60" and the 5%
   figure are properties of this experiment, with its sample size and its
   bandwidth. Generation counts do not transfer to a language model, and the
   reel never implies they do.
2. **This isolates one of the paper's mechanisms.** Shumailov et al. name
   statistical error from finite sampling, functional expressivity error, and
   functional approximation error. Our loop demonstrates the first cleanly. The
   other two are real and are not shown here.
3. **No claim that synthetic data is useless.** The finding is about
   *indiscriminate recursive* training with no real data re-entering the loop.
   Mixing in real data is exactly the mitigation the paper points at, and the
   handoff prompt asks the viewer about that rather than about avoiding
   synthetic data.
4. **The bulk is not claimed to be identical.** Its histogram peak is lower at
   generation 40 because the smoothing spreads it slightly. The reel's claim is
   about the mean and standard deviation, which are the two numbers shown, and
   those did stay in place.
