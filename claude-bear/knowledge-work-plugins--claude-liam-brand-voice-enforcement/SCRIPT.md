# SCRIPT.md — Check the Spec, Not the Vibe. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-brand-voice-enforcement` (Teardown, walks the Anthropic
`brand-voice-enforcement` Skill) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

**Source-material note:** the source reel's own narration carries several
unfilled `>` placeholders (in B00, B03, BVDT, BHTF) where the specific
brand-voice rules the Skill checks were never written in — the source's
`source_skill` path points at a machine this build has no access to, and no
copy of the actual `brand-voice-enforcement/SKILL.md` exists anywhere in
this workspace (checked). Per the redo contract's "facts must be true and
current... when in doubt, describe behavior generically," those gaps are
filled with the generic, load-bearing facts the source's own B01/B02 already
establish with confidence (a skill is a folder with a SKILL.md that Claude
reads before acting; the Steps section runs linearly) rather than invented
specifics about what any particular brand's rules say. No claim is made
about brand-voice-enforcement's actual rule list, because the source never
supplied one.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude just knows their brand's voice from training. It
doesn't — it checks against a written spec. So: does Claude already check my
brand's voice?

*(Text typed on screen: "Does Claude\nalready know\nmy brand's voice?" —
trigger word "know" corrects to "check", landing on: "Does Claude already
check my brand's voice?" 3 lines, 33 characters — short enough to leave
comfortable margin inside the >=9s TIMING LAW window at a moderate charMs,
per the fix pattern documented on the `claude-plugins-official--claude-liam-
agent-development` sibling, applied proactively here rather than
discovered by a failed first render.)*

## Body — anatomy, pipeline, the actual job

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
brand-voice-enforcement. Its SKILL.md file holds the full instruction set,
in plain language — no hidden logic. Claude reads it, then acts. The file
is the program.

**NB02 — Steps, in order** (source B02, pipeline)
The instructions are laid out in a Steps section. Claude reads each step in
order and runs it — linear, no branching unless a step says otherwise.

**NB03 — Check, don't guess** (source B03, design tell — re-registered
Teardown → Plain, and the source's unfilled `>` placeholder replaced with
the generic mechanism its own B01/B02 already commit to, per the
source-material note above)
Here's the actual job: check a piece of writing against whatever rules the
SKILL.md lists — banned words, preferred phrasing, tone, whatever it
actually says — and flag anything that doesn't match. Same file, same
rules, every single run.

## Close

**BCRY — carry-out**
brand-voice-enforcement doesn't know your brand's voice — it checks your
writing against whatever its SKILL.md actually lists. Same input, same
output, every time. The limit is exactly what the file says, nothing more.

**BHTF — your turn**
Your turn. Paste this into Claude: My brand voice rules are — no
contractions, no exclamation points, always say customers, never users.
Check this paragraph against exactly those three rules and tell me which
line breaks which one. Don't flag anything outside that list. That's the
same discipline the skill runs on: check only what's written down, nothing
else.

**BOUT — outro**
Claude, Brand Voice Enforcement. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a knowledge question — does Claude already know a brand's voice, the way a person who's absorbed a style guide would? |
| Wrong guess | B00 (WRITER LAW) | "know" corrected to "check" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a skill is a folder with a SKILL.md Claude reads before acting; the Steps section runs linearly; the actual job is comparing a draft against whatever rules the file lists |
| Anchor | the brand-voice-enforcement skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time, same shape as the agent-development sibling |
| Both directions | folded into NB03 + BCRY | NB03 states what the check catches (anything the file actually lists); BCRY states the same design's boundary in the other direction (the limit is exactly what the file says, nothing more) — together they cover what the check catches and what it misses, matching the source's verdict beat, which paired the same two facts ("same input, same output, every run" / "know the limit: only what the file says") |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the source's own narration commits to without hedging (a skill is a folder
with a SKILL.md; Claude reads it before acting; the Steps section runs
linearly; the check runs against whatever the file lists; same input
produces same output) — not an inference about hidden model internals or
about the specific brand-voice rules the Skill enforces (which the source
never supplied — see source-material note above, not a flagged inference
but an acknowledged gap the script doesn't paper over with invented
specifics). Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right / where it bites" framing (repeatable
results / anything outside the spec) is compressed into NB03 as a plain
mechanism description (what the check does), with the "gets it right /
misses" pairing preserved but redistributed across NB03 (catches) and BCRY
(the limit) rather than kept as its own explicit list, per the NO JUDGMENT
register check; BVDT's verdict facts (repeatable results, "only what the
file says") are merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as
the your-turn handoff — the source's own prompt was itself an unfilled `>`
placeholder ("I want to >. Read the brand-voice-enforcement skill..."), so
rather than inventing a call to a specific Anthropic skill a general viewer
likely doesn't have installed, this redo writes a concrete, paste-ready
prompt that exercises the identical mechanism (an explicit, closed rule
list; check only what's listed) with materials any viewer already has —
their own draft text and three invented example brand rules used
illustratively, not as a factual claim about brand-voice-enforcement's
actual rule set; BOUT kept, re-skinned to the Humanitarians AI outro.
Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
