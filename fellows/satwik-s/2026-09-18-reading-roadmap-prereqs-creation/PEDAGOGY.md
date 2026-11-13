# PEDAGOGY — GATE P (+ PROOF) — "Read the Book, Draft the Graph" · week-08 (Prerequisite Graph)

Film on `claude-hai` (Bella · Pragmatist / skeptical-explainer), built only from `sources/`. GATE P: a human
signs `VERDICT: PASS` before any audio. Carries the **PROOF** rubric + production gate (framework-first; no
source, no verdict). The dependency-graph-construction film: **how to draft a graph experts can trust — read
it from the book, type each edge hard/soft, ship it as a draft.**

## The one idea

> A dependency graph can be **drafted from the book's own structure** and made **faculty-reviewable** by
> typing every edge **hard** (strict order) or **soft** (helpful, never blocks) with a **confidence** + a
> **rationale**, and left as a **draft** (`approve` blank) — because reading order is a signal, not proof.

## Act structure (framework-first per PROOF)

- **B00 hook / ASK** (claude) — the graph was 0 approved edges; now built for the whole book — how to draft one experts trust?
- **B01 THE FRAMEWORK** (humanitarians) — the **three moves** (read from book / type hard-soft / ship as draft), before any count.
- **B02–B06 the worked build** — what was built (book + 2 graphs) · **move 1 read from the book** · **move 2 hard vs soft** · the worked chain (MOD0→CH01→CH02→CH04) · **draft, not verdict (falsifiability)**.
- **B07 verdict** (claude) · **B08 handoff/CTA** (claude, draft one graph) · **B09 outro**.

## PROOF teaching rubric — self-score (target ≥ 8/12; ship bar)

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | B01 shows the three moves as a structure before any count | 2 |
| Reusable rubric | the three moves apply to any textbook; CTA hands the template | 2 |
| Worked example | B05 walks the real opening chain, hard + soft, with confidences + reasons | 2 |
| Falsifiability / edge | B06: reading order is a signal not proof; every edge a draft (0 approved); rationale-to-reject; Intro/Summary carry none | 2 |
| Active task | B08: read from structure → type hard/soft + confidence → rationale → leave approve blank | 2 |
| Friction | "isn't chapter order already the reading order?" resolved via hard/soft + cross-chapter deps | 2 |
| **Total** | | **12 / 12 (target design)** |

## PROOF production gate (binary)

- **Legible at assertion:** real counts (B02), hard/soft split (B04), the chain edges + confidences (B05), the draft facts (B06), held ≥2s.
- **Framework-first:** B01 lands the three moves before any count.
- **Side-by-side:** B04 hard beside soft; B05 the chain shows hard (solid) vs soft (dashed) together.
- **Caveats shown, not just voiced:** B06 (approve=blank, 0 approved, order≠proof, corroboration next).
- **Audio present:** master audio volumedetect ≈ −20 dB (not −91). Verified at QC.

## Claim discipline (no source, no verdict — see SOURCES.md)

| Guardrail | How honored |
|---|---|
| Counts are real | B02/B07 (102 = 41/61; 248 = 96/152; 42 units, 213 topics) |
| Every edge is a draft | B06 (approve blank, 0 approved), B07 (a draft for faculty) |
| Order is a signal, not proof | B06 (rationale-to-reject; RefD + LLM + faculty next) |
| MOD0 the only external prereq | B03, B05 |
| Method grounded, nothing invented | B03 (Wang 2016), B04 (PREAP/PRAT), B07 (RefD, LLM prereq prediction) |
| No authoritative / learning claim | never asserted; the graph is a reviewable draft |

## Series / connection

Weeks 00–07 built and interrogated the roadmap on a graph that was a promise. **Week-08 fills the graph** —
the artifact the test-to-advance gate (week-07) and the roadmap ordering consume. Reuses framework-first +
no-source-no-verdict discipline.

## Duration & deliverables

≈ 530 spoken words → est. **~3:15–3:30**. Deliverables: **4K 16:9** master (primary). A **≤1-min 4K 9:16
Short** (B01 framework + B05 the chain + B09) may follow via portrait `916` components. Run
audio/render/compile under `PYTHONUTF8=1`; use the venv python for Kokoro; **render with temp on D:**
(`TMPDIR/TEMP/TMP=d:/_remotion_tmp`); **assemble audio with the concat FILTER** (the demuxer yields silent audio here).

## Palette & voice

- Two-skin (claude UI / humanitarians body). **TEAL = hard / ordering, GOLD = the key insight / hard
  emphasis, SAGE = soft / non-blocking, SLATE = the book / substrate, CRIMSON = the draft / falsifiability.**
- Voice Kokoro `af_bella`. Greeting `Hello, fellows`. Sign-off "This is Satwik for Humanitarians AI."

## Reviewer checklist (sign only when all true)

- [x] The one idea lands: draft a graph from the book, typed hard/soft, as a reviewable draft.
- [x] B01 lands the three moves **before** any count.
- [x] B04 shows hard vs soft with confidences; B05 the real chain with reasons.
- [x] B06 shows every edge is a draft (0 approved), order≠proof, corroboration next.
- [x] Every count/edge traces to `sources/`; no authoritative or learning-outcome claim.
- [ ] **Master audio present (volumedetect ≈ −20 dB, not −91).** (verify at QC)
- [x] Greeting / sign-off approved; narration reviewed on the animated slate.

---

VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-09-20
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
