# Claude, Cowork Plugin Customizer. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet, itself an
unfinished batch build — see QUESTION.md "Source defect found and
handled"). Register: **Plain**. 7 beats ≈ 1:45.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes cowork-plugin-customizer is a plugin Claude installs, like an app. It isn't — it's a skill folder Claude actually reads. So what does reading it, instead of installing it, really mean?" | BrutalistHesitantWriter — types "Is cowork-plugin-customizer a plugin that Claude installs?", corrects "installs" → "reads" |
| B01 | 1 stakes / 2 wrong guess, falsified / 4 anchor planted | A Claude Skill is a folder, not an installed program. Inside, a file named SKILL.md — plain-language instructions, no hidden binary. Claude opens that file before it does anything else. cowork-plugin-customizer is one such folder: its whole job, written in one line inside that file, is to customize a Claude Code plugin for one organization's tools. | THE ANCHOR — a folder opening to reveal SKILL.md, the one job-line typing itself out |
| B02 | 3 mechanism | Reading it is only step one. Claude then works through whatever Steps section the file lays out, top to bottom, in order — no branching unless a step explicitly says so. For cowork-plugin-customizer, that means the same request runs the same sequence every time; nothing about what happens in between is left to guesswork. | a numbered Steps list drawing in top to bottom, a loop arrow marked "same request, same order" |
| B03 | 4 anchor payoff / 5 both directions | That's the guarantee: read the file, and you can predict the run before it starts, because the steps are sitting right there in plain language. But the guarantee only covers what's written. Ask for something the Steps section never anticipated, and Claude isn't wrong to attempt it — it just isn't following cowork-plugin-customizer anymore. It's using its own judgment, off the map the file drew. | THE ANCHOR RETURNS — the SKILL.md job-line reappears inside its steps, then a request steps off the edge of the drawn steps into open, unmarked space |
| **BCRY** | **6 carry-out** | A Skill isn't installed software — it's a file Claude reads before it acts. Same request gets the same steps every time, but only for what that file actually wrote down. | the sentence, alone, serif, large |
| BHTF | handoff (generalized — see QUESTION.md) | Your turn. Here's the prompt — read it with me. Pick any Skill you have — one of Claude's built-ins, or one from a plugin — and ask: open this skill's SKILL.md, and walk me through the exact steps you'll take, in order, before you run it. Then run it, and check whether it followed the order it just showed you. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Cowork Plugin Customizer. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder/file split before B02's step-by-step pipeline |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (installed plugin); B01 falsifies it directly — it's a folder Claude reads |
| Exactly one inference flag | none needed — every claim is read directly off the source's own unmasked text (the one job-line, "folder/SKILL.md," "Steps run in order") or is a generic, accurate description of how Claude Skills work; nothing behind the source's unfilled `>` placeholders is guessed at |
| One anchor, planted early, paid off late | B01 → B03 (cowork-plugin-customizer's stated job-line, planted inside the folder/file reveal, paid off by showing the same line still governs the steps — and where a request can step past them) |
| Both directions | B03 — reading the file lets you predict the run when the request stays inside the Steps section (holds); a request outside that section doesn't error, it just switches Claude over to its own general judgment (flips) |
| No design judgment | B03 states the scope boundary as a fact about how Skills work, never a verdict on whether cowork-plugin-customizer's SKILL.md should cover more |

## Deliberately not claimed

- **Not what cowork-plugin-customizer specifically does, step by step.**
  The source left this behind four unfilled `>` placeholders (B00, B03,
  BVDT, BHTF) and the real SKILL.md lives only on a machine this workspace
  can't reach (see QUESTION.md). The one fact the source states outright —
  "customize a Claude Code plugin for a specific organization's tools" — is
  the anchor; how it does that is never guessed at.
- **Not a verdict on the design.** The source's B03/BVDT framed "what it
  gets right" / "where it bites" as Teardown judgment. Plain keeps the same
  underlying fact (repeatable inside scope, hands off outside it) as a
  mechanism boundary, not a critique.
- **Not that going past the file's scope is a failure.** B03 states plainly
  that Claude doesn't break or refuse past the Steps section — it switches
  to general judgment, a different mode, not an error.

## Handoff prompt (BHTF, read aloud)

> "Open this skill's SKILL.md, and walk me through the exact steps you'll
> take, in order, before you run it."

Why it's generalized: the source's own Your Turn task named
`cowork-plugin-customizer` by name and asked the viewer to invoke it — but
that skill exists only in a private book on Bear's machine, not anywhere a
viewer could reach. Pointing the same move (read the file, predict the run,
then check the prediction) at *any* Skill the viewer actually has keeps the
lesson runnable for a general audience instead of asking them to run
something that doesn't exist for them.

---
**GATE P — signed:** ______________________  (human)
