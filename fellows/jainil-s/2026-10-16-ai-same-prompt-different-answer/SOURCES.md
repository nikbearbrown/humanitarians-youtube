# SOURCES — Same Prompt, Different Answer

## Primary evidence (ships in this folder)

**`sampling_evidence.py`** — pure numpy, no model is called, runs instantly.
**Every probability, percentage and float shown on screen is printed by this
file.** It is all arithmetic you can check by hand.

The seven candidate tokens and their scores are **illustrative**, and the reel
says so on screen. The argument is about the shape of the softmax and how
temperature rescales it, which holds for any logits; the specific numbers exist
so the viewer has something concrete to look at rather than a hand-wave.

| Quantity | Value |
|---|---|
| Top token at T=1.0 | 46.5% → 53.5% chance of a different word |
| Top token at T=0.2 | 95.1% → 4.9% chance of a different word |
| `top_p=0.5` at T=1.0 | 2 of 7 tokens eligible |
| Identical 200-token answer at T=0.2 | 0.004% — **1 in 22,991** |
| Same 1000 float32 values, summed sequentially | −48028.30078125 |
| ...summed in ten blocks | −48028.27343750 |
| Difference | 0.027 |

## Published source

**SGLang documentation — Deterministic Inference.**
<https://docs.sglang.io/advanced_features/deterministic_inference.html>

Quoted verbatim on B06:

> "The main source is varying batch sizes. Different batch sizes cause GPU
> kernels to split reduction operations differently, leading to different
> addition orders."

> "Even with temperature=0, standard LLM inference can produce different outputs
> due to dynamic batching."

The page also documents `--enable-deterministic-inference`, which enables
batch-invariant operations, and `sampling_seed` for reproducible non-greedy
sampling.

## A correction this source forced

The reel was first going to say, in effect, "temperature 0 isn't deterministic
**because** floating point isn't associative." That is wrong, and the sources
are explicit about why: a fixed sequence of operations on the same inputs is
deterministic. Non-associativity is the *mechanism* by which a changed order
produces a changed result — it is not itself the *cause* of run-to-run
variation.

The cause is **dynamic batching**: the same request lands in a differently
sized batch, the kernel splits its reductions differently, and the order
changes. B06 was rewritten to say exactly that, and the narration now spends a
sentence on the distinction rather than glossing it.

## Deliberate omissions

1. **No measured divergence rate for any real model.** Secondary write-ups
   quote figures such as "80 distinct completions in 1,000 runs" for a specific
   model. That is a single secondary report about a system we have not run, so
   it is not in the reel.
2. **No throughput cost figure.** Reports of a ~34% slowdown for deterministic
   modes trace back to one benchmark we have not reproduced.
3. **No claim about how often real logits are close enough to flip.** An
   earlier draft of the script measured how often a tiny perturbation flips the
   argmax of a near-tie. That number was a property of a tie we constructed by
   hand, not of real decoding, so it was removed rather than quoted.
4. **No claim these specific logits come from a model.** They are illustrative,
   stated as such, and the conclusion does not depend on them.
