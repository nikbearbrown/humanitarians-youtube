# Week of 2026-09-07

Two videos this week:

1. [BLIP-2, How Much Can You Freeze?](#blip-2-how-much-can-you-freeze)
2. [Week 2 Progress: BLIP-2](#week-2-progress-blip-2)

---

## BLIP-2, How Much Can You Freeze?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [blip2-frozen-169.mp4](https://drive.google.com/file/d/1lDngIFeZlZUq1cu9UXBUlBPIt4fXL_2m/view)
- **Video (9:16):** [blip2-frozen-916.mp4](https://drive.google.com/file/d/1lhbFj5KyhcCLOqszDQ47ZW7qkDYFDCmH/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:57.6 (117.63s), 11 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

BLIP-2 keeps a pretrained image encoder and a pretrained language model frozen and trains only a small
querying transformer (the Q-Former, 188M parameters, 32 learned queries) between them. The reel runs a
four-question **freeze audit** — what is frozen, what trains, how much of the image reaches the frozen LLM,
and where freezing loses — against the paper's own tables:

- **The bridge.** 32 × 768 query outputs stand in for the frozen ViT-L/14's 257 × 1024 features (§3.1).
- **Two stages.** First the queries learn contrastive, matching and image-grounded generation losses against the
  frozen image encoder; then one linear layer turns them into soft visual prompts for the frozen LLM (§3.2–3.3).
- **The receipt, and its condition.** Zero-shot VQAv2 65.0 against Flamingo80B's 56.3 with "54x fewer trainable
  parameters" — but with OPT as the frozen LLM the same bridge scores 52.3 and 52.6, below Flamingo (Table 2).
- **The bill.** On OK-VQA Flamingo80B still wins, 50.6 to 45.9, which the paper attributes to the knowledge in its
  70B LLM; skipping stage 1 sharply lowers zero-shot VQA (Fig. 5); in-context examples don't help, and the frozen
  LLM's risks are inherited (§5).

One number needs care: Table 1 lists the Q-Former's 188M as BLIP-2's trainable parameters (the basis of the 54x
claim), while Table 2 lists 103M–108M per configuration. The reel uses 188M only where the paper itself does.

### Sources

- Li, Li, Savarese & Hoi — *BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large
  Language Models*, ICML 2023 · [arXiv:2301.12597](https://arxiv.org/abs/2301.12597) — §3.1–3.3, Tables 1–2, Fig. 5, §5
- Alayrac et al. — *Flamingo: a Visual Language Model for Few-Shot Learning*, NeurIPS 2022 ·
  [arXiv:2204.14198](https://arxiv.org/abs/2204.14198) — Flamingo80B figures as reported in BLIP-2 Table 2

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | clean | clean |
| Clip lengths vs measured audio | all 11 match | all 11 match |
| GATE V — final frame check | clean | 1 MAJOR — end card fills 53% (min 55%) |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Toolkit-only: every beat uses an existing brutalist.art pattern that already has a registered 9:16 twin
(`ClaudeComposerAsk`, `ReelExecSummary`, `ReelFramework`, `ClaudeWindow`, `BlipLadder`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so the reel builds with **no new scene code**. The portrait sheet is the landscape sheet with
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

## Week 2 Progress: BLIP-2

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [week2-progress-169.mp4](https://drive.google.com/file/d/1ca-1iCnwY_edAiayc6BO3cM8IyQu7NES/view)
- **Video (9:16):** [week2-progress-916.mp4](https://drive.google.com/file/d/1gaPF3hE8dF7CSDIdTsVNsbSiTm-0vC-8/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:11.0 (71.03s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet-week2-progress.json`](beat_sheet-week2-progress.json) · [`beat_sheet-week2-progress-916.json`](beat_sheet-week2-progress-916.json)

### What the video covers

The week's progress update: what shipped (the BLIP-2 explainer as two 4K masters with identical audio), how
the week went (read and check every number, one beat list for both sheets, narrate and render at 4K, check
clip lengths and frames), what it taught (test a headline against every row of the table — BLIP-2's win holds
for FlanT5 but not for OPT), and what is still open (9:16 twins for
`ClaudeScienceLayerStack` and `ClaudeCodeBeat`). It also shows the reuse trend across the series' reels: new
scene components per reel went 7 (VQA) → 5 (BLIP) → 0 (BLIP-2).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the BLIP-2 section above
- Earlier reels' build logs, for the trend figures: [VQA and BLIP](../2026-09-01-vqa-blind/) —
  `BUILD-LOG.md` (7 components, 16 layout defects) and `BUILD-LOG-blip-bootstrap.md` (5 new, 12 defects)
- Li, Li, Savarese & Hoi — BLIP-2 · [arXiv:2301.12597](https://arxiv.org/abs/2301.12597) — Table 2

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | clean | clean |
| Clip lengths vs measured audio | all 8 match | all 8 match |
| GATE V — final frame check | clean | clean |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |
