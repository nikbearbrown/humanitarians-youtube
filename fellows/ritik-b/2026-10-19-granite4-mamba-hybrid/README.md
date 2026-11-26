# Week of 2026-10-19

Two videos this week:

1. [Granite 4.0, Mostly Mamba?](#granite-40-mostly-mamba)
2. [Week 8 Progress: Granite 4.0](#week-8-progress-granite-40)

---

## Granite 4.0, Mostly Mamba?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [granite4-mamba-hybrid-169.mp4](https://drive.google.com/file/d/1fYeWFmFMB0kxK_cx2s8JeArL1uGAByhP/view)
- **Video (9:16):** [granite4-mamba-hybrid-916.mp4](https://drive.google.com/file/d/1FilXawY-8AZ_bYV2c5diV4mTZeojJPBm/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:15.2 (75.15s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

IBM's Granite 4.0-H-Small has 40 layers and only four of them are attention; the other 36 are **Mamba-2**
state-space layers. The reel takes the hybrid apart, every number from `config.json`, the model card or the Mamba-2
paper:

- **The layout.** Attention sits at layers 6, 16, 26 and 36 only (32 query heads, 8 KV heads); every layer routes
  each token to 10 of 72 experts plus a shared expert; 32B parameters in total, 9B active, 128K context.
- **No position encoding.** On its own an attention score q · k doesn't depend on where the key sits. Mamba-2
  updates a state token by token (h ← A·h + B·x, read out as y = C·h — §2.1, eq. 2), so order is built in and the
  attention layers run with `position_embedding_type: nope`.
- **The memory math (computed, BF16).** Four attention layers cache 4 × 8 × 128 × 2 = 8,192 values per token: about
  0.54 GB at 32K tokens and 2.1 GB at 131,072. If all 40 layers were attention it would be about 21.5 GB. The Mamba
  state is 128 heads × 64 × 128 per layer × 36 layers ≈ 75 MB, at any length.
- **The open question.** The state is small because it compresses, so exact lookup of one old token rests on four
  layers. The hand-off gives a needle test at 4K, 32K and 128K tokens to find where the hybrid starts to miss.

### Sources

- IBM — *granite-4.0-h-small* model card and `config.json` ·
  [huggingface.co/ibm-granite/granite-4.0-h-small](https://huggingface.co/ibm-granite/granite-4.0-h-small) —
  layer types, head counts, experts, Mamba-2 state size, NoPE, 32B / 9B, 128K
- Dao & Gu — *Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space
  Duality* (Mamba-2) · [arXiv:2405.21060](https://arxiv.org/abs/2405.21060) — §2.1, eq. 2 (selective SSM recurrence)

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| Clip lengths vs measured audio | ✅ 8/8 match | ✅ 8/8 match |
| GATE V — final frame check | ✅ clean (0 BLOCKER / 0 MAJOR, 16 frames) | ✅ clean (0 BLOCKER / 0 MAJOR, 16 frames) |
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

## Week 8 Progress: Granite 4.0

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week8-progress-169.mp4](https://drive.google.com/file/d/1lbDOFUorgvt8Ass1yJjSBAsF9eaQK_CA/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 0:58.5 (58.49s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week8-progress.json`](beat_sheet-week8-progress.json)

### What the video covers

The week's progress update (16:9 only): what shipped (the Granite 4.0 explainer as two 4K masters with identical
audio, re-cut from the drafted 9-beat teardown to 8 beats on patterns that all have 9:16 twins, with no new scene
code), how the week went (read the model card, `config.json` and the Mamba-2 paper; re-cut; narrate and render at 4K;
check clip lengths, frames and loudness — clean in both orientations on the first pass), what it taught (cite a claim
to the page that makes it: the draft credited a vendor memory pitch to the model card, which never mentions memory, so
it was cut; and a 75 MB state reads 0.1 on a gigabyte axis, so its label carries the MB figure), and what is still
open (9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Granite 4.0 section above
- ibm-granite/granite-4.0-h-small model card + `config.json` · [huggingface.co/ibm-granite/granite-4.0-h-small](https://huggingface.co/ibm-granite/granite-4.0-h-small)
- Dao & Gu — Mamba-2 · [arXiv:2405.21060](https://arxiv.org/abs/2405.21060) — §2.1, eq. 2

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| Clip lengths vs measured audio | ✅ 7/7 match |
| GATE V — final frame check | ✅ clean (0 BLOCKER / 0 MAJOR, 14 frames) |
| GATE P — narration | ✅ signed off — Ritik B. |
