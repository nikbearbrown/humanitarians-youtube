# FACTCHECK — Grokking: When AI Suddenly Understands

Status: claims checked by Claude Code against SOURCES.md and the evidence run. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | A small AI aces practice problems almost at once but fails new ones; trained far longer, it gets them too | PASS | grok_toy.out.txt: train 100 % at step 263, test 0 %; test 99 % at step 5,299 | step counter on screen is our run's |
| 2 | B03 | 2022, OpenAI researchers trained a tiny transformer on (a + b) mod 97, from part of the answer table | PASS | Power et al. 2022 (arXiv:2201.02177) | "our numpy re-run" caption on the 40 % split |
| 3 | B04 | Training accuracy hits 100 % fast; test stays near zero; it memorized | PASS | grok_toy.out.txt (step 263, test 0.0 %) | — |
| 4 | B05 | Many times more steps later, test accuracy shoots toward 100 % (log-scale axis) | PASS | grok_toy.out.txt: 5,299 / 263 = 20.1× | "≈ 20× more steps" |
| 5 | B06 | Weight decay favors simpler solutions; memorizing is expensive, a rule cheap; it swaps the table for the rule | PASS (soft) | Nanda et al. 2023; Varma et al. 2023; our run: norm 98.9 → 61.4, control without decay stays at 0 % test with norm 125 | explanation stated as the field's account, shown with our control |
| 6 | B07 | 2023, Nanda and colleagues looked inside: it adds with waves, sines and cosines, like hands around a clock | PASS | Nanda et al. 2023 (arXiv:2301.05217; their model used mod 113) | spectrum labelled "our run" |
| 7 | B08 | A flat curve isn't always stuck; memorized and understood look alike until they don't | PASS | grok_toy: practice 100 % at both snapshots, new 0 % vs 100 % | — |
| 8 | B09 | The word is from Heinlein's 1961 novel Stranger in a Strange Land: to understand so fully it becomes part of you | PASS | Heinlein 1961 | meaning paraphrased, labelled so |
| 9 | B10 | Viewer prompt: "What do I only think I understand? Quiz me on a case I haven't seen." | EXEMPT | Handoff prompt, not a factual claim | — |
