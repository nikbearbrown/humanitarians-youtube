# SOURCE-brief — "How AI Image Generators Turn Noise Into a Picture"

## What was asked for

A STEM video on something audio, AI, or the intersection, planned carefully,
with strong visuals, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md) for the full exchange). Rohan picked image diffusion
from a list of fifteen after rejecting a topic that overlapped earlier videos.

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who
have typed a prompt into Midjourney — many of them trained on it by Rohan's own
six-part series — but have no idea what happens between the prompt and the four
pictures. No maths background assumed; the one equation is introduced as
"part picture, plus part noise" before it is shown.

## The one idea

**Every AI image starts as random static, and a model removes a little noise at
a time. The prompt steers every step; the seed sets the starting static.** From
that, one practical habit: lock the seed when you test a prompt change, because
then the only thing that changed is your words.

## Why this topic, of the fifteen offered

- It connects directly to work Lyrical Literacy already does (the Midjourney
  series), so the takeaway is usable the same day.
- It is **executable locally**: a diffusion model can be trained from scratch on a
  laptop CPU in half an hour, so every picture on screen is a real model's real
  output rather than an illustration — the EXECUTABLE-EVIDENCE rule.
- The one first-party source needed (Midjourney's Seeds documentation) says, in
  Midjourney's own words, the thing the whole reel builds on: the starting point
  is random noise like TV static.

## Evidence plan

| Beat | Evidence |
|---|---|
| B01 | Midjourney docs quote; the toy's real seed-7 starting static, walked back to a heart |
| B02 | a real training picture noised by the exact forward process (no model) |
| B03 | the forward equation and loss, typeset; the schedule's real numbers |
| B04 | the training set sample, the run's stats, the reverse run and the model's guesses |
| B05 | seed 38 under both prompts; four seeds under one prompt |
| B06 | Midjourney's own best-practice advice on seeds |

## Out of scope, deliberately

- Text encoders, latent space, U-Nets, transformers — true of real generators,
  unnecessary for the one idea, and each would need its own reel.
- Any claim about Midjourney's internals beyond its documentation.
