# Claude, Contract Review. — Narration Script (redo, Plain register)

*Skill: `hai-simple`. Register: **Plain**. Carry-out written first
(CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, no puppet/host).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "People type it like this: is Claude my contract's lawyer? It isn't. It's my contract's checklist — the same steps, every single time. So what does that checklist actually catch, and what does it miss?" | writer types "Is Claude my contract's lawyer?", corrects "lawyer" -> "checklist" |
| NB01 | 1 stakes | People hand Claude a contract expecting a review. What actually runs in between is a written file: SKILL.md. | contract -> SKILL.md -> ??? |
| NB02 | 2 wrong guess | The natural assumption: Claude reads it like a lawyer would, weighing the whole document clause by clause, case by case. | read it all -> weigh each clause -> lawyer's call |
| NB03 | 3 mechanism (anatomy) | A skill is a folder Claude reads before it acts. SKILL.md is the whole instruction set — plain language, no hidden logic. | SKILL.md / plain language / no hidden logic |
| NB04 | 3 mechanism (pipeline) | The pipeline is fixed: read the file, execute each step in order, return the result. Linear — no branching unless a step says so. | read steps -> execute in order -> return result |
| NB05 | **2 break it / 3 mechanism** | So it isn't judgment — it's a checklist, written in advance. That trade buys repeatable results: the same input gets the same output, every run. | checklist / not judgment / repeatable |
| NB06 | **4 anchor planted** | Run it on a freelance contract, and it flags the termination clause. The checklist says look there, so it looks. | THE ANCHOR — freelance contract -> termination clause -> flagged |
| NB07 | 3 mechanism (the limit) | But the checklist only names what it names. An arbitration clause the list never mentions gets no comment — not because it's fine. | on the list -> off the list -> no comment |
| NB08 | **4 anchor payoff / 5 direction A** | Run the same contract again: the termination flag comes back, identical. That's consistency — a flag means a listed check matched, not a verdict on the contract. | THE ANCHOR RETURNS — freelance contract -> same flag -> not a verdict |
| NB09 | **5 direction B** | And a clean pass isn't a clean bill of health either — it means nothing on the list tripped. What's off the list stays invisible either way. | clean pass -> nothing tripped -> still invisible |
| **BCRY** | **6 carry-out** | A SKILL.md gives Claude the same checklist every time — that's consistency, not judgment, so the read-through is still yours. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude, along with any contract you're reviewing: "Before you review this, list exactly what you will check for and what you will not. Then do the review." That first list turns an invisible checklist into one you can see. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Contract Review — the checklist, not the lawyer. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | NB01; mechanism waits until NB03 |
| Wrong guess surfaced *and falsified by a case* | NB02 states the read (Claude as lawyer, weighing judgment); NB07 breaks it with the arbitration-clause case — a clause off the list gets no comment, not a clean bill |
| Inference flags | N/A — direct mechanism description throughout (how a Claude Skill executes: read file, run steps, return result); no probabilistic claim requiring a flag |
| One anchor, planted early, paid off late | NB06 -> NB08 (the same freelance contract, same termination flag, run twice) |
| Both failure directions | NB08 (a flag isn't a verdict) and NB09 (a clean pass isn't safety) |
| No design judgment | NB03-NB05 describe how the mechanism works; they never rule on whether a checklist-only skill is a good or bad way to build contract review |

## Beat-count note (redo)

Source (`claude-liam-contract-review`, Teardown "skill anatomy" format,
7 beats: B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro) compressed its whole body argument into
3 beats plus a verdict recap — no dedicated wrong-guess beat, no anchor, no
both-directions beat, because Teardown's "design tell" format states the
strength/weakness pair directly rather than building to it. hai-simple's
Plain register requires the six-move spine (WRONG-GUESS LAW, ANCHOR LAW,
BOTH-DIRECTIONS LAW are all mandatory, not present in the source shape), so
the body expanded from 3 source beats to 9 (NB01-NB09) to give the wrong
guess, the anchor plant/payoff, and both directions each their own beat —
the same expansion-for-format-fit already precedented on
`books--claude-liam-what-plugins-are`'s BUILD-LOG. Every fact in the
source's real (non-placeholder) argument carries over exactly:
- B01 "a skill is a folder... SKILL.md is the instruction set... the file
  is the program" -> NB03, word-for-word substance.
- B02 "pipeline... read each step in order and execute it. Linear — no
  branching unless the step says so" -> NB04, word-for-word substance.
- B03 "a specification written as an instruction set... what it gets
  right: repeatable results. What it bites: anything outside the spec" ->
  NB05 (repeatable half) + NB07 (outside-the-spec half, made concrete with
  the arbitration-clause case instead of the source's unfilled `>`).
- BVDT "same input, same output, every run. Know the limit: only what the
  file says" -> BCRY, word-for-word substance (the carry-out line).

The only invented content is the anchor's worked example (a freelance
contract; termination clause flagged; arbitration clause off the list) —
supplied because the source's own worked example was never filled in
(literal `>` placeholders in B00/B03/BVDT/BHTF's narration_text). Per
PHASE 1's "when in doubt, describe behavior generically," the example
describes a plausible, generic contract-review scenario without asserting
any fact about a specific real skill's actual clause list. See QUESTION.md
for the full account of the source defect.

## Deliberately not claimed

- **No specific clause roster.** The reel never claims the real
  `contract-review` skill's checklist actually contains "termination" or
  "arbitration" as items — those are the anchor's illustrative stand-ins,
  used because the source never specified its own. The reel's claim is
  about the mechanism (checklist-only, bounded by what's specified), which
  the source's real, non-placeholder text supports directly.
- **No legal advice.** The reel never tells a viewer a contract is safe or
  unsafe to sign; NB08/NB09 explicitly deny that a flag or a clean pass is
  a verdict.

## Handoff prompt (BHTF, read aloud)

> "Before you review this, list exactly what you will check for and what
> you will not. Then do the review."

Why it's worth running: it converts an invisible checklist into a visible
one, which is the whole carry-out.
