# FACTCHECK — week7 (Nov 02) (Security in Physical AI)

Every claim the narration makes, mapped to the source document:
`D:/Ameya/Career/Humanitarians AI/humanitarians-youtube/fellows/ameya-p/2026-11-02-vla-adversarial-attack-research-setup/work_report.md`
("Security & Exploitation in Physical AI: Cloud-Offloaded VLA Inference Infrastructure & Closed-Loop Simulation Setup").

## B00 — Cold open

- **"The plan targets OpenVLA-7B on the LIBERO benchmark, but the two fine-tuned checkpoints need thirty gigabytes of disk and over sixteen gigabytes of VRAM. Can two engineers on Windows laptops run twenty hertz closed-loop robot experiments anyway?"**
  Source §1: "a finalized two-engineer experimental plan... targeting `OpenVLA-7B` on the `LIBERO` benchmark". Source §2: "the two `OpenVLA-7B` fine-tuned checkpoints (`openvla-7b-finetuned-libero-object` and `openvla-7b-finetuned-libero-spatial`) require ~30 GB of disk and >16 GB VRAM for practical closed-loop inference—beyond laptop hardware". Source §2: "a closed-loop robotic system running at 20 Hz" (20 Hz figure from the Week 1 report's framing of the closed-loop loop; both engineers develop on Windows laptops per §2).

## B01 — BLUF

- **"Running OpenVLA-7B locally is beyond laptop hardware, so we split the system in two: the physics simulation stays local for low latency, and the model moves to a free Kaggle cloud server. Both engineers now drive fifteen-gigabyte checkpoints from their laptops."**
  Source §2: "This finding drove the week's central architectural decision: keep the **simulation local** and offload the **model to the cloud**." Source §4: "simulation and data collection stay local (low-latency `MuJoCo` stepping), inference stays remote (high-throughput FP16 T4 compute)". Source §3: "replaced local checkpoint inference with a remote GPU server built on free Kaggle resources"; each checkpoint is 15 GB ("Both 15 GB fine-tuned checkpoints were published as persistent Kaggle Datasets").

## B02 — The Architecture (local sim + remote inference)

- **"A local rollout engine steps the MuJoCo physics simulator and renders 224-pixel RGB observations. The client serializes each frame as a lossless base64 PNG, sends it through an auto-discovered Cloudflare tunnel, and a Kaggle T4 server runs FP16 inference. The seven degree of freedom action comes back and the episode is saved."**
  Source §4: "`OpenVLAClient`... auto-discovers the live Kaggle Cloudflare tunnel URL from the `ntfy.sh` topic, and exposes `health()` and `predict_action(image, instruction)` using lossless base64 PNG transport"; "rendering $224 \times 224$ `agentview` RGB observations, converting `OpenVLA` gripper predictions ($[0, 1] \rightarrow [-1, +1]$), stepping the physics simulator, and asserting finite 7-DoF motor actions"; "`run_closed_loop_rollout`, which opens a `LIBERO` task locally, queries the remote `OpenVLA-7B` server per step, and optionally saves each full episode". Source §3: "loaded per session in `torch.float16`... with `device_map="auto"` sharding it across both Tesla T4 GPUs".

## B03 — FUSE Pre-Warming Measurement

- **"Kaggle mounts datasets over FUSE, and cold-loading model shards page-faults at sixty-five megabytes per second. Our warm safetensors routine streams all four shards into the Linux page cache first, cutting checkpoint load time from three minutes thirty-six seconds down to forty-one seconds."**
  Source §3: "`from_pretrained()` on cold `mmap`-ed shards page-faults sequentially at ~65 MB/s. A `warm_safetensors_inram()` routine (4-thread `ThreadPoolExecutor`, `os.posix_fadvise(...)`) streams all 4 `.safetensors` shards (14.05 GiB) concurrently into the Linux RAM page cache first." Source §3 finding: "FUSE shard-load speedup (3m 36s → 41s): pre-warming cut checkpoint warmup to 26.2 s and `from_pretrained()` shard loading to 15.0 s (41.2 s total, down from 216 s of cold sequential FUSE `mmap` page faults)."

## B04 — Server Constraints & Windows Fixes

- **"Loading both checkpoints at once exhausted the T4's memory and thrashed system RAM, so exactly one model runs per session, sharded across both GPUs with fifteen gigabytes of headroom."**
  Source §3 finding: "Dual-model constraint on `T4 x2`: loading both checkpoints simultaneously... left only 12.81 MiB free on `cuda:0`—triggering `OutOfMemoryError` on forward activations—and mapped 28.1 GiB of shards into a 29 GiB system RAM, causing OS thrashing. Running **one model per session**, sharded across both GPUs, uses ~7.0 GiB per 14.56 GiB GPU and leaves ~15 GB of total VRAM headroom for activations."
- **"The tunnel's live URL is pushed to an ntfy topic, so local clients auto-discover the server with zero copy-paste."**
  Source §3: "published over a free Cloudflare Quick Tunnel (`trycloudflare.com`) whose live URL is pushed to a constant `DISCOVERY_KEY` topic on `ntfy.sh`, so local clients need no manual URL copy-paste."
- **"On Windows, four known incompatibilities are fixed automatically by the setup script."**
  Source §2 table: (1) `git -c core.longpaths=true` for MAX_PATH; (2) auto-generated `third_party/LIBERO/libero/__init__.py`; (3) `weights_only=False` patch for PyTorch >= 2.6; (4) `configure_robosuite_windows()` copies `mujoco.dll` and sets `MUJOCO_GPU_RENDERING = False`.

## B05 — Separation of Concerns & Next Steps

- **"Simulation and data collection stay local, inference stays remote on FP16 T4 compute, and the attack and defense code stays model-agnostic, talking only to the client and the rollout engine."**
  Source §4: "The resulting architecture cleanly separates concerns for the rest of the project: **simulation and data collection stay local** (low-latency `MuJoCo` stepping), **inference stays remote** (high-throughput FP16 T4 compute), and the **attack/defense code stays model-agnostic**, talking only to `OpenVLAClient` and `run_closed_loop_rollout`."
- **"Next: record clean baseline rollouts, collect fifteen trajectories per task, and implement the token and attention hooks."**
  Source §5: "record the clean baseline `.mp4` rollout videos on `LIBERO-Object` and `LIBERO-Spatial`... and collect the 15 clean trajectories per task using `common/utils.py`" and "implement the shared PyTorch hooks to extract the $16 \times 16$ visual token embeddings (`SigLIP + DINOv2` post-projector) and `Llama-2` text-to-vision cross-attention maps".

## B06 — Your Turn Handoff

- Suggested prompt for the viewer to run the smoke-test suite against the Kaggle server and observe a closed-loop LIBERO Task 0 rollout in the MuJoCo viewer (per §4: "with an interactive 3D `MuJoCo` viewer for visual verification of Task 0 on both suites").

## B07 — Outro

- Title restate only (`week7 (Nov 02).` / `Security in Physical AI`).
