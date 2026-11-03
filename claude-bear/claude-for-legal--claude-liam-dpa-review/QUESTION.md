# QUESTION.md

**Question:** When Claude reviews a vendor's Data Processing Agreement (DPA), is it
approving the agreement, or checking it against a fixed list of required clauses?

**Asked by:** no individual asker — this is a `mode: "redo"` build (SUBJECT.json). The
source reel (`claude-liam-dpa-review`, Teardown register) frames the question generically
as "Claude, Dpa Review" — a skill-teardown walkthrough of a hypothetical `dpa-review`
Anthropic Skill built for reviewing DPAs.

**Name usable:** N/A.

**Redo note:** the source `beat_sheet.json` is a batch-templated "skill teardown" whose
skill-specific content was never filled in — several narration lines contain a literal
unresolved `>` placeholder (B00, B03, BVDT, BHTF) instead of real content, and the
referenced `source_skill` file
(`/Users/bear/Documents/CoWork/bear-textbooks/.../privacy-legal/skills/dpa-review/SKILL.md`)
does not exist on this machine. Per the redo contract's spirit and the precedent set by
the `claude-for-legal--claude-liam-cease-desist` sibling (same source batch, same shape,
built 2026-08-29) — where the specific mechanism fact was authored fresh because the
source itself supplied it — this build authors the missing skill-specific fact using
well-established, true legal-practice content: GDPR Article 28(3)'s required DPA clauses
(named sub-processors, deletion-or-return of data at contract end). The generic skill
anatomy (a Skill is a folder; SKILL.md is the instruction set; the pipeline reads, executes
steps in order, and returns) is carried over from the source unchanged — that portion of
the source was real narration, not a placeholder.
