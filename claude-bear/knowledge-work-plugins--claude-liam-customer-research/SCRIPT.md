# Claude, Customer Research. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-customer-research`). Register:
**Plain**. 7 beats ≈ 1:45. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** `BrutalistHesitantWriter`, free Remotion. **Narrator:** Liam,
Kokoro `am_onyx`.

Redo-mode source:
`anthropics/knowledge-work-plugins/youtube/claude-liam-customer-research/beat_sheet.json`
(Teardown register, `claude-liam` / @NikBearBrown, 7 beats). Facts, question,
and beat count kept; register re-written to Plain (no verdict, no design
judgment); B00 replaced with the hesitant-writer cold open; close carries the
Humanitarians AI skin.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Claude doesn't already know your customer — it looks up sources you give it and attributes what it finds. How does that actually work? Let's open the customer-research skill and look." | Writer types "Claude already knows my customer. / How does that work?", hesitates on "knows", corrects to "looks up sources for" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is called customer-research. Inside is one file — SKILL.md — written in plain language: multi-source research on a customer question, with source attribution. Claude reads that file, then acts. | one file, one folder, on cream |
| B02 | pipeline | The instructions are steps, and Claude runs them in order: read the SKILL.md, execute each step as written, then return the output. One pass, no branching unless a step says so. | three phases, left to right, arrows between |
| B03 | mechanism / limit | Because the steps are fixed, the same customer question gets the same treatment every run — pull sources, attribute them, hand back the findings. Ask it to skip the sources and just guess, and there's no instruction for that; customer-research only does what its steps describe. | consistent output chips vs. one chip struck (outside the spec) |
| **BCRY** | carry-out | A skill isn't a new power Claude has — it's a written set of steps. customer-research turns your question into the same multi-source, attributed findings, every single time. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Paste this into Claude: "Read the customer-research skill and walk me through what you're about to do before you do it. Then use it on this: [paste the customer's question here] — research it across the sources I've given you, and attribute what you find." That first line matters — watching Claude explain the plan before it runs shows you exactly which step in the skill is doing the work. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Customer Research. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the misconception and the real question; mechanism waits until B02 |
| Wrong guess surfaced *and corrected* | B00's hesitant-writer correction ("knows" → "looks up sources for") — WRONG-GUESS is folded into the cold open per hai-simple's compact redo shape (source has no separate wrong-guess beat to preserve) |
| One anchor | the SKILL.md file itself — named in B01, its behavior traced through B02, its edge named in B03 |
| No judgment | B03 restates the source's Teardown "what it gets right / what it bites" as a plain behavioral fact (consistency, and an unstated case) — no ruling on whether that design choice is good |
| Carry-out | compresses "skill = instructions, not a new power" plus the concrete, checkable behavior — not a topic summary |
| Host handoff | B00 narrator (Liam) is distinct from the wrong-guess "voice" of the typed, then-corrected text |

## Deliberately not claimed

- **No new capability claim.** The reel never says or implies Claude already
  knows or remembers anything about a customer — only that it looks up and
  attributes sources you provide it.
- **No verdict on the skill's design.** The source's Teardown line ("What it
  gets right... what it bites") is a design judgment; Plain keeps the
  underlying fact (fixed steps → consistent output; uncovered requests
  aren't improvised around) without ruling on whether that's a good
  trade-off.

## Beat-count note

Source is 7 beats (B00 host ask, B01 anatomy, B02 pipeline, B03 design tell,
BVDT verdict, BHTF your-turn, BOUT outro). Per the redo contract, beat count
and facts are kept: B00 → hesitant writer, BVDT → BCRY (carry-out, judgment
stripped), BHTF/BOUT kept with the Humanitarians AI skin. Total: 7 beats.

## Handoff prompt (BHTF, read aloud)

> "Read the customer-research skill and walk me through what you're about to
> do before you do it. Then use it on this: [paste the customer's question
> here] — research it across the sources I've given you, and attribute what
> you find."

---
**GATE P — signed:** unattended build, 2026-09-03.
