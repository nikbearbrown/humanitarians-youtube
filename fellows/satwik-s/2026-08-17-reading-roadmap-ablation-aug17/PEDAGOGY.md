# PEDAGOGY — GATE P (+ PROOF) — "What an Ablation Can (and Can't) Decide" · Full-Book Tagging

Film 4 on `claude-hai` (Bella · Pragmatist / skeptical-explainer), built only from `sources/week3_*.md`.
GATE P: a human signs `VERDICT: PASS` before any audio. This film carries the **PROOF** teaching rubric
+ production gate (framework-first; no source, no verdict). It is the promised full-book re-run of
week-02 (n=4 → n=102), and it adds a downstream number and the honest ceiling of the method.

## The one idea

> An ablation can prove a component choice is **reproducible**, that it **matters** (measured
> *downstream*), and **where** two options differ — but it **cannot** tell you which is *correct*; that
> needs **ground truth**. Full book: the dictionary wins reproducibility, speed, and cost and agrees on
> the load-bearing field — yet swapping taggers changes **~74%** of the reading list, so the quality
> winner stays **open until the gold set is graded**.

## Act structure (framework-first per PROOF)

- **B00 hook / ASK** (claude) — recap wk-02 (strongest number on 4 sections) → this week's full 1,340-section book + the sharper question.
- **B01 THE FRAMEWORK** (humanitarians) — the **4 questions**, shown **before any result**; Q1–3 marked answerable, **Q4 marked NOT (the ceiling)**.
- **B02–B06 the worked example** — one question per beat, each with its real table:
  Q1 reproducible (1.000 vs ~0.99; 12 s vs 5 h 27 min, ~1,600×) · Q2 does-it-matter (**downstream 74%**) · Q3 where-differ (per-field Jaccard **with n**; n=4 → n=102) · **Q4 the ceiling — can't say which is correct (falsifiability)** · the gold set + prerequisite review as the human steps (in-progress).
- **B07 verdict** (claude) · **B08 handoff/CTA** (claude, the 4-question + gold-set template) · **B09 outro**.

## PROOF teaching rubric — self-score (target ≥ 8/12; ship bar)

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | B01 shows the 4 questions as a structure before any result — and flags Q4 as out of reach | 2 |
| Reusable rubric | the 4 questions apply to any simple-vs-fancy choice; CTA hands the template + "build a gold set" | 2 |
| Worked example | the full-book tagging ablation walked live, one question per beat, with real tables | 2 |
| Falsifiability / edge | B05 (the ceiling): agreement ≠ correctness; "0.92 doesn't make either right"; needs ground truth | 2 |
| Active task | B08: a copyable 4-question template + "build a small blind gold set, score precision/recall" | 2 |
| Friction | "1,600× faster, exact, agrees on materials — so it wins, right?" resolved via 74% downstream + agreement≠correctness | 2 |
| **Total** | | **12 / 12 (target design)** |

## PROOF production gate (binary — can veto publish)

- **Legible at assertion:** real tables readable, held ≥2s, at the claim (VISUAL-PLAN).
- **Sources on screen:** every number traces to `week3_*.md`; model named exactly; gold set / prerequisite review render as **in-progress**, never results.
- **Side-by-side at comparison:** dictionary vs model together for reproducibility, speed/cost (B02), and per-field agreement (B04); B05 shows the two backends comparing only to each other.
- **`n` shown with every agreement number** (materials 0.919 · n=102, etc.).
- Verified at QC on the compiled master (see `_qc/REPORT.md`).

## Claim discipline (no source, no verdict — see SOURCES.md)

| Guardrail | How honored |
|---|---|
| Show `n` with every agreement number | full per-field table carries n (materials 0.919·n=102 … concepts 0.296·n=755); B00/B04 call out n=4 → n=102 |
| No tagger winner / no P-R-F1 number | the gold set is **being graded, not scored**; "hybrid" labeled a hypothesis (B06/B07) |
| "The choice matters," not "the model is wrong" | headline is the **74%** downstream swing; divergence framed as a precision/recall trade-off with no gold standard |
| No efficacy/learning claim | none; scope is reproducibility + agreement + downstream effect only |
| Ordering | **dormant** (0 prerequisite edges); the 26 Ch-27 links are *proposed*, awaiting faculty (B06/B07) |
| Model named exactly | `qwen2.5-coder:7b` (temp 0, self-hosted NEU cluster T4) — not "an LLM," not a vendor API |
| ~0.99 drift not portable | architectural point (temp-0 self-hosting ≠ exact) holds; the exact figure is hardware-tied |

## Series (film 4 vs film 3 — PROOF /series)

Delivers the denser re-run week-02 promised: **materials 0.933 (n=4) → 0.919 (n=102)** on the full
1,340-section book. Goes beyond repeating: adds the **downstream 74%** (does-it-matter, measured on the
actual roadmap) and names the **ceiling** (which tagger is *correct* is undecided) plus how it gets
settled (the gold set). Continues the week-01/02 honesty discipline (sources-on-screen, denominators,
ordering shown dormant).

## Duration

≈ 500 spoken words → est. **~3:30–3:45** at Bella's measured pace. Duration is an output, confirmed
after audio. Run audio/render/compile under `PYTHONUTF8=1` (Windows — see memory gotcha). If ≤3:00
wanted, trim B02/B06/B07 before sign-off.

## Palette & voice

- Two-skin (claude UI beats / humanitarians body). TEAL-led; **CRIMSON reserved for B03 (the 74% swing) and B05 (the ceiling)**; GOLD for the gold set (B06) and the speed callout.
- Voice Kokoro `af_bella`. Greeting `Hello, fellows` (audience address, consistent with wk-01/02). Sign-off "This is Satwik for Humanitarians AI."

## Reviewer checklist (sign only when all true)

- [ ] The one idea lands: an ablation shows reproducible / matters / where — **not** which is correct; verdict is undecided pending the gold set.
- [ ] B01 lands the 4-question framework **before** any result, and flags Q4 as the ceiling.
- [ ] B05 shows the falsifiability break (agreement ≠ correctness; needs ground truth); no winner is crowned anywhere.
- [ ] Every on-screen agreement number carries its **n**; n=4 → n=102 connected to week-02.
- [ ] No P/R/F1 number; "hybrid" reads as a hypothesis; ordering shown dormant; model named exactly; no efficacy claim; not "the model is wrong."
- [ ] Greeting / sign-off approved (`Hello, fellows` / "This is Satwik for Humanitarians AI.").
- [ ] Narration reviewed on the animated slate.

---

VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-08-16
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
