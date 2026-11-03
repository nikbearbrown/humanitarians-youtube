# SCRIPT.md — Claude, Build Zoom Rest Api App. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-build-zoom-rest-api-app` (Teardown, skill-teardown format
for the Anthropic `build-zoom-rest-api-app` skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

Source facts preserved verbatim (nothing invented beyond these):
- Skill name: `build-zoom-rest-api-app`.
- Its own description: "Reference skill for Zoom REST API. Use after choosing
  an API-based workflow when you need endpoint selection, resource-management
  patterns, OAuth requirements, rate-limit awareness, or API error debugging."
- A skill is a folder Claude reads before it works; the SKILL.md contains the
  full instruction set in plain language, no hidden logic; the file is the
  program.
- The pipeline lives in the Steps section; Claude reads each step in order and
  executes it — linear, no branching unless a step says so.
- What it gets right: repeatable results (same input, same output, every
  run). What it doesn't cover: anything outside the spec.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked if Claude already knows how to build a Zoom REST API app. Not
quite — it reads a skill file first. So here's the real question: does Claude
already read the Zoom API skill?

## Act I — What a skill actually is

**NB01 — A skill is a folder** (source B01)
A skill is a folder Claude reads before it works. This one is called
build-zoom-rest-api-app — the reference skill for the Zoom REST API. The
instructions live in one file, in plain language, no hidden logic. The file
is the program.

## Act II — The wrong guess, and the case that breaks it

**NB02 — "So it already knows the Zoom API?"** (WRONG GUESS)
So does naming the skill mean Claude already knows everything about the Zoom
API, out of the box? That's the natural guess — one file, and suddenly it's
an expert.

**NB03 — Five things, written down** (ANCHOR PLANTED, BREAK)
Open the file and the knowledge is specific, not general: endpoint
selection, resource-management patterns, OAuth requirements, rate-limit
awareness, API error debugging. Five things, written down — nothing broader
than that.

## Act III — How it runs

**NB04 — Steps, in order** (source B02)
The instructions run in order, in the Steps section. Claude reads each step
and executes it — linear, no branching unless a step says so.

**NB05 — Ask twice, same answer** (ANCHOR PAYOFF, source verdict facts)
Ask about those same five things twice, and Claude reads the same file
twice — endpoint selection, OAuth, rate limits, and the rest, delivered the
same way both times.

## Act IV — Both directions

**NB06 — Inside the file, outside the file** (BOTH DIRECTIONS, source B03/verdict)
Stay inside those five things and the answer repeats reliably, run after
run. Step outside them — a Zoom feature the file never mentions — and the
skill has nothing written to read, so the guidance stops.

## Close

**BCRY — carry-out**
Claude repeats the exact same Zoom REST API guidance every time — but only
for the five things this skill actually writes down.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm about to use the
build-zoom-rest-api-app skill for a Zoom integration. Before you touch any
code, read the skill file and tell me which of the five things it covers —
endpoint selection, resource management, OAuth, rate limits, or error
debugging — actually applies to what I'm building, and which parts I'll need
to figure out myself.

**BOUT — outro**
Claude, Build Zoom Rest Api App. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–NB01 | a skill is a folder Claude reads, not knowledge it already has; the naive guess is that naming it grants general expertise |
| Wrong guess | NB02 → NB03 | "it already knows the Zoom API, out of the box" corrected/broken by the file's actual, narrow contents — five named things, nothing broader |
| Mechanism | NB01, NB04 | the folder/file anatomy, then the linear step-by-step pipeline |
| Anchor | NB03 → NB05 | the five named things (endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, API error debugging) — planted as what's actually inside, paid off as what makes repeated answers identical |
| Both directions | NB06 | reliable and repeatable inside those five things; nothing written to read the moment a question falls outside them |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct restatement of the
source skill's own description and the source sheet's stated facts (folder/
file anatomy, linear step execution, the five named capabilities, same-
input-same-output, limited to what the file specifies) — not an inference
about hidden internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats (skill-teardown chassis: B00 cold open + B01 anatomy + B02
pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT outro,
PEDAGOGY.md: "Batch build — skill teardown format"). hai-simple's spine
wants a distinct wrong-guess beat and a both-directions pair, which the
thin 4-body-beat source does not carry as separate beats — B03's own
"what it gets right: repeatable results / what it bites: anything outside
the spec" line already IS a both-directions statement, just phrased with
Teardown's trade-off framing ("what it bites"), which is exactly the
judgment language Plain register cuts. So: B01 (anatomy) and B02 (pipeline)
carry over near-verbatim (NB01, NB04) since their register was already
Plain — no verdict, no trade-off, just mechanism; B03's two facts were
split and re-expressed without judgment — the "repeatable results" half
becomes NB05's anchor payoff, the "anything outside the spec" half becomes
NB06's direction B; a wrong-guess beat (NB02) and an anchor-plant/break beat
(NB03) were added, built entirely from the skill's own description text (the
five named capabilities) rather than invented, to give the reel a concrete
case for the naive "already knows the API" guess to break against; BVDT's
"same input, same output, every run" fact was kept as NB05's anchor payoff
rather than as a separate verdict beat, since Plain register carries one
carry-out sentence, not a bulleted recap (CARRY-OUT LAW). Net: B00 (writer)
+ 6 body beats (NB01–NB06) + BCRY/BHTF/BOUT = 10 beats, up from the source's
7 — the increase adds no new facts, only makes the wrong-guess and
both-directions moves explicit as their own beats instead of leaving them
folded into the design-tell beat's judgment framing. Logged per
BUILD-LOG.md.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (ClaudeComposerAsk,
SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism,
ClaudeVerdictArtifact, ClaudeTitleOutro) — NO-GENAI/NO-PANTRY LAW required
no substitution beyond B00. The new body beats (NB02, NB03, NB05, NB06)
reuse the same `SkillTeardownMechanism` REMOTION pattern the source already
used for its design-tell beat — a generic text-card component, not
source-locked — so no new component authoring was needed (GATE L: library
hit, not a miss).
