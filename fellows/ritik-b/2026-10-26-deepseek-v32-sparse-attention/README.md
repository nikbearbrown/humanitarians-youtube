# Week of 2026-10-26

Two videos this week:

1. [DeepSeek-V3.2, Sparse Enough?](#deepseek-v32-sparse-enough)
2. [Week 9 Progress: DeepSeek-V3.2](#week-9-progress-deepseek-v32)

---

## DeepSeek-V3.2, Sparse Enough?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [deepseek-v32-sparse-attention-169.mp4](https://drive.google.com/file/d/1cDOqNkpBt_bPW6HNqd3gqOcuW1L0xDPr/view)
- **Video (9:16):** [deepseek-v32-sparse-attention-916.mp4](https://drive.google.com/file/d/1qCq_Oq8fKMoOqMAcinjWRUB-d7qioJaZ/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:11.9 (71.86s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

DeepSeek-V3.2-Exp keeps DeepSeek-V3's 671B / 37B mixture-of-experts base (continued from V3.1-Terminus) and
changes one thing: **DeepSeek Sparse Attention** — decide where each token looks before attention runs. The reel
follows that one change through three beats of evidence:

- **The indexer.** A lightning indexer — 64 heads × 128 dims, in FP8 — scores every earlier token; only the top
  2,048 per query reach multi-head latent attention. Everything else is V3: 256 routed + 1 shared experts, 61 layers
  (config.json: `index_n_heads 64`, `index_head_dim 128`, `index_topk 2048`).
- **The count.** At 131,072 tokens, dense causal attention scores ≈ 8.6B query–key pairs (L²/2); sparse main
  attention scores ≈ 268M (L × 2,048) — 32x fewer. Both figures are computed from config.json and labelled as computed.
- **What stays quadratic.** The indexer still scores all ≈ 8.6B pairs — cheaper per pair, not fewer pairs — and
  selection is a hard cut: a token the indexer misses is invisible to main attention. DeepSeek reports quality on par
  with V3.1-Terminus and labels the release experimental.

One number needs care: 268M is an upper bound (the first 2,048 queries have fewer than 2,048 earlier tokens to pick
from), so "32x" is the long-context ratio L / (2 × 2,048), not a measured speed-up.

### Sources

- deepseek-ai — *DeepSeek-V3.2-Exp* model card and `config.json` ·
  [huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) —
  `index_n_heads`, `index_head_dim`, `index_topk`, `num_hidden_layers`, `n_routed_experts`, `n_shared_experts`
- DeepSeek-AI — *DeepSeek-V3.2-Exp* technical report (repository) ·
  [github.com/deepseek-ai/DeepSeek-V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) — lightning indexer,
  FP8 index scores, top-k selection, quality against V3.1-Terminus

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| Clip lengths vs measured audio | ✅ all 8 clips match their beats | ✅ all 8 clips match their beats |
| GATE V — final frame check | ✅ clean — 16 frames, 0 BLOCKER, 0 MAJOR | ✅ clean — 16 frames, 0 BLOCKER, 0 MAJOR (first pass: B00 title edge-bleed + B07 outro underfill, fixed with props) |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Toolkit-only: every beat uses an existing brutalist.art pattern that already has a registered 9:16 twin
(`ClaudeComposerAsk`, `ReelExecSummary`, `ReelFramework`, `BlipLadder`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`),
so the reel builds with **no new scene code**. The first draft of this teardown used `ClaudeScienceLayerStack` and `ClaudeCodeBeat`, which have no 9:16 twin, so it was re-cut from 9 beats to 8 with those beats rebuilt as `ReelFramework` rows and a `BlipLadder` count. The portrait sheet is the landscape sheet with
`aspect_ratio: "9:16"` and a `916` suffix on every pattern, emitted from the same beat list, and both cuts share one
set of narration files, so they cannot drift. The `.mp4` masters are not in this repo — they are linked at the top.

```bash
# in a brutalist.art clone, with each sheet copied into its own reel folder as beat_sheet.json
python3 runtime/scripts/generate_audio_kokoro.py <reel>          # Kokoro am_onyx — the clock
python3 runtime/scripts/remotion_scenes.py <reel>                # --scale=2 -> 4K
python3 runtime/scripts/compile.py <reel> --height 2160          # 9:16 twin: --height 3840
python3 runtime/qc/final_frame_check.py <reel>                   # GATE V
```

---

## Week 9 Progress: DeepSeek-V3.2

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week9-progress-169.mp4](https://drive.google.com/file/d/103LBoK9lYGsmQa_6alrbZvcO6n8U_00Q/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 0:59.5 (59.51s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week9-progress.json`](beat_sheet-week9-progress.json)

### What the video covers

The week's progress update: what shipped (the DeepSeek-V3.2 explainer as two 4K masters with identical audio),
how the week went (read the report and config and check every number; re-cut the 9-beat draft to 8 beats on patterns
that have 9:16 twins; narrate and render at 4K, twice; check clip lengths and frames), what the paper taught (sparse
attention is two costs, not one — main attention scores 32x fewer pairs at 131,072 tokens while the indexer still
scores every pair), and what is still open (9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the DeepSeek-V3.2 section above — measured
  narration, clip-length check and frame-check results from its build, in both orientations
- deepseek-ai — *DeepSeek-V3.2-Exp* model card and `config.json` ·
  [huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp)

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| Clip lengths vs measured audio | ✅ all 7 clips match their beats |
| GATE V — final frame check | ✅ clean — 14 frames, 0 BLOCKER, 0 MAJOR |
| GATE P — narration | ✅ signed off — Ritik B. |
