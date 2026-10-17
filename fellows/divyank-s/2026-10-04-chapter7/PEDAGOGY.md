# PEDAGOGY — Claude, Signed. (deep-explainer, claude-liam)

Source chapter: `ai1-cli/chapters/07-facts-check-a-claim-record-it-sign-it.md`
(Chapter 7 — Facts: Check a Claim, Record It, Sign It), read in full.
Thesis: a fact is a record, not a recollection — models state fabricated
claims with the same fluent confidence as true ones, so the book keeps a
claims database (`facts.json`) governed by three rules (check before
searching, new facts enter unverified, verified facts are append-only),
exercised through trace → add → sign-or-refuse, closing Part I of the book.

## Spine check

- B00 cold open, signed for Divyank from the start ✓
- 4 acts × (1 `FluencySegmentCard` + 6 content beats) = 28 body beats:
  I why a fact is a record not a recollection (Mata v. Avianca, the
  `verified` flag), II the three constitutional rules, III the
  trace-add-sign-and-refuse exercise + the real worked example, IV the
  chapter's own failure table + the Part I bridge ✓
- VERDICT → HANDOFF ("Your turn.") → title-restate OUTRO ✓

## Fidelity to the source chapter

Every mechanism beat traces to a specific line in
`07-facts-check-a-claim-record-it-sign-it.md`: the Mata v. Avianca case
(opening), the `facts.json` schema (Overview), the three numbered rules
(Overview), the three-step exercise (trace/add/sign-and-refuse), the
worked example (the real Rosser Reeves USP entry, confirmed present
verbatim in the live `facts.json` this session), and the chapter's own
"what can go wrong" table (all 4 rows represented in Act IV). No claim
beyond the chapter + its research doc is asserted — see `FACTCHECK.md`.

## Lesson carried forward from the Chapter 6 build

Act-card beats (A1C–A4C) are given real spoken narration ("Act one: a
fact is a record, not a recollection.") and the correct
`FluencySegmentCard` prop shape (`{title, index}`) from the start — the
chapter-6 build shipped these silent with the wrong props, which made
`compile.py` fall back to a fully silent master until caught and fixed.

## Beat-mix contract

28 body beats — VOX 5/28 = **17.9%** (inside 15–30%), REMOTION 19/28 =
67.9% (absorbing the MANIM share, no Manim on this machine), CARD 4/28.

## Portrait (9:16 Short) plan, decided up front

`BinaryBranch`/`DivergentFates` assigned to A1-5, A2-4, A3-3, A4-3 — one
hero beat per act. Expect `shorts.py`'s auto cap-check to need a manual
`--drop` override, the auto-rewritten `BOUT` outro to need a hand
rewrite, and the derived `short/media/END.png` end-card to need its
handle regenerated explicitly (it bakes in `--handle`, default
`@nikbearbrown`, at PNG-generation time rather than reading the beat
sheet at compile time — found during the chapter-6 build).

## Honesty discipline

Every claim is kept at the level of the chapter's own text, its one
footnoted legal case, and the live `facts.json` file checked directly
this session. No fabricated version numbers, no benchmark claims. See
`FACTCHECK.md`.

## Time-limit expectation

Estimate: 508s (8.47 min) — inside the 5–10 min band with margin.

## Status

**VERDICT: PASS** — signed off by the human (Divyank Singh,
singh.divya@northeastern.edu) in chat, 2026-10-12, on review of this
PEDAGOGY.md, FACTCHECK.md, and the beat sheet's narration.
