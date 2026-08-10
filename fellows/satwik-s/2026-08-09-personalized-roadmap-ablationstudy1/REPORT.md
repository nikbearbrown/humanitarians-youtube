# VISUAL QC + PROOF gate — "Does the Fancy Part Earn It?" · Tagging Ablation (week-03)

Master: `reading-roadmap-tagging-ablation.mp4` — 1920×1080, **206.9s (≈3:27)**, 10/10 beats VIDEO.
Built entirely under `PYTHONUTF8=1` (audio + render + compile) → **no mojibake**.
Method: settled frames from the compiled master, read against the 9-point rubric + two-skin +
**PROOF production gate** + no-source-no-verdict.

## Beat-by-beat

| Beat | Skin | Result | On-screen artifact / notes |
|---|---|---|---|
| B00 ask | claude | PASS | "Hello, fellows"; RESULT lines clean (1.000 / ~0.991 · materials 0.89 · verdict + n≈4); @HumanitariansAI overlay |
| B01 framework | humanitarians | PASS | **5-check rubric before any result** (ISOLATE…DENOMINATOR) + decision rule |
| B02 isolate | humanitarians | PASS | control vs treatment (model named + digest); "only the backend changes"; HELD-FIXED chips |
| B03 stability | humanitarians | PASS | **side-by-side** lollipops rb 1.000 vs qwen 0.987–0.996; mean 1.000 vs 0.991; "GPU float, not sampling" |
| B04 agreement | humanitarians | PASS | per-field Jaccard bars; materials 0.887 hi; "+extra terms"; "neither is ground truth" |
| B05 weight | humanitarians | PASS | materials lifted → drives core role (Stage 4b); Jaccard 0.89 · recall 0.90 |
| B06 denominator | humanitarians | PASS | **falsifiability:** 0.996 → **0.933 + crimson `n = 4`**; control 1.000; VERDICT · PROVISIONAL + denser run next |
| B07 verdict | claude | PASS | 5-line decision incl. provisional (n≈4) caveat; "ship the deterministic default" |
| B08 handoff | claude | PASS | "Your turn." — 5-check template + reproducible command; "report the n" highlighted |
| B09 outro | claude | PASS | "Does the Fancy Part Earn It?" + @HumanitariansAI + sign-off |

## PROOF production gate — PASS

- **Legible at assertion:** every table/number readable, held for its beat. PASS.
- **Sources on screen:** every figure traces to `ablation_study_tagging.md`/`tagger_comparison.md`; model named exactly; denser run = "next," never a result. PASS.
- **Side-by-side at comparison:** rb vs qwen together (B03/B04); B06 shows plain + non-empty + n=4 together. PASS.

## PROOF teaching rubric — 12/12 (design, verified on screen)

Explicit framework (B01) · reusable rubric (5 checks + CTA template) · worked example (B02–B06 live) ·
falsifiability (B06, n=4 breaks the headline) · active task (B08 template + command) · friction
(99%/89% vs repro-free/no-gold-standard/n=4). **Ship rule:** teaching ≥8 ✓ AND production gate PASS ✓
AND passes its own standard ✓ → clears the bar. (Per toolkit law the master stays in the folder — not published.)

## Rubric / encoding / two-skin

- Edge bleed / title-safe / overflow / collision / legibility: PASS (type ≥~24px effective).
- Encoding: PASS — `—`/`·`/`→`/`≈` all render correctly (PYTHONUTF8).
- Two-skin: PASS (claude UI beats; humanitarians body, TEAL-led; CRIMSON reserved for B06).

## Non-blocking notes

- `compile.py --review` slate cut still fails on Windows (ffmpeg drawtext font-path spaces+backslashes); clean master unaffected.
- Beat-mix advisory: illustrate 6/10 (60%) — expected for a 6-body-beat explainer.

**Verdict: zero BLOCKER, zero MAJOR. Master clean; PROOF production gate PASS; teaching 12/12. Do not publish — master stays in the reel folder.**
