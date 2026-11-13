# FACTCHECK — Microduck and Sim-to-Real Training

Status: claims checked by Claude Code against the sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | At NVIDIA's keynote (GTC Berlin, Oct 21, 2026), Huang told four ducks: sit, stand, take a nap | PASS | Yahoo/KSL/Pillitteri | Event + date on screen |
| 2 | B03 | 25 cm, $399, open-source biped from Pollen Robotics + Hugging Face, 15 motors, retrainable RL stack | PASS | pollen-robotics.com/microduck | "$399 preorder, before tax + shipping" |
| 3 | B04 | Sim-to-real: learns in a physics simulation, not on fragile hardware | PASS | Pollen; NVIDIA/Pollen tutorial | — |
| 4 | B05 | Isaac Lab: thousands of copies at once (4,096, one GPU, ≤1.25 M steps/s); fall, reset, retry | PASS (corrected) | Tech Times / RuntimeWire | "obstacles" → slopes/stairs/rough/shoves |
| 5 | B06 | Policy exported (ONNX) and loaded onto the real robot's motors | PASS | Tech Times: ONNX, unmodified, 50 Hz, 61 in / 14 out | — |
| 6 | B07 | Thousands of real falls would wreck hardware; in sim a fall costs nothing | PASS (judgment + toy) | toy run: 12,649 falls, $0 | captioned "toy run" |
| 7 | B08 | Told to nap, 3 of 4 toppled; sim still isn't real | PASS | Pillitteri; Yahoo | gap list labelled "typical", not a diagnosis |
| 8 | B09 | Simulate at scale, then transfer, is becoming physical AI's standard in 2026 | PASS (judgment) | Tutorial + industry framing | "becoming", not "is" |
| 9 | B10 | Viewer prompt: "What should my robot practice in sim, and what will the sim get wrong?" | EXEMPT | Handoff prompt for the viewer, not a factual claim | — |
