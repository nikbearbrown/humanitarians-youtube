# SOURCES — Why Neural Networks Need a Bend

There is no single source article. This is a concept film written from standard references, and every number shown is executed locally.

## References
- I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning* (MIT Press, 2016), §6.1 "Example: Learning XOR". This is the source of the hand-set weights in B07 and of the "folded hidden space" picture that B08 rebuilds from our own executed numbers.
- M. Minsky, S. Papert, *Perceptrons* (MIT Press, 1969). It is the classic statement that a single linear threshold unit cannot compute XOR.
- V. Nair, G. Hinton (2010), "Rectified Linear Units Improve Restricted Boltzmann Machines", ICML. X. Glorot, A. Bordes, Y. Bengio (2011), "Deep Sparse Rectifier Neural Networks", AISTATS. These cover ReLU as an activation.
- A. Saxe, J. McClelland, S. Ganguli (2014), "Exact solutions to the nonlinear dynamics of learning in deep linear neural networks", ICLR. Deep linear networks have the same function class but different training dynamics; this backs the FACTCHECK #2 correction.
- G. Montúfar, R. Pascanu, K. Cho, Y. Bengio (2014), "On the Number of Linear Regions of Deep Neural Networks", NeurIPS. R. Arora, A. Basu, P. Mianjy, A. Mukherjee (2018), "Understanding Deep Neural Networks with Rectified Linear Units", ICLR. Both show that ReLU networks are piecewise linear; they back the B10 claim and the FACTCHECK #28 correction.

## Executable evidence
- `demo/nonlinearity_demo.py` is pure Python + numpy. It writes `demo/evidence.json` and `demo/RUN-LOG.txt`.
- Run environment: Python 3.12.13, numpy 2.5.5, Windows 11. The run takes about 60 s, mostly the 300 training runs.
- `make_sheet.py` reads every on-screen number from `evidence.json`.
- Assertions in the script:
  - the collapse is identical (B03);
  - ten-layer and bias gaps are below 10⁻¹²;
  - the best line gets exactly 3 of 4;
  - no deep-linear seed reaches 4 of 4;
  - the hand-set ReLU net outputs exactly (0, 1, 1, 0);
  - the diagonal trace matches its closed form.

## Corrections applied (DOUBLE-CHECK LAW)
- B01: "Stacking alone does nothing" became "Stacking alone isn't enough". Depth changes training dynamics, though not the function class.
- B02: "Two moves build every network" became "…a plain neural network", because other architectures add other operations.
- B09: "Eighteen find XOR" became "Here, eighteen find XOR". The success rate belongs to one stated training setup, not to ReLU networks in general.
- B10 and BVDT: "a ReLU network is straight lines" became "is made of straight pieces". The pieces are planes in 2-D.
- B00: the result line now reads "trained from 100 seeds, it finds it 18 times".

## Seeds
- Collapse matrices: numpy `default_rng(0)`. This was the first seed; seeds 0–11 were previewed and seed 0 was kept.
- 1,000-input and ten-layer check: `default_rng(1)`.
- Training runs: `default_rng(s)` for s = 0…99, at two widths (2 and 8 hidden units), plus the deep-linear runs.
- Hesitant writer: `claude-liam-nonlinearity-b01`.
- Outro mascot and polarity: seeded by slug `claude-liam-nonlinearity`.
