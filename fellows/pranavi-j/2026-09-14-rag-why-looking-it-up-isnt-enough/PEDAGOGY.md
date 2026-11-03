# PEDAGOGY — self-assessment against PROOF.md

**Film:** "RAG: Why 'Looking It Up' Doesn't Guarantee It's True" — Sai Pranavi J.
**Genre:** framework-first STEM/AI explainer (same register as the closest sibling reel, `2026-08-17-why-ai-generated-code-still-needs-a-human`, which scored 11/12 against this same rubric — cited here for calibration, not as a target to match)
**Reviewed against:** `PROOF.md` (copied into this folder), self-scored by the builder, not an external reviewer session — flagged here as `[ASSUMPTION: self-scored]` per PROOF's own `/silent` convention.

## Gate P

Fellow reviewed and approved the beat-by-beat outline 2026-09-17 (see `BEAT-SHEET.md`'s own Gate P record). `VERDICT: PASS`.

## The rubric — does this explainer actually teach?

| Criterion | Score /2 | Why |
|---|---|---|
| **Explicit framework** | 2 | B03 shows all 3 rubric questions (Relevant / Current / Grounded) together as a card, skeleton-first (all 3 badges+labels land before any one question is explained), fully before B04's worked example. Not narrated after the fact. |
| **Reusable rubric** | 2 | The three questions ("is the source actually relevant / actually current / did the model actually use it") are stated as general questions to ask of *any* RAG answer, not tied to the support-bot scenario's specifics — a viewer can carry them to a different system. |
| **Worked example** | 2 | B04 walks the rubric live against the support-bot case: Relevant — yes; Current — no, 8 months stale; Grounded — doesn't matter, because the source itself is wrong. This is the reasoning *step*, not just a labeled conclusion — the "doesn't matter" line is the film explicitly refusing to let a technically-grounded answer pass. |
| **Falsifiability / edge case** | 2 | B05 is a genuine stress test, not a strawman: same mechanism (retrieval), same rubric implicitly in play, but a *different source quality* — an internal launch doc that actually is current, relevant, and used. This directly tests the film's own framing ("retrieval is treated as the fix") against a case where it legitimately is, avoiding the one-per-example tell PROOF specifically warns about (both B04 and B05 exercise the full rubric conceptually, not one axis each). |
| **Active task** | 2 | B06's task is concrete and scaffolded: take one real recent RAG answer, ask the three questions, and specifically try to point to the exact sentence the answer came from. Not "ask Claude" — it names the exact check and the exact failure signal ("if you can't point to that sentence, you don't know it's grounded, you're just hoping"). |
| **Friction** | 1 | The film mostly *narrates* the resolution of its own tension (B04's "doesn't matter" line resolves the ambiguity for the viewer rather than making them sit with it) rather than leaving a genuine unresolved moment inside the video itself. The real friction — actually auditing a RAG system and discovering you can't point to the sentence — is deferred to the B06 take-home task, which is a legitimate design (this is a 2:19 explainer, not an interactive exercise) but is friction *assigned*, not friction *experienced* during the runtime. |

**Total: 11/12.**

## The production gate (binary)

- **Evidence legible at the moment of assertion** — PASS. B04 shows the retrieved document's stamped date ("Last updated: Jan 12, 2026") and the "TODAY: September 14, 2026" banner simultaneously, both held well past 2s (confirmed by direct frame extraction from the true clean master, both landscape and vertical). B05's "NO RETRIEVAL" and "WITH RETRIEVAL" attempts are both fully legible together, held ~10-16s each with both panels visible throughout, not a quick cut.
- **Sources on screen, not just voiced** — PASS, with a caveat worth stating plainly: this film's central framing claim ("RAG is widely treated as the fix for LLM hallucination") is presented as general/uncited — `FACTCHECK.md` explicitly resolved this by skipping an external citation rather than inventing one PROOF would reject anyway. What *is* on screen and sourced-to-itself is every claim the film actually makes about its two worked scenarios (the stale-doc date, the launch-doc date) — both are visible artifacts, not asserted facts about the real world requiring external sourcing. The film does not claim RAG-hallucination-treatment is an empirical finding with a citation; it states it as the premise the video exists to complicate, which is consistent with PROOF's "no source, no verdict" rule applied to *claims of fact*, not framing statements.
- **Side-by-side at the moment of comparison** — PASS. B04's document+answer and B05's no-retrieval/with-retrieval attempts are both on screen together (top/bottom stack in the vertical cut, since portrait width can't hold true left/right columns; side-by-side-equivalent simultaneity preserved) for well over the 2s floor, confirmed by direct frame extraction in both aspect ratios, not inferred from the automated GATE V number alone.

**Production gate: PASS.**

## Ship rule

Teaching 11/12 (≥8 floor) AND production gate PASS AND the video holds itself to its own "check before you trust it" standard (it explicitly declines to call the support-bot's technically-grounded-but-stale answer good, and explicitly scaffolds the viewer's own audit rather than asserting "trust RAG" or "never trust RAG"). Self-assessed verdict: **clear-for-public** on the teaching/production standard — this is a pedagogical self-score, not a publishing authorization; see `README.md`'s Production state (`NOT AUTHORIZED`) for the actual gate that governs release.

## Honest gaps

- The Friction score (1/2) is the honest weak point — noted above, not smoothed over.
- This self-assessment was done by the same builder who made the film, not an independent PROOF review session with pasted frames. The frame-legibility claims above were verified by this builder's own direct `ffmpeg` frame extraction from the true clean masters (both aspect ratios), the same discipline PROOF itself requires ("if you can't see it, ask for the frame — don't infer a pass or a fail"), but it is still a self-review, not adversarial.
