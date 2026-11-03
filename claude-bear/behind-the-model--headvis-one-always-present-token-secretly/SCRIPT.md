# Why One Always-Present Token Secretly Hijacks Every Attention Statistic — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`behind-the-model/headvis-one-always-present-token-secretly` (Teardown-register
scaffold, never rendered). 10 beats ≈ 2:20.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes that when one token wins the attention max almost every time, it must be the real signal. It isn't — it's the sink. So: signal, or sink?" | Writer types "Token zero keeps / winning the attention / max — that must be / the real signal, right?", hesitates on "signal", corrects to "sink" |
| B01 | 1 stakes + **4 anchor planted** | Look at one real attention head: layer four, head three, across fifty thousand sentences. Token zero — the sentence-start marker — wins the max-attention position in ninety-one percent of them, with more than half the weight every time. The verb-to-subject link everyone expects only shows up once token zero is excluded from that count. | THE ANCHOR — a heatmap grid, column 0 glowing terracotta in every row; stat callout 91% / >0.55 |
| B02 | 2 wrong guess | The natural guess: if one position wins that statistic almost every time, across thousands of unrelated sentences, it must be carrying the sentence's real meaning — attention is supposed to point at what matters most. | Column 0 spotlighted, arrows from many sentence icons converging on it, labeled "the real signal?" |
| B03 | **2 break it** + 3 mechanism | But softmax has to spend all of its probability on every single row, whether any position deserves it or not. Token zero is present in every sequence and carries no sentence-specific meaning, so it's the cheapest place to park the leftover weight — that's not a discovery about meaning, it's just where the math had nowhere else to go. | "the real signal?" struck through; a probability bar forced to sum to 1, the leftover mass draining into the always-present, empty seat |
| B04 | 3 mechanism, continued | Take one sentence starting with that marker: the raw weights might read something like point five eight on the marker and far less on every real word. Run that pattern across a thousand sequences and the marker wins the max ninety-four percent of the time. Exclude just that one position from the count, and the real dependency — the verb pointing back to its subject — wins sixty-eight percent instead. | a small bar chart of raw weights (marker vs. real words); before/after stat: 94% raw max → 68% once excluded |
| B05 | **5 direction A** | One direction: seeing the sink dominate a head's max doesn't mean that head learned nothing. The real signal can still be sitting in the rest of the row — it's just outweighed by the one reflex position the moment you only look at the max. | a row's full distribution: tall sink bar, smaller real bars still present, labeled "still there, not the max" |
| B06 | **5 direction B** + **4 anchor payoff** | The other direction: a head that doesn't lean on token zero isn't automatically trustworthy either — it might just be parking its leftover weight on a different filler, like a comma or a padding token. Mask out the known non-signal positions across this same head, and the patterns that were invisible before — real subject, object, and verb links — light up across almost every row. | THE ANCHOR RETURNS — same heatmap, column 0 masked out, diverse real patterns lighting up across the remaining columns |
| **BCRY** | **6 carry-out** | One always-present, meaning-empty token quietly wins nearly every attention statistic you compute — exclude it before you trust what the rest of the pattern is actually showing you. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I'm looking at attention weights in a transformer, and one position — often token zero — keeps winning the max across almost every head and layer. Walk me through how to check whether that's a real signal or an attention sink, and show me how to redo the statistic with that position excluded so I can see what's actually underneath it. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Why One Always-Present Token Secretly Hijacks Every Attention Statistic. Liam, in for Bear. | `OutroCTA` |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced *and falsified by a case* | B02 states the guess; B03 breaks it with the source's own mechanism (softmax must spend its mass, BOS is the cheapest seat) plus the measured 91%/verb-subject case from B01 |
| Exactly one inference flag | None needed — every claim restates the source's stated mechanism and measured example (QUESTION.md) |
| One anchor, planted early, paid off late | B01 → B06 (the heatmap) |
| Both failure directions | B05 and B06 |
| No design judgment | B03–B04 describe why the sink exists and how it was measured; never rule on whether the model was well built |

## Deliberately not claimed

- **Not "the sink means the head learned nothing."** B05 draws the line: a
  dominant sink measures where the max landed, not whether the rest of the
  row carries signal.
- **Not "excluding token zero always reveals the truth."** B06 is precise:
  the same exclusion logic applies to other low-information filler tokens
  too, not uniquely to token zero.
- **Not a claim about why models learn this behavior during training** —
  only the observed mechanism (softmax must spend its mass somewhere) and
  its measured consequence for aggregate statistics.

## Handoff prompt (BHTF, read aloud then discussed)

> "I'm looking at attention weights in a transformer, and one position —
> often token zero — keeps winning the max across almost every head and
> layer. Walk me through how to check whether that's a real signal or an
> attention sink, and show me how to redo the statistic with that position
> excluded so I can see what's actually underneath it."

Why it's worth running: it turns the video's one measured mechanism into a
direct diagnostic on the viewer's own attention-weight dump, and re-deriving
the statistic with the sink excluded is itself the fix the video argues for.

---
**GATE P — signed:** ______________________  (human)
