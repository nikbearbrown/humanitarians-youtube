# SOURCES — Softmax and Temperature, Explained

There is no single source article. This is a concept film written from standard references. Every number shown is executed locally from constructed logits, which are labelled as constructed on screen.

## References
- J. S. Bridle (1990), "Probabilistic interpretation of feedforward classification network outputs, with relationships to statistical pattern recognition," in *Neurocomputing: Algorithms, Architectures and Applications* (Springer). This is the paper that coined the name "softmax".
- I. Goodfellow, Y. Bengio, A. Courville, *Deep Learning* (MIT Press, 2016), §6.2.2.3 "Softmax Units for Multinoulli Output Distributions".
- G. Hinton, O. Vinyals, J. Dean (2015), "Distilling the Knowledge in a Neural Network," arXiv:1503.02531. Eq. 1 is softmax with temperature T.
- A. Holtzman, J. Buys, L. Du, M. Forbes, Y. Choi (2020), "The Curious Case of Neural Text Degeneration," ICLR. Covers sampling versus maximization decoding and temperature. Background only; the film makes no claim from it.
- OpenAI API reference, Chat Completions `temperature` and `seed` entries, retrieved 2026-11-22 (developers.openai.com/api/reference/resources/chat). Quoted in FACTCHECK #21 and #25 only, and not named in the film.
- Anthropic Messages API reference, retrieved 2026-11-22 (platform.claude.com/docs/en/api/messages). The page as read showed no `temperature` body parameter, so the film makes no Claude-specific temperature claim.

## Executable evidence
- `demo/softmax_demo.py` (pure Python + numpy, seed 2) writes `demo/evidence.json` and `demo/RUN-LOG.txt`.
- Run environment: Python 3.12.13, numpy 2.5.5, Windows 11. A second run under Python 3.12.7 / numpy 2.3.5 gave identical numbers.
- `make_sheet.py` reads every on-screen number from `evidence.json` and asserts every spoken number against it.

## Corrections applied (DOUBLE-CHECK LAW)
- **"Real logits" became constructed logits, labelled as such.** The pure-numpy rule rules out running a real model. See open question 2 in BUILD-LOG.
- **B01:** "token" became "word" for the lay summary; "token" is introduced in B02.
- **B08:** "Same prompt, same answer" became "…at least in principle", because providers do not guarantee determinism.
- **B09:** "Canberra barely moves" became "Canberra actually slips" (33.3% → 30.5%).
- **No product or API temperature ranges in narration.** They date, and Anthropic's page shows no such parameter.
- **B07 sampling method changed after an outlier.** Logged openly in FACTCHECK #18 and BUILD-LOG.

## Seeds
- Demo: numpy `default_rng(2)`. The first 20 uniforms are the B06 rolls; the next 10,000 are the B07 rolls. Both sets are reused across T = 0.2, 1 and 2.
- Hesitant writer: `claude-liam-softmax-temperature-b01`.
- Outro mascot and polarity: seeded by slug `claude-liam-softmax-temperature`.
