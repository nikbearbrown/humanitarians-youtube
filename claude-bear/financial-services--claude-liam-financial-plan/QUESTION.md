# QUESTION — financial-services--claude-liam-financial-plan

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-financial-plan/beat_sheet.json`.
Like the `dcf-model` and `3-statement-model` sibling redos, this source sheet
is NOT a placeholder shell — its B00 narration states the Anthropic
`financial-plan` skill's real, specific facts in full: it builds or updates a
comprehensive financial plan covering retirement projections, education
funding, estate planning, and cash flow analysis; it's used for new client
onboarding, annual plan reviews, or scenario modeling; it triggers on
"financial plan", "retirement plan", "can I retire", "education funding",
"estate plan", "cash flow analysis", or "plan update". (The same sentence
recurs truncated mid-word in B03/BVDT/BHTF — a template character-limit
artifact, not a second, different fact; B00 carries the untruncated version.)
The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/wealth-management/skills/financial-plan/SKILL.md`)
does not exist on this machine (different machine's home directory), but the
source *beat_sheet.json*'s own narration already states the skill's function
in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown -> Plain (the source's B03
framed "what it gets right / what it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer assumes
Claude's financial plan reflects its own judgment about what's best for the
client, the way a human advisor who has gotten to know someone's situation
reaches a conclusion) falsified by what the skill actually is (it only
recognizes the cases SKILL.md names — onboarding, an annual review, a
scenario request — and only produces the four things the file names;
anything outside that list has no independent expertise underneath to fall
back on, because there is no step for it); the anchor (one input — the
retirement age — driving one output, the monthly savings target) planted at
B02 and paid off at B03 across a small scenario grid; both directions at B03
(a savings target that jumps a lot for a five-year change in retirement age
doesn't mean the skill is improvising — it's the same fixed steps, fed a
different number; a target that barely changes between two close retirement
ages doesn't mean the skill weighed them and judged both acceptable — it
means the inputs were close and the same steps produced a similar result).
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("judgment" -> "a skill" — the naive
assumption that a financial plan reflects Claude's own judgment call,
corrected to: it is Claude running a skill's fixed steps over the inputs it
was given). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off, per hai-simple's channel skin.

**Question this reel actually answers:** Does Claude's financial plan
reflect its own judgment about what's best for the client — or is it running
a fixed set of steps from a written skill file?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
