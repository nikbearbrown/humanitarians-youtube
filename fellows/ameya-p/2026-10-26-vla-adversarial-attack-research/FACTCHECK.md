# FACTCHECK â€” week6 (Oct 26) (Security in Physical AI)

Every claim the narration makes, mapped to the source document:
`D:/Ameya/Career/Humanitarians AI/humanitarians-youtube/fellows/ameya-p/2026-10-26-vla-adversarial-attack-research/work_report.md`
("Security & Exploitation in Physical AI: Stealthy Trajectory Steering & Spatial Consistency Verification in VLA Models").

## B00 â€” Cold open

- **"In static image classification, a tiny perturbation only has to fool a single frame. But in a closed-loop robot running at 20 Hz, can a visual patch smoothly steer a clean Vision-Language-Action model toward a decoy object without touching the user's prompt?"**
  Source Â§2: "In classical image classification, an adversarial perturbation only needs to fool a model on a single static frame. In a closed-loop robotic system running at 20 Hz, as soon as an attack nudges the robot arm at Step 1, the camera viewpoint shifts at Step 2, breaking static perturbations... Smoothly and stealthily steering a clean, unpoisoned, standard VLA model to execute an attacker-chosen multi-step trajectoryâ€”without modifying the user's text prompt or poisoning training dataâ€”remains largely unsolved."

## B01 â€” BLUF

- **"Across 23 recent papers, existing visual patches on standard VLA models only make the robot arm freeze, twitch, or miss. Smoothly hijacking a clean model's multi-step trajectory requires tricking its semantic object representationâ€”not forcing raw motor actions."**
  Source Â§2 & Â§3: "A survey of 23 recent papers (2024â€“2026)... Almost all existing test-time visual attacks on VLA models only induce untargeted failures or static action states (causing the robot arm to freeze, twitch in place, or miss an object)." Source Â§3: "(1) Semantic Object-Identity Swap Steering (tricking the vision-language representation rather than forcing raw `[dx, dy, dz]` motor outputs at every frame)."

## B02 â€” Two-Stage Simulation Pipeline on LIBERO & OpenVLA-7B

- **"Following peer feedback from Dev, we eliminated fragile coordinate matching and designed a two-stage simulation pipeline on LIBERO and OpenVLA-7B. During training, differentiable Kornia homography warps a tabletop coaster patch across camera angles; at test time, native MuJoCo rendering evaluates closed-loop control alongside our spatial consistency shield."**
  Source Â§3: "Standardized the testbed exclusively on `LIBERO` (`LIBERO-Object` and `LIBERO-Spatial`) using the official fine-tuned checkpoints (`openvla-7b-finetuned-libero-object` and `-spatial`), explicitly separated differentiable `kornia` homography warping (during patch training) from native `MuJoCo` 3D coaster rendering (during rollout evaluation)..."

## B03 â€” Vision-Encoder Shortcut (GPU Memory Reduction)

- **"OpenVLA computes its 256 visual tokens inside a 0.6B parameter vision encoder before the 7B parameter Llama-2 backbone. By targeting the vision encoder directly, we cut training memory from ~16 GB down to ~4 GB."**
  Source Â§3 ("Way 2 â€” The Auto-Feature Copy Patch"): "Because `OpenVLA`'s 256 visual tokens are produced by the `SigLIP + DINOv2` vision encoder (~0.6B parameters) before the 7B `Llama-2` backbone, Way 2 can be trained in ~3â€“4 GB of GPU VRAM 5â€“10x faster." (Standard 7B bf16/fp16 backprop requires ~16 GB VRAM).

## B04 â€” Two Attack Mechanisms & 3x3 Covering Grid Shield

- **"Dev noted that 5 random masks often miss a small patch or let the poisoned view win a median vote. So we upgraded our shield to a systematic 3x3 covering grid with two-round minority verification and a 3-step persistence rule to keep false positives below 5% per episode."**
  Source Â§3 ("Upgrading the Defense from Random Masking to Systematic Grid + Two-Round Verification"): "Dev pointed out that with 5 random 10%â€“15% masks, most views still contain a small adversarial patchâ€”meaning a naive median vote actually selects the attacked action, and random masks frequently miss the patch altogether. To address this, we kept Method 1 (Naive Random 5-View Masking) as a baseline and added Method 2 (Systematic 3x3 Covering Grid + Two-Round Minority Check, extending PatchCleanser to closed-loop control)... We also calibrated false-positive rates per full episode (<5%) with a 3-consecutive-step persistence rule..."

## B05 â€” 6-Week Two-Engineer Execution Plan

- **"Weeks 1â€“3 build the shared LIBERO harness, PyTorch attention hooks, and Kornia patch trainer. Weeks 4â€“6 split into parallel tracks to benchmark Attention Magnet, Auto-Feature Copy, and the combined patch on Targeted Steering Success Rate and kinematic jerk."**
  Source Â§4 ("Finalized Two-Engineer Execution Plan (Weeks 1â€“6)"): "the codebase development is shared in Weeks 1â€“3 and split by attack mechanism (Way 1: Attention Magnet vs. Way 2: Auto-Feature Copy vs. Combined Way 1 + Way 2) in Weeks 4â€“6... using Targeted Steering Success Rate (TSSR) and Kinematic Smoothness (`jerk`)."

## B06 â€” Your Turn Handoff

- Suggested prompt for the viewer to attach PyTorch forward hooks to `openvla-7b-finetuned-libero-object` and inspect the `16x16` visual token grid.

## B07 â€” Outro

- Title restate only (`week6 (Oct 26).` / `Security in Physical AI`).
