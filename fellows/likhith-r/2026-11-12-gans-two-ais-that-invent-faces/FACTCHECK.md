# FACTCHECK — GANs: Two AIs That Invent Faces

Status: claims checked by Claude Code against the sources below and the evidence run. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix / note |
|---|---|---|---|---|---|
| 1 | B02 | "This person never existed. No camera took it. Two competing AIs made it." | PASS (illustrative) | GANs generate faces with no camera (S1, S2) | The face on screen is a **drawn stand-in**, labelled "drawn stand-in for a GAN face". It is not GAN output. A real StyleGAN sample could be swapped into the slot later |
| 2 | B03 | In 2014, Ian Goodfellow and colleagues proposed GANs: a generator (forger) and a discriminator (detective) | PASS | S1: Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville, Bengio, "Generative Adversarial Nets", arXiv:1406.2661 (10 Jun 2014), NIPS 2014. The paper itself uses the counterfeiter vs. police analogy | forger / detective is the film's wording for that analogy |
| 3 | B04 | Forger makes fakes from noise; detective calls real or fake; a sharper detective makes a better forger | PASS | S1 (G maps noise z to samples; D estimates the probability a sample is real; alternating training) · our run, `evidence/gan_toy.py` | Histogram on screen = our run's forger samples at steps 0, 100, 300, 1,000, 3,000, 6,000 vs. the real N(4, 1.25²) |
| 4 | B05 | Done when the detective is right half the time: a coin flip | PASS | S1 (at the global optimum D(x) = ½ everywhere) · our run: detective accuracy 99.9 % at step 19, **50.6 %** mean over the last 500 of 6,000 steps (range 49.6 to 51.9 %) | Shown curve starts at step 1 (step 0 = untrained detective, 24.7 %, omitted) |
| 5 | B06 | Blurry 2014 faces became NVIDIA's StyleGAN in 2019 | PASS | S1 (2014 samples: small, low-res faces) · S2: Karras, Laine, Aila (NVIDIA), "A Style-Based Generator Architecture for GANs", arXiv:1812.04948 (Dec 2018), CVPR 2019; code released Feb 2019 | Faces on screen are drawn stand-ins (labelled) |
| 6 | B06 | A website showed a new fake face on every refresh | PASS | S3: thispersondoesnotexist.com, launched Feb 2019 by Phillip Wang on NVIDIA's StyleGAN code | — |
| 7 | B07 | That helped open the deepfake era: scam profiles, forged videos, non-consensual images | PASS (soft) | GAN-generated faces have been used in fake profiles; "deepfake" face-swap video and non-consensual imagery followed | On-screen footnote: "Newer deepfakes often use diffusion models. GANs opened the door." |
| 8 | B07 | In 2024, a Hong Kong employee sent about 25 million dollars after a call with deepfake colleagues | PASS | S4: Hong Kong police (Feb 2024, via CNN): finance worker paid HK$200 M (≈ US$25.6 M) after a video call with a deepfaked CFO and colleagues; 15 transfers to 5 accounts. S5: Arup confirmed it was the company (May 2024) | Screen: "≈ US$25 million · Hong Kong · early 2024 · HK$200 million" |
| 9 | B08 | Confirm through a channel you trust; content credentials; detectors miss fakes; consent | PASS (guidance) | S6: C2PA / Content Credentials standard. Detector false negatives are widely documented | Screen card 2 names the C2PA standard |
| 10 | B09 | When the detective can't tell anymore, the job falls to us | EXEMPT | Closing line (framing, not a factual claim); the 50.6 % shown is from our run | — |
| 11 | B10 | Viewer prompt: "How would I check a surprising video call is real?" | EXEMPT | Handoff prompt | — |

## Our run (every number shown on screen that isn't a citation)

`evidence/gan_toy.py` (numpy 2.5.3, seed 2026): a tiny 1-D GAN learns N(4, 1.25²). G is 1 → 16 → 16 → 1 (tanh), D is 1 → 32 → 32 → 1 (leaky ReLU). Adam, hand-written backprop, 6,000 forger steps, 5 detective steps per forger step (the *k* in S1's Algorithm 1). The detective's accuracy is logged at every step on a fixed held-out set of 4,000 real + 4,000 fake samples.

- detective accuracy: 99.9 % at step 19 → 50.6 % mean over the last 500 steps (`gan_toy.out.txt`)
- forger output: mean 0.00 / sd 0.15 at step 0 → mean 4.00 / sd 1.25 at step 6,000 (target 4.0 / 1.25)

A first configuration (one detective step per forger step, equal learning rates) was run and **rejected** before any scene was built. The detective never got good: its accuracy started at 25 % and swung between "everything real" and "everything fake", so a "50 %" read-out would have been meaningless. Logs are kept as `evidence/run1_rejected.*`. The second configuration was run once; nothing was tuned against its result.

## Sources

- S1 — Goodfellow et al., "Generative Adversarial Nets", 2014. https://arxiv.org/abs/1406.2661
- S2 — Karras, Laine, Aila, "A Style-Based Generator Architecture for Generative Adversarial Networks", CVPR 2019. https://arxiv.org/abs/1812.04948 · https://openaccess.thecvf.com/content_CVPR_2019/html/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.html
- S3 — StyleGAN / This Person Does Not Exist (Feb 2019, Phillip Wang). https://en.wikipedia.org/wiki/StyleGAN · https://techxplore.com/news/2019-02-highly-realistic-fake-images.html
- S4 — Hong Kong deepfake video-call fraud, Feb 2024 (CNN reporting, summarised in the AI Incident Database). https://incidentdatabase.ai/reports/3629
- S5 — Arup named as the victim (May 2024). https://abc17news.com/?p=1323402 · https://businessinsider.nl/an-engineering-giant-behind-apples-hq-and-the-sydney-opera-house-lost-25-million-when-scammers-tricked-an-employee-with-a-deepfake-of-a-senior-exec/
- S6 — C2PA (Coalition for Content Provenance and Authenticity) / Content Credentials. https://c2pa.org
