# QUESTION.md — healthcare--claude-liam-fhir-developer-skill

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-fhir-developer-skill`, a
skill-teardown walkthrough of the Anthropic `fhir-developer-skill` Claude
Skill from the `healthcare` book's plugin set) into the Plain register for
@HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When a FHIR request is invalid, does Claude just say pass or fail, or does
> it name the exact problem?

**The naive framing (what B00 types and corrects):** "Does Claude just
return pass-fail on a bad FHIR request?" — the newcomer's assumption is
that an API validator has one binary outcome: the request either goes
through or it's rejected. It doesn't work that way here. The corrected
question: "Does Claude just return the exact code on a bad FHIR request?"
— `fhir-developer-skill` returns a *specific* HTTP status code for the
*specific* thing that's wrong, and that specificity is the mechanism, not
an afterthought. That correction ("pass-fail" → "the exact code") is the
wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-fhir-developer-skill/beat_sheet.json`
and its `AUDIT.md`/`REBUILD-LOG.md`): `fhir-developer-skill` is a Claude
Skill for FHIR REST API development for healthcare; a skill is a folder
Claude reads before it works, containing `SKILL.md` (the full instruction
set, in plain language, no hidden logic) plus `references/` and `scripts/`
— three items total; the pipeline lives in `SKILL.md`'s Steps section and
runs linearly (read a step, execute it, return the result — no branching
unless a step itself says so); the skill validates FHIR resources and
returns the specific HTTP status code for what's wrong — 422 for an
invalid enum value, 412 for an ETag mismatch on a conditional update; the
status code is the spec, so the same input produces the same code every
run.

**No content correction needed against the source.** Unlike the
`clinical-note-extract-skill` sibling, this source's own `AUDIT.md` records
every Phase-1 accuracy check as PASS with no open accuracy note — so this
redo carries the facts over as documented, without correcting anything.

**Adaptation made to BHTF (your turn), not an invented fact:** the source's
prompt asked the viewer to "read the fhir-developer-skill skill," which
requires installing a specific Anthropic healthcare plugin a general viewer
won't have. This redo substitutes an equivalent, actually paste-ready
prompt that exercises the same two disciplines — a specific reason (not a
binary pass/fail) for every failure, and explaining the plan before
executing — without depending on any specific Skill file.
