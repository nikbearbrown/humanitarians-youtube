# PEDAGOGY — Inside the Black Box, Part 2

**Reel** `weekly_updates/2026-10-23-inside-the-black-box-part-2/` · **slug** `claude-sai-inside-the-black-box-part-2`
**Part 1** `weekly_updates/2026-10-19-inside-the-black-box/`
**Subject** Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?" (14 Feb 2023) · **week of** 2026-10-23
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + two figure plates (6 of Wolfram's figures), no Manim, nothing paid

---

## The ONE idea

> Open a trained net and you can see everything: in GPT-2, every one of
> 124,439,808 weights, and exactly where each sits. What no one can do yet is
> read them.

Split from the single "Inside the Black Box" reel at Sai's request on
2026-10-26. Part 1 (how a net gets its numbers) is in the 10-19 folder; this
part opens trained nets up. The folder date 2026-10-23 is the one Sai gave.

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open; "last time … part two". |
| B01 | LOOKING INSIDE | figure plate · 2 figures | A cat in layer 1 (nameable) and in layer 10 (not). |
| B02 | GPT-2, OPENED | `ExecutedData` | Blocks, heads, embedding length and weights, counted from the weights file. |
| B03 | EVERY WEIGHT, COUNTED | `TypesetMath` | N = Vd + Pd + L(12d² + 13d) + 2d = 124,439,808, from the tensor shapes. |
| B04 | INSIDE GPT-2 | figure plate · 4 figures | Word map, 12 attention patterns, a 768×768 matrix raw and smoothed. |
| B05 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B06 | HANDOFF | `ClaudeComposerAsk` | Open GPT-2 yourself; ask what a weight plot can and can't tell you. |
| B07 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

B01, B02, B04 and B06 keep the narration of the single-reel version (old B05,
B06, B07, B09); Kokoro re-measured them identically.

## ILLUSTRATE LAW check

Claude UI at B00, B06 and the verdict only. Body beats:
`figures → ExecutedData → TypesetMath → figures`. No repeats; every beat has an
ordered `show` block.

## 9:16

Every Remotion pattern has a `*916` sibling; the two figure plates have
re-composed portrait plates in `pantry/`. **Portrait-only edit:**
`fix_vertical.py` swaps B04's GATE V contrast boxes to portrait coordinates —
re-run it after every `shorts.py --vertical`.

## Evidence and honesty

- **Executed locally:** `evidence/gpt2_inspect.py` reads `openai-community/gpt2`'s
  `model.safetensors`: 12 blocks, 12 heads (config.json), 768 per token, 50,257
  tokens, 1,024 positions, 7,087,872 weights per block (all 12 equal),
  124,439,808 in all. A NumPy forward pass reproduces Wolfram's first figure to
  5 significant figures (said once in B02).
- **The math is a count, checked both ways:** `build_beats.py` asserts
  12d² + 13d = 7,087,872 = the measured block, and Vd + Pd + 12·block + 2d = the
  measured total.
- **B04's word map is not GPT-2's embedding** (Wolfram built it from "5 billion
  words from the web"); captioned "Words laid out by meaning".
- **GATE V:** B04 declares `qc.contrast_regions` (kicker, first caption, credit),
  because Wolfram's pale weight-matrix figure drags the whole-frame average under
  0.30 though the text is dark ink on cream.

## Images and license

Six figures from the essay, CC BY-NC-SA 4.0 (approved by Sai 2026-10-25):
credited on every plate and in DESCRIPTION.md; **not monetized; the video
carries CC BY-NC-SA 4.0.**

## Pronunciation (narration only)

- `GPT-2's first block` → "the first block of GPT-2"; numbers written as words.

## Expected build noise (not bugs)

- SKIN LINT at B07 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
- **Do not edit `beat_sheet.json` while `remotion_scenes.py` is running.**

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Does Part 2 stand on its own for someone who missed Part 1?
- [ ] B03: is the weight-count derivation clear enough at speaking speed?
- [ ] License: OK to publish unmonetized, under CC BY-NC-SA 4.0?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 13.9s measured (43 words)

> Last time: a neural net is simple parts, and nobody writes its weights. This
> is Sai. Part two of Stephen Wolfram's tour of what's inside ChatGPT: what you
> actually see when you open a trained net, from a vision net to GPT-2 itself.

### B01 · LOOKING INSIDE — `figure plate · pair` · 17.8s measured (69 words)

> So what does looking inside show? Feed a cat picture to a net trained to tell
> cats from dogs. In its first layer, you can still name some of what you see:
> the cat without its background, the outline of the cat. By the tenth layer,
> Wolfram writes, it's harder to interpret. The net is picking out features,
> maybe pointy ears, but mostly ones we have no names for.

### B02 · GPT-2, OPENED — `ExecutedData` · 19.3s measured (58 words)

> Now the language side. ChatGPT itself can't be downloaded, but GPT-2, the
> small model Wolfram uses for his examples, can. We opened its weights file on
> this Mac: twelve attention blocks, twelve heads in each, seven hundred sixty-
> eight numbers per token, a hundred twenty-four million weights. Our rerun even
> matches his first figure's next-word odds, to the decimal.

### B03 · EVERY WEIGHT, COUNTED — `TypesetMath` · 18.9s measured (60 words)

> Where does that number come from? Count the shapes. The token table: about
> fifty thousand tokens, seven hundred sixty-eight numbers each. Then each
> block: twelve d squared plus thirteen d, about seven million. Twelve blocks,
> plus the table of positions, add up to exactly one hundred twenty-four
> million, four hundred thirty-nine thousand, eight hundred eight. Every weight
> is accounted for.

### B04 · INSIDE GPT-2 — `figure plate · quad` · 22.7s measured (72 words)

> Inside, each word becomes a list of numbers. Projected flat, words with
> related meanings land near each other: alligator beside crocodile. In the
> first block of GPT-2, twelve attention heads look back over the text, each
> with its own pattern. Here's one of its weight matrices, seven hundred sixty-
> eight by seven hundred sixty-eight. It looks like static. Smooth it, and some
> structure appears. What that structure encodes, Wolfram writes, is quite
> unknown.

### B05 · VERDICT — `ClaudeVerdictArtifact` · 16.3s measured (52 words)

> So, part two: in GPT-2 you can print every one of a hundred twenty-four
> million numbers, and say exactly where each one sits. What no one can do yet
> is read them. Wolfram calls ChatGPT's success a scientific discovery, an
> honest way of saying nobody has a theory for why it works.

### B06 · HANDOFF — `ClaudeComposerAsk` · 15.4s measured (54 words)

> Your turn. GPT-2 is free and runs on a laptop. Load it, count its weights, and
> plot one of its weight matrices. Then ask an assistant the hard question: what
> does that picture actually tell you about what the model knows, and what can't
> it tell you? Then check its answer against the picture.

### B07 · OUTRO — `LogoOutro` · 3.2s measured (7 words)

> Inside the black box, part two. Sai.

**Total: 415 words** → 127.3s measured (2:07). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: __________     — reviewer: ______________  date: __________
