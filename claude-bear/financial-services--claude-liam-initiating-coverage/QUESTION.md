# QUESTION — financial-services--claude-liam-initiating-coverage

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-initiating-coverage/beat_sheet.json`.
This source sheet's narration already carries real, specific facts about the
Anthropic `initiating-coverage` skill: it creates institutional-quality
equity research initiation reports through a **5-task workflow** — (1)
company research, (2) financial modeling, (3) valuation analysis, (4) chart
generation, (5) final report assembly. Tasks must be executed individually
with verified prerequisites; tasks 3–5 have dependencies on earlier tasks.
Each task produces specific deliverables (markdown docs, Excel models,
charts, or DOCX reports). The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md`)
does not exist on this machine (different machine's home directory), but —
same situation as the `clean-data-xls` sibling redo — the source
*beat_sheet.json*'s own narration already states the skill's function in
enough detail to redo faithfully. No reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
"design tell" framed the skill as "what it gets right: repeatable results /
what it bites: anything outside the spec" — Teardown judgment on the
design choice itself. Plain keeps only the mechanism (the five ordered,
dependency-gated tasks) and its two failure directions, no verdict on
whether the skill was built well. The source's 7-beat shape (cold open /
anatomy / pipeline / design tell / verdict / handoff / outro) carried no
WRONG-GUESS, ANCHOR, or BOTH-DIRECTIONS beat — Teardown's shape does not
require them. This redo's Phase 1 structure does, so those are new: the
wrong guess (a newcomer assumes "initiate coverage" means Claude writes the
whole report in one continuous pass, in whatever order looks natural)
falsified by what the skill actually is (five fixed tasks, executed in
order, each requiring the previous task's verified deliverable before it
runs — ask it to jump straight to valuation before a financial model
exists, and there's nothing to value); the anchor (one ticker's coverage
package moving through all five task-cards — research, model, valuation,
charts, report — planted at B02 and paid off at B03); both directions at
B03 (finishing the chain proves the dependencies were respected — no step
ran on a missing input — but it does not prove the analysis inside each
step is sound; conversely, a task refusing to start on a missing deliverable
is a sequencing gap, not proof the earlier research was bad). B00 replaced
the source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
per WRITER LAW ("instantly" → "five ordered tasks" — the naive assumption
that asking for coverage produces the whole report in one pass, corrected
to: it runs a fixed five-task pipeline with dependencies). Close re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per hai-simple's
channel skin. No source beat was AI-VIDEO, pantry, or a human-drop slot —
every source beat was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no beat replacement beyond B00 itself.

**Question this reel actually answers:** When you ask Claude to "initiate
coverage" on a stock, does it just generate the whole research report in
one pass — or is it doing something more structured?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
