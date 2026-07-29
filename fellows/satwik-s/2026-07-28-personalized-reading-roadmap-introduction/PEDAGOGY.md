# PEDAGOGY — GATE P — Personalized, Project-Driven Reading Roadmaps for CaNCURE Trainees

AI-explainer reel on the `claude-hai` channel (Humanitarians AI · Bella · Pragmatist), built **only** from the paper draft (`sources/manuscript.pdf`). GATE P is a **quality** gate: a human reviews the narration on an animated slate and signs `VERDICT: PASS` **before** any audio is generated. Audio is free here — this gate protects the teaching, not the budget.

## The one idea (the reel must land exactly this)

> The textbook already contains the knowledge the trainee needs, but it's organized by scientific **topic**, not by the **sequence of problems** the trainee meets at the bench. The method **selects** relevant sections and **reorders** them around the trainee's project. This is a **reordering** problem — not search, retrieval, or summarization.

Every beat serves that sentence; nothing that doesn't is in the cut.

## Act structure (ai-explainer spine, HAI register)

- **B00 cold open** on `ClaudeComposerAsk` with RESULT lines (ASK→RESULT at B00) ✓ — COLD OPEN LAW
- **B01–B06 body** all ILLUSTRATE their concept on the humanitarians stage; the Claude UI never appears inside the body (ILLUSTRATE LAW) ✓; no two consecutive beats share a visual scheme ✓
- **B07 verdict** `ClaudeVerdictArtifact` (one-page recap) ✓
- **B08 handoff** `ClaudeComposerAsk` "Your turn." — an interesting, runnable prompt shown on screen; the shortened narration **summarizes and discusses** it rather than reading it verbatim (a deliberate relaxation of HANDOFF LAW's read-aloud clause — see Post-review corrections) ✓
- **B09 outro** `ClaudeTitleOutro` — title restate + `@HumanitariansAI` + Satwik sign-off (OUTRO LAW) ✓
- Spine order: cold open → body → verdict → HANDOFF → title-restate outro ✓

## Brief coverage (every required point has a home)

| Brief requirement | Beat(s) |
|---|---|
| 1. Problem: same topic-organized textbook to everyone; each student a different lab project | B00, B01 |
| 2. Framing: a reordering problem, not just search / retrieval / summarization | B02 |
| 3. Method: extract → tag metadata → build faculty-reviewable dependency graph → generate project-aligned roadmap | B03 (+ B04 graph) |
| 4. Output: weekly sequence — what to read / why it matters / which lab task it supports / what to read first | B05 |
| 5. Faculty approve **authoritative** prerequisite relationships (NOT all approved) | B04, B07 |
| 6. Future adaptive layer: faculty assessment + student progress may later update the roadmap | B06 |
| Central message (topic-order vs problem-order; select + reorder) | B02 (thesis beat), reinforced B00/B07 |

## Pragmatist-register requirement (HAI main event)

The HAI register **requires** a "when NOT to use it / where it fails" beat — this is not hedging, it's the diagnostic the audience needs. **B06** carries it: single textbook, advisor-heuristic timing (not learned), **rule-based/deterministic tagging** with uncertain metadata (and any future model-assisted suggestions) sent to faculty review, and **no learning-outcome data**. This beat simultaneously discharges three of the user's "do not claim" guardrails, so it is load-bearing and must not be cut for time.

**Irreducibly-Human tangent (0–1, used once):** folded into **B04** — *proposing* dependency edges is what the AI does well; deciding which prerequisite relationships are *authoritative* is the faculty's judgment and cannot be handed off. One bounded decision boundary, not a sermon.

## Claim discipline (the "do not claim" contract — see SOURCES.md ledger)

| Guardrail | How the cut honors it |
|---|---|
| No improved-learning-outcomes claim | Stated nowhere; B06 says "no outcome data yet," B07 closes "Learning outcomes: future work." |
| No "all prerequisites faculty-approved" | B04 always shows **model-proposed, under-review** edges beside the faculty-approved ones; B07 says "review is ongoing." |
| No real-time student-progress adaptation as shipped | B06's adaptive layer is greyed + stamped **DEFERRED · not implemented**. |
| No effect sizes / instructional-variable numbers | All Hattie *d*-values are `[TO DO: confirm]` in the draft → omitted entirely. |
| No unverified specifics (textbook title, pilot data, Jaccard, thresholds, embedding model) | All are draft `[TO DO]`s → omitted; B05's table rows are illustrative structure from the draft's own dependency example, not measured results. |

## Friction protected (what stays / what's cut)

- **Kept:** the strike-through reframe in B02 (content→ordering) and the ranker-can't-order beat — this is the paper's thesis and the reel's reason to exist; cutting it would make this a generic "AI summarizes your textbook" video, which the draft explicitly argues against.
- **Kept:** B06's limits beat in full — required by register and by the guardrails.
- **Cut:** the educational-theory apparatus (four instructional variables + effect sizes) — extraneous for a 2–3 min explainer and resting on unconfirmed d-values. Lives in the paper.
- **Cut:** implementation minutiae (parse_confidence, scoring weights, cycle detection, GraphML tooling) — method-section detail, not reel material.

## Duration

Estimated ≈ 3:06 at ~2.9 wps (post-correction); Bella-measured runtime expected ~2:48–3:02 — inside/at the top of the 2–3 min target. Duration is an **output**: it is confirmed only after the audio step. If the measured cut exceeds 3:00, trim B06 then B07 and **regenerate audio** — never hand-edit timing.

## Palette & voice decisions (logged)

- **Two-skin palette:** claude fidelity skin on UI beats (B00/B07/B08/B09); humanitarians token set on body beats (B01–B06) — per ai-explainer ASK→RESULT LAW. Not a retint of the Claude UI; the UI beats stay exact.
- **Voice:** Kokoro `af_bella` ("Bella") per HOW-TO.md / CLAUDE.md / brands/hai.md and the explicit user request. (`CLAUDE-BRAND.md`'s channel table lists `am_onyx` for `claude-hai`; treated as stale inherited text — flagged for the reviewer.)
- **Greeting:** `Hello, Satwik` — persona = the narrating first author (Satwik); matches the sign-off. Plain "Hello" (per reviewer) — well within the HAI "shortest-forms" budget, one serif line. B00's spoken opener is "Hello." to match the on-screen cue.
- **No IN-FOR-BEAR LAW:** that binds the Liam/Onyx cut only; this is the Bella/HAI cut, so no "in for Bear" line.

## Post-review corrections (2026-07-27, author-directed — logged for the reviewer)

Three accuracy corrections were applied after the first draft; full provenance in SOURCES.md ("Post-review corrections"):

1. **B05 pull-forward made conditional** — "Once faculty-approved prerequisites are available, required background sections can be pulled earlier automatically." The reel no longer implies prerequisites are *already* actively reordering sections. (est. 18s→21s.)
2. **B06 tagger corrected to rule-based/deterministic** — "The current tagging pass is rule-based and deterministic. Uncertain metadata and any future model-assisted suggestions remain subject to faculty review." Overrides the draft's §3.2 "LLM-assisted first pass." *Scope:* Stage-2 tagger only; **B04's Stage-3 edge inference still says "model proposes edges → faculty review"** — reviewer decides whether to extend the correction to B04. (est. 23s→25s.)
3. **B08 handoff shortened** — spoken line now summarizes + discusses the prompt (composer still shows the full paste-ready prompt); no longer read verbatim. (est. 24s→16s.)

Net estimated total 3:09 → **3:06**.

## Reviewer checklist (sign only when all true)

- [ ] The one idea lands and is not diluted.
- [ ] Every "do not claim" guardrail holds in narration AND on-screen text.
- [ ] B04 visibly shows prerequisites still under review (not all approved).
- [ ] B06's future layer reads as deferred, not shipped.
- [ ] **B06 tagging reads as rule-based/deterministic** (not LLM); B04↔B06 scope decision made (extend the rule-based correction to Stage-3 edge inference, or leave as drafted).
- [ ] **B05 pull-forward reads as conditional** on faculty-approved prerequisites (not "already happening").
- [ ] Greeting / sign-off wording approved (`Hello, Satwik` / "This is Satwik for Humanitarians AI.").
- [ ] Narration reviewed on the animated slate (not a page of text).

---

VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-07-27
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date. (Requested stop point: files created for review before any audio or render.)
