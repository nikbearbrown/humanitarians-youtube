# Experiment Plan: Stealthy Object-Swap Steering & Spatial Consistency Shielding in VLA Models

This readme focuses on an experimental plan, combining the following 2 hypotheses, on **Vision–Language–Action (VLA) Models** for **Physical AI**:

1.  _Hypothesis 1: Existing visual patch attacks on VLAs mostly cause the robot arm to freeze, twitch, or fail its task because they try to force raw low-level motor commands (`[dx, dy, dz]`) at every frame, which breaks as soon as the arm moves and the camera angle shifts. Instead, if we optimize a 3D tabletop patch/texture to hijack where the VLA grounds the user's instruction—without needing prior knowledge of where Object A or Object B are located, via either an Attention Magnet Patch or an Auto-Feature Copy Patch—the robot’s own closed-loop controller will smoothly and naturally steer the arm across the entire trajectory to grasp whatever decoy object sits next to the patch._
2.  _Hypothesis 2: When a VLA robot executes a genuine task grounded in a real physical object, masking out small background regions of the camera frame does not significantly change where the robot plans to move next. However, when a robot is being stealthily steered by an adversarial patch or localized perturbation, masking out the region containing the perturbation causes the predicted trajectory to snap back toward the true object. Measuring action consistency across masked views of the same frame at runtime—comparing random multi-view masking against systematic grid masking—can detect and neutralize stealthy steering without retraining the VLA._

## Minimizing Impact of Simulation Limitations on this study

Robotics studies often lose credibility in simulation when they rely on unrealistic contact physics (such as idealized friction) or "digital pixel cheating" (modifying 2D image arrays directly in code).
This experimental study is designed to avoid those pitfalls in three specific ways:

1. **Focus on Official Fine-Tuned VLA Weights:** We evaluate the official pre-trained, open-weight `OpenVLA-7B` checkpoints fine-tuned for the LIBERO benchmark (`openvla-7b-finetuned-libero-object` and `openvla-7b-finetuned-libero-spatial`). The vulnerability and defense operate in the vision-language representation and action-selection layers, not in hardware-specific motor drivers.
2. **Targeting High-Level Object Identity Rather Than Millimeter Contact Physics:** The attack does not rely on exploiting simulator friction or delicate collision glitches. Once the VLA's perception layer is tricked into mapping the target instruction to the wrong object, the model’s own normal closed-loop controller smoothly guides the arm to grasp it - just as it does in a normal task.
3. **Two-Stage 3D Scene Placement (Honest 3D Projection & Native Rendering):** Because `MuJoCo`'s built-in renderer is not directly differentiable, we separate patch optimization from evaluation. During patch optimization, we use a differentiable perspective warp (homography based on known 3D table coordinates and camera poses) to project the flat patch onto the scene so gradients can flow. During evaluation rollouts, we load the finished patch directly onto a 3D coaster/surface inside `MuJoCo`'s native renderer with no 2D overlay.

---

## Experiment Execution Plan

### 1. Shared Testbed Setup (Used Across Both Hypotheses)

- **Simulation Environment (LIBERO):**
  - What it is: `LIBERO` is an open-source tabletop manipulation benchmark built on the `MuJoCo` physics engine with a simulated 7-joint Franka Emika Panda robot arm.
  - How it works: At each control step (20 Hz), `LIBERO` provides a $224 \times 224$ RGB camera frame of the workspace. The VLA model takes the camera frame and text instruction and outputs a 7-DoF motor action vector (`[dx, dy, dz, droll, dpitch, dyaw, gripper]`), which `LIBERO` executes to advance the physics state.
  - Why it fits this experiment: Its built-in task suites (`LIBERO-Object` and `LIBERO-Spatial`) naturally place a target object alongside multiple distractor objects on the same table, providing ready-made two-object scenes without custom 3D world building.
- **Victim Model:** `OpenVLA-7B` using the official LIBERO-finetuned checkpoints (`openvla-7b-finetuned-libero-object` and `-spatial`, frozen clean weights - no training-time data poisoning).
- **Task Scenes & Two-Method Scaling:**
  In a realistic setting, an attacker placing a coaster on a table does not know where Object A or Object B will be placed, or even which object the user will ask for. Instead of relying on ground-truth simulator coordinates for Object A and Object B, our code only knows the grid squares covered by our own patch. Our hypothesis compares two "blind" steering methods:
  - _Method A — The "Attention Magnet" Patch:_
    - How it works: Trains the patch across diverse scenes and prompts inside `OpenVLA`’s `Llama-2` cross-attention layers with one rule: maximize the text-to-image attention score on the patch’s own squares (pushing it toward $100\%$) for whatever words are in the user's prompt.
    - Result: The patch acts like a universal visual magnet. Wherever the patch is placed next to a Decoy Object B, `OpenVLA` focuses its attention on the patch and smoothly steers the arm to grasp Decoy B—without ever needing to know what or where Object A is.
  - _Method B — The "Auto-Feature Copy" Patch (Built by Engineer 2):_
    - How it works: Uses `OpenVLA` itself to find Object A automatically on Frame 1 (by selecting whichever 3–4 grid squares naturally receive the highest attention on the clean image), averages their visual token ID numbers (`mean(tokens_A)`), and uses the Vision-Encoder to train the patch’s own squares to copy that average visual ID vector.
    - Result: The patch disguises its own squares with the visual appearance ID of the target object without needing simulator bounding boxes or manual coordinate matching.
- **User Instruction:** Fixed and completely benign. The attacker never edits the user’s text command.

---

### 2. Plan for Hypothesis 1 (The Attack): Stealthy Steering via Attention Magnet & Auto-Feature Copy

> **Hypothesis 1:** _Existing visual patch attacks on VLAs mostly cause the robot arm to freeze, twitch, or fail its task because they try to force raw low-level motor commands (`[dx, dy, dz]`) at every frame, which breaks as soon as the arm moves and the camera angle shifts. Instead, if we optimize a 3D tabletop patch/texture to hijack where the VLA grounds the user's instruction—without needing prior knowledge of where Object A or Object B are located, via either an Attention Magnet Patch or an Auto-Feature Copy Patch—the robot’s own closed-loop controller will smoothly and naturally steer the arm across the entire trajectory to grasp whatever decoy object sits next to the patch._

#### Execution Steps:

- Step 1 — Record Clean Rollouts & Build Shared Extractors:
  Run 10–20 clean, unattacked rollouts across tasks in `LIBERO-Object` and `LIBERO-Spatial`. Record `OpenVLA`'s internal post-projector visual token embeddings ($16 \times 16$ grid of 256 visual tokens from fused `SigLIP + DINOv2`) and `Llama-2` text-to-image cross-attention maps.
- Step 2 — Optimize the Two "Blind" Patch Methods (Only Updating the Patch's Own Squares):
  Place a small patch on the 3D table plane using differentiable perspective warping. Crucially, the optimizer never looks up simulator coordinates for Object A or Object B—it only operates on the grid indices covered by the patch itself:
  - _Attention Magnet" Patch:_ Optimize the patch across multiple prompts and random table placements to maximize `Llama-2` cross-attention from the instruction tokens directly onto the patch's spatial grid squares.
  - _Auto-Feature Copy Patch:_ On clean frames, automatically take the mean visual embedding of the top-3 highest-attention squares (where `OpenVLA` naturally sees Object A), and train the patch's squares to minimize cosine/$L_2$ distance to that pooled target vector. Because those 256 visual tokens are produced by the vision encoder + projector (~0.6B parameters) \_before\_ entering `Llama-2-7B`, Way 2 can be trained in ~3–4 GB of GPU VRAM $5\text{–}10\times$ faster.
- Step 3 — Full Closed-Loop Rollout Evaluation:
  Bake the finished patches directly onto the 3D coaster next to Decoy B in `MuJoCo`, reset the robot to random starting poses, issue the benign user prompt, and let the robot execute a full closed-loop rollout (up to 100–200 control steps) using native `MuJoCo` rendering across both `LIBERO-Object` and `LIBERO-Spatial`.
- Step 4 — Benchmark Against Baselines & Compare Attack Mechanisms:
  Compare Attention Magnet and Auto-Feature Copy against standard motor-level adversarial patches (_TMA_-style, which directly optimize motor output discrepancy) and untargeted feature-disruption patches (_EDPA_-style, which globally scramble visual-textual alignment).
  - Key Metrics:
    1. Targeted Steering Success Rate (TSSR): Percentage of episodes where the robot smoothly grasps _Decoy B_ next to the patch (comparing Way 1 vs. Way 2 vs. Combined).
    2. Zero-Shot Prompt/Scene Transferability: How well the Universal Attention Magnet (Way 1) steers the robot on unseen prompts and across both `LIBERO-Object` and `LIBERO-Spatial`.
    3. Kinematic Stealthiness (Smoothness): Comparison of velocity and acceleration profiles (`jerk`) against normal unattacked demonstrations to verify the trajectory looks completely natural.

---

### 3. Plan for Hypothesis 2 (The Defense): Runtime Prevention via "Spatial Consistency Shield"

> **Hypothesis 2:** _When a VLA robot executes a genuine task grounded in a real physical object, masking out small background regions of the camera frame does not significantly change where the robot plans to move next. However, when a robot is being stealthily steered by an adversarial patch or localized perturbation, masking out the region containing the perturbation causes the predicted trajectory to snap back toward the true object. Measuring action consistency across masked views of the same frame at runtime—comparing random multi-view masking against systematic grid masking—can detect and neutralize stealthy steering without retraining the VLA._

#### Execution Steps:

- Step 1 — Build Two Masking Variants Wrapper (Random vs. Systematic Grid):
  Create a lightweight inference wrapper around OpenVLA that replaces masked regions with neutral tabletop color/local blur (or masks the corresponding ViT tokens directly, avoiding harsh black-box edges that push the vision encoder off-distribution). We implement and compare two masking designs:
  - _Method 1 (Naive Random 5-View Masking):_ Generate $N = 5$ copies of the current camera frame, each with a random square ($10\%\text{–}15\%$ of the frame) masked out.
  - _Method 2 (Systematic $3 \times 3$ Grid Masking — Extending PatchCleanser to Closed-Loop Control):_ Divide the tabletop workspace into a fixed, overlapping $3 \times 3$ ($K = 9$) covering grid so that any localized patch is guaranteed to be completely covered in at least one view.
- Step 2 — Compute Batch Action Disagreement:
  Pass all masked frames ($N = 5$ for Method 1, or $K = 9$ for Method 2, evaluated at every step or lazily at $K$-step action-chunk boundaries) through OpenVLA in a single parallel GPU batch. Compute the pairwise distance (variance) among the predicted motor vectors `[dx, dy, dz, gripper]`.
- Step 3 — Calibrate the Per-Episode Safe Threshold ($\tau$) on Clean Tasks:
  Run 50 normal, unattacked rollouts across LIBERO tasks to measure natural variance across the masked views. Because per-step false alarms compound over 100–200 steps, calibrate $\tau$ _per full episode_ and require disagreement to persist across $m = 3$ consecutive steps before raising an alarm (targeting $< 5\%$ false-alarm episodes on clean runs).
- Step 4 — Evaluate Both Shield Methods Under Attack (Detection & Recovery):
  Activate the Spatial Consistency Shield during episodes attacked by _Hypothesis 1 (Object-Swap Steering)_ as well as baseline patch attacks (_TMA_ / _EDPA_). When disagreement persists above $\tau$ for 3 consecutive steps, test two defense modes across both Method 1 and Method 2:
  - Mode A (Safe Stop / Alert): Immediately halt motor execution and flag a perception hijack before the arm reaches Object B.
  - Mode B (Action Recovery — Median vs. Two-Round Minority Check):
    - In _Method 1 (Random Masks)_, execute the spatial median of the agreeing views (testing whether majority voting accidentally favors the attacker when most random views still see the patch).
    - In _Method 2 (Systematic Grid)_, when 1 minority grid view disagrees with the other 8 views, run a _Two-Round Minority Check_: take that 1 disagreeing view (where the patch is covered) and mask one additional grid cell at a time. If the predicted action stays locked onto Object A across the second round, confirm that the minority view removed the patch and execute that recovered action.
  - Key Metrics:
    1. Attack Detection Rate: Percentage of stealthy steering episodes caught before physical contact with Object B (comparing Method 1 vs. Method 2).
    2. Task Recovery Rate (Mode B): Percentage of attacked episodes where the robot successfully recovers and grasps the true target (Object A) under Method 1 (Median) vs. Method 2 (Two-Round Grid Check).
    3. Clean Task Retention & Latency Overhead: Episode-level false positive rate and inference speed impact.

---

## Success Criterion (Target Goals)

_Note: All numerical percentages below serve as target research benchmarks to evaluate how far each method goes, rather than rigid pass/fail cutoffs; characterizing where a method falls short is an equally valuable experimental finding._

### 1. Hypothesis 1 (The Attack): Stealthy Steering via "Object-Identity Swap"

#### Baselines to Compare Against

1. Clean / Unattacked Baseline (No Patch): The robot runs normally with no patch or with a plain, unoptimized coaster on the table (measures normal task completion on Object A and accidental grasping of Object B).
2. Untargeted Feature-Disruption Baseline (_UADA_ / _EDPA_-style): A standard adversarial patch optimized to globally disrupt visual-textual latent alignment or maximize overall action error (which typically makes the robot miss, freeze, or twitch).
3. Motor-Level Targeted Patch Baseline (_TMA_-style): An adversarial patch optimized directly to force low-level motor outputs (`[dx, dy, dz]`) toward Object B at each frame.

#### Target Goals for Hypothesis 1

- Primary Goal — Targeted Steering Success Rate (TSSR): Guide the robot to smoothly reach for and grasp _Decoy B_ (placed next to the patch) with a target benchmark of $\sim 60\%$ of episodes under the benign prompt (_"Pick up Target A"_), aiming to outperform the Motor-Level Targeted Patch baseline (_TMA_) by $25\text{–}30$ percentage points on complete multi-step grasps.
- Comparative Discovery Goal — Attention Magnet (Way 1) vs. Auto-Feature Copy (Way 2) vs. Combined: Quantify whether pulling `Llama-2` cross-attention onto the patch (Way 1), copying pooled target visual features onto the patch (Way 2), or combining both losses yields the strongest closed-loop steering and best transferability across unseen prompts.
- Stealthiness Goal — Kinematic Naturalness: Keep the robot arm's trajectory velocity and acceleration profiles (`jerk` and step-to-step action variance) within $1.2\times$ of clean, unattacked trajectories, avoiding the mid-air stalling, oscillation, or freezing behavior seen in untargeted attacks.

---

### 2. Hypothesis 2 (The Defense): Runtime Prevention via "Spatial Consistency Shield"

#### Baselines to Compare Against

1. Unshielded VLA Baseline: Standard fine-tuned `OpenVLA-7B` running directly on the camera feed with no runtime defense.
2. Single-Frame Input Smoothing Baseline (Gaussian Blur / JPEG Compression): Standard image-level preprocessing applied to the camera frame before feeding it to the VLA.
3. Text / Plan-Level Guardrail Baseline (_RoboGuard_-style): A high-level language/logic checker that only inspects the user prompt and high-level task plan (which is blind to visual identity swaps in the camera feed).
4. Internal Comparison (Method 1 Random 5-View vs. Method 2 Systematic $3 \times 3$ Grid): Direct ablation showing why systematic grid coverage and two-round minority verification outperform naive random masking.

#### Target Goals for Hypothesis 2

- Primary Goal — Attack Detection Rate (Mode A: Safe Stop): Achieve a target goal of $\sim 90\%$ detection and halting of stealthy steering episodes (under Method 2 Systematic Grid) _before_ the robot gripper makes physical contact with Object B, while quantifying how often Method 1 (Random Masks) misses small patches.
- Recovery Goal — Task Completion Under Attack (Mode B: Action Recovery): Demonstrate that while naive median voting (Method 1) can be outvoted by views that still see the patch, Method 2's Two-Round Minority Check recovers the true trajectory and completes the original safe task (_grasping Object A_) with a target goal of $\sim 70\%$ of attacked episodes.
- Usability Goal — Low Episode-Level False Positives & Real-Time Speed:
  - Episode False Positive Rate (FPR): Using the 3-consecutive-step confirmation rule and neutral color/token masking, keep false alarms below $< 5\%$ of full clean episodes.
  - Latency Overhead: By batching masked views on a single GPU and triggering the second-round check lazily only when single-mask disagreement spikes, keep average control-loop latency overhead below $< 25\%$.

---

## Risks & Points of Failure

### 1. Differentiable-render → native-render transfer gap

- **Why it’s likely:** The patch is optimized through a differentiable homography warp (`kornia`), but evaluated in `MuJoCo`’s native rasterizer. Lighting, specularity, antialiasing, and texture sampling differ between the two pipelines, so a patch that works in optimization can weaken materially once baked into the 3D scene.
- **Mitigation:** Two-stage separation of optimization vs. evaluation rendering (`kornia` perspective warp during training → native `MuJoCo` 3D coaster texture during rollout testing), plus configuring the 3D coaster material in the `MuJoCo` XML with flat, non-glossy material properties (`specular="0" shininess="0"`) so `MuJoCo`’s scene lights do not wash out the patch colors with glare.
- **Residual risk:** Antialiasing and texture interpolation differences between `kornia` and `MuJoCo`’s OpenGL rasterizer can still slightly soften high-frequency patch patterns. We will log TSSR both on _PyTorch-warped frames_ and _native `MuJoCo`-rendered frames_ to explicitly measure the renderer transfer drop; if the drop is large, we will add a light Gaussian smoothing filter during training so the patch relies on coarse color blocks rather than single-pixel edges.

### 2. Spatial token correspondence between Object A and Object B

- **Why it’s likely:** A naive feature-swap loss assumes a clean way to match Object B’s visual tokens to Object A’s reference tokens, but the two objects sit at different grid positions, Vision Transformers bake 2D positional embeddings into each square, and object positions shift as the arm moves.
- **Mitigation:** Hypothesis 1 uses two "blind" methods that only ever update the grid squares covered by the patch itself (returned directly by the `kornia` warp mask) and never require matching Object A's grid coordinates to Object B's grid coordinates: (i) _Way 1 ("Attention Magnet" Patch)_ pulls $100\%$ of `Llama-2`’s text-to-vision cross-attention directly onto the patch’s own squares regardless of where Object A is, and (ii) _Way 2 ("Auto-Feature Copy" Patch)_ automatically takes the mean (pooled) visual embedding of the top-3 highest-attention squares on the clean frame (`mean(tokens_A)`) and trains the patch’s squares to match that single pooled vector.
- **Residual risk:** In _Way 2_, because Vision Transformer tokens contain both appearance and 2D position information, matching a pooled vector from Object A’s location could still carry residual positional bias from Object A’s side of the table. Comparing _Way 1 (Attention Magnet)_ vs. _Way 2 (Auto-Feature Copy)_ will directly reveal whether positional bias hurts Way 2.

### 3. Real-time cost of the masking defense (Hypothesis 2)

- **Why it’s likely:** `OpenVLA-7B` is already near the edge of 20 Hz real-time inference unmodified. Running $N=5$ (Method 1) or $K=9$ (Method 2) masked views per control step, even batched on a GPU, adds meaningful wall-clock latency.
- **Mitigation:** Single-batch parallel GPU inference across masked views, plus lazy execution (running the grid check only once every $K$ steps at action-chunk boundaries, and triggering the second-round check only when single-mask disagreement exceeds $\tau$). Because `LIBERO` is a synchronous (step-locked) simulator, inference latency does not degrade physics stability or control accuracy in simulation.
- **Residual risk:** On a single 16–24 GB GPU in `bfloat16`, running a batch of 9 views at every single step will likely exceed the $<25\%$ target latency goal. We treat $<25\%$ as a target benchmark and will report the exact latency-vs.-security trade-off curve across checking every step ($k=1$) vs. every $k=5$ or $k=8$ steps.

### 4. Clean-task false positives from occlusion masking

- **Why it’s likely:** A mask can land directly on the actual target object (Object A), not just the background, especially in a $224 \times 224$ frame where objects occupy a noticeable fraction of the view. When Object A is covered on a clean run, that single masked view cannot see the target and will predict a different action, spiking disagreement on normal tasks.
- **Mitigation:** In addition to neutral tabletop-color/blur fill (instead of harsh black squares) and a 3-consecutive-step persistence rule, Method 2 (Systematic $3 \times 3$ Grid + Two-Round Minority Check) naturally distinguishes _"a mask covered the real Object A on a clean frame"_ from _"a mask covered the adversarial patch on an attacked frame"_ without needing prior scene knowledge: if a view disagrees because its mask covered the adversarial patch, the real Object A remains visible in that view so masking a second background cell keeps the predicted action locked onto Object A; if a view disagrees because its mask covered the real Object A on a clean frame, Object A remains invisible in the second round and the predictions do not converge to an alternative target.
- **Residual risk:** If Object A and Decoy B + Patch sit so close together on the table that a single $3 \times 3$ grid cell covers both the patch and Object A at the same time (or when the robot gripper fills most of the camera view right before grasping), view variance will rise even under Method 2. We may need to disable the shield during the final gripper-closing phase (last 10–15 steps when the arm is already within $3\text{ cm}$ of the target).

---

## Future Scope

1. **Adaptive Attacker Evaluation (Expectation Over Transformation Across Masks):**
   Once the baseline defense comparison between Method 1 (Random Masks) and Method 2 (Systematic $3 \times 3$ Grid) is complete, a natural next step is testing an _Adaptive White-Box Attacker_ that knows about the masking defense and optimizes the patch through the masking operation (`EOT over masks`) so that even a partially visible patch attempts to steer the robot. We can then experimentally map the exact patch-size boundary where a single grid cell no longer covers $100\%$ of the patch.
2. **Real-World Camera Noise:**
   Extend evaluation to include synthetic sensor noise such as lighting flicker, motion blur and auto-exposure shifts.

---

## Bibliography - Research Papers

### 1. Robot Foundation Models & Simulation Benchmarks (Testbed)

1. OpenVLA: _"OpenVLA: An Open-Source Vision-Language-Action Model." ([arxiv 2406.09246](https://arxiv.org/abs/2406.09246))_
2. Octo: _"Octo: An Open-Source Generalist Robot Policy." ([arxiv 2405.12213](https://arxiv.org/abs/2405.12213))_
3. LIBERO: _"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning." ([arxiv 2306.03310](https://arxiv.org/abs/2306.03310))_
4. SimplerEnv: _"Evaluating Real-World Robot Manipulation Policies in Simulation." ([arxiv 2405.05941](https://arxiv.org/abs/2405.05941))_

### 2. Visual Patch, Trajectory Steering & Adversarial Attacks on VLAs (Hypothesis 1 Baselines & Context)

5. TMA / UADA / UPA: _"Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics." ([arxiv 2411.13587](https://arxiv.org/abs/2411.13587))_
6. EDPA: _"Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models." ([arxiv 2510.13237](https://arxiv.org/abs/2510.13237))_
7. AttackVLA & BackdoorVLA: _"AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models." ([arxiv 2511.12149](https://arxiv.org/abs/2511.12149))_
8. UPA-RFAS: _"When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models." ([arxiv 2511.21192](https://arxiv.org/abs/2511.21192))_
9. Partially Observable Patch Attacks: _"Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics." ([arxiv 2606.03556](https://arxiv.org/abs/2606.03556))_
10. DURA: _"Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models." ([arxiv 2608.10393](https://arxiv.org/abs/2608.10393))_
11. Tex3D: _"Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models." ([arxiv 2604.01618](https://arxiv.org/abs/2604.01618))_
12. TRAP: _"TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches." ([arxiv 2603.23117](https://arxiv.org/abs/2603.23117))_
13. RoboGCG: _"Adversarial Attacks on Robotic Vision-Language-Action Models." ([arxiv 2506.03350](https://arxiv.org/abs/2506.03350))_
14. Command-Preserving Trajectory Redirection: _"Trajectory-Level Redirection Attacks on Vision-Language-Action Models." ([arxiv 2606.12978](https://arxiv.org/abs/2606.12978))_
15. SilentDrift: _"SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models." ([arxiv 2601.14323](https://arxiv.org/abs/2601.14323))_
16. DropVLA: _"DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models." ([arxiv 2510.10932](https://arxiv.org/abs/2510.10932))_

### 3. Embodied Robot Guardrails, Safety Shields & Patch Certification (Hypothesis 2 Baselines & Context)

17. PatchCleanser: _"PatchCleanser: Certifiably Robust Defense against Adversarial Patches for Any Image Classifier." ([arxiv 2108.09135](https://arxiv.org/abs/2108.09135))_
18. RoboGuard: _"Safety Guardrails for LLM-Enabled Robots." ([arxiv 2503.07885](https://arxiv.org/abs/2503.07885))_
19. SENTINEL: _"SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents." ([arxiv 2510.12985](https://arxiv.org/abs/2510.12985))_
20. Reachability Verification for LLM Robots: _"Safe LLM-Controlled Robots with Formal Guarantees via Reachability Analysis." ([arxiv 2503.03911](https://arxiv.org/abs/2503.03911))_
21. SafeVLA: _"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning." ([arxiv 2503.03480](https://arxiv.org/abs/2503.03480))_
22. RoboPAIR: _"Jailbreaking LLM-Controlled Robots." ([arxiv 2410.13691](https://arxiv.org/abs/2410.13691))_
23. BadRobot: _"BadRobot: Jailbreaking Embodied LLM Agents in the Physical World." ([arxiv 2407.20242](https://arxiv.org/abs/2407.20242))_
