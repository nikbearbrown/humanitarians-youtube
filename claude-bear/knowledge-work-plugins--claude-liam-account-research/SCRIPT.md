# Claude, Account Research — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a Teardown `claude-liam` reel). Register: **Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, machine-rendered). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer | "You ask Claude what's going on with an account, and it feels like it should already remember everything about it. It doesn't — it has to go check first. So how does that checking actually work?" | writer types "You ask about an account. Claude must already remember it, right?"; corrects "remember"→"check" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's a reasonable guess — Claude does hold a huge amount of general knowledge. But an account's signals change today: a new hire, a funding round, a product launch. None of that lives in anything Claude was trained on. Answering from memory alone would mean guessing, not researching. | a frozen "trained on" calendar date; today's signals arriving after it, unreachable from memory |
| B02 | 3 mechanism / 4 ANCHOR PLANTED | The fix is a `SKILL.md` file Claude reads before it acts — instructions, not memory. It only fires when your words match its triggers: "research a company," "what's going on with an account," phrases like that. Say "research Acme Corp," and it runs the same three steps every time: read the file, pull the account's signals, return them. | THE ANCHOR — "research Acme Corp" typed, matched against the trigger list, then walked through Read → Execute → Return |
| B03 | 4 ANCHOR PAYOFF / 5 both directions | Run "research Acme Corp" again next week, and Claude walks the same three steps — that's what a written spec buys you: repeatable, not remembered. But phrase it outside the trigger list, some account question the file never anticipated, and the pipeline never starts. You're back to Claude answering from what it already knows — the exact guess we started with. | THE ANCHOR RETURNS — same query, same three steps; then a non-matching question that never enters the pipeline |
| **BCRY** | **6 carry-out** | account-research doesn't make Claude remember your account. It makes Claude follow the same steps to look — only when your words match what it was built to hear. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: "I want to research a company using the account-research skill. Read the skill file and walk me through what you'll do, step by step, before you do it." Watch for two things: does Claude name the exact trigger phrase your words matched, and does it lay out the steps before running them? Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Account Research. Liam, in for Bear. | `OutroCTA` |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the `SKILL.md` mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states "it must already remember"; B01 falsifies it with the dated-signal case — nothing dated today lives in training data |
| Exactly one anchor, planted early, paid off late | B02 → B03 ("research Acme Corp," run twice, same three steps) |
| Both failure directions | B03: matching the triggers gets the pipeline; missing them falls back to memory-only Claude |
| No design judgment | B01–B03 state what the mechanism does and where it stops firing; they never rule on whether the skill's trigger design is a good trade-off |

## Deliberately not claimed

- **Not "Claude has no general knowledge of companies."** It plainly does.
  The point is narrower: that knowledge is frozen at training time, and an
  account's live signals are not — so a research answer needs a lookup, not
  a memory.
- **Not a verdict on the trigger-phrase design.** The source's B03 framed
  the spec as "what it gets right" against "where it bites" — a Teardown
  trade-off judgment. This reel keeps only the mechanism fact: matching
  words run the pipeline, non-matching words don't.
- **No accusation that a missed trigger errors loudly.** The source
  describes no error state for an out-of-spec request; the reel states it
  as the pipeline simply never starting, not as a failure message.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to research a company using the account-research skill. Read the
> skill file and walk me through what you'll do, step by step, before you
> do it."

Why it's worth running: asking Claude to narrate its steps before executing
surfaces whether it actually matched a trigger phrase or is answering from
general knowledge instead — the exact distinction this reel is about.

---
**GATE P — signed:** ______________________  (human)
