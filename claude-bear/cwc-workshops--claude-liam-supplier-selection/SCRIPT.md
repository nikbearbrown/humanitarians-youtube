# Claude, Supplier Selection — Narration Script (Plain register)

*Skill: `hai-simple`, mode `redo`. Register: **Plain**. 9 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (hai-simple WRITER LAW — no puppet, no
human step). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "You'd guess Claude just picks whichever supplier is cheapest and calls it done. It doesn't. It scores every supplier on a weighted formula. So what's actually deciding the winning score?" | Writer types "Claude just picks / whichever supplier / is cheapest, / right?" — hesitates on "cheapest", corrects to "highest-scoring" |
| B01 | 1 stakes + anatomy | A Claude "skill" is a folder Claude reads before it acts. This one is called supplier-selection. Open it up, and there's one file inside: SKILL.md — plain language, no hidden logic. | folder `supplier-selection/`, one file `SKILL.md`, chip "1 FILE" |
| B02 | 2 wrong guess | The natural guess is that Claude just ranks suppliers by price and picks whoever's cheapest — quote low, win the order. | the "lowest price wins" reading, sold as reasonable |
| B03 | **2 break it / 4 anchor planted** | Open SKILL.md and price is only part of the story: the score weighs price, lead time, and reliability together — fifty percent, thirty percent, twenty percent. | THE ANCHOR — the weighted score, three factors |
| B04 | 3 mechanism | Claude normalizes price and lead time onto the same zero-to-one scale, multiplies each factor by its weight, and adds them up. Highest score wins; ties break on price, then lead time, then name. | NORMALIZE → WEIGHT → SUM, linear |
| B05 | **4 anchor payoff / 5 both directions** | Feed it the same quotes twice and the formula scores them identically, every time — that repeatability is real. But SKILL.md also carries override notes that never show up in the catalog data, and if one applies, it can beat the top score. | THE ANCHOR RETURNS — same weights; third chip becomes "an override can flip it" |
| **BCRY** | **6 carry-out** | A Claude skill's pick isn't the cheapest supplier. It's the highest score from a weighted formula — and a note the formula never sees can still beat it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: "I'm going to hand you a short scoring formula with a few weighted factors in it. Before you compute anything, tell me each factor's weight and how you'd combine them — before you run the numbers." | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Supplier Selection. Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the "lowest price wins" read; B03 breaks it by opening the actual file and finding a three-factor weighted score instead of a price sort |
| Exactly one inference flag | None — direct, confirmed mechanism throughout (this is how the Claude Skill's SKILL.md works, not an inference about Claude); `one_flag: "N/A"` in metadata |
| One anchor, planted early, paid off late | B03 → B05 (the weighted score — price/lead-time/reliability, fifty/thirty/twenty) |
| Both failure directions | B05: same-input consistency (positive) vs. an out-of-band override beating the top score (negative) |
| No design judgment | B02–B03 describe why the wrong guess fails; nothing rules on whether "supplier-selection" is a *good* skill (the source's Popper/Plato lens moves and verdict language — "what it gets right," "what it bites" — are dropped; Plain explains and stops) |

## Deliberately not claimed

- **Not "price never matters."** Price carries the largest single weight
  (50%) in the formula — the reel's claim is that it isn't the *whole*
  formula, not that it's irrelevant.
- **Not a verdict on whether "supplier-selection" is a good skill.** The
  source (Teardown register) ran a Popper move ("what it bites: anything
  outside the spec") and a Plato move (artifact vs. world) as design
  judgment. Plain register keeps the same facts — a three-factor weighted
  score, override notes that sit outside the CSV data — without ruling on
  whether that's a good or bad way to build a purchasing tool.
- **No invented numbers.** The formula's exact weights (0.5 / 0.3 / 0.2) and
  the fact that supplier-specific overrides exist and sit outside the
  catalog data both come directly from the skill's SKILL.md; the reel does
  not invent supplier names, prices, or a specific override to narrate — it
  states that the override category exists and can change the pick, which
  is the true, generic claim the source data supports.

## Handoff prompt (BHTF, read aloud)

> "I'm going to hand you a short scoring formula with a few weighted factors
> in it. Before you compute anything, tell me each factor's weight and how
> you'd combine them — before you run the numbers."

Why it's worth running: it doesn't require having the "supplier-selection"
skill installed — any Claude conversation can run it with any short weighted
formula you hand over. Watching Claude narrate the weights and the
combination method before it computes anything generalizes the source's own
handoff idea (the supplier-selection reel's version: "walk me through what
you will do before you do it") so today's viewer can try it without a
custom workshop skill or supplier data.

## Beat-count note (redo)

Source (`claude-liam-supplier-selection`, Teardown) ran 7 beats: B00
(puppet-style `ClaudeComposerAsk` ask), B01 anatomy, B02 pipeline, B03
design-tell, BVDT verdict, BHTF handoff, BOUT outro. This redo runs 9: B00
(writer) absorbs the same stakes-setting job; B01–B02 split the source's B01
anatomy beat into anatomy (B01) and the wrong-guess beat Plain register
requires (B02, not present in the Teardown source, which skips straight to
mechanism); B03 keeps the source's exact weighted-score fact (price 50%,
lead time 30%, reliability 20%) and lets it double as the falsifying case
against the "lowest price wins" guess; B04 is the source's B02 pipeline beat
(normalize → weight → sum, tie-breaks), narration re-registered; B05
compresses the source's B03 design-tell + BVDT verdict into one
both-directions beat with the judgment stripped out (repeatable consistency
stated as fact, not as a design "get right"; the override-notes limit stated
as fact, not as a verdict "bite"). No facts added or dropped — the weighted
formula, the normalize/weight/sum mechanism, the tie-break order, and the
existence of supplier-specific overrides outside the catalog data all carry
over unchanged from the source SKILL.md.
