# Week of 2026-09-21

Two videos this week:

1. [gpt-oss, Paying Attention to Nothing?](#gpt-oss-paying-attention-to-nothing)
2. [Week 4 Progress: gpt-oss](#week-4-progress-gpt-oss)

---

## gpt-oss, Paying Attention to Nothing?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [gpt-oss-attention-sinks-169.mp4](https://drive.google.com/file/d/1oXFTqgWIqeHm6_wSq51TBweFYGb4ESkl/view)
- **Video (9:16):** [gpt-oss-attention-sinks-916.mp4](https://drive.google.com/file/d/1raEFyXtsDF_CcJ50gZFSBiqv-MM2Zn6f/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:06.8 (66.75s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

What gpt-oss-120b changes inside attention, and what that buys in memory — every figure from OpenAI's model
card or computed from `config.json`:

- **The layout.** The 36 layers alternate: 18 use a 128-token sliding window, 18 attend over the full context; 64 query
  heads share 8 key-value heads, and every layer routes each token to 4 of 128 experts (`layer_types`,
  `sliding_window 128`, `num_key_value_heads 8`, `experts_per_token 4`; model card §2.2).
- **The sink.** Each head has one learned bias in the softmax denominator, so the weights over real tokens can sum to
  less than one — the model card says it lets attention "pay no attention to any tokens" (§2.2).
- **The memory.** One full layer caches 8 KV heads × 64 dims × 2 (K, V) × 2 bytes = 2,048 bytes per token. At 131,072
  tokens the 18 full layers hold ≈ 4.8 GB; the 18 sliding layers, capped at 128 tokens, hold ≈ 4.7 MB; all 36 full
  would be ≈ 9.7 GB (computed from `config.json`, BF16 cache assumed).
- **The limits.** Weights and the model card are released; the training data is not (§2.4). What each head learns to
  route to its sink isn't documented. MXFP4 at 4.25 bits per parameter on the MoE weights is what lets 120b fit one
  80 GB GPU (§2.1).

The cache figures are decimal gigabytes and assume a 2-byte (BF16) cache; they are arithmetic from the config, not
a measurement of a running server.

### Sources

- OpenAI — *gpt-oss-120b & gpt-oss-20b Model Card* · [arXiv:2508.10925](https://arxiv.org/abs/2508.10925) — §2.1,
  §2.2, §2.4 (116.8B total, 5.1B active, 36 layers)
- [openai/gpt-oss-120b `config.json`](https://huggingface.co/openai/gpt-oss-120b) — `layer_types`, `sliding_window`,
  `num_attention_heads`, `num_key_value_heads`, `head_dim`, `num_local_experts`, `experts_per_token`,
  `quantization_config`

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

## Week 4 Progress: gpt-oss

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week4-progress-169.mp4](https://drive.google.com/file/d/1FWzFuXup1o193CtYY6ly_eCPAQJwVZOI/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 0:57.2 (57.17s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week4-progress.json`](beat_sheet-week4-progress.json)

### What the video covers

The week's progress update: what shipped (the gpt-oss explainer as two 4K masters with identical audio, 1:06.8
in eight beats), how the week went (read the model card and re-check every number, write one beat list for both
sheets, narrate and render at 4K, check clip lengths and frames in both orientations), what it taught (one learned
logit per head lets attention over real tokens sum to less than one; only the 18 full layers grow the cache, ≈ 4.8 GB
at 131,072 tokens; the cache arithmetic needs a byte size the config doesn't state, so it is labelled), and what is
still open (9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the gpt-oss section above
- OpenAI — gpt-oss-120b & gpt-oss-20b Model Card · [arXiv:2508.10925](https://arxiv.org/abs/2508.10925) — §2.2;
  [openai/gpt-oss-120b `config.json`](https://huggingface.co/openai/gpt-oss-120b)

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| Clip lengths vs measured audio | ✅ all 7 clips match the measured audio |
| GATE V — final frame check | ✅ clean — 0 BLOCKER, 0 MAJOR (14 frames) |
| GATE P — narration | ✅ signed off — Ritik B. |

### Build

Same pipeline and patterns as the explainer, as a single 16:9 master — from this week on, progress updates
ship in landscape only. It was authored after the explainer's frame check, so every quality figure on screen is
the measured result.
