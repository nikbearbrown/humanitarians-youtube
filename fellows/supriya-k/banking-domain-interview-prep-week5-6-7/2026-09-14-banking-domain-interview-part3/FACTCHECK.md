# Sources & Fact-Check — "The STAR Method Banking Panels Actually Score"

**Source chapters:** `chapters/12-behavioral-round.md`, `chapters/14-full-loop-mock-interviews.md`
(Stage 4 — Behavioral only). **Source fact-check:** `factchecks/MASTER_REPORT.md`.

## Claim trace

| # | Beat(s) | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B02 | The STAR definition — Situation/Task/Action/Result | Ch. 12, "The STAR method, and the failure specific to banking" (footnoted to Indeed Career Advice and Wikipedia — the general framework is externally documented, reused as-is) | CONFIRMED |
| 2 | B03 | The generic STAR failure — "all Situation, no Result" | Ch. 12, same section, quoted directly | CONFIRMED |
| 3 | B05 | The three banking-specific competencies | Ch. 12, "What a banking panel weights beyond the generic" — **explicitly labeled the book's own pedagogical synthesis**, not a published/attributed rubric | CONFIRMED as the book's stated position — this video keeps that same hedge (see "process vs. fact" section below), never presents it as an external industry standard |
| 4 | B06 | The three behavioral archetypes | Ch. 12, "Banking behavioral archetypes", quoted/condensed | CONFIRMED |
| 5 | B07 | The banking-specific failure — accepted vs. rejected Result phrasing | Ch. 12, same section, quoted directly | CONFIRMED |
| 6 | B08 | The delivery rule — "we fixed it" vs. naming the control | Ch. 12, "Building your story bank and delivering it", quoted directly | CONFIRMED |
| 7 | B10 | The weak-answer quote (full) | Ch. 12, worked example, quoted verbatim | CONFIRMED |
| 8 | B11 | The STAR-rewrite quote (full, all four parts) | Ch. 12, worked example, quoted/paraphrased directly from the book's own rewrite | CONFIRMED |
| 9 | B12 | What's scored — risk awareness, escalation, outcome/control | Ch. 12, worked-example closing note, quoted directly | CONFIRMED |
| 10 | B14 | The five-stage banking loop | Ch. 14, "Assembling the loop" | CONFIRMED |
| 11 | B15 | Stage 4 prompt — "Tell me about a time you found an error…" | Ch. 14, "Worked example — Daniel's full simulated loop", quoted verbatim | CONFIRMED |
| 12 | B16 | Daniel's answer and where it stops | Ch. 14, Stage 4, paraphrased/quoted directly | CONFIRMED |
| 13 | B17 | Daniel's full self-scoring table (all five stages) | Ch. 14, "Daniel's completed self-scoring sheet", quoted verbatim | CONFIRMED |
| 14 | B18 | The lesson and the final-week allocation principle | Ch. 14, "Turning the scores into a plan", paraphrased/quoted directly | CONFIRMED |

## The process/framing vs. attributed-standard distinction

Three different kinds of claim run through this video, and the narration is written to keep them
distinct rather than flattening them into one register:

1. **Externally documented fact** — the STAR method itself (Act I). This is a well-documented,
   widely-cited technique; the book cites Indeed Career Advice and Wikipedia, and this video reuses
   it as a settled fact.
2. **The book's own pedagogical synthesis** — the three banking-specific competencies (Act II) and
   the archetype/delivery framing built on top of them. The book is explicit, and repeatedly so,
   that no published source names these as a formally scored banking rubric — it is a defensible
   inference built on the well-documented STAR method plus the well-documented reality of heavy
   bank supervisory examination. This video's narration (B05) frames it the same way: "a banking
   panel is listening for three things the generic rubric doesn't name" — a claim about what the
   book argues panels listen for, not a claim that a named, published rubric says so.
3. **Illustrative worked example** — the weak-answer/STAR-rewrite (Act III) and Daniel's mock loop
   (Act IV) are the book's own pedagogical worked examples — a persona (Daniel, introduced in
   Ch. 1 and reused consistently through Ch. 14) walking through invented-but-representative
   scenarios. Nothing here is presented as a real transcript or a real bank's actual interview.

## What was NOT invented

Nothing. Unlike the SQL-bug video (which needed illustrative sample ledger data the book's worked
example didn't include), this video draws every quote, score, and worked example directly from the
book's own text — the weak answer, the STAR rewrite, Daniel's five prompts and answers, and his
five-stage self-scoring table are all quoted or paraphrased directly from Chapters 12 and 14, not
supplemented with any new invented content.

## Fact-check status

`factchecks/MASTER_REPORT.md` lists Chapter 12 among the chapters with **zero errors found**.
Chapter 14's one correction (a Stage 1/Stage 3 cross-reference and labeling drift) does not touch
Stage 4 (Behavioral), which is the only part of Chapter 14 this video uses.

## No paid services

Kokoro (local, free) for narration; Manim (local, free) for 11 scenes; Remotion (local, free,
already-installed `node_modules`) for 11 beats. No ElevenLabs, no Higgsfield, no paid API calls.

---

## v3 corrections (2026-10-16)

| Beat | v1 | Book | v3 |
|---|---|---|---|
| Title, B00, outro | "The STAR Method Banking Panels *Actually* Score"; "how banking interviewers actually score" | ch12:6, :16: "This book's own framing, not a documented industry rubric"; "not an attributed industry standard" | Title → "What a Banking Panel Listens For in a STAR Answer" (Supriya, 2026-10-16) |
| B00 vs B_VERDICT | "Banks don't grade a STAR answer differently" vs "A bank panel scores the Result differently" | ch12:3: the method is the same; what changes is "which half of the story a bank panel is straining to hear" | B00: "Same method; a different half of the story"; verdict: what the panel *listens for* in the Action and Result |
| B05 | "three things the generic rubric doesn't name", stated as fact | ch12:6: "pedagogical synthesis… not a published, cited standard" | opens "This is the book's own framing, not a published rubric" |
| B_VERDICT | "or the story doesn't score"; "correct answers, no credit" | ch14:29: STAR without a named escalation still scores 2; Daniel's other stages scored 2 | "Name them." (no absolute) |
| B17 | "Scored against the book's own rubric: a one" | ch14:29 rubric gives "STAR shape, but no named escalation" a 2; Daniel's self-score sheet (ch14:86) records 1 with "no named escalation or outcome" (the book is internally inconsistent) | "He scores that stage a one: STAR shape, but no named escalation or outcome" (his self-score, not a rubric claim) |
| B14 | "A realistic banking loop runs five stages back to back" | ch14:18: "Not every loop runs all five in one day, and not every bank labels them this way" | "can run five stages, though not every bank runs all five in a day" |
| B_VERDICT | "in the Result" | ch12:10: "in the Action and Result" | "in the Action and the Result" |
| B11 | dropped "a teammate had built"; escalation recipient missing; "a dbt test now catches it automatically" | ch12:55-58: a teammate's dashboard; flagged "to my teammate and our shared lead"; a plausible-range check | "a teammate's dashboard"; "flag your teammate and lead that day"; "a dbt range check" |
| B12 (screen) | "checked as a habit" | ch12:60: "a check worth running" | screen text follows the book |
| B05/B06 (screen) | "Examiner comfort" (dropped "audit"); "Survive an audit…" | ch12:14 "comfort under audit or examiner scrutiny"; ch12:34 "Working through" | screen text follows the book |
| B18 (screen) | invented bar proportions; omitted the final 48 hours | ch14:91 | bars labelled illustrative; final-48-hours block shown |
| B10/B15/B16 (screen) | doubled quote marks (“"…"”) | — | single quotation marks |
| B_YOURTURN | prompt paraphrased | HANDOFF LAW | read verbatim; on-screen text identical |
