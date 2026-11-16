# FACTCHECK — RLHF: How Chatbots Learned to Help

Status: claims checked by Claude Code against SOURCES.md and the evidence run. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | A raw model asked how to bake bread may reply with more questions | PASS (illustrative) | InstructGPT paper's moon-landing example | "illustrative" caption on screen |
| 2 | B03 | Pretraining reads huge amounts of text (GPT-3: 300B tokens) and can continue any of it, but has no notion of a good answer | PASS | Brown et al. 2020 | — |
| 3 | B04 | Step one: people write example answers; the model is trained to imitate them (~13,000 prompts) | PASS | InstructGPT §3 | "about" on screen |
| 4 | B05 | Step two: several answers ranked; a reward model learns preferences; 4 answers → 6 comparisons; toy RM 77.7 % | PASS | InstructGPT (K = 4–9); rlhf_toy.out.txt | "toy" caption |
| 5 | B06 | Step three: RL toward higher scores with a drift penalty (KL); toy mean +0.05 → +2.34 at KL 1.18 | PASS | InstructGPT PPO + KL; rlhf_toy.out.txt | "toy" caption |
| 6 | B07 | InstructGPT 2022: people preferred 1.3B RLHF outputs over 175B GPT-3; more than 100× smaller | PASS | Ouyang et al. 2022 abstract; 175/1.3 = 134.6 | brief's "more than 100×" kept on screen |
| 7 | B08 | It learns to please the reward model, not to be right: sycophancy, reward hacking; toy curve | PASS (soft) | Sharma et al. 2023; Gao et al. 2022; rlhf_toy.out.txt | toy caption |
| 8 | B09 | DPO and AI feedback (Constitutional AI) make it cheaper; preferences still train every major chatbot | PASS (soft) | Rafailov et al. 2023; Bai et al. 2022 | "in 2026" dropped from voice |
| 9 | B10 | Viewer prompt: "Where might you be telling me what I want to hear?" | EXEMPT | Handoff prompt, not a factual claim | — |
