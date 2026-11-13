# PROOF — Review Results: "WSJF: What To Build Next."

*Reviewed with the PROOF protocol (skeptical explainer-video standard). Reviewed from the
rendered 4K frames + the narration/beat sheet of both cuts. Creator: for Sanjana /
@HumanitariansAI. Film 1 (no prior film to compare — `/series` N/A).*

---

## Verdict

**clear-for-public.** Teaching **10 / 12**. Production gate **PASS**.

> This film attempts to teach a *reusable prioritization method* (not WSJF trivia) and
> largely delivers it, because the framework is shown as a structure before any example,
> the ranking is computed from on-screen code and real data, and the revision makes the
> method's logic visible — it loses points only where the **falsifiability case is narrated
> rather than shown**, and where the two rankings are compared **sequentially rather than
> side-by-side**.

Both the **16:9** and **9:16** cuts earn the same verdict. Differences are noted per section.

---

## Rubric — does this explainer actually teach?

| Criterion | What it means | This cut | Why |
|---|---|---|---|
| **Explicit framework** | Organizing idea shown as a structure *before* the examples | **2** | B01 shows `WSJF = Cost of Delay ÷ Job Size` and the three parts of CoD as a built graphic, ahead of any backlog item. |
| **Reusable rubric** | A viewer could score a *new* case on the same axes | **2** | The axes (Value, Time-Criticality, Risk-Reduction, Size) are explicit and generic; the CTA hands the exact CSV columns to reuse. |
| **Worked example** | At least one case walked through the framework live | **2** | A 5-item backlog is scored and re-sorted on screen, twice; the reasoning step (÷ size) is shown, not just the conclusion. |
| **Falsifiability / edge case** | Framework stress-tested against a counter/ambiguous case | **1** | The limits ("blind to dependencies", "only as good as your estimates") are **stated** (note card in 16:9, narration in both) but a dependency overriding the ranking is **not shown** as a worked case. Gestured at, not demonstrated. |
| **Active task** | CTA requires the viewer to *do* something structured | **2** | "Your turn" hands a copy-paste prompt that computes WSJF on the viewer's own backlog **and flags dependency conflicts** — not "ask Claude". |
| **Friction** | Viewer must resolve a tension, not just receive facts | **1** | The counter-intuitive result (big feature sinks; security work leaps) creates real tension, but the film resolves it *for* the viewer; it never pauses for the viewer to predict the order first. |

**Total: 10 / 12** (ship bar is 8). The two dropped points are the same in both cuts.

---

## Production gate (binary — can veto publish)

| Check | Result | Note |
|---|---|---|
| **Evidence legible at the moment of assertion** | **PASS** | Every claim beat's artifact (formula, code, ranked board) is on screen and readable when the claim is made. Verified against toolkit GATE T (type-lock) on both cuts: text ≥ the 1.9%-frame-height floor, 4.5:1 contrast, no overflow. |
| **Sources on screen, not just voiced** | **PASS** | The film's load-bearing claims are the *rankings*, and they are computed on screen from the visible `wsjf.py` + `backlog.csv` — the artifact is its own receipt. The numbers match the real run (see `../FACTCHECK.md`). *Minor:* the method's origin (SAFe) is credited in `SOURCES.md`, not on a lower-third. |
| **Side-by-side at the moment of comparison** | **PASS (with edit)** | The v1 (value-only) and v2 (full CoD) rankings are shown **sequentially** (B04 then B07), each held well over 2s, and the moving re-sort makes the change legible. They are *not* held on screen together — the one production edit worth making (below). |

A film can score well and still fail the gate; this one passes. Gate failures would mean
unlisted-until-fixed; none apply.

---

## The problem (the single biggest fix)

**The falsifiability case is told, not shown.** The film earns the right to say "WSJF is
blind to dependencies" — so show it: one 3-4s beat where a low-WSJF task that *blocks* a
high-WSJF task is forced to the top by a dependency arrow, overriding the score. That moves
*Falsifiability* from 1 → 2 and converts the strongest skeptical objection into on-screen
proof, at the frame (after B08) where the limit is currently only narrated.

---

## Do next (punch list)

1. **[EDIT]** Add a brief **side-by-side** of the Pass-1 and Pass-2 rankings (or a single
   board that re-animates with the "API rate limiting" row highlighted jumping #4 → #2), held
   ≥2s, so the comparison claim is shown together, not only in sequence.
2. **[EDIT / NEW SCENE]** Add the **dependency edge-case beat** described in *The problem* —
   a worked counter-case, not a caption. This is the one change that lifts the teaching score.
3. **[EDIT]** Add a one-line **on-screen source** ("Method: SAFe · WSJF") as a lower-third on
   B01 so the method's provenance is on screen, not only in `SOURCES.md`.
4. **[EDIT]** (9:16 only) The vertical drops the falsifiability **note card** to satisfy the
   strict portrait text-floor; fold the "mind dependencies & estimates" line back in as a
   full-width end-of-board caption at ≥72px so the caveat is on screen in the Short too.

All fixes are cheap edits to the existing cut — no reshoot, no new source material.

---

## What works (keep)

- **Framework before examples.** The formula graphic lands first; the examples are poured into
  it. This is the spine most explainers retrofit — here it's load-bearing and up front.
- **The output is a real receipt.** The ranked board is computed from code and data the viewer
  can run; the on-screen numbers are the actual program output, not a mockup.
- **The revision teaches the formula.** Changing Cost of Delay from "value only" to
  "value + time-criticality + risk" and watching the security task leap is the clearest
  possible argument for *why* CoD has three parts.
- **The CTA transfers skill.** A copyable prompt that ranks the viewer's own backlog and flags
  dependencies — a scaffold, not a slogan.
- **Legibility and restraint.** Clean Claude-palette type, one terracotta accent, generous
  negative space; both cuts pass the type-lock at native 4K.

---

### Scorecard

| | 16:9 | 9:16 |
|---|---|---|
| Teaching | 10 / 12 | 10 / 12 |
| Production gate | PASS | PASS |
| Verdict | clear-for-public | clear-for-public |
| Resolution | 3840 × 2160 | 2160 × 3840 |
