# SCRIPT.md — Claude, Earnings Preview Single. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-earnings-preview-single` (Teardown, skill-teardown
format) — question and true facts carried over verbatim from the source;
narration re-registered to Plain (explain, then stop); cold open replaced
with the BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** unlike sibling redos in this loop, the source
beat_sheet.json here is fully filled in — no placeholder gap. Facts kept:
the skill's job ("generate a concise 4-5 page equity research earnings
preview for a single company: recent earnings transcript, competitor
landscape, valuation, and recent news, into a professional HTML report"),
its three files (LICENSE, report-template.md, SKILL.md — the latter two
accented in the source as the ones that matter), its linear pipeline (read
SKILL.md, execute steps in order, return output), and its specification
semantics (repeatable results, a hard limit at the file's edge).

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude decides whether a stock is a buy once it picks up the
earnings-preview-single skill. It doesn't — it fills in a fixed report
template. Let's see what's actually inside that file.

## Act I — the wrong guess

**B01 — Sounds like analyst judgment**
Hear "Claude has an earnings-preview skill" and it sounds like Claude is
doing the analyst's job — reading the numbers and forming its own view on
whether to buy.

**B02 — Broken, with a case** (pays off B00)
But nothing about its financial judgment changes. Delete the skill's folder
and Claude doesn't lose any investment opinion — there was none to begin
with. It just stops filling in that one template.

## Act II — the mechanism

**B03 — Two files** (ANCHOR PLANTED)
Here's what's actually inside: a license, and two files that matter — a
forty-four-page report template, and a SKILL.md that tells Claude how to
fill it in: pull the latest earnings transcript, map the competitor
landscape, note the valuation, and fold in recent news.

**B04 — Read it, then follow it in order**
Claude reads that SKILL.md and works through the steps in order — transcript,
competitors, valuation, news — pouring each into the template's shape, no
branching unless the file itself says branch.

**B05 — Template, not judgment**
That makes it a template-filler, not a stock picker. The payoff: the same
four-to-five page structure, filled from real inputs, every time. The limit:
it never forms an opinion the template doesn't ask for.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So earnings-preview-single never gave Claude a view on the stock. It just
guarantees that every run pulls the same categories of fact — transcript,
competitors, valuation, news — into the same report-template.md shape.

## Act III — both directions

**B07 — Neither one is proof**
A report that states a number with total confidence doesn't prove Claude
checked it against a second source — the template may simply present figures
in a confident voice. And a report that hedges a claim doesn't mean the
underlying data was shaky — the template may ask for cautious language in
that section regardless.

## Close

**BCRY — carry-out**
A skill named earnings-preview-single doesn't hand Claude a view on the
stock — it's a template Claude fills in from the same categories of fact
every time, and forming an actual investment opinion is still on you.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to generate a concise four-to-five
page equity research earnings preview for a single company. Read the
earnings-preview-single skill and walk me through what you will do, before
you do it. That way you'll see exactly which categories of fact it pulls,
before the report gets written.

**BOUT — outro**
Claude, Earnings Preview Single. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "an earnings-preview skill" sounds like Claude gained analyst judgment |
| Wrong guess | B00 → B02 | "decides" corrected to "organizes"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | two files, read top to bottom, template not judgment |
| Anchor | B03 → B06 | report-template.md + SKILL.md, planted then returned to |
| Both directions | B07 | confident phrasing proves nothing about verification; hedged phrasing proves nothing about weak data |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts across to the anchor; B06 is a new anchor-payoff
beat restating the design tell against the named anchor; B07 (both
directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT = 11 beats —
the identical proportionate expansion used on the `claude-for-legal--claude-
liam-hiring-review` sibling redo. No financial detail was invented anywhere
in this expansion — every fact traces to the source's filled-in beats.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the source's own stated job description and
file list — not an inference about the unread SKILL.md's internal template
structure. Nothing here asserts what report-template.md's actual sections
or wording look like beyond "report template" and the four input categories
the source names (transcript, competitors, valuation, news).
