#!/usr/bin/env python3
"""model_facts.py — the numbers B02's arithmetic is worked on, read from the models
themselves rather than from a model card.

For each Qwen3.5 tag pulled into Ollama: the parameter count the GGUF declares
(general.parameter_count), the byte size of the weights layer in the local manifest
(the text model only: no vision projector, no draft model), the bits per weight that
implies (8 × bytes / parameters), and the attention shape that sets the KV cache.

Stdlib only; needs a running Ollama. Run:  python3 model_facts.py > model_facts.out
"""
import json
import urllib.request
from pathlib import Path

API = "http://127.0.0.1:11434"
MANIFESTS = Path.home() / ".ollama/models/manifests/registry.ollama.ai/library/qwen3.5"
BW_M2_PRO = 200e9          # bytes/s — Apple Newsroom, 2023-01-17: "200GB/s of unified memory bandwidth"


def show(model):
    req = urllib.request.Request(API + "/api/show", data=json.dumps({"model": model}).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


for tag in ("0.8b", "4b", "9b"):
    model = f"qwen3.5:{tag}"
    layers = json.loads((MANIFESTS / tag).read_text())["layers"]
    weights = [l for l in layers if l["mediaType"].endswith(".model")][0]
    kinds = [l["mediaType"].rsplit(".", 1)[-1] for l in layers]
    d = show(model)
    mi, det = d["model_info"], d["details"]
    n = mi["general.parameter_count"]
    L = mi["qwen35.block_count"]
    every = mi["qwen35.full_attention_interval"]
    kv, kd = mi.get("qwen35.attention.head_count_kv"), mi["qwen35.attention.key_length"]
    bpw = 8 * weights["size"] / n
    print(f"{model}: quant {det['quantization_level']} · parameters {n:,} · weights layer "
          f"{weights['size']:,} B ({weights['size']/1e9:.3f} GB) · {bpw:.3f} bits/weight · "
          f"layers {L}, full attention every {every} → {L // every} KV layers, kv_heads {kv}, "
          f"head_dim {kd} · manifest layers {kinds}")
    if "projector" not in kinds:
        print("  NOTE: this tag was pulled 2026-09-29 in Ollama's older single-file layout — the "
              "weights layer also holds the vision encoder, which is not read per text token. The "
              "registry's current qwen3.5:9b splits it out: text weights 5,629,109,120 B "
              "(registry manifest, read 2026-10-09). Not used for the B02 worked example.")
    if weights["size"] != sum(l["size"] for l in layers if l["mediaType"].endswith(".model")):
        print("  (more than one weights layer)")
    print(f"  decode ceiling on M2 Pro: {BW_M2_PRO:.0e} B/s ÷ {weights['size']:,} B = "
          f"{BW_M2_PRO / weights['size']:.1f} tokens/s")
    if kv:
        per_tok = 2 * (L // every) * kv * kd * 2          # K and V, fp16
        print(f"  KV cache (fp16, full-attention layers only): {per_tok:,} B/token → "
              f"{per_tok * 8192 / 2**30:.3f} GiB at 8K context, "
              f"{per_tok * 65536 / 2**30:.3f} GiB at 64K")
