# Week of 2026-11-09

Two videos this week:

1. [Inkling, Encoder-Free at Scale?](#inkling-encoder-free-at-scale)
2. [Week 11 Progress: Inkling](#week-11-progress-inkling)

---

## Inkling, Encoder-Free at Scale?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [inkling-encoder-free-169.mp4](https://drive.google.com/file/d/1bCWA92UmQoMY3BFcxz0qiN3Ieh85s-_x/view)
- **Video (9:16):** [inkling-encoder-free-916.mp4](https://drive.google.com/file/d/1XdU-P2jDEcIhdPBmkRdCn7A_5CHfDQJd/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 2:07.5 (127.55s), 12 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

A reusable **four-step, config-first audit** for any open model — *read the config, compute the cost, check each
claim against a receipt, name what would break it* — shown as a structure before any example, then run on Thinking
Machines' Inkling (975B total, 41B active). Step 1 reads the stack from `config.json` and the weight map: 55
sliding-window (512-token) + 11 global layers, two dense layers then 6 of 256 routed experts + 2 shared, a learned
relative-position bias instead of RoPE, and image/audio input with no separate encoder (40×40 hMLP patches, dMel audio).
Step 2 computes the KV cache at 1,048,576 tokens row by row — 4.29 GB per global layer, 47 GB for Inkling's 11 vs 283 GB
if all 66 were global. The friction: that saving is real, but the BF16 checkpoint is 1.9 TB, so sparse compute is not
sparse memory. Step 3 marks each claim *verified* (the 5:1 layout, the encoder-free inputs), *ambiguous* (975B stated vs
≈952B implied by the checkpoint at 2 bytes per parameter) or *trust* (relative position beating RoPE — no published
ablation). Step 4 names a result that would break "the decoder perceives" (swap inputs for noise) beside the caveats
the lab flags itself. The handoff hands the viewer the same four steps for any open model, with what a good and a
flagged result look like.

### Sources

- Thinking Machines — *Introducing Inkling* (Jul 15, 2026) ·
  [thinkingmachines.ai/news/introducing-inkling](https://thinkingmachines.ai/news/introducing-inkling/)
- thinkingmachines/Inkling — model card (license: apache-2.0) and
  [`config.json`](https://huggingface.co/thinkingmachines/Inkling/blob/main/config.json) ·
  [huggingface.co/thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling)
- thinkingmachines/Inkling — [`model.safetensors.index.json`](https://huggingface.co/thinkingmachines/Inkling/blob/main/model.safetensors.index.json)
  (weight map: dense layers 1–2; `total_size` 1,904,604,285,204 bytes)

Every number on screen carries its source in the same frame. Computed figures (the KV-cache rows, 82 GB of active
weights, ≈952B) are labelled as computed, with the arithmetic on screen.

### Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat-sheet lint | ✅ clean | ✅ clean |
| PROOF self-review (before render) — [`PROOF-REVIEW.md`](PROOF-REVIEW.md) | 12/12 · production gate PASS (round 1: 10/12, gate FAIL — six edits) | same sheet |
| Clip lengths vs measured audio | ✅ all 12 clips match their beats | ✅ all 12 clips match their beats |
| GATE V — final frame check | ✅ clean — 0 BLOCKER, 0 MAJOR | ✅ clean — 0 BLOCKER, 0 MAJOR |
| PROOF frame review (after render) | ✅ PASS after 2 fixes — two framework labels ran into their text in 16:9 (GATE V passed them); shortened, B03 + B08 re-rendered in both cuts | ✅ PASS after 2 fixes — two framework labels ran into their text in 16:9 (GATE V passed them); shortened, B03 + B08 re-rendered in both cuts |
| GATE P — narration | ✅ signed off — Ritik B. | ✅ same |

### Build

Toolkit-only: every beat uses an existing brutalist.art pattern that already has a registered 9:16 twin
(`ClaudeComposerAsk`, `ReelFramework`, `BlipLadder`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so the reel builds
with **no new scene code**. The researched draft of this episode was written for eight new `Inkling*` scenes that were
never built; it was re-cut onto these patterns, structured to the PROOF teaching rubric, and self-reviewed before audio.
The portrait sheet is the landscape sheet with `aspect_ratio: "9:16"` and a `916` suffix on every pattern, emitted from
the same beat list, and both cuts share one set of narration files, so they cannot drift. The `.mp4` masters are not in
this repo — they are linked at the top.

```bash
# in a brutalist.art clone, with each sheet copied into its own reel folder as beat_sheet.json
python3 runtime/scripts/generate_audio_kokoro.py <reel>          # Kokoro am_onyx — the clock
python3 runtime/scripts/remotion_scenes.py <reel>                # --scale=2 -> 4K
python3 runtime/scripts/compile.py <reel> --height 2160          # 9:16 twin: --height 3840
python3 runtime/qc/final_frame_check.py <reel>                   # GATE V
```

---

## Week 11 Progress: Inkling

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week11-progress-169.mp4](https://drive.google.com/file/d/1r903O2hmjfupwFAMyCCh6cjS9-o3_5xL/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:52.2 (112.25s), 10 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week11-progress.json`](beat_sheet-week11-progress.json)

### What the video covers

The week's progress update: what shipped (the Inkling explainer as two 4K masters with identical audio), how the
week went (read `config.json`, the weight map, the model card and the announcement; re-cut a draft written for eight
unbuilt scenes onto six proven patterns; review the beat sheet with the PROOF teaching rubric before any audio; narrate,
render at 4K twice, check clip lengths and frames), what the review caught (a worked example whose arithmetic was spoken
before it appeared, three claims voiced but never shown, and a "break it" step with no test — round 1 scored 10/12 with
the production gate failing, round 2 scored 12/12 with it passing, after six edits and no re-renders), what the sources
corrected (the contamination wording; the dense layers confirmed in the weight map), what the frame check caught after
rendering (two framework labels running into their text in 16:9, which the automated gate passed), and what is still
open (975B stated vs ≈952B implied by the checkpoint).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Inkling section above — measured narration,
  PROOF self-review, clip-length check and frame-check results from its build, in both orientations
- Thinking Machines — *Introducing Inkling* (Jul 15, 2026) ·
  [thinkingmachines.ai/news/introducing-inkling](https://thinkingmachines.ai/news/introducing-inkling/)
- thinkingmachines/Inkling — model card, `config.json` and `model.safetensors.index.json` ·
  [huggingface.co/thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling)

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| PROOF self-review (before render) — [`PROOF-REVIEW-week11-progress.md`](PROOF-REVIEW-week11-progress.md) | production gate PASS (one edit: narration counted five moves over four rows) |
| Clip lengths vs measured audio | ✅ all 10 clips match their beats |
| GATE V — final frame check | ✅ clean — 0 BLOCKER, 0 MAJOR |
| PROOF frame review (after render) | ✅ PASS |
| GATE P — narration | ✅ signed off — Ritik B. |
