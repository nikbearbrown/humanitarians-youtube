# Explainer — Quantization In LLMs

**Week:** 9–14 Nov 2026
**Type:** STEM / AI explainer · sixth in the inference-mechanics series
**Channel:** Infra with Simblex (personal channel, not the Humanitarians AI one)
**Format:** `ai-explainer` · 11 beats · ~3:10 · 16:9 with a 9:16 cut

- **Video:** TO FILL
- **Drive:** (https://drive.google.com/drive/u/1/folders/10vBcZC-Pgq_oK_yeLS8QyZZNgFg6lbRK)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Script:** `SCRIPT-quantization-in-llms.md` in this folder

## Where it sits in the series

KV Cache → PagedAttention → Prefill vs Decode → Speculative Decoding →
Continuous Batching → **Quantization**. The first five are about how inference
*runs*; this one is about how the model *fits* in the first place.

## The one idea

A model's weights sit in memory at some numeric precision, usually 16-bit
floating point. Quantization swaps that for a smaller fixed-point
representation — typically 8-bit or 4-bit integers — with a scale factor to
convert between them. Same architecture, same weights in spirit, a fraction of
the memory, and often faster math on hardware built for low-precision integers.

The catch is not whether you can shrink the numbers. You always can. It is what
a naive shrink does to the handful of outlier weights every large model turns
out to grow.

## The argument, in order

**The arithmetic is as direct as it sounds.** Two bytes per parameter at FP16,
one at INT8, half a byte at INT4 — so a 7-billion-parameter model's weights go
from roughly 14 GB to 7 GB to 3.5 GB. Half the bits, half the memory.

**Two routes.** Post-training quantization converts a finished model after the
fact: fast, no retraining, and the default for most deployed models.
Quantization-aware training simulates the low precision during training so the
model learns to tolerate the rounding — more compute, usually a smaller
accuracy gap.

**One formula underneath.** A scale factor is derived from the range of the
weights; quantizing divides by it and rounds to an integer; dequantizing
multiplies back. Every quantized weight is an integer plus the instructions for
undoing it.

**Then the catch.** That scale is set by the widest value in the group. One
huge outlier forces the scale wide enough that every ordinary weight is crushed
into a handful of buckets — and large language models reliably grow a small
number of these outlier channels. A scheme that ignores them loses far more
accuracy than the bit count alone predicts.

**Which is why the toolchain has so many names.** GPTQ minimises reconstruction
error layer by layer. AWQ protects the slice of channels activations lean on
hardest. GGUF mixes precisions and runs well on CPU. NF4/QLoRA keeps a frozen
4-bit base with small trainable adapters. Four answers to the same outlier
problem.

**The verdict.** Roughly half the memory at 8-bit, roughly a quarter at 4-bit,
plus faster integer math. Most capability survives 8-bit intact and a
well-chosen 4-bit scheme comes close. Below that, or with a scheme blind to
outliers, accuracy degrades. There is no bit count where the saving is free.

## Why this topic now

The gateway project spent nine sprints establishing that the cheapest model
Mycroft can call answers as well as the expensive one on its tasks. Quantization
is a large part of *why* a cheap tier can exist at all: a smaller numeric
footprint is what lets a model be served at a fraction of the price per token.
This explainer is the mechanism behind the economics the project has been
measuring, and it ends on the same note the project keeps landing on — the
saving is real, and it is not free.

## Sourcing, stated deliberately

Unlike the Mycroft reels, **no source report backs this one.** Every claim is
general, stable ML-systems knowledge: the bit-width memory arithmetic, the
PTQ/QAT split, the scale and zero-point formula, and the outlier-channel
problem that LLM.int8() and AWQ were built around.

Because of that, the script stays at "roughly half" and "roughly a quarter"
and cites no benchmark figures. A decimal-point claim would need a primary
source behind it, and there isn't one here. That restraint is the point rather
than a gap.

## Production notes

Every component is reused from the confirmed-working set; nothing new was
authored for the content. Two needed fixing before that was true:

- **B03 changed component.** It was drafted as a bar chart, but `BarChart`
  turned out to be a differently skinned component with no matching Claude
  skin and no `sparkLine` prop — it was never in the confirmed set, despite an
  earlier note claiming otherwise. B03 now reuses `ClaudeCodeBeat` with the
  same three numbers as a short table. Content and narration unchanged.
- **`MedhavyConceptCard` had the portrait bug** that cost the Sprint 8 reel a
  rebuild: a fixed, unwrapped sparkLine and no `*916` composition. Fixed before
  use this time rather than after, and verified on an isolated still.

The 9:16 cut is a single pass, no revisions: B00 → B02 → B06 → B08 → B10.
B04's two-column comparison stays 16:9 only.

## Limits

- No primary sources cited, by design — so no specific benchmark numbers.
- The channel handle `@InfraWithSimblex` is a best guess from the channel name
  and needs confirming; it appears in B00 and B10.
- The runtime is arithmetic — word count divided by the voice's measured rate —
  not a measured render. Audio sets the real clock.