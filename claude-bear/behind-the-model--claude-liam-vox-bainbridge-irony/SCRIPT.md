# Why More Automation Creates More Supervision Work, Not Less — Narration Script (GATE P)

*Skill: `hai-simple`. Redo of `behind-the-model/claude-liam-vox-bainbridge-irony`.
Register: **Plain** (source was Teardown). One idea = one beat. 11 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes a smarter agent means less work for them. It's backwards — smarter agents create more supervisory work, not less. Liam explains why the irony holds every time. | writer types "If my agent gets smarter, I'll have less work to do, right?", hesitates on "less", corrects to "more" |
| B01 | 1 stakes | A developer hands a bug fix to her AI agent. It reads the files, edits the code, reruns the tests, and reports back: resolved. | code editor, green test result, RESOLVED tag |
| B02 | 2 wrong guess + **4 anchor planted** | The natural guess: a more capable agent means less work for the person supervising it. One lever, capability, goes up. The other lever, workload, comes down. | THE ANCHOR — naive bar pair: capability rises, workload shrinks |
| B03 | **2 break it** | But now she has to read the diff, verify the test results, decide whether an edge case was missed, and check whether anything outside the reported scope was touched. That's more deliberate work than the copy-paste workflow it replaced — not less. | four chips stack: READ DIFF, VERIFY TESTS, CHECK EDGE CASES, AUDIT SCOPE; tally 1→4 |
| B04 | 3 mechanism | This is Bainbridge's Irony, named in 1983: automation doesn't eliminate human work, it relocates it — upstream into design, and into checkpoints at the end. The more capable the automated system, the more demanding the supervisory role becomes. | "AUTOMATION" splits into "DESIGN (upstream)" and "CHECKPOINT (after)" |
| B05 | **4 anchor payoff** | The real scale: as agent capability rises, supervisory load rises with it — not because the agent got worse, but because its reach got wider. Take Priya: without an agent, she moves twenty files by hand, say — one decision each. With an agent reorganizing two hundred files, she now has to write a scope statement, review a taxonomy, approve batches, verify counts, and audit spot-checks — illustrative numbers, but the shape holds: less calendar time, more deliberate decisions. | THE ANCHOR RETURNS — bar pair, workload bar rises to match capability; then Priya: 20 squares vs. 5 decision chips |
| B06 | **5 both directions** | When the task is small and easily undone, the naive picture holds — capability up, workload down, because there's nothing costly to verify. But once an agent's reach is wide, one bad decision multiplies: a wrong scope statement at the start becomes two hundred wrong moves, not one. Manual work fails locally. Agent work fails at scale — which is exactly where the irony bites hardest. | split card: small/reversible task (naive holds) vs. wide-reach task (1 wrong scope → 200 wrong moves) |
| B07 | 3 mechanism (practice) | The practice: write the scope before you delegate. Before the agent starts, define what it can touch, what it must not touch, and what you'll check when it's done. The scope statement isn't friction — it's the work the agent's capability moved upstream. | timeline: BEFORE (scope / can touch / must not touch) → DURING (agent runs) → AFTER (what to check); BEFORE zone widest |
| **BCRY** | **6 carry-out** | More capable agents don't reduce human work — they relocate it: upstream into the scope you write before delegating, and into the checkpoint you run after. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Before you delegate a real task to an agent this week, write down what it can touch, what it must not touch, and what you'll personally check when it's done. Then notice how much of that thinking happens before the agent starts, not after. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why More Automation Creates More Supervision Work, Not Less. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the naive-lever read; B03 breaks it with the diff/tests/edge-case/scope checklist |
| Exactly one inference flag | **B05** — Priya's file counts are illustrative, not measured |
| One anchor, planted early, paid off late | B02 → B05 (the capability/workload bar pair: naive divergence, then both rising together) |
| Both failure directions | B06 — naive picture holds for small/reversible tasks; flips once reach is wide |
| No design judgment | B04–B07 describe the mechanism and the practice; no verdict on whether agentic delegation is a good idea |

## Deliberately not claimed

- **Not "automation always creates more work."** B06 states the direction where
  the naive picture is correct — the source's Teardown register never needed
  this caveat; Plain's both-directions law does.
- **Not precise counts.** Priya's twenty/two-hundred files are illustrative
  (flagged once, B05), matching the source's own FACTCHECK note.
- **No verdict on whether wide-reach delegation is worth it.** That's a
  judgment call outside Plain register; the reel explains the mechanism and
  the practice, then stops.

## Handoff prompt (BHTF, read aloud)

> "Before you delegate a real task to an agent this week, write down what it
> can touch, what it must not touch, and what you'll personally check when
> it's done. Then notice how much of that thinking happens before the agent
> starts, not after."

---
**GATE P — signed:** ______________________  (human)
