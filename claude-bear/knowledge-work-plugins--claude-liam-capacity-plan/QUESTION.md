# QUESTION — knowledge-work-plugins--claude-liam-capacity-plan

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-capacity-plan/beat_sheet.json`.
That source sheet is a 7-beat Teardown "skill-teardown" reel for the Anthropic
`capacity-plan` skill, brand `claude-liam`, @NikBearBrown. It carries real,
specific facts (not unfilled template placeholders): the skill plans resource
capacity — workload analysis and utilization forecasting — and applies when
heading into quarterly planning, the team feels overallocated and you need
the numbers, deciding whether to hire or deprioritize, or stress-testing
whether upcoming projects fit the people you have (source B00/B03). Claude
reads one `SKILL.md` file before acting (source B01 anatomy: "a skill is a
folder... the file is the program") and executes its Steps section linearly,
no branching unless a step says so (source B02 pipeline). The
`source_skill` path it names does not exist on this machine (different
machine's home directory), but the source *beat_sheet.json*'s own narration
already states the skill's function in enough detail to redo faithfully —
no reconstruction needed. There is no separate SCRIPT.md in the source
folder; its `beats[*].narration_text` served as the locked script, same as
the `knowledge-work-plugins--claude-liam-fraud-detection` /
`healthcare--claude-liam-fraud-detection` sibling pattern in this factory.

**What changes in this redo:** register Teardown → Plain. The source's B03
("Here is the Teardown moment... What it gets right: repeatable results.
What it bites: anything outside the spec.") and BVDT ("Know the limit: only
what the file says.") framed the skill's scope as a design verdict; that
judgment is removed here — B03 states only the mechanism and its two
failure directions as properties of the practice, never a verdict on
whether the skill was built well. The source's 7-beat shape (cold open /
anatomy / pipeline / design tell / verdict / handoff / outro) carried no
WRONG-GUESS, ANCHOR, or BOTH-DIRECTIONS beat — Teardown's shape does not
require them. hai-simple's Phase 1 structure does, so those are new here:
the wrong guess (a newcomer assumes Claude senses an overloaded team the
way an experienced manager would, reading strain into how a request is
phrased) falsified by what the skill actually is (it runs two fixed steps —
workload analysis, then utilization forecasting — against the numbers you
give it; hand it a request with no workload or capacity numbers attached
and there is nothing for either step to run on); the anchor (a team heading
into quarterly planning says they're slammed: the question is asked,
matched to "team feels overallocated, need the numbers", stepped through —
total each person's committed hours, project the load across the quarter —
and returns one answer: utilization at 118 percent, hire one person or cut
one project) planted at B02 and paid off at B03; both directions at B03
(ask the same workload/capacity numbers twice and the same utilization
figure and recommendation come back; ask something outside that frame —
say, whether the team's morale can take the load — and there's nothing
tailored to reach for). B00 replaced the source's `ClaudeComposerAsk` cold
open with `BrutalistHesitantWriter` per WRITER LAW ("instinct" → "the
file" — the newcomer's assumption that Claude senses overload by feel,
corrected to: it runs a written procedure against numbers). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. No source beat was AI-VIDEO, pantry, or a
human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** Does Claude tell whether a team is
overloaded by something like a manager's instinct for strain — or is it
doing something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
