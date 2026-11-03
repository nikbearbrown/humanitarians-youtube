# SOURCES — Microduck and Sim-to-Real Training

Brief supplied by the requester (Likhith), 8 points; each checked against the references below (2026-10-22).

- Pollen Robotics, "Microduck — a tiny biped robot you can teach new tricks" — https://pollen-robotics.com/microduck/ (25 cm, 800 g, 15 motors; $399 introductory price before taxes and shipping, preorders from Aug 27, 2026; SDK, simulation and full RL training stack on GitHub under Apache-2.0; presented with Hugging Face; Pollen's own training path names MuJoCo).
- Pollen Robotics, "Meet Microduck" — https://pollen-robotics.com/microduck/blog/introducing-microduck/
- Tech Times, "Sim-to-Real Gap Narrowed for $399 Duck Robot: Isaac Lab 3.0 Proves Pure-Simulation Training Works", Oct 22, 2026 — https://www.techtimes.com/articles/329379/20261022/sim-real-gap-narrowed-399-duck-robot-isaac-lab-30-proves-pure-simulation-training-works.htm (joint NVIDIA + Pollen tutorial on Hugging Face; 4,096 simulated environments on a single GPU; up to 1.25 M sim steps/s; flat ground, stairs, slopes, rough terrain and push perturbations; export to TorchScript + ONNX; ONNX copied to the robot unmodified; RK3566 runs it at 50 Hz; 61 observations in, 14 joint targets out).
- RuntimeWire, "Pollen Robotics gives its $399 Microduck an Isaac Lab gait-training path" — https://runtimewire.com/article/pollen-robotics-microduck-isaac-lab-sim-to-real-training (4,096-environment recipe, ONNX export, deployment; "the GPU requirement and real-world transfer still set the practical limits").
- KSL / Reuters, "Nvidia's Huang hails Europe's AI potential, flanked by robot ducks" — https://www.ksl.com/article/51639111/nvidias-huang-hails-europes-ai-potential-flanked-by-robot-ducks
- Yahoo News UK, "A protester and a robot duck hiccup: 2 moments from Jensen Huang's keynote didn't go to plan" — https://uk.news.yahoo.com/protester-robot-duck-hiccup-2-131742328.html (Berlin keynote, Wed Oct 21, 2026; four Microducks; "take a nap"; one robot wandered off and tripped).
- Pasquale Pillitteri, "Huang Unveils Microduck Robots at GTC Berlin, Trained With RTX Spark" — https://pasqualepillitteri.it/en/news/26263/huang-unveils-microduck-robots-gtc-berlin-rtx-spark (sit / stand / nap; 3 of the 4 fell over immediately when told to nap).
- Pollen Robotics on X — https://x.com/pollenrobotics/status/2112892178535985356 ("Microducks on stage for Jensen Huang's famous keynote").
- Logo: `icons/logos/pollen-robotics/pollen-robotics-01.svg` from https://pollen-robotics.com/assets/pollen-logo-icon.svg (new library folder; PNG rasterised with Quick Look). NVIDIA and Hugging Face marks from the existing library.

## Evidence (executed, not typed)
- `evidence/sim_to_real_toy.py` → `sim_to_real_toy.out.txt` — numpy, seed 7. NOT the Microduck stack: 4,096 parallel inverted pendulums (a stand-in for "stay upright"), randomized mass/length, random shoves, a two-gain policy improved by random search over 30 rounds. 12,649 falls, all reset; falls per round 2,925 → 80; final policy 97.6% upright in fresh randomized sims. B07 shows these numbers and is captioned "toy run". A first version also "deployed" to a delayed "real" pendulum; it showed no meaningful gap, so that leg was removed rather than tuned.

## Corrections / de-sensationalising
- Point 1 "October 2026 keynote": specified as GTC Berlin, Oct 21, 2026 (on screen). Narration says "Nvidia's keynote".
- Point 4 "walking, balancing, and traversing obstacles": the published recipe trains on flat ground, slopes, stairs, rough terrain and shoves; obstacle avoidance is not described. On screen: flat · slopes · stairs · rough · shoves.
- Point 4 "using NVIDIA Isaac Lab": correct for the joint NVIDIA + Pollen tutorial (Isaac Lab 3.0). Pollen's own default stack trains in MuJoCo; the reel does not claim Isaac Lab is the only path.
- Point 4 "thousands of times": 4,096 parallel copies is the published figure; per-copy retry counts are not published, so the B07 counts come from the labelled toy run.
- Point 7: 3 of 4 fell when told to nap ("take a nap" = lie down). The narration says sim "still isn't the real world"; the specific causes on stage are not known, so B08 lists "typical gap sources", not a diagnosis.
- Point 8 "becoming the standard": kept as "becoming", not "is".
- NVIDIA's recap also credits AI agents on RTX Spark laptops for the training workflow; left out for time, not contradicted.
