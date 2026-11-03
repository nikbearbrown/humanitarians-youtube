# QUESTION — financial-services--claude-liam-clean-data-xls

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-clean-data-xls/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `clean-data-xls` skill: it cleans up messy
spreadsheet data by trimming whitespace, fixing inconsistent casing,
converting numbers stored as text into real numbers, standardizing dates,
removing duplicate rows, and flagging columns that mix types — nothing
beyond that six-item list. It is used when data is messy, inconsistent, or
needs prep before analysis (triggers: "clean this data", "clean up this
sheet", "normalize this data", "fix formatting", "dedupe", "standardize this
column", "this data is messy"). Claude reads `SKILL.md` before acting and
executes a linear pipeline (source anatomy/pipeline beats: one file, read →
execute → return; no branching unless a step says so). The `source_skill`
path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/financial-analysis/skills/clean-data-xls/SKILL.md`)
does not exist on this machine (different machine's home directory), but the
source *beat_sheet.json*'s own narration already states the skill's function
in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
"design tell" framed the skill as "what it gets right: repeatable results /
what it bites: anything outside the spec" — a design-tell verdict, Teardown
judgment. Plain keeps only the mechanism (the six fixed operations) and its
two failure directions, no verdict on whether the skill was built well. The
source's 7-beat shape (cold open / anatomy / pipeline / design tell /
verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes "clean this data" is an open-ended request — Claude will notice
whatever looks messy and fix it using its own judgment) falsified by what
the skill actually is (it runs exactly six fixed operations — trim, case,
convert numbers, standardize dates, dedupe, flag mixed types — and nothing
outside that list; a column with the same currency symbol covering two
different currencies is messy but isn't on the checklist, so it passes
through unchanged); the anchor (one Revenue column carrying " 1,200 ",
"1300", "N/A", " 1,400.00 " — trimmed, then converted, then flagged because
"N/A" can't convert) planted at B02 and paid off at B03; both directions at
B03 (a value that converts cleanly from text to a number isn't verified as
the *correct* number — a typo converts just as cleanly as a true figure; a
column flagged as mixed-type isn't automatically broken — an ID column that
mixes numbers and letters on purpose gets the same flag). B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per
WRITER LAW ("judgment" → "a checklist" — the naive assumption that cleaning
messy data takes Claude's own judgment about what looks wrong, corrected to:
it runs a fixed list of six operations). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off, per hai-simple's channel skin. No
source beat was AI-VIDEO, pantry, or a human-drop slot — every source beat
was already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

**Question this reel actually answers:** When you tell Claude to "clean this
data," does it decide what looks wrong and fix it using its own judgment —
or is it doing something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
