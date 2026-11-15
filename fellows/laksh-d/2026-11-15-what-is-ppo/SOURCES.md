# SOURCES: What PPO Is, In Plain Words

- Running example: https://github.com/lakshdhamija/rl-autoscaler, commit 8b126bd, `src/rl_autoscaler/env.py`
  (observation of 25 numbers, 11 actions, reward line).
- Algorithm: Schulman, Wolski, Dhariwal, Radford, Klimov, "Proximal Policy Optimization Algorithms", OpenAI, 2017,
  arXiv:1707.06347 (clipped objective, eq. 7).
- Defaults: stable-baselines3 2.9.2 as installed in the rl-autoscaler venv (`PPO.__init__`, `PPO.train`,
  `ActorCriticPolicy`); recorded in `evidence/facts_stdout.txt` by `evidence/check_facts.py`.
- Toolkit: brutalist.art commit 3a6d3979 (Fellow Tier ai-explainer, hai persona, Kokoro af_bella).
- Logos: OpenAI from `brutalist.art/icons/logos/openai/`; HAI mark from `brutalist.art/logos/humanitarians/`.
