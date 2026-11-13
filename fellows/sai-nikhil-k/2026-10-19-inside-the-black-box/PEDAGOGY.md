# PEDAGOGY — Inside the Black Box, Part 1

**Reel** `weekly_updates/2026-10-19-inside-the-black-box/` · **slug** `claude-sai-inside-the-black-box-part-1`
**Part 2** `weekly_updates/2026-10-23-inside-the-black-box-part-2/`
**Subject** Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?" (14 Feb 2023) · **week of** 2026-10-19 (second reel)
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + two figure plates (6 of Wolfram's figures), no Manim, nothing paid

---

## The ONE idea

> Every part of a neural net is simple arithmetic, and nobody writes its weights:
> training finds them. Two nets can fit the same examples equally well and still
> disagree beyond them, and nothing in the fit says which to trust.

Sai gave the topic and the source and chose the "Inside the Black Box" angle
(2026-10-25). On 2026-10-26 he asked for the one reel to become two: **Part 1**
(this folder) is how a net gets its numbers; **Part 2** is what you see when you
open a trained one. Each part is a complete reel with its own open, verdict,
handoff and outro, and its own math and evidence beats.

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open; "this is part one". |
| B01 | SIMPLE PARTS | figure plate · 3 figures | A small net with its weights, the activation curves, the net written out as one formula. |
| B02 | ONE NEURON | `TypesetMath` | Wolfram's f(w·x + b), with a worked case ReLU clips to zero. |
| B03 | LEARNED, NOT WRITTEN | figure plate · 3 figures | Descent on a loss landscape, 10k → 10M training runs, four equally good nets. |
| B04 | WHICH NET IS RIGHT? | `BinaryBranch` | "There's really no way to say." |
| B05 | TEN NETS, TRAINED HERE | `ExecutedData` | Our own test of that claim: ten nets, worst MSE 0.0022, guesses at x = 3 from −0.43 to 2.84. |
| B06 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B07 | HANDOFF | `ClaudeComposerAsk` | Train two tiny nets yourself and plot them past the data. |
| B08 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

B01–B04 are unchanged from the single-reel version (same narration, audio and
renders; Kokoro re-measured identically).

## ILLUSTRATE LAW check

Claude UI at B00, B07 and the verdict only. Body beats:
`figures → TypesetMath → figures → BinaryBranch → ExecutedData`. No two
consecutive body beats share a pattern; every beat has an ordered `show` block.

## 9:16

Every Remotion pattern has a `*916` sibling; the two figure plates have
re-composed portrait plates in `pantry/`. No positional words in the narration.

## Evidence and honesty

- **Executed locally:** `evidence/train_nets.py` trains ten 1-32-32-1 ReLU nets
  (NumPy, Adam, seeds 0–9, all reported) on a constructed step function over
  [−1, 1], then asks each about x = 3. Every net fits (worst MSE 0.0022); the
  guesses run from −0.43 to 2.84. The task is constructed and labelled so; it
  tests Wolfram's claim, it does not reproduce his figure.
- **"ChatGPT" in the essay means its 2023 model.** The narration dates it.
- **ReLU is Wolfram's choice for his toy nets;** GPT-2 uses GELU (B02 card says so).
- **B02's numbers are constructed** and labelled on screen.

## Images and license

Six figures from the essay, CC BY-NC-SA 4.0 (approved by Sai 2026-10-25):
credit on every plate and in DESCRIPTION.md; **not monetized; the video carries
CC BY-NC-SA 4.0.**

## Attribution

Hosted by Sai in his own name. The only person named is Stephen Wolfram.

## Pronunciation (narration only)

- `ReLU` → "ray-loo"; `2023` → "twenty twenty-three"; decimals are written out
  as words in B05 ("minus point four three").

## Expected build noise (not bugs)

- SKIN LINT at B08 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
- **Do not edit `beat_sheet.json` while `remotion_scenes.py` is running.**
- The single-reel masters of 2026-10-25 are parked in `_superseded/`.

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Is the split point right (training here, looking inside in Part 2)?
- [ ] B05: is a constructed ten-net test a fair check of Wolfram's claim?
- [ ] License: OK to publish unmonetized, under CC BY-NC-SA 4.0?
- [ ] Delete `_superseded/` once you're happy with both parts?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 14.2s measured (50 words)

> ChatGPT writes one word at a time, and every word comes out of a giant neural
> net. This is Sai. In twenty twenty-three, Stephen Wolfram opened nets like
> that one up, one picture at a time. This is part one: what the parts are, and
> where their numbers come from.

### B01 · SIMPLE PARTS — `figure plate · left+2` · 18.3s measured (57 words)

> Start with the parts. A neural net is layers of artificial neurons. Each one
> takes in numbers, weighs them, adds them up, and passes a single number on
> through a simple function. Write out everything this tiny net computes and you
> get one tangled formula. ChatGPT, Wolfram writes, is a formula like that, with
> billions of terms.

### B02 · ONE NEURON — `TypesetMath` · 18.3s measured (65 words)

> Here's one neuron, the way Wolfram writes it. Multiply the inputs by weights,
> add a constant b, and apply a function f. In his examples, f is ray-loo: it
> turns any negative number into zero. Say the weights are one half and minus
> point eight, both inputs are one, and b is point one. The sum is minus point
> two, so the neuron outputs zero.

### B03 · LEARNED, NOT WRITTEN — `figure plate · hero+strip` · 20.4s measured (73 words)

> Nobody types those weights in. Training shows the net examples, measures how
> far off its answers are, and nudges every weight downhill on that error, like
> water running down a mountain. It settles into some mountain lake, not always
> the lowest one. Even this toy net needed millions of examples to learn one
> simple shape. And train it twice, and you can get nets that agree on the
> examples but not beyond them.

### B04 · WHICH NET IS RIGHT? — `BinaryBranch` · 16.9s measured (61 words)

> So which net is right? Wolfram's answer is blunt: there's really no way to
> say. Both are consistent with every example they were shown. Each just has its
> own built-in way of guessing beyond them, and some of those guesses look more
> reasonable to us than others. That's the black box in miniature: you can check
> the fit, not the reasoning.

### B05 · TEN NETS, TRAINED HERE — `ExecutedData` · 17.8s measured (62 words)

> We tried it on this Mac. Ten small nets, the same examples of a step shape,
> different random starts. All ten fit: the worst training error is point zero
> zero two two. Then ask each one about x equals three, outside the data. The
> answers run from minus point four three to two point eight four. Same data,
> same fit, no agreement.

### B06 · VERDICT — `ClaudeVerdictArtifact` · 15.2s measured (49 words)

> So, part one: every neuron does simple arithmetic, and nobody writes the
> weights. Training slides them downhill until the net fits its examples. But
> two nets can fit the same examples equally well and still disagree beyond
> them, and nothing in the fit tells you which guess to trust.

### B07 · HANDOFF — `ClaudeComposerAsk` · 14.5s measured (53 words)

> Your turn. Ask an assistant for a short script that trains two tiny nets on
> the same points, with different random seeds. Run it, and plot both nets past
> the edge of your data. Then ask the hard question: where they disagree, which
> one would you trust, and how would you find out?

### B08 · OUTRO — `LogoOutro` · 3.1s measured (7 words)

> Inside the black box, part one. Sai.

**Total: 477 words** → 138.8s measured (2:18). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: __________     — reviewer: ______________  date: __________
