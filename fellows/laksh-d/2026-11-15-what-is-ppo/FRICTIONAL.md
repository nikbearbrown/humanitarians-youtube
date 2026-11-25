# Frictional Log

## 2026-11-11: What PPO is, in plain words

- **Work and expectation:** explain Proximal Policy Optimization (PPO), the algorithm my autoscaler trains with, on my own environment. I expected the usual short descriptions of PPO to be accurate enough for the narration.
- **What I tried:** checked every number on screen against the installed Stable-Baselines3 2.9.2 and my `env.py` with one script (`evidence/check_facts.py`), and the objective against Schulman et al. 2017.
- **Where it resisted:**
  - Common phrasings overstate PPO. "An update cannot wreck the policy" and "the ratio stays between 0.8 and 1.2" are not true: the objective is clipped, so a single update is less likely to move the policy far, but nothing forces the ratio to stay in that range. The narration and the screen now say "clipped to".
  - The voice read the letter "A" (the advantage) as the word "a". The line is respelled so it is said as a letter.
  - A preview step of the toolkit downloaded a 171 MB browser into the toolkit folder. I removed it and used the browser the toolkit already uses for final renders.
- **AI and other contributions:** Claude Code wrote the narration and scenes and rendered the video; I chose the topic and asked for the two accuracy fixes after reviewing the preview. Narration is an AI voice (Kokoro `af_bella`).
- **What I understand now:** PPO's key idea is the size of each update. If RL training suddenly collapses, the size of each update is the first thing to check.
- **Evidence:** [README](README.md#watch-and-review), [FACTCHECK.md](FACTCHECK.md), [evidence/facts_stdout.txt](evidence/facts_stdout.txt)
