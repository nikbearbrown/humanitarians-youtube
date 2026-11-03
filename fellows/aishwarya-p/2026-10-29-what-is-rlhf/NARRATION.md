# STEM Video: What Is RLHF? — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya from the Mycroft team.
This video is about RLHF, reinforcement learning from human feedback: the training stage that turned a text predictor into an assistant you can talk to.

## B00 — Cold open
In 2022, OpenAI researchers found that people preferred answers from a model with 1.3 billion parameters over answers from GPT-3, a model a hundred times larger. The smaller model wasn't bigger or better read. It had been trained on what people actually preferred.

## B01 — Stage one: supervised fine-tuning
Method: RLHF, as OpenAI described it in the InstructGPT paper, has three stages. Stage one is supervised fine-tuning. Human labelers write example answers to real prompts, showing what a good response looks like. The pretrained model is then fine-tuned on those examples, so it starts by imitating the people who wrote them.

## B02 — Stage two: the reward model
Stage two trains a reward model. The fine-tuned model writes several answers to the same prompt, and labelers rank them from best to worst. Ranking is much faster than writing. A separate model learns from those rankings to predict which answer a person would prefer, and turns that prediction into a single score.

## B03 — Stage three: reinforcement learning with PPO
Stage three is reinforcement learning. The model answers new prompts, the reward model scores each answer, and an algorithm called PPO, Proximal Policy Optimization, nudges the model toward higher-scoring answers. A penalty keeps it from drifting too far from the stage-one model. OpenAI says ChatGPT was trained with these same methods, starting from a model in its GPT-3.5 series.

## B04 — Constitutional AI
Human preference labels are slow and expensive. Anthropic's Constitutional AI, which is used to train Claude, takes a different route for harmlessness. The model received no human data on harmlessness. Instead, it gets a written list of principles, a constitution, and learns to critique and revise its own answers against them.

## B04B — RLAIF
In the reinforcement learning stage, an AI model, not a person, judges which of two answers is better. That's called RLAIF, reinforcement learning from AI feedback. A 2023 Google study found RLAIF performed comparably to RLHF. Humans still write the principles, though, and the feedback is only as good as the model giving it.

## B05 — Handoff
Your turn. Ask any chatbot the same question twice, then write down which answer you prefer and one sentence on why. That sentence is a preference label. Now imagine writing a hundred thousand of them, and you'll see why RLAIF exists.

## B06 — Outro
What Is RLHF? Built with Claude, for Humanitarians AI.
