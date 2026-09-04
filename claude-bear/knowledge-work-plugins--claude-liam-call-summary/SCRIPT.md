# Claude, Call Summary. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-call-summary`). Register: **Plain**.
7 beats ≈ 1:45. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** `BrutalistHesitantWriter`, free Remotion. **Narrator:** Liam,
Kokoro `am_onyx`.

Redo-mode source: `anthropics/knowledge-work-plugins/youtube/claude-liam-call-summary/beat_sheet.json`
(Teardown register, `claude-liam` / @NikBearBrown, 7 beats). Facts, question,
and beat count kept; register re-written to Plain (no verdict, no design
judgment); B00 replaced with the hesitant-writer cold open; close carries the
Humanitarians AI skin.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Claude doesn't hear your calls — it reads the notes you paste in and writes the summary from those. How does that actually work? Let's open the call-summary skill and look." | Writer types "Claude hears my calls / and writes the summary. / How does that work?", hesitates on "hears", corrects to "reads the notes from" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is called call-summary. Inside is one file — SKILL.md — written in plain language: what to do with call notes or a transcript, and when to do it. Claude reads that file, then acts. | one file, one folder, on cream |
| B02 | pipeline | The instructions are steps, and Claude runs them in order: read the call notes or transcript, pull out the action items, draft the follow-up email, generate the internal summary, then hand back the result. One pass, no branching unless a step says so. | five steps, left to right, arrows between |
| B03 | mechanism / limit | Because the steps are fixed, the same call notes get the same treatment every run — same action-item pull, same email draft, same summary shape. Ask it for something the file doesn't cover — say, booking the follow-up meeting — and there's no instruction for that; call-summary only does what its steps describe. | consistent output chips vs. one chip struck (outside the spec) |
| **BCRY** | carry-out | A skill isn't a new power Claude has — it's a written set of steps. call-summary turns your call notes into the same action items, follow-up email, and summary, every single time. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Paste this into Claude: "Read the call-summary skill and walk me through what you're about to do before you do it. Then use it on these call notes: [paste your notes here] — pull out the action items, draft the follow-up email, and give me the internal summary." That first line matters — watching Claude explain the plan before it runs shows you exactly which step in the skill is doing the work. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Call Summary. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the misconception and the real question; mechanism waits until B02 |
| Wrong guess surfaced *and corrected* | B00's hesitant-writer correction ("hears" → "reads the notes from") — WRONG-GUESS is folded into the cold open per hai-simple's compact redo shape (source has no separate wrong-guess beat to preserve) |
| One anchor | the SKILL.md file itself — named in B01, its behavior traced through B02, its edge named in B03 |
| No judgment | B03 restates the source's Teardown "what it gets right / what it bites" as a plain behavioral fact (consistency, and an unstated case) — no ruling on whether that design choice is good |
| Carry-out | compresses "skill = instructions, not a new power" plus the concrete, checkable behavior — not a topic summary |
| Host handoff | B00 narrator (Liam) is distinct from the wrong-guess "voice" of the typed, then-corrected text |

## Deliberately not claimed

- **No new capability claim.** The reel never says or implies Claude can
  listen to, dial, or transcribe a call — only that it processes text you
  already have (notes or a transcript).
- **No verdict on the skill's design.** The source's Teardown line ("What it
  gets right... what it bites") is a design judgment; Plain keeps the
  underlying fact (fixed steps → consistent output; uncovered requests aren't
  improvised around) without ruling on whether that's a good trade-off.

## Beat-count note

Source is 7 beats (B00 host ask, B01 anatomy, B02 pipeline, B03 design tell,
BVDT verdict, BHTF your-turn, BOUT outro). Per the redo contract, beat count
and facts are kept: B00 → hesitant writer, BVDT → BCRY (carry-out, judgment
stripped), BHTF/BOUT kept with the Humanitarians AI skin. Total: 7 beats.

## Handoff prompt (BHTF, read aloud)

> "Read the call-summary skill and walk me through what you're about to do
> before you do it. Then use it on these call notes: [paste your notes here]
> — pull out the action items, draft the follow-up email, and give me the
> internal summary."

---
**GATE P — signed:** unattended build, 2026-09-02.
