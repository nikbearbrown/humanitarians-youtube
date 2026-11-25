# PROOF — Review Results: "Who Does What, By When."

*Reviewed with the PROOF protocol (skeptical explainer-video standard), from the rendered
4K frames + narration/beat sheet of both cuts. Creator: for Sanjana / @HumanitariansAI.
Topic: Gen AI tools in management. Film 1 of this series (`/series` N/A).*

---

## Verdict

**clear-for-public.** Teaching **11 / 12**. Production gate **PASS**.

> This film attempts to teach a *reusable method* — turn meeting talk into owned, dated,
> triaged actions — and delivers it, because the framework (owner + task + due, triaged by
> impact + urgency) is shown before any example, the triage runs on a real transcript on
> screen, and the revision makes the payoff visible: the extraction surfaces two gaps a
> summary would have buried. It loses its one point on *friction* — the film resolves the
> tension for the viewer rather than making them predict — and the honest soft spot is that
> the v1 "summary" is drawn a little weak to sharpen the contrast (see Calibration).

Both the **16:9** and **9:16** cuts earn the same verdict.

---

## Rubric

| Criterion | What it means | This cut | Why |
|---|---|---|---|
| **Explicit framework** | Organizing idea shown as a structure *before* the examples | **2** | B01 shows `OWNER + TASK + DUE` and `PRIORITY = impact + urgency` as a built graphic, ahead of the transcript. |
| **Reusable rubric** | A viewer could apply it to a *new* case | **2** | The axes are generic; the CTA hands the exact extraction schema to reuse on any meeting. |
| **Worked example** | At least one case walked through live | **2** | A real 6-line transcript is run through v1 and v2; priorities are computed on screen, not asserted. |
| **Falsifiability / edge case** | Framework stress-tested against an ambiguous/counter case | **2** | The two **gaps** (SSL cert = no owner; interviews = no owner + no date) are shown being flagged — the framework tested against items that don't fully fit it, on screen. |
| **Active task** | CTA requires the viewer to *do* something structured | **2** | "Your turn" hands a copy-paste extraction prompt that ranks actions and lists gaps to close — run live in the meeting. |
| **Friction** | Viewer must resolve a tension, not just receive facts | **1** | The summary-vs-extraction contrast is real tension, but the film resolves it; it never pauses for the viewer to predict which item has no owner. |

**Total: 11 / 12** (ship bar is 8).

---

## Production gate

| Check | Result | Note |
|---|---|---|
| **Evidence legible at assertion** | **PASS** | Every claim beat's artifact (rubric, code, action table) is readable when the claim is made. Verified by the toolkit's GATE T (type-lock) on both cuts. |
| **Sources on screen** | **PASS** | The actions and priorities are computed on screen from the visible transcript + `actions.py` — the output is its own receipt; the on-screen numbers are the real program output (see `../FACTCHECK.md`). |
| **Side-by-side at comparison** | **PASS (with edit)** | v1 (summary) and v2 (extraction) are shown sequentially (B04 → B07), each held >2s; they are not held together. The one production edit worth making. |

---

## The problem (single biggest fix)

**Show the misattribution limit, don't just say it.** The film earns the claim "the tool only
hears what was said — verify with the room," but only narrates it. One 3–4s beat where the
model mishears who committed (assigns the SSL cert to the wrong person, then a human corrects
it) would convert the strongest skeptical objection into on-screen proof and tighten *friction*.

---

## Do next (punch list)

1. **[EDIT]** Add a **side-by-side** of the v1 topic list and the v2 action table (or one board
   that transforms from one to the other) held ≥2s, so the comparison is shown together.
2. **[EDIT / NEW SCENE]** Add the **misattribution beat** from *The problem* — a worked
   correction, not a caption.
3. **[EDIT]** Strengthen the v1 "summary" so it isn't a strawman (see Calibration) — e.g. let the
   summary include one owner it *did* catch, so the lesson is "structure + triage + gaps," not
   "summaries are useless."
4. **[EDIT]** (9:16) The vertical drops the B08 falsifiability note to fit the portrait text
   floor; fold "verify with the room" back in as a full-width end caption at ≥72px.

All fixes are cheap edits to the existing cut — no reshoot.

## Calibration (honest self-critique)

The v1 pass renders the "summarize" output as bare topics with no owners or dates. A good
model summary is usually a bit better than that, so the contrast is drawn slightly in the
film's favor. The *structural* claim still holds — a summary is prose to read, an extraction
is a triaged, owned worklist with the gaps surfaced — but a skeptic would (fairly) push on the
strawman, so the narration is careful to attack "summarize" the instruction, not the model.

## What works (keep)

- **Framework before examples**, and the framework is a one-line rule you can actually apply.
- **The gaps are the payoff.** Flagging the unowned/undated items in terracotta is the single
  clearest argument for extraction over summary — it shows value a summary structurally can't.
- **The output is a real receipt** — computed from the transcript by the shown code.
- **The CTA is a scaffold**, not a slogan: a prompt that ranks and lists gaps to close.
- **Legibility and restraint** — Claude palette, one terracotta accent used only to flag gaps;
  both cuts pass the type-lock at native 4K.

---

### Scorecard

| | 16:9 | 9:16 |
|---|---|---|
| Teaching | 11 / 12 | 11 / 12 |
| Production gate | PASS | PASS |
| Verdict | clear-for-public | clear-for-public |
| Resolution | 3840 × 2160 | 2160 × 3840 |
