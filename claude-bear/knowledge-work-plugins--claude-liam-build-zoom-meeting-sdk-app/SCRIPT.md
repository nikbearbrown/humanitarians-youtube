# SCRIPT.md — It Doesn't Design the App. It Follows the File. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-build-zoom-meeting-sdk-app` (Teardown, walks the
Anthropic `build-zoom-meeting-sdk-app` Claude Skill from the
`knowledge-work-plugins` book's Zoom partner-built plugin) — question,
facts, and body argument carried over; narration re-registered to Plain
(explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would design a whole Zoom meeting app from
scratch. It doesn't — it follows steps written in a reference file. So:
does Claude follow steps for a whole Zoom meeting app?

*(Text typed on screen: "Does Claude / design a whole / Zoom meeting /
app?" — trigger word "design" corrects to "follow steps for", landing on:
"Does Claude follow steps for a whole Zoom meeting app?" Rates reused
from the working `financial-services--claude-liam-kyc-rules` sibling's
configuration (42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line
text), which cleared the >=9s TIMING LAW floor cleanly with a comparably
short text.)*

## Body — anatomy, pipeline, what build-zoom-meeting-sdk-app actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
build-zoom-meeting-sdk-app. Inside: a RUNBOOK.md and a SKILL.md, then one
folder per platform — android, electron, iOS, Linux, macOS,
react-native. Six platforms, one shared reference. The file is the
program.

**NB02 — Linear pipeline** (source B02, pipeline)
The instructions are steps, and Claude runs them in order. Read the
SKILL.md. Execute each step — join the meeting, handle the waiting room,
apply the platform's rules. Return the result. No branching, unless a
step itself tells it to branch.

**NB03 — Reference, Not Decision** (source B03, design tell —
re-registered Teardown → Plain: the source's "gets it right: repeatable
results / what it bites: anything outside the spec" framing is dropped
for a plain statement of the mechanism and its boundary)
This particular skill is a reference, not a decision-maker. It's read
only after a build has already been routed to a meeting-embed
workflow — that routing happened somewhere else, before this file ever
opens. Once it's open, it supplies the platform's exact rules: real
meeting joins, auth and join flows, waiting-room handling, meeting-bot
patterns, one platform folder at a time. It doesn't choose the platform
or decide to embed a meeting at all. It supplies the rules for the one
already chosen.

## Close

**BCRY — carry-out**
Build-zoom-meeting-sdk-app never decides to build a Zoom integration — it
hands Claude the platform's exact join rules once that decision's already
made.

**BHTF — your turn**
Your turn. Paste this into Claude: I've already decided to add a video
call to my app, and I've picked the platform. Before you write any
integration code, walk me through the platform's exact rules for joining
a call, handling a waiting room, and any bot behavior I need to account
for. That's the same order build-zoom-meeting-sdk-app follows — the
decision to embed comes first, the platform's rules come after.

**BOUT — outro**
It Doesn't Design the App. It Follows the File. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a design-or-follow question — does Claude improvise the Zoom integration, or read a file that already has the platform's rules? |
| Wrong guess | B00 (WRITER LAW) | "design" corrected to "follow steps for" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure (RUNBOOK.md, SKILL.md, six platform folders) and the linear step pipeline Claude runs it through |
| Anchor | the build-zoom-meeting-sdk-app skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (supplies the platform's exact rules once a meeting-embed build is routed to it) and what it does not do (choose the platform, decide to embed at all); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the build-zoom-meeting-sdk-app Skill's own narration specifies (the
RUNBOOK.md/SKILL.md/six-platform-folder structure, the linear step
execution, the "used after routing to a meeting-embed workflow" scoping
language, and the same-input/same-output determinism) — not an inference
about hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each; B03's Teardown "gets it right: repeatable results / what it bites:
anything outside the spec" framing is restated in NB03 as a plain
mechanism-and-boundary fact (what the skill supplies, and what it declines
to decide) rather than a strengths/gaps verdict, per the NO JUDGMENT
register check; BVDT's verdict facts (same input → same output every run;
limited to what the file specifies) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the source's
prompt text is adapted rather than copied verbatim — the source asked the
viewer to "read the build-zoom-meeting-sdk-app skill," which requires a
plugin install a general viewer won't have, so this redo substitutes an
equivalent, actually paste-ready prompt that exercises the same
decide-then-follow-the-rules habit ("before you write any integration
code, walk me through the platform's exact rules...") without depending
on any specific Skill file; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
