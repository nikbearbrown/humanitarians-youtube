# QUESTION — financial-services--claude-liam-dcf-model

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-dcf-model/beat_sheet.json`.
Like the `3-statement-model` sibling redo, this source sheet is NOT a
placeholder shell — its narration carries real, specific facts about the
Anthropic `dcf-model` skill: it builds a real DCF (Discounted Cash Flow)
model for equity valuation; it retrieves financial data from SEC filings and
analyst reports, builds cash flow projections with WACC (weighted average
cost of capital) calculations, performs sensitivity analysis, and outputs a
professional Excel model with an executive summary; triggered when a user
needs to value a company using DCF methodology, wants an intrinsic-value
analysis, or asks for financial modeling with growth projections and
terminal-value calculations. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md`)
does not exist on this machine (different machine's home directory), but the
source *beat_sheet.json*'s own narration already states the skill's function
in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown -> Plain (the source's B03
framed "what it gets right / what it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes Claude's DCF output reflects its own judgment about what a company
is worth, the way an analyst who has studied the business reaches a
conclusion) falsified by what the skill actually is (it runs your
assumptions — growth rate, discount rate, terminal growth — through a fixed
formula; it never argues that an assumption is wrong, it just recomputes);
the anchor (one dial — the discount rate, WACC — driving one output number,
the intrinsic value) planted at B02 and paid off at B03 via the sensitivity
analysis; both directions at B03 (a valuation that swings a lot for a small
assumption change doesn't mean the model is broken — the input was never
precise; a valuation that holds steady across the sensitivity range doesn't
prove it's right either — the terminal-value assumption, which usually
carries most of the total, is still just a guess about the distant future).
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("judgment" -> "the formula" — the
naive assumption that a DCF number is Claude's judgment call, corrected to:
it is Claude running a formula over the assumptions it was given). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin.

**Question this reel actually answers:** Does Claude's DCF valuation reflect
its own judgment about what a company is worth — or is it running a fixed
formula over the assumptions it was given?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
