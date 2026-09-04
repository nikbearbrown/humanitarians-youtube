# Claude, Equity Research. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Ask Claude to do equity research, and it's easy to picture a trained analyst inside the model. It isn't — it's a written file Claude reads before acting. Liam explains what that file does." | BrutalistHesitantWriter — types "Ask Claude for equity research — is that a trained analyst inside it?", corrects "trained analyst" → "written file" |
| B01 | 1 stakes / 2 wrong guess, falsified | A Claude Skill is a folder Claude reads before it works — not a specialized model, not extra training. This one is called equity-research, and it's one file: a SKILL.md written in plain language, telling Claude to combine analyst consensus estimates, company fundamentals, historical prices, and macro context into a research snapshot. | an `equity-research` folder holding one file, `SKILL.md`; an arrow to four source chips — consensus estimates, fundamentals, historical prices, macro context |
| B02 | 3 mechanism / **4 anchor planted** | Here's the concrete case: ask Claude to research one company. It opens the SKILL.md and runs the steps in order — pull the analyst consensus estimates, pull the fundamentals, pull the historical prices, pull the macro context — then assembles all four into one snapshot and hands it back. Same steps, every time, for any company you name. | THE ANCHOR — a request card into SKILL.md; four step-cards light up teal in sequence; arrows converge into one "snapshot" card |
| B03 | **4 anchor payoff / 5 both directions** | Ask that same skill a different kind of question — should you buy the stock — and nothing happens, because no step says to answer that. That's not Claude refusing to think; it's this file not covering it. And the reverse holds too: a clean snapshot doesn't mean the numbers were checked or judged — the file only assembled what its steps say to pull. | a "should I buy it?" card into SKILL.md, a dashed line to an empty card labelled "no step written for it"; below, a "clean snapshot" card beside a struck-through "checked? judged?" |
| **BCRY** | **6 carry-out** | Equity-research isn't a trained analyst inside Claude — it's a written file of steps, and Claude only runs the steps that are written down. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want a comprehensive equity research snapshot for a company I follow — combining analyst consensus estimates, fundamentals, historical prices, and macro context. Read the equity-research skill first, and walk me through what you'll do before you do it. Watch whether it names each step before running — that's the file doing the deciding, not a hidden judgment call. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Equity Research. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states what the skill is and its purpose; the four-step run-through waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (a trained analyst inside the model); B01 falsifies it directly — one plain-language file, no separate training |
| Exactly one inference flag | none needed — every claim is read directly off the source's own stated purpose and pipeline description, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (ask Claude to research one company; the same file, asked a question its steps don't cover) |
| Both directions | B03 — a question outside the file's steps goes unanswered, but that's not Claude "can't" (flips: it's this file not covering it); a clean snapshot doesn't prove the numbers were checked or judged (the positive case doesn't prove more than it does) |
| No design judgment | B03 states the boundary and the assembled-not-verified fact as mechanism, never a verdict on whether the skill file should do more |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed this as "what
  it gets right: repeatable results. What it bites: anything outside the
  spec" — Teardown language. Plain keeps the same underlying facts
  (repeatable because it's a spec; bounded to what the spec says) but
  states them as mechanism boundaries, not a critique of the skill file.
- **Not a specific company, estimate, or price.** The source narration
  never names one, and neither does this reel — the anchor shows what
  runs, not what number comes back.
- **No claim that Claude in general can't reason about valuation
  questions.** B03 is explicit that the boundary is this file's steps, not
  Claude's general capability.

## Handoff prompt (BHTF, read aloud)

> "I want a comprehensive equity research snapshot for a company I follow
> — combining analyst consensus estimates, fundamentals, historical
> prices, and macro context. Read the equity-research skill first, and
> walk me through what you'll do before you do it."

Why it's worth running: watching Claude name each step — pull consensus
estimates, pull fundamentals, pull historical prices, pull macro context —
before it runs any of them shows the file doing the deciding, the same
split B01–B03 walk through.

---
**GATE P — signed:** ______________________  (human)
