# SHOTLIST -- cli-deploy-runner
## Deploy a Keyword Spotter: Find the Layer That Leaked Accuracy

| Beat | Source | Duration | Description |
|------|--------|----------|-------------|
| B00  | remotion | 3.6s | NikBearBrownOpen -- Deploy runner, taken apart |
| B01  | manim | 30.1s | B01_Problem -- 94% vs 91% accuracy, toolchain vs quant loss |
| B02  | remotion | 18.9s | NikBearBrownTerminalAsk -- deploy_runner.py prompt |
| B03  | remotion | 23.1s | NikBearBrownCodeBlock -- deploy_runner.py bisect code |
| B04  | manim | 21.6s | B04_Deploy -- per-layer divergence bars, layer 7 spike (illustrative) |
| B05  | remotion | 10.5s | NikBearBrownTerminalAsk -- add CMSIS-NN op check |
| B06  | manim | 22.8s | B06_DeployOp -- OK/FALLBACK chips, CMSIS-NN fallback (illustrative) |
| B07  | manim | 21.3s | B07_Summary -- lesson card |
| B08  | manim | 24.2s | B08_NextSteps -- action items |
| B09  | remotion | 6.9s | NikBearBrownOutro |

**Total: 183.0s (~3:03)**

---

NOTE: B04 and B06 use synthetic/illustrative data.
Swap manim/B04.mp4 and manim/B06.mp4 with a real capture once
a trained keyword-spotter model (Keras or TFLite) and a validation set are available
to run the real TFLite conversion + interpreter bisection.
