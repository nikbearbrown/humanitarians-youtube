# SCRIPT.md — Philosophy Before Canvas. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-canvas-design` (Teardown, walks the Anthropic
`canvas-design` Skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians
AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed asking Claude for a poster returns a picture immediately.
It doesn't — it writes a design philosophy first. So: does asking Claude
for a poster return a picture eventually?

*(Text typed on screen: "Does asking Claude / for a poster return / a
picture / immediately?" — trigger word "immediately" corrects to
"eventually", landing on: "Does asking Claude for a poster return a picture
eventually?")*

## Body — the pipeline, the philosophy's shape, the built-in critique

**NB01 — Two steps, one skill** (source B01, anatomy)
Canvas-design is a two-step pipeline in one skill file. Step one: Claude
writes a design philosophy — it names an aesthetic movement, something like
Geometric Silence, and describes it across four to six paragraphs: form,
space, color, composition. Step two: Claude reads that philosophy back and
generates the canvas itself — a single PDF or PNG page. The philosophy
comes first, every time. It's the brief the second step follows.

**NB02 — Linear, no loops** (source B02, pipeline)
The pipeline runs once, straight through. A request comes in — a poster, a
piece of art, any static visual. Claude writes the philosophy to a markdown
file. Then it reads that file and generates the canvas — a PDF or PNG —
aimed at museum and magazine quality. There's no loop back to revise the
brief. The skill's own instructions even say to treat that first page like
a single page in a coffee-table book, waiting to be filled.

**NB03 — Five dimensions, named** (source B03, self-demo philosophy
structure)
Here's what a philosophy actually contains. First, a movement name — one
or two words, like Geometric Silence. Then five visual dimensions: space
and form, color and material, scale and rhythm, composition and balance,
and visual hierarchy. And one word keeps recurring by design:
craftsmanship. The skill's own instructions say to repeatedly emphasize
that the finished piece should look like it took countless hours to make.
That's a constraint written into the skill itself.

**NB04 — 90% visual, 10% text** (source B04, self-demo canvas output)
The canvas that comes out follows the philosophy directly. For Geometric
Silence, that means grid-based precision, bold negative space, and minimal
typography — a little essential text inside a lot of quiet room. The skill
describes this combination as Swiss formalism meeting Brutalist material
honesty, and tells Claude to treat the composition like a diagram from an
imaginary discipline. Nothing on the page is there just to decorate.

**NB05 — The final step runs first** (source B05, design tell — re-
registered Teardown → Plain, kept as the single most teachable fact rather
than the full "gets it right / where it bites" list)
There's one instruction worth noticing on its own. The skill's final step
begins with a line that's already written into it: "The user already said
it isn't perfect enough." That sentence isn't a response to feedback — no
one said anything yet. It's baked into the skill itself, so a refinement
pass runs on every single canvas, regardless of how the first draft
actually turned out.

## Close

**BCRY — carry-out**
Claude writes the design philosophy first, then draws from it — and the
make-it-better pass that follows is already written into the skill, so it
runs whether the first draft needed it or not.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a concept for a poster — a
meditation retreat in the mountains. Use the canvas-design skill. Before
you write any code, show me the design philosophy — the movement name and
its five visual dimensions — and tell me what the conceptual soul of the
piece will be. That phrase, the conceptual soul, comes straight from the
skill's own instructions. Asking for it before any code runs means Claude
commits to the aesthetic brief out loud, so you can redirect it before a
single pixel exists.

**BOUT — outro**
Philosophy Before Canvas. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an ordering question — does the poster request return a finished picture right away? |
| Wrong guess | B00 (WRITER LAW) | "immediately" corrected to "eventually" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB04 | the two-step pipeline, its linear no-loop shape, the philosophy's five named dimensions plus the craftsmanship mandate, and the canvas output that follows from it |
| Anchor | the canvas-design pipeline itself, named at B00 and never dropped through NB01–NB05 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB05 + BCRY | NB05 states the concrete mechanism (a pre-written critique line that runs on every canvas, not a response to actual feedback); BCRY states the pipeline's ordering payoff and the revision fact together (philosophy always comes first; the revision pass always runs, needed or not) — together they cover what the pipeline guarantees and what it does not check for, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct, verbatim-sourced
description of what the canvas-design Skill's SKILL.md specifies (the
two-step philosophy-then-canvas pipeline, the five-dimension philosophy
structure, the craftsmanship mandate, the coffee-table-book framing, the
90%-visual/10%-text canvas target, and the pre-written final-step critique
line) — not an inference about hidden model internals. Source's own
SOURCES.md declares B04's rendered canvas a SELF-DEMO (a Remotion
demonstration of the philosophy's visual principles, not a screenshot of
actual skill output); this redo's NB04 narration describes the philosophy's
stated visual principles directly rather than claiming to show real skill
output, so no flag is needed there either. Per simple's ONE-FLAG LAW, when
the source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 9 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03/B04 (self-demo philosophy / self-demo canvas) + B05
(teardown design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro).
This redo keeps that same 9-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02, B03→NB03, B04→NB04 kept
as one beat each; B05's Teardown framing ("ultimate design freedom," the
"pre-approves the human's critique" analysis, the "gets it right / where it
bites" pairing) is compressed into NB05, keeping only the single fact a
general audience needs and can act on — the final step's critique line is
pre-written into the skill and always runs — and dropping the evaluative
language per the NO JUDGMENT register check; BVDT's verdict facts (the
two-act ordering, the pre-baked critique) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with the source's
prompt ("I have a concept for a poster — a meditation retreat in the
mountains...") carried over unchanged — it was already a concrete,
paste-ready prompt needing no extra setup, so it's actually runnable by any
viewer today; BOUT kept, re-skinned to the Humanitarians AI outro with a
new title ("Philosophy Before Canvas.") reflecting the carry-out rather
than the source's bare topic title. Total: B00 + NB01–NB05 + BCRY + BHTF +
BOUT = 9 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`CanvasDesignAnatomy` / `CanvasDesignPipeline` / `CanvasDesignPhilosophy` /
`CanvasDesignCanvas` / `CanvasDesignTell` / `ClaudeVerdictArtifact`) with
B00 as a typed composer ask (REMOTION, not AI-VIDEO — the source never
called a generation service). NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's cold open, which this redo replaces per
hai-simple's mandate anyway.
