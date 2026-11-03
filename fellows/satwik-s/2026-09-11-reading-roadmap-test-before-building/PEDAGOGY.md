# PEDAGOGY — GATE P (+ PROOF) — "Test Before You Advance" · week-07 (Test-to-Advance Gate)

Film on `claude-hai` (Bella · Pragmatist / skeptical-explainer), built only from
`source/test_to_advance_gate.tex`. GATE P: a human signs `VERDICT: PASS` before any audio. Carries the
**PROOF** teaching rubric + production gate (framework-first; no source, no verdict). The assessment-layer
film: **the standard prerequisite gate, made honest and cheap — in three moves.**

## The one idea

> Ordering isn't readiness. A **test-to-advance gate** checks a learner *holds* a prerequisite before
> advancing — and three moves make it honest + cheap: **test the edge** (a connection item, not just two
> nodes), **prune + descend** (direct prereqs, skip known, deeper only on failure), **hard gates / soft
> diagnose.** The connection item is the tell a node-only quiz misses.

## Act structure (framework-first per PROOF)

- **B00 hook / ASK** (claude) — ordering never checks readiness; test before advancing, without quizzing the whole chain.
- **B01 THE FRAMEWORK** (humanitarians) — the **three moves**, before any file/item/learner.
- **B02–B06 the worked build** — the six-file model · **move 1 test the edge** · **move 2 prune + descend** · **the two learners (falsifiability)** · **the honest boundary (drafts / MC-first)**.
- **B07 verdict** (claude) · **B08 handoff/CTA** (claude, build one gate) · **B09 outro**.

## PROOF teaching rubric — self-score (target ≥ 8/12; ship bar)

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | B01 shows the three moves as a structure before any file/item/learner | 2 |
| Reusable rubric | the three moves apply to any prerequisite-gated curriculum; CTA hands the template | 2 |
| Worked example | B05 walks two learners through the gate — one held, one advanced, with counts | 2 |
| Falsifiability / edge | B05: STU001 passes both nodes yet fails the connection (a node-only quiz advances them); B08: a "hard" edge nobody fails isn't hard | 2 |
| Active task | B08: one target → direct hard prereqs → one connection item each → mark hard/soft → run | 2 |
| Friction | "passed A and B — why isn't that ready?" resolved via the connection item; "why not test the whole chain?" via prune+descend | 2 |
| **Total** | | **12 / 12 (target design)** |

## PROOF production gate (binary)

- **Legible at assertion:** real figures readable, held ≥2s (the six files; the two item types; the two learners' rows + counts).
- **Framework-first:** B01 lands the three moves before any detail.
- **Side-by-side:** B05 STU001 (hold) beside STU002 (advance); failed **connection** + **pruned** node both visible.
- **Caveats shown, not just voiced:** B06 real-vs-draft split; "needs_review", "none faculty-approved"; MC-first vs open-ended.
- **Audio present:** master audio volumedetect ≈ −20 dB (not −91). Verified at QC.

## Claim discipline (no source, no verdict — see SOURCES.md)

| Guardrail | How honored |
|---|---|
| Engine numbers are real | B02/B04/B05 (six files; counts; 22/26, 11/15, 0.67) — all from `run_assessment.py` |
| Typing + items are drafts | B06 (needs_review; none faculty-approved), B07 (drafts awaiting faculty) |
| Grading deterministic offline | B06 (answer-key matching); open-ended = phase-two vs gold set |
| No learning-outcome claim | never asserted; the gate proves *readiness*, not learning gains |
| Worked-example grading simulated | control flow/pruning/decisions real; production = answer-key (SOURCES caveat) |

## Series / connection

Weeks 00–05 built the *system*; week-06 justified the *idea* (OBER outcomes+items). **Week-07 is the
baseline Prof. Nik asked for** — sequence + test-before-advance — and lands OBER's "outcomes + assessment
items" as a running artifact. Reuses framework-first + no-source-no-verdict discipline.

## Duration & deliverables

≈ 520 spoken words → est. **~3:10–3:25**. Deliverables: **4K 16:9** master (primary). A **≤1-min 4K
9:16 Short** (B01 framework + B05 two-learners + B09) may follow via the `916` portrait components. Run
audio/render/compile under `PYTHONUTF8=1`; use the venv python for Kokoro; **assemble audio with the
concat FILTER** (the demuxer yields silent audio here).

## Palette & voice

- Two-skin (claude UI / humanitarians body). **TEAL = advance/pass, CRIMSON = gate-hold/remediate, GOLD =
  the connection-item insight, SAGE = soft/diagnostic, SLATE = the six-file substrate.**
- Voice Kokoro `af_bella`. Greeting `Hello, fellows`. Sign-off "This is Satwik for Humanitarians AI."

## Reviewer checklist (sign only when all true)

- [x] The one idea lands: ordering isn't readiness; the gate tests it in three moves.
- [x] B01 lands the three moves **before** any file/item/learner.
- [x] B05 shows STU001 (hold, connection fail) beside STU002 (advance, pruned), with counts.
- [x] B06 shows real-vs-draft; "needs_review / none faculty-approved"; MC-first vs open-ended.
- [x] Every number traces to `source/test_to_advance_gate.tex`; no learning-outcome claim.
- [ ] **Master audio present (volumedetect ≈ −20 dB, not −91).** (verify at QC)
- [x] Greeting / sign-off approved; narration reviewed on the animated slate.

---

VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-09-11
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
