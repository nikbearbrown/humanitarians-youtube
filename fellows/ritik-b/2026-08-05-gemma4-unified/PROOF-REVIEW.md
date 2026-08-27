# Feedback: "Gemma 4, Unified?" — Ritik, film 1

**Verdict:** `clear-for-public`. Teaching **12/12**. Production gate **PASS**.

One line: *This film attempts a skeptical teardown of an architecture claim and
delivers one — but the cut that was first handed over asserted every parameter
figure and the whole Platonic-Representation passage with no visible citation,
which is precisely the sin this format exists to punish.*

Reviewed from frames sampled at each claim moment plus the narration in
`NARRATION.md`. Nothing below is inferred from a beat I did not look at.

**Read the two-column scores as the real result.** The film did not arrive at
12/12 and PASS; it arrived at 10/12 and a gate FAIL, and was fixed. Revision 4
applied punch items 1–4.

## Rubric

| Criterion | What it means | First cut | Now |
|---|---|---|---|
| **Explicit framework** | organizing idea shown as a structure *before* the examples | **1** — B01's roadmap landed ahead of every example, but its three cards were an *agenda* (WHAT WAS DELETED / WHAT THE SCORES SAY / WHAT IS MISSING), and the actual transferable move surfaced only narrated, at the twist | **2** — the same three cards are now *questions*: WHAT WAS REMOVED? / WHAT DO THE NUMBERS SAY? / WAS THE TEST CONTROLLED? Shown as a numbered structure at 0:19, and the film then executes them in that exact order (B02–B04, B06, B07) |
| **Reusable rubric** | a viewer could apply the same axes to a new case | **1** — the procedure was encoded but never named as one; nothing told the viewer these transferred | **2** — the three questions are generic to any architecture claim, and the spark line says so ("Three questions, reusable"). Each card now reads axis-on-top, this-case-below |
| **Worked example** | one case walked through the framework live — reasoning, not conclusion | **2** | **2** — B07 is the real thing: it takes 69.1 vs 76.9, refuses the obvious reading, and shows *why* (12B vs 31B), then repeats it in the opposite direction with 0.067 vs 0.075 (12B vs 4.5B), parameter counts on screen as the reasoning happens |
| **Falsifiability / edge case** | stress-tested against a counterexample or ambiguity | **2** | **2** — the two benchmark families give **opposite** answers and the film leads with that. B09 draws a boundary against the claim it's most often confused with. B10 states a falsification condition for the film's own thesis |
| **Active task** | structured doing, not "ask Claude" | **2** | **2** — B10 hands over a copyable prompt naming the artifact and the procedure; revision 4 adds the answer key (`3 comparisons, every one size-confounded / 0 experiments hold size fixed`) so a viewer can tell whether they ran it right |
| **Friction** | viewer resolves a tension, not just receives facts | **2** | **2** — B05 forces a binary commit before any number appears; B06 supports *both* answers; B07 invalidates both. The viewer's own commitment is what gets broken |

**Total: 10/12 → 12/12.**

### Why 12/12 is not the same as "finished"

Two things the rubric does not price, and I am not going to pretend it does:

1. **Every figure is redrawn, not shown.** The film cites `arXiv:2607.02770` but
   never puts a page of it on screen. For a format whose rule is that the target
   must be *shown*, not paraphrased, cited-but-redrawn is the weaker standard.
   That's punch item 5, and it's the one real [RESHOOT].
2. **The narration never reinforces reuse.** The reusability lives in on-screen
   text and a three-word spark line. A viewer listening rather than reading is
   still only watching good reasoning, not being handed it.

## Production gate

**Legibility — PASS.** Every artifact is readable at the moment of its claim; no
element drops below the opacity floor while its claim is live. The toolkit's own
frame check (24 sampled frames) reports 0 BLOCKER / 0 MAJOR.

**Sources on screen — FAILED in the first cut, now PASS.** What failed, precisely:

- **B02, B03, B04 (0:30–1:20)** asserted 150M/550M ViT, 305M Conformer, 35M
  matmul, 48×48×3 patches, 16 kHz/40 ms frames and 262k vocabulary. The header
  carried the model and the date and **no citation**. Every number, unsourced.
- **B09 (2:25–2:50)** named the Platonic Representation Hypothesis, asserted
  representational convergence, and asserted it is **contested** because
  similarity metrics inflate with scale. Three claims, six model names, zero
  citations visible.
- **B01 (0:11–0:30)** quoted 550M/35M/305M on the roadmap cards with no source.

Fixed in revision 4: `arXiv:2607.02770 · Gemma 4 Technical Report` now sits on the
header line of B02–B04 and under the B01 cards, live for the whole beat;
`arXiv:2405.07987` sits beside the hypothesis and `arXiv:2604.18572` beside "and
contested" — each citation on the same line as the claim it backs; the six model
chips are labelled `pointers only · Show-o arXiv:2408.12528`.

Already passing before the fix: B00 (`reading arXiv:2607.02770…`), B06 and B07
(`GEMMA 4 TECHNICAL REPORT · TABLES 6–8` on the header while the numbers are up),
B08 (`arXiv:2607.02770 — Tables 6 and 8. The ablation is not among them.` on the
verdict card's face).

**Side-by-side — PASS.** B06 holds both benchmark families in one frame for the
full 20s beat; B07 holds the scores against the parameter counts that confound
them. The comparison is never voiced-and-gone.

## The problem

The biggest fix was the gate, not the teaching. A film whose thesis is *"they
never showed you the controlled experiment"* was itself showing numbers without
showing where they came from. Under this format's own rule — the film is held to
its rule first — that is disqualifying on its own, at 10/12 or at 12/12.

Worth naming as a pattern rather than an incident: the sourcing was strong exactly
where I had *built* a source into the scene (B06/B07 header, B08 card) and absent
everywhere I hadn't. Sourcing was a per-scene afterthought, not a contract. That's
what punch item 6 fixes.

## Do X next week

1. **[EDIT — done]** Citation on the encoder-stack exhibit (B02–B04) and the exec
   summary (B01), top-right on the header line, live for the whole beat.
2. **[EDIT — done]** Cite both halves of the B09 claim on the claim's own line —
   hypothesis and rebuttal — and label the model chips as pointers.
3. **[EDIT — done]** Relabel B01's cards as the three reusable questions. Converts
   an agenda into axes for one prop change.
4. **[EDIT — done]** Answer key on the B10 task.
5. **[RESHOOT/NEW SOURCE — open]** Show the actual report. One screenshot of
   Table 6 beside the redrawn chart moves sources-on-screen from *cited* to
   *shown*, which is the stronger standard for a grade-the-graders format.
6. **[STANDING TEMPLATE — open]** Make sourcing a contract, not a per-beat
   decision: a reusable source lower-third every claim beat takes as a required
   prop, so a beat cannot ship unsourced. Solved once instead of re-fixed per reel.
7. **[EDIT — open]** One narration line in B01 telling the viewer the three
   questions are theirs to reuse. Costs ~4s and closes the listening-vs-reading gap.

## What works

Keep the twist structure. Commit → both answers supported → both invalidated by
the same confound is a genuinely good pedagogical shape, and B07 does the hard
thing: it refuses the reading that would have made an easier, more shareable
video. Keep B10's falsification offer — inviting the audience to prove the film
wrong, and handing them the exact procedure, is the format's argument made
literal. And keep the restraint at B09: naming six models as pointers while
explicitly claiming nothing about their performance is the correct call, not a
hedge.
