# Explainer — Prefill vs Decode

**Week:** 14–18 Sep 2026
**Type:** STEM / AI explainer

- **Video:** (https://www.youtube.com/watch?v=G-BSNylji68&t=4s)
- **Drive:** https://drive.google.com/drive/folders/1dNRtEobtVoOo96AsAAauUyMaR99WWjsT?usp=sharing
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

The two phases of LLM inference: prefill, where the whole prompt is processed in
parallel, and decode, where output tokens are produced one at a time.

## Why this topic, this week

The same week's project work was blocked by this distinction in the most direct
way possible. Every call to the strong tier was refused before the model ran,
because the account's cap is **1000 output tokens per minute**  a decode-side
limit  and the configured budget asked for 1024. Lowering the budget to 896
fixed it.

It also explains the pricing asymmetry this whole project routes around: output
tokens cost several times what input tokens cost, because decode is sequential
while prefill is not. That is why the router measures input length in characters
and sets a per-tier **output** budget, and why
[Sprint 2](../09032026mycroft-gateway/) found real cost
ratios of 1.4x and 19–26x where the rate card said 2x and 10x  the difference is
entirely how much each model chooses to say.

## Limits

- Source material is in the Drive folder.