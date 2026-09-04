# Claude, Mining — Narration Script (Plain register)

*Skill: `hai-simple`, mode `redo`. Register: **Plain**. 9 beats ≈ 2:10.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (hai-simple WRITER LAW — no puppet, no
human step). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "You'd guess Claude just knows Minecraft trivia — that a skill means built-in knowledge. It doesn't. It reads a file. So what's actually happening when Claude reads a skill?" | Writer types "Claude just knows / where diamonds spawn / in Minecraft 1.20, / right?" — hesitates on "knows", corrects to "reads" |
| B01 | 1 stakes + anatomy | A Claude "skill" is a folder Claude checks before it acts. This one is called mining. Open it up, and there's exactly one file inside: SKILL.md. | folder `mining/`, one file `SKILL.md`, chip "1 FILE" |
| B02 | 2 wrong guess | The natural guess is that Claude already knows this — trained on years of Minecraft guides somewhere in there — and the skill just gives it permission to say so. | the "trained on it" reading, sold as reasonable |
| B03 | **2 break it / 4 anchor planted** | Open SKILL.md and there's no permission, no reasoning, no guide to cross-reference — one sentence. "Where diamonds spawn in Minecraft 1.20." That's the entire file. | THE ANCHOR — SKILL.md, one line of text, nothing else |
| B04 | 3 mechanism | Claude reads that sentence, then acts on it directly — no branching, no extra steps invented along the way. Read the instruction, follow it, hand back the answer. | READ → FOLLOW → ANSWER, linear |
| B05 | **4 anchor payoff / 5 both directions** | Ask twice and you get the identical answer both times — that consistency is real. But ask about Minecraft 1.21 instead, or emeralds instead of diamonds, and there's nothing left to reach for. The file only ever said the one thing. | THE ANCHOR RETURNS — same SKILL.md line; "same question → same answer" beside "different question → nothing extra" |
| **BCRY** | **6 carry-out** | A Claude skill isn't Claude knowing more. It's Claude reading one short file, right before it answers — and it can't answer past what that file says. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: "I'm going to hand you a short instruction file. Before you use it, tell me exactly what you'll read in it, and what you'll do with what's inside — before you act." Watching it explain first is how you see the constraint for yourself. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Mining. Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the "already trained on it" read; B03 breaks it by opening the actual file and finding one sentence |
| Exactly one inference flag | None — direct, confirmed mechanism throughout (this is how Claude Skills work, not an inference about Claude); `one_flag: "N/A"` in metadata |
| One anchor, planted early, paid off late | B03 → B05 (the single sentence inside SKILL.md) |
| Both failure directions | B05: same-question consistency (positive) vs. different-question emptiness (negative) |
| No design judgment | B02–B03 describe why the wrong guess fails; nothing rules on whether "mining" is a *well-built* skill (the source's Popper/Plato lens moves and verdict language are dropped — Plain explains and stops) |

## Deliberately not claimed

- **Not "Claude has no knowledge at all."** The reel's claim is narrower and
  true: *this specific skill's answer* comes from the one sentence in its
  SKILL.md, not from general training recall. It never claims Claude is
  otherwise ignorant of Minecraft.
- **Not a verdict on whether "mining" is a good skill.** The source
  (Teardown register) ran a Popper move ("what it bites: anything outside
  the spec") and a Plato move (artifact vs. world) as design judgment. Plain
  register keeps the same facts — the file is short, the answer only covers
  what's written — without ruling on whether that's a good or bad way to
  build a skill.
- **No claim that every Claude Skill is one sentence.** "Mining" is used
  because it's the source's actual example and it makes the point vividly;
  the reel doesn't generalize to "skills are always this small."

## Handoff prompt (BHTF, read aloud)

> "I'm going to hand you a short instruction file. Before you use it, tell
> me exactly what you'll read in it, and what you'll do with what's inside —
> before you act."

Why it's worth running: it doesn't require having the "mining" skill
installed — any Claude conversation can run it with any short instruction
you hand over. Watching Claude narrate what it will read and do, before it
does it, is the source's own handoff idea (the mining reel's version: "walk
me through what you will do before you do it"), generalized so today's
viewer can try it without a custom workshop skill.

## Beat-count note (redo)

Source (`claude-liam-mining`, Teardown) ran 7 beats: B00 (puppet-style
`ClaudeComposerAsk` ask), B01 anatomy, B02 pipeline, B03 design-tell, BVDT
verdict, BHTF handoff, BOUT outro. This redo runs 9: B00 (writer) absorbs the
same stakes-setting job; B01–B02 split the source's B01 anatomy beat into
anatomy (B01) and the wrong-guess beat Plain register requires (B02, not
present in the Teardown source, which skips straight to mechanism); B03
keeps the source's exact one-sentence anchor fact and lets it double as the
falsifying case; B04 is the source's B02 pipeline beat, narration
re-registered; B05 compresses the source's B03 design-tell + BVDT verdict
into one both-directions beat with the judgment stripped out (repeatable
consistency stated as fact, not as a design "get right"; the spec limit
stated as fact, not as a verdict "bite"). No facts added or dropped — the
one-sentence SKILL.md content, the read-then-act mechanism, and the
same-input/same-output limit all carry over unchanged.
