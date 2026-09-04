# SCRIPT.md — It Scores and Routes. It Doesn't Decide. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-kyc-rules` (Teardown, walks the Anthropic `kyc-rules`
Claude Skill from the `financial-services` book's `kyc-screener` plugin) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would approve or reject a new client. It doesn't —
it scores the file against a rules grid. So: does Claude score a new
client's KYC file against the firm's rules?

*(Text typed on screen: "Does Claude / approve a new / client's KYC / file?"
— trigger word "approve" corrects to "score", landing on: "Does Claude
score a new client's KYC file?" Rates reused from the working
`financial-services--claude-liam-break-trace` sibling's configuration
(42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line text), which
cleared the >=8s TIMING LAW floor cleanly with a comparably short text.)*

## Body — anatomy, pipeline, what kyc-rules actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
kyc-rules. It's just one file, SKILL.md, written in plain language — no
hidden logic. Claude reads the file, then acts on what it says. The file
is the whole program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside, the instructions are steps, and Claude runs them in order. First:
read the parsed onboarding record. Then: apply each rule from the grid, in
order. Then: hand back the ratings and the flags. No branching, unless a
step itself tells it to branch.

**NB03 — Scores and Routes** (source B03, design tell — re-registered
Teardown → Plain: the source's "gets it right: repeatable results / what it
bites: anything outside the spec" framing is dropped for a plain statement
of the mechanism and its boundary)
This particular skill runs after another skill has already parsed a new
client's onboarding record into structured fields. Kyc-rules' job is to
apply the firm's KYC and AML rules grid to that record: assign a risk
rating, list every rule outcome with the rule that produced it, and flag
anything missing or worth escalating. It doesn't decide whether to accept
the client. It scores the file and routes it — the accept-or-reject call
stays with a person.

## Close

**BCRY — carry-out**
Kyc-rules scores a client file against the firm's own rules and flags what
needs a person — it never decides whether to accept anyone.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a set of compliance rules, and a
record I need to check against them. Before you tell me whether it passes,
walk me through each rule, whether the record satisfies it, and what's
missing — then hand the actual decision back to me. That's the same order
kyc-rules follows — score against the rules, flag what's missing, and
leave the decision to a person.

**BOUT — outro**
It Scores and Routes. It Doesn't Decide. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an approve-or-score question — does Claude decide the client's fate, or just grade the file? |
| Wrong guess | B00 (WRITER LAW) | "approve" corrected to "score" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the linear step pipeline Claude runs it through |
| Anchor | the kyc-rules skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (scores, cites the rule, flags) and what it does not do (decide the client's fate); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the kyc-rules Skill's SKILL.md specifies (the one-file folder structure,
the linear step execution, the rules-grid-to-risk-rating mechanism, the
dependency on kyc-doc-parse's prior parsing, and the same-input/same-output
determinism) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right: repeatable results / what it bites: anything
outside the spec" framing is restated in NB03 as a plain mechanism-and-
boundary fact (what the skill scores and routes, and what it declines to
decide) rather than a strengths/gaps verdict, per the NO JUDGMENT register
check; BVDT's verdict facts (same input → same output every run; limited
to what the file specifies) are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the source's prompt
text is adapted rather than copied verbatim — the source asked the viewer
to "read the kyc-rules skill," which requires a plugin install a general
viewer won't have, so this redo substitutes an equivalent, actually
paste-ready prompt that exercises the same score-before-decide habit
("walk me through each rule... then hand the actual decision back to me")
without depending on any specific Skill file; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
