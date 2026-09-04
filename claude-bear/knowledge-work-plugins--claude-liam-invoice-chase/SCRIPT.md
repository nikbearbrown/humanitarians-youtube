# SCRIPT.md — Steps, Not Guesses. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-invoice-chase` (Teardown, walks the Anthropic
`invoice-chase` small-business Skill) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed chasing an invoice means Claude guessing case by case. It
doesn't — it follows a written procedure. So: does Claude need the right
steps, not the right guesses, to chase an invoice?

*(Text typed on screen: "Does Claude / need the right / guesses to chase /
an invoice?" — trigger word "guesses" corrects to "steps", landing on:
"Does Claude need the right steps to chase an invoice?" charMs/mistakeRate/
hesitateBetween set conservatively (42ms, 4%, 8%) from the start, per the
fix already proven necessary on the claude-plugins-official--claude-liam-
agent-development sibling, which ran its window out at higher rates on
first attempt — verify media/B00.mp4 >= 8s and that "steps" is settled and
legible well before the clip ends.)*

## Body — anatomy, the pipeline, the constraint

**NB01 — SKILL.md is the program** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is invoice-chase —
the SKILL.md inside it holds the whole instruction set, plain language, no
hidden code. Claude reads the file, then works through it. The file is the
program.

**NB02 — Read, then execute** (source B02, pipeline)
The instructions run as steps, in order. Claude reads each one and carries
it out, top to bottom — no branching unless the file says so. One flag: we
don't have invoice-chase's literal file here, only the shape every Skill
shares — read the steps, execute them in order, then return the result.

**NB03 — The limit is the file** (source B03, design tell — re-registered
Teardown → Plain, kept as the single most teachable fact)
Here's the constraint worth knowing: since the file is the whole program,
Claude can only do what its steps say. Same input, same output, every run —
repeatable. But if a client's situation doesn't match any step in the file,
Claude has nothing else to reach for. The limit is exactly what the file
specifies, nothing more.

## Close

**BCRY — carry-out**
A Skill isn't Claude improvising — it's Claude following a written
procedure, the same one, every run. The whole limit is what that file says,
nothing more.

**BHTF — your turn**
Your turn. Paste this into Claude: I run an invoice-chase process for
late-paying clients — write me a SKILL.md that spells out the exact steps,
no improvising. Then walk me through what you'll do, before you do it. That
clause matters: explaining first shows you the actual procedure, not a
guess.

**BOUT — outro**
Steps, Not Guesses. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a mechanism question — does chasing an invoice mean Claude guessing case by case, or following steps? |
| Wrong guess | B00 (WRITER LAW) | "guesses" corrected to "steps" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | what a Skill folder is and what SKILL.md holds; the read-steps-in-order-then-return pipeline |
| Anchor | the invoice-chase skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete failure mode the fixed-procedure design creates (a situation outside the file's steps, Claude has nothing to reach for); BCRY states the design's payoff and its failure mode together (repeatable, same input same output — and limited to exactly what's written) — together they cover what the fixed-procedure model gets and what it misses, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

One inference flag, at NB02: the reel does not reconstruct invoice-chase's
literal step list, because the source SKILL.md is not present on this
machine (its recorded path lives on a different machine — see QUESTION.md's
source-fidelity note) and the source `beat_sheet.json`'s own narration for
this material is a set of unfilled template placeholders (`>`), not the
actual file text. NB02 states this directly rather than inventing specific
steps (checking due dates, drafting a particular reminder email, etc.) that
were never confirmed. Everywhere else, the claims are the generic,
confirmed mechanism every Anthropic Skill shares (a folder + SKILL.md read
before acting, executed step by step, same input to same output) — Per
`simple`'s ONE-FLAG LAW, exactly one flag, at the moment the leap happens.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's design-tell beat becomes NB03, kept as one beat, re-registered to
Plain; BVDT's verdict facts (same input/same output every run, limited to
what the file says) are merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW;
BHTF kept as the your-turn handoff, with the source's prompt template
(which asked the viewer to fill in `>` — an unfilled placeholder for "I want
to [chase down a specific invoice]") replaced with a genuinely paste-ready,
concrete prompt: writing a SKILL.md for an invoice-chase process, since the
literal source prompt could not be carried over verbatim (it was never
filled in) and a viewer cannot run a `>` placeholder; BOUT kept, re-skinned
to the Humanitarians AI outro (`OutroSeries`) with a new title, "Steps, Not
Guesses.", replacing the source's generic "Claude, Invoice Chase." per the
sibling convention (`claude-plugins-official--claude-liam-agent-development`
similarly retitled to its carry-out). Total: B00 + NB01–NB03 + BCRY + BHTF +
BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold-open swap.

## Deliberately not claimed

- **Not invoice-chase's literal step list.** The source SKILL.md was never
  available on this machine, and the source `beat_sheet.json`'s own
  narration for the invoice-chase-specific material was never filled in
  (literal `>` placeholders in B00, B03, BVDT, BHTF) — so there was nothing
  locked to carry over beyond the generic Skill mechanism. NB02 flags this
  directly rather than inventing a plausible-sounding but unconfirmed step
  list (e.g., specific due-date thresholds, a specific reminder cadence, a
  specific tone-of-voice policy).
- **No claim about what invoice-chase's actual constraint is.** Source B03
  ("Claude's job: >. What it gets right... What it bites...") never states
  the actual interesting constraint — NB03 instead states the one constraint
  every Skill genuinely has (bounded to exactly what its file specifies),
  which is confirmed by BVDT's own unconditioned lines ("Same input, same
  output, every run" / "Know the limit: only what the file says").
- **No accusation about the source's unfilled placeholders.** They read as
  an ordinary production gap (a template variable never substituted before
  the source was marked built), not misconduct, and this redo treats it as
  a source-fidelity fact to disclose, not a verdict on anyone's work
  (register check — Plain explains, it does not judge).
