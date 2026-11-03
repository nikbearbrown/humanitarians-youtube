# Solve-Verify Asymmetry — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`behind-the-model/claude-liam-solve-verify-asymmetry` (Teardown, CLI-style).
10 beats ≈ 2:20.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes that if Claude solves a problem in seconds, checking the answer must be just as fast. It isn't — for hard problems, checking can take far longer. So: is checking fast, or harder?" | Writer types "Claude solved it / in two seconds. / So checking is fast, / right?", hesitates on "fast", corrects to "harder" |
| B01 | 1 stakes + **4 anchor planted** | Try it yourself: ten problems of rising difficulty, timed two ways — how fast the AI answers, and how long a strict, deterministic check takes to confirm it. Divide the two. Simple arithmetic: the check ran about three times as long as the answer. Hard combinatorics: about a hundred times. | THE ANCHOR — a ratio ladder, four rungs (arithmetic/algebra/quadratic/combinatorics), raw measured ratios |
| B02 | 2 wrong guess | The natural guess: since the AI already produced the answer, confirming it should be just as fast — glance at the same work, done. | "fast in → fast out" mirrored arrows around one answer box |
| B03 | **2 break it** + 3 mechanism | But the measured ratios break that guess — checking took three to a hundred times longer, not the same. For many hard problems, producing one plausible answer is comparatively cheap; actually confirming it's correct means doing the real computation over — and that's the expensive part. | the "fast in → fast out" mirror struck through; two paths shown at different costs — GUESS (cheap) vs. CONFIRM (expensive) |
| B04 | 3 mechanism, continued | One number looked wrong: three times seemed too low for arithmetic — checking should barely cost anything there. The culprit was a hidden startup cost in the checker itself. Strip that out, and arithmetic ties out close to one-to-one. Algebra, quadratic, and combinatorics don't move at all — the gap there was never a measurement artifact. | a checker box with a hidden "startup cost" weight removed; before/after arithmetic bar shrinking to parity, other bars unmoved |
| B05 | **5 direction A** | One direction: a big ratio on a hard problem doesn't mean the AI's answer was wrong — it only means confirming correctness costs more, whether the answer is right or not. | a ratio number boxed as "CHECKED: cost to confirm", a separate faded card "right or wrong?" outside the box |
| B06 | **5 direction B** + **4 anchor payoff** | The other direction: a faster AI model doesn't close this gap — it can widen it, since more candidate answers arrive per second, and each one still needs the same expensive check. Redo the ladder after the fix: arithmetic near one-to-one, algebra and combinatorics unchanged, and a full proof sketch runs about three hundred times longer to check than to produce — off the chart. | THE ANCHOR RETURNS — same ladder, corrected arithmetic rung, a fifth "proof" rung overflowing the chart with an arrow |
| **BCRY** | **6 carry-out** | For hard problems, checking an answer costs far more than producing one — and a faster model doesn't close that gap, it just produces more answers that still need checking. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want to measure the solve-verify gap in my own work. Walk me through picking three tasks I do with AI — one trivial, one medium, one hard — and timing a deterministic check against how long the AI took to answer. What should I do differently if that ratio turns out to be large? Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Solve-Verify Asymmetry — AI Thinks Fast, Verification Thinks Harder. Liam, in for Bear. | `OutroCTA` |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced *and falsified by a case* | B02 states the guess; B03 breaks it with the source's own measured ratios (3x–100x, not parity) |
| Exactly one inference flag | None needed — every claim restates a measured experiment and its documented correction (QUESTION.md) |
| One anchor, planted early, paid off late | B01 → B06 (the ratio ladder) |
| Both failure directions | B05 and B06 |
| No design judgment | B03–B04 describe why the gap exists and how it was checked for rigor; never rule on whether the setup was well built |

## Deliberately not claimed

- **Not "NP-hard" jargon.** Source states the complexity-theory framing
  explicitly; this cut keeps the fact (producing a candidate is cheap,
  confirming it is the expensive part for hard problems) without the
  technical term, since the audience is meeting Claude for the first time.
- **Not "this proves the AI was right or wrong."** B05 draws the line: a
  large ratio measures confirmation cost, not correctness.
- **Not "faster models make the ratio worse."** B06 is precise: the
  per-problem ratio is unaffected by model speed; what changes is the volume
  of unchecked answers produced per unit time.
- **The measurement-artifact fix (B04) is stated as a correction the source
  made, not a caveat about the whole reel** — it strengthens the claim
  (the gap survived a rigor check) rather than undermining it.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to measure the solve-verify gap in my own work. Walk me through
> picking three tasks I do with AI — one trivial, one medium, one hard — and
> timing a deterministic check against how long the AI took to answer. What
> should I do differently if that ratio turns out to be large?"

Why it's worth running: it turns the video's one measured experiment into a
five-minute check on the viewer's own workflow, and a growing ratio is itself
the argument for adding a deterministic check before trusting an AI answer.

---
**GATE P — signed:** ______________________  (human)
