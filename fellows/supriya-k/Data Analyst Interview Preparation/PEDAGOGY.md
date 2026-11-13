# PEDAGOGY AUDIT (GATE P) — hai-sql-window-functions-tie-bug
# "The SQL Interview Bug Even a Correct-Looking Query Can Hide"
# Prepared by: Claude (agent) | 2026-07-24 | Awaiting human review

GATE P: a human reviews narration (on an animated slate, once beats are
built) and signs VERDICT before any audio is generated. This is a QUALITY
gate, not a cost gate — Kokoro audio is free. **No audio has been
generated for this reel.**

## Checklist

### 1. Required cli-explainer spine present
INTRO (B00) → PROBLEM (B01) → MECHANISM (B02) → CLI/CODE/OUTPUT cycle 1
(B03–B05) → CLI/CODE/OUTPUT cycle 2 = the revision (B06–B08) → SUMMARY (B09)
→ NEXT STEPS/HANDOFF (B10) → OUTRO (B11). All mandatory elements present.
**CHECK: complete.**

### 2. Revision Law
One full revision cycle present: check the buggy output (B06 narration
opens on "check the output before you trust it") → revised ask → revised
code → better, verified output (B08). **CHECK: satisfied.**

### 3. Actual-Code Law
Both CODE beats (B04, B07) show complete, real, runnable MySQL — no
pseudocode. The diff between them is exactly one function swap plus one
added tiebreaker column, discussed explicitly in B07's narration.
**CHECK: satisfied.**

### 4. Moving output, never a still
Both OUTPUT beats (B05, B08) are specified as Manim animations with rows
flying in and a live row-count ticker — not static tables.
**CHECK: satisfied at planning stage** (actual Manim scene code not yet
written — that's a build-phase task, not a planning-phase gap).

### 5. No fabrication / original-questions rule
Every claim traces to Chapter 4 or Chapter 7 of the signed, fact-checked
manuscript (see `SOURCES-FACTCHECK.md`). The one new element — sample
`plays` rows for the tie scenario — is illustrative data for the book's
own already-invented company, not a new real-world claim, and its query
results are hand-verified in `VISUAL-PLAN.md`.
**CHECK: satisfied.**

### 6. Handoff quality
B10's suggested prompt is directly runnable, specific to this episode's
lesson (ties in top-N-per-group queries), and is read aloud in full per
HANDOFF LAW rather than only shown on screen.
**CHECK: satisfied.**

### 7. No paid services
All visuals planned as Manim/Remotion; no stock media, no gen-AI clips,
no external API calls anywhere in the plan.
**CHECK: satisfied.**

## Outstanding for the human reviewer

- [x] Confirm the narration register (Pragmatist/HAI) reads naturally when
  read aloud — this review was done on the page, not on an animated slate
  (no audio/render exists yet to build one from).
- [x] Confirm the narrator-identity line ("Supriya, for Humanitarians AI," in
  B00 and B11) matches intent — this replaces the toolkit's default
  world-language-hello / "Hello, Bella" greeting pattern per explicit
  instruction.
- [x] Confirm the sample data and worked query results in `VISUAL-PLAN.md`
  before any Manim scene is built from them.

## VERDICT: PASS

Signed: Supriya Kushwaha (human, author)  Date: 2026-07-24  Evidence: approval given in chat ("Approve Gate P for all three existing video packages").
