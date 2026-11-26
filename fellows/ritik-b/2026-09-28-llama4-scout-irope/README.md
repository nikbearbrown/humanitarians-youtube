# Week of 2026-09-28

Two videos this week:

1. [Llama 4, Ten Million Tokens?](#llama-4-ten-million-tokens)
2. [Week 5 Progress: Llama 4 Scout](#week-5-progress-llama-4-scout)

---

## Llama 4, Ten Million Tokens?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [llama4-scout-irope-169.mp4](https://drive.google.com/file/d/12fnd2sgry17IVL7BSzihOUYolIrs_olJ/view)
- **Video (9:16):** [llama4-scout-irope-916.mp4](https://drive.google.com/file/d/1p1uiRlh6dxr_Q5c4TZlkxyPUmeDbNbf8/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:08.3 (68.28s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

How Llama 4 Scout mixes layers that know token position with layers that don't, what that means for how far a
single token can see, and why a configured 10,485,760-token maximum is not a result — figures from Meta's release
post or computed from `config.json`:

- **The pattern.** Every fourth layer (4, 8 … 48) has no position encoding and attends over the full causal context;
  the other 36 use RoPE and attend only inside 8,192-token chunks. Each token goes to 1 of 16 routed experts
  (`no_rope_layers`, `attention_chunk_size 8192`, `num_local_experts 16`). Meta calls the design iRoPE and pairs it
  with inference-time attention temperature scaling for length generalization.
- **The reach.** The token at (0-indexed) position 20,000 sits in the chunk 16,384–24,575, so in a RoPE layer it sees
  20,000 − 16,384 + 1 = 3,617 tokens; in a NoPE layer it sees all 20,001. Anything older than its chunk reaches it only
  through the 12 NoPE layers.
- **The claim.** `max_position_embeddings` is 10,485,760 — a ceiling the code allows. Meta says Scout was pre- and
  post-trained with a 256K context length. Quality at length has to be measured with retrieval and reasoning tests,
  not perplexity alone. The weights ship under the Llama 4 Community License, with use restrictions.

The 256K training length is Meta's statement in the release post; the 10,485,760 figure is the config value. The
reel shows both, side by side, rather than the "10M" headline alone.

### Sources

- Meta AI — *The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation* (Apr 5, 2025) ·
  [ai.meta.com](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) — 109B total / 17B active, 16 experts,
  iRoPE, 256K training context
- [Llama-4-Scout-17B-16E-Instruct `config.json`](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct) (read
  via the unsloth mirror) — `no_rope_layers`, `attention_chunk_size`, `num_hidden_layers`, `num_local_experts`,
  `num_experts_per_tok`, `max_position_embeddings`

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

## Week 5 Progress: Llama 4 Scout

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week5-progress-169.mp4](https://drive.google.com/file/d/1Hu8U1A8GMs46QfDu2Qi3Gj_L0UB8Jq2b/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 0:59.2 (59.19s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week5-progress.json`](beat_sheet-week5-progress.json)

### What the video covers

The week's progress update: what shipped (the Llama 4 Scout explainer as two 4K masters with identical audio,
1:08.3 in eight beats), how the week went (read the release post and re-check every number against `config.json`,
write one beat list for both sheets, narrate and render at 4K, check clip lengths and frames in both orientations),
what it taught (past its 8,192-token chunk a token hears older context only through the 12 NoPE layers; the
configured 10,485,760 sits far above the 256K context Meta says Scout was trained with), and what is still open
(9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Llama 4 section above
- Meta AI — The Llama 4 herd (Apr 5, 2025) · [ai.meta.com](https://ai.meta.com/blog/llama-4-multimodal-intelligence/);
  [Llama-4-Scout-17B-16E-Instruct `config.json`](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct)

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
