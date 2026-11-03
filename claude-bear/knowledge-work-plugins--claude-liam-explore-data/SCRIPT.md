# SCRIPT.md — Claude Doesn't Write a Report. It Profiles the Data. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-explore-data` (Teardown, walks the Anthropic
`explore-data` Skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

**Source-material note:** matching the pattern already logged on the
`knowledge-work-plugins--claude-liam-email-sequence` sibling, the source
reel's own B00 narration carries the FULL, untruncated skill description:
"Profile and explore a dataset to understand its shape, quality, and
patterns. Use when encountering a new table or file, checking null rates
and column distributions, spotting data quality issues like duplicates or
suspicious values, or deciding which dimensions and metrics to analyze."
Later source beats (B03, BVDT, BHTF) quote the same description but got cut
off mid-sentence by whatever produced them ("...Use when encountering ."
and a stray "us." fragment). This redo uses B00's complete version as the
source of record everywhere the description is needed. Per ONE-FLAG LAW:
no flag is used in this reel, because the source genuinely supports
everything stated.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed the skill would explore the data and write up a report. It
doesn't — it profiles the dataset: shape, quality, and patterns, the same
checklist every time. So: does Claude write a report?

*(Text typed on screen: "Does Claude\nexplore my data\nand write a\nreport?"
— trigger word "report" corrects to "profile", landing on: "Does Claude
explore my data and write a profile?" 4 lines, short — same short-line,
moderate-charMs shape as the `knowledge-work-plugins--claude-liam-discover-
brand`/`claude-liam-email-sequence` siblings, kept inside the >=9s TIMING
LAW window rather than discovered by a failed first render.)*

## Body — anatomy, pipeline, the actual job

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
explore-data. Its SKILL.md file holds the full instruction set, in plain
language — no hidden logic. Claude reads it, then acts. The file is the
program.

**NB02 — Steps, in order** (source B02, pipeline)
The instructions are laid out in a Steps section. Claude reads each step
in order and runs it — linear, no branching unless a step says otherwise.

**NB03 — Profile the dataset** (source B03, design tell —
re-registered Teardown → Plain; no inference, no flag — the full
description is read directly from the source's own B00)
Here's the actual job: profile a dataset to understand its shape, quality,
and patterns. Check null rates and column distributions, spot issues like
duplicates or suspicious values, and decide which dimensions and metrics
are worth analyzing next.

## Close

**BCRY — carry-out**
Ask it to explore your data, and explore-data hands back a profile —
shape, quality, patterns, and the issues worth flagging — the same
checklist every time, not a freeform report.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a CSV of customer orders. Profile
it for me — how many rows and columns, which columns have missing values
and how often, whether any rows look like duplicates, and which two or
three columns are most worth digging into next. Walk me through your plan
before you start. That clause matters — explaining first surfaces the real
constraint logic.

**BOUT — outro**
Claude, Explore Data. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a written-report question — will Claude explore the data and hand back some kind of narrative report or insights, the way a person answering "explore this for me" might read the ask? |
| Wrong guess | B00 (WRITER LAW) | "report" corrected to "profile" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a skill is a folder with a SKILL.md Claude reads before acting; the Steps section runs linearly; the actual job is a structured profile — shape, null rates, distributions, duplicates, suspicious values, and which dimensions/metrics are worth analyzing — not a written report |
| Anchor | the explore-data skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — matches the email-sequence/discover-brand siblings' shape exactly |
| Both directions | folded into NB03 + BCRY | NB03 states what gets produced (the profile, every listed checklist item); BCRY states the same design's boundary in the other direction (one dataset in, the same profile checklist out, built the same way every time — never a freeform report) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

Zero flags. Per simple's ONE-FLAG LAW: "if the source genuinely supports
everything, there is no flag." Every claim in this script — the skill's job
(profile shape, quality, patterns), its use cases (new table/file, null
rates and column distributions, duplicates or suspicious values, deciding
which dimensions and metrics to analyze), the anatomy (a skill is a folder
with a SKILL.md Claude reads before acting), the pipeline (Steps run
linearly), and the verdict (same input, same output, every run; the limit
is only what the file says) — is read directly off the source
`beat_sheet.json`'s own `narration_text` fields, principally B00's
complete, untruncated skill description. Nothing here is inferred from a
name, a sibling skill, or an inaccessible file.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right / where it bites" framing is compressed into
NB03 as a plain mechanism description, per the NO JUDGMENT register check;
BVDT's verdict facts (same input, same output, every run; the limit is
only what the file says) are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff — the source's own
prompt asks Claude to "read the explore-data skill," which assumes an
Anthropic Skill file a general viewer is unlikely to have installed, so
this redo writes a concrete, paste-ready prompt that exercises the
identical mechanism (a dataset in, a profile — shape, nulls, duplicates,
which columns matter — out) without requiring any specific Skill install;
BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03
+ BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
