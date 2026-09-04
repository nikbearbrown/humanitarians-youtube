# QUESTION.md — healthcare--claude-liam-clinical-note-extract-skill

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-clinical-note-extract-skill`, a
skill-teardown walkthrough of the Anthropic `clinical-note-extract-skill`
Claude Skill from the `healthcare` book's plugin set) into the Plain
register for @HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude pulls structured data out of a clinical note, does it guess
> at a value it can't find, or only report what's literally on the page?

**The naive framing (what B00 types and corrects):** "Does Claude guess a
value from a clinical note?" — the newcomer's assumption is that an
extraction tool fills gaps the way a person would, using context and
medical knowledge to infer what's probably true. It doesn't. The corrected
question: "Does Claude cite a value from a clinical note?" —
`clinical-note-extract-skill` only reports a value when it can point to the
exact span of text that supports it, and returns an explicit null for
everything it can't find. That correction ("guess" → "cite") is the
wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-clinical-note-extract-skill/beat_sheet.json`
and its `AUDIT.md`): a skill is a folder Claude reads before it works,
containing a `SKILL.md` written in plain language plus `assets/`,
`references/`, `scripts/`, and `workflows/` — six files/folders total; the
skill's job is structured extraction from clinical notes against a
user-defined schema, with a span citation for every value it reports and an
explicit null for every value it can't find; same note and same schema
produce the same output every run; the skill only handles what its file
specifies.

**One correction made against the source (not an invented fact):** the
source's B02 narration claimed "the pipeline has 2 steps" and named only
the two sub-checks of validation (span check, then per-field-type check).
The source's own `AUDIT.md` (Check: "Content accuracy note") flags this as
a scripting error, stating the actual `SKILL.md` defines four steps —
Define schema, Extract, Validate, Report — and that the locked narration
only ever described the two sub-steps inside Validate. This redo corrects
NB02 to state the real four-step pipeline (folding in the two validation
sub-steps the source did get right), per the honesty rule that facts about
Claude must be true and current — it does not invent a new fact, it applies
the correction the source material already documented but never fixed.
