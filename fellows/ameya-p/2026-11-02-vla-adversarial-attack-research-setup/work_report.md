# Security & Exploitation in Physical AI: Cloud-Offloaded VLA Inference Infrastructure & Closed-Loop Simulation Setup

---

Volunteer Name: Ameya Padwad  
Report Week: Nov 2 to Nov 8, 2026

## 1. Introduction

This week marked the transition of the **Security & Exploitation** research exploration—**stealthy trajectory steering & spatial consistency verification in Vision–Language–Action (VLA) models**—from planning into execution. Last week closed with a finalized two-engineer experimental plan (`experiment_plan.md`, `weekly_execution_plan.md`) targeting `OpenVLA-7B` on the `LIBERO` benchmark; this week delivered the execution substrate that plan depends on: a fully automated, cross-platform local simulation environment and a cloud-offloaded inference pipeline that lets both engineers run fast closed-loop `MuJoCo` rollouts on laptops without downloading 15 GB checkpoints or owning a 24 GB GPU.

The week's work covered the first block of the execution roadmap (**Week 1–2: Environment Setup & Baselines**):

1. Committing and publishing the Week 1 research artifacts (`README.md`, `research_ideas.md`, `experiment_plan.md`, `weekly_execution_plan.md`, `WORK_PROGRESS.md`) to the team repository.
2. Automating the `LIBERO` + `OpenVLA` project setup on Windows with a one-command provisioning script (`common/setup.py`) and validating it with a growing smoke-test suite (`smoke_tests/setup_tests.py`).
3. Offloading `OpenVLA-7B` checkpoint storage and GPU inference to a persistent **Kaggle `T4 x2`** cloud server, exposed to local machines over an auto-discovered public tunnel.
4. Building the shared local rollout engine (`common/utils.py`) that will serve trajectory collection, patch attacks, and defenses for the remainder of the project.

## 2. Automated Cross-Platform Project Setup on Windows

The first engineering task was turning a fragile, manual environment setup into a reproducible one-command pipeline. [`common/setup.py`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/setup.py) now automates cloning `LIBERO`, installing the core simulation and differentiable-vision stack (`torch`, `mujoco==3.1.6`, `robosuite==1.4.0`, `bddl`, `gym`, `kornia`, `numpy`, `Pillow`, `imageio`), and registering `libero` as an editable package, with [`requirements.txt`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/requirements.txt) pinning the dependency set.

Because both engineers develop on Windows laptops, several platform-specific incompatibilities had to be solved automatically inside the setup script itself:

| #   | Windows Incompatibility                                                                             | Automated Fix in `common/setup.py`                                                                                   |
| :-- | :-------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| 1   | `git clone` fails on Windows `MAX_PATH` limits for deep LIBERO paths.                               | Checkouts run with `git -c core.longpaths=true`.                                                                     |
| 2   | `setuptools.find_packages()` does not register the cloned `libero` package.                         | Auto-generates top-level `third_party/LIBERO/libero/__init__.py` after cloning.                                      |
| 3   | `LIBERO`'s `torch.load(init_states_path)` breaks on `PyTorch >= 2.6` (default `weights_only=True`). | Patched to pass `weights_only=False` for initial-state loading.                                                      |
| 4   | `robosuite` `MuJoCo` rendering fails when `mujoco.dll` is not on the loader path.                   | `configure_robosuite_windows()` copies `mujoco.dll` into `robosuite/utils/` and sets `MUJOCO_GPU_RENDERING = False`. |

The full `LIBERO` (`MuJoCo` + `robosuite`) installation and editable package registration now succeed end-to-end on Windows (`Python 3.10`, Conda `vla-adv`), documented for both engineers in [`HOW_TO.md`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/HOW_TO.md).

However, the local-first design hit a hard wall: the two `OpenVLA-7B` fine-tuned checkpoints (`openvla-7b-finetuned-libero-object` and `openvla-7b-finetuned-libero-spatial`) require ~30 GB of disk and >16 GB VRAM for practical closed-loop inference—beyond laptop hardware, which would otherwise force slow CPU-to-GPU weight offloading on every control step of a 20 Hz loop. This finding drove the week's central architectural decision: keep the **simulation local** and offload the **model to the cloud**.

## 3. Cloud-Offloading `OpenVLA-7B` to a Persistent Kaggle `T4 x2` Server

The second and largest work stream replaced local checkpoint inference with a remote GPU server built on free Kaggle resources, implemented in [`common/kaggle_openvla_server.ipynb`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/kaggle_openvla_server.ipynb):

1. **Persistent Checkpoint Datasets:** Both 15 GB fine-tuned checkpoints were published as persistent Kaggle Datasets (`ameyapadwad44/openvla-libero-object` and `ameyapadwad44/openvla-libero-spatial`), so any new session mounts the weights directly via `kagglehub.dataset_download(...)` without re-downloading from the Hugging Face Hub.
2. **RAM Page-Cache Pre-Warming:** Kaggle mounts datasets over FUSE, and `from_pretrained()` on cold `mmap`-ed shards page-faults sequentially at ~65 MB/s. A `warm_safetensors_inram()` routine (4-thread `ThreadPoolExecutor`, `os.posix_fadvise(..., os.POSIX_FADV_WILLNEED)` in 16 MB chunks) streams all 4 `.safetensors` shards (14.05 GiB) concurrently into the Linux RAM page cache first.
3. **Single-Model-per-Session Loading:** A single `ACTIVE_MODEL` (set in `CELL 0`) is loaded per session in `torch.float16`—native to Turing SM75 FP16 Tensor Cores—with `device_map="auto"` sharding it across both Tesla T4 GPUs.
4. **Public Inference API:** A FastAPI server exposes `GET /health` and `POST /act` endpoints, published over a free Cloudflare Quick Tunnel (`trycloudflare.com`) whose live URL is pushed to a constant `DISCOVERY_KEY` topic on `ntfy.sh`, so local clients need no manual URL copy-paste.

Two measured engineering findings shaped the final server configuration:

- **FUSE shard-load speedup ($3\text{m }36\text{s} \rightarrow 41\text{s}$):** pre-warming cut checkpoint warmup to 26.2 s and `from_pretrained()` shard loading to 15.0 s (41.2 s total, down from 216 s of cold sequential FUSE `mmap` page faults).
- **Dual-model constraint on `T4 x2`:** loading both checkpoints simultaneously (one per 14.56 GiB T4) left only 12.81 MiB free on `cuda:0`—triggering `OutOfMemoryError` on forward activations—and mapped 28.1 GiB of shards into a 29 GiB system RAM, causing OS thrashing. Running **one model per session**, sharded across both GPUs, uses ~7.0 GiB per 14.56 GiB GPU and leaves ~15 GB of total VRAM headroom for activations.

## 4. Local Auto-Discovering Client, Closed-Loop Smoke Tests & Shared Rollout Engine

The cloud server is paired with a thin local layer that makes remote inference feel like a local library call:

- **`common/openvla_client.py` (`OpenVLAClient`):** reads `OPENVLA_DISCOVERY_KEY` from `.env` (auto-generated as a unique `libero-xxxx-xxxx-xxxx` key by `common/setup.py`), auto-discovers the live Kaggle Cloudflare tunnel URL from the `ntfy.sh` topic, and exposes `health()` and `predict_action(image, instruction)` using lossless base64 PNG transport. A dedicated `smoke_tests/test_kaggle_tunnel.py` validates the discovery path.
- **`smoke_tests/setup_tests.py`:** a unified, self-configuring smoke-test suite (`test_cloned_repos`, `test_package_imports`, `test_health`, `test_libero_object`, `test_libero_spatial`) that auto-detects the active model on the Kaggle server and runs end-to-end closed-loop rollouts—rendering $224 \times 224$ `agentview` RGB observations, converting `OpenVLA` gripper predictions ($[0, 1] \rightarrow [-1, +1]$), stepping the physics simulator, and asserting finite 7-DoF motor actions and simulation states, with an interactive 3D `MuJoCo` viewer for visual verification of Task 0 on both suites.
- **`common/utils.py` (in progress, currently uncommitted):** the last piece of the week is factoring the rollout logic into a single shared engine, `run_closed_loop_rollout`, which opens a `LIBERO` task locally, queries the remote `OpenVLA-7B` server per step, and optionally saves each full episode (`trajectory.npz` with frames/actions/`MuJoCo` states, `metadata.json`, and `video.mp4`)—the exact data layout the Week 2–3 trajectory collection, patch attacks, and consistency-shield defenses will consume. `setup_tests.py` has already been refactored to call it (net −39 lines), keeping the smoke tests as a thin validation shell over the engine.

The resulting architecture cleanly separates concerns for the rest of the project: **simulation and data collection stay local** (low-latency `MuJoCo` stepping), **inference stays remote** (high-throughput FP16 T4 compute), and the **attack/defense code stays model-agnostic**, talking only to `OpenVLAClient` and `run_closed_loop_rollout`.

## 5. Next Steps

- **Week 1 Deliverable Completion:** record the clean baseline `.mp4` rollout videos on `LIBERO-Object` and `LIBERO-Spatial` through the Kaggle `T4 x2` tunnel and collect the 15 clean trajectories per task using `common/utils.py`.
- **Week 2 Hook Implementation:** implement the shared PyTorch hooks to extract the $16 \times 16$ visual token embeddings (`SigLIP + DINOv2` post-projector) and `Llama-2` text-to-vision cross-attention maps—the observability layer both the attention-magnet attack (Hypothesis 1, Way 1) and the two-round consistency shield (Hypothesis 2) depend on.
