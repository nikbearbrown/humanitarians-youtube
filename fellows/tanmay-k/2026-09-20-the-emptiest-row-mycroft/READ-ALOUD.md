# READ ALOUD — *The Emptiest Row*

Generated from `beat_sheet.json`. **Do not edit here** — edit the narration in
`beat_sheet.json` and regenerate this sheet, or the words you read stop being the words
that ship.

am_onyx · Pragmatist register · presenter Tanmay Kulkarni, in for Humanitarians AI
17 beats · 1018 words · target ~5:49

**Gate P fully cleared — draft 1 (16 beats) + draft 2 (B04) — see `PEDAGOGY.md`.**
Audio generation may proceed.

No clips or slates are rendered yet — this is the first Gate P pass, run on narration
alone before any audio or visuals are built. Each beat below describes its planned
on-screen content in place of a slate, pulled from `beat_sheet.json`'s own
`legibility.artifact` field.

**This film is about a real pattern in what Lloyds discloses, and a real, already-fixed
defect in Tanmay's own build — read both as findings, not as accusations.** Per direct
instruction: do not let this land as negatively portraying the case study or the
reference implementation. B10–B13 in particular cover a bug that was found and fixed
during Tanmay's own adversarial testing pass — if any line in that stretch sounds like a
gotcha about the build being sloppy, rather than a demonstration of testing working as
intended, mark it FIX. Same standard for B06 and B09: the finding is about Lloyds'
disclosure pattern and an already-well-documented gate design, not a takedown of anyone's
work.

## How to run the pass

1. Read every beat **out loud, at pace**. Not in your head — the defects this gate
   exists for are audible only.
2. After each beat mark `PASS` / `FIX` / `CUT` below. If `FIX`, write **what you heard**,
   not what you would rewrite.
3. Answer the six questions in `PEDAGOGY.md`. Only the read can answer them.
4. Sign the verdict line in `PEDAGOGY.md`. Audio stays blocked until it reads PASSED —
   Gate P is a precondition for narration, not a review of it.

Watch for three things this film can fail on. **First, the two-axis matrix language**
("mechanism disclosed," "human reviews before customer hears it") repeats across six
beats (B02–B06, B15) — if it starts sounding like a script tic rather than a returning
frame, mark it. **Second, the malformed-date beat (B12)** reads two similar date strings
aloud in the same breath — if they do not separate cleanly by ear, the whole beat's point
is lost. **Third, tone** — per the note above, B09 through B13 are the stretch most at
risk of sounding critical of the build rather than complimentary of the process that
tested it; read them at the same even, matter-of-fact pace as the rest of the film, not
with a "gotcha" lift.

---

## B00 · COLD OPEN · ~19 s
*declarative*

> on screen (planned): two numbers, side by side, unlabeled which system — "3 dated disclosures" vs "1 (reach only)"

One company.

Two of its own AI systems, both public, both live right now.

One of them has published three separate results over eleven months — search time, usage, all dated.

The other answers customers directly, with nobody reviewing what it says first, and publishes exactly one number about it: how many people it reaches.

`PASS / FIX / CUT` ____________

what I heard:

---

## B01 · HOOK + PRESENTER · ~19 s
*direct*

> say: **Kulkarni** = kul-KAR-nee
> on screen (planned): title card, four system names under the Lloyds name

Hi.

This is Tanmay Kulkarni, in for Humanitarians AI.

Lloyds Banking Group discloses four named AI systems across the same set of public documents.

Most coverage treats that as one company doing AI.

I wanted to know what happens if you refuse to average them, and ask the same two questions of all four instead.

`PASS / FIX / CUT` ____________

what I heard:

---

## B02 · METHOD · ~17 s
*expository*

> on screen (planned): empty two-axis frame — "mechanism disclosed?" / "human reviews before customer hears it?"

Two questions, and they're the whole method.

First: is the mechanism actually disclosed, do we know how the thing works.

Second: does a human review the answer before a customer ever hears it.

Every system gets scored on both, before I say a word about which one is good.

`PASS / FIX / CUT` ____________

what I heard:

---

## B03 · ATHENA ROW · ~20 s
*expository*

> on screen (planned): Athena row fills the matrix — mechanism = RAG (named), outcome = 59s→20s / 21k→35k+, human review = yes

Start with Athena, Lloyds' own colleague-facing assistant.

Mechanism: confirmed, named, retrieval-augmented generation, grounded to source articles.

Outcome: three separate dated releases across eleven months, search time cut from fifty-nine seconds to about twenty, usage climbing from twenty-one thousand colleagues to more than thirty-five thousand daily.

And a colleague reviews every answer before a customer hears it.

Full marks, both axes.

`PASS / FIX / CUT` ____________

what I heard:

---

## B04 · THIN SYSTEMS · ~29 s
*expository*
**[CHANGED since the draft-1 read — see below]**

> on screen (planned): two thinner rows fill in — HR shows the ~90% figure as real text; Complaints shows function confirmed, outcome cell empty; human-review column on both rows renders "N/A" instead of yes/no

Two more systems, and both thinner.

The AI HR assistant: one figure, about ninety percent of queries resolved on first contact, no volume, no time period, no method behind it.

The complaints tool: a confirmed function, classification and routing, and not one number attached to it anywhere in the public record.

Both internal.

Neither one answers a customer directly, so the second axis does not even quite apply here.

It takes a system that faces a customer at all before that question is worth asking.

**New since the signed draft-1 read:** the last two sentences. Added per PROOF Review 1's
falsifiability finding — this is the film's one moment where the human-review axis
doesn't cleanly fit a system, and the addition turns that into an explicit stress-test of
the framework instead of leaving it implicit. Everything before "so the second axis..."
is unchanged and already passed.

`PASS / FIX / CUT` **PASS**

what I heard: signed off 2026-09-21, "read aloud and pass B04" — see `PEDAGOGY.md` draft 2.

---

## B05 · FINANCIAL ASSISTANT ROW · ~25 s
*declarative*

> on screen (planned): fourth row fills in almost entirely with the same mark repeated — undisclosed / undisclosed / no

Now the fourth system, the one that actually talks to customers.

Lloyds' financial assistant, live to over half a million Bank of Scotland customers.

Mechanism: undisclosed.

No architecture, no confidence score, no stated rule for when it hands off to a human.

Outcome: also undisclosed, not one resolution rate, not one escalation number, nothing.

And this is the one system, of the four, where nobody reviews the answer before the customer hears it.

`PASS / FIX / CUT` ____________

what I heard:

---

## B06 · THE PATTERN · ~31 s
*declarative — load-bearing*

> on screen (planned): full four-row matrix at once, financial assistant row visually highlighted
> tone check: about Lloyds' disclosure choices, not a judgment on the case study itself

Lay the four out and a pattern falls out that no single write-up would show you.

The two internal tools get thin disclosure because, frankly, nobody outside the company needs to see it.

Athena gets rich disclosure, and a human checks every answer anyway.

The one system with the least disclosed mechanism and the least disclosed outcome is also the only one of the four answering a customer with nobody checking first.

Same company.

The gap isn't an accident of what got written down.

It's exactly where the risk actually sits.

`PASS / FIX / CUT` ____________

what I heard:

---

## B07 · BRIDGE TO THE BUILD · ~21 s
*expository*

> on screen (planned): quote card, attributed — case study §4b, "Why the financial assistant, and not Athena"

So which system do you build a reference implementation around?

Not Athena.

A human already catches Athena's mistakes, so an undisclosed detail there doesn't reach a customer unfiltered.

You build around the row where that safety net doesn't exist.

That's the choice this case study makes, in its own words: the financial assistant is where an undisclosed boundary actually does the damage.

`PASS / FIX / CUT` ____________

what I heard:

---

## B08 · ARCHITECTURE · ~19 s
*expository*

> on screen (planned): three-box pipeline diagram — Intake → Retrieval → Authorization Gate

Here's what that build actually is.

One pipeline, three stages, run in strict order: intake, retrieval, authorization.

Not a swarm of agents, a single linear sequence, because that's what Lloyds' own record actually supports for this system.

A customer's question goes in one end.

Either an answer comes out the other, or it's handed to a human.

`PASS / FIX / CUT` ____________

what I heard:

---

## B09 · THE GATE · ~26 s
*even, matter-of-fact — not a reveal*

> on screen (planned): gate.py's constructor raise, docstring's Lemonade/Zurich/Capital One reference visible
> tone check: stated plainly as known territory, not built up as a discovery

One stage in this pipeline is the direct code version of the gap I just showed you: the authorization gate.

It ships with zero built-in rules for when to answer and when to escalate.

Ask it to run with no real decision rule supplied, and it refuses, at construction.

This exact refusal has already shown up at three other companies in this series.

By now, it isn't the discovery.

It's just what building this honestly looks like.

`PASS / FIX / CUT` ____________

what I heard:

---

## B10 · CLEAN ≠ CORRECT · ~20 s
*even — states a true, honest result*

> on screen (planned): "29 / 29 passing" stat card, second line fades in — "never tested: malformed input"
> tone check: this is a genuinely clean, honestly-recorded result, not a setup for embarrassment

Before any of that, the pipeline had to actually work.

The first complete build passed all twenty-nine of its tests, on the first run.

That's true, and it was recorded exactly that way, a clean pass.

But a clean pass only proves what you actually tested for.

And the first twenty-nine tests never once tried to break it.

`PASS / FIX / CUT` ____________

what I heard:

---

## B11 · THE ATTACK, ON PURPOSE · ~18 s
*declarative*

> on screen (planned): test_adversarial_edge_cases.py, the two crash-case test names visible
> tone check: "on purpose" is the operative phrase — this is deliberate, disciplined testing, not luck

So the next step was to attack it on purpose, feed it the exact kind of malformed, ugly input a real customer eventually types.

Two of those attacks crashed the pipeline outright: an amount sent as text instead of a number, a question sent as nothing at all.

Loud failures.

Easy to catch.

`PASS / FIX / CUT` ____________

what I heard:

---

## B12 · THE ONE THAT DIDN'T CRASH · ~22 s
*even, not triumphant*

> on screen (planned): `intake.py`'s own corrected docstring (lines 11–30), which already narrates this exact history in its own comment — no before/after diff, no separate broken-state visual, per direct instruction
> pronunciation: read the two dates slowly and distinctly — "two-oh-two-six dash six dash fifteen" vs. "two-oh-two-six dash oh-six dash fifteen" — if they blur together the beat's point is lost

The third attack didn't crash, which is worse.

Type a date without the leading zero, two-oh-two-six dash six dash fifteen instead of two-oh-two-six dash oh-six dash fifteen, against the earlier version of this code, and it came back with no transaction found.

A confident, wrong answer, for a transaction that was actually there.

Not a crash.

A wrong answer wearing a right answer's clothes.

`PASS / FIX / CUT` ____________

what I heard:

---

## B13 · THE FIX · ~18 s
*expository*

> on screen (planned): `intake.py:115-118` and `orchestrator.py:56-69` (the distinct `malformed_date` reason) shown together

Here's the fix, and it's smaller than it sounds.

A date that can't be read now gets its own name, malformed date, kept completely separate from no matching record.

I can't read this, and I checked and there's genuinely nothing here, are different claims about the world.

This pipeline no longer mixes them up.

`PASS / FIX / CUT` ____________

what I heard:

---

## B14 · VERIFIED, NOT CLAIMED · ~17 s
*declarative — closing the loop, not scoring a point*

> on screen (planned): terminal output, re-run live — "49 passed"

I didn't take any of this on the file's word.

I re-ran the whole suite myself: forty-nine tests, forty-nine passing, zero failing.

The row with the least disclosed mechanism, the one nobody else was checking, is now, line for line, the most adversarially tested code in the entire build.

`PASS / FIX / CUT` ____________

what I heard:

---

## B15 · THE RUBRIC, RESTATED · ~22 s
*direct*

> on screen (planned): the two-axis matrix, now generic and blank, ready for any company

So here's the move, and you can run it on any company that discloses more than one AI system at once.

Don't average them into one verdict.

Put each one on the same two axes, mechanism disclosed, human checking before a customer hears it, before you write a word about any single one.

The interesting finding is usually sitting in whichever row comes back empty.

`PASS / FIX / CUT` ____________

what I heard:

---

## B16 · SIGNOFF · ~6 s
*flat*

> say: **Kulkarni** = kul-KAR-nee
> on screen (planned): title card, cream ground

The Emptiest Row.

Tanmay Kulkarni, in for Humanitarians AI, signing off.

`PASS / FIX / CUT` ____________

what I heard:

---
