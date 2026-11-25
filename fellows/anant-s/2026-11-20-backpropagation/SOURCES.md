# SOURCES — Backpropagation, One Error at a Time

This is a concept film written from standard references. Every number on screen comes from local execution.

## References
- **Rumelhart, Hinton & Williams (1986).** "Learning representations by back-propagating errors", *Nature* 323.
- **Goodfellow, Bengio & Courville, *Deep Learning*** (MIT Press, 2016). §6.5 covers back-propagation; §8.2 covers ill-conditioning and vanishing gradients.
- **Hochreiter (1991)**, diploma thesis, and **Bengio, Simard & Frasconi (1994)**, "Learning long-term dependencies with gradient descent is difficult". Both cover vanishing gradients.
- **Glorot, Bordes & Bengio (2011).** "Deep Sparse Rectifier Neural Networks".

## Executable evidence
- **Script:** `demo/bp_demo.py`, pure Python + numpy and deterministic. It writes `demo/evidence.json` and `demo/RUN-LOG.txt`.
- **Environment:** Python 3.12.13, numpy 2.5.5, Windows 11.
- **Data flow:** `make_sheet.py` reads every on-screen number from `evidence.json`.

## Seeds
- **Hesitant writer:** `claude-liam-backpropagation-b01`.
- **Outro:** the mascot and polarity are seeded by the slug.

## Series
Film 2 in the series. Film 1, "Gradient Descent, One Step at a Time", named backpropagation in its scale beat; this film explains it.
