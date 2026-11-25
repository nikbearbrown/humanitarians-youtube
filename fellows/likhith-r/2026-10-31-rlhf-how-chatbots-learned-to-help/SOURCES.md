# SOURCES — RLHF: How Chatbots Learned to Help

## Executable evidence (every on-screen number)
- `evidence/rlhf_toy.py` → `evidence/rlhf_toy.out.txt` + `evidence/rlhf_toy.json` (numpy 2.5.3, seed 2026). Toy, not a benchmark.
  Each answer = two numbers: substance c, flattery f. Simulated raters prefer u = c + 1.0·f and rank 4 answers with Gumbel noise (Plackett–Luce). The "SFT model" writes 6 % people-pleasing answers (c ≈ −2, f ≈ +3).
  - B05: 4 answers → C(4,2) = 6 comparisons (9 → 36). Linear Bradley–Terry reward model, 3,000 ranked sets → 18,000 pairs; held-out agreement 50 % (untrained) → 77.7 %; learned weights substance 0.99, flattery 1.02.
  - B06: KL-regularised RL, exact optimum π ∝ π_ref·exp(r/β) over 20,000 SFT answers, β = 1.0: mean reward +0.05 → +2.34, KL 1.18 nats; score histograms before/after.
  - B08: β sweep. Learned reward climbs monotonically (+0.05 → +6.19); true substance peaks at KL 1.18 (+0.41), then falls to −1.32; people-pleasing share 6.3 % → 99.9 %.
  - Paper constants echoed by the script: GPT-3 175B parameters, 300B training tokens; InstructGPT 1.3B; 175 / 1.3 = 134.6; InstructGPT prompt counts SFT ~13k, RM ~33k, PPO ~31k.

## Literature
- Ouyang et al., "Training language models to follow instructions with human feedback" (InstructGPT), OpenAI, NeurIPS 2022, arXiv:2203.02155. Abstract: "outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters." Three steps: SFT on labeler demonstrations (~13k prompts), reward model from rankings of K = 4–9 outputs (~33k prompts), PPO with a per-token KL penalty to the SFT model (~31k prompts). The paper's own example of raw GPT-3 answering an instruction with more instructions ("Explain the moon landing to a 6 year old" → more "Explain…" lines) is the basis for the B02 hook; the bread exchange on screen is illustrative and labelled so.
- Brown et al., "Language Models are Few-Shot Learners" (GPT-3), 2020, arXiv:2005.14165: 175B parameters, trained on 300B tokens.
- Christiano et al., "Deep reinforcement learning from human preferences", 2017, arXiv:1706.03741; Stiennon et al., "Learning to summarize from human feedback", 2020, arXiv:2009.01325 (RLHF lineage, Bradley–Terry reward model).
- Gao, Schulman, Hilton, "Scaling Laws for Reward Model Overoptimization", 2022, arXiv:2210.10760 (proxy reward rises while gold reward peaks then falls as KL grows — the shape the B08 toy reproduces).
- Sharma et al., "Towards Understanding Sycophancy in Language Models", Anthropic, 2023, arXiv:2310.13548 (RLHF assistants are sycophantic; human preference data partly rewards agreeing answers).
- Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model", NeurIPS 2023, arXiv:2305.18290 (trains on preference pairs directly; no separate reward model, no RL loop).
- Bai et al., "Constitutional AI: Harmlessness from AI Feedback", Anthropic, 2022, arXiv:2212.08073 (RLAIF: an AI, guided by a written constitution, produces the preference labels). Lee et al., "RLAIF", 2023, arXiv:2309.00267.
- Logos: icons/logos/openai/openai-01.svg (B07), icons/logos/anthropic/anthropic-01.svg (B09), copied into runtime/remotion/public/logos/.

## Corrections applied (DOUBLE-CHECK LAW)
1. Point 1 (hook): the bread exchange is not a recorded output; it is captioned "illustrative" on screen, and the documented example (InstructGPT's moon-landing prompt) is cited here.
2. Point 6: the paper says "100x fewer parameters"; 175 / 1.3 = 134.6, so the screen shows "175 ÷ 1.3 ≈ 135 · more than 100× smaller", and the narration says "a hundred times smaller" (the paper's own figure).
3. Point 7: sycophancy and reward hacking are presented as the documented failure modes (Sharma et al. 2023; Gao et al. 2022). The toy curve is a toy, captioned as such; it is not a measurement of any real model.
4. Point 8: "in 2026" dropped from the voice to keep the reel from dating; "every major chatbot" is kept as a soft claim (preference-based post-training — RLHF, DPO or RLAIF — is the published method for the major assistants). DPO and RLAIF are described as cheaper variants of the same idea, not replacements for preference learning.
