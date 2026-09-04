# SCRIPT.md — Plan, Then Check the Plan. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-frontend-design` (Teardown, walks the Anthropic
`frontend-design` Claude Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would just guess at a good design. It won't — a
design plan comes first. So: ask Claude for a landing page — will it just
guess something nice?

*(Text typed on screen: "Ask Claude for / a landing page. / It'll just
guess / something nice?" — trigger word "guess" corrects to "plan", landing
on: "Ask Claude for a landing page. It'll just plan something nice?")*

## Body — anatomy, the process, restraint, the catch

**NB01 — Five principles, three traps** (source B01, anatomy)
The skill covers five design principles. One: the hero is a thesis — open
with the most characteristic thing in the subject's world, in whatever form
makes sense. Two: typography carries personality — pair typefaces
deliberately for this brief, not the same families you'd reach for on any
other project. Three: structure is information — numbered markers only if
the content is actually a sequence. Four: motion serves the subject —
orchestrated moments beat scattered effects. Five: complexity matches the
vision — minimalism needs precision, maximalism needs execution. And it
blocks three AI design defaults by name: warm cream with a serif and
terracotta accent, near-black with acid-green, and broadsheet hairline
columns.

**NB02 — Plan, critique, code** (source B02, self-demo)
The process runs in two passes. First, a design plan with four parts: color
— four to six named hex values; type — a display face, a body face, and a
utility face if needed; layout — one-sentence descriptions and ASCII
wireframes to compare options; and a signature — the one element the page
will be remembered by. Then a critique: does any part of this plan read as
the default Claude would produce for any similar brief? If yes, it revises
and says what changed. Only after that check does it write any code.

**NB03 — Spend it once** (source B03, restraint + writing)
Restraint: spend your boldness in one place. Let the signature be the
memorable thing, and keep everything around it quiet — the Chanel rule,
look in the mirror before you leave the house and remove one accessory. And
words on a page exist for one reason: to help the person using it. Active
voice by default — "Save Changes," not "Submit." An error message says what
went wrong and how to fix it, plainly.

**NB04 — What the check catches** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable
mechanism fact plus its honest limit, rather than the full "gets it right /
where it bites" list)
There's one instruction here doing most of the real work: after Claude
drafts the plan, it has to ask itself a single question — does this read as
the default I'd produce for any similar brief? If yes, it revises before
writing a line of CSS. That catch happens before any code exists. What it
doesn't guarantee: how well Claude reads the actual subject in the first
place — the check catches a generic answer, not bad judgment in an original
one.

## Close

**BCRY — carry-out**
Claude doesn't design well by guessing — it designs well by drafting a
plan, then checking whether that plan is actually different from the
default. Skip the check, and the default comes back.

**BHTF — your turn**
Your turn. Paste this into Claude: Design a landing page for a handmade
ceramic studio. I want a strong visual identity — distinctive typography, a
considered palette, and one design element I won't have seen on other
ceramic studio sites. Use the frontend-design skill. Then watch: does it
name a subject and audience before choosing anything? Does it state a
palette as actual hex values? Does it tell you the signature element before
it writes any CSS? If it starts coding immediately — no plan, no
critique — the check got skipped, and that's the tell.

**BOUT — outro**
Plan, Then Check the Plan. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a trust question — does Claude just guess at good design, or does it plan first? |
| Wrong guess | B00 (WRITER LAW) | "guess" corrected to "plan" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the five design principles and three blocked defaults, then the two-pass plan/critique/code process itself |
| Anchor | the frontend-design skill's own plan-then-critique gate, named at B00 and never dropped through NB01–NB04 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB04 + BCRY | NB04 states what the critique step catches (a generic plan) and what it does not guarantee (good subject judgment in an original one); BCRY states the same pairing as the carry-out — plan without the check lets the default back in, and the check is what actually does the work, not the plan alone |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the `frontend-design` Skill's SKILL.md specifies (the five design
principles, the three named defaults, the two-pass plan/critique/code
process, the four-part plan token system, the restraint and writing rules,
and the critique gate's actual scope) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 8 beats: B00 (composer-ask cold open) + B01/B02/B03 (anatomy /
process / restraint) + B05 (teardown analysis) + BVDT (verdict) + BHTF
(your turn) + BOUT (outro). This redo keeps that same 8-beat shape: B00
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02,
B03→NB03 kept as one beat each; B05's "gets it right / where it bites" list
(names and blocks 3 AI design traps, forces a token system, inserts a
critique gate, makes every decision derive from the plan, restraint makes
over-design self-diagnosable — versus design quality still depending on
subject interpretation, "take one aesthetic risk" having no formula,
writing quality being unconstrained, the CSS-specificity note being a
warning and not a checker) is compressed into NB04, keeping only the single
fact a general audience needs and can act on — the critique step is what
actually catches a generic plan, and what it does not catch is subject
judgment — and dropping the implementation-level gaps (aesthetic-risk
formula, writing-quality enforcement, CSS-specificity checking) that assume
a technical audience simple/hai-simple doesn't target; Teardown framing
("gets it right," "where it bites") is stripped to a plain mechanism-and-
limit description, per the NO JUDGMENT register check; BVDT's verdict facts
(the four-part plan, the three blocked defaults, the critique question, the
restraint and writing rules) are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff, with the source's prompt
(a ceramic-studio landing page, using the frontend-design skill) carried
over unchanged — it was already a concrete, paste-ready prompt needing no
extra setup, so it's actually runnable by any viewer today; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB04 + BCRY +
BHTF + BOUT = 8 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`FrontendDesignAnatomy` / `FrontendDesignProcess` / `FrontendDesignRestraint`
/ `FrontendDesignTell` / `ClaudeVerdictArtifact`), with B00 as a typed
composer ask (REMOTION, not AI-VIDEO — the source never called a generation
service). NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's cold
open, which this redo replaces per hai-simple's mandate anyway. The source's
custom `FrontendDesign*` Remotion components hardcode Claude-fidelity-skin
colors and, for `FrontendDesignTell`, hardcode literal "WHAT IT GETS RIGHT /
WHERE IT BITES" Teardown-judgment column headers directly in the component
(only `sparkLine` is prop-exposed — confirmed by reading the .tsx source).
Reusing those components verbatim would bake forbidden judgment text and the
wrong palette into the redo regardless of narration changes, and editing a
shared library component to fit one redo is out of scope. NB01–NB04 are
instead built as fresh humanitarians-palette Manim GRAPHIC beats (this
reel's own `scenes.py`/`render_scenes.py`, the same reusable "chip row"
pattern used on the `claude-plugins-official--claude-liam-agent-development`
sibling), carrying the same facts without touching the source components.
