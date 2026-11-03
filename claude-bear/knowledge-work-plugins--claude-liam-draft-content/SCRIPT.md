# SCRIPT.md — Claude, Draft Content. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-draft-content` (Teardown, walks the Anthropic
`draft-content` partner-built skill — marketing content drafting) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed running a named skill gives Claude a new writing talent it
didn't have before. It doesn't — it's one file, scoped to one job. So:
Claude picked up a new writing talent. Wait — what does this skill actually
do?

*(Text typed on screen: "Claude got a / new writing talent. / Wait — what
does / this skill actually do?" — trigger word "talent" corrects to "file,"
landing on: "Claude got a new file. Wait — what does this skill actually
do?" Params follow the proven-safe fixed values from the sibling
`knowledge-work-plugins--claude-liam-design-mcp-workflow` build's B00 fix
(charMs 42, mistakeRate 4%, hesitateWithin 2%, hesitateBetween 8%, jitter
26) to keep the text comfortably inside its audio window.)*

## Body — anatomy, pipeline, this skill's one job

**B01 — A skill is a file** (source B01, anatomy)
A Claude skill is a folder Claude reads before it works. This one is called
draft-content. Its SKILL.md file holds the entire instruction set — plain
language, nothing hidden. Claude reads the file, then acts. The file is the
program.

**B02 — How Claude runs it** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and runs it — start to finish, no branching unless a step says otherwise.

**B03 — One specific job** (source B03, design tell — re-registered
Teardown → Plain, the "gets it right / where it bites" verdict pairing
dropped in favor of a plain scope statement)
This particular skill has one job: draft marketing content — blog posts,
social media, email newsletters, landing pages, press releases, and case
studies — with channel-specific formatting and SEO recommendations
attached. It's written for three moments — writing any marketing content,
generating headline or subject-line options, or adapting a message for a
specific platform, audience, and brand voice. Outside those three moments,
the file has nothing to say.

## Close

**BCRY — carry-out** (source BVDT, verdict — merged into a single carry-out
sentence per CARRY-OUT LAW)
A Claude skill isn't a new writing talent — it's one file doing one job.
Same input, same output, every time you run it, and only for the content
it's actually scoped to write.

**BHTF — your turn**
Your turn. Paste this into Claude: I need to draft a blog post announcing a
product update, formatted for both a company blog and a LinkedIn post. Read
through how you'd write that, and walk me through what you're about to do
before you do it. Watching the plan come first is how you actually see a
skill's scope, not just its description.

**BOUT — outro**
Claude, Draft Content. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a scope question — did Claude just gain a new writing talent, or is this narrower? |
| Wrong guess | B00 (WRITER LAW) | "talent" corrected to "file" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | B01–B02 | the file-as-program fact and the linear read-then-execute pipeline |
| Anchor | the draft-content skill itself, named at B00 and never dropped through B01–B03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into B03 + BCRY | B03 states what the skill's scope covers (three named moments) and what it doesn't (nothing outside them); BCRY states the mechanism's reliability and its boundary together (same input → same output, but only for what it's scoped to write) — together they cover what the skill does and does not reach, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the draft-content Skill's SKILL.md specifies (the file-as-instruction-set
fact, the linear steps pipeline, and the three named scope moments — any
marketing content, headline/subject-line options, platform-and-brand-voice
adaptation) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

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
the source's prompt structure carried over (asking Claude to draft a piece
of marketing content and explain its plan before acting on it — the same
artifact-vs-world/Plato move the source's own LENS-AUDIT.md flagged) —
reworded into one genuinely paste-ready sentence rather than the source's
awkwardly truncated quoted string ("I want to draft blog posts, social
media, email newsletters, landing pages, press releases. Read the
draft-content skill and walk me through what you will do before you do
it." reads as a request for six channels at once, not a runnable single
task); BOUT kept, re-skinned to the Humanitarians AI outro (`OutroSeries`).
Total: B00 + B01–B03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap. B01–B03 reuse the source's own
`SkillTeardownAnatomy`/`SkillTeardownPipeline`/`SkillTeardownMechanism`
components unchanged (documented as generic "for any skill teardown," so no
new component authoring or GATE L punt was needed — `./art scenes --check`
confirmed all patterns used in this sheet, including `WantQuote` and
`OutroSeries`, are RENDERABLE before slating).
