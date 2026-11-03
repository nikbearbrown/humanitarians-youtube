# Are You Supervising Claude at the Right Level? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-three-level-supervision-classifier`,
CLI-explainer → Plain). Register: **Plain**. 9 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wonders if they're trusting AI the same amount every time. That's not quite it — the real question is whether you're trusting it the right amount, matched to the task. Liam explains." | writer types "Am I trusting AI / the same amount / every time?", hesitates on "same", corrects to "right" |
| B01 | 1 stakes / 2 wrong guess | The natural assumption is that trusting AI the right amount means picking one comfort level and keeping it steady for every task. But renaming a variable and proposing a whole system architecture aren't the same task — one is quick and low-stakes, the other hands over a real decision. A fixed comfort level can't tell them apart, and the mismatch stays invisible until you actually compare what you asked for against how closely you checked it. | left: a single unchanging comfort-level gauge; right: a variable rename next to a system-architecture proposal, wildly different weight |
| B02 | 3 mechanism | Sheridan and Verplank catalogued ten levels of automation back in 1978, for humans supervising machines generally. Applied to AI, three matter. Level One: copy-paste use — a quick edit you could just as easily have made yourself. Level Two: research-level use — you're leaning on it to gather or summarize something you'd otherwise have to dig for. Level Three: true collaboration — it's proposing the approach, not just executing yours. | three stacked level cards, I / II / III, each lighting as named |
| B03 | **4 anchor planted** | Take Priya, on one ordinary afternoon. She renames a variable — Level One — gives it a quick glance, fine, that's calibrated. She asks it to cite a market size — Level Two — and gives it the same quick glance. Below the line. She asks it to propose a whole system architecture — Level Three — and gives it that same quick glance again. Far below the line. Same glance, three very different amounts of trust handed over. | THE ANCHOR — usage/supervision grid, diagonal line, Priya's 3 dots: one on the line, two below |
| B04 | **3 mechanism, continued / ONE FLAG** | The fix is a simple rule: flag any interaction where the checking was short but the task handed over the real decision — high stakes, barely glanced at. That's the dangerous case, not the careful one. One flag: Sheridan and Verplank never wrote this framework with AI chat in mind — applying their 1978 automation levels here is an adaptation, not something they specified themselves. It fits well enough to be useful, which is the only claim being made. | the rule as a single arrow: SHORT CHECK + HIGH STAKES → FLAG; a small "adaptation, not their own case" marker |
| B05 | **4 anchor payoff** / 5 both directions | Run the flag on Priya's afternoon and it catches exactly what you'd expect: the market-size answer and the architecture proposal both light up, the variable rename doesn't. But a flag doesn't prove the architecture proposal was actually wrong — it proves only that the checking didn't match what was handed over. And no flag on the variable rename doesn't prove nothing was missed there either — it just means this rule wasn't built to catch that kind of mistake. | THE ANCHOR RETURNS — same grid, 2 of Priya's dots flag terracotta; splits into two both-directions cards |
| **BCRY** | **6 carry-out** | Trusting AI the right amount isn't a fixed habit — it's calibrated to what you actually handed it, task by task. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Look back at your last ten AI interactions and sort each into one of three levels: a quick edit, research help, or a real decision handed over. For any you call Level Three, say how many minutes you actually spent checking it. Anything under two minutes on a Level Three is the gap — ask what you'd need to check to close it. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Are You Supervising Claude at the Right Level? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "one comfort level, kept steady"; falsified by B03's Priya case — the same quick glance applied to a variable rename and to a system-architecture proposal |
| Exactly one inference flag | **B04** — applying the 1978 Sheridan-Verplank automation framework to AI chat is an adaptation, one step beyond what they wrote themselves |
| One anchor, planted early, paid off late | B03 → B05 (Priya's three interactions on the usage/supervision grid) |
| Both failure directions | B05: "a flag doesn't prove it was wrong, only that checking didn't match stakes" / "no flag doesn't prove nothing was missed, only that this rule didn't catch it" |
| No design judgment | B01/B02/B04 describe the framework and the rule; no verdict on whether Sheridan-Verplank or the flag rule is well designed |

## Deliberately not claimed

- **Not that Sheridan and Verplank wrote this for AI.** B04 is the explicit
  flag: their 1978 framework covers human supervision of automation
  generally; applying it to an AI chat interface is this reel's adaptation
  of their scale, not a claim about their own research.
- **Not a claim about any specific product UI, command, or model name.**
  The source describes an actual Claude Code invocation that writes a
  Python script calling a named model; this redo keeps the mechanism
  (classify by level, flag the mismatch) as plain narration and drops the
  terminal command, the code, and the model name — general audience, no
  invented or stale product specifics.
- **Not "a flag means something went wrong."** B05 is the explicit guard:
  a flag measures a mismatch between stakes and checking time, not an
  audit of whether the output itself was correct.

## Handoff prompt (BHTF, read aloud)

> "Look back at my last ten interactions with Claude and sort each into one
> of three levels: a quick edit, research help, or a real decision I handed
> over. For any I'd call Level Three, tell me how many minutes I actually
> spent checking it, and flag any where that was under two minutes — that's
> the gap. Ask me what I'd need to check to close it."

Why it's worth running: most people can name their last ten AI interactions
in a minute, but almost nobody has actually lined up "how much I handed
over" against "how long I checked" side by side — the gap is usually
somewhere they didn't expect.

---
**GATE P — signed:** ______________________ (human)
