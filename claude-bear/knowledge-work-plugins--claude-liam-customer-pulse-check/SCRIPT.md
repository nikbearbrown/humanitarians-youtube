# SCRIPT.md — It Drafts the Reply. It Never Sends It. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-customer-pulse-check` (Teardown, walks the Anthropic
`customer-pulse-check` Claude Skill from the `knowledge-work-plugins` book)
— question, facts, and body argument carried over; narration re-registered
to Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would send replies to unhappy customers
automatically. It doesn't — it drafts them after finding the patterns
first. So: does Claude draft replies to unhappy customers?

*(Text typed on screen: "Does Claude / send replies / to unhappy /
customers?" — trigger word "send" corrects to "draft", landing on: "Does
Claude draft replies to unhappy customers?" Rates reused from the
`knowledge-work-plugins--claude-liam-audit-support` sibling's proven
working configuration (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text), which cleared the >=8s TIMING LAW floor cleanly with a
comparably short text.)*

## Body — anatomy, pipeline, what customer-pulse-check actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
customer-pulse-check. It's just one file, SKILL.md, written in plain
language — no hidden logic. Claude reads it, then acts on what it says.
The file is the program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside, the instructions are steps, and Claude runs them in order. First:
pull complaints from PayPal disputes, HubSpot tickets, and review exports.
Then: find the themes that repeat. Then: rank the top three and draft a
reply for each. No branching, unless a step itself tells it to branch.

**NB03 — Finds the pattern, drafts the reply** (source B03, design tell —
re-registered Teardown → Plain: the source's "gets it right: repeatable
results / what it bites: anything outside the spec" framing is dropped for
a plain statement of the mechanism and its boundary)
This particular skill is built for one job: turning scattered complaints
into a short, fixable list. Give it a since-date and it pulls from PayPal,
HubSpot, and reviews, groups the recurring themes, and drafts a reply
template for each of the top three. It doesn't decide which replies go
out. It drafts them — sending one is still a person's call.

## Close

**BCRY — carry-out**
Customer-pulse-check finds the repeating complaints and drafts a reply for
each — it never decides which ones actually go out.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a stack of customer complaints.
Before drafting any responses, find the three that come up most often,
tell me what people are actually saying, and only then draft a reply for
each — leave it to me whether any of them goes out. That's the same order
customer-pulse-check follows — find the pattern, draft the reply, and
leave sending it to a person.

**BOUT — outro**
It Drafts the Reply. It Never Sends It. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a send-or-draft question — does Claude resolve the customer's complaint itself, or just find the pattern and draft a reply? |
| Wrong guess | B00 (WRITER LAW) | "send" corrected to "draft" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the linear step pipeline Claude runs it through (pull complaints, find themes, rank top three, draft replies) |
| Anchor | the customer-pulse-check skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (pulls complaints, groups themes, drafts replies) and what it does not do (decide which reply is sent); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the customer-pulse-check Skill's SKILL.md specifies (the one-file
folder structure, the linear step execution, the PayPal/HubSpot/review
synthesis into a top-3 fixable-issues list, the optional since-date
argument, the drafted response templates, and the same-input/same-output
determinism) — not an inference about hidden model internals. Per
simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each; B03's Teardown "gets it right: repeatable results / what it bites:
anything outside the spec" framing is restated in NB03 as a plain
mechanism-and-boundary fact (what the skill finds and drafts, and what it
declines to decide) rather than a strengths/gaps verdict, per the NO
JUDGMENT register check; BVDT's verdict facts (same input → same output
every run; limited to what the file specifies) are merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the
source's prompt text is adapted rather than copied verbatim — the source
asked the viewer to "read the customer-pulse-check skill," which requires
a plugin install a general viewer won't have, so this redo substitutes an
equivalent, actually paste-ready prompt that exercises the same
find-before-draft-before-send habit ("find the three that come up most
often... then draft a reply... leave it to me whether any of them goes
out") without depending on any specific Skill file; BOUT kept, re-skinned
to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT
= 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
