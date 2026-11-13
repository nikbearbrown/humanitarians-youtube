# Weekly Hours: Week 8 — Security & Exploitation in Physical AI: OpenVLA Text-to-Vision Attention Extraction

**Project:** Security & Exploitation in Physical AI (VLA Adversarial Robustness)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Report Week:** Nov 9 to Nov 15, 2026  
**Total Hours:** 22.5 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **Kaggle Inference Runtime Extraction (`common/kaggle_utils.py`, `common/kaggle_openvla_server.ipynb`)** | Moving checkpoint resolution, parallel SafeTensors page-cache warming, dual-T4 `OpenVLA-7B` loading, attention extraction, and FastAPI construction out of the notebook into a reviewable Python module (`MODEL_CONFIGS`, `resolve_checkpoint_dir()`, `warm_safetensors_in_ram()`, `load_openvla()`, `extract_llama_cross_attention_maps()`, `create_app()`); reducing the notebook to a thin session driver that selects `ACTIVE_MODEL`/`DISCOVERY_KEY`, copies the versioned module from the `ameyapadwad44/kaggle_utils` dataset, and publishes the Cloudflare tunnel | 4.5 |
| **Real Text-to-Vision Attention Endpoint (`common/kaggle_utils.py`)** | Implementing a forward pass with `output_attentions=True` that measures causal self-attention from prompt-token queries to the 256 visual-key positions inserted after `<BOS>`, normalizes visual mass, averages across heads and selected text tokens, and reshapes to the native `16 x 16` grid; adding `POST /attention` returning per-layer `(L, 16, 16)` and averaged `(16, 16)` maps as a base64-compressed `.npz` with prompt, layer, token-position, grid, model, and inference-time metadata; enforcing active-model and normalization-key validation | 6.5 |
| **Validated Local Client Interface (`common/openvla_client.py`)** | Adding `OpenVLAClient.extract_attention(...)` with layer, text-token, grid-size, and normalization controls; decoding the compressed payload and validating returned shapes, dtypes, and finite values before exposing maps to local attack code | 2.5 |
| **Live Attention Smoke Tests & Deterministic Frame Asset (`smoke_tests/utils_tests.py`, `smoke_tests/assets/libero_agentview.png`)** | Adding a real `224 x 224` `LIBERO-Object` Task 0 `agentview` render as the fixed test frame; implementing `ExtractLlamaAttentionMapsTests` (`test_basic_response`, `test_prompt`, `test_determinism`, `test_instruction_sensitivity`, `run_all_tests`) against the live Kaggle endpoint with graceful skips when the tunnel is unavailable; verifying 32-layer/256-token shapes, per-layer mass `1.0`, repeatability, and instruction sensitivity | 3.5 |
| **Clean-Trajectory Episode Layout (`common/utils.py`, `hypothesis_1/record_clean_trajectories.py`, `smoke_tests/record_clean_trajectories_tests.py`)** | Standardizing per-episode persistence under `<task_name>/epNN` (`trajectory.npz` + `video.mp4`) and adding model-name, 7-DoF action-shape, and finite-value validation so the Week 3 attention baselines and later patch evaluations load consistent records | 2.0 |
| **Documentation & Work Logging** | Updating `HOW_TO.md` (required `kaggle_utils` dataset attachment and fail-fast behavior), `README.md`, and `WORK_PROGRESS.md`; authoring `work_report.md`, `FRICTIONAL.md`, and `HOURS.md` | 2.5 |
| **Meetings** | Weekly Humanitarians AI fellow meeting and coordination with Dev on shared Kaggle session usage | 1.0 |
| **Total** | | **22.5** |
