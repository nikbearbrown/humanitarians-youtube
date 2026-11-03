# Research Ideas: Stealthy Trajectory Steering and Verification in Physical AI (VLA Models)

These hypothesis ideas focus on the research vertical Security & Exploitation.

## 1. Motivation & Core Problem Statement

In classical **Verifiable Machine Learning**, a central problem is understanding how a tiny, barely noticeable perturbation to an input can cause a model to flip its output completely - and designing certified or empirical defenses to prevent it.

As AI moves from text chatbots to **Physical AI** (robots controlled by **Vision-Language-Action (VLA)** that take `[Camera Image + Text Instruction]` as inputs and directly output motor commands `[dx, dy, dz, gripper]`) the stakes change from generating bad text to executing dangerous physical actions.

However, a major review of the current literature reveals a critical gap highlighted by the **AttackVLA** benchmark ([arXiv:2511.12149](https://arxiv.org/abs/2511.12149)):

> **The Core Gap:** _Almost all existing adversarial attacks on VLA models only cause "untargeted failures or static action states" (making the robot arm freeze, twitch in place, or miss an object). Driving a clean, unmodified robot model to smoothly and stealthily perform a **specific, long-horizon sequence of actions** - and verifying against such stealthy steering - remains largely unsolved._

### Why Is Stealthy Steering So Much Harder Than Breaking the Robot?

In a static image classifier, an attacker only needs to fool the model **once**.
In a physical robot running a closed-loop controller at 5–50 Hz, as soon as an adversarial perturbation nudges the robot arm $2\text{ cm}$ to the left at Step 1, **the camera viewpoint changes at Step 2**. Because the visual input has shifted, a static perturbation designed for Step 1 loses effectiveness at Step 2, causing the robot to either self-correct or stall in place.

---

## 2. Literature Review: Recent Attempts at Steering VLA Robots (2025–2026)

Over the past year (2025–2026), researchers have explored **four distinct approaches** to overcome closed-loop feedback and steer VLA-controlled robots toward specific physical outcomes. Each approach exposes a significant limitation:

### Approach A: Tweaking the Text Instruction ("Prompt Redirection")

Instead of perturbing the camera feed, these methods modify words or tokens in the text instruction given to the robot. Because the text instruction remains fixed across every video frame, its effect persists across the entire trajectory.

- **RoboGCG — _Adversarial Attacks on Robotic Vision-Language-Action Models_** (Jones, Robey, Kolter et al., June 2025 — [arXiv:2506.03350](https://arxiv.org/abs/2506.03350))
  - **Method:** Adapts Greedy Coordinate Gradient (`GCG`) token-forcing to VLA models. Applying a single adversarial text suffix at the start of an episode grants broad reachability over the robot's action space across multiple steps.
  - **Limitation:** Requires injecting obvious gibberish token suffixes into the text prompt and primarily forces repetitive directional movements rather than natural task execution.
- **Command-Preserving Trajectory Redirection — _Trajectory-Level Redirection Attacks on Vision-Language-Action Models_** (Puthumanaillam et al., June 2026 — [arXiv:2606.12978](https://arxiv.org/abs/2606.12978))
  - **Method:** Uses on-policy rollout search to find natural-looking rewordings of the user's command (without naming the attacker's target object) that redirect the robot's closed-loop trajectory to an attacker-chosen target.
  - **Limitation:** Assumes the attacker can intercept and rewrite the **user's text prompt** before the episode starts. It does not work when a user issues a trusted voice or text command directly.

---

### Approach B: Poisoning the Model During Training (Backdoor Attacks)

Because test-time visual patches struggle to sustain smooth 50-step trajectories on clean models, several teams resorted to **training-time data poisoning** so the robot learns a hidden rule triggered at deployment:

- **AttackVLA / BackdoorVLA — _Benchmarking Adversarial and Backdoor Attacks on VLAs_** (Zhao et al., Nov 2025 — [arXiv:2511.12149](https://arxiv.org/abs/2511.12149))
  - **Method:** Benchmarks existing VLA attacks and introduces `BackdoorVLA`, which poisons training demonstrations so that a combined visual-textual trigger compels the robot to execute an attacker-specified long-horizon action sequence (58.4% average targeted success rate, up to 100% on selected tasks).
- **DropVLA — _An Action-Level Backdoor Attack on Vision-Language-Action Models_** (Xu et al., IROS 2026 — [arXiv:2510.10932](https://arxiv.org/abs/2510.10932))
  - **Method:** Poisons just $0.31\%$ of fine-tuning episodes so that a visual trigger in the camera view forces a specific action primitive (such as `open_gripper` mid-air to drop a held object) within 0.05 seconds while keeping $>98.5\%$ normal task success.
- **SilentDrift — _Exploiting Action Chunking for Stealthy Backdoor Attacks on VLAs_** (Xu et al., ACL Findings 2026 — [arXiv:2601.14323](https://arxiv.org/abs/2601.14323))
  - **Method:** Identifies a key architectural flaw in modern VLAs: **action chunking** (where the model looks at 1 camera frame and executes $K$ motor steps open-loop without re-checking the camera). By poisoning keyframes using a smooth $C^2$-continuous curve (`Smootherstep`), the robot arm smoothly drifts off trajectory with zero jerky velocity spikes (93.2% attack success rate).
  - **Limitation of Approach B:** **All backdoor methods require poisoning the training or fine-tuning pipeline ahead of time.** They cannot steer an already-trained, clean off-the-shelf VLA model.

---

### Approach C: Hijacking the Robot’s "Inner Monologue" (Chain-of-Thought VLAs)

What if the attacker cannot poison training data and cannot alter the user's text prompt, and can only place a physical patch in the workspace?

- **TRAP — _Hijacking VLA CoT-Reasoning via Adversarial Patches_** (Huang et al., ICML 2026 — [arXiv:2603.23117](https://arxiv.org/abs/2603.23117))
  - **Method:** Instead of trying to force low-level `[dx, dy, dz]` motor outputs at every single frame, `TRAP` targets **Chain-of-Thought (CoT) VLAs** that generate an intermediate text reasoning step before acting. By placing a printed adversarial tablecloth on the table, the patch hijacks the internal CoT text (e.g., changing the internal plan from _"pick up the apple"_ to _"deliver the knife to the person"_). Once the intermediate reasoning flips, the robot's normal controller smoothly executes the hazardous task.
  - **Limitation:** Only applies to VLAs that explicitly generate intermediate Chain-of-Thought text reasoning, and relies on a visible adversarial pattern.

---

### Approach D: Natural-Looking Visual Patches & 3D Textures

Early visual patches on VLAs looked like obvious rainbow static stickers and primarily caused task failure rather than controlled steering. Recent work has focused on improving physical realism and cross-view persistence:

- **TMA — _Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics_** (Wang et al., ICCV 2025 — [arXiv:2411.13587](https://arxiv.org/abs/2411.13587))
  - **Method:** Introduces Untargeted Action Discrepancy (`UADA`), Universal Patch Attacks (`UPA`), and Trajectory Manipulation Attacks (`TMA`) using a small colorful patch in the camera view, causing up to a 100% drop in task success.
- **UPA-RFAS — _When Robots Obey the Patch: Universal Transferable Patch Attacks on VLAs_** (Lu et al., CVPR 2026 — [arXiv:2511.21192](https://arxiv.org/abs/2511.21192)) & **EDPA** (Zhang et al., Oct 2025 — [arXiv:2510.13237](https://arxiv.org/abs/2510.13237))
  - **Method:** Optimizes universal physical patches that disrupt vision-language alignment and transfer across unknown VLA architectures.
- **Partially Observable Patch Attacks** (Tang et al., IEEE RA-L 2026 — [arXiv:2606.03556](https://arxiv.org/abs/2606.03556))
  - **Method:** Generates a fixed camera patch from only a short prefix of the robot's trajectory, increasing trajectory curvature to compound control errors over time.
- **DURA — _Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on VLAs_** (Han et al., Aug 2026 — [arXiv:2608.10393](https://arxiv.org/abs/2608.10393))
  - **Method:** Optimizes along a pretrained diffusion model's latent space to generate visually natural patches that steer the robot toward target actions in both white-box and black-box settings.
- **Tex3D — _Objects as Attack Surfaces via Adversarial 3D Textures for VLAs_** (Chen et al., April 2026 — [arXiv:2604.01618](https://arxiv.org/abs/2604.01618))
  - **Method:** Wraps a 3D adversarial texture onto manipulated objects using differentiable rendering so the perturbation remains effective across changing camera angles (causing up to 96.7% task failure).
  - **Limitation of Approach D:** Standard non-CoT VLAs remain difficult to steer into **precise, smooth multi-step alternative tasks** purely via visual perturbations because forcing low-level motor actions frame-by-frame fights against the model's closed-loop visual grounding.

---

## 3. Summary Comparison: What Exists vs. What Is Missing

| Approach                         | Representative Papers (2025–2026)                                                                                                                                                          |         Smoothly Steers Trajectory?         | Works on Clean (Unpoisoned) Model? | Leaves User Prompt Untouched? | Works on Standard (Non-CoT) VLAs? |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------: | :--------------------------------: | :---------------------------: | :-------------------------------: |
| **Prompt Redirection**           | _RoboGCG_ ([2506.03350](https://arxiv.org/abs/2506.03350)), _Trajectory Redirection_ ([2606.12978](https://arxiv.org/abs/2606.12978))                                                      |                     Yes                     |                Yes                 |            **No**             |                Yes                |
| **Training Backdoors**           | _BackdoorVLA_ ([2511.12149](https://arxiv.org/abs/2511.12149)), _DropVLA_ ([2510.10932](https://arxiv.org/abs/2510.10932)), _SilentDrift_ ([2601.14323](https://arxiv.org/abs/2601.14323)) |                     Yes                     |               **No**               |              Yes              |                Yes                |
| **CoT Thought Hijacking**        | _TRAP_ ([2603.23117](https://arxiv.org/abs/2603.23117))                                                                                                                                    |                     Yes                     |                Yes                 |              Yes              |              **No**               |
| **Visual Patches / 3D Textures** | _TMA_ ([2411.13587](https://arxiv.org/abs/2411.13587)), _Tex3D_ ([2604.01618](https://arxiv.org/abs/2604.01618)), _DURA_ ([2608.10393](https://arxiv.org/abs/2608.10393))                  | **Partially (Short nudges / task failure)** |                Yes                 |              Yes              |                Yes                |

---

## 4. Proposed Research Directions & Testable Hypotheses

Based on the limitations above, **no existing work cleanly achieves (or verifies against) stealthy, long-horizon trajectory steering on a clean, standard VLA without touching the user's prompt or poisoning training data.**

Below are three concrete, testable research hypotheses:

### Direction 1: "Object-Identity Swap" Perturbations (Semantic Steering Instead of Motor Steering)

- **The Insight:** Existing visual patches fail at smooth multi-step steering because they try to directly optimize low-level motor outputs (`[dx, dy, dz]`) at every camera frame. As soon as the arm moves, the motor gradient changes. However, a VLA already knows how to smoothly reach for whatever object matches the text instruction.
- **Research Question:** _Instead of optimizing a visual perturbation to force raw motor commands, can we optimize a small visual perturbation (or realistic lighting/texture change) that swaps the **visual embedding identity** of two objects on the table (making a hazardous object match the embedding of the requested target object)?_
- **Testable Hypothesis:** On a clean OpenVLA model in the LIBERO simulator, optimizing a localized patch or object texture purely in the **vision-language alignment layer** (to make Object B look like Object A to the encoder) will cause the robot's own closed-loop controller to smoothly and reliably steer the arm to grasp the wrong object across the entire trajectory, achieving a much higher targeted steering success rate than motor-level patch optimization (`TMA`).

### Direction 2: Test-Time "Action-Chunk Drift" on Clean Models

- **The Insight:** _SilentDrift_ ([arXiv:2601.14323](https://arxiv.org/abs/2601.14323)) revealed that modern VLAs predict $K$-step action chunks open-loop (blindly executing $K$ steps before looking at the camera again), allowing tiny nudges to integrate into large physical drift—but they only exploited this via training-time backdoors.
- **Research Question:** _Can an attacker exploit the open-loop action-chunking boundary at **test time** on a **clean, unpoisoned VLA** by applying tiny, imperceptible visual or sensor perturbations only at the decision keyframes where a new $K$-step chunk is computed?_
- **Testable Hypothesis:** Perturbing only the chunk-boundary frames with a smooth directional gradient (`Smootherstep`-constrained) can stealthily drift a clean VLA robot arm into a forbidden workspace zone or obstacle while keeping per-step velocity and acceleration completely within normal human-demonstration bounds.

### Direction 3: Verifiable Defense via "Action-Chunk & Spatial Consistency" Shielding

- **The Insight:** Existing formal robot guardrails like _RoboGuard_ ([arXiv:2503.07885](https://arxiv.org/abs/2503.07885)) and _SENTINEL_ ([arXiv:2510.12985](https://arxiv.org/abs/2510.12985)) verify high-level plans assuming perception is accurate, while visual adversarial training (_EDPA_, [arXiv:2510.13237](https://arxiv.org/abs/2510.13237)) requires costly retraining and offers no runtime guarantee.
- **Research Question:** _Can we detect and block stealthy trajectory steering at runtime—without retraining the VLA—by testing whether the predicted action chunk stays physically consistent under small random camera crops/masks and temporal frame shifts?_
- **Testable Hypothesis:** Genuine object-grounded trajectories remain targeting the same 3D physical point when small background regions of the camera frame are masked or jittered, whereas patch-steered or perturbation-steered trajectories exhibit high variance in their predicted $K$-step endpoint. A lightweight runtime verifier that checks **endpoint consistency across $N$ masked views** can block $>90\%$ of targeted patch and drift attacks with near-zero false positives on clean tasks.

---

## References

1. **RoboPAIR:** Robey et al., _"Jailbreaking LLM-Controlled Robots,"_ ICRA 2025. [arXiv:2410.13691](https://arxiv.org/abs/2410.13691)
2. **BadRobot:** Zhang et al., _"BadRobot: Jailbreaking Embodied LLM Agents in the Physical World,"_ ICLR 2025. [arXiv:2407.20242](https://arxiv.org/abs/2407.20242)
3. **POEX / POEF:** Lu et al., _"Easier Said Than Done: Unpacking Intent-Behavior Gap in Jailbreaking LLM-Based Robots,"_ NDSS 2027. [arXiv:2412.16633](https://arxiv.org/abs/2412.16633)
4. **TMA / UADA / UPA:** Wang et al., _"Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics,"_ ICCV 2025. [arXiv:2411.13587](https://arxiv.org/abs/2411.13587)
5. **RoboGCG:** Jones, Robey, Kolter et al., _"Adversarial Attacks on Robotic Vision-Language-Action Models,"_ June 2025. [arXiv:2506.03350](https://arxiv.org/abs/2506.03350)
6. **AttackVLA & BackdoorVLA:** Zhao et al., _"AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models,"_ Nov 2025. [arXiv:2511.12149](https://arxiv.org/abs/2511.12149)
7. **DropVLA:** Xu et al., _"DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models,"_ IROS 2026. [arXiv:2510.10932](https://arxiv.org/abs/2510.10932)
8. **SilentDrift:** Xu et al., _"SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models,"_ ACL Findings 2026. [arXiv:2601.14323](https://arxiv.org/abs/2601.14323)
9. **TRAP:** Huang et al., _"TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches,"_ ICML 2026. [arXiv:2603.23117](https://arxiv.org/abs/2603.23117)
10. **Command-Preserving Trajectory Redirection:** Puthumanaillam et al., _"Trajectory-Level Redirection Attacks on Vision-Language-Action Models,"_ June 2026. [arXiv:2606.12978](https://arxiv.org/abs/2606.12978)
11. **DURA:** Han et al., _"Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models,"_ Aug 2026. [arXiv:2608.10393](https://arxiv.org/abs/2608.10393)
12. **Tex3D:** Chen et al., _"Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models,"_ April 2026. [arXiv:2604.01618](https://arxiv.org/abs/2604.01618)
13. **UPA-RFAS:** Lu et al., _"When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models,"_ CVPR 2026. [arXiv:2511.21192](https://arxiv.org/abs/2511.21192)
14. **EDPA:** Zhang et al., _"Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models,"_ Oct 2025. [arXiv:2510.13237](https://arxiv.org/abs/2510.13237)
15. **Partially Observable Patch Attacks:** Tang et al., _"Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics,"_ IEEE RA-L 2026. [arXiv:2606.03556](https://arxiv.org/abs/2606.03556)
16. **Reachability Verification:** Hafez et al., _"Safe LLM-Controlled Robots with Formal Guarantees via Reachability Analysis,"_ March 2025. [arXiv:2503.03911](https://arxiv.org/abs/2503.03911)
17. **RoboGuard:** Ravichandran et al., _"Safety Guardrails for LLM-Enabled Robots,"_ March 2025. [arXiv:2503.07885](https://arxiv.org/abs/2503.07885)
18. **SENTINEL:** Zhan et al., _"SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents,"_ Oct 2025. [arXiv:2510.12985](https://arxiv.org/abs/2510.12985)
19. **SafeVLA:** Zhang et al., _"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning,"_ NeurIPS 2025. [arXiv:2503.03480](https://arxiv.org/abs/2503.03480)
