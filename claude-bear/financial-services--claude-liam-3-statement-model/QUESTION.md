# QUESTION — financial-services--claude-liam-3-statement-model

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-3-statement-model/beat_sheet.json`.
Unlike some sibling redos in this factory (e.g. `claude-for-legal--claude-liam-handbook-updates`),
this source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `3-statement-model` skill: it completes,
populates, and links 3-statement financial model templates (Income
Statement, Balance Sheet, Cash Flow Statement); it is triggered when asked
to fill out model templates, complete existing model frameworks, populate
financial models with data, complete a partially filled IS/BS/CF framework,
or link integrated statements within an existing template structure; Claude
reads its `SKILL.md` before acting and executes the steps linearly. The
`source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/model-builder/skills/3-statement-model/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
function in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown -> Plain (the source's B03
framed "what it gets right / where it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes Claude reasons about the business like an analyst, deciding what
belongs in the model from general financial judgment) falsified by what the
skill actually is (a fixed list of steps that link an existing template,
nothing more); the anchor (net income traveling from the income statement
into retained earnings on the balance sheet, then into the cash flow
statement) planted at B02 and paid off at B03; both directions at B03
(a model that ties out is not the same as a model that is right; a blank
line does not mean the run failed). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER LAW
("judgment" -> "the steps" — the naive assumption that filling in the model
takes financial judgment, corrected to: it takes following a written set of
steps). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off, per hai-simple's channel skin.

**Question this reel actually answers:** Does Claude fill in a 3-statement
financial model by reasoning about the business like an analyst — or is it
doing something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
