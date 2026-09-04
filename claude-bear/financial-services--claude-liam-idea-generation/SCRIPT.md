# SCRIPT.md — Claude, Idea Generation. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-idea-generation` (Teardown, skill-teardown format) —
question and true facts carried over verbatim from the source; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source's job line survives verbatim (source
B00 states it in full; B03/BVDT truncate it mid-word to "…thematic res." /
"…quantitative s." — a template-truncation bug in the source script, not
reproduced here): "Systematic stock screening and investment idea sourcing.
Combines quantitative screens, thematic research, and pattern recognition to
surface new long and short ideas." The source's anatomy beat (B01) lists
exactly one file: `SKILL.md` (3k, accented) — no second file is ever named,
so none is invented here. Linear pipeline (read SKILL.md → execute → return
output) and specification semantics (repeatable results, a limit at the
file's edge) also carry over unchanged.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude brainstorms new stock ideas with the idea-generation
skill, like an analyst free-associating. It doesn't — it runs a systematic
screen. Let's see how that actually works.

## Act I — the wrong guess

**B01 — Sounds like brainstorming**
Hear "Claude has an idea-generation skill" and it sounds like Claude is
creatively brainstorming — free-associating its way to a promising stock
idea, the way an analyst might in a pitch meeting.

**B02 — Broken, with a case** (pays off B00)
But it never free-associates. Run the same screen twice on the same data,
and you get the same candidates back both times — not two different
creative pitches.

## Act II — the mechanism

**B03 — A screen, run** (ANCHOR PLANTED)
Here's the anchor: a screen. Say the criteria are rising free cash flow plus
recent insider buying. idea-generation runs the quantitative screen, checks
the thematic angle, looks for the pattern — and three candidates surface.

**B04 — Screen, then research, then pattern, in order**
It runs in a fixed order: quantitative screen first, then thematic research,
then pattern recognition, surfacing long and short candidates. The steps
don't branch unless the SKILL.md itself says to.

**B05 — Screener, not strategist**
That makes it a screener, not a strategist. The payoff: the same criteria
surface the same candidates, run after run. The limit: it only finds what
fits the screen you wrote — nothing outside it.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So back to that screen: run it again tomorrow with the same criteria, and
the same three candidates surface — not a fresh set, not a new pitch. The
screen doesn't get creative between runs.

## Act III — both directions

**B07 — Neither proves the other**
A candidate surfacing from the screen doesn't prove it's a good trade — it
only proves it matched the screen's criteria, not that those criteria are
the ones that matter here. And a stock that never surfaces isn't proven
bad — it may simply not fit this particular screen's pattern.

## Close

**BCRY — carry-out**
idea-generation doesn't brainstorm — it runs the same quantitative screen,
thematic check, and pattern rule on every request, so the same criteria
always surface the same candidates.

**BHTF — your turn**
Your turn. Paste this into Claude: I want systematic stock screening and
investment idea sourcing — combining quantitative screens, thematic
research, and pattern recognition to surface new long and short ideas. Read
the idea-generation skill and walk me through what you will do, before you
do it. That way you'll see exactly which screens run and in what order,
before a single candidate surfaces.

**BOUT — outro**
Claude, Idea Generation. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "an idea-generation skill" sounds like Claude is creatively brainstorming |
| Wrong guess | B00 → B02 | "brainstorms" corrected to "screens for"; broken with the run-the-same-screen-twice case |
| Mechanism | B03–B05 | a screen defined and run, in a fixed order, screener not strategist |
| Anchor | B03 → B06 | the FCF-up + insider-buying screen and its 3 candidates, planted then returned to |
| Both directions | B07 | surfacing proves nothing about trade quality; not surfacing proves nothing about badness |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts forward and B03 also plants the anchor; B06 is a
new anchor-payoff beat restating the design tell against the named anchor;
B07 (both directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT =
11 beats — the identical proportionate expansion used on the
`financial-services--claude-liam-gl-recon` sibling redo. No financial detail
was invented beyond an illustrative example (a screen for rising free cash
flow plus insider buying, surfacing 3 candidates) built to visualize the
source's own literal job line — not a claim about any real screen the skill
has run.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the source's own stated job description — not
an inference about the unread SKILL.md's internal instruction text.
