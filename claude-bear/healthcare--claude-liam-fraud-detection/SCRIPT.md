# SCRIPT.md — It Flags and Ranks. It Never Convicts. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-fraud-detection` (Teardown, walks the Anthropic
`fraud-detection` Claude Skill from the `healthcare` book's plugin set) —
question, facts, and body argument carried over; narration re-registered
to Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would convict a Medicare claim as fraud. It
doesn't — it flags and ranks suspicious claims for a person to
investigate. So: does Claude flag fraudulent claims?

*(Text typed on screen: "Does Claude / convict / fraudulent / claims?" —
trigger word "convict" corrects to "flag", landing on: "Does Claude flag
fraudulent claims?" Rates reused from the working
`financial-services--claude-liam-kyc-rules` sibling's configuration
(42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line text), which
cleared the >=8s TIMING LAW floor cleanly with a comparably short text.)*

## Body — anatomy, pipeline, what fraud-detection actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
fraud-detection — eight files: a claims schema, reference data, a file for
loading claims, one for proposing detectors, an architecture doc, a
package file, a README, and the SKILL.md itself. Claude reads them, then
acts on what they say. The file is the program.

**NB02 — Relay: one output** (source B02, pipeline)
Claude points itself at that claims schema and the reference data, runs
the claims through the proposed detectors, and relays one thing back: a
ranked list of referrals. Each entry names the provider by NPI, the
suspected scheme, the dollar exposure, and a confidence score.

**NB03 — Flags and Ranks** (source B03, design tell — re-registered
Teardown → Plain: the source's "gets it right: repeatable results / what
it bites: anything outside the spec" framing is dropped for a plain
statement of the mechanism and its boundary)
fraud-detection's job is to screen a Medicare/Medicaid claims corpus for
fraud, waste, and abuse and produce those ranked, fully-cited referrals for
an SIU or program-integrity team. Same input, same output, every run. It
doesn't decide that fraud happened. It flags and ranks candidates — the
investigation, and the finding, stay with a person.

## Close

**BCRY — carry-out**
Fraud-detection ranks and cites suspect claims for a person to
investigate — it never decides that fraud happened.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a batch of claims data and want
to screen it for possible fraud or billing errors. Before you tell me
what's suspicious, walk me through how you'd rank and cite each flagged
claim — then hand the actual determination to a human reviewer.

**BOUT — outro**
It Flags and Ranks. It Never Convicts. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a convict-or-flag question — does Claude render the fraud finding, or just grade the claim? |
| Wrong guess | B00 (WRITER LAW) | "convict" corrected to "flag" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure (eight named files) and the relay pipeline that turns claims + detectors into ranked referrals |
| Anchor | the fraud-detection skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (screens, ranks, cites) and what it does not do (decide that fraud happened); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the fraud-detection Skill's beat_sheet.json (the locked source script)
already states — the eight-file folder contents, the relay-to-ranked-
referrals pipeline (NPI, scheme, dollar exposure, confidence), the screen-
for-FWA-and-produce-referrals mandate, and the same-input/same-output
determinism — not an inference about hidden model internals. Per simple's
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
boundary fact (what the skill screens/ranks/cites, and what it declines to
decide) rather than a strengths/gaps verdict, per the NO JUDGMENT register
check; BVDT's verdict facts (same input → same output every run; limited
to what the file specifies) are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the source's prompt
text is adapted rather than copied verbatim — the source asked the viewer
to "read the fraud-detection skill," which requires a plugin install a
general viewer won't have, so this redo substitutes an equivalent, actually
paste-ready prompt that exercises the same screen-then-hand-off habit
("walk me through how you'd rank and cite each flagged claim... then hand
the actual determination to a human reviewer") without depending on any
specific Skill file; BOUT kept, re-skinned to the Humanitarians AI outro.
Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
