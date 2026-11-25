# PLAN — tldr-attention-scaling · "Why Attention Divides By The Square Root"

Section S2 of `../tldr-sections-attention-is-all-you-need.md` · source: Vaswani et al. 2017, §3.2.1 + footnote 4 · tier: **single-insight**
Channel claude-liam · Liam (Kokoro `am_onyx`) · palette claude · `learn_canvas: cream` · greeting **Hola** (Kokoro says it cleanly; not Hej, which it voices "hedge")

**Key case (Gate 1.1):** one query scored against 6 keys. At d_k=4 the softmax weights are sensible; at d_k=512, with the same recipe, one key takes 99.6% and the rest round to zero.

## Evidence already run (real, seeded; files in this folder)
`experiment.py` → `experiment_output.txt`, `naive_fixed_divisor.py` → `naive_output.txt`. seed 7, q and k components iid N(0,1) (the paper's footnote-4 assumption), 6 keys, 20 000 trials.

| d_k | var(q·k) | mean largest weight, raw | …scaled by √d_k | mean largest p(1−p), raw | …scaled |
|---|---|---|---|---|---|
| 4 | 3.99 | 0.574 | 0.400 | 0.2031 | 0.2190 |
| 16 | 15.98 | 0.778 | 0.416 | 0.1357 | 0.2256 |
| 64 | 63.99 | 0.890 | 0.419 | 0.0737 | 0.2272 |
| 512 | 512.65 | 0.961 | 0.420 | 0.0276 | 0.2276 |
| 2048 | 2052.58 | 0.980 | 0.422 | 0.0141 | 0.2277 |

Single d_k=512 instance: raw softmax `[0, 0.996, 0.004, 0, 0, 0]`; scaled `[0.027 0.356 0.278 0.085 0.103 0.151]`.
Naive (fixed divisor 10): largest weight 0.209 (d=4) → 0.368 (d=64) → 0.648 (d=512) → 0.809 (d=2048); √d_k divisor holds ~0.40–0.42 at every d. Uniform over 6 keys would be 0.167.

Honesty notes: "p(1−p)" is OUR proxy for how much gradient can flow through softmax; the paper only says "extremely small gradients". The result holds for the paper's idealised assumption (independent, mean 0, variance 1), not for trained vectors; the paper itself says "We suspect". The film says so on screen.

## Beats (section 1 owns B10–B18; nine body beats — within the density limit)
| id | role | what the viewer watches (show) | learn: Q → next |
|---|---|---|---|
| B00 | TL;DR·WHAT | `ClaudeTldrWhat` | — |
| B01 | TL;DR·WHY | `ClaudeTldrWhy` | — |
| B02 | THE QUESTION | `BrutalistHesitantWriter` — "Why divide by the square root of d_k?" with correction "a detail you can skip" → "the thing that keeps the softmax from collapsing" | — |
| B03 | TERMS | `ClaudeDefinitions`: dot product · softmax · variance | — |
| B10 | HOOK | 6 key bars at d_k=4: sensible weights. Same query, a d slider sweeps to 512: bars snap to one-hot (0.996). "Same recipe. Bigger vectors. One word takes everything." | Why does bigger collapse? |
| B11 | INSTANCE 1 | d slider sweeps 4→16→64→512; scores plot as dots on a line: the spread visibly widens; largest-weight counter climbs 0.574→0.961 | Is it the spread? |
| B12 | INSTANCE 2 | the softmax curve; saturated scores sit on its flat ends; slope readout p(1−p) falls 0.203→0.028 (labelled "our measure") | What does flatness cost? |
| B13 | NAIVE | "just divide by 10" — works near d=64, but at d=4 bars go flat (0.209) and at d=2048 collapse again (0.809). A fixed fix fits one d | What divisor tracks d? |
| B14 | SHIFT | representation: the **width of the cloud of scores** versus d, points std = 2, 4, 8, 16, 22.6, 45.3 landing on a √d curve | Why √d? (**predict: true** — "if the spread doubles each time d quadruples, what do we divide by?") |
| B15 | TRANSFORM | the d=512 cloud shrinks by 1/√512 onto the d=4-width cloud (same dots, same identity); bars beneath morph from one-hot to the healthy spread | — (the aha) |
| B16 | ABSTRACTION | equation lands by MathText SVG: Var(q·k) = d_k, then Var(q·k/√d_k) = 1 | symbols? |
| B17 | TANGENT | five zones, symbols mapped to the dots and the width bar; explain, not derive (EQUATIONS.md) | the opening object? |
| B18 | PAYOFF | the HOOK's exact 6 bars, d=512: raw vs scaled `[0.027 0.356 …]`, same objects as B10 | — |
| BVDT | recap | `ClaudeVerdictArtifact` — "Let's recap with Claude." | — |
| BHTF | YOUR TURN | `ClaudeComposerAsk`: paste-able prompt (below) | — |
| BOUT | outro | `ClaudeTitleOutro`, OUTRO-LOCK, "<exact title>. At Nik Bear Brown." | — |

**BOUNDARY (folded into BHTF):** not taught — whether trained vectors really behave like independent unit-variance numbers; the multi-head and masking parts of attention.
**YOUR TURN prompt:** "Write a short Python script that draws random queries and keys with variance 4 instead of 1, computes the variance of their dot products at d_k = 64, and checks whether dividing by √d_k still gives 1. Predict the number first, then run it, then explain what divisor would fix it."  (Expected: variance 16·d_k scaling → var(q·k) = 16·64 = 1024 → divisor must be 4·√d_k; the viewer's own check.) To be recomputed in FACTCHECK before approval of the script.

## Terms and equations
TERMS: dot product, softmax, variance (prerequisites only; the film earns "scaling" and the √d_k itself). Equations: Var(q·k)=d_k and Var(q·k/√d_k)=1. Algebra to verify separately: Var(q_i k_i)=E[q_i²]E[k_i²]=1 for independent mean-0 variance-1 components; variances of independent terms add (d_k terms); Var(cX)=c²Var(X). **Typography route: MathText SVG (matplotlib), not Manim MathTex — dvisvgm missing on this machine.** Each equation frame to be inspected at its revealed states and at 15/50/85%.

## Length (§5): single-insight
TL;DR ≈ 36 s (two cards) + question 12 + terms 15 + body 9 beats ≈ 9×~20 = 180 + recap 25 + your turn 35 + outro 6 ≈ **5.2 min**. Derived, not targeted; nothing padded.

## Gate-1 audit
| Check | Pass? |
|---|---|
| Key case named | ✓ (6-key query, d=4 vs 512) |
| Opens unsolved; no vocabulary before the felt problem | ✓ B10 (terms live in B03, defined as prerequisites only) |
| ≥ 2 moving instances before the abstraction | ✓ B11, B12 |
| Definitions are endpoints | ✓ variance of the dot product arrives at B16 |
| NAIVE shown | ✓ B13 fixed divisor 10 |
| One representation in one sentence | ✓ "the width of the score cloud against d" |
| Exactly one TRANSFORM | ✓ B15 |
| Equation followed by TANGENT | ✓ B17 |
| PAYOFF returns the HOOK's object | ✓ B18 = B10's bars |
| Nothing for completeness; deferrals logged | ✓ multi-head, mask, trained-vector behaviour → boundary |
| Mystery-framed opener | ✓ |
| `predict: true` before TRANSFORM | ✓ B14 |
| Boundary + transfer → BHTF | ✓ |
| SHOW/HOLD/CARD | 9 SHOW body beats (Manim), 0 PUNT; bookends are Remotion cards by contract |

## Library-first (GATE L)
`./art scenes` for "softmax bars", "histogram spread", "weighted average grid", "code listing" returned only unrelated Remotion scenes (finance/report charts, mascot grids, `LectureCodeTrace`). tldr LEARN beats must be pure Manim, so every LEARN beat is a miss logged by the search to `TEMPLATE-MISSES.md`; they are authored as `scenes.py` classes sharing one state factory (the score cloud and bars persist across B10–B18). Bookends reuse registered `ClaudeTldrWhat`, `ClaudeTldrWhy`, `BrutalistHesitantWriter`, `ClaudeDefinitions`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`, `ClaudeTitleOutro` (to be confirmed with `./art scenes --check`).

## Open items before building
1. Your approval of this plan (GATE: approve the plan).
2. Fact-check pass: re-derive the table independently, confirm footnote-4 wording, recompute the BHTF answer, strip datable claims.
3. Render environment: first `./art run` will be the real test of Manim 0.20.1 + Remotion + Chrome on this Mac (the toolkit notes a Chrome crash on its author's Mac; fallback is Playwright's chromium).
