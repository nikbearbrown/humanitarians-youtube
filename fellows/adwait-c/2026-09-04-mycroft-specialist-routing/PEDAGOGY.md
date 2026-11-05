# PEDAGOGY — Gate P (narration review before audio)

Weekly work video · Friday 2026-09-04 · Mycroft Finance Investigator

## The one idea

**The supervisor ranks evidence gaps by money and routes them to specialists, and every
ranked gap is blocked on an owner's explanation that no agent in the system can write.**

A summary would lead with "it now uses multiple agents." That is the least interesting true
sentence about it, and it is the sentence every multi-agent demo already makes. The week's
real work was the ordering (verify before routing), the ranking rule (arithmetic over
verified periods, not vibes), and the fences around each specialist.

## Stands alone

No back-references, no week or episode number. A viewer arriving cold loses nothing.

## HAI PM criteria

1. **Brutalist format** — `ai-explainer`, 13 beats, zero slates.
2. **4K at source** — 3840×2160; the 9:16 cut at 2160×3840.
3. **Both aspect ratios** — 9:16 derived via `./art shorts`.
4. **Formatting clean** — frame-level QC; both mono tables sized from their longest line.
5. **Intro line verbatim** — *"Hi, I am Adwait Changan, and this video is about turning a
   single finance agent into a small team of specialists."*
6. **Real takeaway** — the viewer leaves with a test for their own multi-agent system: for
   every delegated task, what evidence closes it, and can any agent here actually produce
   that evidence? BHTF makes it active.

## PROOF

- **Framework before examples** — B01 states verify / rank / route before the first table.
- **The falsifiability beat is B05, and it points at my own build.** The obvious claim about
  a specialist system is that it gets more done. B05 shows the opposite where it counts: the
  highest-ranked gap in the queue, worth 200,000, is waiting on `OWNER_CAUSAL_EXPLANATION`,
  which nothing in the system can produce. A video that skipped that beat would be a demo.
- **Side-by-side** — B03 and B05 each hold all three ranked gaps in one frame.
- **Worked example** — B03 and B05 are the framework run on the real generated queue.

## Honesty notes confirmed at this gate

- [x] **Every figure is copied from the generated report**, not from a written summary:
      `reports/generated/mycroft-finance-investigator-routing-week36.md`. Revenue 200,000,
      COGS 100,000, opex 36,000; four delegations; the missing-evidence column verbatim.
- [x] **B06 is verbatim** via `inspect.getsource(orchestration._category_priority)`; ten
      lines, counted not estimated.
- [x] **"Two categories share one specialist" is checked against the trace** — cogs and opex
      both route to `cost-specialist`. It matters because one-agent-per-row is the thing this
      design is avoiding, and the report proves it did.
- [x] **No causal language.** The video says the queue is *ranked by money*; it never says
      revenue caused anything. The report's own classification is
      `EVIDENCE_GAP_WORK_QUEUE_NOT_CAUSAL_ANALYSIS` and the narration matches it.
- [x] **Synthetic sample data and an OPEN human gate** are stated on screen in B08 and the
      verdict, not buried.
- [x] The closing caption on B08 quotes the report's own last line verbatim: *"A prioritised
      queue is not an approved explanation or decision."*

## Verdict

- Plan: APPROVED — 13/13 Remotion, zero slates, no consecutive pattern repeats.
- Narration: APPROVED — body beats 34–62 words.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by the build agent under the fellow's standing
> delegation. Unlocks audio and the master render. Does not authorize publishing or upload.
