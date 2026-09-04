# Claude, Cash Flow Snapshot. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:05.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude built the cash-flow-snapshot skill itself, writing the logic on the fly. It didn't. Claude reads a file someone else wrote and follows it, step by step. What's actually in that file?" | BrutalistHesitantWriter — types "Claude built the cash-flow-snapshot skill. Right?", corrects "built" → "reads" |
| B01 | 1 stakes / 2 wrong guess, falsified | Open the cash-flow-snapshot folder and there's no hidden script waiting to run the real logic. Two items: a SKILL.md file — about six kilobytes of plain language — and a reference folder beside it. Claude reads that SKILL.md itself and treats it as the program. There's nothing else in there to find. | a folder listing opens: SKILL.md (6k) + reference/ — nothing else; the SKILL.md tile highlighted |
| B02 | 3 mechanism / **4 anchor planted** | The pipeline lives in the Steps section, and Claude runs it top to bottom — linear, no branching unless a step says so. Ask it for a cash flow snapshot covering March, and it reads the SKILL.md, works through each step in order, and hands back a snapshot — the same steps, every single time. | THE ANCHOR — a request ("cash flow snapshot · March") goes in, three ordered steps light up in sequence, an output card comes out |
| B03 | **4 anchor payoff / 5 both directions** | Ask for that same March snapshot again, and the answer comes back identical — not because Claude re-examined the numbers with fresh judgment, but because the exact same steps ran a second time. That cuts both ways: identical output on identical input doesn't prove Claude understood anything about cash flow — it only proves the fixed steps repeated. And different output next month, on different numbers, doesn't mean the logic changed either — the same steps just ran on new input. | THE ANCHOR RETURNS — the same request submitted twice, two identical output cards; beside it, a different month's request producing a different card from the same three steps |
| **BCRY** | **6 carry-out** | A Claude skill isn't code Claude writes on the fly. It's a file someone already wrote, that Claude reads and follows the same way, every single time. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Open the cash-flow-snapshot skill folder. Before you run anything, read me the SKILL.md and tell me, in your own words, what steps it says to follow, in order. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Cash Flow Snapshot. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder's actual contents as an observable fact; the Steps mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude built this itself); B01 falsifies it with a case — the folder holds exactly two items, a SKILL.md and a reference folder, no hidden script anywhere |
| Exactly one inference flag | none needed — every claim is the source's own confirmed statement about how Agent Skills work; the one unconfirmed thing (what a snapshot specifically computes) is never asserted, so there is nothing to flag (see CARRY-OUT.md) |
| One anchor, planted early, paid off late | B02 → B03 (the "cash flow snapshot · March" request, submitted, walked through the same three steps, run twice) |
| Both directions | B03 — identical output on identical input isn't proof of understanding (it's the same fixed steps repeating); different output on different input isn't proof the logic changed (same fixed steps, new numbers) |
| No design judgment | B03 states the determinism fact and its limits, never a verdict on whether the skill's design is good |

## Deliberately not claimed

- **Not what a cash flow snapshot specifically computes.** The source's own
  template lost the line naming the skill's exact job (visible in the
  delivered source as a bare `>` at every occurrence). No other copy of
  `cash-flow-snapshot`'s `SKILL.md` exists on this machine to recover it.
  This reel states only the mechanism the source's other beats already
  confirm — folder, SKILL.md, ordered steps, determinism — never the
  snapshot's specific fields or formulas.
- **Not a verdict on the design.** The source's B03 framed the same facts
  as "what it gets right" / "what it bites" — Teardown language. Plain
  keeps the facts (folder mechanism, determinism) but states them without
  judging whether the design is good.
- **Not that every skill is this simple in practice.** Only that the
  mechanism itself — read the file, run the steps in order, same input
  same output — is what every Agent Skill guarantees.

## Handoff prompt (BHTF, read aloud)

> "Open the cash-flow-snapshot skill folder. Before you run anything, read
> me the SKILL.md and tell me, in your own words, what steps it says to
> follow, in order."

Why it's worth running: it forces Claude to surface the actual instruction
set in its own words before acting on it — the same explain-first habit
that makes a deterministic skill auditable rather than a black box.

---
**GATE P — signed:** ______________________  (human)
