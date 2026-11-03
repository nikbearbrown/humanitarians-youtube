# GATE P — Pedagogy review · `ai-data-quality`

**Reel:** The Rule, Not The Report. (12 beats · ~3:30 · Kokoro `am_onyx` "Onyx")
**Skill:** `ai-explainer` · Register: Teardown · Narrator: Hussain (first person)
**Reviewed:** 2026-08-30

---

## The ONE idea

> **AI's real contribution to data quality is not cleaning values. It is
> proposing, evidencing, and maintaining the RULES — at a scale humans have
> never been able to reach — while a human still ratifies every one.**

Everything in the reel is built to land that sentence. If a viewer remembers
one thing, it is the test in B09: *can this rule fail a row, and does that
failure reach a person?*

## Why this is worth 3.5 minutes

The default treatment of this topic ("AI cleans your data!") is both wrong and
dangerous — it points people at the one application that destroys
auditability. The honest version is more useful and less obvious: the
bottleneck was never the cleaning, it was the **rule-writing**, and that is
the part that scales badly for humans and well for a model. That inversion is
the teachable moment.

## The teach chain (does each beat earn its place?)

| Beat | Job in the chain | Earns it? |
|---|---|---|
| B00 | Frame: "valid" is a decision somebody has to make 4,000 times | ✅ names the real problem in the first breath |
| B01 | Destroy the false comfort: the 98.7% measures presence and type, not meaning | ✅ the reveal (score lifts, six spellings all PASS) is the whole argument in one image |
| B02 | Why humans can't just write more rules — the arithmetic | ✅ supplies the *why AI* without ever asserting "AI is good" |
| B03 | Define the unit precisely: a rule is a thing that can fail a row | ✅ this is the load-bearing definition; without it B05–B07 are mush |
| B04 | The correct ask (and the wrong one) | ✅ ASK→RESULT receipt; also inoculates against "clean my data" |
| B05 | What good output looks like: evidence *before* rule, blast radius attached | ✅ shows the deliverable, not a claim about it |
| B06 | The human gate — the part that gets skipped | ✅ this is the ethical spine; 218/59/41 reconciles to B00's 318 |
| B07 | Rules at run time: quarantine + owner routing | ✅ converts a document into an operating system |
| B08 | Teardown: three honest failure modes | ✅ the register's value; without it this is a vendor ad |
| B09 | Verdict recap, one page | ✅ |
| B10 | Handoff prompt, read aloud and discussed | ✅ the "columns it refuses to guess on" note makes it a real prompt, not "learn more" |
| B11 | Title restate | ✅ |

## Register check (Teardown)

Mechanism first, then judgment. B01/B02/B03 explain how it actually works
before B06/B08 judge it. The judgment lands on both sides: B06 says the
model is not allowed to decide, B08 names three ways the whole approach
bites. Nothing in the script is a product claim, and no vendor, tool or
model capability is asserted anywhere.

## SHOW-DON'T-TELL check

Every body beat has a `show` block of ordered visual events, authored before
the narration. Evidence is on screen, judgment is in the voice:

- The six country spellings are **read by the viewer**, not listed by the voice.
- The 330-day arithmetic **computes on screen**; the voice only reacts to the total.
- The 1,284 failing rows is a **counter that spins**, not a spoken statistic alone.
- The 318 → 218/59/41 sort is a **physical sort into three lanes**.

PPT test: no beat is a headline-plus-paragraph hold. B08 is the closest
(three cards) and is saved by staged reveal + the terracotta underline on the
one that matters.

## Honesty check

Every on-screen figure is a **declared worked example**, not a cited
statistic — see `FACTCHECK.md`. Each numbered beat carries a small
`Worked example · illustrative figures` footnote so no viewer can mistake it
for industry data. The reel makes **no** claim about how well any real model
performs at this task.

## Narrator override (logged)

The human asked for a first-person intro — "Hi, I am Hussain, and this video
is about…". That replaces the IN-FOR-BEAR sign-off, so:

- B00 opens in Hussain's own voice; B11 signs off "I am Hussain."
- The folder chip and outro handle read `@HussainShariff` (human's choice).
- Voice remains Kokoro `am_onyx` ("Onyx") — the house male voice, free.

## Narration budget

Body beats 52–62 words (law: 45–70). ✅
Bookends (B00 57 · B09 62 · B10 68) are exempt; B10 is long because HANDOFF
LAW requires the prompt to be read aloud and then discussed.

---

## VERDICT: PASS

Signed off by the human (Hussain) — build authorized 2026-08-30, with the
narrator override above and the worked-example labelling as the condition of
the pass.
