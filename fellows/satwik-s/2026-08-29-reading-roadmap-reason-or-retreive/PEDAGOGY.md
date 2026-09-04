# PEDAGOGY — GATE P (+ PROOF) — "Does It Reason, or Just Retrieve?" · week-05

Film 6 on `claude-hai` (Bella · Pragmatist / skeptical-explainer), built only from
`sources/week5_video_numbers.md`. GATE P: a human signs `VERDICT: PASS` before any audio. This film
carries the **PROOF** teaching rubric + production gate (framework-first; no source, no verdict). It is
the week the dormant dependency graph is turned on (draft) and the project's core "selects and
sequences, not retrieves" claim is *shown*.

## The one idea

> Retrieval returns what's **similar**; reasoning adds what's **required**. Prove the difference by
> A/B-ing the mechanism and counting what a search can't reach. With the graph on, the roadmap pulls
> in **36 (LNP) / 19 (PT)** foundations a top-k search misses and states dozens of "read-before" links
> — it selects and sequences. But it's **insertion, not reshuffle** (0 matched sections moved), on
> **DRAFT** edges (authoritative graph = 0). Tagging win hardened: F1 **0.89 vs 0.35**, gap CI clears zero.

## Act structure (framework-first per PROOF)

- **B00 hook / ASK** (claude) — recap wk-04's dormant ordering → turn the graph on; reasons or retrieves?
- **B01 THE FRAMEWORK** (humanitarians) — the **4 steps** (A/B the mechanism · count the unreachable · name it precisely · mark what's draft), shown **before any result**.
- **B02–B06 the worked example** — one step per beat, each with its real table:
  with/without A/B (64→100, 45→64) · what retrieval can't reach (+36/+19 foundations) · **insertion, not reshuffle (0 moved — falsifiability)** · the DRAFT status (62/43; auth 0; 1,483 review) · tagging hardened (F1 gap CI clears zero).
- **B07 verdict** (claude) · **B08 handoff/CTA** (claude, the reason-vs-retrieve template) · **B09 outro**.

## PROOF teaching rubric — self-score (target ≥ 8/12; ship bar)

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | B01 shows the 4-step "reasons or retrieves?" test as a structure before any result | 2 |
| Reusable rubric | the 4 steps apply to any "does my system reason or just search?" question; CTA hands the template | 2 |
| Worked example | the with/without-graph run walked live, one step per beat, with real tables | 2 |
| Falsifiability / edge | B04: "insertion, not reshuffle" — 0 matched sections moved; the naive reorder claim refused. (+ B06 CI clears zero) | 2 |
| Active task | B08: A/B the mechanism, count the unreachable, name it precisely, mark what's draft | 2 |
| Friction | "+36 sections → it reordered my list?" resolved via insertion ≠ reshuffle + draft ≠ authoritative | 2 |
| **Total** | | **12 / 12 (target design)** |

## PROOF production gate (binary — can veto publish)

- **Legible at assertion:** real tables readable, held ≥2s, at the claim (VISUAL-PLAN).
- **Framework-first:** B01 lands the 4 steps before any result.
- **Side-by-side at comparison:** with/without (B02), retrieval ✗ vs graph ✓ (B03), dictionary vs model + CI (B06).
- **DRAFT + provisional marked:** ordering carries DRAFT + "authoritative = 0" (B05/B07); tagging carries "provisional · grader 1" (B06); 1,483 = review size.
- Verified at QC on the compiled master (see `_qc/REPORT.md`).

## Claim discipline (no source, no verdict — see SOURCES.md)

| Guardrail | How honored |
|---|---|
| DRAFT, not approved | B05 DRAFT stamp + "authoritative graph: 0 edges"; B07 "edges are DRAFT"; one sign-off activates |
| Insertion, not reshuffle | B04 shows 0-reordered + IS/IS-NOT; B07 restates "insertion, not reshuffle" |
| 1,483 = review size | shown as the one-time faculty review (ranked/capped/triageable), never "done" |
| Tagging provisional | B06 "provisional · grader 1" even with the CI |
| No learning/efficacy claim | none; scope is selection/sequencing + tagging correctness |
| Model named exactly | `qwen2.5-coder:7b` (temp 0, self-hosted) — series continuity |

## Series (film 6 vs film 5 — PROOF /series)

Turns on what was dormant: wk-02 ablation (n=4) → wk-03 full book + ceiling → wk-04 gold verdict
(provisional) → **wk-05 the ordering demonstrated (draft) + tagging hardened (CI)**. The ordering was
"0 edges, pending faculty" for three films; this film shows its effect non-destructively and keeps the
authoritative graph at 0. Standing honesty pattern applied: DRAFT/provisional marked from the first
result beat; the falsifiability (insertion ≠ reshuffle) is foregrounded, not buried.

## Duration

≈ 555 spoken words → est. **~3:40–3:55** at Bella's measured pace. Duration is an output, confirmed
after audio. Run audio/render/compile under `PYTHONUTF8=1` (Windows — see memory gotcha); use the
toolkit venv python for Kokoro. If ≤3:20 wanted, trim B03/B05/B07.

## Palette & voice

- Two-skin (claude UI beats / humanitarians body). TEAL-led; **CRIMSON reserved for B04 (insertion not reshuffle) and B05 (DRAFT)** + the B06 provisional stamp; GOLD for the +delta (B02).
- Voice Kokoro `af_bella`. Greeting `Hello, fellows` (consistent with wk-01–05). Sign-off "This is Satwik for Humanitarians AI."

## Reviewer checklist (sign only when all true)

- [ ] The one idea lands: retrieval returns similar, reasoning adds required — shown via with/without + what a search misses.
- [ ] B01 lands the 4-step method **before** any result.
- [ ] B04 shows "insertion, not reshuffle" with the 0-reordered fact; no reorder/reshuffle claim anywhere.
- [ ] The ordering is marked **DRAFT** with "authoritative = 0" (B05/B07); 1,483 = review size; tagging "provisional · grader 1" (B06).
- [ ] B06's F1-gap CI [0.44,0.64] visibly clears zero; side-by-side comparisons legible; model named exactly.
- [ ] Greeting / sign-off approved (`Hello, fellows` / "This is Satwik for Humanitarians AI.").
- [ ] Narration reviewed on the animated slate.

---

VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-08-29
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
