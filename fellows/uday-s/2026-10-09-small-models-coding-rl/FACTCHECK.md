# FACTCHECK — One Model, Three Numbers

Status: **GATE F SIGNED — 2026-10-09. 16 rows PASS.**

Topic as commissioned: *optimizing smaller models for coding with the help of
agentic systems and RL.*

Primary sources:
- **DeepSWE-Preview** — Agentica / Together AI, Qwen3-32B base, RL only.
- **SWE-smith** — Yang, Lieret, Jimenez, Wettig, Khandpur, Zhang, Hui, Press,
  Schmidt, Yang, *"SWE-smith: Scaling Data for Software Engineering Agents"*.

## Sourcing rule applied to this reel

The search results for this topic are dominated by aggregator pages (vendor
roundups, newsletter summaries, "best models of 2026" listicles). **No figure in
this reel comes from one.** Every number was taken from the model release or the
paper abstract. This matters here more than usual: the whole reel is about
numbers quoted without their conditions, and quoting a number without its
condition while making that argument would be self-refuting.

## Verified figures used on screen

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B01, B04 | DeepSWE-Preview scores 42.2 pass@1 on SWE-bench Verified | ✓ PASS | DeepSWE release — pass@1 averaged over 16 runs |
| 2 | B01, B04 | it also reports 59.0 with hybrid test-time scaling | ✓ PASS | same — Best@16 with a verifier |
| 3 | B01, B04 | it also reports 71.0 | ✓ PASS | same — Pass@16, the oracle upper bound |
| 4 | B04 | Best@8 scores 57.9 | ✓ PASS | same |
| 5 | B03 | base model is Qwen3-32B | ✓ PASS | same |
| 6 | B03 | trained with RL only, no distillation | ✓ PASS | same |
| 7 | B03 | the algorithm is a modified GRPO | ✓ PASS | same — the authors call it GRPO++ |
| 8 | B03 | ~4,500 tasks from an R2E-Gym subset | ✓ PASS | same |
| 9 | B03 | repositories appearing in SWE-bench Verified were filtered out of training | ✓ PASS | same — `sympy` named as an example |
| 10 | B03 | 64 H100s, six days | ✓ PASS | same |
| 11 | B05 | Devstral-Small (24B) scores 46.6 on one attempt, on OpenHands | ✓ PASS | DeepSWE release, comparison table |
| 12 | B05 | DeepSWE's own evaluation used R2E-Gym at 64k context, 100 max steps | ✓ PASS | same |
| 13 | B06 | the comparison table mixes four scaffolds and three test-time settings | ✓ PASS | counted from the table: R2E-Gym, OpenHands, SWE-Agent, and the iterative OpenHands variant; settings are one-run, Best@8, Best@16 |
| 14 | B06, B07 | SWE-Agent-LM-32B scores 40.2 pass@1 | ✓ PASS | SWE-smith abstract, and the DeepSWE table agrees |
| 15 | B07 | SWE-smith built 50k instances across 128 GitHub repositories | ✓ PASS | SWE-smith abstract |
| 16 | B07, B08 | best-of-16 moved the same model by 16.8 points (42.2 → 59.0) | ✓ PASS | arithmetic on rows 1 and 2 |

## Arithmetic shown on screen

- `59.0 − 42.2 = 16.8` — the selection gain (B07, B08).
- `42.2 − 40.2 = 2.0` — RL against distillation at one attempt (B07).
- `46.6 − 42.2 = 4.4` — Devstral-Small's margin over DeepSWE at one attempt (B05).
- `32B − 24B = 8B` — the parameter difference in B05.

## A discrepancy in the primary source, and how it is handled

The DeepSWE release gives the hybrid test-time-scaling score as **59%** in its
table and figures but **59.2%** in its conclusion. The reel uses **59.0**, the
table figure, because the table is the one that carries the scaffold and setting
columns the reel is arguing about. The 0.2 difference changes nothing in the
argument and is recorded here rather than smoothed over.

## Precision notes

- **pass@16 is not best@16.** 71.0 is the fraction solved by *any* of 16
  trajectories — an oracle that already knows which patch passes. B04 draws it
  with a dashed border and labels it "upper bound, not shippable", because this
  is the single most misread number in the area.
- **42.2 is itself an average over 16 runs.** It is a stable estimate of one
  attempt, not one lucky attempt. Stated in the citation strip.
- **B06 shows 6 of the 10 rows.** The six were chosen to span all three
  settings and three of the four scaffolds; the citation strip says "6 of the 10
  rows shown" so the selection is visible. No row was dropped for being
  inconvenient — the two highest and the two lowest are both included.
- **Devstral-Small's 46.6 is as reported in DeepSWE's table**, not Mistral's own
  evaluation, which reports a different figure under a different setup. Using
  one table's internally-consistent numbers is the point of the beat.
- **"Modified GRPO" is said rather than "GRPO++"** in narration, because the
  name is not the claim; the modification is. The ingredients are listed in the
  source but not on screen, as they would not survive 4 seconds of reading.

## Claims deliberately NOT made

- **No claim that DeepSWE is the best open coding model.** The reel's own
  argument forbids ranking across scaffolds.
- **No claim that RL beats distillation**, or the reverse. Two points at one
  attempt, from different scaffolds, supports neither.
- **No claim about closed models.** None appear in the reel.
- **No claim that test-time scaling is illegitimate.** The verdict says to
  budget for it — 16× inference — not to avoid it.
- **No cost, latency or throughput figures**, because the sources do not give
  comparable ones and the 16× is a count of trajectories, not a price.
- **No recommendation of a specific model to use.** The deliverable is the
  rubric, not a purchase.
