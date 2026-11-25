# SOURCES — Gradient Descent, One Step at a Time

There is no single source article. This is a concept film written from standard references, and every number shown is executed locally.

## References
- A.-L. Cauchy (1847), *Méthode générale pour la résolution des systèmes d'équations simultanées*: the original steepest-descent method.
- I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning* (MIT Press, 2016), §4.3 "Gradient-Based Optimization" and §8.1.3 "Batch and Minibatch Algorithms".
- D. Rumelhart, G. Hinton, R. Williams (1986), "Learning representations by back-propagating errors", *Nature* 323.

## Executable evidence
- `demo/gd_demo.py` (pure Python + numpy, seed 7) writes `demo/evidence.json` and `demo/RUN-LOG.txt`.
- Run environment: Python 3.12.13, numpy 2.5.5, Windows 11.
- `make_sheet.py` reads every on-screen number from `evidence.json`.

## Corrections applied (DOUBLE-CHECK LAW)
- B01: "millions of times" became "step after step", because the step count was overstated.
- B07: "this same rule" became "a version of this same rule", because most models use momentum or Adam variants.

## Seeds
- Hesitant writer: `claude-liam-gradient-descent-b01`.
- Line-fit data and batches: numpy `default_rng(7)`.
- Outro mascot and polarity: seeded by slug `claude-liam-gradient-descent`.
