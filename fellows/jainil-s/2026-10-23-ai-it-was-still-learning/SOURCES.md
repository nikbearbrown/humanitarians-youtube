# SOURCES — It Was Still Learning

## Primary evidence (ships in this folder)

**`grokking_evidence.py`** — pure numpy, no framework, no download. About 70
seconds for the 8-seed main run plus roughly a minute for the ablation.
**Every figure spoken or shown in the reel is printed by this file.**

Setup: modular addition `(a + b) mod 23`. All 529 pairs; 317 train, 212 held
out, no overlap. One hidden layer, 96 units, **squared activation**, full-batch
Adam at `lr=1e-3` with decoupled weight decay `0.8`.

| Quantity | Value |
|---|---|
| Training accuracy reaches 100% | step **500**, in all 8 seeds |
| Held-out accuracy at that step | **0.5%** (chance is 4.3%) |
| Held-out accuracy reaches 95% | median step **6,125** (range 4,750–7,750) |
| Gap | **12× later** than memorisation |
| Seeds that generalised | **8 / 8** |
| Final held-out accuracy | **99.8%** |

Weight-decay ablation, 3 seeds, 10,000 steps, nothing else changed:

| Weight decay | Held-out accuracy |
|---|---|
| 0.0 | 0.9% |
| 0.3 | 10.4% |
| 0.5 | 86.3% |
| 0.8 | 99.5% |

## Published source

**Power, A., Burda, Y., Edwards, H., Babuschkin, I. & Misra, V. (2022).**
*Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets.*
[arXiv:2201.02177](https://arxiv.org/abs/2201.02177), submitted 6 January 2022.
Work done at OpenAI.

Quoted on B05, as two fragments from the abstract with ellipses:

> "… improving generalization performance from random chance level to perfect
> generalization…"

> "… this improvement in generalization can happen well past the point of
> overfitting."

Both fragments were read off the arXiv abstract page. They are not contiguous —
the card shows them as two separate quoted lines with leading ellipses rather
than stitched into one sentence, so nothing implies they ran together.

## Why squared activation

Modular addition has Fourier structure, and a quadratic unit can express it
directly. That is why this groks in seconds on a CPU instead of hours on a GPU.
It is a deliberate choice to make the phenomenon cheap to reproduce, and it is
stated on screen in the setup beat rather than buried.

## Deliberate omissions

1. **No claim about which algorithm the network learned.** Establishing that
   would need mechanistic analysis we have not done. The reel says only that
   weight decay selects a smaller-weight solution — which the ablation supports
   directly.
2. **No numeric claim about large models.** "Step 500" and "12× later" are
   properties of this experiment at this size. Step counts do not transfer.
3. **No claim that grokking is common in practice.** It is demonstrated here on
   a small algorithmic task, which is exactly the setting the paper studies.
   The reel's practical point is about *early-stopping rules*, not about
   expecting every run to grok.
4. **ReLU was tried first and is not in the reel.** With ReLU the same task gave
   delayed *partial* generalisation — held-out accuracy plateaued around 53–60%
   rather than reaching 95%. That is a real result but it is not grokking, so
   the configuration was changed rather than the claim softened. See
   `FACTCHECK.md`.
