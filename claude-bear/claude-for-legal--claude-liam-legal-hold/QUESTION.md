# QUESTION.md

**Question:** Claude picked up a "skill" called legal-hold — does it decide,
on its own, when documents need to be frozen for a lawsuit?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-legal-hold`, a Teardown skill-explainer
under `anthropics/claude-for-legal/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note — no gap this time:** unlike the `case-brief` and
`build-guide` sibling redos (whose source SKILL.md files were unreachable
from this machine), the actual `legal-hold` SKILL.md **was found locally**:
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/litigation-legal/skills/legal-hold/SKILL.md`.
Read in full before scripting. This redo is grounded directly in that file,
not only in the source beat_sheet.json's narration summary.

**The fact that reshapes this redo:** the source beat_sheet's narration
("issue, refresh, release, or report... drafts the hold notice") is true but
compresses past the skill's actual signature behavior — a hard confirmation
gate before either consequential step (`--issue`, `--release`). Quoting the
SKILL.md directly: *"Do not send the notice without an explicit yes"* and,
for a non-lawyer user, *"Have you reviewed this with an attorney? If yes,
proceed. If no, here's a brief to bring to them."* The skill also names its
own edges explicitly, in a section titled "What this skill does not do":
it does not enforce preservation, does not set scope alone, does not
auto-refresh without review, and does not send the notice — a person does
every one of those. This redo's wrong-guess/mechanism spine is built on that
gate and that edge-list, not invented.
