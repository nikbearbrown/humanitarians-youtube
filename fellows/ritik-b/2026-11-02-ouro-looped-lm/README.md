# Week of 2026-11-02

Two videos this week:

1. [Ouro, Smarter by Repeating?](#ouro-smarter-by-repeating)
2. [Week 10 Progress: Ouro](#week-10-progress-ouro)

---

## Ouro, Smarter by Repeating?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [ouro-looped-lm-169.mp4](https://drive.google.com/file/d/1nEsEcptbolj3M_1NaD8sblE6fU1ACdxe/view)
- **Video (9:16):** [ouro-looped-lm-916.mp4](https://drive.google.com/file/d/1MbTqtBZNpW2CseMdlH2dEv8LwUxbQf0V/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:07.9 (67.87s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

Ouro is ByteDance's family of looped language models (LoopLM): one stack of layers, run several times with the
same weights, so depth comes from repetition rather than from storing more layers. The reel counts what the headline
claim is counting:

- **The loop.** Ouro-2.6B runs one 48-layer stack up to 4 recurrent steps, refining the same hidden state each time
  (config.json: `num_hidden_layers 48`, `total_ut_steps 4`). After each step a learned exit gate can stop early; the
  paper trains depth allocation with an entropy-regularized objective, on 7.7T tokens.
- **The count.** 2.6B parameters stored, but 48 × 4 = 192 layer applications per token at full depth — about 10.1B
  dense-equivalent parameters of compute per token (4 × 2.47B looped layers + 0.20B embeddings and head, which run
  once), computed from config.json and the 2.67B-parameter checkpoint and labelled as computed.
- **Is "matches 12B" fair?** The abstract says the 1.4B and 2.6B models "match the results of up to 12B" models. That
  is fair on memory (2.6B weights to hold) and softer on compute (four passes cost about four times one). The paper's
  own controlled experiments credit "knowledge manipulation", not more knowledge capacity.

Two numbers need care. The Ouro-2.6B model card's table lists 24 layers, but its `config.json` says 48 and the
checkpoint's 2,667,974,657 parameters only add up with 48 (24 is the 1.4B model's depth), so the reel uses 48. And the
same model card claims the 2.6B model matches **3–4B** standard transformers, against the abstract's "up to 12B"; the
reel puts both on screen.

### Sources

- Zhu et al. (ByteDance Seed) — *Scaling Latent Reasoning via Looped Language Models* ·
  [arXiv:2510.25741](https://arxiv.org/abs/2510.25741) — abstract: LoopLM design, entropy-regularized depth allocation,
  7.7T tokens, "match the results of up to 12B", knowledge manipulation vs capacity
- ByteDance — *Ouro-2.6B* model card and `config.json` ·
  [huggingface.co/ByteDance/Ouro-2.6B](https://huggingface.co/ByteDance/Ouro-2.6B) — `num_hidden_layers 48`,
  `total_ut_steps 4`, `hidden_size 2048`, `vocab_size 49152`, adaptive exit, "Matches 3-4B" claim

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| Clip lengths vs measured audio | ✅ all 8 clips match their beats | ✅ all 8 clips match their beats |
| GATE V — final frame check | ✅ clean — 16 frames, 0 BLOCKER, 0 MAJOR | ✅ clean — 16 frames, 0 BLOCKER, 0 MAJOR |
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

## Week 10 Progress: Ouro

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week10-progress-169.mp4](https://drive.google.com/file/d/1JmD6r4JrgCwFjj84PWHtbaRTRsiBnK0d/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 0:58.3 (58.26s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week10-progress.json`](beat_sheet-week10-progress.json)

### What the video covers

The week's progress update: what shipped (the Ouro explainer as two 4K masters with identical audio), how the
week went (read the abstract, model card and config and check every number; re-cut the 9-beat draft to 8 beats on
patterns that have 9:16 twins; narrate and render at 4K, twice; check clip lengths and frames), what the sources taught
(count compute, not weights — four passes of the 2.6B model cost about 10.1B parameters' worth per token — and when the
model card and the config disagree on depth, the checkpoint's parameter count settles it), and what is still open (9:16
twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Ouro section above — measured narration,
  clip-length check and frame-check results from its build, in both orientations
- Zhu et al. (ByteDance Seed) — *Scaling Latent Reasoning via Looped Language Models* ·
  [arXiv:2510.25741](https://arxiv.org/abs/2510.25741)

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| Clip lengths vs measured audio | ✅ all 7 clips match their beats |
| GATE V — final frame check | ✅ clean — 14 frames, 0 BLOCKER, 0 MAJOR |
| GATE P — narration | ✅ signed off — Ritik B. |
