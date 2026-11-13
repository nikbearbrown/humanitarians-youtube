# Security & Exploitation in Physical AI: OpenVLA Text-to-Vision Attention Extraction

---

Volunteer Name: Ameya Padwad  
Report Week: Nov 9 to Nov 15, 2026

## 1. Introduction

This week advanced the **Security & Exploitation** exploration of stealthy trajectory steering in Vision-Language-Action (VLA) models from clean-rollout infrastructure to the observability required by Hypothesis 1's **Attention Magnet Patch**. The prior week established a local `LIBERO` simulation loop backed by remote `OpenVLA-7B` inference on Kaggle. This week exposes the model's real text-to-vision attention over the `16 x 16` visual-token grid, making it possible to measure and eventually optimize whether a physical patch attracts the task prompt's visual attention.

The week's completed work focused on:

1. Moving the reusable Kaggle inference runtime out of the notebook and into a tested Python module.
2. Adding a server-side endpoint that extracts per-layer `Llama-2` text-to-vision attention maps from a real OpenVLA forward pass.
3. Adding a validated local client interface and live smoke tests using a deterministic `LIBERO` camera frame.

## 2. Reusable Kaggle Runtime

The remote server implementation was extracted from [`common/kaggle_openvla_server.ipynb`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/kaggle_openvla_server.ipynb) into [`common/kaggle_utils.py`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/kaggle_utils.py). The module now owns checkpoint configuration and resolution, parallel SafeTensors page-cache warming, dual-T4 OpenVLA loading, attention extraction, and FastAPI app construction.

The Kaggle notebook is now a thin session driver: it selects `ACTIVE_MODEL` and `DISCOVERY_KEY`, copies the versioned utility module from the attached `ameyapadwad44/kaggle_utils` dataset, loads the model, starts the app, and publishes the Cloudflare tunnel. This separation makes the server implementation reviewable and testable in the repository while preserving the persistent Kaggle execution environment.

## 3. Real Text-to-Vision Attention API

[`extract_llama_cross_attention_maps()`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/kaggle_utils.py) now performs an OpenVLA forward pass with `output_attentions=True` and produces an attention map for each selected `Llama-2` layer. Although OpenVLA uses a decoder-only Llama-2 backbone rather than encoder-decoder cross-attention, its multimodal forward pass inserts the 256 visual tokens directly after `<BOS>`. The extractor therefore measures causal self-attention from prompt-token queries to those visual-key positions, normalizes the mass over visual tokens, averages across heads and selected text tokens, and reshapes it to the native `16 x 16` visual grid.

The FastAPI server now exposes `POST /attention`, alongside `/health` and `/act`. It returns per-layer `(L, 16, 16)` maps and an average `(16, 16)` map in a base64-encoded compressed `.npz`, avoiding a large JSON-float response. Metadata records the prompt, selected layers, token positions, grid shape, model identity, and inference time. Request validation enforces that the client requests the active model and matching normalization key.

[`common/openvla_client.py`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/openvla_client.py) now provides `OpenVLAClient.extract_attention(...)`, which calls the endpoint, decodes the compressed payload, and validates returned shapes, dtypes, and finite values before exposing the maps to local attack code.

## 4. Validation Results

The new attention pathway is covered by `ExtractLlamaAttentionMapsTests` in [`smoke_tests/utils_tests.py`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/smoke_tests/utils_tests.py). A real `224 x 224` `LIBERO-Object` Task 0 `agentview` render was added as a deterministic test asset. The suite checks basic responses, prompt construction, repeatability, and instruction sensitivity against the live Kaggle endpoint, while skipping cleanly when the public tunnel is unavailable.

All four live attention smoke tests passed against the `libero-object` server:

- Returned maps have shape `(32, 16, 16)`, covering 32 Llama-2 layers and 256 visual tokens.
- Every normalized per-layer map sums to `1.0` over the visual grid.
- Repeated requests produced an exact maximum difference of `0.000e+00`.
- Changing the instruction produced non-zero map changes (mean `1.14e-4`, maximum `2.27e-3`), confirming that the endpoint captures prompt-dependent attention rather than a static vision-only signal.

The setup requirement for the attached `ameyapadwad44/kaggle_utils` dataset was documented in [`HOW_TO.md`](../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/HOW_TO.md); the notebook now fails clearly if the attachment is missing.

## 5. Next Steps

- Compute and store clean per-task attention baselines for the Hypothesis 1 Attention Magnet objective.
- Connect `extract_attention()` to the differentiable and native patch-optimization loops, then evaluate whether attention can be concentrated on a patch under changing closed-loop viewpoints.
- Add the `SigLIP + DINOv2` post-projector visual-token extraction path required by Hypothesis 1's Auto-Feature Copy method.
