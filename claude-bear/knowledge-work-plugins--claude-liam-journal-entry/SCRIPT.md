# SCRIPT.md — By File, Not By Feel. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-journal-entry` (Teardown, walks the Anthropic
`journal-entry` finance Skill: prepare journal entries with proper debits,
credits, and supporting detail) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone wondered if Claude just books journal entries by feel — the way an
accountant would from experience. It doesn't. So: does Claude book journal
entries by file?

*(Text typed on screen: "Does Claude / book journal / entries by / feel?" —
trigger word "feel" corrects to "file", landing on: "Does Claude book
journal entries by file?" Config (42ms/char, 8% hesitateBetween, 4%
mistakeRate, 38-char/4-line text) reuses the already-fixed values from the
`claude-plugins-official--claude-liam-agent-development` sibling's B00
TIMING LAW incident — that reel's first, longer/slower config ran out of
its render window before the final line finished typing; the fixed config
worked at 60 characters, and this text is shorter still (38 characters),
giving extra margin against the same failure mode.)*

## Body — anatomy, pipeline, the design tell

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works — this one is
journal-entry. Its SKILL.md holds the full instruction set, in plain
language, with no hidden logic and no accounting judgment baked in. Claude
reads the file, then acts exactly on what's written. The file is the
program.

**NB02 — Steps, in order** (source B02, pipeline)
The steps live in the SKILL.md's Steps section, in order — booking a
month-end accrual, recording depreciation, adjusting deferred revenue, or
documenting an entry for audit review, whichever the request calls for.
Claude executes each step top to bottom. No branching, no judgment calls,
unless the step itself says so.

**NB03 — Spec, not expertise** (source B03, design tell — re-registered
Teardown → Plain, kept as the single most teachable fact rather than the
full "gets it right / where it bites" framing)
That's the deliberate trade. journal-entry is a specification, not
expertise — the same request produces the same debits, credits, and
supporting detail, every single run. But anything outside what the
SKILL.md actually specifies, Claude has no basis for deciding on its own.

## Close

**BCRY — carry-out** (merges source's BVDT verdict beat, per CARRY-OUT LAW)
A Skill makes Claude follow one written checklist, not an accountant's
judgment — same input, same output, every time, and nothing past what the
file specifies.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to prepare a journal entry with
proper debits, credits, and supporting detail for a month-end accrual.
Read the journal-entry skill and walk me through what you will do before
you do it. That's the tell — it should describe the steps from the file,
not general accounting reasoning.

**BOUT — outro**
By File, Not By Feel. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a judgment-vs-file question — does Claude book entries the way an accountant would from experience? |
| Wrong guess | B00 (WRITER LAW) | "feel" corrected to "file" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the SKILL.md as instruction set Claude reads before acting; the Steps section executed linearly, top to bottom, no branching unless a step says so |
| Anchor | the journal-entry skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the spec design gets right (repeatable output) and what it bites (no basis outside the spec); BCRY states the same pairing as the carry-out — together they cover what the file guarantees and what it doesn't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the journal-entry Skill's SKILL.md specifies (the folder/instruction-set
structure, the linear Steps section, the specification-not-expertise
trade) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's design-tell framing ("what it gets right" / "what it bites") is
compressed into NB03, stripped of the Teardown "gets right / bites"
verdict language per the NO JUDGMENT register check, kept as a plain
mechanism-and-consequence description; BVDT's verdict facts (the
checklist behavior, same input → same output, the limit at the spec's
edge) are merged into the single BCRY carry-out sentence rather than kept
as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, with the source's prompt carried over near-unchanged
(narrowed from the source's four-way "accruals / depreciation / revenue
recognition / audit documentation" list to one concrete scenario — a
month-end accrual — so the pasted prompt is a single runnable request
rather than a list of options); BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
