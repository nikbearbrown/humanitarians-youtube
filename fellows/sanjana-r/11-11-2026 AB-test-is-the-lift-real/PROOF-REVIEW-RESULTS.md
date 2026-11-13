# PROOF — Review Results: "Is The Lift Real?"

*Reviewed with the PROOF protocol (skeptical explainer-video standard), from the rendered
4K frames + narration/beat sheet of both cuts. Creator: for Sanjana / @HumanitariansAI.
Topic: product management (experimentation). Film 1 of this series (`/series` N/A).*

---

## Verdict

**clear-for-public.** Teaching **11 / 12**. Production gate **PASS**.

> This film attempts to teach a *reusable method* — don't call an A/B test a win until it's
> significant, and size the test before you peek — and delivers it, because the framework is
> shown before the example, the z-test runs on real numbers on screen, and the output is a
> genuine falsifiability demonstration: the "+20% win" fails the test at n=1,000 and only
> becomes real once the intervals pull apart. It loses its point on *friction* (the film
> resolves the suspense rather than making the viewer call it), and the honest soft spot is
> the confidence-interval overlap heuristic (see Calibration).

Both the **16:9** and **9:16** cuts earn the same verdict.

---

## Rubric

| Criterion | What it means | This cut | Why |
|---|---|---|---|
| **Explicit framework** | Shown as a structure *before* the examples | **2** | B01: a result = `lift + sample size + noise`, and "overlapping intervals → not a result yet," ahead of the test. |
| **Reusable rubric** | Applies to a *new* case | **2** | The z-test + sample-size method works on any experiment; the CTA hands the exact prompt. |
| **Worked example** | Walked through live | **2** | Real rates run through the two-proportion z-test; p-value and CIs computed on screen, v1 vs v2. |
| **Falsifiability / edge case** | Framework stress-tested against a counter case | **2** | The whole v2 beat *is* the stress test: the obvious "+20% win" is shown failing significance at n=1,000, then surviving at ~3,835 — on screen. |
| **Active task** | CTA requires structured action | **2** | "Your turn" hands a copy-paste z-test prompt and the rule "decide n before you look." |
| **Friction** | Viewer must resolve a tension | **1** | The counterintuitive "your win isn't real yet" is strong tension, but the film resolves it; it never pauses for the viewer to call significant-or-not first. |

**Total: 11 / 12** (ship bar is 8).

---

## Production gate

| Check | Result | Note |
|---|---|---|
| **Evidence legible at assertion** | **PASS** | Rubric, code, bars, CIs and verdict are readable when each claim is made. Verified by GATE T on both cuts. |
| **Sources on screen** | **PASS** | Every statistic (rates, p-values, CIs, required n) is the real output of the shown `abtest.py` (see `../FACTCHECK.md`). |
| **Side-by-side at comparison** | **PASS** | Stronger than most: the v2 beat shows the *transition itself* on screen — intervals wide-and-overlapping → tight-and-separated, verdict flipping — so the before/after is held in one shot. v1-vs-v2 is also shown in sequence. |

---

## The problem (single biggest fix)

**Make the viewer call it before the reveal.** The one place to lift *friction* from 1 → 2:
hold the n=1,000 frame and ask on screen "ship it? y/n" for a beat before the significance
verdict lands. That converts a demonstration into a decision the viewer has to make and then
check — the exact tension the topic is about.

---

## Do next (punch list)

1. **[EDIT]** Add a 2–3s "call it first" hold at n=1,000 (a "ship it?" prompt) before the
   verdict reveals — raises friction and dramatizes the trap.
2. **[EDIT]** Put a one-line on-screen source on B06 ("two-proportion z-test") so the method
   is named on the frame, not only in `SOURCES.md`.
3. **[EDIT]** (9:16) The vertical keeps the verdict + caption; confirm the CI whiskers read at
   phone size — if thin, thicken the whisker stroke one more step.

All fixes are cheap edits to the existing cut — no reshoot.

## Calibration (honest self-critique)

The film uses "overlapping confidence intervals → not a result yet" as its visual rule. That
is a *conservative* heuristic, not an identity: two per-group CIs can overlap while the
*difference* is still significant. The film is built so the two always agree (the on-screen
VERDICT is driven by the two-proportion z-test p-value, and the example is chosen so the
overlap and the test point the same way), and `FACTCHECK.md` states this. A stats-literate
viewer could still push on the heuristic, so the narration leans on the p-value as the actual
verdict and uses the overlap only as the picture.

## What works (keep)

- **The output is the argument.** Watching the intervals tighten and the verdict flip — same
  lift throughout — is the clearest possible case that significance is about sample size, not
  the gap.
- **Framework before example**, and it's a rule you can act on ("overlap → not yet").
- **Real statistics, on screen** — the p-values and required n are the program's real output.
- **The CTA is a scaffold** — a z-test prompt plus the discipline of fixing n before you look.
- **Restraint** — Claude palette, one terracotta accent (variant bar + the not-yet warning);
  both cuts pass the type-lock at native 4K.

---

### Scorecard

| | 16:9 | 9:16 |
|---|---|---|
| Teaching | 11 / 12 | 11 / 12 |
| Production gate | PASS | PASS |
| Verdict | clear-for-public | clear-for-public |
| Resolution | 3840 × 2160 | 2160 × 3840 |
