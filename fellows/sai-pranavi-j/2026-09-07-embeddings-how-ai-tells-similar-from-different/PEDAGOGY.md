# PEDAGOGY — self-assessment against `PROOF.md`

# Feedback: "Embeddings: How AI Tells Similar From Different (When Keyword Matching Can't)" — Sai Pranavi Jeedigunta

**Verdict (by PROOF's own rubric):** clear-for-public. **11/12**. Production gate **PASS**.
**This project's own publish authorization remains NOT AUTHORIZED** regardless of this verdict —
PROOF's ship rule is a teaching/legibility bar, not a substitute for the fellowship's separate
publish sign-off, which was never sought here.

One line: this film attempts to teach *when* to reach for embeddings over keyword matching, and
delivers a genuinely reusable 3-axis rubric with a real worked example and a real stress test —
the one soft spot is the closing task, which is concrete but doesn't show what a good vs. bad
self-audit looks like.

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| **Explicit framework** | The organizing idea is shown as a structure *before* the examples | **2/2** — B03 (`B03_ThreeQuestionsFramework`) shows all 3 questions (Wording Varies / Context Flips Meaning / Exactness Is The Point) as a skeleton — badge + label for all 3 — before any single question's explanation streams in, and well before B04's worked example. Framework-first, not narrated after the fact. |
| **Reusable rubric** | A viewer could apply the same axes to a new case without guessing | **2/2** — the 3 questions are genuinely generalizable ("does wording vary," "does context flip meaning," "is exactness the point") — not phrased in terms of the RIA example at all, so they transfer cleanly to a case the viewer supplies themselves. B06 restates them as a literal checklist, reinforcing reuse. |
| **Worked example** | At least one case is walked through the framework live — the reasoning step, not just the conclusion | **2/2** — B04 doesn't just assert "RIA and investment adviser are similar" — it shows the reasoning as a real 2D scatter (`meaning_space_frame()`/`plot_point()`), plots the 3 synonyms close together with a grouping ellipse, and separately plots an unrelated term far away, so the *mechanism* (closeness in a shared space) is visible, not just claimed. |
| **Falsifiability / edge case** | The framework is stress-tested against a counterexample or an ambiguous case | **2/2** — B05 is a genuine stress test, not a strawman: it reuses the exact same diagram grammar as B04 (so the viewer can't dismiss it as a different kind of case) and shows "Section 4.12"/"Section 4.13" landing close together in the *same* meaning space — the same mechanism that helped in B04 actively hurts here. The resolution is visibly different (gold/crimson warning triangle vs. B04's teal checkmark), so the contrast reads as a real reversal, not a restatement. |
| **Active task** | The CTA requires the viewer to *do* something structured — not "ask Claude" | **1/2** — B06 gives a real, structured decision procedure (ask the 3 questions on a rule you own; if the first two are yes and the third is no, migrate it) — this clears PROOF's low bar of "not a vague pointer." But it stops short of PROOF's own CTA guidance ("what does a good vs. bad result look like?"): the video never shows what applying the checklist to a concrete rule actually produces — no on-screen example of a rule that passes vs. fails the audit. That's the gap keeping this at 1, not 2. |
| **Friction** | The viewer must resolve a tension or ambiguity, not just receive facts | **2/2** — B05 is real friction, not just a second fact: the viewer has just been told closeness-in-meaning is the fix (B04), then is immediately shown a case where the identical closeness would be the bug. Resolving that (exactness is sometimes the point) is active reasoning, not passive reception. |

**Total: 11/12.**

## Production gate

- **Evidence legible at the moment of assertion — PASS.** Every claim beat's artifact was
  visually confirmed via `_qc/contact_sheet_4k_16x9.png` and `_qc/contact_sheet_9x16.png`: B02's
  document/rule cards, B03's full 3-row rubric, B04/B05's labeled scatter points and grouping
  indicators, B06's checklist — all legible, no clipped labels, no sub-40%-opacity ghosting.
  GATE V's 165 (16:9) / 98 (9:16) MAJOR findings are `underfill` (compact cards, not a
  legibility failure) and `low-contrast` (a whole-frame luminance heuristic diluted by dark
  backgrounds, not a specific illegible pairing — the one real contrast bug found, teal-on-ink,
  was fixed pre-render; see `BUILD-LOG.md`). 0 BLOCKER on both true masters.
- **Sources on screen, not just voiced — PASS (not fully applicable).** This video makes no
  external factual/statistical claims that require a citation — it's a conceptual mechanism
  explainer, not a fact-check-genre video. The one thing that could be mistaken for a sourced
  claim (B05's "Section 4.12"/"Section 4.13") is a fictional placeholder by explicit design (see
  `FACTCHECK.md`); it's not presented as a real regulation citation on screen, so there's no
  unsourced factual assertion to flag.
- **Side-by-side at the moment of comparison — PASS.** B04's cluster and far term are visible in
  the same frame simultaneously (held well past 2s). B05's "Section 4.12"/"Section 4.13" are
  plotted together in the same panel, held ~13s combined. B02's before/after (doc that matches
  vs. doc that doesn't) is sequential rather than simultaneous, but each state is held ≥1.5s with
  a clear visual verdict badge (✓ FLAGGED / ✗ NOT FLAGGED) — a legitimate before/after
  demonstration, not a "trust me" assertion.

## The problem

The closing task (B06) is the one beat that gestures at structure without fully demonstrating
it. If this project were revised, the single highest-value fix would be adding one on-screen
example of the checklist actually applied to a made-up rule — showing what a "yes/yes/no ->
migrate" answer looks like versus a "no/no/yes -> keep exact match" answer — so the viewer has a
worked template for their own audit, not just the three questions in the abstract.

## Do X next week

1. [EDIT] Add a 4th micro-beat (or extend B06) showing the checklist applied once, live, to a
   throwaway example rule — not RIA/Section 4.12 again, a fresh one — landing on one of the two
   possible verdicts, so the viewer has seen the decision procedure actually run, not just
   stated.
2. [EDIT] Consider a one-line on-screen tag on B02/B04/B05 ("illustrative example") matching the
   convention this fellow's sibling video (`2026-08-17-...`) uses in its B04 header
   (`"illustrative example — a generic before/after pattern"`) — strengthens the self-consistency
   between what's said in `FACTCHECK.md` and what's visible on screen, even though no viewer is
   likely to mistake either example for real given how the acronym/placeholder framing reads.
3. [EDIT] The `underfill` MAJOR count (165/288 sampled frames on the 16:9 master) is higher than
   this fellow's other 2 videos' own accepted precedent (~27-30%) — mostly driven by B00/B01/B03/
   B06/B07/B08's generous whitespace-by-design and B05's early single-dot hold matching a slow
   opening sentence. Not a legibility defect (confirmed by eye), but a future revision could
   trade some of that held whitespace for slightly denser mid-beat builds if a tighter GATE V
   MAJOR count becomes a hard requirement.

## What works

The B04/B05 pairing is the strongest structural choice in this cut: reusing the exact same
diagram grammar (bordered panel, dashed grouping ellipse, labeled dots) for both the "closeness
helps" and "closeness hurts" cases means the falsifiability beat reads as a genuine reversal of
the same mechanism, not a second, unrelated example bolted on to look rigorous. The 9:16 short's
redesign of that same diagram as a tall vertical scatter (rather than a shrunk crop of the wide
version) preserves that legibility in portrait, which is the harder-to-get-right half of this
kind of visual argument.
