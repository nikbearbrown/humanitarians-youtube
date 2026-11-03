# SCRIPT.md — A Skill Is A File, Not An App. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-customer-pulse` (Teardown, walks the anatomy of a Claude
Skill named `customer-pulse`) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

**Source data note:** the source `beat_sheet.json`'s B03 and BVDT
`narration_text` fields contain an unfilled template placeholder (a literal
`>` where the skill's specific one-line task description should have been —
confirmed against sibling `claude-liam-forecast`, which has the equivalent
line filled in full, so this is a data gap in this one source file, not a
deliberate omission; the sibling `claude-liam-business-pulse` source has the
identical defect, redone earlier under this same skill). Per PHASE 1's "when
in doubt, describe behavior generically" rule, this redo does not invent the
missing specific (no claim about exactly which feedback sources customer-pulse
reads or how it formats a report); every fact this reel states about
customer-pulse is the generic Claude Skills mechanism the source's non-broken
beats (B01, B02) already fully support: a skill is a folder holding a
SKILL.md instruction file, Claude reads it before acting, and a Steps section
is executed in order. The name "customer-pulse" is used only as the named
example throughout, never elaborated with invented specifics (in particular,
this reel does NOT borrow the sibling `customer-pulse-check` skill's
integration details — PayPal disputes, HubSpot tickets, review exports — since
those are confirmed facts about a *different*, adjacent skill, not this one).

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed customer-pulse was an app that Claude opens and runs on its
own. It isn't — it's a plain file Claude reads before acting. So: does
opening customer-pulse's file tell Claude exactly what to do?

*(Text typed on screen: "Does opening / customer-pulse's app / tell Claude /
what to do?" — trigger word "app" corrects to "file", landing on: "Does
opening customer-pulse's file tell Claude what to do?")*

## Body — anatomy, how it runs, the limit

**NB01 — SKILL.md: the instruction set** (source B01, anatomy)
A Claude skill is a folder Claude reads before it works. This one is called
customer-pulse. Inside is one file, SKILL.md — the full instruction set,
written in plain language, with no hidden code underneath it. Claude reads
that file, then acts on what it says. The file is the program.

**NB02 — How it runs: one step at a time** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and carries it out — linear, one step after another. No branching, unless a
step itself says to branch.

**NB03 — The limit is the file** (source B03 + BVDT, design tell + verdict —
re-registered Teardown → Plain, merged into one mechanism-and-consequence
fact rather than kept as a separate "gets right / bites" list plus a
separate verdict card)
Because customer-pulse is a written spec, Claude only does what that file
says — the same steps, in the same order, every time it runs. That's what
makes it repeatable. It also means the reverse: anything not written in the
file is simply outside what the skill covers. The file isn't a suggestion
Claude improvises around — it's the whole boundary.

## Close

**BCRY — carry-out**
A Claude skill isn't an app running on its own — it's a file Claude reads,
so it does exactly what that file says, the same way, every time, and
nothing beyond what's written.

**BHTF — your turn**
Your turn. Paste this into Claude: "I want a quick pulse-check on what my
customers are actually saying right now. Before you do anything, read any
skill you have for this and walk me through exactly what steps you're about
to take." That clause matters — asking Claude to explain first shows you
exactly what the file says to do, before it does it.

**BOUT — outro**
A Skill Is A File, Not An App. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an installed-software question — does opening customer-pulse's app tell Claude what to do? |
| Wrong guess | B00 (WRITER LAW) | "app" corrected to "file" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the folder/SKILL.md structure and the Steps section's linear execution |
| Anchor | the customer-pulse skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the spec-boundary gives (repeatability) and what it costs (anything unwritten is out of scope) together; BCRY restates both in the single carry-out sentence — together they cover what the file guarantees and what it doesn't, matching the source's B03+BVDT pairing |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of the
generic Claude Skills mechanism the source's intact beats (B01, B02) state —
a folder, one SKILL.md file, plain-language instructions, a Steps section
executed in order, no hidden logic. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated. (The
source's broken B03/BVDT placeholder is not treated as a fact to flag or
infer around — see "Source data note" above; this reel simply never states
the missing specific.)

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right / where it bites" framing and BVDT's separate
verdict card are merged into the single NB03 mechanism-and-consequence beat
(both were building toward the same fact — the spec is the boundary —
so keeping them as two cards would have restated rather than added); BCRY
carries the compressed carry-out per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, rewritten to a prompt any viewer can run today without
already having the customer-pulse skill installed (the source's own prompt
depended on a customer-task fill that the source itself never completed —
see "Source data note"); BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.
