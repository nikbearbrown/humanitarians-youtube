# QUESTION.md — healthcare--claude-liam-clinical-trial-protocol-skill

**Mode:** redo. There is no literal asked question — this reel re-registers an
existing Teardown reel (`claude-liam-clinical-trial-protocol-skill`, a
skill-teardown walkthrough of the Anthropic `clinical-trial-protocol-skill`
Claude Skill from the `healthcare` book's plugin set) into the Plain register
for @HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude helps put together a clinical trial protocol, is it making the
> trial-design calls itself, or just drafting the document to a fixed
> specification a person still has to sign off on?

**The naive framing (what B00 types and corrects):** "Does Claude decide a
clinical trial protocol?" — the newcomer's assumption is that a skill named
for something this consequential must be exercising clinical or regulatory
judgment: choosing endpoints, deciding dosing, weighing what's safe. It
isn't. The corrected question: "Does Claude draft a clinical trial protocol?"
— `clinical-trial-protocol-skill` is an instruction set that produces a
protocol *document* to a fixed spec; it does not decide how the trial should
run. That correction ("decide" → "draft") is the wrong-guess pedagogy per
WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-clinical-trial-protocol-skill/beat_sheet.json`):
a skill is a folder Claude reads before it works, containing a `SKILL.md`
written in plain language plus `README.md`, `assets/`, `references/`, and
`scripts/` — five files/folders total (per the source B01
`SkillTeardownAnatomy` beat's own file list); the pipeline runs as three
linear steps — read `SKILL.md`, execute each step from the Steps section in
order, return the result — with no branching unless a step itself says so;
the skill's job is generating clinical trial protocols for medical devices or
drugs, for requests like "create a clinical trial protocol" or "help me
design a clinical study"; it follows the SKILL.md's instructions exactly, so
the same request produces the same kind of protocol every run; it only
covers what the file specifies.

**No correction needed against the source** (unlike some sibling redos in
this series): the source's own `AUDIT.md` for this reel passed its content
checks (Check 9, Check 10) with only cosmetic fixes (truncated strings,
sparkline word-count, a datable model-name claim) — no factual/content error
is flagged, so nothing here is corrected against documented source error. The
one substantive change this redo makes is a **register** change, not a
content correction: the source's B03/BVDT beats stated the same facts inside
a Teardown "gets it right / what it bites" verdict frame; this redo restates
them as a plain mechanism-and-boundary fact per the NO JUDGMENT check, and
folds the two into one beat (NB03) plus the carry-out (BCRY), matching this
factory's established redo pattern for the sibling
`healthcare--claude-liam-clinical-note-extract-skill` and
`financial-services--claude-liam-financial-plan` reels.
