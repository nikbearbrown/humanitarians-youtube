# PEDAGOGY — What Is RLHF? (hai cli-explainer, STEM/AI concept video)

A concept video on reinforcement learning from human feedback, the training stage that turns a pretrained text predictor into an assistant. It opens on the InstructGPT result (a 1.3B model preferred over the 175B GPT-3), walks the three real stages as OpenAI published them (supervised fine-tuning, reward model, reinforcement learning with PPO), notes that ChatGPT used the same methods, then covers how Anthropic's Constitutional AI and RLAIF replace some human labels with AI feedback, and what that does not remove.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the surprising fact: a model 100x smaller was preferred, because of how it was trained ✓
- B01 — stage 1: supervised fine-tuning on labeler-written demonstrations ✓
- B02 — stage 2: labelers rank answers; a reward model learns to predict the preferred one as a single score ✓
- B03 — stage 3: reinforcement learning with PPO, the drift penalty, and ChatGPT using the same methods ✓
- B04 — Constitutional AI: no human data on harmlessness; self-critique and revision against written principles ✓
- B04B — RLAIF: an AI judge in place of the human ranker; comparable results; the limits ✓
- B05 — HANDOFF, a concrete exercise: write one preference label yourself ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| People preferred outputs of a 1.3B-parameter InstructGPT model over the 175B GPT-3, despite 100x fewer parameters | Ouyang et al. 2022, "Training language models to follow instructions with human feedback", arXiv 2203.02155 (abstract) | OK — quoted from the abstract |
| RLHF has three stages: labeler demonstrations for supervised fine-tuning, rankings for a reward model, then RL | Ouyang et al. 2022 (abstract) | OK — directly stated |
| Stage 3 uses PPO, with a penalty against drifting from the supervised model | Ouyang et al. 2022 (paper body: PPO with a per-token KL penalty from the SFT model) | OK — from the paper body, not the abstract; consistent with the method as published |
| Ranking answers is faster than writing them | Inferred from the method's design (rankings collected over many model outputs per prompt) | OK — framed as a practical point, not a measured claim |
| ChatGPT was trained with the same methods as InstructGPT, with PPO, fine-tuned from a GPT-3.5-series model | OpenAI, "Introducing ChatGPT", Nov 30, 2022 | OK — page returned 403 to automated fetch; content corroborated by Wikipedia's ChatGPT article (SFT with human trainers, reward model from rankings, PPO) |
| Constitutional AI: self-critique and revision against principles, then an AI model judges which answer is better (RLAIF) | Bai et al. 2022, "Constitutional AI: Harmlessness from AI Feedback", arXiv 2212.08073 (abstract) | OK — directly stated |
| Claude is trained with Constitutional AI; "the model received no human data on harmlessness" | Anthropic, "Claude's Constitution", May 9, 2023 | OK — quoted from the post |
| RLAIF performed comparably to RLHF; human preference labels are expensive | Lee et al. 2023, "RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback", arXiv 2309.00267 (abstract) | OK — quoted from the abstract |
| Humans still write the principles; the feedback is only as good as the judging model | Bai et al. 2022 ("the only human oversight is provided through a list of rules or principles"); reasoning about AI feedback | OK — the first half is sourced; the second is framed as a limitation, not a finding |

## Friction protected

- Kept: the brief's "the difference between GPT-3 and ChatGPT wasn't parameters or data" was not used as stated. RLHF is itself new data (demonstrations and rankings), and ChatGPT started from a newer GPT-3.5-series model. The video says the smaller model "wasn't bigger or better read" and rests the claim on the InstructGPT comparison.
- Kept: Constitutional AI is described as removing human data on *harmlessness*, matching Anthropic's wording. The video does not claim Claude is trained with no human feedback at all.
- Kept: RLAIF is "comparable", not "better", matching the study's wording.
- Kept: B04B ends on the limits: humans still write the principles, and AI feedback is only as good as the model giving it.
- Kept: the B02 answer letters and ranking are illustrative; no scene shows an invented score or metric.

VERDICT: PASS
