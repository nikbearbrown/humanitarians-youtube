# Correlated Failure in AI Auditing — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-liam-correlated-failure-research`
(Teardown register, CLI 10-beat spine: PROBLEM/ASK/CODE/OUTPUT/CHANGE/OUTPUT/
SUMMARY/NEXT STEPS) — question, facts, and argument kept; body recompressed to
one idea per beat; cold open replaced; close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes three AI judges agreeing proves an answer is verified. It doesn't — agreement like that is just consensus. So the real question: when AI checks AI, is agreement ever actually verification? | writer types "Three AI judges agree. That means it's verified, right?", hesitates on "verified", corrects to "consensus" |
| B01 | 1 stakes | It's increasingly common to have one AI system check another one's work — grading an answer, reviewing code, auditing a claim. When several AI reviewers look at the same output and agree, that agreement gets treated as proof the answer is correct. | several AI reviewer cards converging on one output, a checkmark forming where they agree |
| B02 | 2 wrong guess | That seems reasonable. More opinions converging on the same verdict looks like stronger evidence — the way several judges reaching the same score, or several doctors agreeing on a diagnosis, makes you more confident, not less. | the AI reviewers relabeled as JUDGES / DOCTORS, all pointing to one confident verdict |
| B03 | **2 BREAK IT — ANCHOR PLANTED** | Here's a test. Give an AI judge the same two answers twice — once in order A, once with the order swapped. Nothing about the answers changed. But the judge's verdict flipped: it picked whichever answer came first, not whichever answer was better. | THE ANCHOR — two identical answer cards, order swapped between two runs, the "winner" flips |
| B04 | 3 mechanism | That's not a glitch — it's one of three documented judging biases: favoring the first answer shown, favoring the longer answer, and favoring answers that sound like its own style. These are structural, and they show up whenever an AI model checks another AI's output. | three labeled bias cards: POSITION, LENGTH, STYLE |
| B05 | 3 mechanism | Cross-checking only reduces error when the checkers fail independently. If two checkers share the same blind spots, their agreement tells you nothing new. AI models built on similar training data and similar tuning share exactly that — the same blind spots. Agreement between them is evidence they share priors, not evidence they're both right. | two overlapping circles, the shared region marked; agreement lives only inside the overlap |
| B06 | 3 mechanism | The fix isn't zero AI — it's pairing each kind of claim with a check that fails differently. A factual claim gets checked against a retrieval lookup. A math result gets checked by running the actual code. A schema or format claim gets checked by a validator. None of those share the model's blind spots. | a small pairing table: claim type -> independent check, each row landing outside the shared-bias circle |
| B07 | **3 ONE FLAG** | One flag — a check only counts as independent if it doesn't quietly run on the same kind of model underneath. A search index built by an AI, or a validator whose rules an AI wrote, can reintroduce the exact blind spot it was supposed to catch. | THE FLAG — a "clean" check card, a hidden AI gear revealed inside it |
| B08 | **5 both directions — ANCHOR PAYOFF** | So this cuts both ways. When a code check and an AI's claim agree, that's real evidence — their failure modes don't overlap. When three AI judges agree, that alone still proves nothing — swap the order, and the "verified" answer flips. And when AI judges disagree, that doesn't prove one is wrong either — it can just mean the same shared bias landed differently this run. | mirrored panel: INDEPENDENT AGREE (holds) vs. THE ANCHOR RETURNS, order swapped, verdict flips |
| **BCRY** | **6 carry-out** | More AI models agreeing isn't more verification. It's the same blind spot, counted twice. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Consensus Isn't Verification. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 falsifies it with the order-swap case — the verdict changes with position, not content |
| One anchor, planted early, paid off late | B03 (the order-swap demo) → B08 (the same demo, closing the reel) |
| Exactly one inference flag | **B07** — a check only counts as independent if it truly doesn't share the model's blind spot underneath; this is the one place the reel notes a real edge that could undercut the fix |
| Both failure directions | B08 — what a positive result proves (independent checks agreeing) vs. does not prove (correlated checkers agreeing); what a negative result does not prove (disagreement between correlated checkers doesn't confirm either is wrong) |
| No design judgment | Beats describe why agreement is or isn't evidence; none rules on whether any specific product or vendor built its judge models badly |

## Deliberately not claimed

- **Not "AI-on-AI checking is always worthless."** B08's first direction is the
  correction to that overreach: a structurally independent check (code execution,
  retrieval) agreeing with an AI's claim is real evidence.
- **Not "disagreement between AI judges proves one is wrong."** B08's second direction
  bounds this: disagreement between correlated checkers can just mean the shared bias
  landed differently, not that either verdict is reliable.
- **No accusation of any specific product or vendor** having a defective judge model —
  the three biases are described as documented and structural to LLM-as-judge setups
  generally.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to find correlated-failure seams in an AI pipeline I use. Look at how outputs
> get checked, and tell me every place where an AI call is verifying another AI's output.
> For each one, tell me if the checker could share the same blind spot as what it's
> checking, and suggest a structurally different way to verify it instead — a retrieval
> lookup, running actual code, a schema validator, or a named human reviewer."

Why it's worth running: the independence requirement only feels real once it's applied to
an actual pipeline you use. Naming the seams and picking one structurally different
replacement takes a few minutes and turns an abstract audit rule into a concrete change.

---
**GATE P — signed:** ______________________  (human)
