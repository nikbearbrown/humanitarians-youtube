# QUESTION.md

**Question:** Claude picked up a "skill" called legal-writing — does it grade
your memo, or does it just write a better one for you?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-legal-writing`, a Teardown skill-explainer
under `anthropics/claude-for-legal/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note — no gap this time:** the actual `legal-writing`
SKILL.md was found locally and read in full:
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/law-student/skills/legal-writing/SKILL.md`.
This redo is grounded directly in that file, not only in the source
beat_sheet.json's narration summary (whose `>` markers were unfilled
placeholders — see BUILD-LOG.md).

**The fact that reshapes this redo:** the source beat_sheet's narration is a
generic "Claude reads a SKILL.md, then acts" summary with unfilled `>`
placeholders where the skill's actual specifics belonged. The real SKILL.md's
signature behavior is a hard guardrail stated twice, in its own words:
*"Hard rule: no rewriting. Ever."* and, in the closing section titled "What
this skill does not do," *"Rewrite. Period. The hard guardrail."* Asked to
rewrite anyway, it "Refuse[s]. Gracefully, not preachy" and offers instead:
more specific structural feedback, a labeled example of the structural move
("write yours — don't copy"), or a socratic drill on the underlying rule.

The skill also states its own confidence discipline explicitly: structural
feedback (organization, IRAC/CRAC, topic sentences, active voice) is given
with full confidence — "writing is writing" — but content feedback (is the
stated rule correct, is the cited case applicable) carries a `[VERIFY]` flag
whenever the skill is not certain, and citation form gets `[VERIFY]` on
anything non-routine. Its own worked example — "if the student is writing
about negligence in a car accident hypo, an example sentence about
'defendant's breach' is too close to their draft" — supplies this reel's
anchor: a first-year's negligence memo, planted early and returned to late.

This redo's wrong-guess/mechanism spine is built on that guardrail and that
confidence discipline, not invented.
