# Claude, Buyer List. — Narration Script (hai-simple redo)

*Skill: `hai-simple`. Redo of `claude-liam-buyer-list` (Teardown, @NikBearBrown) into
the Plain register for @HumanitariansAI. Register: **Plain** — explain, then stop.
Narrator: Liam, Kokoro `am_onyx`. Cold open: `BrutalistHesitantWriter` (no puppet, no
paid step). 7 beats, matching the source's 7.*

**Source (locked facts):** `/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-buyer-list/beat_sheet.json`
— a Teardown-register skill showcase of `buyer-list`, an Anthropic-style Claude Skill
(a `SKILL.md` folder) that builds and organizes a universe of potential acquirers for
sell-side M&A: identifies strategic and financial buyers, assesses fit, and prioritizes
outreach. Triggers on "buyer list", "buyer universe", "potential acquirers", "who would
buy this", "strategic buyers", "financial sponsors".

**What changes in this redo:** the cold open becomes the hesitant writer (was
`ClaudeComposerAsk`); the Teardown "design tell" beat (verdict language — "what it gets
right" / "what it bites") is rewritten as a plain mechanism-and-scope statement; the
verdict beat becomes the carry-out line; the outro takes the Humanitarians AI skin
(`OutroSeries`, not the locked `ClaudeTitleOutro`). The facts about the skill — what it
does, how a Skill folder executes — are unchanged.

## The question, corrected

Naive framing: "How does the buyer-list **app** find buyers?" — the wrong word is
"app": it implies an autonomous program that goes and hunts for buyers on its own.
Corrected word: "**skill**" — a written set of instructions Claude reads and follows,
not an independent agent. Final question: **"How does the buyer-list skill find
buyers?"**

## Carry-out (written first, per CARRY-OUT LAW)

> A Skill doesn't make Claude smarter — it makes Claude follow your steps, in order,
> every time.

Test: repeatable by someone half-listening in a meeting next week, still true. It
compresses the distinction (instruction-following vs. autonomous intelligence), not
the topic (buyer-list itself).

## Beats

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask how the buyer-list app finds buyers on its own. It's not an app — it's a skill, a folder of instructions Claude reads first. So: how does the buyer-list skill find buyers?" | `BrutalistHesitantWriter`, humanitarians ink/accent/bg — types "app", reconsiders, replaces with "skill" |
| B01 | anatomy | "A skill is a folder Claude reads before it works. This one is buyer-list. The SKILL.md contains the full instruction set — plain language, no hidden logic. Claude reads it, then acts. The file is the program." | `SkillTeardownAnatomy` — one file, SKILL.md, accented |
| B02 | pipeline | "The pipeline is in the Steps section. Claude reads each step in order and executes it. Linear — no branching unless the step says so." | `SkillTeardownPipeline` — read → execute → return |
| B03 | mechanism + scope (no verdict) | "buyer-list is a specification written as an instruction set: build and organize a universe of potential acquirers for sell-side M&A, spot strategic and financial buyers, and prioritize outreach. Because Claude follows exactly what's written, the result is the same every run — and it only covers what the page says." | `SkillTeardownMechanism` — heading + body, no verdict pill |
| **BCRY** | carry-out | "A Skill doesn't make Claude smarter — it makes Claude follow your steps, in order, every time." | `WantQuote` — the sentence, alone |
| BHTF | Your Turn | "Your turn. Paste this into Claude: 'Explain what a Claude Skill is — then, if I wrote a three-step SKILL.md for making coffee, walk me through exactly how you'd read and follow it, step by step, before you start.' Watching it name the steps before it starts is what shows you the mechanism is real." | `ClaudeComposerAsk` — the paste-ready prompt |
| BOUT | outro (HAI skin) | "Claude, Buyer List. Liam, in for Bear." | `OutroSeries` — @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states mechanism (follows exactly what's written) and scope (only what the page says) as fact, not a trade-off verdict — the source's "what it gets right / what it bites" language is removed |
| Facts unchanged | buyer-list's stated job, trigger phrases, anatomy, and pipeline are verbatim from the source's SKILL.md description |
| Carry-out | Written first; compresses the instruction-following-vs-autonomy distinction, not the buyer-list topic |
| Host handoff | B00 names the mechanism it's about to explain and hands off implicitly to the body (Liam narrates throughout — no puppet) |
| No AI-video / no pantry | Every beat is REMOTION (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`, `WantQuote`, `ClaudeComposerAsk`, `OutroSeries`) |

## Handoff prompt (BHTF, read aloud)

> "Explain what a Claude Skill is — then, if I wrote a three-step SKILL.md for making
> coffee, walk me through exactly how you'd read and follow it, step by step, before
> you start."

Why it's worth running: it's generically runnable by anyone with Claude, without the
proprietary buyer-list SKILL.md — and watching Claude name its steps before acting is
the same mechanism the reel just showed.

## Known template limitation (logged, not a blocker)

`OutroSeries`/`OutroCTA` (the registered Humanitarians AI outro components) import
`tokens/vox` (teardown: white/near-black/crimson) with no palette-override props; no
registered scene imports `tokens/humanitarians.ts`. `BrutalistHesitantWriter` (B00) DOES
expose `ink`/`accent`/`bg` overrides and is built with the true humanitarians hex
values. `SkillTeardownAnatomy`/`Pipeline`/`Mechanism` and `WantQuote` hardcode the
Claude palette internally (no override props) — the best registered library match per
GATE L; no humanitarians-retinted alternative exists. See BUILD-LOG.md.
