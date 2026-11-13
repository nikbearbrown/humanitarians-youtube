# NARRATION — GATE P — "Evaluate, Then Advance" · week-09 (Evaluation Pipeline)

**Voice:** Kokoro `af_bella` ("Bella"). **Register:** Pragmatist / skeptical-explainer. **Narrator:** Satwik.
Framework-FIRST (PROOF): B01 lands the rule — **evaluate, never assume · pass→prune, fail→descend · hard
gates, soft diagnose** — before any example. Falsifiability = **B06** (MCQ live, but item text at scale is
template stubs; open-ended off until a gold set; edges pending faculty). The gate the past weeks designed
and fed now **runs end to end.** Target ≈ 3:15–3:30. GATE P.

Grounded **only** in `sources/` (weekly_report_2026-09-27.md, evaluation_pipeline.md, evaluation_example.md,
the two gate_result CSVs, evaluate_gate.py, build_item_bank.py).

| Beat | Act | Narration (spoken) |
|---|---|---|
| **B00** | hook / ASK | Hello, fellows. Two weeks ago we designed the gate that tests a learner before advancing them. Last week we built the prerequisite graph it runs on. This week it runs — for real. The pipeline grades a learner, decides advance or send back, and names the exact gap. The question — how do you do that without wasting questions, and without assuming what a learner already knows? |
| **B01** | the framework (the rule) | The whole pipeline follows one rule, in three moves. One: evaluate, never assume — every prerequisite is tested; nothing is taken on trust. Two: a pass earns a prune, a fail makes you descend — pass a prerequisite and we skip everything beneath it; fail, and we dig into its own prerequisites to find how deep the gap runs. Three: hard prerequisites gate, soft ones only diagnose — and we test the connection, not just the concept. Evaluate, prune or descend, block only on the hard links. |
| **B02** | the loop | Here's the loop, top down from the learner's goal. For each hard prerequisite: grade the node. Pass? Then grade the connection — do they see how it supports the target? Both pass, it's satisfied, and we prune its whole subtree. If the node fails, we descend into its prerequisites and recurse. Soft prerequisites are tested as diagnostics only. At the end: advance if every hard prerequisite is satisfied, otherwise hold and remediate to the gap. The cost tracks the size of the gap near the goal, not the length of the chain. |
| **B03** | evaluate, don't assume | Here's what changed this week. The earlier demo pruned against a list of what the learner said they knew. Now nothing is assumed — every skip is earned by a passing answer. If a learner claims a topic but can't answer for it, we don't skip it; we test it. Trust is earned, question by question, not declared up front. |
| **B04** | item pools, one per learner | And the questions come from a pool. Each concept and each connection can carry several. The engine samples one item per learner, deterministically — so different learners get different questions from the same approved pool, and no two sit an identical test. We don't hand-write a test per student; we author one pool tied to the graph, and the engine assembles each learner's test from it. Multiple choice is graded offline against the key — free and reproducible; open-ended answers are wired in as a seam for later. |
| **B05** | worked example (two learners) | Two learners, same goal: immune checkpoint inhibitors. Student A knows the immunology — that passes, so we prune its whole subtree — but fails the basics of cancer treatment. We descend, find they do know what cancer is, so the gap is exactly the basics of cancer treatment, and we send them there: six questions, two subtrees pruned. Student B passes both hard branches, so both subtrees prune, and advances after five questions. Foundational cell biology was never tested for either — because the topics above it passed. |
| **B06** | at scale · the honest boundary | Then we ran it on the real graph: two hundred twenty concepts, two hundred forty-eight edges, a five-hundred-thirty-six-item pool. A learner heading for oncogene activation, weak on mutations, saw just five of those items — and the gap was pinned to mutations. What's honest about it: multiple-choice grading is done and running, but the item text at scale is still template stubs; real questions are next, drafted then faculty-approved. Open-ended grading is wired but off until we have a gold set. And the whole thing waits on faculty approving the edges. The engine is real; the questions and the sign-off are the work ahead. |
| **B07** | verdict | So — where it stands. The gate runs end to end: it grades, it prunes what a learner has earned, it descends only where they fail, and it names the exact gap — in five questions out of five hundred, not the whole chain. Multiple-choice is live; open-ended is a seam; the real questions and the faculty sign-off are next. |
| **B08** | your turn / handoff | Your turn. When you build an assessment on a prerequisite structure: test before you trust — earn every skip with a passing answer; prune on a pass, descend on a fail; and pull questions from one approved pool, not a hand-written test per learner. Measure the gap, not the chain. |
| **B09** | outro | Design the gate, build the graph, then let it run. This is Satwik for Humanitarians AI. |

## Register & claim notes for the reviewer (PROOF)

- **Framework-first:** B01 lands the rule (evaluate-first / pass-prune, fail-descend / hard-gate, soft-diagnose + connection) before any example.
- **Falsifiability = B06:** MCQ grading is real & running, but the scale item bank is **template stubs**; open-ended grading is a **seam** (off until a gold set); edges **pending faculty**.
- **The upgrade (B03):** earlier demo pruned against a declared knows-list → now every skip is earned by a passing answer (nothing assumed).
- **Numbers spoken/shown:** STU-A remediate→"basics of cancer treatment", 6 administered / 4 nodes / 2 pruned / closure 6; STU-B advance, 5 / 3 / 3 / 6; scale: 220 concepts / 248 edges / 536-item pool, STU-SIM saw 5 items, gap "Mutations", closure 8.
- **No-source-no-verdict:** every figure from `sources/`. MCQ live; item text stubs; open-ended off; faculty approval pending. No learning-outcome claim.
- **Length:** ≈ 560 spoken words → est. **~3:15–3:30**. Confirm after audio.

---

Human sign-off required before Kokoro (Bella) audio spend. GATE P.
VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-09-27
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
