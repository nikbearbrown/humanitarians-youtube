# Claude, Reorder Policy — Narration Script (Plain register)

*Skill: `hai-simple`, mode `redo`. Register: **Plain**. 9 beats ≈ 2:05.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (hai-simple WRITER LAW — no puppet, no
human step). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "You'd guess Claude just knows how much stock to reorder — that it's making a judgment call. It isn't. It's following a written rule. So what's actually happening when Claude recommends a reorder?" | Writer types "Claude just knows / how much stock / to reorder, / right?" — hesitates on "knows", corrects to "follows" |
| B01 | 1 stakes + anatomy | A Claude "skill" is a folder Claude reads before it acts. This one is called reorder-policy. Open it up, and there's one file inside: SKILL.md — plain language, no hidden logic. | folder `reorder-policy/`, one file `SKILL.md`, chip "1 FILE" |
| B02 | 2 wrong guess | The natural guess is that Claude is weighing this the way a person would — supplier trust, seasonal demand, gut feel about the market — and deciding case by case. | the "judgment call" reading, sold as reasonable |
| B03 | **2 break it / 4 anchor planted** | Open SKILL.md and there's no weighing anything — there's a Steps section, a numbered list Claude runs top to bottom. No step on that list says "use your judgment." | THE ANCHOR — the Steps section, a numbered list, no judgment step |
| B04 | 3 mechanism | Claude reads each step in order and runs it — no branching, unless a step itself says to branch. Read the step, run the step, move to the next one. | READ → RUN → NEXT STEP, linear |
| B05 | **4 anchor payoff / 5 both directions** | Feed it the same stock numbers twice and the steps hand back the identical recommendation both times — that repeatability is real. But ask it something the list never covers, and there's no step left to run. The list only ever does what's written on it. | THE ANCHOR RETURNS — same Steps list; "same input → same output" beside "nothing outside the list" |
| **BCRY** | **6 carry-out** | A Claude skill isn't Claude judging the market. It's Claude running a written list of steps, in order — and it can't handle a case the list doesn't cover. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: "I'm going to hand you a short instruction file with numbered steps in it. Before you run it, tell me which step you're on and what you'll do next — before you act on it." | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Reorder Policy. Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the "judgment call" read; B03 breaks it by opening the actual file and finding a numbered Steps section with no judgment step |
| Exactly one inference flag | None — direct, confirmed mechanism throughout (this is how the Claude Skill's SKILL.md works, not an inference about Claude); `one_flag: "N/A"` in metadata |
| One anchor, planted early, paid off late | B03 → B05 (the Steps section — a numbered list Claude runs top to bottom) |
| Both failure directions | B05: same-input consistency (positive) vs. uncovered-case emptiness (negative) |
| No design judgment | B02–B03 describe why the wrong guess fails; nothing rules on whether "reorder-policy" is a *well-built* skill (the source's Popper/Plato lens moves and verdict language — "what it gets right," "what it bites" — are dropped; Plain explains and stops) |

## Deliberately not claimed

- **Not "Claude never uses judgment anywhere."** The reel's claim is narrower
  and true: *this specific skill's* recommendation comes from running the
  numbered steps in its SKILL.md, not from Claude weighing market factors
  itself. It never claims Claude is incapable of judgment in general.
- **Not a verdict on whether "reorder-policy" is a good skill.** The source
  (Teardown register) ran a Popper move ("what it bites: anything outside
  the spec") and a Plato move (artifact vs. world) as design judgment. Plain
  register keeps the same facts — the file is a short numbered procedure,
  the answer only covers what's written — without ruling on whether that's
  a good or bad way to build a reordering tool.
- **No claim about what the specific steps compute.** The source narration
  never specified the individual steps' business logic beyond "linear, no
  branching unless the step says so" — the reel doesn't invent thresholds,
  formulas, or step content the source never gave.

## Handoff prompt (BHTF, read aloud)

> "I'm going to hand you a short instruction file with numbered steps in it.
> Before you run it, tell me which step you're on and what you'll do next —
> before you act on it."

Why it's worth running: it doesn't require having the "reorder-policy" skill
installed — any Claude conversation can run it with any short numbered
procedure you hand over. Watching Claude narrate which step it's on and what
it will do next, before it does it, is the source's own handoff idea (the
reorder-policy reel's version: "walk me through what you will do before you
do it"), generalized so today's viewer can try it without a custom workshop
skill.

## Beat-count note (redo)

Source (`claude-liam-reorder-policy`, Teardown) ran 7 beats: B00
(puppet-style `ClaudeComposerAsk` ask), B01 anatomy, B02 pipeline, B03
design-tell, BVDT verdict, BHTF handoff, BOUT outro. This redo runs 9: B00
(writer) absorbs the same stakes-setting job; B01–B02 split the source's B01
anatomy beat into anatomy (B01) and the wrong-guess beat Plain register
requires (B02, not present in the Teardown source, which skips straight to
mechanism); B03 keeps the source's exact Steps-section fact (the pipeline
lives in a numbered Steps section) and lets it double as the falsifying
case against the "judgment call" guess; B04 is the source's B02 pipeline
beat, narration re-registered; B05 compresses the source's B03 design-tell +
BVDT verdict into one both-directions beat with the judgment stripped out
(repeatable consistency stated as fact, not as a design "get right"; the
spec limit stated as fact, not as a verdict "bite"). No facts added or
dropped — the Steps-section pipeline, the read-then-run mechanism, and the
same-input/same-output limit all carry over unchanged.
