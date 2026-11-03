# QUESTION — financial-services--claude-liam-dd-checklist

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-dd-checklist/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `dd-checklist` skill: generate and track
comprehensive due diligence checklists tailored to the target company's
sector, deal type, and complexity; covers all major workstreams with request
lists, status tracking, and red-flag escalation; used when kicking off
diligence, organizing a data room review, or tracking outstanding items.
Claude reads `SKILL.md` before acting and executes the steps linearly
(source anatomy/pipeline beats: one file, read → execute → return). The
`source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/private-equity/skills/dd-checklist/SKILL.md`)
does not exist on this machine (different machine's home directory), but the
source *beat_sheet.json*'s own narration already states the skill's function
in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain (the source's B03
framed "what it gets right / where it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer assumes
Claude sizes up the specific deal and decides, from its own judgment, which
risks are worth chasing) falsified by what the skill actually is (it reads
the target's sector, deal type, and complexity, then builds the checklist
from workstreams the file already defines — hand it a sector the file never
lists and it has no independent research to reach for); the anchor (a
software company acquisition's "customer contracts" request traveling
requested → received → reviewed → flagged as a red flag for the deal team)
planted at B02 and paid off at B03; both directions at B03 (ask for that same
software acquisition checklist twice and the workstreams and request items
come back identical; ask for a deal type the file never described — a
mineral rights transfer — and there's nothing tailored to reach for, the
checklist stops exactly where SKILL.md does). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER LAW
("judgment" → "the file" — the naive assumption that building the checklist
takes Claude's own judgment about this deal's risks, corrected to: it
tailors from what the file already defines). Close re-skinned to `OutroCTA`
/ @HumanitariansAI with Liam's sign-off, per hai-simple's channel skin. No
source beat was AI-VIDEO, pantry, or a human-drop slot — every source beat
was already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

**Question this reel actually answers:** Does Claude use its own judgment to
decide what belongs in a due diligence checklist — or is it doing something
narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
