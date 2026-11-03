# QUESTION — financial-services--claude-liam-ai-readiness

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-ai-readiness/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `ai-readiness` skill: it scans the
portfolio for the highest-leverage AI opportunities and ranks where to
deploy operating-partner time; it ingests quarterly updates and financials
across multiple portfolio companies, identifies quick wins at each, and
stacks them into a single ranked action list; it is used during quarterly
portfolio reviews, annual planning, or when deciding which companies get AI
investment first. Claude reads `SKILL.md` before acting and executes the
steps linearly (source anatomy/pipeline beats: one file, read → execute →
return). The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/private-equity/skills/ai-readiness/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
function in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain (the source's B03
framed "what it gets right / where it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes Claude decides, from its own judgment, which portfolio company is
most ready for AI investment) falsified by what the skill actually is (for
each company it ingests the quarterly update and financials and identifies
quick wins strictly from what's written there — give it a company whose
update never mentions an AI opportunity and it has nothing to rank for that
company this quarter); the anchor (one portfolio company's Q3 update —
ingested, quick wins found, scored, ranked into the stack) planted at B02
and paid off at B03; both directions at B03 (a high rank means the update
scored well against the spec's criteria — that isn't the same as being the
single best next investment across the whole portfolio; a low rank this
quarter doesn't mean the company has no AI opportunity — it can mean the
update simply didn't mention one, which sits outside what the skill can
see). B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("judgment" → "the update" — the
naive assumption that ranking AI-readiness takes Claude's own judgment
about the companies, corrected to: it works from what's in the update).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. No source beat was AI-VIDEO, pantry, or a
human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** Does Claude decide, using its own
judgment, which portfolio company is most ready for AI investment — or is
it doing something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
