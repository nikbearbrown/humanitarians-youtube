# PEDAGOGY — GATE P (+ PROOF) — "Which One Is Right? Scoring Taggers Against a Gold Set" · week-04

Film 5 on `claude-hai` (Bella · Pragmatist / skeptical-explainer), built only from `sources/week4_*.md`
+ `gold_scoring.md`. GATE P: a human signs `VERDICT: PASS` before any audio. This film carries the
**PROOF** teaching rubric + production gate (framework-first; no source, no verdict). It is the graded
verdict week-03's ceiling pointed to (n=4 → n=102 → the gold set), kept **provisional (one grader)**.

## The one idea

> Agreement proves the tagger choice **matters**; only a **blind gold set** says which is **correct** —
> scored on **precision and recall**, not just F1, and read with **where each tag came from**.
> Provisional result: the deterministic dictionary wins outright (**F1 0.89 vs 0.35**, P and R), the
> hybrid guess is **rejected**, and *why* is legible (rule-only tags 85% correct vs model-only 12%) —
> holding only until a second grader reconciles.

## Act structure (framework-first per PROOF)

- **B00 hook / ASK** (claude) — recap wk-03's ceiling (an ablation can't say which is correct → ground truth) → this week the gold set is graded.
- **B01 THE FRAMEWORK** (humanitarians) — the **4 steps** (blind gold set · precision & recall · read the split · trace provenance), shown **before any result**.
- **B02–B06 the worked example** — one step per beat, each with its real table:
  the blind set (20 · 333; 191/142) · the F1 verdict (0.89 vs 0.35) · **read the split — hybrid REJECTED (falsifiability)** · trace provenance (85% vs 12%) · **the catch — one grader → provisional (honesty floor)**.
- **B07 verdict** (claude) · **B08 handoff/CTA** (claude, the blind-gold-set template) · **B09 outro**.

## PROOF teaching rubric — self-score (target ≥ 8/12; ship bar)

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | B01 shows the 4-step scoring method as a structure before any result | 2 |
| Reusable rubric | the 4 steps apply to any "which option is more correct?" choice; CTA hands the template | 2 |
| Worked example | the tagging gold set walked live, one step per beat, with real tables | 2 |
| Falsifiability / edge | B04: the hybrid / "model = recall" hypothesis is stated, then **rejected** by ground truth (model loses recall too) | 2 |
| Active task | B08: build a blind gold set, score P & R, read the split, trace provenance, report grader count | 2 |
| Friction | "F1 0.89 vs 0.35 — done, right?" resolved via one-grader-provisional + the split + provenance (why it wins) | 2 |
| **Total** | | **12 / 12 (target design)** |

## PROOF production gate (binary — can veto publish)

- **Legible at assertion:** real tables readable, held ≥2s, at the claim (VISUAL-PLAN).
- **Framework-first:** B01 lands the 4 steps before any result.
- **Precision & recall with F1:** B03 (F1 + overall) and B04 (the P/R split) — never F1 alone.
- **Side-by-side at comparison:** rule vs model together in B03/B04/B05.
- **Provisional + pending:** PROVISIONAL (one grader) stamp wherever F1 appears; ordering dormant (0 edges), one sign-off away — never a result.
- Verified at QC on the compiled master (see `_qc/REPORT.md`).

## Claim discipline (no source, no verdict — see SOURCES.md)

| Guardrail | How honored |
|---|---|
| Provisional verdict | PROVISIONAL (one grader) on B02/B03/B07; "second grading + faculty next" spoken (B06/B07) |
| No "hybrid wins" | B04 names the hybrid a **hypothesis** and stamps it **rejected**; B07 restates "didn't survive ground truth" |
| Precision & recall, not F1 alone | B03 shows F1 + overall; B04 shows the P/R split as the teach |
| Don't conflate the two 333 splits | B02 uses 191 literal / 142 inferred; 184 kept / 149 rejected stays out of the spoken line |
| Ordering | **dormant** (0 edges); 26 Ch-27 links *proposed*, one faculty sign-off (B06/B07) |
| Model named exactly | `qwen2.5-coder:7b` (temp 0, self-hosted NEU cluster T4) |
| No efficacy/learning claim | none; scope is correctness scoring + provenance only |

## Series (film 5 vs film 4 — PROOF /series)

Closes the arc week-03 opened: wk-02 ablation on n=4 → wk-03 full book (n=102) + the **ceiling** ("an
ablation can't say which is correct; the gold set will") → **wk-04 the graded verdict** (rule F1 0.89
vs 0.35). The recap ablation numbers (74%, ~1,600×, materials 0.919) stay in B00/verdict only; the body
**advances** to the gold set. Standing honesty pattern applied from the first result beat: state the
provisional/one-grader limit, and mark ordering dormant.

## Duration

≈ 570 spoken words → est. **~3:40–3:55** at Bella's measured pace. Duration is an output, confirmed
after audio. Run audio/render/compile under `PYTHONUTF8=1` (Windows — see memory gotcha); use the
toolkit venv python for Kokoro. If ≤3:20 wanted, trim B03/B07 and tighten B01 before sign-off.

## Palette & voice

- Two-skin (claude UI beats / humanitarians body). TEAL-led; **CRIMSON reserved for B04 (hybrid rejected) and B05 (model-only 12%)** + the PROVISIONAL stamps; GOLD for the gold set (B02).
- Voice Kokoro `af_bella`. Greeting `Hello, fellows` (consistent with wk-01–04). Sign-off "This is Satwik for Humanitarians AI."

## Reviewer checklist (sign only when all true)

- [ ] The one idea lands: agreement says the choice matters; a blind gold set says which is correct — provisionally, the dictionary.
- [ ] B01 lands the 4-step method **before** any result.
- [ ] B04 shows the hybrid hypothesis **rejected** (model loses recall too); no hybrid conclusion anywhere.
- [ ] Every gold-set beat carries the **PROVISIONAL (one grader)** mark; "second grader + faculty next" is stated.
- [ ] Precision & recall shown **with** F1 (B03/B04); the two 333 splits not conflated; ordering shown dormant; model named exactly.
- [ ] Greeting / sign-off approved (`Hello, fellows` / "This is Satwik for Humanitarians AI.").
- [ ] Narration reviewed on the animated slate.

---

VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-08-24
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
