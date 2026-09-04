# SCRIPT.md — Claude, Close Month. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-close-month` (Teardown, walks the Anthropic
`close-month` Claude skill — reconciles QuickBooks vs. payment processors,
flags gaps, writes a P&L narrative, exports a close packet) — question,
facts, and body argument carried over; narration re-registered to Plain
(explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone wondered if Claude would close the books using its own judgment.
It doesn't — it follows a written skill file, step by step. So: can Claude
close my books using a skill file?

*(Text typed on screen: "Can Claude / close my books / using / judgment?" —
trigger word "judgment" corrects to "a skill file", landing on: "Can Claude
close my books using a skill file?" Calibrated timing per the established
hai-simple fix pattern: charMs=42, mistakeRate=4%, hesitateWithin=2%,
hesitateBetween=8%, jitter=26 — the same rates that fixed the timing defect
on the `agent-development` sibling, applied here from the start rather than
discovered by a failed first render.)*

## Body — anatomy, pipeline, the limit

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is called
close-month, and its SKILL.md file is the instruction set — plain language,
no hidden logic. Claude reads the file, then follows it. The file is the
whole program.

**NB02 — Four fixed steps** (source B02, pipeline)
The instructions run as a fixed pipeline. Reconcile the books against
payment processors. Flag anything that doesn't match. Write a
plain-language summary of the month. Export the finished packet. Each step
runs in order — there's no improvising outside that list.

**NB03 — Reliable, and only that wide** (source B03 + BVDT, design tell +
verdict — re-registered Teardown → Plain, kept as the single most teachable
fact rather than a full "gets it right / where it bites" list)
Run it twice on the same numbers and it does the same four steps both
times — same input, same output. That reliability has one edge: it only
does what those steps say. Anything the file doesn't cover, it doesn't do.

## Close

**BCRY — carry-out**
Claude doesn't improvise the close — it runs the same written steps every
time, on any numbers you give it. The edge of what it does is exactly the
edge of what that file says.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to close the month — reconcile
QuickBooks against payment processors, flag anything that doesn't match,
write a P&L narrative, and export the close packet. Read the close-month
skill first, and walk me through what you'll do before you do it. That
last part matters — asking Claude to explain itself first is how you catch
a bad step before it runs.

**BOUT — outro**
Claude, Close Month. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a judgment-vs-file question — is Claude improvising the close, or following a written skill? |
| Wrong guess | B00 (WRITER LAW) | "judgment" corrected to "a skill file" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder / SKILL.md-as-instruction-set anatomy, and the four-step fixed pipeline (reconcile, flag, write, export) that runs in order |
| Anchor | the close-month skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states both what the fixed pipeline buys (same input, same output, every run) and what it costs (only what the file specifies, nothing past that edge); BCRY restates the same pair as the carry-out — together they cover what the design catches and what it misses, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the close-month skill's narration specifies (the SKILL.md-as-instruction-set
anatomy, the four-step pipeline, and the same-input/same-output reliability
with its edge at the file's own scope) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown-framed "gets it right / where it bites" analysis and BVDT's
verdict ("same input, same output, every run... know the limit: only what
the file says") are merged into NB03 as a single plain mechanism-and-
consequence beat, keeping only the fact a general audience needs and can
act on — the same-input/same-output reliability paired with its scope
limit — and stripping the Teardown language ("gets it right," "where it
bites") per the NO JUDGMENT register check; those same verdict facts are
then restated once more, in one sentence, as BCRY's carry-out, per CARRY-OUT
LAW (not kept as a separate bulleted artifact card, unlike the source's
BVDT); BHTF kept as the your-turn handoff, with the source's prompt
(reconcile QuickBooks vs. payment processors, flag gaps, write a P&L
narrative, export the close packet, read the skill first and narrate the
plan before acting) cleaned up from the source's truncated metadata-
concatenation string into a complete, paste-ready sentence — the underlying
ask is unchanged; BOUT kept, re-skinned to the Humanitarians AI outro.
Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
