# SOURCES — Grokking: When AI Suddenly Understands

## Executable evidence (every on-screen number)
- `evidence/grok_toy.py` → `evidence/grok_toy.out.txt` + `evidence/grok_toy.json` (+ every-step curves in `evidence/grok_toy_steps.npz`). numpy 2.5.3, seed 2026. A toy re-run of the setup, not a reproduction of the paper's transformer.
  - Task: (a + b) mod 97. The 97 × 97 table has 9,409 cells; 3,763 (40 %) are shown in training, 5,646 are held out.
  - Model: shared 128-d number embeddings → 256 ReLU units → 97 logits. Full-batch AdamW, lr 1e-3, 30,000 steps. Two runs, same seed and split: weight decay 1.0 (grokking run) and 0.0 (control).
  - Logged every step: train accuracy, test accuracy, total weight norm. End of run: energy of the learned embeddings at each of the 48 cos/sin frequencies over the 97 numbers.
  - `evidence/make_scene_data.py` writes `runtime/remotion/src/grokkingData.ts` from the JSON; the Grokking.tsx scenes read numbers only from that file.
  - Results (grok_toy.out.txt):
    - With weight decay 1.0: train accuracy first hits 100 % at step 263 (test 0.0 % at that step); test first 50 % at step 3,579, first 99 % at step 5,299, final 100 %. 5,299 / 263 = 20.1 → "≈ 20× more steps" (B05).
    - Weight norm (with decay): 26.5 at start → peak 98.9 at step 1,408 (every-step log) → 61.4 at step 30,000 (B06 "lookup table 99" vs "the rule 61").
    - Without weight decay: train 100 % at step 228; test 0.02 % at step 30,000 (shown "0%"); weight norm 125.4 and still rising (B06).
    - Embedding spectrum (B07): with decay, the top 5 of 48 frequencies (k = 14, 27, 17, 6, 36) hold 71.9 % of the energy ("72%"); without decay 13.9 %; a flat spectrum would put 10.4 % in any 5.
    - B02 and B08 read the same curve: practice 100 % / new 0 % at step 263; practice 100 % / new 100 % at step 30,000.
    - Example cells (B03, B04, B07) are checked against the split: 60 + 50, 12 + 40, 88 + 23 are training cells; 33 + 71, 90 + 9, 3 + 58 are held out.
  - Seed note: one run, seed 2026, no tuning of hyperparameters after seeing results (the first full run is the one on screen).

## Literature
- Power, Burda, Edwards, Babuschkin, Misra, "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets", OpenAI, 2022, arXiv:2201.02177. Small transformer trained on binary-operation tables mod 97 (including a + b), trained on a fraction of the table; validation accuracy jumps to near 100 % long after training accuracy saturates; weight decay was the most effective intervention for data efficiency.
- Nanda, Chan, Lieberum, Smith, Steinhardt, "Progress measures for grokking via mechanistic interpretability", ICLR 2023, arXiv:2301.05217. Reverse-engineers a one-layer transformer trained on addition mod 113: it maps numbers to rotations on a circle (cosines and sines at a few key frequencies) and adds with trigonometric identities. Describes three phases: memorization, circuit formation, cleanup (weight decay removes the memorizing parts).
- Varma, Shah, Kenton, Kramár, Kumar, "Explaining grokking through circuit efficiency", 2023, arXiv:2309.02390. A generalizing circuit is more efficient (smaller parameter norm for the same output) than a memorizing one; weight decay favors it. Basis for B06's "memorizing is expensive, a rule is cheap".
- Liu, Michaud, Tegmark, "Omnigrok: Grokking Beyond Algorithmic Data", ICLR 2023, arXiv:2210.01117 (weight norm as the driver of grokking).
- Robert A. Heinlein, *Stranger in a Strange Land*, G. P. Putnam's Sons, 1961. "Grok" is the Martian word the novel introduces; it means to understand something so thoroughly that it becomes part of you. Meaning paraphrased on screen; no text from the novel is quoted.
- Logos: icons/logos/openai/openai-01.svg (B03), already in runtime/remotion/public/logos/.

## Corrections applied (DOUBLE-CHECK LAW)
1. Points 2–4: the curves on screen come from our numpy re-run (a small embedding + MLP network), not from Power et al.'s transformer. The narration describes the paper's setup; the screen labels the numbers "our numpy re-run".
2. Point 5: "weight decay pushes toward simpler solutions" is the explanation offered by Nanda et al. 2023 and Varma et al. 2023, stated here in plain words. Our run backs it two ways: the weight norm falls as test accuracy rises, and the same run without weight decay does not generalize within 30,000 steps.
3. Point 6: Nanda et al. studied a one-layer transformer on addition mod 113, not mod 97; the narration doesn't attach 97 to their work. The frequency spectrum shown is from our run's embeddings, labelled as such.
4. Point 1 (hook): "trained far longer" is shown with our run's real step counter. The paper's own runs were much longer than ours, so the step counts on screen describe our run only.
