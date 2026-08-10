# PEDAGOGY — GATE P (+ PROOF) — "Does the Fancy Part Earn It?" · Tagging Ablation

Film 3 on `claude-hai` (Bella · Pragmatist / skeptical-explainer), built only from `sources/`.
GATE P: a human signs `VERDICT: PASS` before any audio. This film also carries the **PROOF** teaching
rubric + production gate (framework-first; no source, no verdict).

## The one idea

> When the cheap deterministic component is **exactly reproducible** and **agrees where it matters**,
> the simple part earns the default — proven by an **ablation** whose limits (n, no gold standard) are
> shown, not hidden. Verdict: ship rule-based v1; keep the pinned LLM as a named option; strongest
> number **provisional (n≈4)** pending the denser re-run.

## Act structure (framework-first per PROOF)

- **B00 hook / ASK** (claude) — the skeptical question: does the fancy tagger earn it?
- **B01 THE FRAMEWORK** (humanitarians) — the 5-check ablation rubric, **before any result** (PROOF gate).
- **B02–B06 the worked example** — the tagger ablation walked one check per beat, each with its real table:
  ISOLATE (setup) · STABILITY (1.000 vs 0.991) · AGREEMENT (per field) · WEIGHT (materials) · **DENOMINATOR (0.996→0.933, n=4 — the falsifiability beat)**.
- **B07 verdict** (claude) · **B08 handoff/CTA** (claude, the 5-check template + command) · **B09 outro**.

## PROOF teaching rubric — self-score (target ≥ 8/12; ship bar)

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | B01 shows the 5 checks as a structure before any example | 2 |
| Reusable rubric | the 5 checks apply to any simple-vs-fancy choice; CTA hands the template | 2 |
| Worked example | the tagger ablation walked live, one check per beat, with real tables | 2 |
| Falsifiability / edge | B06: the headline breaks once padding is stripped (0.996→0.933, n=4); control holds | 2 |
| Active task | B08: a copyable 5-check template + the reproducible command (not "ask Claude") | 2 |
| Friction | "99% stable + 89% agree — so why not the LLM?" resolved via repro-is-free + no-gold-standard + n=4 | 2 |
| **Total** | | **12 / 12 (target design)** |

## PROOF production gate (binary — can veto publish)

- **Legible at assertion:** real tables readable, held ≥2s, at the claim (VISUAL-PLAN).
- **Sources on screen:** every number traces to the study; model named exactly; denser run = "next," never a result.
- **Side-by-side at comparison:** rule-based vs qwen together (B03/B04); **B06 shows plain + non-empty + n=4 together.**
- Verified at QC on the compiled master (see `_qc/REPORT.md`).

## Claim discipline (no source, no verdict — see SOURCES.md)

| Guardrail | How honored |
|---|---|
| Show `n` with every small-sample number | materials 0.887/0.933 always with n≈4; B06 shows the plain→restricted pair + n together |
| Not "LLM bad" | precision/recall trade-off, no gold standard; LLM near-reproducible + agrees where it matters |
| No efficacy/learning claim | none; scope is reproducibility + agreement only |
| Denser `--chapters 19-27` run | shown as planned "next," never a result (it hasn't run) |
| Model named exactly | `qwen2.5-coder:7b` (temp 0, pinned/self-hosted, digest) — not "an LLM," not a vendor API |
| Difficulty (0.350 / MAE 0.88) | weakest signal / faculty-calibration item, never a usable score |

## Series (film 3 vs film 2 — PROOF /series)

Continues week-02's honesty discipline (sources-on-screen, denominators). This film *is* the
"where the two backends disagree = the faculty-review agenda" thread week-02's B04/B06 set up. Standing
pattern applied: show the real data + state the limit (n) from the first result beat.

## Duration

≈ 510 spoken words → est. **~3:30–3:45** at Bella's measured pace. Duration is an output, confirmed after
audio. Run audio/render/compile under `PYTHONUTF8=1` (Windows — see memory gotcha). If ≤3:00 wanted,
trim B01/B06/B07 before sign-off.

## Palette & voice

- Two-skin (claude UI beats / humanitarians body). TEAL-led; CRIMSON reserved for the B06 falsifiability break.
- Voice Kokoro `af_bella`. Greeting `Hello, fellows` (audience address, consistent with week-02). Sign-off "This is Satwik for Humanitarians AI."

## Reviewer checklist (sign only when all true)

- [ ] The one idea lands: simple earns the default when exactly-reproducible + agrees where it matters; verdict provisional (n≈4).
- [ ] B01 lands the 5-check framework **before** any result (framework-first).
- [ ] B06 shows the falsifiability break (0.996→0.933, **n=4**) and the control at 1.000; verdict reads **provisional**.
- [ ] Every on-screen number carries its n; model named exactly; denser run = "next," not a result; no "LLM bad"; no efficacy claim.
- [ ] Greeting / sign-off approved (`Hello, fellows` / "This is Satwik for Humanitarians AI.").
- [ ] Narration reviewed on the animated slate.

---

VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-07-30
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
