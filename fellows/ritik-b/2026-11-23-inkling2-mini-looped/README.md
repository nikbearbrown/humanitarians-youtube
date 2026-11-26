# Week of 2026-11-23

Two videos this week:

1. [Inkling 2 Mini, Looped Is Better?](#inkling-2-mini-looped-is-better)
2. [Week 13 Progress: Inkling 2 Mini](#week-13-progress-inkling-2-mini)

---

## Inkling 2 Mini, Looped Is Better?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [inkling2-mini-looped-169.mp4](https://drive.google.com/file/d/1N6uIPn9NCNa_1ZSzIrA1yzXO36-L6Ra5/view)
- **Video (9:16):** [inkling2-mini-looped-916.mp4](https://drive.google.com/file/d/1s4aH7dZ-FrY3s4uu-jstimCpI1yGwSGW/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 2:07.8 (127.75s), 11 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

Inkling 2 Mini (Thinking Machines, released November 20, 2026) is the lab's first released looped transformer: a
26.4B-parameter mixture-of-experts model that runs its middle 12 layers three times for every token. The reel teaches a
three-step audit you can reuse on any open model — **read the config, compute the cost, check each claim against its
evidence** — and runs it on this model, one step per beat:

- **Read the config.** `config.json` has 24 layers (in attention-residual blocks of 6), each routing a token to 8 of 128
  experts, and `loop_config` says `core_start 6`, `core_end 18`, `num_passes 3`. The config counts from 0, so counting from 1 that is layers 7–18
  (the lab's own label), run three times with shared weights: 6 + 12 × 3 + 6 = **48 layer applications per token from 24
  stored**.
- **Compute the cost.** One pass uses 3.4B parameters (lab-reported). One looped layer is attention (18.9M) plus 8 active
  experts (8 × 8.0M), about 83M; × 12 layers ≈ 0.99B per extra pass, computed from the config's dimensions. Two extra
  passes: 3.4 + 2 × 1.0 = **5.4B per token**, which is the figure the lab's table lists as "activated". The tension: the
  post's text says "3.4B active", its table says 5.4B. Memory follows the stored count (26.4B, ≈20 GB in NVFP4 + MXFP8);
  speed and cost follow the per-token count — looping saves memory, not compute.
- **Check the claim.** The lab says looping the middle beat looping the end on 27 of 28 evaluations; its chart shows a
  no-loop run needing 1.51–1.91× the compute to match the middle loop vs 1.24–1.36× for the end, at training step
  2,000 — the ranges don't overlap, but it is one checkpoint and the 28 evaluations aren't listed. The bigger claim,
  "over 50% more compute-efficient" than not looping, rests on one sentence (a scaling-law prediction on unpruned test
  runs, where the no-loop run cost 7.5% less to train), with no curves, run sizes or outside replication cited. What
  would break "looped is better"? Facts: on the lab's variable-loop model, going from 1 pass to 3 lifts GraphWalks BFS
  256K from 21.1% to 63.2% but SimpleQA Verified only from 6.3% to 7.3% — and the lab's caveat that 1-pass scores may
  understate applies to both.

The verdict scores the claims by evidence type: the loop is **verified** (config), the cost is **computed**, the
middle-vs-end and 50% claims are **lab-only**, and the lab's own data says looping buys reasoning, not recall. The
handoff gives a runnable test: a ~5B-active non-looped rival (match per-token compute, not the 3.4B headline), 30
reasoning and 30 closed-book questions, with what a good and a flagged result look like.

Three things need care, and the reel handles them on screen or leaves them out:

- **3.4B vs 5.4B.** Both are the lab's. The model card reconciles them (each extra pass adds about 1.0B effective active
  parameters), and the reel recomputes that increment from `config.json` (0.99B). The one-pass 3.4B is not recomputed —
  it depends on how embeddings, the vision encoder and the multi-token-prediction head are counted — so it is labelled
  lab-reported.
- **A claim the lab's own table contradicts.** The post's Limitations section says Inkling 2 Mini is behind Qwen3.8-27B
  on ComplexConstraints v1.1 (33.4%), but the comparison table in the same post and in the model card lists Qwen3.8-27B
  at 30.1% on that row. The draft carried the sentence; this cut leaves it out.
- **What isn't published.** The 28 evaluations behind "27 of 28" are not listed in the post or the model card, and the
  50% comparison has no published curves; the reel says so rather than filling the gap.

### Sources

- Thinking Machines — *Introducing Inkling 2 Mini* (Nov 20, 2026) ·
  [thinkingmachines.ai/news/inkling-2-mini](https://thinkingmachines.ai/news/inkling-2-mini/) — 26.4B total, 3.4B
  active, 5.4B "weight activations per token"; four blocks of six, 48 layer applications; 27 of 28 evaluations; the
  compute-equivalent chart (1.51–1.91× vs 1.24–1.36× at step 2,000); the message gate; 7.5% and "over 50% more
  compute-efficient"; ≈20 GB in NVFP4 + MXFP8; "knowledge is mostly a function of total parameter count"
- Thinking Machines — *Inkling 2 Mini* model card and `config.json` ·
  [huggingface.co/thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) —
  `num_hidden_layers 24`, `n_layers_per_attn_res_block 6`, `loop_config` (`core_start 6`, `core_end 18`,
  `num_passes 3`, `gate_rank 64`, `is_varloop false`), `n_routed_experts 128`, `num_experts_per_tok 8`,
  `n_shared_experts 0`, `hidden_size 2304`, `intermediate_size 1152`, 24 query / 8 key-value heads × 128; "each extra
  pass … adds about 1.0B effective active parameters"; "compute per token is higher than the active-parameter count
  alone suggests"
- Thinking Machines — *TML-d24-varloop-research* model card ·
  [huggingface.co/thinkingmachines/TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)
  — per-pass evaluations (GraphWalks BFS 256K 21.1% → 63.2%, SimpleQA Verified 6.3% → 7.3%, 1 → 3 passes) and the
  1:2:6:2:1 pass-count training mix behind the "may understate" caveat
- Kimi Team (Chen et al.) — *Attention Residuals* · [arXiv:2603.15031](https://arxiv.org/abs/2603.15031) — the
  residual scheme the lab uses to pass each loop's message forward (cited by the lab; background for the loop, not voiced
  in this cut)

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| PROOF self-review (before render) — [`PROOF-REVIEW.md`](PROOF-REVIEW.md) | 11/12 · production gate PASS (first pass 10/12, gate FAIL) | same |
| Clip lengths vs measured audio | ✅ all 11 clips match their beats | ✅ all 11 clips match their beats |
| GATE V — final frame check | ✅ clean — 22 frames, 0 BLOCKER, 0 MAJOR | ✅ clean — 22 frames, 0 BLOCKER, 0 MAJOR |
| PROOF frame review (after render) | ✅ PASS after 1 fix — B02 row 3 said "Zero-indexed: layers 7–18" (that range counts from 1); reworded, B02 re-rendered in both cuts | ✅ PASS — same B02 fix; otherwise no clipping or overlap |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Toolkit-only: every beat uses an existing brutalist.art pattern that already has a registered 9:16 twin
(`ClaudeComposerAsk`, `ReelExecSummary`, `ReelFramework`, `BlipLadder`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`),
so the reel builds with **no new scene code**. The researched draft in this folder was written for an `Inkling*` scene
family that was never built; it was re-cut from 12 beats (an estimated 2:51) to 11 on the six proven patterns, around a reusable
three-step audit, and self-reviewed against PROOF before any audio was generated. The portrait sheet is the landscape
sheet with `aspect_ratio: "9:16"` and a `916` suffix on every pattern, emitted from the same beat list, and both cuts
share one set of narration files, so they cannot drift. The `.mp4` masters are not in this repo — they are linked at
the top.

```bash
# in a brutalist.art clone, with each sheet copied into its own reel folder as beat_sheet.json
python3 runtime/scripts/generate_audio_kokoro.py <reel>          # Kokoro am_onyx — the clock
python3 runtime/scripts/remotion_scenes.py <reel>                # --scale=2 -> 4K
python3 runtime/scripts/compile.py <reel> --height 2160          # 9:16 twin: --height 3840
python3 runtime/qc/final_frame_check.py <reel>                   # GATE V
```

---

## Week 13 Progress: Inkling 2 Mini

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week13-progress-169.mp4](https://drive.google.com/file/d/1KEdkx06w4Vo8wOw6EMS3jlhwGDCfw6fj/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:02.5 (62.45s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week13-progress.json`](beat_sheet-week13-progress.json)

### What the video covers

The week's progress update, cut to about a minute: what shipped (the Inkling 2 Mini explainer as two 4K masters with
identical audio, 2:07.8, eleven beats on six toolkit patterns, no new scene code), how it was checked (four primary
sources, one claim dropped because the lab's own table contradicts it, the PROOF rubric before audio — 10/12 with the
gate failing, then 11/12 with it passing after fourteen fixes — and GATE V in both cuts), the lesson (evidence has to
land before the voice does), and what is still open (the explainer shows its tensions but resolves them for the
viewer — friction stayed at 1 of 2).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Inkling 2 Mini section above — measured
  narration, PROOF self-review, clip-length check and frame-check results from its build, in both orientations
- Thinking Machines — *Introducing Inkling 2 Mini* (Nov 20, 2026) ·
  [thinkingmachines.ai/news/inkling-2-mini](https://thinkingmachines.ai/news/inkling-2-mini/)

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| PROOF self-review (before render) — [`PROOF-REVIEW-week13-progress.md`](PROOF-REVIEW-week13-progress.md) | production gate PASS (2 edits before audio) |
| Clip lengths vs measured audio | ✅ all 7 clips match their beats |
| GATE V — final frame check | ✅ clean — 14 frames, 0 BLOCKER, 0 MAJOR |
| PROOF frame review (after render) | ✅ PASS — contact sheet read; labels fit, no overlap |
| GATE P — narration | ✅ signed off — Ritik B. |
