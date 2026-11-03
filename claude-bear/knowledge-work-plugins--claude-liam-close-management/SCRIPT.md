# SCRIPT.md — Same Close, Same Order. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-close-management` (Teardown, walks the Anthropic
`close-management` finance Skill — task sequencing, dependencies, and
status tracking for the month-end close) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed close-management would automate the whole month-end close
by itself. It doesn't — it only structures how Claude carries it out. So:
does close-management structure the way you run your month-end close?

*(Text typed on screen: "Does close-management / automate the way / I run
my / month-end close?" — trigger word "automate" corrects to "structure",
landing on: "Does close-management structure the way I run my month-end
close?" Timing params reused verbatim from the proven-safe fix on the
`claude-plugins-official--claude-liam-agent-development` sibling: charMs 42,
mistakeRate 4%, hesitateWithin 2%, hesitateBetween 8%, jitter 26 — this
text is 63 chars, close to that sibling's fixed 60-char text, well clear of
the 67-char text that ran out of its window at less-safe settings. Verify
media/B00.mp4 >= 8s and that the correction lands on screen before
compiling.)*

## Body — anatomy, the pipeline, the bounded spec

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is
close-management — it manages the month-end close process: task
sequencing, dependencies, and status tracking. Claude reaches for it when
planning the close calendar, tracking progress, spotting blockers, or
sequencing close activities by day. The SKILL.md inside is plain language,
no hidden code — Claude reads it, then acts. The file is the whole
program.

**NB02 — The pipeline is linear** (source B02, pipeline)
Inside the file is a Steps section — an ordered list. Claude reads each
step and executes it in that order: task sequencing and dependencies
aren't something Claude improvises, they're written into the steps
themselves. It's linear — step two doesn't start until step one finishes,
and there's no branching unless a step explicitly says to branch.

**NB03 — A bounded spec** (source B03, design tell — re-registered
Teardown → Plain: the source's "what it gets right / what it bites"
framing is stripped to a plain mechanism-and-scope description, per the
NO JUDGMENT register check)
close-management is a specification written as an instruction set — the
file names the task sequencing, dependencies, and status checks it covers,
in the order they happen. Follow it as written and the same close produces
the same sequence, every time. But it only covers what it names: anything
a real close needs that the file never wrote down, this skill doesn't
handle.

## Close

**BCRY — carry-out** (source BVDT, verdict — merged into a single
carry-out sentence per CARRY-OUT LAW)
Follow the close-management spec, and Claude runs the same close the same
way, every time — but only for what the spec actually names.

**BHTF — your turn** (source's prompt carried over, with its "statu"
truncation bug fixed to the full word "status tracking")
Your turn. Paste this into Claude: I want to manage my month-end close with
task sequencing, dependencies, and status tracking. Read the
close-management skill and walk me through what you will do, before you do
it. That last clause matters — asking Claude to explain itself first is
what surfaces the actual step order and dependencies it's about to follow.

**BOUT — outro**
Same Close, Same Order. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an automation question — does the skill run the whole close by itself? |
| Wrong guess | B00 (WRITER LAW) | "automate" corrected to "structure" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the folder-and-SKILL.md anatomy (no hidden code, Claude reads then acts) and the linear, non-branching Steps pipeline |
| Anchor | the close-management skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the spec covers and what it doesn't (repeatable within scope, silent outside it); BCRY states the same pairing as the single carry-out sentence — the payoff (same close, same way, every time) and its limit (only for what the spec names) together, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the close-management Skill's SKILL.md specifies (the folder-and-file
anatomy, the linear Steps pipeline, the task-sequencing/dependency/status-
tracking scope, and the bounded, spec-only coverage) — not an inference
about hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's "gets it right / where it bites" framing is compressed into NB03,
keeping the same two facts (repeatable within scope, silent outside it)
but stated as plain mechanism and consequence rather than a design verdict,
per the NO JUDGMENT register check; BVDT's verdict facts (same input, same
output, every run; limit: only what the file says) are merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with
the source's prompt carried over and its truncation bug ("statu") repaired
to "status tracking"; BOUT kept, re-skinned to the Humanitarians AI outro.
Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
