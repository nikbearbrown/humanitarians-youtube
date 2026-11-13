# Weekly Hours: Week 7 — Security & Exploitation in Physical AI: Cloud-Offloaded VLA Inference Infrastructure & Closed-Loop Simulation Setup

**Project:** Security & Exploitation in Physical AI (VLA Adversarial Robustness)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Report Week:** Nov 2 to Nov 8, 2026  
**Total Hours:** 22.5 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **Automated Cross-Platform Project Setup (`common/setup.py`, `requirements.txt`, `HOW_TO.md`)** | Scripting the `LIBERO` clone, dependency installation (`torch`, `mujoco==3.1.6`, `robosuite==1.4.0`, `bddl`, `kornia`), and editable `libero` registration; implementing the four automated Windows compatibility fixes (`core.longpaths=true`, auto-generated `__init__.py`, `weights_only=False` patch for `PyTorch >= 2.6`, `configure_robosuite_windows()` for `mujoco.dll` + `MUJOCO_GPU_RENDERING`); authoring `HOW_TO.md` | 4.0 |
| **Kaggle `T4 x2` Cloud GPU Server (`common/kaggle_openvla_server.ipynb`)** | Publishing both 15 GB `OpenVLA-7B` fine-tuned checkpoints as persistent Kaggle Datasets; implementing `warm_safetensors_in_ram()` (4-thread `ThreadPoolExecutor`, `os.posix_fadvise`, 16 MB chunks) to cut shard loading from 216 s to 41.2 s; debugging the dual-model `OutOfMemoryError` into the single-`ACTIVE_MODEL`, `device_map="auto"` sharded layout (~7 GiB per 14.56 GiB T4); standing up the FastAPI `GET /health` / `POST /act` server behind the auto-published Cloudflare Quick Tunnel | 6.5 |
| **Local Auto-Discovering Client & Discovery Automation (`common/openvla_client.py`, `smoke_tests/test_kaggle_tunnel.py`)** | Building `OpenVLAClient` (`.env` `OPENVLA_DISCOVERY_KEY`, `ntfy.sh` tunnel auto-discovery, `health()` / `predict_action()` with lossless base64 PNG transport); auto-generating the unique discovery key in `common/setup.py` | 3.0 |
| **Closed-Loop Smoke Tests (`smoke_tests/setup_tests.py`)** | Implementing the interactive 3D `MuJoCo` viewer rollouts on Task 0 of `LIBERO-Object` and `LIBERO-Spatial` ($224 \times 224$ `agentview` rendering, gripper $[0,1] \rightarrow [-1,+1]$ conversion, finite 7-DoF action/state assertions); unifying the suite (`test_cloned_repos`, `test_package_imports`, `test_health`, `test_libero_object`, `test_libero_spatial`) with active-model auto-detection | 3.5 |
| **Shared Rollout Engine Refactor (`common/utils.py`)** | Extracting `run_closed_loop_rollout` as the single closed-loop engine (episode saving as `trajectory.npz` + `metadata.json` + `video.mp4`, stabilization steps, `MuJoCo` state capture) and refactoring `setup_tests.py` into a thin shell over it (net −39 lines) | 2.5 |
| **Documentation & Work Logging** | Committing the Week 6 research artifacts (`README.md`, `research_ideas.md`, `experiment_plan.md`, `weekly_execution_plan.md`, `WORK_PROGRESS.md`); updating `HOW_TO.md` / `README.md` for the cloud-offload architecture; authoring `work_report.md`, `FRICTIONAL.md`, and `HOURS.md` | 2.0 |
| **Meetings** | Weekly Humanitarians AI fellow meeting and coordination with Dev on the shared Kaggle server workflow | 1.0 |
| **Total** | | **22.5** |
