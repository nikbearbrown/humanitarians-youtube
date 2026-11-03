# QUESTION — knowledge-work-plugins--claude-liam-analyze

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-analyze/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `analyze` skill: answer data questions,
from quick lookups to full analyses; use when looking up a single metric,
investigating what's driving a trend or drop, comparing segments over time,
or preparing a formal data report for stakeholders. Claude reads `SKILL.md`
before acting and executes the steps linearly (source anatomy/pipeline
beats: one file, read → execute → return; linear, no branching unless a
step says so). The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/data/skills/analyze/SKILL.md`)
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
assumes Claude's data analysis comes from something like an analyst's own
feel for what's interesting in the numbers) falsified by what the skill
actually is (it reads what kind of question you're asking — a single-metric
lookup, a trend-or-drop investigation, a segment comparison, or a formal
stakeholder report — then runs the steps written for that shape, in order;
ask it something outside those four shapes and it has no procedure tailored
to reach for); the anchor (weekly signups drop twelve percent: the question
is asked, matched to "trend or drop", stepped through — pull the metric,
break it down by segment, isolate what changed — and returns one answer:
organic search traffic fell while paid channels held steady) planted at B02
and paid off at B03; both directions at B03 (ask the same drop question
twice and the match, steps, and driver come back identical; ask for
something outside the four shapes — say, whether to cut next quarter's
marketing budget — and there's nothing tailored to reach for). B00 replaced
the source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
per WRITER LAW ("instinct" → "the file" — the naive assumption that the
analysis comes from Claude's own feel for the data, corrected to: it reads
the question against a file). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off, per hai-simple's channel skin. No
source beat was AI-VIDEO, pantry, or a human-drop slot — every source beat
was already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

**Question this reel actually answers:** Does Claude's data analysis come
from something like an analyst's own instinct for what's interesting — or
is it doing something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
