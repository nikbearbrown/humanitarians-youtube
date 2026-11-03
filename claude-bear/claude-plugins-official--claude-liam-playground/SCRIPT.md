# SCRIPT.md — The Prompt Is The Deliverable. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-playground` (Teardown, walks the Anthropic `playground`
Claude Code plugin Skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians AI
skin.

## B00 — cold open (BrutalistHesitantWriter)
You might expect a settings panel that hands you back raw values. It
doesn't — playground hands you back a prompt: natural language you copy
straight into Claude. So: will Claude build a settings panel that hands back
a prompt?

*(Text typed on screen: "Will Claude build / me a settings panel / that
hands back / values?" — trigger word "values" corrects to "a prompt",
landing on: "Will Claude build me a settings panel that hands back a
prompt?" Timing parameters matched to the fixed values on the
`claude-plugins-official--claude-liam-agent-development` sibling, which hit
the TIMING LAW floor at 42ms/char, 26% jitter, 4% mistakeRate, 2%
hesitateWithin, 8% hesitateBetween on a comparably-sized 4-line/~61-char
text — reverify by frame pull after render regardless.)*

## Body — anatomy, the state invariant, the enforcement gap

**NB01 — Six templates, four zones** (source B01, anatomy)
The skill organizes around six templates across four zones. Design decisions
use design-playground — components, layouts, spacing, color, typography.
Data and queries use data-explorer — SQL, APIs, pipelines, regex. Learning
uses concept-map — knowledge gaps and scope mapping. And review work gets
three templates — document-critique, diff-review, and code-map. Every
playground, whatever the template, has to meet five requirements: one
self-contained HTML file with everything inlined, a live preview that
updates on every change with no Apply button, a prompt written in natural
language instead of a dump of values, a copy button, and three to five
ready-made presets so it looks right the moment it loads.

**NB02 — One state object** (source B02, design/workflow)
The whole thing runs on one invariant: a single state object. Every control
writes to it when it changes, every part of the preview reads from it, and
one function — updateAll — refreshes both the preview and the prompt
together. Skip that, and the pattern doesn't just get messy, it breaks
silently: read a control's value straight from the page instead of from
state, and the live preview stops being reliable. The prompt itself has its
own rule — it has to read like an instruction, not a printout. Not
"border-radius: 8px, shadow-blur: 4" but "a tight border radius with a
subtle shadow" — only the settings that changed from default, with enough
context to act on even without the playground open.

**NB03 — Nothing enforces it** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Nothing in the skill actually stops the value-dump output from happening.
Whether the prompt reads as a natural instruction or as a colon-separated
list of settings is left entirely to whoever writes the code — there's no
check built in. That's exactly why opening the finished file in a browser is
a required last step, not an afterthought: it's the only way to catch a
prompt that came out as a dump instead of an instruction, before it ships.

## Close

**BCRY — carry-out**
The playground's real output is a prompt, not a list of settings. If what
it hands back can't be copied straight into Claude and acted on, it's not
finished — it's a value dump.

**BHTF — your turn**
Your turn. Paste this into Claude: build an interactive playground for
designing a card component — border radius, shadow, padding, and color —
with a live preview and a copyable prompt. Then check what comes out. Does
the prompt read like an instruction — a tight border radius, a subtle
shadow — or does it read like a printout of numbers? Does every control
update the preview the instant you move it, with no button to click? Are
there at least three presets already in place when it loads? And does
opening the file in a browser actually work?

**BOUT — outro**
The Prompt Is The Deliverable. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a deliverable question — does the playground hand back the values you picked, or something else? |
| Wrong guess | B00 (WRITER LAW) | "values" corrected to "a prompt" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the six templates / four zones and five core requirements; the state-object invariant (controls write, renders read, updateAll) and the natural-language prompt rule |
| Anchor | the playground skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete risk the unenforced rule creates (a value dump ships if nobody checks); BCRY states the design's payoff and its failure mode together (a natural-language prompt is the real deliverable; a value dump is not) — together they cover what the pattern catches and what it misses, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the playground Skill's SKILL.md specifies (the six templates and four zones,
the five core requirements, the state-object invariant, the
natural-language/non-value-dump prompt rule, and the fact that nothing in
the skill checks that rule automatically) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy / design)
+ B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT (outro).
This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each; B05's
long "gets it right / where it bites" list (six templates covering a
realistic range, the state pattern codified explicitly, the anti-value-dump
rule stated clearly, the anti-pattern list ordered by frequency, the
required open-in-browser step — versus templates being markdown descriptions
rather than starter HTML, no disambiguation rule between overlapping
templates, dark theme required but unspecified, qualitative prompt language
not templated per-template, and the external-dependency ban forcing
hand-rolled charts and syntax highlighting) is compressed into NB03, keeping
only the single fact a general audience needs and can act on — nothing
automatically enforces the natural-language prompt rule, so checking by hand
is required — and dropping the implementation-detail gaps (dark theme
specifics, per-template qualitative-language templates, the external-
dependency ban's downstream cost) that assume a technical audience
simple/hai-simple doesn't target; Teardown framing ("gets it right," "where
it bites") is stripped to a plain mechanism-and-consequence description, per
the NO JUDGMENT register check; BVDT's verdict facts (the working
state-object + natural-language-prompt format, and the enforcement gap it
leaves open) are merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as
the your-turn handoff, with the source's prompt (an interactive card-design
playground with border radius, shadow, padding, and color) carried over
unchanged — it was already a concrete, paste-ready prompt needing no extra
setup, so it's actually runnable by any viewer today; BOUT kept, re-skinned
to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT =
7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`PlaygroundAnatomy` / `PlaygroundDesign` / `PlaygroundTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway. NB01–NB03 are built fresh as
GRAPHIC (Manim) rather than reused from the source's `PlaygroundAnatomy` /
`PlaygroundDesign` / `PlaygroundTell` REMOTION components: those components
bake Teardown framing directly into on-screen text ("PLAYGROUND · TEARDOWN",
"What it gets right / where it bites", a GETS_RIGHT/BITES two-column split)
that is a register violation on screen, not just in narration — Plain
requires the visual framing to drop the verdict too, so this redo builds new
GRAPHIC beats on the shared generic "chip row" Manim template instead of
retrofitting judgment-shaped card components.
