# QUESTION

**The question:** Claude is trained partly by critiquing and revising its own
harmful outputs. If the same model is both the one answering and the one
checking the answer, isn't that just an AI grading its own homework — and why
would anyone trust the grade?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/constitutional-ai-self-critique/beat_sheet.json`
("Teaching an AI to Grade Its Own Homework", Teardown-register, `register:
"Teardown"`, `channel: "NikBearBrown"`, cold open a `ClaudeComposerAsk` direct
ask beat, four body beats, a handoff beat, `ClaudeTitleOutro`). The source's
body beats were fully written (unlike some redo sources, this one was not a
placeholder scaffold): B01 stated the three problems with human harmlessness
labeling, B02 the constitutional-AI loop (16 principles, red-team prompt,
critique, revise), B03 the four-step mechanism (elicit, critique, revise,
RLAIF), B04 the result (matched RLHF on harmlessness, beat it on
helpfulness, auditable refusals). This reel keeps every one of those facts,
compresses them into hai-simple's Plain-register spine (stakes → wrong guess
→ break it → mechanism → both directions → carry-out), replaces the cold
open with the Brutalist Hesitant Writer, and closes with the Humanitarians AI
skin.

**Why it earns a reel:** the obvious reaction to "the AI grades its own
homework" is suspicion — a student who grades their own exam can just pass
themselves, so self-critique sounds circular and unreliable. The break is
that the model isn't checking against its own opinion of whether an answer
is good; it's checking against one specific, fixed, written rule pulled from
a list of sixteen — the same rule, worded the same way, applied to every
answer, by design not by the model's preference. And the method is verified
against an external result: it matches independently-labeled human RLHF on
harmlessness, and beats it on helpfulness, because human labelers reward
caution (over-refusal) in a way a written rule doesn't. But the source
material — and the original teardown script's own framing — flags a real
residual: the same model that generates the answer also applies the rule to
it, so a blind spot in how the model reads "harm" can survive being checked
by that same model's reading of the rule. That isn't resolved by matching
human labels on the cases those labels covered; it is a live open question,
not a solved one.

**Naive framing (B00, corrected on screen):** "Grading its own homework —
isn't that cheating?" → corrects "cheating" to "checkable" (the real fact:
the question that matters isn't whether it's cheating, it's whether the
grading is actually checkable against something fixed and written, rather
than the model's own say-so).

**Body facts carried from source (unchanged):**
- the three problems with human harmlessness labeling: expensive (paying
  people to read disturbing content), inconsistent (two annotators disagree
  on the same output), doesn't generalize (labels from one year miss harms
  that emerge later)
- the wrong guess: self-grading sounds like grading your own homework —
  worthless, because the same model that answered can just decide it did
  fine
- the break / anchor: the check isn't the model's opinion — it's one
  specific written principle out of a fixed list of sixteen (e.g. "choose
  the response least likely to help someone cause harm"), the same rule
  applied to every response
- the mechanism (four steps, unchanged from source B03): elicit a
  problematic response via a red-team prompt → critique it against the
  written principle → revise it to follow the principle → the revision
  becomes the training example (RLAIF — AI feedback, not human feedback)
- the result (unchanged from source B04): CAI matched human-labeled RLHF on
  harmlessness; beat it on helpfulness because human annotators reward
  caution and over-refuse; the CAI model can cite the specific principle it
  followed, which a human annotator's gut call cannot do
- both directions (new — required by hai-simple's BOTH-DIRECTIONS LAW,
  drawn from the source Teardown cold open's own framing: "what the paper
  treats as solved that practitioners still argue about"): (a) matching
  human labels on harmlessness does not prove the critique step is
  unbiased — the same model both answers and grades, so a shared blind spot
  in what it calls "harmful" is not caught by that same model applying the
  rule; this is the one inference flag, not resolved by the source; (b)
  beating human RLHF on helpfulness does not prove the model is more
  correct when it refuses less — it could simply be refusing less broadly;
  telling "correctly less cautious" from "unsafely less cautious" needs a
  separate check, not this comparison alone
- anchor payoff: back to the one written rule — the answer is still graded
  against it, not against Claude's opinion, but the same model holding the
  rule can still miss what it was never trained to flag under that rule
