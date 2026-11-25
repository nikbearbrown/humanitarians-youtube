Name ten words, as different from each other as you can. That's a real creativity test, the Divergent Association Task (DAT). One researcher made it the reward for training a 27-billion-parameter model. Did the model get more creative, or just better at the test?

This week's second reel walks through Sasha Savsunenko's "Inducing creativity in LLM models" (Nov 5, 2026), and checks it against his own raw data.

How the test scores. Seven words that come easily (cat, dog, horse, cow, sheep, pig, goat) score 42. Seven far apart (volcano, spoon, justice, violin, glacier, receipt, tiger) score 87. The math is two lines: seven words make 21 pairs, and the score is 100 times their average distance in GloVe, a map of word meanings learned from a crawl of the web (Olson et al., PNAS 2021).

The experiment. A Qwen3.8-27B model wrote word lists and was reinforced (GRPO) for higher scores, minus a penalty for words of the wrong type. Nouns and verbs in training; adjectives held back as a test. The weights are open.

We re-scored all 192 of his raw word lists with the official scorer; every one matches his numbers:
- Nouns: 71.8 → 89.6
- Verbs: 51.1 → 85.2
- Held-out adjectives: 60.7 → 86.3

But asked for adjectives after training, it wrote: endpoint, biblical, bark, mule, contour, demon, suture, crumb, staple, gavel. Only "biblical" and "staple" can be adjectives. Lists made entirely of adjectives fell from 29 of 32 to 1 of 32 (our WordNet check matches his). The score rose partly by bending the instruction, and his own repo says so.

Did it write better? A strong AI judge (64 story pairs, both orders) rated the stories more creative (+0.70 of 10) and more vivid (+0.62), but less coherent (−0.90). Automatic writing benchmarks saw no gain. Instruction-following (IFEval) fell 3.7 points, from 83.2% to 79.5%.

Verdict: a creativity test makes a good probe, and a leaky reward.

Try it yourself: write ten nouns as different as you can, ask an assistant for its ten, score both at https://www.datcreativity.com, and check whether every one of the assistant's words is still a noun.

Chapters:
0:00 Ten words, as different as you can
0:14 How the test scores
0:31 The whole score, in two lines
0:46 The experiment
1:05 We re-scored it
1:22 Asked for adjectives
1:40 Did it write better?
1:56 Verdict
2:11 Your turn: your ten words
2:22 Outro

Sources:
Sasha Savsunenko, "Inducing creativity in LLM models" — https://crazylog.substack.com/p/inducing-creativity-in-llm-models
Code, raw results and figures (MIT) — https://github.com/crazyleg/dat-grpo-creativity
Model — https://huggingface.co/crazyleg11/qwen3.8-27b-dat-grpo-full250
Olson et al., "Naming unrelated words predicts creativity", PNAS 2021 — https://doi.org/10.1073/pnas.2022340118
DAT scorer (MIT) — https://github.com/jayolson/divergent-association-task
GloVe — https://nlp.stanford.edu/projects/glove/

Images:
Figures — Sasha Savsunenko, MIT
Model card screenshot — Hugging Face, crazyleg11
Word photos (Wikimedia Commons):
Bark — Gregory Schick aka leadgolem, Public domain, Wikimedia Commons
Cat — Dmitry Makeev, CC BY-SA 4.0, Wikimedia Commons
Contour — National Centers for Environmental Prediction, Public domain, Wikimedia Commons
Cow — Dietrich Michael Weidmann, CC BY-SA 3.0, Wikimedia Commons
Crumb — Safa.daneshvar, CC BY-SA 4.0, Wikimedia Commons
Dog — Muldoonsamuel, CC0, Wikimedia Commons
Gavel — perpetual.fostering, CC BY 2.0, Wikimedia Commons
Glacier — Valentinamaur, CC BY-SA 4.0, Wikimedia Commons
Goat — Béria Lima de Rodríguez, CC BY-SA 3.0, Wikimedia Commons
Horse — Jules Verne Times Two, CC BY-SA 4.0, Wikimedia Commons
Justice — DP Singh Bhullar, CC BY-SA 4.0, Wikimedia Commons
Mule — Unknown authorUnknown author, Public domain, Wikimedia Commons
Pig — Gzen92, CC BY-SA 4.0, Wikimedia Commons
Receipt — Bernd Schwabe, CC BY-SA 4.0, Wikimedia Commons
Sheep — Rude Health, CC BY-SA 2.0, Wikimedia Commons
Spoon — Silar, CC BY-SA 4.0, Wikimedia Commons
Staple — Jacek Halicki, CC BY-SA 4.0, Wikimedia Commons
Suture — Saltanat ebli, CC0, Wikimedia Commons
Tiger — Luis Miguel Bugallo Sánchez (Lmbuga), CC BY-SA 3.0, Wikimedia Commons
Violin — David Schou, CC BY-SA 4.0, Wikimedia Commons
Volcano — Giles Laurent, CC BY-SA 4.0, Wikimedia Commons

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the formula typeset locally as SVG. The DAT scores were recomputed on a MacBook Pro with the official scorer and GloVe 840B; the judge and benchmark numbers are the author's. No image was generated. No human-performed audio or video.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: creativity, Divergent Association Task, DAT, reinforcement learning, GRPO, reward hacking, Goodhart's law, Qwen, LLM fine-tuning, word embeddings, GloVe, LLM as a judge, creative writing, AI evaluation, Humanitarians AI, Computational Skepticism

#AI #Creativity #ReinforcementLearning #LLM #RewardHacking #OpenSource #HumanitariansAI #ComputationalSkepticism
