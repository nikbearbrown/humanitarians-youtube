# SCRIPT.md — Same Battlecard, Every Time. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-competitive-intelligence` (Teardown, walks the Anthropic
`competitive-intelligence` sales Skill) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would watch their competitors continuously, like a
monitoring service. It doesn't — it researches on request, following one
fixed recipe. So: can Claude research my competitors for me?

*(Text typed on screen: "Can Claude / watch my / competitors / for me?" —
trigger word "watch" corrects to "research", landing on: "Can Claude
research my competitors for me?")*

## Body — anatomy, pipeline, the fixed spec

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
competitive-intelligence — research your competitors, then build an
interactive battlecard. The SKILL.md holds that whole instruction set,
plain language, no hidden logic. Claude reads it, then acts. The file is
the program.

**NB02 — The pipeline, and the anchor** (source B02, pipeline)
Ask with a phrase like "battlecard for one competitor" or "how do we
compare to them," and the pipeline runs: read the trigger, research each
competitor named, then build one HTML artifact — clickable competitor
cards, plus a comparison matrix. Claude works through the steps in order.
Linear — no branching unless a step says so.

**NB03 — The fixed spec, both ways** (source B03, design tell — re-registered
Teardown → Plain: the source's "what it gets right / what it bites" framing
is stripped to a plain mechanism-and-consequence description)
That's the whole job, not open-ended monitoring: research the competitors
you named, build that one battlecard, then stop. Ask for a rival that's not
on your list, or a shape besides the battlecard, and there's nothing to
fall back on — the spec only produces what's written into it.

## Close

**BCRY — carry-out** (source BVDT, verdict — merged into the single
carry-out sentence per CARRY-OUT LAW)
A skill runs the same recipe on the same request every time — the same
battlecard, never more than what the file says to build.

**BHTF — your turn** (source BHTF, cleaned: the source narration_text
carried a mid-word truncation bug — "outputs an html a" — from an
automated string-shortening pass; rewritten here as an actually paste-ready
prompt, same intent)
Your turn. Paste this into Claude: Read the competitive-intelligence skill
and walk me through what you'll do before you do it. Then run it for one
real competitor of mine. Check what comes back: is it the same two things
every time — the battlecard's cards and its comparison matrix — or did it
wander outside the spec?

**BOUT — outro**
Same Battlecard, Every Time. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | naive framing is a scope question — is this ongoing surveillance, or a research task Claude does on request? |
| Wrong guess | B00 (WRITER LAW) | "watch" corrected to "research" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the SKILL.md as the whole instruction set ("the file is the program"); the linear pipeline from trigger phrase to one HTML battlecard |
| Anchor | the battlecard (HTML artifact: clickable competitor cards + comparison matrix), named at NB01, developed at NB02, paid off at NB03 and BCRY | one concrete object recurs across every body beat rather than a separate planted/paid-off case — the object itself is what "only what the file says" and "same battlecard, every time" resolve against |
| Both directions | NB03 | one beat states both: works for the competitors you named (produces the battlecard), fails for anything else (nothing to fall back on) — the source's B03 already paired these as "gets it right" / "bites", carried over without the judgment framing |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct restatement of what
the competitive-intelligence Skill's SKILL.md specifies (the file-as-program
framing, the linear step pipeline, the battlecard artifact's two parts, the
same-input-same-output guarantee, and the boundary at what the spec
covers) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape, 1:1: B00 replaced with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02, B03→NB03 kept as one beat
each, facts unchanged, Teardown "gets it right / bites" framing in B03
flattened to plain mechanism-and-consequence; BVDT's verdict facts (same
input → same output every run; the limit is only what the file says) merged
into the single BCRY carry-out sentence per CARRY-OUT LAW rather than kept
as a separate bulleted artifact card; BHTF kept as the your-turn handoff —
the source's prompt text carried a truncation artifact ("outputs an html
a.") from an automated shortening pass, so it was rewritten as a clean,
actually-runnable prompt with the same ask (read the skill, walk through
the plan, then run it and check the two-part battlecard output); BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
