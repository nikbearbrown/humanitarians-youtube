# SOURCES: Why Autoscalers Need Yesterday's Traffic

- Project code and results: https://github.com/lakshdhamija/rl-autoscaler, commit 8b126bd (2026-11-08),
  "Add autoscaling environment, real Azure traffic, fitted generator and baselines".
- Data: Azure Functions Trace 2019, https://github.com/Azure/AzurePublicDataset, CC-BY 4.0.
  Shahrad et al., "Serverless in the Wild: Characterizing and Optimizing the Serverless Workload at a Large
  Cloud Provider", USENIX ATC 2020. Processed by the repo into `data/azure2019_http_apps.csv.gz`.
- Recorded runs (this folder): `evidence/demo_stdout.txt` (`python scripts/demo.py`, 28 s, Python 3.11.15),
  `evidence/pytest_stdout.txt` (13 passed), `evidence/env.txt` (numpy, gymnasium, matplotlib versions),
  `evidence/demo.png` (the repo's own figure, regenerated here; not used on screen).
- Curves and counts on screen: `evidence/make_evidence.py` -> `evidence/evidence.json`, embedded into `scenes.py`.
  Deterministic: no random draws in the data used by this video.
- Toolkit: brutalist.art commit 3a6d3979 (Fellow Tier ai-explainer, hai persona, Kokoro af_bella).
- Logos: Azure, Kubernetes, Colab from `brutalist.art/icons/logos/`; HAI mark from `brutalist.art/logos/humanitarians/`.
