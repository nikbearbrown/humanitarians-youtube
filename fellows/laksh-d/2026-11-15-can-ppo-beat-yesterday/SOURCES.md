# SOURCES: Can PPO Beat Yesterday?

- Project code and results: https://github.com/lakshdhamija/rl-autoscaler, commit 35e922d (2026-11-15),
  "Train PPO agents on Modal: plain and residual". PPO results: `results/ppo/*.json` (30 runs).
- Data: Azure Functions Trace 2019, https://github.com/Azure/AzurePublicDataset, CC-BY 4.0.
  Shahrad et al., "Serverless in the Wild: Characterizing and Optimizing the Serverless Workload at a Large
  Cloud Provider", USENIX ATC 2020. Processed by the repo into `data/azure2019_http_apps.csv.gz`.
- Training: Stable-Baselines3 2.9.2 PPO, run on Modal CPUs (`scripts/modal_train.py`).
- Recorded runs (this folder): `evidence/pytest_stdout.txt` (17 passed).
- Numbers and curves on screen: `evidence/make_evidence.py` -> `evidence/evidence.json`, embedded into `scenes.py`.
  Deterministic: no random draws.
- Toolkit: brutalist.art commit 3a6d3979 (Fellow Tier ai-explainer, hai persona, Kokoro af_bella).
- HAI mark from `brutalist.art/logos/humanitarians/`.
