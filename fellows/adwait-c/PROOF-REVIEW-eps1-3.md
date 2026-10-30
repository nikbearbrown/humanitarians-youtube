# PROOF Review — *Agentic AI: From the Loop to MCP*, films 1–3

Reviewed 2026-08-13 by the build agent, self-applying PROOF to work it produced. Inputs: the
rendered frames read during visual QC (`_qc/frames/`, plus each `qc-sheet.png`) and the narration
in each `beat_sheet.json`.

**Scope caveat, stated up front:** I read every beat of each film in the contact sheet, and read
**full-resolution frames** for Ep1 B01/B02/B03/B05/B08/B09, Ep2 B02/B03/B06/B07/B08, and Ep3
B02/B03/B05/B07/B08. I did **not** read full-res frames for the bookend beats (B00, BHTF, BOUT) or
the verdict cards in any film. Findings below are scoped to what the frames actually support;
where a judgement rests on narration rather than a frame, it says so.

---

## Verdicts

| Film | Teaching | Production gate | Verdict |
|---|---|---|---|
| **Ep1 — What Makes an AI "Agentic"** | **7/12** | **FAIL** (side-by-side) | **unlisted-until-fixed** |
| **Ep2 — The Agent Loop** | **11/12** | PASS | **clear-for-public** |
| **Ep3 — Tools: Giving a Model Hands** | **11/12** | PASS | **clear-for-public** |

One line each:

- **Ep1** attempts to define an agent but delivers a well-produced assertion, because its central
  comparison is narrated across two beats that never share a frame, and its rubric is stated at B09
  without ever being run on a case.
- **Ep2** attempts to locate the load-bearing part of the loop and does exactly that, because the
  claim is executed on screen rather than asserted.
- **Ep3** attempts to show that a tool is a contract and does exactly that, because it runs a
  controlled A/B with the control visible in frame.

---

## Rubric

| Criterion | Ep1 | Ep2 | Ep3 |
|---|---|---|---|
| **Explicit framework** (shown before examples) | **1** — the loop framework (B05) arrives *after* the flight-booking example (B03). Order is example → framework, which PROOF specifically inverts. | **2** — B02 lays out thought/action/observation before B03 shows a real pass through it. | **2** — B02 names the three things that cross the wire before B03 prints them. |
| **Reusable rubric** (applies to a new case) | **2** — B09's three conditions (task needs doing / undo is cheap / result is checkable) are genuinely reusable. | **2** — B05's three properties of an observation. | **2** — B06's three questions a description must answer. |
| **Worked example** (reasoning walked live) | **1** — the flight example demonstrates a chatbot failing; no case is ever walked through the three-condition rubric the film hands over. | **2** — B03 walks one real call through the framework, recorded two ways; B07 runs it to the budget. | **2** — B07 walks `read_file` through all three questions, twice. |
| **Falsifiability / edge case** | **0** — no counterexample, no ambiguous case. | **1** — B08's four death modes are a taxonomy, not a stress test of the framework. | **1** — the B06 caption gestures at "two tools that both sound right" but never shows that case. |
| **Active task** | **2** — BHTF hands over a real scaffold with a named output. | **2** — "write the three worst observations a lazy implementation would return." | **2** — "tell me where you would genuinely be unsure." |
| **Friction** | **1** — the prompt asks the model to argue against itself, but the film itself resolves every tension it raises. | **2** — the viewer is asked to author the bad versions deliberately. | **2** — the "unsure" list forces the viewer to confront their own vague sentences. |
| **Total** | **7/12** | **11/12** | **11/12** |

---

## Production gate

**Evidence legible at the moment of assertion — PASS (all three).** Verified against full-res
frames during QC. Two defects that would have failed this gate were caught and fixed before master:
Ep1 B03 rendered a disclaimer as a numbered plan step, and Ep2 B03 rendered a terminal trace as a
numbered list. Both were factual misrepresentations, not cosmetic issues.

**Sources on screen, not just voiced — PASS (all three).** These films make no external factual
claims; every substantive claim is carried by a visible artifact from the shipped `.py` file. Ep3
is the strongest case — `function bodies identical: True` is the program asserting the film's own
control on screen.

**Side-by-side at the moment of comparison — Ep1 FAIL, Ep2/Ep3 PASS.**

- **Ep1 FAILS.** The film's entire comparison is *chatbot vs agent*. B02 shows the model's one-turn
  contract; B05 shows the loop. They are 35 seconds apart and never share a frame. The viewer is
  told the difference and never shown it in one image. This is the gate's exact target, and it
  vetoes publish regardless of the 7/12.
- **Ep2 PASSES** — B03 holds `ok` and `ERROR FileNotFoundError: sales.csv` in one frame, ~13s.
- **Ep3 PASSES** — B07 holds the 13-char and 292-char contracts in one frame with the identical-
  bodies control beneath, ~15s.

---

## The problem

**Ep1, beat B03 → B05.** The film's thesis is a comparison, and the comparison is never composed.
Everything downstream inherits it: with no single frame contrasting the two, there is nothing to run
the B09 rubric *against*, which is why the worked-example and falsifiability scores collapse. Ep1 is
not a weaker production than Ep2 or Ep3 — it is the same production around a missing beat.

Worth naming plainly: Ep1 is the film where I let the `ai-explainer` chassis do the thinking. The
chassis makes the production gate easy (real output, legible mono cards) and does nothing at all for
the teaching rubric. Eps 2 and 3 score higher because the argument happened to demand executable
evidence, not because I applied a standard.

---

## Do this next

1. **[EDIT] Add one side-by-side beat to Ep1, between B03 and B04.** `ClaudeScienceLayerStack` or a
   two-column `ClaudeWindow`: left, *one turn* — prompt / generate / return / stop. Right, *the
   loop* — think / act / observe / repeat. Same frame, held ≥2s. Fixes the gate veto and lifts
   "explicit framework" to 2. One beat of new narration (~12s), one render, one recompile.
2. **[EDIT] Move Ep1's framework ahead of its example.** Reorder so the loop is shown before the
   flight-booking artifact, per the build arc (hook → framework → worked example). Audio is per-beat,
   so this is a reorder plus two narration patches, not a re-record.
3. **[EDIT] Run the B09 rubric on one case, on screen, in Ep1.** Take the flight booking and score it
   against the three conditions. Lifts "worked example" 1 → 2. ~15s.
4. **[RESHOOT/NEW SOURCE] Add a falsifiability beat to Ep4 onward, and retrofit one into Ep1.** The
   standing gap across all three films. For Ep1: a task that satisfies two of the three conditions
   but not the third — an agent that can act and undo cheaply but whose result you cannot verify.
   That is the case the rubric must survive.
5. **[EDIT — standing template] Build a side-by-side comparison scene once.** This is the second
   time a comparison problem has surfaced (Ep1's gate failure; Ep3's B06 caption gesturing at a
   case it never shows). Per PROOF, a recurring production fix becomes a template, not a per-film
   patch. A parameterised two-column Remotion scene in `runtime/remotion/src/scenes/` pays for
   itself by Ep5.

Items 1–3 are roughly one build cycle. They take Ep1 to ~11/12 with a passing gate.

---

## What works

Keep these — they are why Eps 2 and 3 clear the bar, and they should be non-negotiable for Eps 4–10:

- **Executable evidence.** Every code beat shows real file contents; several beats show real printed
  output. Ep2's eight-pass log and Ep3's identical-bodies control are the strongest moments in the
  series precisely because the program makes the claim, not the narrator.
- **The scaffolded handoff.** All three CTAs hand over a runnable prompt with a named deliverable
  and a stated thing to look for. None is "ask Claude."
- **The honesty discipline in the paperwork.** Ep3's FACTCHECK caught a false claim of mine before
  audio and fixed it *in the code* rather than softening the script. That is the PROOF instinct
  already operating — it just needs pointing at the teaching rubric as well as the facts.
- **Generating code props with `inspect.getsource()`.** Removes transcription drift as a category.
