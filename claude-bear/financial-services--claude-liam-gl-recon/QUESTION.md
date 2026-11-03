# QUESTION.md

**Question:** Claude picked up a skill called gl-recon — does that mean
Claude itself is now deciding which ledger is right and fixing the books?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-gl-recon`, a Teardown skill-explainer
under `anthropics/financial-services/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json is fully filled in for
its job description and mechanism — no unfilled `>` placeholder. The skill's
job line survives verbatim in the source's B00 beat: "Reconcile general
ledger to subledger for a trade date or period — match at the position or
transaction level, surface breaks, and classify each break by likely cause.
Use for daily or month-end recon runs across asset classes." The source's
anatomy beat (B01) lists exactly one real file: `SKILL.md` (2k, accented) —
unlike some `financial-services` siblings, this source never names a second
file, so this redo does not invent one. The skill's own source file
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-
services/plugins/agent-plugins/gl-reconciler/skills/gl-recon/SKILL.md`) is
not reachable from this machine (confirmed via `ls`) — same class of gap
documented on other `financial-services` sibling redos — but nothing here
depends on reading it: the source beat_sheet.json already states the job,
the file count, the linear pipeline (read SKILL.md → execute → return
output), and the specification semantics (repeatable results, a limit at the
file's edge). The "GL: $104,000 / Subledger: $100,000 / break: late trade"
anchor figures in this redo are an illustrative example built to visualize
the source's own literal job line (match, surface breaks, classify by
cause) — not a claim about any specific real reconciliation, transcript, or
account the skill has ever processed.
