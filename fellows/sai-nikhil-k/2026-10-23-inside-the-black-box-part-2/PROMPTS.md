# PROMPTS — Inside the Black Box, Part 2

**No open generation slots.** Six Remotion compositions and two plates of
Stephen Wolfram's published figures. No image model, no paid API.

## B00 — the on-screen typed ask

> Part two. A neural net is simple parts with learned weights. Now open a trained one: what do its layers and weights actually show, and what can we read from them?

## B06 — the handoff the viewer can paste

> I loaded GPT-2 on my laptop, counted its weights and plotted one 768×768 weight matrix. Help me think it through: what does that picture actually tell me about what the model knows, and what can't it tell me?

## The evidence command (B02, B03)

```bash
python3 weekly_updates/2026-10-23-inside-the-black-box-part-2/evidence/gpt2_inspect.py \
  > weekly_updates/2026-10-23-inside-the-black-box-part-2/evidence/gpt2_inspect.out
```
