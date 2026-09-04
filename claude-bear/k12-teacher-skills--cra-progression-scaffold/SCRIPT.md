# SCRIPT.md — The CRA Ladder (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `cra-progression-scaffold` (a Plain-adjacent explainer walking the
CRA — Concrete, Representational, Abstract — progression applied to
1/3 + 1/2) — question, facts, and body argument carried over; narration
re-registered where the source drifted toward design-judgment language;
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
A teacher first types: three levels, run it separate. Not quite — the real
question is whether one lesson can run as three entry points. Here's how
the CRA ladder does that.

*(Text typed on screen: "When I tier one lesson / for three levels, / do I
run it / separate?" — trigger word "separate" (the single last content word
before the terminal "?") corrects to "as three entry points", landing on:
"When I tier one lesson for three levels, do I run it as three entry
points?" Component note carried over from the `k12-lesson-differentiation`
sibling's Gate V finding: `triggerWords`/`replacementWords` must each be a
single whitespace token — the component matches against one split token's
punctuation-stripped core, so a multi-word trigger never matches and the
correction silently never fires. Built the single-token trigger correctly
from the start this time.)*

## Body — the CRA ladder, one lesson, three rungs

**NB01 — Three rungs, one problem** (source B01, mechanism + THE ANCHOR
planted)
One third plus one half. Three rungs on one ladder. Concrete: fraction
circles — push a one-third piece and a one-half piece together and watch
five sixths appear. Representational: a tape diagram split into thirds and
halves, finding the shared unit before the arithmetic. Abstract: the
equation itself — one third plus one half equals two sixths plus three
sixths equals five sixths. A student below grade level starts at Concrete.
A student at grade level starts at Representational. A student above
starts at Abstract. Every rung climbs toward the same result.

**NB02 — One staircase, three starting steps** (source B02, mechanism)
The design move is the arrows between rungs, not the rungs themselves.
Three journeys run at once, all aimed at the same abstract destination. A
student who reaches five sixths with the circles is ready for the tape
diagram. A student who can draw the diagram is ready for the equation. The
rungs aren't separate tracks — they're one shared staircase, with three
places to start climbing.

**NB03 — The rung that helped yesterday** (source B02a, both directions —
what helps a novice can stop helping)
There's a catch called the expertise-reversal effect. The concrete support
that helps a beginner — the physical fraction pieces — becomes noise for a
student who already holds the representational picture in mind. The
support that was scaffolding turns into clutter. So the CRA ladder isn't a
fixed setting for a student — it's a path, and the rung that helped
yesterday may not help today.

**NB04 — THE ANCHOR PAYOFF — the contract behind the ladder** (source B02b,
mechanism, returns to the 1/3 + 1/2 rungs from NB01)
Scaffolding carries a three-part contract: contingency — support matched to
where the learner is right now; fading — steady withdrawal as skill grows;
and transfer — the learner ends up doing it alone. Skip fading, and support
that once matched five sixths on the circles just stays in place forever.
Removing a rung and checking whether the learning still holds is how you
find out if it was scaffolding or a permanent prop.

## Close

**BCRY — carry-out**
Claude doesn't build three separate lessons — it builds one shared target
with three rungs to reach it, and the test is whether every rung gets there
without skipping a step.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a sixth grade lesson on solving
one-step equations. Design the full CRA progression — a concrete task, a
representational task, and an abstract task — as three entry points into
one lesson, each one building toward the next.

**BOUT — outro**
The CRA Ladder. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is the standard differentiation assumption — three levels means three separate lessons |
| Wrong guess | B00 (WRITER LAW) | "separate" corrected to "as three entry points" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no dedicated wrong-guess beat to redistribute, so none is invented beyond this |
| Mechanism | NB01–NB04 | three rungs on one ladder (concrete/representational/abstract); the staircase design move; the expertise-reversal limit; the contingency/fading/transfer contract |
| Anchor | 1/3 + 1/2 = 5/6, planted NB01 (fraction circles → tape diagram → equation), held through NB02–NB03, PAID OFF at NB04 ("support that once matched five sixths on the circles") | a genuine planted-and-returned case, unlike a single-worked-example reel with nothing to return to |
| Both directions | NB03 | states both directions of the expertise-reversal effect: scaffolding helps a novice AND the same scaffolding stops helping (becomes noise) once the learner has moved up a rung |
| Carry-out | BCRY | one sentence, survives repetition, and answers B00's wrong guess directly (one shared target, not three separate lessons) |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
established CRA-progression and cognitive-load literature (Bruner's
concrete-representational-abstract sequence; Witzel's CRA implementation
work; the expertise-reversal effect; the contingency/fading/transfer
scaffolding contract — see SOURCES.md carried over from the source reel) —
not an inference about hidden model internals or unconfirmed behavior. Per
simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Register note (redo)

The source reel's B02a/B02b used a few Teardown-leaning phrases ("has
violated the contract," "the scaffold becomes a load-bearing wall") that
name a verdict on the design rather than just describing the mechanism.
This redo strips that framing: NB03/NB04 keep the same underlying facts
(the expertise-reversal effect; the three-part scaffolding contract; the
fading test) but state them as descriptions and consequences, not as
judgments on whether a lesson was well or badly designed — per Plain's "No
judgment" register check.

## Beat-count note (redo)

Source (`build.filled: 8, of: 8`) is B00 (ClaudeComposerAsk cold open) +
B01/B02/B02a/B02b (four body beats: CRA ladder, staircase principle,
expertise reversal, scaffolding contract) + B03 (verdict) + B04 (handoff) +
B05 (outro) = 8 beats. This redo keeps that exact 8-beat shape: B00 replaced
1:1 with BrutalistHesitantWriter; B01→NB01, B02→NB02, B02a→NB03, B02b→NB04
kept as one beat each; B03's two verdict facts (Claude can generate the
full CRA set on demand, and the reach-without-skipping test) compressed
into the single BCRY carry-out sentence (CARRY-OUT LAW: Plain carries one
carry-out sentence, not a bulleted verdict); B04 kept as the your-turn
handoff, source's generic "pick any math concept" framing replaced with a
concrete, paste-ready scenario (a sixth-grade one-step-equations lesson);
B05 kept, re-skinned to the Humanitarians AI outro (`OutroSeries`). Total:
B00 + NB01–NB04 + BCRY + BHTF + BOUT = 8 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source was already entirely REMOTION (`ClaudeComposerAsk`, `K12Fig02CRA`,
`ClaudeWindow`, `K12Fig07ExpertiseReversal`, `K12Fig08ScaffoldContract`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`). NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's cold open, which this redo replaces
per hai-simple's mandate anyway. The source's `K12Fig02CRA` /
`K12Fig07ExpertiseReversal` / `K12Fig08ScaffoldContract` components ARE
registered in this toolkit's scene library (confirmed via `./art scenes`),
but their colors are hardcoded to the Claude fidelity skin (no ink/accent/bg
props — `props: sparkLine` only) and cannot be repainted to the
humanitarians palette. Per hai-simple's channel-skin law (the whole channel
skin, not only the outro, moves to the humanitarians palette) and matching
the direct precedent set by the `k12-teacher-skills--claude-liam-k12-lesson-
differentiation` sibling (same book, same skill, same decision), NB01–NB04
are built fresh as GRAPHIC (Manim) beats on the same generic "chip row"
template that sibling used, carrying the same teaching points as the
source's Remotion figures rather than the fixed-palette components
themselves.
