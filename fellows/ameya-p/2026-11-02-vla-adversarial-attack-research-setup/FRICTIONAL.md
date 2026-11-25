# Friction Log: Week 7 — Security & Exploitation in Physical AI: Cloud-Offloaded VLA Inference Infrastructure & Closed-Loop Simulation Setup

**Project:** Security & Exploitation in Physical AI (VLA Adversarial Robustness)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Nov 2 to Nov 8, 2026

---

## 1. Focus of the week

- Executing the first block of the finalized 6-week plan (**Week 1–2: Environment Setup & Baselines**): turning the `LIBERO` + `OpenVLA` experimental design from last week into runnable, reproducible infrastructure both engineers can drive from their laptops.
- Publishing the Week 1 planning artifacts (`README.md`, `research_ideas.md`, `experiment_plan.md`, `weekly_execution_plan.md`, `WORK_PROGRESS.md`) to the team repository.
- Automating the cross-platform project setup (`common/setup.py`, `requirements.txt`, `HOW_TO.md`) and validating it with a growing smoke-test suite (`smoke_tests/setup_tests.py`).
- Offloading `OpenVLA-7B` checkpoint storage and GPU inference to a persistent **Kaggle `T4 x2`** cloud server (`common/kaggle_openvla_server.ipynb`), paired with an auto-discovering local client (`common/openvla_client.py`).
- Factoring the shared closed-loop rollout engine (`common/utils.py`) that trajectory collection, patch attacks, and defenses will reuse for the rest of the project.

## 2. What was tried, and what was expected

- **Local-first inference on developer laptops.** Expectation: both engineers could download the two fine-tuned checkpoints (`openvla-7b-finetuned-libero-object` and `-spatial`) and run closed-loop `LIBERO` rollouts locally with acceptable speed.
- **A quick manual `LIBERO` install on Windows.** Expectation: cloning `LIBERO` and `pip install`-ing the stack (`mujoco==3.1.6`, `robosuite==1.4.0`, `bddl`) would work out of the box on Windows, as it does on Linux.
- **Cold-loading Kaggle-mounted checkpoints via `mmap`.** Expectation: `from_pretrained()` on the FUSE-mounted `.safetensors` shards would stream quickly enough that session startup was a non-issue.
- **One shared dual-model server (one checkpoint per T4 GPU).** Expectation: loading both `libero-object` and `libero-spatial` simultaneously on the two 14.56 GiB Tesla T4s would give both engineers a single always-ready endpoint.
- **Manual tunnel-URL configuration.** Expectation: copying the fresh `trycloudflare.com` URL into a local `.env` each session would be an acceptable workflow for a free-tunnel setup.

## 3. Points of resistance, and next steps taken

### Windows compatibility broke the standard `LIBERO` install
- **Resistance:** the documented `LIBERO` setup assumes Linux: `git clone` fails on Windows `MAX_PATH` limits, `setuptools.find_packages()` does not register the cloned `libero` package, `LIBERO`'s `torch.load(init_states_path)` breaks on `PyTorch >= 2.6` (default `weights_only=True`), and `robosuite` rendering fails when `mujoco.dll` is not on the loader path.
- **Next step:** moved all four fixes into `common/setup.py` so the environment is reproducible by a single command: `git -c core.longpaths=true` checkouts, auto-generated `third_party/LIBERO/libero/__init__.py`, a `weights_only=False` patch for initial-state loading, and `configure_robosuite_windows()` (copying `mujoco.dll` into `robosuite/utils/`, setting `MUJOCO_GPU_RENDERING = False`). Local installation and editable registration now succeed end-to-end on Windows (`Python 3.10`, Conda `vla-adv`).

### Local hardware cannot host the 15 GB checkpoints
- **Resistance:** the two checkpoints need ~30 GB of disk, and laptop GPUs under 16 GB VRAM force slow CPU-to-GPU weight offloading on every control step—unusable for closed-loop rollouts.
- **Next step:** architectural split—**simulation stays local** (low-latency `MuJoCo` stepping) while **inference moves to the cloud**: both checkpoints published as persistent Kaggle Datasets (`ameyapadwad44/openvla-libero-object` / `-spatial`), mounted per session via `kagglehub.dataset_download(...)`.

### Cold FUSE shard loading took 3m 36s per model
- **Resistance:** Kaggle mounts datasets over FUSE, and `from_pretrained()` page-faults the `mmap`-ed shards sequentially at roughly 65 MB/s—216 s of dead time before every session.
- **Next step:** implemented `warm_safetensors_in_ram()` in `common/kaggle_openvla_server.ipynb`: a 4-thread `ThreadPoolExecutor` issuing `os.posix_fadvise(..., os.POSIX_FADV_WILLNEED)` in 16 MB chunks to pull all 4 shards (14.05 GiB) concurrently into the Linux RAM page cache before loading. Checkpoint warmup dropped to 26.2 s and shard loading to 15.0 s—**41.2 s total, a $5.2\times$ speedup**.

### Dual-model loading OOM'd the `T4 x2` server
- **Resistance:** placing one 14.07 GiB checkpoint on each 14.56 GiB T4 left only 12.81 MiB free on `cuda:0`—`OutOfMemoryError` on forward activations—while mapping 28.1 GiB of shards into 29 GiB of system RAM caused OS thrashing.
- **Next step:** single-model-per-session design: one `ACTIVE_MODEL` (set in `CELL 0`) loaded in `torch.float16` with `device_map="auto"` sharded across both T4s, using ~7.0 GiB per 14.56 GiB GPU and leaving ~15 GB of total VRAM headroom; engineers switch models between sessions instead of co-hosting them.

### Smoke-test logic duplicated the rollout loop the project actually needs
- **Resistance:** `smoke_tests/setup_tests.py` carried its own inline closed-loop rollout code, while next week's baseline collection needs the same loop plus trajectory persistence—two divergent copies waiting to happen before the attack and defense scripts even exist.
- **Next step:** extracted `run_closed_loop_rollout` into `common/utils.py` as the single shared engine (opens a `LIBERO` task locally, queries the remote server per step, optionally saves each episode as `trajectory.npz` + `metadata.json` + `video.mp4`), and refactored the smoke tests into a thin shell over it (net −39 lines). The tunnel workflow was also automated: the FastAPI server (`GET /health`, `POST /act`) publishes its live Cloudflare Quick Tunnel URL to an `ntfy.sh` `DISCOVERY_KEY` topic, and `OpenVLAClient` auto-discovers it from `.env`, removing manual URL copy-paste entirely.

## 4. AI and other contributions: accepted, changed, rejected

### Dev (Peer Review & Shared Execution Constraints)
- **Accepted:** Dev's Week 6 scoping constraints—pure-simulation study with no physical robot hardware, executable by both engineers on ordinary laptops—directly shaped this week's architecture; the local-simulation + remote-inference split is what makes the two-engineer plan runnable without a 24 GB local GPU.
- **Changed:** none of Dev's review points were rejected this week; his constraints were operationalized in code rather than revised.

### AI Research Assistant (Optimus)
- **Accepted:** the Week 6 planning artifacts committed this week (`README.md`, `experiment_plan.md`, `weekly_execution_plan.md` drafted with AI assistance), plus this week's reporting (`work_report.md`, this friction log, and `HOURS.md`).
- **Changed:** dropped the redundant local `third_party/openvla` (`prismatic`) repository clone from the setup flow once inference moved to Kaggle—the local-first design it belonged to was superseded by the client–server design (commit `9b7bf7c`).

## 5. Understood now, and still unresolved

### Understood
- **Why the checkpoints cannot live on laptops:** ~30 GB of disk for two 15 GB fine-tunes and >16 GB VRAM for practical FP16 inference rule out a local-first design; offloading storage *and* compute (not just one) is what removes the bottleneck.
- **How FUSE-mounted `mmap` loading behaves and why pre-warming works:** sequential page faults over Kaggle's FUSE mount are the bottleneck, not disk read speed; `posix_fadvise(WILLNEED)` from a small thread pool saturates the mount and cuts load time $5.2\times$.
- **VRAM budgeting on `T4 x2`:** sharding *one* FP16 7B model across both 14.56 GiB GPUs (~7 GiB each) beats co-hosting two models; activations need real headroom that a one-model-per-GPU layout cannot spare.
- **The architecture that keeps attacks and defenses model-agnostic:** attack and defense scripts should only ever talk to `OpenVLAClient` and `run_closed_loop_rollout`, never to model-loading or tunnel logic.

### Unresolved (To Be Tested in Weeks 2–6)
- **End-to-end tunnel latency for closed-loop control:** whether the Cloudflare Quick Tunnel + base64 PNG transport sustains acceptable step rates for full `LIBERO` episodes, measured during baseline trajectory collection.
- **Tunnel and session stability:** how long free `trycloudflare.com` tunnels and Kaggle sessions survive long rollout batches, and how disruptive re-discovery is mid-run.
- **Baseline collection correctness:** whether the 15 clean trajectories per task record end-to-end through `common/utils.py` with intact frames, actions, and `MuJoCo` states.
- **The Week 2 observability layer:** the `Llama-2` text-to-vision cross-attention hook ($16 \times 16$ grid) and the `SigLIP + DINOv2` post-projector visual token hook are specified but not yet implemented.
- **Last week's open questions stand:** the renderer transfer gap (`kornia` warp $\to$ native `MuJoCo` rasterizer) and the Way 1 vs. Way 2 vs. Combined comparison remain untested until the infrastructure built this week is exercised.
