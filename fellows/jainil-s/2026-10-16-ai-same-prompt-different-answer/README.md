# Same Prompt, Different Answer

**Track:** educational (STEM / AI) · **Week ending:** 2026-10-16

> The model does not pick the next word. It produces a probability for every
> word it could say, and something draws one. Temperature decides how peaked
> that distribution is — it does not add the randomness.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:24. **No video files are in this repo.**

## The argument

1. **One position, seven candidates.** The top word takes 46.5% at temperature
   1.0 — so better than half the time you get something else. Nothing has gone
   wrong; that is the distribution doing what it says.
2. **Temperature reshapes, it does not randomise.** At T=0.2 the same scores
   give the top word 95.1% and flatten the rest into the floor.
3. **Low temperature still does not buy repeatability.** The chance that every
   token in a 200-token answer takes the top choice, at T=0.2, is **1 in
   22,991**. Two identical long answers are a coincidence, not a guarantee.
4. **And temperature 0 is not the guarantee people think.** Greedy decoding is
   deterministic only if the scores come out the same every time — and they
   need not.

## The correction that shaped the video

The obvious way to explain point 4 is "floating point isn't associative, so
results vary." **That is wrong**, and the reel says so explicitly. A fixed
sequence of operations on fixed inputs is perfectly deterministic.
Non-associativity is the *mechanism* by which a changed order yields a changed
result; it is not the *cause* of run-to-run variation.

The cause is **dynamic batching**. Your request lands in a batch of a different
size, the kernel splits its reductions differently, the order changes, and the
logits shift by a hair. If the top two candidates are closer than that hair,
greedy decoding can pick the other one. SGLang's own documentation says this
directly and is quoted on B06.

## Reproduce it

```bash
python sampling_evidence.py
```

No model is called. Everything is arithmetic you can check by hand: a softmax
over seven illustrative logits, and one demonstration that summing the same
thousand float32 values in a different order gives a different answer
(−48028.30078125 vs −48028.27343750).

The logits are illustrative and the reel says so. The argument is about the
shape of the softmax, which holds for any logits; the numbers exist so there is
something concrete on screen.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | "Is this a bug?" — answered twice over |
| B01 | BLUF | `BrutalistHesitantWriter` | "The model **picks**" → **draws** |
| B02 | SETUP | `BarChart` | Seven candidates and their probabilities at T=1.0 |
| B03 | TURN | `DistributionShape` | The same scores at T=0.2, with T=1.0 ghosted behind |
| B04 | EVIDENCE | `PositionCurve` | Chance of an identical answer against its length |
| B05 | LAND | `DigitDiff` | The same thousand numbers, summed two ways |
| B06 | SOURCE | `FormACard` | SGLang's docs on batching, verbatim |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt for a flaky test you own |
| B08 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

Only `DigitDiff` + `DigitDiff916`. Three of four body beats reuse existing
components — `BarChart`, `DistributionShape` (built the same day for *The Tails
Go First*, its `ghost` prop repurposed from "what was lost" to "what was
reshaped"), and `PositionCurve`.

## Honesty notes

- **No measured divergence rate for a real model.** Figures like "80 distinct
  completions in 1,000 runs" circulate in secondary write-ups about systems we
  have not run. Not used.
- **No throughput cost figure** for deterministic inference, for the same
  reason.
- **An earlier draft measured how often a tiny perturbation flips the argmax.**
  That number described a near-tie constructed by hand, not real decoding. Cut.
- **The logits are not a real model's** and the reel says so.

Full ledger in `FACTCHECK.md`, sources in `SOURCES.md`, build record in
`FRICTIONAL.md`.
