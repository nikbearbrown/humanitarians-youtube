# Feedback: "Can AI Discover New Quantum Materials?" — 9:16 vertical cut — Dhrumil Shah, film 2b

**Verdict:** **unlisted-until-fixed.** Teaching score **12/12**. Production gate
**PASS**.

One line: this is a native portrait recomposition, not a crop — the argument,
narration, and every cited figure survive the rotation intact, and the one
item holding it back is inherited from the 16:9 cut rather than introduced by
this one.

## What this review is, and is not

This cut shares its **content** with the approved 16:9 master: same narration,
same measured timing, same claims, same sources, same framework. That content
was already reviewed. Re-scoring the same six teaching criteria would be
theatre.

So the teaching rubric below is carried forward, and the real work of this
review is the **production gate** — because that is the only thing a change of
aspect ratio can actually break.

## Rubric (carried forward from the 16:9 review)

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | CLAIM still lands at 00:26, ahead of the first example at 00:35. The 3+2 grid changes the shape, not the timing. | **2** |
| Reusable rubric | Five axes plus a decision rule at 02:46–02:59, unchanged. | **2** |
| Worked example | LK-99 scored row by row at 02:33–02:46, unchanged. | **2** |
| Falsifiability | Four different verdicts across five axes, unchanged. | **2** |
| Active task | Scaffold with an executable stop rule, unchanged. | **2** |
| Friction | The model's genuine win at 01:00 reframed at 01:10, unchanged. | **2** |
| **Total** | | **12/12** |

## Production gate — the part this cut had to re-earn

| Gate | Portrait-master evidence | Status |
|---|---|---|
| Evidence legible at the moment of assertion | Eleven 4K portrait stills inspected on the final master. No clipped headline, overlapping text, card overflow, or obscured source plate. Three portrait-specific defects were found and fixed before this master — two in preflight, one only after inspecting the stills of an earlier completed render (see below). | **PASS** |
| Sources on screen, not just voiced | Every scene carries a `SOURCE` plate spanning the full safe width at 27 px with a 1.32 line-height, so long citations wrap to two lines instead of clipping — the specific failure mode a narrower canvas invites. Scene 03 still shows the full bibliographic citation. | **PASS** |
| Side-by-side at the moment of comparison | **This is the gate the rotation put at risk.** Scene 08's comparison is now top/bottom rather than left/right, but both panels are on screen **together for 11.2 s** — claim panel enters 02:10, replication panel 02:22, both held to 02:33. The axis of comparison rotated; the simultaneity did not. Confirmed in `_qc/final/08-lk99-stacked.png`. | **PASS** |

The third row is the one worth stating plainly. "Side-by-side" is a
description of a 16:9 solution, not the requirement. The requirement is that
the viewer can see the claim and its refutation **at the same time**, held long
enough to read both. A stacked layout satisfies that; a layout that showed one
panel, cut, then showed the other would not — regardless of orientation.

## Portrait-specific defects found and fixed

| # | Beat | Defect | Fix |
|---|---|---|---|
| 1 | B01 | Portrait narrows the plot, which pushed the centred `YBCO 92K` label underneath the unlabelled BSCCO point at 110 K. A label sitting on a data point is exactly the illegibility this film criticises elsewhere. | Added per-point label anchoring to `TC_DATA`; YBCO is now left-anchored clear of its neighbour. |
| 2 | B01/B02 | Scene 02 was bottom-light — a chart squashed into the top third with roughly 850 px of dead column beneath the CLAIM grid. | Chart height raised 700 → 860 px and the framework block moved down, using the height portrait actually provides. |
| 3 | **all scenes** | **Systemic.** Every scene was pinned to fixed tops carried over from landscape thinking, so content occupied roughly the top 40 % of the 3840 px column. Scene 09 was the worst: its rubric card ended at y≈1520 with the footer line stranded at y≈2580 and nothing between them. Nothing was illegible — but a frame whose bottom 60 % is empty reads as unfinished, not as margin. | Introduced a `ContentColumn` primitive centring each scene's content between the headline and the source plate; opacity-gated children keep their space so nothing shifts on reveal. Scene 09's rows were scaled up for the portrait column. Framing checked against the house `mycroft-thesisguard-9x16` cut. |

Defects 1 and 2 were caught in preflight. **Defect 3 was caught only after a
complete master had already rendered and passed every technical check** — the
QC stills showed it, the probe could not. That master was discarded and the cut
re-rendered. It is the clearest example in this project of why the workspace
rule is to verify renders by looking at frames rather than by probe output.

## Inherited defects that did not recur

The two defects found in the 16:9 cut — colliding high-pressure chart labels,
and funnel bars narrower than their own labels — do not reappear here. The
portrait composition inherits both fixes structurally: high-pressure values
live in a callout rather than as point labels, and the funnel label sits in
its own column rather than inside the bar. That is the fix holding under a
layout change, which is the useful test of whether it was a real fix or a
patch.

## The problem

**Unchanged and inherited: one number blocks release.**

Scene 04 displays **±9.5 K** at 200 px — the largest element in this cut too —
as the reported out-of-sample RMSE from Hamidieh 2018, and that figure has not
been checked against the primary paper.

Because both cuts show the same number, **verifying it once clears both
masters**. This cut adds no new content risk; it inherits the existing one.

## Do X next

1. **[EDIT — BLOCKING, SHARED]** Verify the ±9.5 K RMSE against Hamidieh 2018
   §4. If correct, both cuts move to clear-for-public. If it differs, edit
   `MethodScene` in **both** composition files, regenerate B05 in the 16:9
   project, update `AUDIO_BEATS` in both, and re-render both.
2. **[RESHOOT/NEW SOURCE, SHARED]** Scene 05 still teaches the funnel with an
   illustrative schematic and no instance. Same prepared slots as the 16:9
   cut.
3. **[EDIT]** Align `@remotion/paths` (4.0.490) with the workspace (4.0.486).
   This is now the third film carrying the note — fix it at the workspace
   level.
4. **[EDIT]** The two cuts now duplicate `TcChart`, `SourceTag`, `Card`, and
   `Reveal` with only sizing differences. A shared primitives module
   parameterised by canvas would mean a chart-label fix lands in both cuts at
   once, instead of being re-derived per orientation as it was here.

## What works

**The recomposition is honest about being a recomposition.** Nothing was
cropped, letterboxed, or scaled to fake a vertical frame. Where the portrait
canvas made a layout worse, the layout changed — the chart got taller rather
than narrower, a label moved rather than shrank.

**It kept the hard requirement and dropped the incidental one.** The easy
mistake in a 9:16 port is to preserve "side-by-side" literally and end up with
two unreadable 900 px columns, or to abandon simultaneity entirely and cut
between panels. This cut rotated the axis and kept the thing that mattered.

**Reused audio rather than a second copy.** There is no `mp3/` folder here by
design. Two copies of the same narration are two things that can drift, and
the sync script fails loudly if the source is missing rather than silently
rendering a stale cut.
