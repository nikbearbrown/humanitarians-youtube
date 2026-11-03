# Claude, Month Heads Up. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude built the month-heads-up skill itself, writing the cash-flow logic on the fly. It didn't. Claude reads a file someone else wrote and follows it, step by step. What's actually in that file?" | BrutalistHesitantWriter — types "Claude built the month-heads-up skill. Right?", corrects "built" → "reads" |
| B01 | 1 stakes / 2 wrong guess, falsified | Open the month-heads-up folder and there's no hidden script computing the cash-flow numbers. One item sits there: SKILL.md — about two kilobytes of plain language. Claude reads that file itself and treats it as the program. There's nothing else in there to find. | a folder listing opens to exactly one item — SKILL.md — nothing else; the tile highlighted as the program itself |
| B02 | 3 mechanism / **4 anchor planted** | The pipeline lives in the Steps section, and Claude runs it top to bottom — linear, no branching unless a step says so. Ask it for the month check on the 25th with the default 30-day horizon, and it reads the SKILL.md, works through each step in order, and flags what needs attention before month-end. | THE ANCHOR — a request ("month check · 25th · 30-day horizon") goes in, three ordered steps light up in sequence, an output card comes out |
| B03 | **4 anchor payoff / 5 both directions** | Ask for that same 30-day check again, and the answer comes back identical — not because Claude re-examined the cash flow with fresh judgment, but because the exact same steps ran a second time. Switch the horizon to 60 days instead, and the output changes — not because the logic changed, but because a different input ran through those same fixed steps. Identical output on identical input doesn't prove understanding. A different horizon producing different output doesn't prove the logic changed either. | THE ANCHOR RETURNS — the same 30-day request submitted twice, two identical output cards; beside it, a 60-day horizon request producing a different card from the same three steps |
| **BCRY** | **6 carry-out** | A Claude skill isn't code Claude writes on the fly. It's a file someone already wrote, that Claude reads and follows the same way, every single time. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Open the month-heads-up skill folder. Before you run anything, read me the SKILL.md and tell me, in your own words, what steps it says to follow, in order. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Month Heads Up. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder's actual contents as an observable fact; the Steps mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude built this itself); B01 falsifies it with a case — the folder holds exactly one item, SKILL.md, no hidden script anywhere |
| Exactly one inference flag | none needed — every claim is the source's own confirmed statement about how Agent Skills work and about this skill's specific job/horizon parameter; see CARRY-OUT.md |
| One anchor, planted early, paid off late | B02 → B03 (the "month check · 25th · 30-day horizon" request, run through the same three steps, then run again, then with a 60-day horizon) |
| Both directions | B03 — identical output on identical input isn't proof of understanding (same fixed steps repeating); a different horizon producing different output isn't proof the logic changed (same fixed steps, new input) |
| No design judgment | B03 states the determinism fact and its limits, never a verdict on whether the skill's design is good |

## Deliberately not claimed

- **Not how month-heads-up computes a cash-flow outlook.** The source
  states only that Claude reads the Steps section and executes it in
  order — never the arithmetic behind "cash-flow outlook." This reel
  doesn't invent it either.
- **Not a verdict on the design.** The source's B03 framed the same facts
  as "what it gets right" / "what it bites" — Teardown language. Plain
  keeps the facts (folder mechanism, determinism, the horizon parameter)
  but states them without judging whether the design is good.
- **Not that every skill is this simple in practice.** Only that the
  mechanism itself — read the file, run the steps in order, same input
  same output — is what every Agent Skill guarantees.

## Handoff prompt (BHTF, read aloud)

> "Open the month-heads-up skill folder. Before you run anything, read
> me the SKILL.md and tell me, in your own words, what steps it says to
> follow, in order."

Why it's worth running: it forces Claude to surface the actual instruction
set in its own words before acting on it — the same explain-first habit
that makes a deterministic skill auditable rather than a black box.

---
**GATE P — signed:** ______________________  (human)
