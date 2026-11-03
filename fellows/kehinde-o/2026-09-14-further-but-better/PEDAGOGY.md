# Pedagogy Review

## Topic
Post-training quantization: why the method that moves weights furthest from the
originals is the one that damages the model least.

## The ONE idea
Rounding error is a move in weight space, but damage is measured in loss space,
and the loss surface around a trained layer is a tilted valley. Naive rounding
snaps each weight to the nearest step and takes whatever hit the grid dictates.
GPTQ rounds one column at a time and slides the not-yet-rounded columns to
absorb the error first. It ends up provably worse by weight distance and
dramatically better by output accuracy.

Distance from the original is not damage to the answer.

## Learning Objective
Viewer can state the diagnostic: measure the thing you care about rather than
the thing that is easy to measure, and change one axis at a time or the winner
is half method and half accounting.

## Audience
Smart people getting proficient with AI. No quantization background assumed;
Hessians, perplexity internals and group sizes are deliberately not named. The
benchmark is introduced simply as "lower is better".

## Register check (Plain)
States the method, the decision trigger, and where it fails: the video reports
that the author's own first benchmark was confounded, and that AWQ with the
paper's fixed alpha performed worse than plain grouped rounding until the
per-layer search was implemented.

## Honesty
Every figure is measured in the repository across 34 evaluations on one fixed
wikitext-2 protocol: 26.2 fp32 baseline, 28.5 at 4-bit, 112 against 2,482 at
3 bits, weights 2.5x further with outputs 2x more accurate. The failed configs
are acknowledged on screen rather than dropped.

## Source
https://github.com/Kenny0bi/quantlab
B03 is the author's own Manim animation, re-rendered at 4K from
assets/manim_gptq.py rather than upscaled from the repo's 1080p file.

## Kehinde's HAI requirement
B00 opens verbatim: "Hi, I am Kehinde Obidele and this video is about ..."

## VERDICT: PASS
