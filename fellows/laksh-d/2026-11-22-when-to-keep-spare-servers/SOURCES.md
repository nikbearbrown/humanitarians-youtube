# SOURCES: When to Keep Spare Servers

- Project code and results: https://github.com/lakshdhamija/rl-autoscaler @ a886c1b (2026-11-22):
  `train.py` (Headroom, HEADROOM_TARGETS, WEEKLY, real_traffic with misleading history), `policies.py` (ThresholdPolicy = HPA),
  `env.py`, `scripts/frontier.py --hpa` (rule_late_at), `scripts/stress.py`, `scripts/modal_train.py --batch hpa`,
  `results/ppo-hpa/*.json` (30 runs), `results/stress-hpa.json`; README sections "RL sets HPA's target", "Limits", "Plan".
- Data: Azure Functions Trace 2019, https://github.com/Azure/AzurePublicDataset, CC-BY 4.0 (Shahrad et al., USENIX ATC 2020).
  Huawei Cloud traces 2023, https://github.com/sir-lab/data-release, CC BY 4.0 (Joosen et al., ACM SoCC 2023), via `scripts/prepare_huawei.py`.
- Training: Stable-Baselines3 PPO on Modal CPUs, 3M steps per run.
- Recorded runs (this folder): `evidence/pytest_stdout.txt` (21 passed, at a886c1b).
- Numbers and curves on screen: `evidence/make_evidence.py` -> `evidence/evidence.json`, embedded into `scenes.py`. Deterministic;
  it refuses to run on uncommitted repo changes and asserts every number against the brief.
- Chart in B05: redrawn natively from the evidence numbers; `results/frontier-hpa.png` was the reference.
- Toolkit: brutalist.art commit 3a6d3979 (Fellow Tier ai-explainer, hai persona, Kokoro af_bella).
