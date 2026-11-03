# SCRIPT.md — One File, One Job, Every Time. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-design-mcp-workflow` (Teardown, walks the Anthropic
`design-mcp-workflow` partner-built skill, Zoom plugin) — question, facts,
and body argument carried over; narration re-registered to Plain (explain,
then stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a skill hands Claude a new general ability. It doesn't —
it's one file, scoped to one job. So: Claude got a new ability. Wait — what
does this skill actually do?

*(Text typed on screen: "Claude got a / new ability. / Wait — what does /
this skill do?" — trigger word "ability" corrects to "file," landing on:
"Claude got a new file. Wait — what does this skill do?" Params follow the
proven-safe fixed values from the `claude-plugins-official--claude-liam-
agent-development` sibling's B00 fix (charMs 42, mistakeRate 4%,
hesitateWithin 2%, hesitateBetween 8%, jitter 26) rather than the pilot's
original higher-hesitation defaults, to keep the ~55-character/4-line text
comfortably inside its audio window.)*

## Body — anatomy, pipeline, this skill's one job

**B01 — A skill is a file** (source B01, anatomy)
A Claude skill is a folder Claude reads before it works. This one is called
design-mcp-workflow. Its SKILL.md file holds the entire instruction set —
plain language, nothing hidden. Claude reads the file, then acts. The file
is the program.

**B02 — How Claude runs it** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and runs it — start to finish, no branching unless a step says otherwise.

**B03 — One specific decision** (source B03, design tell — re-registered
Teardown → Plain, the "gets it right / where it bites" verdict pairing
dropped in favor of a plain scope statement)
This particular skill has one job: design a Zoom MCP workflow for Claude.
It's written for three moments — deciding whether Zoom's MCP tools fit a
task, planning a tool-based AI workflow, or separating MCP responsibilities
from Zoom's REST API. Outside those three moments, the file has nothing to
say.

## Close

**BCRY — carry-out** (source BVDT, verdict — merged into a single carry-out
sentence per CARRY-OUT LAW)
A Claude skill isn't a new ability — it's one file doing one job. Same
input, same output, every time you run it, and only for what that file
actually covers.

**BHTF — your turn**
Your turn. Paste this into Claude: I need to decide whether to use Zoom's
MCP tools or its REST API for a task. Read through how you'd design that
workflow, and walk me through what you're about to do before you do it.
Watching the plan come first is how you actually see a skill's scope, not
just its description.

**BOUT — outro**
One File, One Job, Every Time. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a scope question — did Claude just gain a new ability, or is this narrower? |
| Wrong guess | B00 (WRITER LAW) | "ability" corrected to "file" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | B01–B02 | the file-as-program fact and the linear read-then-execute pipeline |
| Anchor | the design-mcp-workflow skill itself, named at B00 and never dropped through B01–B03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into B03 + BCRY | B03 states what the skill's scope covers and what it doesn't (three named moments, nothing outside them); BCRY states the mechanism's reliability and its boundary together (same input → same output, but only for what the file covers) — together they cover what the skill does and does not reach, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the design-mcp-workflow Skill's SKILL.md specifies (the file-as-instruction-
set fact, the linear steps pipeline, and the three named scope moments —
Zoom MCP fit, tool-based workflow planning, MCP vs. REST separation) — not
an inference about hidden model internals. Per simple's ONE-FLAG LAW, when
the source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01 and B02 kept as one beat each, content
essentially unchanged since the source text was already a plain factual
description, not Teardown judgment; B03's "what it gets right: repeatable
results / what it bites: anything outside the spec" verdict pairing is
stripped to a plain scope statement (three named moments, nothing outside
them), per the NO JUDGMENT register check; BVDT's verdict facts (repeatable
same-input/same-output execution, and the file-only limit) are merged into
the single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with
the source's prompt structure carried over (asking Claude to design the
Zoom MCP-vs-REST decision and explain its plan before acting on it — the
same artifact-vs-world move the source's own LENS-AUDIT.md flagged as a
Plato move) — reworded into a single, genuinely paste-ready sentence rather
than the source's slightly garbled truncated string; BOUT kept, re-skinned
to the Humanitarians AI outro (`OutroSeries`). Total: B00 + B01–B03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap. B01–B03 reuse the source's own
`SkillTeardownAnatomy`/`SkillTeardownPipeline`/`SkillTeardownMechanism`
components unchanged (they are documented as generic "for any skill
teardown," so no new component authoring or GATE L punt was needed —
`./art scenes --check` confirmed all patterns used in this sheet, including
`WantQuote` and `OutroSeries`, are RENDERABLE before slating).
