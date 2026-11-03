# NARRATION — GATE P — "Read the Book, Draft the Graph" · week-08 (Prerequisite Graph)

**Voice:** Kokoro `af_bella` ("Bella"). **Register:** Pragmatist / skeptical-explainer. **Narrator:** Satwik.
Framework-FIRST (PROOF): B01 lands **the method in three moves — read it from the book · type each edge
hard/soft · ship it as a draft** before any count. Falsifiability = **B06** (reading order is a signal, not
proof; every edge a draft; 0 approved; RefD + LLM + faculty corroboration next). The graph the past weeks
assumed now exists — **as a reviewable draft, never a verdict.** Target ≈ 3:10–3:25. GATE P.

Grounded **only** in `sources/` (the two CSVs + the two reports + the README).

| Beat | Act | Narration (spoken) |
|---|---|---|
| **B00** | hook / ASK | Hello, fellows. Week after week our roadmap has ordered the reading and tested for readiness — but on a graph that was mostly empty. The dependencies were a promise: zero approved edges, pending faculty. This week we built it — the prerequisite graph for the entire textbook. The question — how do you draft a dependency graph experts can actually trust? |
| **B01** | the framework (three moves) | Here's the method in three moves. One: read it from the book — let the textbook's own structure, its chapter and section order, propose the edges; every edge points to a real unit inside the book. Two: type each edge hard or soft — hard means must-know-first, a strict order; soft means helpful but never blocking — and give each one a confidence. Three: ship it as a draft, not a verdict — every edge carries a rationale and an empty approval box, because faculty are the source of truth. Read it, type it, leave it open for review. |
| **B02** | what was built | Here's what that produced. One textbook — Cancer Biology and Therapeutics — thirty-eight chapters plus four appendices, forty-two units, over thirteen hundred sections. From it, two graphs. At the chapter level: a hundred and two edges — forty-one hard, sixty-one soft. At the topic level, section by section: two hundred forty-eight edges — ninety-six hard, a hundred fifty-two soft — across two hundred thirteen topics. Every edge, one reviewable row. |
| **B03** | move 1 · read it from the book | Move one: read it from the book. The signal is the text itself — the order chapters are taught in, and where each idea is first introduced. That's a known way to pull concept maps out of textbooks. So every edge references another unit by its stable ID — chapter twenty-seven, section one — never outside material, with a single exception: Module Zero, course foundations, the only external prerequisite, sitting at the very first chapter. And a validation step confirmed every edge points to a real section — no dangling links. |
| **B04** | move 2 · hard vs soft | Move two: type each edge. A hard prerequisite is one the target directly assumes — it must come first; these are the strict ordering constraints. A soft one is helpful or enriching, but the target reads fine without it — it only nudges the order, it never blocks. Each carries a confidence: hard edges around zero-point-seven to one, soft around zero-point-four to zero-point-six. That editable strong-versus-weak weight is exactly what a faculty reviewer adjusts — it's the published model for annotating a textbook's prerequisites. |
| **B05** | the worked chain | Watch it on the opening chain. Chapter one — normal cell biology — needs Module Zero: hard, confidence one. Chapter two — what cancer is — needs chapter one, hard, zero-point-nine: you can't define a disease of deregulation without the biology it deregulates. Chapter four — genomic instability — needs chapter one hard, because it builds straight on DNA and the cell cycle; and it needs chapter two only softly, zero-point-five — the cancer context motivates it but isn't required. Same book: hard and soft, each with a reason you can read. |
| **B06** | draft, not verdict (falsifiability) | And the honest part. Every one of these edges is a draft. The approve column is blank — not one is faculty-confirmed. Reading order is a strong signal, not proof: a book can introduce a topic before its true prerequisite, or imply a link that isn't real — so each row carries a rationale precisely so a reviewer can reject it. Next we corroborate: a deterministic reference-distance score from the book's own cross-references, then an optional language-model pass to surface what the manual draft missed. A grounded draft — faculty have the final say. |
| **B07** | verdict | So — where it stands. The dependency graph the past weeks assumed now exists: a hundred and two chapter edges, two hundred forty-eight topic edges, read from the book, typed hard or soft, each with a confidence and a reason. It's grounded in the prerequisite-relation literature, and it is entirely a draft — built for faculty to approve, edit, or reject. |
| **B08** | your turn / handoff | Your turn. To draft a dependency graph for any book: read the edges from its own structure — order and first-mention; type each one hard or soft and give it a confidence; write a one-line rationale; and leave the approval box empty for the expert. A prerequisite is a hypothesis until someone who knows the field signs off. |
| **B09** | outro | Week after week we pointed at an empty graph. Now it's drawn — in pencil, for faculty. This is Satwik for Humanitarians AI. |

## Register & claim notes for the reviewer (PROOF)

- **Framework-first:** B01 lands the three moves (read from book / type hard-soft / ship as draft) before any count.
- **Falsifiability = B06:** reading order is a signal not proof; every edge a draft (`approve` blank, 0 confirmed); rationale exists so reviewers can reject; RefD (deterministic) + LLM pass + faculty next. Intro/Summary/Conclusion sections carry no prerequisites (a deliberate null).
- **Numbers spoken/shown:** 42 units (38 chapters + 4 appendices) · 1,340 sections · 213 topics · chapter graph 102 edges (41 hard / 61 soft) · topic graph 248 edges (96 hard / 152 soft) · confidence hard 0.7–1.0 / soft 0.4–0.6 · MOD0 the only external prereq · worked chain CH01←MOD0 (hard 1.0), CH02←CH01 (hard 0.9), CH04←CH01 (hard 0.9) & CH04←CH02 (soft 0.5).
- **No-source-no-verdict:** every edge/number from `sources/`; drafts marked draft (none faculty-approved); method grounded in Wang 2016 (concept maps from textbooks), RefD/Liang 2015, PREAP/PRAT (Alzetta & Torre 2025), Le & Abel 2025, ACM CSUR survey 2025. No claim that any edge is authoritative.
- **Length:** ≈ 530 spoken words → est. **~3:15–3:30**. Confirm after audio.

---

Human sign-off required before Kokoro (Bella) audio spend. GATE P.
VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-09-20
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
