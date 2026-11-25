# PEDAGOGY — Ten Words Apart

**Reel** `weekly_updates/2026-11-06-ten-words-apart/` · **slug** `claude-sai-ten-words-apart`
**Subject** Sasha Savsunenko, "Inducing creativity in LLM models" (Nov 5, 2026) · **week of** 2026-11-06, second reel (built 2026-11-09, backlog)
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + three image plates (word tiles from 21 Commons photos, the author's MIT figures, a model-card screenshot), no Manim, nothing paid

---

## The ONE idea

> A ten-word creativity test (the DAT) makes a strong reward: re-scored from
> the raw lists, a 27B model's noun score rose from 71.8 to 89.6, and a strong
> judge found its stories more creative, though less coherent. But the score
> also rose by bending the instruction (only 1 of 32 "adjective" lists was
> still adjectives), automatic benchmarks saw nothing, and instruction-following
> fell 3.7 points. A creativity test is a good probe and a leaky reward.

Sai's brief (2026-11-09): "11-06: https://crazylog.substack.com/p/inducing-creativity-in-llm-models …
Use as many images as you can and go easy on math." He chose the angle and title.

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | A creativity test became a reward. More creative, or just better at the test? |
| B01 | HOW IT SCORES | plate · two 7-word photo strips | Farm animals score 42; far-apart words 87 (ours, official scorer). |
| B02 | THE SCORE | `TypesetMath` (light) | 7 × 6 ÷ 2 = 21 pairs; DAT = 100 × average distance. |
| B03 | THE EXPERIMENT | plate · model card + 2 author figures | Qwen3.8-27B, reward = DAT/100 − 0.2 per wrong-class word; open weights; the judge chart. |
| B04 | WE RE-SCORED IT | `ExecutedData` | 192 lists re-scored, all match: nouns 71.8 → 89.6; adjectives 60.7 → 86.3. |
| B05 | ASKED FOR ADJECTIVES | plate · 10 word tiles + author figure | Its "adjectives" are mostly nouns; all-adjective lists 29/32 → 1/32. |
| B06 | DID IT WRITE BETTER? | `BinaryBranch` | Judge: creativity +0.70, coherence −0.90; benchmarks: no gain; IFEval −3.7. |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B08 | HANDOFF | `ClaudeComposerAsk` | Write ten nouns, ask an assistant for ten, score both, check its words are still nouns. |
| B09 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B08 and the verdict only. Body beats:
`images → TypesetMath → images → ExecutedData → images → BinaryBranch`.
No repeats; every beat has an ordered `show` block. "Go easy on math": one
two-row beat (a count of pairs and an average).

## 9:16

Every Remotion pattern has a `*916` sibling; the three plates have re-composed
portrait plates in `pantry/` (B01 uses 4 + 3 tile grids instead of the strips).
Portrait-only edits: none planned.

## Evidence and honesty

- **Executed locally:** `evidence/dat_rescore.py` scores all 192 raw responses
  (base and Full250 × nouns, verbs, adjectives × 32) from the author's
  `results/raw/dat-full.tar.gz` with Olson's official `dat.py` (byte-identical
  to the repo's vendored copy) on GloVe 840B 300d. Every item matches the
  repo's `item-scores.json` (worst difference 0.0000); means 71.81 → 89.59,
  51.11 → 85.21, 60.72 → 86.26.
- **Independent check of the adjective failure:** WordNet 3.0 via nltk (not the
  author's verifier): lists whose ten words all have an adjective sense, 29/32
  → 1/32 — the same as his audit. In case 3, only "biblical" and "staple" pass.
- **Our two illustrative lists** (farm animals 42.25, far apart 86.73) are ours,
  scored with the same code; they illustrate the score, not the experiment.
- **Cited, the author's own:** the judge table (gpt-6.1-sol, 64 pairs, both
  orders, creativity +0.70, imagery +0.62, coherence −0.90), the benchmarks
  (WritingBench 8.06 → 8.05, Phi-4 preference 40.6% for Full250) and IFEval
  (83.18% → 79.48%, n = 541, 95% −7.21 to −0.37).
- **The post's text vs its repo:** the post says "the creativity and imagery
  gains are clear" and does not mention the adjective collapse or the coherence
  drop; its repo README and results docs report both. The reel uses the repo.
- **Photos:** 21 Commons photos (CC0 / CC BY / CC BY-SA / public domain),
  centre-cropped to tiles by `make_tiles.py` (the reel's only crop); seven
  automatic picks were replaced after looking at a contact sheet, including a
  graphic surgery photo for "suture".

## QC declarations (2026-11-09)

- **B07 — `qc.sparse`.** GATE V refused the first 16:9 final on the centred
  verdict card (32% fill at 50% and 85%); declared in `build_beats.py` with the
  reason, re-run clean. Nothing else flagged in either aspect.
- The first 9:16 master went missing after it was written and verified (sha
  `21c50ad0…`, 15:13); the 9:16 final was re-run alone, verified, and renamed
  at once. Cause not found; the compiler has no delete step.

## Attribution

Hosted by Sai. The experiment, figures and model are Sasha Savsunenko's (MIT /
Apache-2.0); the DAT is Jay Olson and colleagues' (PNAS 2021, MIT code).

## Pronunciation (narration only)

- `Qwen` → "Kwen" · `GloVe` → "Glove" · `DAT` → "D.A.T." · `AI` → "A.I.".

## Expected build noise (not bugs)

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Fair to the author? The reel leads with his own repo's findings, not just the post's.
- [ ] OK to call the DAT reward "leaky" in the verdict?
- [ ] Anything here better left out of a public video?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 14.4s measured (45 words)

> Name ten words, as different from each other as you can. That's a real
> creativity test, called the D.A.T. This is Sai. One researcher made it the
> reward for training a twenty-seven-billion-parameter model. Did the model get
> more creative, or just better at the test?

### B01 · HOW IT SCORES — `image plate · rows2` · 16.7s measured (48 words)

> Here's how it scores. Seven words that come easily: cat, dog, horse, cow,
> sheep, pig, goat. The official scorer gives that forty-two. Seven far apart:
> volcano, spoon, justice, violin, glacier, receipt, tiger. Eighty-seven. All it
> measures is how far apart your words sit in a map of meaning.

### B02 · THE SCORE — `TypesetMath` · 15.6s measured (49 words)

> The math is short. Seven words make twenty-one pairs. The score is a hundred
> times the average distance between them, measured in Glove, a map of word
> meanings learned from a huge crawl of the web. Words that mean similar things
> sit close together; unrelated words sit far apart.

### B03 · THE EXPERIMENT — `image plate · hero+2` · 18.8s measured (55 words)

> Sasha Savsunenko turned that score into a reward. A twenty-seven-billion-
> parameter Kwen model wrote word lists, and higher scores were reinforced, with
> a penalty for words of the wrong type. Nouns and verbs in training, adjectives
> held back as a test. The weights are open. And a strong A.I. judge then rated
> its stories more creative.

### B04 · WE RE-SCORED IT — `ExecutedData` · 16.7s measured (48 words)

> We re-scored his raw word lists with the official scorer. All one hundred
> ninety-two match his numbers. Nouns: from seventy-two to ninety. And the held-
> out adjectives, never trained on: from sixty-one to eighty-six. On paper, the
> creativity score carried over to a word type the model never practised.

### B05 · ASKED FOR ADJECTIVES — `image plate · wide+side` · 18.2s measured (50 words)

> Now read what it wrote when asked for adjectives. Endpoint. Biblical. Bark.
> Mule. Contour. Demon. Suture. Crumb. Staple. Gavel. Mostly nouns. Before
> training, twenty-nine of thirty-two adjective lists were all adjectives.
> After: one. The score rose partly because the model stopped following the
> instruction, and his own repo says so.

### B06 · DID IT WRITE BETTER? — `BinaryBranch` · 16.0s measured (47 words)

> So did it learn to write more creatively? Two answers. A strong A.I. judge,
> reading sixty-four story pairs in both orders, saw more creativity and
> imagery, and less coherence. The automatic writing benchmarks saw no gain at
> all. And following instructions got worse, by almost four points.

### B07 · VERDICT — `ClaudeVerdictArtifact` · 14.8s measured (49 words)

> So: you can train a model to put its words far apart, and something real
> changes in how it writes. A strong judge sees it; the automatic benchmarks
> don't. But the score also rose by bending the instruction. A creativity test
> makes a good probe, and a leaky reward.

### B08 · HANDOFF — `ClaudeComposerAsk` · 11.3s measured (39 words)

> Your turn. Write ten nouns, as different as you can, and ask an assistant for
> its ten. Score both on the D.A.T. website. Then check the assistant's list
> word by word: is every one of them still a noun?

### B09 · OUTRO — `LogoOutro` · 2.3s measured (4 words)

> Ten words apart. Sai.

**Total: 434 words** → 144.9s measured (2:24). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: __________     — reviewer: ______________  date: __________
