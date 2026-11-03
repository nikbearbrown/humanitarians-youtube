# SCRIPT.md — Write Triggers, Not Topics. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-example-skill` (Teardown, walks the Anthropic
`example-skill` reference template — the SKILL.md schema for model-invoked
skills) — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop, no verdict); cold open replaced
with the BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a one-line topic summary would get their skill found. It
isn't enough — the description has to work as a trigger. So: does my
skill's trigger description tell Claude when to use it?

*(Text typed on screen: "Does my skill's / topic description / tell Claude
/ when to use it?" — trigger word "topic" corrects to "trigger", landing
on: "Does my skill's trigger description tell Claude when to use it?"
Parameters (42ms/char, 4% mistakeRate, 2% hesitateWithin, 8%
hesitateBetween, 26% jitter) are the sibling
`claude-plugins-official--claude-liam-agent-development`'s own post-fix,
proven-safe settings, applied from the start here since this text (63
chars / 4 lines) is comparable in length to that sibling's fixed text (60
chars) — see BUILD-LOG.md for the render-time verification.)*

## Body — the schema, the trigger template, the untestable gap

**NB01 — SKILL.md: four fields** (source B01, anatomy)
A skill is one file: SKILL.md, inside a folder under skills. Frontmatter
has four fields. Name is the identifier — required. Description is the
trigger — also required, and it deserves more attention than any other
field, because it's what Claude reads to decide whether to activate the
skill at all. Version and license are optional. For a complex skill, that
same folder can also hold reference material, examples, and helper
scripts — but the minimum is just the one file.

**NB02 — Three activation modes** (source B02, design)
The skill's own template for a good description: say it should be used
when the user asks a specific phrase, mentions a keyword, or discusses a
topic area. That's because Claude reads the description and decides to
activate on its own — nobody types anything to invoke it. A command only
runs when a user types the slash. An agent is something Claude spawns to
handle a subtask. Get the mode wrong, and you've built a command when you
needed a skill — and nobody ever sees it trigger.

**NB03 — Write it, ship it, hope** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Here's the gap: nothing here explains how Claude actually matches your
description against a request — no rule for how long it should be, or
which phrases carry the most weight. The only testing advice is to check
that your skill activates for expected queries, but there's no method
given for running that check — no example query, no way to see the match
happen. So most authors write a description, ship it, and never actually
see whether it fires.

## Close

**BCRY — carry-out**
A skill's description isn't a summary of what it does — it's the trigger
Claude reads to decide when to use it. Write it as an activation rule, not
a topic blurb.

**BHTF — your turn**
Your turn. Paste this into Claude: build a model-invoked skill for a
plugin that helps with database query optimization. Then check what comes
back: does the description name specific trigger phrases — a phrase
someone might say, a keyword, a topic — or does it just summarize what the
skill does? Does it include a 'when to use' section with concrete
examples? Did you check whether it overlaps with any other skill's
description? Are references, examples, or helper scripts split into their
own folders, or is everything crammed into one file? And did you actually
test it — hand Claude a realistic query and watch whether the skill
activates, or did you just call it done?

**BOUT — outro**
Write Triggers, Not Topics. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an activation question — does naming what the skill is about get it used at the right moment? |
| Wrong guess | B00 (WRITER LAW) | "topic" corrected to "trigger" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the four frontmatter fields and the description's dispatch role; the three activation modes (skill/command/agent) and why the description-as-trigger template exists |
| Anchor | the example-skill reference template itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill schema), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete consequence of the untestable-trigger gap (most authors ship without ever verifying the match works); BCRY states the design's requirement and its failure mode together (a trigger-written description activates correctly, a topic-only description doesn't) — together they cover what a good description does and what a weak one misses, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the example-skill reference template's SKILL.md specifies (the four-field
frontmatter, the description's activation role, the three-mode
skill/command/agent distinction, the optional directory structure, and the
absence of any stated matching mechanism or testing method) — not an
inference about hidden model internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B05's "gets it right / where it bites" list (the skills-vs-commands-vs-
agents distinction, the description-as-trigger good pattern, the five-point
content guidelines, the optional directory structure, and the overlap-
avoidance best practice on the "right" side; the unexplained version/license
runtime effect, the unspecified trigger-matching mechanism, the missing
testing methodology, no description-length guidance, and overlap avoidance
with no detection method on the "bites" side) is compressed into NB03,
keeping only the single fact a general audience needs and can act on — you
can't verify your description works, so most people never do — and dropping
the Claude-harness-internals gaps (embedding vs. keyword matching, the
version/license runtime question, overlap detection tooling) that assume a
technical audience simple/hai-simple doesn't target; Teardown framing
("gets it right," "where it bites") is stripped to a plain mechanism-and-
consequence description, per the NO JUDGMENT register check; BVDT's verdict
facts (four frontmatter fields, description-as-trigger, optional
directories, the same untested-match gap) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with the source's
prompt ("Build a model-invoked skill for a plugin that helps with database
query optimization") carried over unchanged — it was already a concrete,
paste-ready prompt needing no extra setup, so it's actually runnable by any
viewer today; BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ExampleSkillAnatomy` / `ExampleSkillDesign` / `ExampleSkillTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.

## Facts carried over from the source (available material)

The plugin's actual `SKILL.md` file (source path:
`claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md`)
is not present on this machine (the `plugins/` tree wasn't checked out
locally) — same situation as the `claude-cookbooks--claude-liam-creating-
financial-models` precedent. Every fact in this reel is instead carried
from the source reel's own already-narrated `beats[*].narration_text` (a
fully-built, already-reviewed Teardown cut of that file) and cross-checked
against the source's `PEDAGOGY.md`, which independently states the same
five teaching points and the same five gaps. Nothing beyond what those two
source documents state is asserted here.
