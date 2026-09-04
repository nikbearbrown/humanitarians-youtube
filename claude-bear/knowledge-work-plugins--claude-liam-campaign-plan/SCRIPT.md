# Claude, Campaign Plan — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a Teardown `claude-liam` reel). Register: **Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, machine-rendered). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer | "You ask Claude for a campaign plan, and it's tempting to picture it inventing a strategy from nothing. It doesn't — it assembles one, from a fixed set of written steps. What's actually in that file?" | writer types "You ask for a campaign plan. Claude must invent the whole strategy, right?"; corrects "invent"→"assemble" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's a fair guess — Claude can talk marketing strategy in general. But ask it for a campaign plan twice, for two completely different products, and the same six pieces come back every time: objectives, audience, messaging, channel strategy, a content calendar, and success metrics. That's not improvisation. That's a spec being filled in. | two different product requests produce the identical six-piece shape, side by side |
| B02 | 3 mechanism / 4 ANCHOR PLANTED | The fix is one file: `SKILL.md`. It's the whole instruction set — one page telling Claude to produce exactly those six pieces, and naming exactly when to fire: a product launch, a lead-generation push, an awareness campaign, or a request for a week-by-week content calendar. Say "plan a launch campaign for a new fitness app," and it matches, reads the file top to bottom, and executes each step in order. | THE ANCHOR — the request typed, matched against the trigger list, then walked through Read → Execute → Return |
| B03 | 4 ANCHOR PAYOFF / 5 both directions | Ask that same thing again next month, and Claude walks the same file, in the same order — the six pieces come back again. That's the payoff of a written spec: repeatable, not reinvented. But ask something the file never named — say, "write one tweet for this product" — and the trigger never matches. The pipeline doesn't start; you get whatever Claude would say without the skill at all. | THE ANCHOR RETURNS — same query, same three steps; then a non-matching request that never enters the pipeline |
| **BCRY** | **6 carry-out** | campaign-plan doesn't make Claude a strategist. It makes Claude fill six fixed slots, the same way, every time your words match what the file was built to hear. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: "I want a campaign plan for a product I'm describing to you now. Read the campaign-plan skill and walk me through what you'll do, step by step, before you do it." Watch for two things: does Claude name the six pieces before writing them, and does it match your request to one of its own stated triggers? Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Campaign Plan. Liam, in for Bear. | `OutroCTA` |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the `SKILL.md` mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states "Claude must invent the whole strategy"; B01 falsifies it with the same-shape case — two unrelated products, identical six-piece output |
| Exactly one anchor, planted early, paid off late | B02 → B03 ("plan a launch campaign for a new fitness app," run twice, same three steps) |
| Both failure directions | B03: matching the triggers gets the six-piece pipeline; missing them falls back to Claude answering without the skill |
| No design judgment | B01–B03 state what the mechanism does and where it stops firing; they never rule on whether the skill's trigger design is a good trade-off |

## Deliberately not claimed

- **Not "Claude has no marketing knowledge."** It plainly can discuss
  strategy generally. The point is narrower: the skill's deliverable shape
  is fixed by the file, not chosen fresh by creative judgment each time.
- **Not a verdict on the trigger-phrase design.** The source's B03 framed
  the spec as "what it gets right" against "where it bites" — a Teardown
  trade-off judgment. This reel keeps only the mechanism fact: matching
  words run the pipeline, non-matching words don't.
- **No accusation that a missed trigger errors loudly.** The source
  describes no error state for an out-of-spec request; the reel states it
  as the pipeline simply never starting, not as a failure message.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want a campaign plan for a product I'm describing to you now. Read the
> campaign-plan skill and walk me through what you'll do, step by step,
> before you do it."

Why it's worth running: asking Claude to narrate its steps before executing
surfaces whether it actually matched a trigger phrase and named the fixed
six-piece deliverable, or is answering from general marketing knowledge
instead — the exact distinction this reel is about.

---
**GATE P — signed:** ______________________  (human)
