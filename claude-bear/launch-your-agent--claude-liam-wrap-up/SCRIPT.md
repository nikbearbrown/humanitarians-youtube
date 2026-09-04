# SCRIPT.md — Claude, Wrap Up. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-wrap-up` (Teardown, walks the Anthropic `wrap-up`
Skill — closes out, or revisits, a Claude Managed Agent build) —
question, facts, and body argument carried over; narration re-registered
to Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumes wrapping up your agent means Claude closes the project
down for good. It doesn't — it recaps where things stand, and you can
run it again any time. So: a recap, not a shutdown?

*(Text typed on screen: "Tell Claude to / wrap up my agent / and it
closes / the project, right?" — trigger word "closes" corrects to
"recaps", landing on: "Tell Claude to wrap up my agent and it recaps the
project, right?" Timing, mistake/hesitation rates, and typing speed
(42ms/char, 8% hesitateBetween, 4% mistakeRate, jitter 26,
lead_silence_s 1.0) reused from the already-fixed pattern proven on the
claude-plugins-official--claude-liam-agent-development sibling and its
launch-your-agent--claude-liam-launch-your-agent sibling in this same
family, both of which hit the TIMING LAW failure mode on longer/faster/
noisier first attempts.)*

## Body — anatomy, the pipeline, the fixed-spec boundary

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
wrap-up. The SKILL.md file holds the full instruction set, in plain
language — no hidden logic. Claude reads it, then acts. The file is the
program.

**NB02 — What the recap covers** (source B02, pipeline — the source's
own pipeline beat stayed abstract ("the pipeline is in the Steps
section"); this redo restores the concrete steps the skill actually
runs, using the one place the source states them without truncation —
B00's own narration_text — per the truncation-repair note below)
Inside the SKILL.md is the pipeline. Claude runs it in order: refresh
the overview page, recap every primitive you now own, show the run log
and live status, suggest one or two tailored upgrades, then sweep
hygiene — old sessions archived, the key kept only in dot-env, no
literal dates left in deployment kickoffs.

**NB03 — Idempotent, not a rebuild** (source B03, design tell —
re-registered Teardown → Plain, "interesting constraint" / "deliberate
trade-off" language stripped to a plain mechanism-and-consequence
description)
Because wrap-up is idempotent, running it again doesn't start the build
over or duplicate anything — it refreshes the same overview page and
status tables. Same input, same output, every run. And it only recaps
and suggests: it doesn't build the upgrades it names, and it only checks
what the SKILL.md tells it to check.

## Close

**BCRY — carry-out** (merges source BVDT's verdict facts — same
input/output every run, limited to what the SKILL.md specifies — into
the single sentence that resolves B00's wrong guess, per CARRY-OUT LAW)
Wrapping up your agent isn't a shutdown — it's a recap you can re-run
any time, and running it again only refreshes what's already there.

**BHTF — your turn** (source's prompt restored from a mid-list
truncation bug — see "Truncation note" below — content unchanged)
Your turn. Paste this into Claude: I want to close out — or check in on
— a Claude Managed Agent build. Refresh the overview page, recap every
primitive I now own, show the run log and live status, suggest one or
two tailored next upgrades, and sweep hygiene: archive old sessions,
keep the key only in dot-env, and use no literal dates in deployment
kickoffs. Read the wrap-up skill and walk me through what you will do
before you do it. That clause matters — explaining first surfaces the
hygiene sweep before Claude runs it.

**BOUT — outro**
Claude, Wrap Up. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a build question — does telling Claude to wrap up your agent shut the project down, or hand back a recap you can ask for again? |
| Wrong guess | B00 (WRITER LAW) | "closes" corrected to "recaps" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | the SKILL.md as the program (NB01); the recap pipeline — refresh, recap primitives, show run log/status, suggest upgrades, sweep hygiene (NB02); the idempotent consequence — same input/output, and the recap-not-build boundary (NB03) |
| Anchor | the wrap-up skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the idempotent design guarantees (repeatable, safe to re-run) and what it cannot do (it recaps and suggests, it doesn't build the upgrades or check anything outside the SKILL.md); BCRY states the design's payoff and its shape together (a recap now, safely repeatable, never a rebuild) — together they cover what the skill delivers and what it withholds, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the wrap-up Skill's SKILL.md specifies (a skill is a folder read
before Claude acts, the pipeline refreshes the overview / recaps
primitives / shows the run log and status / suggests upgrades / sweeps
hygiene, and the idempotent-run consequence of repeatable results with a
hard boundary at what the file states) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02, B03→NB03 kept as
one beat each; BVDT's verdict facts (same input → same output every
run, limited to what the SKILL.md specifies) are merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY
+ BHTF + BOUT = 7 beats, matching the source exactly.

**Truncation note.** The source `beat_sheet.json`'s narration/prop
strings were generated by a batch builder that truncated several fields
mid-list at a fixed character count (B03's design-tell body cuts off
after "Idempotent: running it again just refreshes the page and
tables.." with a stray double period; BVDT's narration ends "...refresh
the overview page,." then jumps straight to "Same input, same output";
BHTF's prompt ends "...refresh the overview page,." then jumps to "Read
the wrap-up skill"). This redo restores the full, non-truncated list
using the one place the source states it completely — B00's own
`narration_text`, which spells out the skill's full job ("Close out (or
revisit) a Claude Managed Agent build — refresh the overview page,
recap every primitive the founder now owns, show the run log and live
status, suggest 1–2 tailored next upgrades, and sweep hygiene (sessions
archived, key only in .env, no literal dates in deployment kickoffs).")
— no fact is added or changed beyond what that sentence already
specifies, only the mid-list cutoffs are repaired.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk`
/ `SkillTeardownAnatomy` / `SkillTeardownPipeline` /
`SkillTeardownMechanism` / `ClaudeVerdictArtifact`), so NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's mandated cold-open
swap.
