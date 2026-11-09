# FACTCHECK — Ten Words Apart

The author's own measurements (repo `crazyleg/dat-grpo-creativity` @ f4715f6,
archived in `research/`) are cited as his. Numbers we measured are marked so.

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | "Name ten words as different as you can" is a real creativity test, the DAT | B00, B01 | Olson et al., PNAS 118(25) e2022340118, 2021 ("Naming unrelated words predicts creativity"); datcreativity.com | ✅ |
| 2 | A researcher made it the reward for a 27B model | B00, B03 | post; model card: Qwen3.8-27B, 27,356,728,560 parameters, 250 GRPO updates | ✅ |
| 3 | Farm animals score 42; far-apart list 87 | B01, B02 | `evidence/dat_rescore.out`: 42.25, 86.73 (official code, GloVe 840B) | ✅ measured |
| 4 | It measures how far apart words sit in a map of meaning (GloVe, learned from a web crawl) | B01, B02 | dat.py: mean cosine distance × 100; GloVe 840B = Common Crawl | ✅ |
| 5 | 7 words → 21 pairs; DAT = 100 × average distance | B02 | dat.py (`itertools.combinations(subset, 2)` of the first 7 valid unique words) | ✅ |
| 6 | Higher scores reinforced, penalty for wrong-type words | B03 | README: `reward = dat_score / 100.0 - 0.2 * wrong_class_word_count` (GRPO) | ✅ |
| 7 | Nouns and verbs in training; adjectives held back | B03 | post; README "Adjectives are excluded from training" | ✅ |
| 8 | Weights are open | B03 | HF model card (Apache-2.0), GGUF release | ✅ |
| 9 | A strong AI judge rated its stories more creative | B03, B06 | `research/sol-table_f4715f6.md`: creativity +0.70 [+0.46, +0.95], imagery +0.62, coherence −0.90 [−1.28, −0.54]; gpt-6.1-sol, 64 pairs, both orders | ✅ (author) |
| 10 | All 192 re-scored lists match his numbers | B04, B00 | `dat_rescore.out`: worst per-item difference 0.0000 | ✅ measured |
| 11 | Nouns 72 → 90; adjectives 61 → 86 | B04, B07 | `dat_rescore.out`: 71.81 → 89.59; 60.72 → 86.26 | ✅ measured |
| 12 | Its "adjectives": endpoint, biblical, bark, mule, contour, demon, suture, crumb, staple, gavel | B05 | raw response `dat_adjectives/3`, step250; also quoted in his results doc | ✅ measured |
| 13 | Only biblical and staple can be adjectives | B05 | WordNet 3.0 via nltk (`dat_rescore.out`) | ✅ measured |
| 14 | All-adjective lists 29 of 32 before, 1 after | B05, B00, B07 | `dat_rescore.out` (our WordNet check) = his audit (29/32 → 1/32) | ✅ measured |
| 15 | His own repo says so | B05 | `research/noun-verb-full250-dat-results-2026-11-03.md`: "Raw distance therefore masks a large deterioration in the requested-class constraint" | ✅ |
| 16 | Automatic writing benchmarks saw no gain | B06, B07 | post ("absolutely non-impressive and showed no gains"); `fig_writing_evals.png` (WritingBench 8.06 → 8.05, Phi4 40.6%) | ✅ (author) |
| 17 | Instruction-following fell 3.7 points (IFEval 83.2 → 79.5, n = 541, 95% −7.2 to −0.4); math and coding held | B06, B07 | capabilities aggregate (strict prompt accuracy); GSM8K 98.05 → 98.44, HumanEval+ 93.90 → 92.07 | ✅ (author) |

## The math (B02)

1. `7 × 6 ÷ 2 = 21` — pairs among the seven scored words.
2. `DAT = 100 × (d₁ + d₂ + ⋯ + d₂₁) / 21` — Olson's dat.py, d = cosine distance.

Asserted in `build_beats.py`; the post writes the same formula as
`(100/21) Σ (1 − cos)`.

**Rendered-frame math review (2026-11-09, both aspects):** B02 at 15/50/85/95% of
its 15.58 s and at each row's reveal (1.0 / 2.6 s), in `media/B02.mp4` and the
portrait master. ×, ÷, =, the fraction bar, subscripts d₁…d₂₁ and the ellipsis
render; upright "DAT"; no tofu, no clipping. 16:9: both rows at full size. 9:16:
row 2 renders smaller, about 3% of frame height (floor 2%).
