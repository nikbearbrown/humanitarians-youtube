# SOURCES: When History Misleads

- Project code: https://github.com/lakshdhamija/rl-autoscaler @ a886c1b ("Add Huawei multi-week traces and a PPO agent
  that sets HPA's target", 2026-11-22): `scripts/stress.py` (the six history changes, HPA under the same change),
  `scripts/frontier.py` `rule_late_at` (HPA's late requests at the same cost), `src/rl_autoscaler/train.py`
  (`real_traffic` with `bad_days`, `Headroom`, `HEADROOM_TARGETS`, `WEEKLY`), `src/rl_autoscaler/env.py` (`_obs`),
  `src/rl_autoscaler/policies.py` (`ThresholdPolicy`), results `results/stress-hpa.json`, `results/ppo-hpa/*.json`.
- Data: Azure Functions Trace 2019, https://github.com/Azure/AzurePublicDataset, CC-BY 4.0 (Shahrad et al., USENIX ATC 2020).
  Huawei Cloud traces 2023, https://github.com/sir-lab/data-release, CC BY 4.0 (Joosen et al., "How Does It Function?",
  ACM SoCC 2023). The example day in B02 and B03 is Azure app ec941895, day 12 (an unseen test day).
- Domain randomization: Tobin et al., "Domain Randomization for Transferring Deep Neural Networks from Simulation to the
  Real World", IROS 2017 (arXiv:1703.06907). Used here only for the term; the method on screen is the repo's own.
- HPA rule: Kubernetes Horizontal Pod Autoscaler documentation (desired replicas = ceil(current x current metric / target)),
  as implemented in `policies.py`.
- Numbers on screen: `evidence/make_evidence.py` -> `evidence/evidence.json`, embedded into `scenes.py` and
  `vertical/scenes.py`. Deterministic; it asserts the expected counts and stops on any difference.
- Toolkit: brutalist.art commit 3a6d3979 (Fellow Tier ai-explainer, hai persona, Kokoro af_bella).
- Corrections during the build: the brief said HPA "is not affected" by changed history. HPA reads no history, but a
  changed yesterday still reaches it at midnight through the day's starting servers, so the video says "HPA reads no
  history" and "never fooled by history", not "unaffected".
