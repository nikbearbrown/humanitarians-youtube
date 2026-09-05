# Teaching an AI to Grade Its Own Homework — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/constitutional-ai-self-critique`
(Teardown register, fully-written body, 7 beats) — question, facts, and the
four-step mechanism kept unchanged, body compressed to hai-simple's
stakes → wrong guess → break it → mechanism → both directions → carry-out
spine, cold open replaced, close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone hears the AI grades its own homework and assumes that's cheating — the student passing itself. It isn't cheating. It's checked against a written rule. Is grading its own work actually checkable? | writer types "Grading its own homework — isn't that cheating?", hesitates on "cheating", corrects to "checkable" |
| B01 | 1 stakes | Checking every Claude answer for harm used to mean paying people to read disturbing content — expensive. Two readers often disagree — inconsistent. And rules written one year miss harms that show up later — they don't generalize. Constitutional AI wants Claude to check its own homework instead. | three problem cards (expensive / inconsistent / doesn't generalize), then "check its own homework" |
| B02 | 2 wrong guess | So the natural skepticism: if Claude grades its own answer, it can just pass itself — the same model deciding it did fine, on its own opinion. That's what grading your own homework usually means, and it sounds worthless. | a student figure grading its own paper, stamping itself PASS |
| B03 | **2 break it — ANCHOR PLANTED** | But the grading isn't Claude's opinion of its own work. It's checked against one specific written rule, pulled from a fixed list of sixteen — for example: choose the response least likely to help someone cause harm. Same rule, same wording, applied to every answer. | THE ANCHOR — a rubric card, numbered 1–16, one line highlighted |
| B04 | 3 mechanism | The loop runs in four steps. Elicit — a red-team prompt draws out a harmful response. Critique — Claude checks that response against the rule and names the violation. Revise — Claude rewrites the answer to follow it. Then the revised answer becomes the training example — feedback from the AI, not from a human. | four-step flow: ELICIT → CRITIQUE → REVISE → TRAIN |
| B05 | 3 mechanism — result | The result matched human-labeled training on harmlessness, and beat it on helpfulness — human graders tend to reward caution, so those models over-refuse. And Claude can point to the specific rule it followed. A human grader's gut feeling can't be cited that way. | two-bar comparison (harmlessness: matched / helpfulness: beat it), plus a "cites the rule" tag |
| B06 | **5 both directions + ONE FLAG — ANCHOR PAYOFF** | Two things this doesn't prove. Matching on harmlessness doesn't mean the check is unbiased — the same model answers and grades, so a blind spot in what it calls harmful can slip past the very rule meant to catch it. That's flagged by researchers, not resolved. And beating on helpfulness doesn't mean it's more correct — it might just refuse less; telling those apart takes a separate check. Back to that one rule: the answer is graded against it, not against Claude's opinion — but the same student holding the rubric can still miss what it was never trained to flag. | mirror icon over the rubric (shared blind spot); refuse-less ≠ more-correct card; THE RUBRIC RETURNS, same highlighted line |
| **BCRY** | **6 carry-out** | Self-critique doesn't mean Claude approves of itself. It means the answer gets checked against a written rule instead of a gut feeling. The check still can't catch what that same model was never trained to see. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Teaching an AI to Grade Its Own Homework. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read (self-grading = worthless); B03 breaks it with the concrete case — a fixed written rule, not the model's opinion, applied identically every time |
| One anchor, planted early, paid off late | B03 (the numbered rubric, one principle highlighted) → B06 (the same rubric returns, resolved) |
| Both failure directions | B06 — matching harmlessness doesn't prove the check is unbiased (the flag); beating helpfulness doesn't prove the model is more correct, only less cautious |
| Exactly one inference flag | B06 — the same-model blind-spot claim, explicitly named as flagged by researchers rather than resolved |
| No design judgment | Beats describe why the loop is built this way; none rules on whether Anthropic drew the line in the right place |

## Deliberately not claimed

- **Not "the check is bias-free."** B06's first direction is the correction
  to that overreach: matching human labels on harmlessness only shows the
  method works on the cases those labels covered, not that the critique step
  has no shared blind spot with the model it's checking.
- **Not "fewer refusals means better judgment."** B06's second direction
  bounds the opposite overreach: beating RLHF on helpfulness could mean the
  model refuses less broadly, not that it refuses more correctly — that
  needs a separate evaluation the source doesn't claim to run.
- **Not "this is how all AI self-improvement works."** The reel names
  Constitutional AI's specific critique-and-revise loop, never AI
  self-improvement in general.

## Handoff prompt (BHTF, read aloud then discussed)

> "Take something I wrote — an email, a paragraph, a piece of code. Don't
> tell me if it's good. Give me one specific written rule to check it
> against — for example, does this avoid overstating what I'm sure of.
> Critique my draft against just that rule, then revise it so it follows
> the rule."

Why it's worth running: the whole distinction in this reel — checked
against a written rule vs. checked against a gut feeling — only becomes real
once it's applied to something you actually wrote. Naming one specific rule
and watching the revision follow it, instead of a vague "make this better,"
takes a few minutes and makes the mechanism concrete.

---
**GATE P — signed:** ______________________  (human)
