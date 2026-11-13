# Friction Log: Week 8 — Security & Exploitation in Physical AI: OpenVLA Text-to-Vision Attention Extraction

**Project:** Security & Exploitation in Physical AI (VLA Adversarial Robustness)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Nov 9 to Nov 15, 2026

---

## 1. Focus of the week

- Executing **Week 2 (Token/Attention Hooks)** of the 6-week plan: exposing `OpenVLA-7B`'s real text-to-vision attention over the `16 x 16` visual-token grid so Hypothesis 1's **Attention Magnet Patch** becomes measurable.
- Turning last week's notebook-only Kaggle server into a tested repository module (`common/kaggle_utils.py`) with the notebook reduced to a thin session driver.
- Adding a server-side `POST /attention` endpoint that extracts per-layer `Llama-2` attention maps from a real forward pass, plus a validated local client (`OpenVLAClient.extract_attention(...)`).
- Validating the pathway with live smoke tests on a deterministic `LIBERO` camera frame.

## 2. What was tried, and what was expected

- **Hooking "cross-attention" as if `OpenVLA` were an encoder-decoder model.** Expectation: a standard cross-attention module would expose text-to-image attention directly, as in image-captioning Transformers.
- **Serving attention maps as JSON floats from FastAPI.** Expectation: returning a `(32, 16, 16)` map set as plain JSON would be a straightforward, debuggable response.
- **Testing the endpoint against the live tunnel on every run.** Expectation: the Cloudflare Quick Tunnel would be reachable whenever the Kaggle session was up.
- **Treating "attention looks different when the instruction changes" as sufficient evidence of a usable signal.** Expectation: any non-zero difference would confirm the map is prompt-conditioned and therefore optimizable.
- **Keeping the server logic in the notebook.** Expectation: the notebook was already a working artifact, so continued in-place edits would be the fastest path.

## 3. Points of resistance, and next steps taken

### `OpenVLA` has no encoder-decoder cross-attention to hook
- **Resistance:** `OpenVLA`'s backbone is a decoder-only `Llama-2`; there is no separate cross-attention sublayer, so the "text-to-vision cross-attention" named in the plan had no direct module to read. A naive hook would have measured self-attention over a flattened sequence with no separation between prompt tokens and image tokens.
- **Next step:** defined the measurement explicitly in `extract_llama_cross_attention_maps()`: run `output_attentions=True`, use prompt-token positions as queries and the 256 visual-key positions inserted directly after `<BOS>` as keys, normalize the attention mass over those visual keys, average across heads and the selected text tokens, and reshape to `16 x 16`. The naming stays ("cross-attention" semantics), but the implementation now says what it actually computes.

### Notebook logic had drifted out of reviewable form
- **Resistance:** the server had grown into the notebook, mixing model loading, checkpoint paths, tunnel publishing, and inference handlers. It could not be unit-tested, and edits were invisible in code review.
- **Next step:** extracted the runtime into `common/kaggle_utils.py` (536 new lines: `MODEL_CONFIGS`, `resolve_checkpoint_dir()`, `warm_safetensors_in_ram()`, `load_openvla()`, `extract_llama_cross_attention_maps()`, `create_app()`) and cut the notebook to a thin driver. Because Kaggle cannot import the repository directly, the notebook now copies the versioned module from the attached `ameyapadwad44/kaggle_utils` dataset and fails fast with a clear `FileNotFoundError` when the attachment is missing.

### Full-size attention maps are too large for JSON
- **Resistance:** a `(32, 16, 16)` float set per request, plus metadata, is a poor fit for JSON floats—slow to serialize, large over the tunnel, and lossy if rounded.
- **Next step:** serialize maps as a compressed `.npz` and base64-encode it (`maps_npz_b64`), keeping metadata in plain JSON. The client decodes the payload and rejects malformed, mis-shaped, or non-finite maps before they reach attack code.

### Passing repeatability does not prove the map is prompt-dependent
- **Resistance:** a deterministic vision-only signal would also reproduce exactly across repeat requests, so repeatability alone cannot distinguish "attention to the prompt" from "attention to the picture." The first concern was that the endpoint might be returning a static saliency image.
- **Next step:** added both checks to `ExtractLlamaAttentionMapsTests`. Repeated requests against the live `libero-object` server produced an exact maximum difference of `0.000e+00`, while changing the instruction produced non-zero changes (mean `1.14e-4`, maximum `2.27e-3`). All four tests pass: shapes `(32, 16, 16)`, 256 visual tokens at positions `1–256`, per-layer masses summing to `1.0`, exact prompt match, determinism, and instruction sensitivity.

### Small absolute instruction sensitivity
- **Resistance:** the instruction-sensitivity difference is statistically clean but small in absolute terms (`1.14e-4` mean). Whether that is a strong enough gradient signal for patch optimization is not yet known; a map can be prompt-conditioned and still be too flat to steer.
- **Next step:** flagged for the Week 3 baseline work rather than answered this week—compute clean per-task attention baselines first, then judge whether the signal is usable before wiring it into the optimizer.

## 4. AI and other contributions: accepted, changed, rejected

### Dev (Shared Execution Constraints)
- **Accepted:** Dev's Week 7 constraints continue to hold—pure-simulation `LIBERO` study, executable by both engineers without a local 24 GB GPU—so attention extraction stayed on the shared Kaggle server and the client interface remained model-agnostic.
- **Changed:** no new review points landed this week; the attack/defense scripts still talk only to `OpenVLAClient` and the shared rollout engine, never to model-loading or tunnel logic.

### AI Research Assistant (Optimus)
- **Accepted:** AI-assisted extraction scaffolding for `kaggle_utils.py`, the `ExtractLlamaAttentionMapsTests` harness, and the documentation updates to `HOW_TO.md`, `README.md`, and `WORK_PROGRESS.md`.
- **Changed:** relocated the attention extractor out of `common/utils.py` into `common/kaggle_utils.py` so all Kaggle-side runtime code lives in one module, and made the notebook copy a versioned module from a dataset instead of importing repository code.
- **Rejected:** returning raw JSON attention floats. Replaced with a compressed `.npz` base64 payload to keep the tunnel response small and the maps exact.

## 5. Understood now, and still unresolved

### Understood
- **What "text-to-vision attention" means in a decoder-only VLA:** it is causal self-attention from prompt-token query positions to visual-key positions, not encoder-decoder cross-attention. Normalizing over visual keys is what makes the map comparable across prompts and layers.
- **Why the endpoint must be tested for both determinism and instruction sensitivity:** exact repeatability is necessary but not sufficient; only a controlled instruction change separates prompt-conditioned attention from a static vision-only map.
- **Why the server belongs in a module, not a notebook:** reviewability and testability. The notebook can only carry session state and secrets (`ACTIVE_MODEL`, `DISCOVERY_KEY`), not logic anyone needs to diff.

### Unresolved (To Be Tested in Weeks 3–6)
- **Whether clean per-task attention baselines are concentrated enough to optimize:** the Attention Magnet objective depends on there being a usable concentration signal on real `LIBERO` observations, not just a non-zero instruction difference.
- **Whether `1.14e-4` mean sensitivity survives patch optimization:** small absolute differences may vanish under viewpoint shift in closed loop.
- **The `SigLIP + DINOv2` post-projector path:** Way 2's Auto-Feature Copy hook is specified but not implemented; only the `Llama-2` attention path exists today.
- **Tunnel and session stability for attention batches:** smoke tests skip cleanly when the tunnel is down, but long baseline-collection runs remain untested.
- **Last week's open questions stand:** end-to-end tunnel latency for closed-loop control, clean-trajectory correctness at 15 episodes per task, and the renderer transfer gap (`kornia` warp to native `MuJoCo` rasterizer).
