# Claude, Create Cowork Plugin. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet — see
QUESTION.md "Source defect found, and NOT repeated here"). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks Claude to create a plugin, expecting it to just make one on the spot. It doesn't — first it plans. So what actually happens before Claude writes a single file?" | BrutalistHesitantWriter — types "Ask Claude to create a plugin — does it just make it?", corrects "make" → "plan" |
| B01 | 1 stakes / 2 wrong guess, falsified / 4 anchor planted | Ask for a new plugin — say, one that onboards new hires — and Claude doesn't start writing files. It runs five phases in order: Discovery, Component Planning, Design, Implementation, then Review and Package. Discovery comes first: what should this plugin do, and who's going to use it. | THE ANCHOR — five phase cards draw in left to right; only Phase 1 lights up, the onboarding-plugin example typing in beneath it; the other four stay blank |
| B02 | 3 mechanism | Next it plans components: does the plugin need a skill for know-how, an MCP server for an outside tool, an agent for a multi-step task, a hook that fires on its own? For the onboarding plugin, that means one skill for the checklist and a connector to the HR system — laid out in a table, waiting on your confirmation. | a four-row component table (Skill / MCP / Agent / Hook); Skill and MCP get a check, Agent and Hook get a faint cross; the table sits boxed, waiting |
| B03 | 4 anchor payoff / 5 both directions | Only after you confirm that plan does Implementation start — every file gets written in one pass, matching exactly what was agreed. Say "whatever you think is best" instead of choosing, and Claude doesn't stall — it gives a specific recommendation and still waits for your yes before writing anything. Either way, the onboarding plugin exists as a file only once you've said go. | THE ANCHOR RETURNS — the five-phase row from B01, now with checks through phase 3; file icons appear ONLY at phase 4; a second branch shows a recommendation card popping up before the same gate opens |
| **BCRY** | **6 carry-out** | Ask Claude to create a plugin, and it doesn't just write one — it walks five phases first, and nothing gets built until you've confirmed the plan. | the sentence, alone, serif, large |
| BHTF | handoff (generalized — see QUESTION.md) | Your turn. Here's the prompt — read it with me. Ask Claude to build you something you actually want — a plugin, a script, a short doc. Before it writes anything, ask it to lay out its plan in phases and wait for your yes. Then watch: does it ask real questions, or does it just guess and go? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Create Cowork Plugin. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the five-phase order before B02's component-by-component detail |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude just makes it); B01 falsifies it directly — five phases run first, nothing written yet |
| Exactly one inference flag | none needed — every mechanism claim (five phases, four component types, Implementation is phase 4, "don't assume industry-standard defaults," the "whatever's best" exception) is read directly off the real `SKILL.md`, verified present in this workspace; the onboarding-plugin scenario is flagged in QUESTION.md/CARRY-OUT.md as an illustrative anchor, not a source claim |
| One anchor, planted early, paid off late | B01 → B03 (the five-phase row, planted with the onboarding-plugin example, paid off showing the confirm-before-build gate and its one flip) |
| Both directions | B03 — confirm the plan and Implementation matches it exactly (holds); say "whatever's best" instead and Claude still won't guess silently, it recommends and still waits for a yes (flips the who's-deciding, not the gate itself) |
| No design judgment | B03 states phase order and the confirm gate as facts about sequencing, never a verdict on whether five phases of questions is the right amount of friction |

## Deliberately not claimed

- **Not a design verdict.** The source's B03/BVDT framed "what it gets
  right" / "where it bites" as Teardown judgment on the skill's design.
  Plain keeps the same underlying mechanism (nothing built until confirmed)
  as a sequencing fact, not a critique.
- **Not that Claude ever refuses to guess.** The "whatever you think is
  best" exception is stated exactly as the real SKILL.md states it: Claude
  gives a specific recommendation, but the confirm-before-build gate still
  applies — it never silently builds on a guess.
- **Not a real onboarding plugin's actual contents.** The onboarding-plugin
  example is this reel's invented anchor, chosen to make the five phases
  and the confirm gate concrete and visualizable — not a claim about what
  Claude would actually produce for that request.

## Handoff prompt (BHTF, read aloud)

> "Before you build anything I ask for, lay out your plan in phases first
> and wait for my yes before writing a single file."

Why it's generalized: `create-cowork-plugin` requires the Cowork desktop
app specifically (its own `compatibility` field says so), which a general
viewer may not have open. The same lesson — plan first, confirm, then
build — runs on any Claude surface a viewer actually has.

---
**GATE P — signed:** ______________________  (human)
