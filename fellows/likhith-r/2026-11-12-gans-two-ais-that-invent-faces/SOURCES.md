# SOURCES — GANs: Two AIs That Invent Faces

## Primary sources
- S1 — Goodfellow et al., "Generative Adversarial Nets", 2014. https://arxiv.org/abs/1406.2661
- S2 — Karras, Laine, Aila, "A Style-Based Generator Architecture for Generative Adversarial Networks", CVPR 2019. https://arxiv.org/abs/1812.04948 · https://openaccess.thecvf.com/content_CVPR_2019/html/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.html
- S3 — StyleGAN / This Person Does Not Exist (Feb 2019, Phillip Wang). https://en.wikipedia.org/wiki/StyleGAN · https://techxplore.com/news/2019-02-highly-realistic-fake-images.html
- S4 — Hong Kong deepfake video-call fraud, Feb 2024 (CNN reporting, summarised in the AI Incident Database). https://incidentdatabase.ai/reports/3629
- S5 — Arup named as the victim (May 2024). https://abc17news.com/?p=1323402 · https://businessinsider.nl/an-engineering-giant-behind-apples-hq-and-the-sydney-opera-house-lost-25-million-when-scammers-tricked-an-employee-with-a-deepfake-of-a-senior-exec/
- S6 — C2PA (Coalition for Content Provenance and Authenticity) / Content Credentials. https://c2pa.org

## Executable evidence (every on-screen number that isn't a citation) (every number shown on screen that isn't a citation)

`evidence/gan_toy.py` (numpy 2.5.3, seed 2026): a tiny 1-D GAN learns N(4, 1.25²). G is 1 → 16 → 16 → 1 (tanh), D is 1 → 32 → 32 → 1 (leaky ReLU). Adam, hand-written backprop, 6,000 forger steps, 5 detective steps per forger step (the *k* in S1's Algorithm 1). The detective's accuracy is logged at every step on a fixed held-out set of 4,000 real + 4,000 fake samples.

- detective accuracy: 99.9 % at step 19 → 50.6 % mean over the last 500 steps (`gan_toy.out.txt`)
- forger output: mean 0.00 / sd 0.15 at step 0 → mean 4.00 / sd 1.25 at step 6,000 (target 4.0 / 1.25)

A first configuration (one detective step per forger step, equal learning rates) was run and **rejected** before any scene was built. The detective never got good: its accuracy started at 25 % and swung between "everything real" and "everything fake", so a "50 %" read-out would have been meaningless. Logs are kept as `evidence/run1_rejected.*`. The second configuration was run once; nothing was tuned against its result.

## Not from a source

- The faces on screen (B02, B06, B07) are seeded ink drawings, labelled "drawn stand-in" on screen. They are not GAN output.
