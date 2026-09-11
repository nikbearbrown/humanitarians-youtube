# NARRATION — GATE P — "Test Before You Advance" · week-07 (Test-to-Advance Gate)

**Voice:** Kokoro `af_bella` ("Bella"). **Register:** Pragmatist / skeptical-explainer. **Narrator:** Satwik.
Framework-FIRST (PROOF): B01 lands **the gate in three moves — test the edge · prune + descend · hard
gates, soft diagnose** before any file, item, or learner. Falsifiability = **B05** (the learner who
passes both node quizzes but fails the *connection* — a node-only quiz would have advanced them). The
gate is a **running baseline built to be corrected**, not a finished, faculty-approved system. Target
≈ 3:10–3:25. Review on the animated slate before audio. GATE P.

Grounded **only** in `source/test_to_advance_gate.tex` / `.pdf` (and the Chapter-27 slice it reports).

| Beat | Act | Narration (spoken) |
|---|---|---|
| **B00** | hook / ASK | Hello, fellows. For six weeks our roadmap has ordered what to read — this section before that one. But ordering never checks the one thing that matters: that a learner actually *holds* a prerequisite before we move them on. So this week we add the test. The question — how do you check someone's ready to advance, without quizzing the entire chain behind the goal? |
| **B01** | the framework (three moves) | Here's the whole design in three moves. One: test the *edge*, not just the nodes — a connection item asks not "do you know A" and "do you know B," but "do you know how B is built on A." Two: go top-down and pruned — test only the direct prerequisites, skip what's already known, and descend deeper only when something fails. Three: hard edges *gate*; soft edges only *diagnose*. Test the edge, prune and descend, let hard block and soft report. That's the gate. |
| **B02** | the six-file model | It runs on six flat files — nothing hidden in a model. Four you author by hand: concepts, the testable sections; dependencies, the typed edges between them; items, the actual questions; and students, each with a target and what they already know. Two the engine writes: responses — every question asked and whether it was right — and gate result, the decision: advance, or send back, and exactly where. Every file is a spreadsheet a faculty reviewer can open and correct. |
| **B03** | move 1 · test the edge | Start with the edge. There are two kinds of question. A concept item asks "do you know this node" — which nanoparticle carrier is a lipid bilayer around an aqueous core? A connection item asks "do you understand how the target rests on this prerequisite" — why does tumour immunology constrain how you design that carrier? A learner can ace both endpoint quizzes and still fail the connection. Knowing two facts is not knowing that one is built on the other — and only the edge question catches it. |
| **B04** | move 2 · prune + descend | Now keep it cheap. The naive check tests the whole closure below the goal — a concept a hundred dependencies deep would mean a hundred questions. So: test only the *direct* prerequisites. Skip any the learner already knows or has placed. And descend into a prerequisite's own prerequisites *only* when it fails — because a pass, by the surmise relation, implies its whole subtree. The number of questions tracks the size of the gap near the goal, not the length of the chain. A hundred-deep chain can clear on a single check. |
| **B05** | the two learners (worked example · falsifiability) | Two learners, one goal: "Types of Nanoparticle Drug Delivery Systems." It has two hard prerequisites and one soft aid. Student one passes both prerequisite *nodes* — but fails the *connection*: why immunology drives carrier design. A node-only quiz would have advanced them. Because that edge is a hard gate, the gate *holds* and sends them back to exactly that section. Student two already had one prerequisite placed, so it's pruned — four questions, not five — passes the rest, and advances. Same goal: one held, one advanced, and a plain quiz would have missed the difference. |
| **B06** | the honest boundary | What's real, and what isn't. The engine runs — six files, deterministic offline grading, every number straight from the code. What's draft: the hard-versus-soft typing and the six seed items are auto-proposed, marked needs-review, none faculty-approved yet. And the question format is a choice. Multiple-choice first — an approved pool, graded against an answer key, free and reproducible. Open-ended written answers would need an LLM as a judge, and we don't trust that until it agrees with human graders on a gold set. A working baseline, honestly — not a finished, approved system. |
| **B07** | verdict | So — where it stands. The roadmap orders the reading; the gate proves a learner is ready before they move. It tests the link, not just the facts; it stays short by pruning and descending; and only hard edges can hold someone back. The typing and the items are drafts awaiting faculty. This is the standard prerequisite gate everyone starts with — built, running, and made to be corrected. |
| **B08** | your turn / handoff | Your turn. Take one target concept. List its *direct* hard prerequisites — no deeper yet. For each, write one connection item: why does the target depend on this? Mark every edge hard or soft. Then run it — skip what's known, test the direct prereqs, descend only where a learner fails. And watch the tests audit the graph: if nobody ever fails a "hard" edge's connection, it probably isn't hard. |
| **B09** | outro | Order tells you what to read next. A test tells you you're ready. This is Satwik for Humanitarians AI. |

## Register & claim notes for the reviewer (PROOF)

- **Framework-first:** B01 lands the three moves (test the edge / prune + descend / hard-gate soft-diagnose) before any file, item, or learner.
- **Falsifiability = B05:** STU001 passes both node quizzes yet fails connection `e1` (a node-only quiz advances them wrongly); the connection item is what verifies the dependency. Also: a "hard" edge nobody ever fails is probably not hard (B08) — the gate audits the graph.
- **Numbers spoken/shown:** six files (4 authored + 2 derived) · 22 concepts / 26 edges (11 hard / 15 soft) · threshold 0.67 · STU001 remediate→CH16-S05, 5 tested / 0 pruned · STU002 advance, 4 tested / 1 pruned · closure_size 3.
- **No-source-no-verdict:** engine numbers are real (from `run_assessment.py`); typing + items are **drafts (needs_review=yes)**, none faculty-approved; grading is deterministic offline; open-ended (LLM-as-judge) is a **separate proposal** vs a gold set. No learning-outcome claim.
- **Length:** ≈ 520 spoken words → est. **~3:10–3:25**. Confirm after audio.

---

Human sign-off required before Kokoro (Bella) audio spend. GATE P.
VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-09-11
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
