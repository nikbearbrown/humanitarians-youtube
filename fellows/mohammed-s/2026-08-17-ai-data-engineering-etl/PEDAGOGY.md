# GATE P — narration review · `ai-data-engineering-etl`

**Title:** ETL, Simplified
**Skill:** `ai-explainer` (the tight reel)
**Register:** Teardown · **Voice:** Kokoro `am_onyx` ("Onyx") · **Palette:** claude
**Deliverables:** 16:9 at 3840×2160 **and** a native-portrait 9:16 cut at 2160×3840
**Narrator:** Mohammed Hussain (no channel persona — IN-FOR-BEAR LAW dropped, per
the prior builds in this book)

> **Signature required before any audio is generated.** Audio here is free; this is
> a quality gate, not a cost gate. Sign by replacing the verdict line at the bottom.

---

## The ONE idea

**AI collapses the glue in ETL, not the judgment.** Schema mapping, connector
boilerplate, tests and docs stop being handwritten. What does *not* move is
deciding what a mismatch *means* — and the new failure mode is a pipeline that
runs green while the values are quietly wrong.

Everything in the reel is built to land that sentence. If a beat does not serve
it, the beat is wrong.

## Who this is for

Data engineers and analytics engineers who have already shipped pipelines and are
deciding how much of the work to hand to a model. Not an "AI is amazing" reel and
not an "AI is useless" reel — a line-drawing reel.

## The arc

| Beat | Act | What it must land |
|---|---|---|
| B00 | INTRO | Who is talking, what the video is about, and the ask arriving already answered. Opens on the user-specified line: *"Hi, I am Hussain, and this video is about…"* |
| B01 | PROBLEM | The glue between source and destination **is** the work — extract and load are easy, the middle is where the weeks go. |
| B02 | ASK | The real prompt: two schemas, one instruction, *do not guess*. |
| B03 | RESULT | 12 match, 3 don't — and the model **found** them without **deciding** them. |
| B04 | CODE | The actual generated transform. Read it like a diff, not an answer. |
| B05 | JUDGMENT | The honest split: what it is good at vs. what it cannot own. |
| B06 | RISK | Green row counts, wrong values. Runs ≠ right. |
| B07 | SUMMARY | The verdict artifact — four lines. |
| B08 | NEXT STEPS | The handoff prompt, read aloud verbatim and then discussed. |
| B09 | OUTRO | Title restate. |

## Where the misconception is broken

Most "AI for data engineering" content stops at *"look, it wrote the pipeline."*
This reel keeps going one beat past the demo: **B03 ends on `0 resolved`** and
**B06 shows the pipeline succeeding while being wrong**. That pair is the
pedagogical hinge. If a reviewer cuts one, the reel becomes the thing it is
arguing against.

## SHOW-DON'T-TELL check

Every body beat carries a `show` block in the beat sheet and is a native animated
illustration, not a slide:

- B01 — glue strips physically stack until they dwarf both endpoints.
- B03 — mapping lines draw; flags unfurl on the spoken column name; the
  `0 resolved` counter never moves off zero.
- B05 — left items check in; right items arrive as rings that never fill.
- B06 — the counter races to green while a second track drifts in terracotta.

No beat here could be exported as a static slide. **PPT TEST: pass.**

## Honesty (DOUBLE-CHECK LAW)

- No vendor benchmarks, no adoption statistics, no model version numbers that
  will date the video. Nothing is cited that isn't a property of the type systems
  involved.
- The three mismatches are real, checkable type facts: `text` → `timestamptz`
  needs a parse; IEEE-754 `float8` → `numeric(12,2)` rounds; `NULL` → `NOT NULL`
  has no defined landing place.
- The 12-match / 3-flag split in B03 is a **worked illustrative example** and is
  captioned as one on screen. It is not a measurement of a real migration.
- The B06 scenario (counts green, values drifting) is presented as a *failure
  mode this enables*, not as an incident that was observed.
- `₹`/currency figures are deliberately not asserted — the drift beat says
  "quietly drifting", not a fabricated number.

## Narration — full script for review

**B00 · INTRO**
> Hi, I am Hussain, and this video is about how AI is changing data engineering
> — moving data from one pipeline into another, and why ETL is finally getting
> simpler. Not because a model builds your warehouse. Because the boring ninety
> percent stops being handwritten.

**B01 · PROBLEM**
> Every pipeline is the same shape: a source, a destination, and a mountain of
> glue in between. Rename this column. Cast that timestamp. Handle the null the
> vendor swears never happens. Extract and load are easy — the transform in the
> middle is where the weeks go.

**B02 · ASK**
> So here is the ask I actually give Claude. Not “build my pipeline.” Two schemas,
> and one instruction: map the columns, flag every mismatch you cannot resolve,
> and do not guess.

**B03 · RESULT**
> Twelve columns line up. Three do not. Created-at is a string going into a timestamp.
> Amount is a float going into a decimal — a rounding bug waiting for month-end.
> And customer-id is nullable on one side, not-null on the other. Claude found
> all three. It decided none of them.

**B04 · CODE**
> And this is what it wrote. One rule per flag. Parse the date. Move money off
> the float. Make the null explicit instead of silently dropping the row. Read
> it like a diff, not like an answer.

**B05 · JUDGMENT**
> It is genuinely good at mapping schemas, boilerplate, tests, and reading a two
> a.m. stack trace. It cannot tell you what the number means, what the business
> promised, or what downstream was guaranteed. It writes the pipeline. It does
> not own it.

**B06 · RISK**
> And here is the failure this creates. The pipeline runs clean. Green check,
> row counts match, nobody gets paged — while a bad cast quietly rounds every
> amount the wrong way. A pipeline that runs is not a pipeline that is right.

**B07 · SUMMARY**
> So, the verdict. AI collapses the glue, not the judgment. It flags the mismatches;
> it never resolves them. And it makes code review the most valuable skill on
> the team — because writing just got free, and reading did not.

**B08 · NEXT STEPS**
> Your turn. Paste this into Claude: here is my source schema and my target schema
> — map every column, and for each mismatch, tell me the failure it causes in
> production and the assertion that would catch it. You are not asking for the
> mapping. You are asking for the test.

**B09 · OUTRO**
> ETL, simplified. The glue, not the judgment. I'm Hussain — thanks for watching.

## Narration budget

398 words across 10 beats — about 119 seconds at Onyx's measured pace. Body beats
run 37–51 words. B08 (51) is the HANDOFF beat and is exempt: HANDOFF LAW requires
the prompt be read aloud verbatim *and* discussed.

## GATE P amendment — the shortening

The reviewer signed **PASS with a cut**: bring the reel under 2:00. Applied:

1. **The standalone E/T/L mechanism beat was dropped.** Its one load-bearing line —
   *"extract and load are easy, the transform in the middle is where the weeks go"* —
   was folded into B01, so the reel still names the three verbs and still says which
   one carries the work. The `EtlStages` composition stays registered in `Root.tsx`
   as a reusable illustration; this cut simply does not consume it.
2. **B03 and B05 were tightened**, and every other beat trimmed. 598 words → 398.
3. **Nothing load-bearing was removed.** The pedagogical hinge survives intact:
   B03 still ends on `0 resolved`, and B06 still shows the pipeline passing while
   being wrong. Those two beats were protected from the cut by design.

---

## VERDICT: PASS

Signed: **Mohammed Hussain** — 2026-08-30
Signed in session, with the shortening amendment above. Audio generated after this
signature, never before.
