# Friction Log: Week 6 — Security & Exploitation in Physical AI: Stealthy Trajectory Steering & Spatial Consistency Verification in VLA Models

**Project:** Security & Exploitation in Physical AI (VLA Adversarial Robustness)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Oct 26 to Nov 1, 2026

---

## 1. Focus of the week

- Exploring a new research direction under the **Security & Exploitation** vertical (`Steps 1 & 2: Explore & Choose`), extending principles from my Master's coursework in **Verifiable Machine Learning** (how small, bounded input perturbations cause catastrophic output flips, and how to certify against them) to **Physical AI** and **Vision–Language–Action (VLA)** robot foundation models (`OpenVLA-7B`).
- Conducting a literature review of 23 primary research papers (2024–2026) spanning LLM-controlled robot jailbreaking (*RoboPAIR*, *BadRobot*, *POEX*), VLA adversarial patches and backdoors (*AttackVLA*, *TMA*, *EDPA*, *UPA-RFAS*, *RoboGCG*, *SilentDrift*, *DropVLA*, *TRAP*, *DURA*, *Tex3D*), and formal safety shields (*RoboGuard*, *SENTINEL*, *SafeVLA*, *PatchCleanser*).
- Formulating and refining two core hypotheses for a pure-simulation study in `LIBERO` (`MuJoCo`) without requiring physical robot hardware:
  - **Hypothesis 1 (The Attack):** Stealthy closed-loop trajectory steering via 3D tabletop patches (**Way 1: "The Attention Magnet Patch"** and **Way 2: "The Auto-Feature Copy Patch"**).
  - **Hypothesis 2 (The Defense):** Runtime perception verification via **Spatial Consistency Shielding** (comparing **Method 1: Naive Random 5-View Masking** against **Method 2: Systematic $3 \times 3$ Covering Grid + Two-Round Minority Check**).
- Incorporating technical peer review from **Dev** to eliminate mathematical and implementation blind spots before code execution, and designing a 6-week, 2-engineer parallel execution plan (`experiment_plan.md` and `weekly_execution_plan.md`).

## 2. What was tried, and what was expected

- **Initial abstract control-theory formulations.** Expectation: framing agent/robot verification using formal dynamical systems math (Lyapunov exponents, Control Barrier Functions in latent space, spectral stability of multi-agent graphs) would provide an immediately actionable experimental project.
- **Naive 5-view random masking + median vote defense (Hypothesis 2 initial draft).** Expectation: blacking out 5 random $10\%\text{–}15\%$ squares on the camera frame and executing the median motor vector would neutralize a localized adversarial patch on the table and detect $>90\%$ of attacks with a $<2\%$ per-step false-positive threshold.
- **Direct grid-coordinate feature matching between Object A and Object B (Hypothesis 1 initial draft).** Expectation: training a patch next to Decoy Object B so that its visual grid tokens match the exact token embeddings of Target Object A (`tokens[idx_B] == tokens[idx_A]`) would smoothly steer `OpenVLA-7B` toward Object B.
- **Using base `OpenVLA-7B` across both `LIBERO` and `SimplerEnv`.** Expectation: a single base `OpenVLA-7B` checkpoint could be evaluated zero-shot across both `LIBERO` and `SimplerEnv` without fine-tuned task weights.

## 3. Points of resistance, and next steps taken

### Abstract mathematical formulations were too disconnected from a buildable simulator experiment
- Initial brainstormed directions (Lyapunov blow-up, polyhedral latent Control Barrier Functions) were overly theoretical and difficult to translate into a clean, reproducible simulation benchmark within a 6-week engineering window.
- **Next step:** pivoted to concrete, observable physical behaviors in embodied VLA models (`OpenVLA-7B` in `LIBERO`), focusing on a crisp empirical gap identified by the *AttackVLA* benchmark: existing visual patches mostly cause the robot arm to freeze, twitch, or fail its task rather than smoothly steering it across a multi-step trajectory to grasp a decoy object.

### Peer review catch #1 (Dev): "5 Random Masks + Median Vote" actually favors the attacker
- **Resistance:** Dev pointed out a critical flaw in our initial Hypothesis 2 defense: if an adversarial patch occupies $\sim 8\%$ of the image and we drop 5 random $10\%\text{–}15\%$ masks, in most frames **4 out of 5 views still see the patch** (or all 5 miss it completely). That means 4 views vote for the hijacked action (Decoy B) and at most 1 minority view votes for the true action (Target A)—so taking the median selects the **hijacked action**! Furthermore, a $2\%$ false-alarm rate *per step* compounds over a 150-step rollout to $1 - 0.98^{150} \approx 95\%$ chance of a false alarm per episode, and black `[0,0,0]` pixel boxes create sharp artificial edges.
- **Next step:**
  1. Kept **Method 1 (Random 5-View Masking + Median)** as a naive baseline and added **Method 2 (Systematic $3 \times 3$ Covering Grid + Two-Round Minority Check, extending *PatchCleanser* to closed-loop control)** so we can experimentally demonstrate why random masking fails and how a covering grid resolves it.
  2. In Method 2's Two-Round Check, when 1 minority grid view disagrees with the other 8 views, we take that 1 disagreeing view (where the patch is covered) and mask one additional cell at a time—confirming the action stays locked onto Object A.
  3. Switched from per-step to **per-episode false-positive calibration ($<5\%$ of episodes)** with a 3-consecutive-step persistence rule, and replaced black pixel squares with neutral tabletop-color/local blur (or ViT token masking).

### Peer review catch #2 (Dev): Matching Object A's grid squares to Object B's grid squares suffers from 2D positional bias and requires knowing object coordinates
- **Resistance:** `OpenVLA` chops a $224 \times 224$ frame into a $16 \times 16$ grid (256 visual tokens), and Vision Transformers (`SigLIP + DINOv2`) bake the **2D screen position** into each token. Copying top-left tokens (Object A) directly onto bottom-right tokens (Object B) copies the wrong screen position, breaks as the camera moves, and assumes the attacker knows the exact simulator coordinates of Object A and Object B ahead of time.
- **Next step:** redesigned Hypothesis 1 around two **"blind" (coordinate-free) patch methods** where the optimizer only ever updates the grid squares covered by the patch itself (returned automatically by the `kornia` perspective warp):
  1. **Way 1 — "The Attention Magnet Patch" (Engineer 1):** Trains the patch inside `Llama-2-7B`’s text-to-image cross-attention layers across diverse scenes and prompts to pull $100\%$ of the prompt's attention score onto the patch’s own squares, luring the arm to whatever decoy sits next to the patch without knowing what or where Object A is.
  2. **Way 2 — "The Auto-Feature Copy Patch" via the Vision-Encoder Shortcut (Engineer 2):** Lets `OpenVLA` find Object A automatically on Frame 1 (by selecting the top-3 highest-attention squares on the clean image), averages their visual embeddings (`mean(tokens_A)`), and trains the patch’s squares to match that pooled vector. Because those 256 visual tokens are produced by the vision encoder + projector (~0.6B parameters) *before* the 7B `Llama-2` model, Way 2 trains in **~3–4 GB of GPU VRAM** ($5\text{–}10\times$ faster).

### Simulator differentiability and checkpoint alignment
- **Resistance:** `MuJoCo`'s built-in renderer is not differentiable, and base `OpenVLA-7B` does not solve `LIBERO` zero-shot (while performing poorly on `SimplerEnv`).
- **Next step:** dropped `SimplerEnv` to focus 100% on **`LIBERO` (`LIBERO-Object` and `LIBERO-Spatial`)** using the official fine-tuned checkpoints (`openvla-7b-finetuned-libero-object` and `-spatial`), and explicitly separated patch training (differentiable `kornia` perspective homography warp) from evaluation (baking the `.png` texture onto a flat, non-glossy `specular="0"` 3D coaster geom inside native `MuJoCo`).

## 4. AI and other contributions: accepted, changed, rejected

### Dev (Peer Review & Risk Analysis)
- **Accepted:** Dev's critique of random 5-view median voting, per-step false-positive compounding, non-differentiable `MuJoCo` rendering, `LIBERO` fine-tuned checkpoint requirements, and spatial token correspondence between Object A and Object B.
- **Changed:** Instead of discarding the original 5-view random masking method, retained it as **Method 1** alongside **Method 2 (Systematic $3 \times 3$ Grid + Two-Round Check)** to create a direct experimental ablation; placed the compute-heavy **Adaptive Attacker (`EOT over masks`)** evaluation into a dedicated `## Future Scope` section rather than blocking the initial 6-week schedule.

### AI Research Assistant (Optimus)
- **Accepted:** Literature synthesis across 23 primary arXiv/conference papers (2024–2026), formulation of the coordinate-free **Way 1 (Attention Magnet)** and **Way 2 (Auto-Feature Copy + Vision-Encoder Shortcut)** split for 2 engineers, and drafting of `README.md`, `experiment_plan.md`, and `weekly_execution_plan.md`.
- **Rejected:** Initial overly theoretical dynamical-systems / control-theory proposals (Lyapunov blow-up, polyhedral latent Control Barrier Functions) and artificial camera-blur/lighting-flicker requirements, in favor of a clean, practical `LIBERO` simulation design.

## 5. Understood now, and still unresolved

### Understood
- **Why existing VLA patches only break robots instead of steering them:** forcing low-level `[dx, dy, dz]` motor outputs at every frame fights against closed-loop visual feedback as soon as the camera angle shifts; hijacking high-level visual attention (**Way 1**) or pooled object token identity (**Way 2**) lets the VLA's own closed-loop controller smoothly guide the arm to the decoy.
- **Why covering grids beat random masks for patch defenses:** a small localized patch is missed by most random masks (causing majority/median voting to side with the attacker), whereas a fixed $3 \times 3$ covering grid guarantees at least one patch-free view that can be verified via a lazy two-round check when single-mask disagreement spikes.
- **Compute efficiency of the Vision-Encoder Shortcut:** decoupling `OpenVLA`'s ~0.6B vision backbone (`SigLIP + DINOv2` + projector) from its 7B `Llama-2` language backbone reduces patch-training VRAM from ~20 GB down to ~3–4 GB.

### Unresolved (To Be Tested in Weeks 1–6)
- **Renderer transfer gap (`kornia` warp $\to$ native `MuJoCo` rasterizer):** how much Targeted Steering Success Rate (TSSR) drops when a patch trained via differentiable homography warping is rendered natively inside `MuJoCo`.
- **Attention Magnet (Way 1) vs. Auto-Feature Copy (Way 2) vs. Combined:** whether pulling `Llama-2` cross-attention onto the patch, copying pooled visual features onto the patch, or combining both losses yields higher closed-loop grasp rates and better zero-shot transfer across unseen prompts.
