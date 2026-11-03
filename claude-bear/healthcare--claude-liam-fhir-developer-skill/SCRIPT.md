# SCRIPT.md — It Doesn't Just Pass or Fail. It Names the Problem. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-fhir-developer-skill` (Teardown, walks the Anthropic
`fhir-developer-skill` Claude Skill from the `healthcare` book's plugin
set) — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop, no verdict); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians
AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude just returns pass or fail on a bad FHIR request. It
doesn't — it returns the exact code that names the problem. So: does
Claude return the exact code for a bad request?

*(Text typed on screen: "Does Claude / just return / pass-fail on a / bad
FHIR request?" — trigger word "pass-fail" corrects to "the exact code",
landing on: "Does Claude just return the exact code on a bad FHIR
request?" Rates reused from the working `financial-services--claude-liam-
kyc-rules` / `healthcare--claude-liam-clinical-note-extract-skill`
configuration (42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line
text), which cleared the >=8s TIMING LAW floor cleanly with a comparably
short text.)*

## Body — anatomy, pipeline, what the skill actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
fhir-developer-skill. It has three items: SKILL.md holds the full
instruction set, in plain language — no hidden logic — plus references
and scripts folders alongside it. Claude reads the file, then acts on
what it says.

**NB02 — Three-step pipeline** (source B02, pipeline)
Inside SKILL.md, the pipeline lives in its Steps section: read a step,
execute it, return the result. Claude works through the steps in order —
linear, with no branching unless a step itself says otherwise.

**NB03 — Status code is the spec** (source B03, design tell —
re-registered Teardown → Plain: the source's "gets it right: repeatable
results / what it bites: anything outside the spec" framing is dropped for
a plain statement of the mechanism and its boundary)
fhir-developer-skill validates FHIR resources and returns the exact HTTP
status code for what's wrong — four twenty-two for an invalid enum value,
four twelve for an ETag mismatch on a conditional update. The status code
is the spec: same input, same code, every run. What it won't validate is
anything outside that spec.

## Close

**BCRY — carry-out**
Fhir-developer-skill doesn't just pass or fail a request — it returns the
exact status code that names what's wrong, and that code is the spec.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm validating structured records
against a schema. For each one that fails, don't just say pass or fail —
give me the specific reason, and a distinct code for it. Walk me through
your plan before you run anything. That's the same discipline
fhir-developer-skill follows — a specific code for a specific problem,
plan before you execute.

**BOUT — outro**
It Doesn't Just Pass or Fail. It Names the Problem. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a pass-fail-or-code question — does Claude just gate a request through/out, or name the exact reason? |
| Wrong guess | B00 (WRITER LAW) | "pass-fail" corrected to "the exact code" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the three-step pipeline (read a step, execute it, return the result) Claude runs it through |
| Anchor | "the exact status code" — planted at B00, resolved at NB03 with the concrete 422/412 examples, compressed at BCRY | a single running idea (specific code, not a binary gate), not a separate case introduced and later revisited — the same phrase and the same two example codes carry it end to end |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (returns the exact code for what's wrong, same input → same code every run) and what it does not do (validate past its own spec); BCRY states the same pair as the carry-out |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the fhir-developer-skill Skill specifies (the folder/file structure,
the three-step pipeline, the specific status-code mechanism, and its
same-input/same-output determinism) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated. The source's own AUDIT.md
records every Phase-1 accuracy check as PASS, so no content correction was
needed either (contrast the clinical-note-extract-skill sibling, whose
source had a documented, uncorrected accuracy error).

## Beat-count note (redo)

Source is 6 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BHTF (your turn) + BOUT (outro) —
no BVDT verdict beat; the source's own REBUILD-LOG.md records that BVDT
was already stripped at build time (body < 5 beats / < 180 words, below
the verdict threshold). This redo is 7 beats: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01 kept as one beat; B02→NB02 kept as
one beat; B03's Teardown framing is restated in NB03 as a plain
mechanism-and-boundary fact rather than a strengths/gaps verdict, per the
NO JUDGMENT register check; BHTF kept as the your-turn handoff, but the
source's prompt text is adapted rather than copied verbatim — the source
asked the viewer to "read the fhir-developer-skill skill," which requires
a plugin install a general viewer won't have, so this redo substitutes an
equivalent, actually paste-ready prompt that exercises the same
specific-reason-not-pass/fail discipline on any schema-validation task,
without depending on any specific Skill file; BOUT kept, re-skinned to the
Humanitarians AI outro. The one net addition versus the source is **BCRY**,
the carry-out beat: simple's CARRY-OUT LAW makes a single, separately-held
carry-out sentence a mandatory beat of the Plain-register spine (written
before any other narration, per the law), a requirement that does not
depend on whether the source happened to keep a verdict beat to fold from.
The source satisfied its own format's closing move through BVDT before
that beat was stripped for brevity; this redo adds the mandatory
carry-out beat rather than omit the format's required close. Total: B00 +
NB01–NB03 (3) + BCRY + BHTF + BOUT = 7 beats (source: 6; +1 for the
mandatory CARRY-OUT LAW beat — this addition is the format's structural
requirement, not new invented content).

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeTitleOutro`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
