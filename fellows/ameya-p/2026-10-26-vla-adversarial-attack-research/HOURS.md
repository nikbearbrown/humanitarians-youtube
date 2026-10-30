# Weekly Hours: Week 6 — Security & Exploitation in Physical AI: Stealthy Trajectory Steering & Spatial Consistency Verification in VLA Models

**Project:** Security & Exploitation in Physical AI (VLA Adversarial Robustness)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Report Week:** Oct 26 to Nov 1, 2026  
**Total Hours:** 22.0 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **Literature Survey on Physical AI & VLA Security (2024–2026)** | Surveying 23 primary research papers across LLM-robot jailbreaking (*RoboPAIR*, *BadRobot*, *POEX*), VLA visual patch & trajectory attacks (*AttackVLA*, *TMA*, *EDPA*, *UPA-RFAS*, *RoboGCG*, *SilentDrift*, *DropVLA*, *TRAP*, *DURA*, *Tex3D*), and formal safety shields (*RoboGuard*, *SENTINEL*, *SafeVLA*, *PatchCleanser*) to identify the unsolved gap in stealthy multi-step trajectory steering on clean models | 7.5 |
| **Hypothesis Formulation & Simulation Architecture Design** | Formulating Hypothesis 1 (Stealthy Object/Attention Steering) and Hypothesis 2 (Runtime Spatial Consistency Shielding), designing the two-stage 3D rendering pipeline (`kornia` perspective warp during training $\to$ native `MuJoCo` 3D coaster rendering during evaluation) on `LIBERO` + `OpenVLA-7B` | 6.0 |
| **Peer Review Integration & Method Refinement** | Incorporating technical peer feedback from Dev: upgrading Hypothesis 2 to compare Method 1 (Random 5-View Masking) against Method 2 (Systematic $3 \times 3$ Covering Grid + Two-Round Minority Check) with per-episode FPR calibration, and redesigning Hypothesis 1 into two coordinate-free methods—Way 1 ("Attention Magnet" Patch) and Way 2 ("Auto-Feature Copy" Patch via the Vision-Encoder Shortcut)—plus documenting 4 primary risks & mitigations | 5.5 |
| **Documentation & Execution Planning** | Authoring `README.md` (literature proposal), `experiment_plan.md` (full experimental design, baselines, target goals, risks, and 23-paper bibliography), `weekly_execution_plan.md` (6-week 2-engineer parallel schedule), and `work_report.md` | 2.0 |
| **Meetings** | Weekly Humanitarians AI fellow meeting and peer review discussion with Dev on VLA attack/defense design | 1.0 |
| **Total** | | **22.0** |
