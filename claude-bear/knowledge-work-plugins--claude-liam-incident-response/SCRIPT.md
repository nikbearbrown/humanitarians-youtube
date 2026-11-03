# SCRIPT.md — Claude, Incident Response (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-incident-response` (Teardown, skill-teardown chassis,
source: the Anthropic `incident-response` skill) — question, facts, and
body argument carried over; narration re-registered to Plain (explain, then
stop, no verdict/judgment language); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
When production goes down, it's tempting to think Claude just knows what to
do — pure instinct. It isn't instinct. It's instructions.

## Act I — The alert

**NB01 — 2 a.m., production down** (stakes; ANCHOR PLANTED)
Two a.m., an alert fires: production is down. Someone asks Claude to run
the incident. What actually tells it what to do next?

**NB02 — instinct vs. the file** (wrong guess, falsified)
The reasonable guess: Claude has read thousands of postmortems, so it
already knows how to run yours. But ask it to handle an incident with no
file loaded, and the plan changes every time you ask. Load the file, and
the same three steps show up, every run.

## Act II — What the file actually is

**NB03 — the file is the program** (mechanism, source B01)
Here's why. A skill is a folder Claude reads before it acts. This one is
named incident-response, and its one file — SKILL.md — is the entire
instruction set, written in plain language. The file is the program.

**NB04 — steps, in order** (mechanism, source B02)
Inside, a Steps section lists what to do, in order. Claude reads each step
and executes it — linear, one after another, no branching unless a step
itself says so.

**NB05 — triage, communicate, postmortem** (mechanism + ANCHOR referenced,
source B00/BVDT)
For incident-response, those steps are three: triage the alert, communicate
a status update, then write a blameless postmortem once it's resolved. And
the file names exactly when to start it — phrases like "production is
down," an alert that needs a severity call, or a status update mid-incident.

## Act III — What that buys you, and what it doesn't

**NB06 — same steps, every time** (both directions, A — source BVDT)
That's what the file buys you: the same three steps, run the same way,
whether it's your first incident or your fiftieth. Reliable under pressure
is the whole point.

**NB07 — outside the page** (both directions, B; ANCHOR PAYOFF — source B03/BVDT)
But back at that two a.m. alert — if what's actually happening isn't
triage, communicate, or postmortem, the file has nothing written for it. It
only knows the page it was given.

## Close

**BCRY — carry-out**
The incident-response skill isn't Claude's judgment about your outage. It's
your team's playbook — triage, communicate, postmortem — typed once and
followed exactly, every time it's asked.

**BHTF — your turn** (source BHTF, Plato move preserved: plan before action)
Your turn. Paste this into Claude: I want to run an incident response
workflow — triage, communicate, and write a postmortem. Read the
incident-response skill and walk me through what you will do, before you do
it.

**BOUT — outro**
Claude, Incident Response. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00→NB01 | a 2 a.m. outage; someone asks Claude to run it |
| Wrong guess | B00→NB02 | "Claude just knows (instinct)" corrected to "it's instructions," then falsified: no file loaded → plan shifts every run; file loaded → same three steps every run |
| Mechanism | NB03–NB05 | SKILL.md is the instruction file (the file is the program); Steps run in order, linear; the actual job is triage/communicate/postmortem, triggered by named phrases |
| Anchor | NB01 → NB07 | the 2 a.m. "production is down" alert, planted at the stakes, returned to at the limit |
| Both directions | NB06 → NB07 | the file gives repeatable steps every run (good); it also has nothing to say the moment reality falls outside those three steps (the limit) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct restatement of the
source skill's own stated behavior (a SKILL.md is read before acting, its
Steps section runs in order, its named trigger phrases start it, its job is
triage/communicate/postmortem) — not an inference about hidden internals.
Per simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats (skill-teardown chassis: B00 cold open, B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF your-turn, BOUT outro).
hai-simple's spine has no separate "design tell"/verdict slot (Plain
register carries one carry-out sentence, not a Teardown judgment beat), and
requires its own stakes/wrong-guess/anchor/both-directions shape that the
7-beat source compressed into single-purpose beats. Expanded to 11 beats
(B00 + 7 GRAPHIC body beats NB01–NB07 + BCRY/BHTF/BOUT) so every one of the
six required Plain-register moves gets its own beat and the anchor (the 2
a.m. alert) can be planted and paid off in two different beats rather than
asserted once — no new facts were introduced; NB01–NB07 collectively
restate exactly what source B00/B01/B02/B03/BVDT already said, reordered
into the required spine and stripped of verdict/judgment language ("what it
bites," "know the limit" restated as a plain fact instead of a verdict).
Logged per BUILD-LOG.md.
