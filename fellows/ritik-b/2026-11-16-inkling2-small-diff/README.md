# Week of 2026-11-16

Two videos this week:

1. [Inkling 2 Small, What Changed?](#inkling-2-small-what-changed)
2. [Week 12 Progress: Inkling 2 Small](#week-12-progress-inkling-2-small)

---

## Inkling 2 Small, What Changed?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [inkling2-small-diff-169.mp4](https://drive.google.com/file/d/1iUqjp5Zr3d9qihruaI0kmUo9SeVotkpo/view)
- **Video (9:16):** [inkling2-small-diff-916.mp4](https://drive.google.com/file/d/1qRI3zhza49UrE339copmyZjH9CehGx4f/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 2:03.1 (123.11s), 10 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

Thinking Machines' first open model, Inkling (July 15), read images and audio with no encoder at all — by
design. Its second generation, Inkling 2 Small (announced November 5, weights November 12), brings a vision encoder
back and drops audio, and the announcement gives no reason. The reel runs a **config-first audit** you can reuse on
any open-weights model — diff the configs, recompute the headline, match every change to a published reason — and
scores each change CHECKED, OPEN or BORROWED:

- **Diff the configs.** 66 layers × 6,144 wide become 48 × 4,608; the local attention window doubles to 1,024 tokens;
  256 routed experts plus 2 shared (6 active) become 384 routed, 8 active, none shared; a 4-layer hMLP on 40-pixel
  patches becomes a 23-layer vision transformer on 20-pixel patches; the `audio_config` block is gone; and one key is
  new, `n_layers_per_attn_res_block: 6`.
- **Recompute the headline (computed).** One expert is 3 × 4,608 × 2,304 ≈ 31.9M parameters; 8 per token across 48
  layers is 12.2B, plus 3.2B of attention and 1.9B of input and output embeddings: 17.3B against the lab's 17B. With all
  384 experts, the multi-token-prediction head and the vision encoder, the total comes to ≈ 594.1B against 594B — and
  only with untied embeddings (tied would give 16.3B and 593.1B).
- **Friction.** Compute per token fell 59% (41B → 17B active), stored parameters only 39% (975B → 594B), and the model
  card asks for at least 500 GB of GPU memory to serve the NVFP4 checkpoint: "Small" per token, not to host.
- **Match change to reason.** The lab's "292M-parameter vision encoder based on Perception Encoder" checks out against
  `vision_config` (23 × 12 × 1,024² ≈ 289.4M before embeddings; 291.7–292.9M with them). Why encoder-free and audio
  were dropped is not published — the November post has no architecture section. Attention residuals are the hard
  case: the lab never mentions them; the nearest paper (Kimi Team, Block AttnRes) gives a reason, but its evidence comes
  from a different model, Kimi Linear (48B total / 3B active). Score: BORROWED.

The verdict: the *what* is fully auditable — both headline numbers reproduce from `config.json` — and the *why* is
open. The hand-off gives a copyable prompt for running the same audit on two generations of any model family, with
what a good and a flagged answer look like.

Two figures need care. The parameter recount assumes a gated (three-matrix) feed-forward layer — the config carries
`mlp_gate_softcap` and `mlp_up_softcap` — and leaves out the router (0.08B); the vision-encoder range depends on whether
the patch embedding includes the temporal axis. Both are labelled "computed" on screen with their assumptions.

### Sources

- Thinking Machines — *Introducing Inkling 2 Small* (Nov 5, 2026; weights Nov 12) ·
  [thinkingmachines.ai/news/inkling-2-small](https://thinkingmachines.ai/news/inkling-2-small/) — 594B / 17B, the
  292M Perception-Encoder-based vision encoder, 20×20 patches with 2×2 pooling, no audio
- Thinking Machines — *Inkling: Our Open-Weights Model* (Jul 15, 2026) ·
  [thinkingmachines.ai/news/introducing-inkling](https://thinkingmachines.ai/news/introducing-inkling/) — 975B / 41B,
  the encoder-free design (40×40 patches, four-layer hMLP; dMel audio)
- *Inkling 2 Small* model card and `config.json` ·
  [huggingface.co/thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) — layers,
  widths, experts, `vision_config`, `n_layers_per_attn_res_block`, ≥ 500 GB VRAM for the NVFP4 checkpoint
- *Inkling* model card and `config.json` ·
  [huggingface.co/thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling) — the other side of the diff
- Kimi Team — *Attention Residuals* · [arXiv:2603.15031](https://arxiv.org/abs/2603.15031) — abstract: Block AttnRes,
  evidence on Kimi Linear (48B total / 3B activated)

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| Clip lengths vs measured audio | ✅ all 10 clips match their beats | ✅ all 10 clips match their beats |
| GATE V — final frame check | ✅ clean — 20 frames, 0 BLOCKER, 0 MAJOR | ✅ clean — 20 frames, 0 BLOCKER, 0 MAJOR |
| PROOF self-review (before render) — [`PROOF-REVIEW.md`](PROOF-REVIEW.md) | 12/12 · production gate PASS (first pass 9/12, gate FAIL) | same |
| PROOF frame review (after render) | ✅ PASS — contact sheet read; every label fits its column, no clipping or overlap | ✅ PASS — contact sheet read; no clipping or overlap |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Toolkit-only: every beat uses an existing brutalist.art pattern that already has a registered 9:16 twin
(`ClaudeComposerAsk`, `ReelExecSummary`, `ReelFramework`, `BlipLadder`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`),
so the reel builds with **no new scene code**. The researched draft of this teardown (12 beats, about 2:48 by
estimate) was written for an `Inkling*` scene family — eight components such as `InklingDiff` and `InklingClaimCheck` —
that was never built; it was re-cut to 10 beats on the six proven patterns, around a three-step audit, and graded
against the PROOF rubric before any audio was generated. The portrait sheet is the landscape sheet with
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

## Week 12 Progress: Inkling 2 Small

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week12-progress-169.mp4](https://drive.google.com/file/d/1sJs0p8JcvJc-YmXKfu1glUItC3KRPpUO/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:50.6 (110.62s), 9 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week12-progress.json`](beat_sheet-week12-progress.json)

### What the video covers

The week's progress update: what shipped (the Inkling 2 Small explainer as two 4K masters with identical audio,
2:03.1, ten beats cut from a twelve-beat draft on six toolkit patterns, no new components), how it was checked (the
PROOF rubric before audio, clip lengths, GATE V in both cuts), what the pre-render review caught (a three-card roadmap
that forced a three-step rubric, two numbers voiced before they were readable, a computed figure made into an honest
range, and an inferred paper link relabelled), and what is still open (the November post gives no reasons for the
architecture changes).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Inkling 2 Small section above — measured
  narration, clip-length check, frame-check and PROOF results from its build, in both orientations
- Thinking Machines — *Introducing Inkling 2 Small* ·
  [thinkingmachines.ai/news/inkling-2-small](https://thinkingmachines.ai/news/inkling-2-small/)
- *Inkling 2 Small* `config.json` ·
  [huggingface.co/thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small)

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| Clip lengths vs measured audio | ✅ all 9 clips match their beats |
| GATE V — final frame check | ✅ clean — 18 frames, 0 BLOCKER, 0 MAJOR |
| PROOF self-review (before render) — [`PROOF-REVIEW-week12-progress.md`](PROOF-REVIEW-week12-progress.md) | production gate PASS · show-over-say PASS (3 edits before audio) |
| PROOF frame review (after render) | ✅ PASS — contact sheet read; labels fit, no overlap |
| GATE P — narration | ✅ signed off — Ritik B. |
