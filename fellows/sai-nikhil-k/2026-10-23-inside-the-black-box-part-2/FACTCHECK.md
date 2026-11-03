# FACTCHECK — Inside the Black Box, Part 2

"Essay" = Wolfram 2023, archived in `research/`.

## Claims

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | Layer 1 shows "the cat without its background", "the outline of the cat" | B01 | Essay, verbatim | ✅ |
| 2 | By layer 10 it's harder to interpret; features "maybe pointy ears", mostly unnamed | B01, B05 | Essay: "By the 10th layer it's harder to interpret what's going on … (maybe pointy ears are among them) … Mostly not." | ✅ |
| 3 | GPT-2 is the small model Wolfram uses for his examples; ChatGPT can't be downloaded | B02, B06 | Essay: "I'll usually work with a simpler GPT-2 system"; GPT-2 weights are public, ChatGPT's are not | ✅ |
| 4 | 12 attention blocks, 12 heads, 768 numbers per token | B02, B05 | Essay states all three; re-measured in `evidence/gpt2_inspect.out` | ✅ |
| 5 | 124,439,808 weights | B00, B02, B03, B05 | `gpt2_inspect.out` (sum of learned tensors) and the B03 formula | ✅ measured |
| 6 | Our rerun matches his first figure's next-word odds, to the decimal | B02 | `gpt2_inspect.out`: learn 4.5%, predict 3.5%, make 3.2%, understand 3.1%, do 2.9%; raw 0.044532 vs his 0.0445305 | ✅ |
| 7 | About fifty thousand tokens; each block about seven million weights | B03 | 50,257 tokens; 7,087,872 per block, all 12 equal | ✅ |
| 8 | Related words land near each other: alligator beside crocodile | B04 | Essay: "'alligator' and 'crocodile' … placed nearby"; figure | ✅ |
| 9 | 12 attention heads in GPT-2's first block, each with its own pattern | B04 | Essay: "the 12 attention heads in the first attention block (in GPT-2) have the following … patterns" | ✅ |
| 10 | A 768×768 weight matrix looks like static; smoothed, structure appears; meaning "quite unknown" | B04 | Essay: "768×768 matrix of weights … 64×64 moving averages … what those features might be is quite unknown"; shape re-measured `(768, 768)` | ✅ |
| 11 | Wolfram calls ChatGPT's success a scientific discovery, no theory yet | B05 | Essay: "a—potentially surprising—scientific discovery"; "no 'ultimate theoretical reason'" | ✅ |

## The math (B03)

1. `N = Vd + Pd + L(12d² + 13d) + 2d`
2. `12d² + 13d = 7,087,872`
3. `N = 124,439,808`

with V = 50,257, P = 1,024, d = 768, L = 12 (all measured). Per block: attention
q, k, v and output projections 4d²; feed-forward d→4d→d 8d²; biases 3d + d + 4d
+ d = 9d; two layer norms 4d; 9d + 4d = 13d. Final layer norm 2d.

**Algebra check** (asserted in `build_beats.py`): 12·768² + 13·768 = 7,077,888 +
9,984 = 7,087,872 = the measured block 0 (all 12 blocks equal);
50,257·768 + 1,024·768 + 12·7,087,872 + 1,536 = 38,597,376 + 786,432 +
85,054,464 + 1,536 = 124,439,808 = the measured total.

**Rendered-frame math review (2026-10-26, both aspects):** frames at each row's
reveal and at 95% of the 18.86 s beat (`media/B03.mp4`, `vertical/media/B03.mp4`).
Italic N, V, P, L, d; superscript 2 on d; parentheses and plus signs clean;
thin-space digit groups (7 087 872, 124 439 808); no tofu or clipping; reveals
inside the 15 s comp. 9:16 ink heights: rows 3.4% / 4.4% / 5.1% of frame height
(floor 2%).
