# QUESTION — financial-services--claude-liam-accrual-schedule

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-accrual-schedule/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `accrual-schedule` skill: it builds the
period-end accrual schedule; for each accrual it computes the entry, cites
the support, and drafts the journal entry; it is used during month-end
close; the drafted JE is a draft for controller approval, not a posting.
Claude reads `SKILL.md` before acting and executes the steps linearly
(source anatomy/pipeline beats: one file, read → execute → return). The
`source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/month-end-closer/skills/accrual-schedule/SKILL.md`)
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
assumes Claude decides, from its own accounting judgment, which expenses or
revenues belong in this period's close) falsified by what the skill
actually is (for each accrual it computes the entry and cites the support
that backs it — give it an expense with no supporting document and it has
nothing to cite, so it drafts nothing); the anchor (a December utility bill
not billed until January — identified, computed, cited, drafted, then it
stops, waiting) planted at B02 and paid off at B03; both directions at B03
(a drafted JE with a citation is not the same as a correct entry — it only
reflects what the cited document says; an accrual with no draft this period
does not mean something broke — it can mean that expense has no qualifying
support yet). B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("judgment" → "the support" — the
naive assumption that building the accrual schedule takes Claude's own
accounting judgment, corrected to: it computes from what's cited). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. No source beat was AI-VIDEO, pantry, or a
human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** Does Claude decide, using its own
accounting judgment, which expenses and revenues to accrue at period end —
or is it doing something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
