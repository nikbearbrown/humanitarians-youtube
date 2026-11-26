# Week of 2026-10-05

Two videos this week:

1. [Qwen3-Next, Attention Optional?](#qwen3-next-attention-optional)
2. [Week 6 Progress: Qwen3-Next](#week-6-progress-qwen3-next)

---

## Qwen3-Next, Attention Optional?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [qwen3-next-deltanet-169.mp4](https://drive.google.com/file/d/1_6PASUqL2PReeNowLO2LA6053S3bjs6f/view)
- **Video (9:16):** [qwen3-next-deltanet-916.mp4](https://drive.google.com/file/d/1GQkZMLLG_GcUFzEwDPYhSG7nQZ0z3MZF/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:07.0 (66.99s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

Qwen3-Next-80B-A3B replaces three of every four attention layers with **Gated DeltaNet**, a linear-attention
layer whose memory is a fixed-size matrix instead of a cache that grows with every token. The reel takes it apart
in four steps, every number from `config.json` or the Gated DeltaNet paper:

- **The layout.** 48 layers in 12 blocks of four: three Gated DeltaNet layers, then one full-attention layer with an
  output gate (16 query heads, 2 KV heads); after every layer, 10 of 512 routed experts plus 1 shared
  (`full_attention_interval 4`, model card hybrid layout).
- **The update.** Each value head keeps one 128 × 128 state. Per token a gate α fades the old memory, then the delta
  rule adds β times the error on this token's value along its key — the decay-then-correct form of §3.1, eq. 10.
- **The memory math (computed).** A full-attention layer caches 2 × 256 × 2 = 1,024 values per token; a DeltaNet
  layer's state is 32 × 128 × 128 = 524,288 values at any length. They break even at 512 tokens; at the full
  262,144-token context the cache is 512x larger.
- **The bill.** A fixed state compresses the past, so exact recall of one old token isn't guaranteed (the paper's
  §3.4 names fixed state size as the retrieval weakness) — which is why one layer in four keeps full attention.
  The hand-off gives a 20-key recall probe to measure it.

### Sources

- Qwen — *Qwen3-Next-80B-A3B-Instruct* model card and `config.json` ·
  [huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct) —
  hybrid layout, head counts, experts, 262,144-token context
- Yang, Kautz & Hatamizadeh — *Gated Delta Networks: Improving Mamba2 with Delta Rule* ·
  [arXiv:2412.06464](https://arxiv.org/abs/2412.06464) — §3.1 eq. 10 (gated delta rule), §3.4 (hybrids, retrieval)

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| Clip lengths vs measured audio | ✅ 8/8 match | ✅ 8/8 match |
| GATE V — final frame check | ✅ clean (0 BLOCKER / 0 MAJOR, 16 frames) | ✅ clean after one fix (end card re-titled; first pass: 2 MAJOR, outro underfill 49%) |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Toolkit-only: every beat uses an existing brutalist.art pattern that already has a registered 9:16 twin
(`ClaudeComposerAsk`, `ReelExecSummary`, `ReelFramework`, `BlipLadder`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`),
so the reel builds with **no new scene code**. The draft teardown's `ClaudeScienceLayerStack`, `ClaudeCodeBeat` and
`ClaudeWindow` beats were rewritten as `ReelFramework` rows and a `BlipLadder` chart, because the first two have no
9:16 twin and the third underfills a portrait frame. The portrait sheet is the landscape sheet with
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

## Week 6 Progress: Qwen3-Next

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week6-progress-169.mp4](https://drive.google.com/file/d/1-T4-hwaqwXvXrCtel4CoKyO0_QTlFQDJ/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 0:58.9 (58.85s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week6-progress.json`](beat_sheet-week6-progress.json)

### What the video covers

The week's progress update (16:9 only): what shipped (the Qwen3-Next explainer as two 4K masters with identical audio,
re-cut from the drafted 9-beat teardown to 8 beats on patterns that all have 9:16 twins, with no new scene code), how
the week went (read and re-check every number, re-cut, narrate and render at 4K, then check clip lengths, frames in
both orientations, and loudness — which caught a silent first 9:16 mix), what it taught (a ratio belongs to a context
length: a DeltaNet layer's state is 512x smaller than a full-attention layer's cache at 262,144 tokens, but equal to
it at 512), and what is still open (9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Qwen3-Next section above
- Qwen3-Next-80B-A3B `config.json` · [huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
- Yang, Kautz & Hatamizadeh — Gated Delta Networks · [arXiv:2412.06464](https://arxiv.org/abs/2412.06464) — §3.1 eq. 10

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| Clip lengths vs measured audio | ✅ 7/7 match |
| GATE V — final frame check | ✅ clean (0 BLOCKER / 0 MAJOR, 14 frames) |
| GATE P — narration | ✅ signed off — Ritik B. |
