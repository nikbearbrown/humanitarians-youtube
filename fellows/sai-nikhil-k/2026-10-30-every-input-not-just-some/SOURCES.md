# SOURCES — Every Input, Not Just Some

## Provenance

Sai gave the topic and URL (2026-11-09) as the second video for the week of
10-30, asked for many images and light math, chose the angle and title, and
decided to show Anthropic's charts with credit.

## Sources

| What | Where | Used for |
|---|---|---|
| Anthropic, "LLMs are making formal software verification feasible at a much larger scale", Frontier Red Team with Theorem, Oct 22, 2026 | https://www.anthropic.com/research/formal-verification · archived `research/anthropic_formal_verification_2026-10-22.html` | every number labelled as the post's; four figures; the limits in B06 |
| Theorem, `oss-verify-proofs` (MIT) | https://github.com/theorem-labs/oss-verify-proofs @ `f1fdc8dd00f2` · README archived `research/theorem_oss_verify_proofs_README_f1fdc8dd.md` | published-proof counts (B05), "What a proof does not say" (B06), repo screenshot |
| Our toy demo | `evidence/fuzz_vs_proof.py` (+ `.out`), z3-solver 5.3.3 | B04 |
| Theorem index tally | `evidence/theorem_index.py` (+ `.out`) | B05 caption |

## Images

| Beat | File | What | Credit / licence |
|---|---|---|---|
| B02 | `anth_hero.jpg` | the post's hero illustration | Anthropic · © Anthropic PBC, shown with credit (Sai's decision) |
| B02 | `dice.jpg` | dice | Anton Ehrola, CC BY-SA 4.0, Wikimedia Commons |
| B02 | `riscv_board.jpg` | StarFive VisionFive 2 RISC-V board | Teeks99, CC BY-SA 4.0, Wikimedia Commons |
| B05 | `anth_proof_order.png` | shared-workspace chart (GIF frame 474/598) | Anthropic, as above |
| B05 | `anth_reuse.png` | proof-reuse block chart | Anthropic, as above |
| B05 | `anth_tokens.png` | tokens-to-proof line chart | Anthropic, as above |
| B05 | `theorem_repo.png` | repo page screenshot | Theorem, MIT |
| — | `a380_cockpit.jpg`, `anth_post_top.png` | fetched, not used on screen | Niklitov CC BY-SA 4.0; Anthropic |

Every file has a sidecar `images/src/<slug>.json`.

## Honesty log

- **Not openly licensed:** Anthropic's figures. Shown with credit by Sai's
  explicit decision (2026-11-09); logged here and in PEDAGOGY.
- **239 vs 90:** the post's proved count vs Theorem's published subset; the reel
  says which is which.
- **The toy is ours.** It illustrates the post's argument; it is not their code,
  their solver, or their scale.
- **Proof of a property, not of the library:** stated in B06 and the verdict,
  as both the post and Theorem's README say.
