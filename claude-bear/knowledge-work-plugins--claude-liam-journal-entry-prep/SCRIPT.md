# SCRIPT.md — Claude, Journal Entry Prep. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-journal-entry-prep` (Teardown, walks the Anthropic
`journal-entry-prep` Claude skill — prepares journal entries with proper
debits, credits, and supporting documentation for month-end close) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone wondered if Claude was specially trained to prep journal entries.
It isn't — it follows a written skill file, step by step. So: can Claude
prep journal entries using a skill file?

*(Text typed on screen: "Can Claude prep / journal entries / using /
training?" — trigger word "training" corrects to "a skill file", landing
on: "Can Claude prep journal entries using a skill file?" Timing rates
follow the calibrated hai-simple fix pattern proven on the
`agent-development` and `close-month` siblings: charMs=42, mistakeRate=4%,
hesitateWithin=2%, hesitateBetween=8%, jitter=26 — applied from the start
rather than discovered by a failed first render.)*

## Body — anatomy, pipeline, the limit

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is called
journal-entry-prep, and its SKILL.md file is the instruction set — plain
language, no hidden logic. Claude reads the file, then follows it. The file
is the whole program.

**NB02 — The steps** (source B02, pipeline)
The instructions run as a pipeline. Read what needs to be booked. Work out
the debit and the credit. Attach the paperwork that backs it up. Each step
runs in order — there's no improvising outside that list.

**NB03 — Reliable, and only that wide** (source B03 + BVDT, design tell +
verdict — re-registered Teardown → Plain, kept as the single most teachable
fact plus the anchor list of what the file actually names, rather than a
full "gets it right / where it bites" account)
Run it on the same numbers twice and you get the same debit, the same
credit, the same documentation both times — same input, same output. That
covers what the file names: accruals, prepaid amortization, depreciation,
payroll, revenue recognition. Anything the file doesn't name, it doesn't
do.

## Close

**BCRY — carry-out**
Claude doesn't guess the accounting — it runs the same written steps on the
numbers you give it, every time. What it covers is exactly what that file
names, and nothing past it.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to prepare journal entries with
proper debits, credits, and supporting documentation for month-end close.
Read the journal-entry-prep skill first, and walk me through what you'll do
before you do it. That last part matters — asking Claude to explain itself
first is how you catch a bad step before it runs.

**BOUT — outro**
Claude, Journal Entry Prep. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a training-vs-file question — is Claude drawing on trained accounting sense, or following a written skill? |
| Wrong guess | B00 (WRITER LAW) | "training" corrected to "a skill file" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder / SKILL.md-as-instruction-set anatomy, and the read-then-post-then-attach pipeline that runs in order |
| Anchor | the named transaction list (accruals, prepaid amortization, depreciation, payroll, revenue recognition), introduced at NB03 and carried straight into BCRY | source is a single worked example throughout (one skill, one named list), not a planted-and-paid-off separate case — the list is the concrete, visualizable object the carry-out resolves against |
| Both directions | folded into NB03 + BCRY | NB03 states both what the fixed steps buy (same input, same output, every run) and what they cost (only the named transaction types, nothing past that edge); BCRY restates the same pair as the carry-out |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the journal-entry-prep skill's narration specifies (the
SKILL.md-as-instruction-set anatomy, the debit/credit/documentation
pipeline, the named transaction list, and the same-input/same-output
reliability with its edge at the file's own scope) — not an inference about
hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown-framed "gets it right / where it bites" analysis and BVDT's
verdict ("same input, same output, every run... know the limit: only what
the file says") are merged into NB03 as a single plain
mechanism-and-consequence beat, keeping the concrete named-transaction list
(accruals, prepaid amortization, depreciation, payroll, revenue
recognition) alongside the reliability/limit pair, and stripping the
Teardown language ("what it gets right," "what it bites") per the NO
JUDGMENT register check; those same facts are then restated once more, in
one sentence, as BCRY's carry-out, per CARRY-OUT LAW (not kept as a separate
bulleted artifact card, unlike the source's BVDT); BHTF kept as the
your-turn handoff, with the source's prompt (prepare journal entries with
proper debits, credits, and supporting documentation for month-end close,
read the skill first and narrate the plan before acting) cleaned up from
the source's truncated metadata-concatenation string into a complete,
paste-ready sentence — the underlying ask is unchanged; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
