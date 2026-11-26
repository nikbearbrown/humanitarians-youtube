# Week of 2026-09-14

Two videos this week:

1. [DeepSeek-V3, Balanced Without a Penalty?](#deepseek-v3-balanced-without-a-penalty)
2. [Week 3 Progress: DeepSeek-V3](#week-3-progress-deepseek-v3)

---

## DeepSeek-V3, Balanced Without a Penalty?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [deepseek-v3-balanced-169.mp4](https://drive.google.com/file/d/106n74jeVgE88DgCrpvmPwjkoJbDhbiYf/view)
- **Video (9:16):** [deepseek-v3-balanced-916.mp4](https://drive.google.com/file/d/1TjKCeOUfFW1SY7JIKA1-lLPgff9vjZZ4/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:13.8 (73.79s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

How DeepSeek-V3 turns 671B parameters into 37B per token, how it balances 256 routed experts without a
large auxiliary loss, and what multi-head latent attention saves in the KV cache — every figure from the technical
report or computed from `config.json`:

- **The routing.** Three dense layers, then 58 mixture-of-experts layers; each token visits 1 shared expert plus 8 of
  256 routed experts (`first_k_dense_replace 3`, `n_routed_experts 256`, `num_experts_per_tok 8`).
- **The bias.** Each expert's bias is added to its sigmoid affinity only when choosing the top 8; the gate weights
  still come from the raw scores. At the end of each step, overloaded experts' biases go down by γ and idle ones'
  go up (§2.1.2, eq. 16).
- **The memory.** At these head sizes standard attention would cache 128 × (192 + 128) = 40,960 values per token per
  layer; MLA caches a 512-value latent plus a 64-value RoPE key = 576 — about 71x smaller, ≈ 70 KB per token across
  61 layers at BF16 (§2.1.1; computed from `config.json`).
- **The catch.** A complementary sequence-wise balance loss stays on with an extremely small weight, so the scheme is
  mostly — not completely — penalty-free; 37B active is compute per token, while all 671B weights are still stored;
  the MTP module mainly densifies training and is optional for speculative decoding (§2.1.2, §2.2).

One number needs care: the 71x is computed with DeepSeek-V3's 192-dim keys (128 + 64 RoPE). With 128-dim keys the
same arithmetic gives about 57x, so the reel shows the full computation rather than a rounded ratio.

### Sources

- DeepSeek-AI — *DeepSeek-V3 Technical Report* · [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) — abstract,
  §2.1.1, §2.1.2 (eq. 16), §2.2
- [deepseek-ai/DeepSeek-V3 `config.json`](https://huggingface.co/deepseek-ai/DeepSeek-V3) — `first_k_dense_replace`,
  `n_routed_experts`, `n_shared_experts`, `num_experts_per_tok`, `num_attention_heads`, `qk_nope_head_dim`,
  `qk_rope_head_dim`, `v_head_dim`, `kv_lora_rank`, `num_nextn_predict_layers`

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| Clip lengths vs measured audio | ✅ all 8 clips match the measured audio | ✅ all 8 clips match the measured audio |
| GATE V — final frame check | ✅ clean — 0 BLOCKER, 0 MAJOR (16 frames) | ✅ clean — 0 BLOCKER, 0 MAJOR (16 frames) |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Toolkit-only: every beat uses an existing brutalist.art pattern that already has a registered 9:16 twin
(`ClaudeComposerAsk`, `ReelExecSummary`, `ReelFramework`, `BlipLadder`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so the reel builds with **no new scene code**. The earlier draft of this teardown used
`ClaudeScienceLayerStack`, `ClaudeCodeBeat` and `ClaudeWindow`; the first two have no 9:16 twin and the third
underfills the portrait canvas, so those beats were rewritten as `ReelFramework` rows and a `BlipLadder`. The
portrait sheet is the landscape sheet with `aspect_ratio: "9:16"` and a `916` suffix on every pattern, emitted from
the same beat list, and both cuts share one set of narration files, so they cannot drift. The `.mp4` masters are
not in this repo — they are linked at the top.

```bash
# in a brutalist.art clone, with each sheet copied into its own reel folder as beat_sheet.json
python3 runtime/scripts/generate_audio_kokoro.py <reel>          # Kokoro am_onyx — the clock
python3 runtime/scripts/remotion_scenes.py <reel>                # --scale=2 -> 4K
python3 runtime/scripts/compile.py <reel> --height 2160          # 9:16 twin: --height 3840
python3 runtime/qc/final_frame_check.py <reel>                   # GATE V
```

---

## Week 3 Progress: DeepSeek-V3

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [week3-progress-169.mp4](https://drive.google.com/file/d/1jdGN60D3HjI8CPCwr3lDqmjra5AY5T0Z/view)
- **Video (9:16):** [week3-progress-916.mp4](https://drive.google.com/file/d/199AR4zNuCL0Ye7mHBc_gwyAikqLspyv2/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 0:57.5 (57.46s), 7 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet-week3-progress.json`](beat_sheet-week3-progress.json) · [`beat_sheet-week3-progress-916.json`](beat_sheet-week3-progress-916.json)

### What the video covers

The week's progress update: what shipped (the DeepSeek-V3 explainer as two 4K masters with identical audio,
1:13.8 in eight beats), how the week went (read the report and re-check every number, write one beat list for both
sheets, narrate and render at 4K, check clip lengths and frames in both orientations), what it taught (the bias picks
experts but never weighs them; "auxiliary-loss-free" still keeps a tiny sequence-wise balance loss; DeepSeek-V3's keys
are 192 dims, so the cache saving is about 71x), and what is still open (9:16 twins for `ClaudeScienceLayerStack` and
`ClaudeCodeBeat`, which is why the teardown draft was re-cut onto responsive patterns).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the DeepSeek-V3 section above
- DeepSeek-AI — DeepSeek-V3 Technical Report · [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) — §2.1.1, §2.1.2

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| Clip lengths vs measured audio | ✅ all 7 clips match the measured audio | ✅ all 7 clips match the measured audio |
| GATE V — final frame check | ✅ clean — 0 BLOCKER, 0 MAJOR (14 frames) | ✅ clean — 0 BLOCKER, 0 MAJOR (14 frames) |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Same pipeline and patterns as the explainer: one beat list, emitted as the 16:9 and 9:16 sheets, sharing one
set of narration files. It was authored after the explainer's frame check, so every quality figure on screen is
the measured result.
