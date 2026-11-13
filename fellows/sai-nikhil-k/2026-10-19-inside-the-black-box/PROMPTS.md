# PROMPTS — Inside the Black Box, Part 1

**No open generation slots.** Seven Remotion compositions and two plates of
Stephen Wolfram's published figures. No image model, no paid API.

## B00 — the on-screen typed ask

> Stephen Wolfram wrote a long explainer on what ChatGPT is doing. Start with the neural net itself: what are its parts, where do their numbers come from, and can two trained nets disagree?

## B07 — the handoff the viewer can paste

> Write me a short Python script that trains two tiny neural nets on the same points from a step function on [−1, 1], with different random seeds, then plots both from −3 to 3. Where they disagree, which should I trust, and how would I find out?

## The evidence command (B05)

```bash
python3 weekly_updates/2026-10-19-inside-the-black-box/evidence/train_nets.py \
  > weekly_updates/2026-10-19-inside-the-black-box/evidence/train_nets.out
```
