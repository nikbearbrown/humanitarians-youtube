# SCRIPT.md — Checks the Picture, Then Stops. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-fsi-strip-profile` (Teardown, walks the anatomy of the
Anthropic `fsi-strip-profile` Skill — an `investment-banking` vertical-plugin
Skill, financial-services family) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

Unlike the `comps-analysis` redo (whose source `SKILL.md` no longer resolves
on this machine), the actual `strip-profile/SKILL.md` was read directly from
`/Users/nik/Documents/Cowork/anthropics/financial-services/plugins/vertical-plugins/investment-banking/skills/strip-profile/SKILL.md`
for this build, so the body beats below are grounded in the real file rather
than only in the source reel's (partly placeholder-broken) narration.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude trusts the slide it just built — generates it, hands
it over, done. It doesn't: it turns the slide into a picture and looks at
that picture first. So: when Claude builds a strip profile, does it check
the slide it built?

*(Text typed on screen: "When Claude builds / a strip profile, / does it
trust / the slide it built?" — trigger word "trust" corrects to "check",
landing on: "When Claude builds a strip profile, does it check the slide it
built?")*

## Body — anatomy, ask-then-research, self-check-and-stop

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
fsi-strip-profile. The SKILL.md file inside it is the full instruction set —
plain language, no hidden logic. Claude reads it, then acts. The file is the
program.

**NB02 — Ask, then research** (source B02, pipeline — replaced with the
actual pipeline instead of the source's generic "reads each step in order"
framing, now that the real file is available)
The file's actual first move isn't research — it's a question. It asks:
one slide or several, and what to focus on. Only once you say yes does it
start digging into filings, market data, and recent news. Nothing gets
pulled before you've confirmed the scope.

**NB03 — Checks its own picture** (source B03 + BVDT, Teardown compressed to
Plain and grounded in the file's actual "MANDATORY VISUAL REVIEW" step,
replacing the source's unfilled placeholder — see "Source defect" below)
Then it builds one slide at a time. After each one, it turns the slide into
a picture and looks for text spilling out of its box, labels cut off, a
chart bleeding into the next quadrant. It fixes what it finds — then shows
you the slide and stops, waiting for your yes before it builds the next one.

## Close

**BCRY — carry-out**
Inside this skill, Claude checks its own picture before it ever shows you
one — then it stops. That's what makes each slide something you actually
approved, not just something the model produced.

**BHTF — your turn**
Your turn. Paste this into Claude: I want a one-slide investment profile
for Nike, ticker NKE. Read the fsi-strip-profile skill and walk me through
what you will do — including how you'll check the slide — before you build
it. That last clause matters — asking Claude to explain the check first is
what actually shows you the picture it's about to look at.

**BOUT — outro**
Checks the Picture, Then Stops. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a mechanism question — does Claude just trust the slide it generated, or does it look at what it made before showing you? |
| Wrong guess | B00 (WRITER LAW) | "trust" corrected to "check" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | the file/folder anatomy (SKILL.md = the program), the actual first pipeline step (ask scope, wait for yes, only then research), and the actual per-slide loop (render to image, inspect for overlap/cutoff/bleed, fix, show, stop for approval) |
| Anchor | the fsi-strip-profile skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the checking step catches (text overflow, cutoff, chart bleed) and what makes each slide happen (your yes, not the model's say-so); BCRY restates both halves as one sentence pair — the check, and the stop — matching the source's verdict beat, which paired two facts about the same mechanism |
| Carry-out | BCRY | one sentence pair, survives repetition |

## One-flag audit

No inference flag in this reel: every claim traces directly to the actual
`strip-profile/SKILL.md` text — "Only after user confirms, proceed to
research" (Workflow §1); "You MUST create ONE slide at a time and get user
approval before proceeding to the next slide" (§3); "MANDATORY: Convert to
image for review... MANDATORY VISUAL REVIEW: Text overlap check... Text
cutoff check... Chart boundary check... Quadrant integrity" (§3.2–3.3);
"STOP and wait for explicit user approval before creating the next slide"
(§3.6). None of this is an inference about hidden model internals — it is
what the file's own Workflow section specifies. Per simple's ONE-FLAG LAW,
when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01 kept as one beat (anatomy, unchanged
in substance from the source); B02→NB02 kept as one beat but its content is
upgraded from the source's generic "reads each step in order" framing to the
file's actual first pipeline step (scope question, wait for confirmation,
then research) — a strengthening, not a contradiction, since "reads each
step in order" is still true and NB02 is one instance of it; B03's Teardown
"design tell" framing ("what it gets right: repeatable results / what it
bites: anything outside the spec") is replaced in NB03 with the file's own
actual, more specific design tell (the mandatory image-render-and-inspect
loop) rather than kept as an unfillable placeholder, stripped of any
strengths/gaps verdict framing per the NO JUDGMENT register check; BVDT's
verdict role (state the consequence of the mechanism) is merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff — the
source's prompt had an unfilled template slot ("I want to │. Read the
fsi-strip-profile skill..."), which this redo fills with a concrete,
paste-ready task (a one-slide Nike profile — Nike is the file's own worked
example, `examples/Nike_Strip_Profile_Example.pptx`, referenced in its
"Visual Reference" section) rather than an invented company; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

**Source defect, found and worked around, not silently carried over:** the
source `beat_sheet.json`'s narration for B00, B03, BVDT, and BHTF contains a
literal unfilled template placeholder character (`│`) where an
fsi-strip-profile-specific clause was evidently meant to be substituted by
whatever batch script generated the source, and never was (confirmed by:
`PEDAGOGY.md` in the source dir reads only "Batch build — skill teardown
format"). Unlike the `comps-analysis` redo, where the equivalent source
Skill file no longer existed on this machine and the gap had to be filled
generically, `strip-profile/SKILL.md` **was found and read in full** at
`/Users/nik/Documents/Cowork/anthropics/financial-services/plugins/vertical-plugins/investment-banking/skills/strip-profile/SKILL.md`
for this build. So rather than filling the placeholder generically, NB02 and
NB03 were upgraded to the file's actual, specific mechanism (the scope
question before research; the mandatory render-to-image-and-inspect loop
before every user approval) — verified facts, not inference. BHTF's
placeholder ("I want to │. Read the fsi-strip-profile skill...") was filled
with the file's own named example task (a one-slide Nike profile) rather
than a generic one, since the file specifies exactly that example.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
