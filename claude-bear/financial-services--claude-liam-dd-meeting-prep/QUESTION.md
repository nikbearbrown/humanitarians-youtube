# QUESTION — financial-services--claude-liam-dd-meeting-prep

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-dd-meeting-prep/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `dd-meeting-prep` skill: prepare for due
diligence meetings — management presentations, expert network calls,
customer references, and advisor sessions; generates targeted question
lists, benchmarks to reference, and red flags to probe; used before any
diligence meeting or call. Triggers on "prep for management meeting",
"diligence call prep", "expert call questions", "customer reference
questions", or "meeting prep for [company]". Claude reads `SKILL.md` before
acting and executes the steps linearly (source anatomy/pipeline beats: one
file, read → execute → return). The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/private-equity/skills/dd-meeting-prep/SKILL.md`)
does not exist on this machine (different machine's home directory), but the
source *beat_sheet.json*'s own narration already states the skill's function
in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain (the source's B03
framed "what it gets right / where it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes Claude draws on some private sense of what makes a sharp diligence
question — instinct built from general deal experience) falsified by what
the skill actually is (it reads which meeting you're prepping for —
management presentation, expert network call, customer reference, or
advisor session — then builds a targeted question list, benchmarks to
reference, and red flags to probe, all from what the file defines for that
meeting type; ask it to prep a meeting type the file doesn't cover and it
has nothing tailored to reach for); the anchor (an expert network call
about a staffing company: one question — same-store margin trend — drafted,
benchmarked, asked live, then flagged when the answer leans on one large
client) planted at B02 and paid off at B03; both directions at B03 (prep
the same expert-network call twice and the question list, benchmarks, and
red flags come back identical; ask for a meeting type the file never
described — a regulator sit-down — and there's nothing tailored to reach
for, the prep stops exactly where SKILL.md does). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER LAW
("instinct" → "the file" — the naive assumption that the sharp questions
come from Claude's own feel for a deal, corrected to: it reads the meeting
type against a file). Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off, per hai-simple's channel skin. No source beat was AI-VIDEO,
pantry, or a human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** Does Claude draw on its own
instinct for what makes a sharp diligence question — or is it doing
something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
