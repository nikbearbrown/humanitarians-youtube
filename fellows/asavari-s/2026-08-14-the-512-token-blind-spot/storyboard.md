# Storyboard — The 512-Token Blind Spot

_Fellow: Asavari (Ash) Shejwal · AI / STEM · 2026-08-14 · 16:9 + 9:16 · 4K (3840×2160)_

Official Brutalist beat-sheet format (renders via brutalist.art / kokoro voice `af_kore`).
Beat two is the executive summary ("why this matters"), per review.

## Beat 1 — GREETING

**On screen:** This is Humanitarians.

**Narration:** This is Humanitarians.

## Beat 2 — OPEN

**On screen:** Why did the model miss the one word that flips the meaning?

**Narration:** Models read tokens, not words, and can only take in so many. Feed a long document past the limit and the rest is cut off, sometimes mid-thought.

## Beat 3 — Why This Matters

**On screen:** What is this video about, and why should I watch it?

**Narration:** Hi, I'm Asavari, a fellow at Humanitarians AI. This video is about a subtle bug that causes big mistakes: how a model's token limit can silently drop the one word that flips a sentence's meaning. You'll learn why chunking is a real decision, not a default. If you feed long text to language models, this is for you.

## Beat 4 — THE PROBLEM

**On screen:** an invisible line

**Narration:** Picture a sentiment model with a five-hundred-and-twelve-token window reading an earnings statement. The text says revenue grew, and then, just past the cutoff, excluding one-time items. The model scores it as strong growth. It never saw the qualifier. The output is confident, clean, and wrong.

## Beat 5 — THE MECHANISM

**On screen:** chunk on meaning, not on count

**Narration:** The fix isn't a bigger model, it's treating chunking as a real decision. The naive approach cuts every five hundred and twelve tokens, splitting ideas in half. The better approach splits on meaning, keeping a claim with the qualifier that modifies it, and overlapping chunks so nothing important lands on a boundary.

## Beat 6 — THE LIMIT

**On screen:** there is always a boundary

**Narration:** A warning, because people reach for the obvious fix. Newer models have larger windows, but every model still has a limit, and long documents still get truncated. Worse, even within the window, models pay less attention to the middle. A bigger window pushes the boundary out. It doesn't make it disappear.

## Beat 7 — The verdict

**On screen:** The cutoff is a silent editor of your data

**Narration:** Know the token limit and how long your input really is. Look at where your chunks actually cut. Ask whether a qualifier could get separated from its claim. And check the tail of the document. The cutoff is a silent editor of your data. If you don't decide where it falls, it decides for you.

## Beat 8 — OUTRO

**On screen:** The 512-Token Blind Spot — outro card

**Narration:** The 512-Token Blind Spot. From Humanitarians AI.
