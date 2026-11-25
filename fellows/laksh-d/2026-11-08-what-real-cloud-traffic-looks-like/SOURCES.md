# SOURCES: What Real Cloud Traffic Looks Like

- Project code: https://github.com/lakshdhamija/rl-autoscaler, commit 8b126bd (2026-11-08).
- Data: Azure Functions Trace 2019, https://github.com/Azure/AzurePublicDataset, CC-BY 4.0. Shahrad et al.,
  "Serverless in the Wild: Characterizing and Optimizing the Serverless Workload at a Large Cloud Provider",
  USENIX ATC 2020. Processed by the repo into `data/azure2019_http_apps.csv.gz`.
- Recorded runs: `evidence/demo_stdout.txt` (`python scripts/demo.py`, Python 3.11.15), `evidence/pytest_stdout.txt`,
  `evidence/env.txt`.
- Curves and counts on screen: `evidence/make_evidence.py` -> `evidence/evidence.json`, embedded into `scenes.py`.
  Random draws: B05 random times (numpy default_rng(0)); B07 redrawn made-up noise (default_rng(1)) and
  FittedTraffic day (default_rng(3)).
- Toolkit: brutalist.art commit 3a6d3979 (Fellow Tier ai-explainer, hai persona, Kokoro af_bella).
- Logos: Azure, Kubernetes from `brutalist.art/icons/logos/`; HAI mark from `brutalist.art/logos/humanitarians/`.
