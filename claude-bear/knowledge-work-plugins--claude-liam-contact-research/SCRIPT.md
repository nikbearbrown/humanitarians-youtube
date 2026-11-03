# Claude, Contact Research — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a Teardown `claude-liam` reel). Register: **Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, machine-rendered). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer | "You ask Claude about a specific person, and it feels like it should already know everything about them. It doesn't — it has to go look them up first. So how does that lookup actually work?" | writer types "You ask about a person. Claude must already know them, right?"; corrects "know"→"look up" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's a reasonable guess — Claude does hold a lot of general knowledge about people. But whether someone's a warm lead right now depends on today's signals: a recent reply, a meeting booked, a title change. None of that lives in anything Claude was trained on. Answering from memory alone would mean guessing, not researching. | a frozen "trained on" calendar date; today's signals arriving after it, unreachable from memory |
| B02 | 3 mechanism / 4 ANCHOR PLANTED | The fix is `contact-research`, a `SKILL.md` file Claude reads before it acts — instructions, not memory. It only fires when your words match its triggers: "who is this person," "is this person a warm lead," phrases like that. Say "who is Jane Doe at Acme," and it runs the same three steps every time: read the file, pull the contact's Common Room signals, return them. | THE ANCHOR — "who is Jane Doe at Acme" typed, matched against the trigger list, then walked through Read → Execute → Return |
| B03 | 4 ANCHOR PAYOFF / 5 both directions | Run "who is Jane Doe at Acme" again next month, and Claude walks the same three steps — that's what a written spec buys you: repeatable, not remembered. But phrase it outside the trigger list, some open-ended question about a person the file never anticipated, and the pipeline never starts. You're back to Claude answering from what it already knows — the exact guess we started with. | THE ANCHOR RETURNS — same query, same three steps; then a non-matching question that never enters the pipeline |
| **BCRY** | **6 carry-out** | contact-research doesn't make Claude know a person. It makes Claude look them up, the same way every time — only when your words match what it was built to hear. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: "I want to research a specific person using Common Room data. Read the contact-research skill and walk me through what you'll do, step by step, before you do it." Watch for two things: does Claude name the exact trigger phrase your words matched, and does it lay out the steps before running them? Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Contact Research. Liam, in for Bear. | `OutroCTA` |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the `SKILL.md` mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states "it must already know them"; B01 falsifies it with the dated-signal case — nothing dated today lives in training data |
| Exactly one anchor, planted early, paid off late | B02 → B03 ("who is Jane Doe at Acme," run twice, same three steps) |
| Both failure directions | B03: matching the triggers gets the pipeline; missing them falls back to memory-only Claude |
| No design judgment | B01–B03 state what the mechanism does and where it stops firing; they never rule on whether the skill's trigger design is a good trade-off |

## Deliberately not claimed

- **Not "Claude has no general knowledge of people."** It plainly does, for
  public or well-documented figures. The point is narrower: that knowledge
  is frozen at training time, and a contact's live signals are not — so a
  research answer needs a lookup, not a memory.
- **Not a verdict on the trigger-phrase design.** The source's B03 called
  the trigger spec "the interesting constraint" and quoted "what it gets
  right" against "what it bites" — a Teardown trade-off judgment. This reel
  keeps only the mechanism fact: matching words run the pipeline,
  non-matching words don't.
- **No accusation that a missed trigger errors loudly.** The source
  describes no error state for an out-of-spec request; the reel states it
  as the pipeline simply never starting, not as a failure message.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to research a specific person using Common Room data. Read the
> contact-research skill and walk me through what you'll do, step by step,
> before you do it."

Why it's worth running: asking Claude to narrate its steps before executing
surfaces whether it actually matched a trigger phrase or is answering from
general knowledge instead — the exact distinction this reel is about.

---
**GATE P — signed:** ______________________  (human)
