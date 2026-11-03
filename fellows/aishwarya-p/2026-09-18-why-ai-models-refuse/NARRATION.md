# STEM Video: Why AI Models Refuse — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video is about why AI models decline certain requests — and a real, surprising finding about how that decision actually gets made inside the model.

## B00 — Cold open
A chef carries a set of kitchen knives to a catering job. A bouncer checking for weapons turns him away. The knives are real. The danger isn't.

## B01 — How refusal actually gets trained in
Method: refusal is trained through a real, multi-step pipeline. A base model learns language from general text. Supervised fine-tuning shows it curated examples of refusing harmful requests. A reward model is trained on human ratings of what counts as unsafe. Reinforcement learning then updates the model's weights to score well against that reward model. By the time it ships, refusal is baked directly into the weights.

## B02 — The real, surprising finding
Real 2024 research found something nobody expected: refusal isn't a complex behavior scattered across a model's billions of parameters. It's mediated by a single direction in the model's internal activation space — a one-dimensional line. Erasing that one direction removes almost all refusal behavior. Injecting it artificially can make a model refuse even a completely harmless request.

## B03 — Why that leads to over-refusal
Because the real signal is a simple, linear direction rather than deep understanding, a model can key off surface features that merely resemble danger. Real research measuring this across thirty-two frontier systems found a strong correlation, point eight nine, between how safety-trained a model is and how often it refuses things that were never actually unsafe. The bouncer isn't reading intent. It's pattern-matching on weapon-shaped, and a chef's knife matches the pattern.

## B04 — The real tradeoff
This isn't a flaw someone forgot to fix. Real research describes the tradeoff as structural, not incidental — the same training that makes a model reliably refuse real threats is what makes it occasionally refuse harmless ones that merely look similar. Newer approaches are moving away from a strict refuse-or-comply boundary, toward responses that scale help to actual risk instead of a hard cutoff.

## B05 — Handoff
Your turn. Next time a model declines something harmless, don't just rephrase and resubmit — ask yourself what surface feature of your request might have pattern-matched to something risky, and see if naming that context directly changes the response.

## B06 — Outro
Why AI Models Refuse. Built with Claude, for Humanitarians AI.
