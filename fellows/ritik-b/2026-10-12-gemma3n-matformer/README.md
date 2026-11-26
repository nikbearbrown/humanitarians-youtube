# Week of 2026-10-12

Two videos this week:

1. [Gemma 3n, Four Billion or Eight?](#gemma-3n-four-billion-or-eight)
2. [Week 7 Progress: Gemma 3n](#week-7-progress-gemma-3n)

---

## Gemma 3n, Four Billion or Eight?

- **Status:** complete — both masters built, frame QC done in both orientations; GATE P signed off by Ritik B.
- **Video (16:9):** [gemma3n-matformer-169.mp4](https://drive.google.com/file/d/1ecxen2e4xvbiZo83H5xzRbLQ7neofgjC/view)
- **Video (9:16):** [gemma3n-matformer-916.mp4](https://drive.google.com/file/d/1B1sF6GyBDoeSwhMDUEY571lo56eVhext/view)
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:12.3 (72.25s), 8 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content, same audio
- **Beat sheets:** [`beat_sheet.json`](beat_sheet.json) · [`beat_sheet-916.json`](beat_sheet-916.json)

### What the video teaches

Google calls Gemma 3n's larger model **E4B** — "effectively" four billion parameters — but its weights add up
to about eight. The reel finds the other four, every number from `config.json`, the safetensors index or Google's
Gemma 3n docs:

- **The nesting (MatFormer).** E2B is not a separate model: it is 30 of E4B's 35 layers at half the feed-forward
  width (8,192 vs 16,384), carved out of E4B's own weights. Both use 4 sliding-window layers (512 tokens) to every
  global layer.
- **Per-layer embeddings.** Besides the usual 2,048-number input embedding, each of the 35 layers gets its own
  256-number vector per token. They are table lookups, not matrix multiplies, so Google documents caching them on
  CPU or fast storage.
- **The arithmetic (computed).** The PLE table is 262,144 × 35 × 256 = 2,348,810,240 ≈ 2.35B parameters of E4B's
  8,387,373,392 (safetensors index). For E2B, Google's own figure is over 5B parameters loaded under standard
  execution and 1.91B "effective" with PLE caching and parameter skipping.
- **What "effective" hides.** It is a memory load, not a parameter count: all 8.4B still ship and still run. The
  hand-off measures whether the memory was saved or just moved to the CPU.

### Sources

- Google — *Gemma 3n model overview* · [ai.google.dev/gemma/docs/gemma-3n](https://ai.google.dev/gemma/docs/gemma-3n) —
  effective parameters (E2B: over 5B loaded, 1.91B effective, Fig. 1), PLE caching, MatFormer, MobileNet-V5
- `gemma-3n-E4B-it` / `gemma-3n-E2B-it` `config.json` and `model.safetensors.index.json` (read via the unsloth
  mirrors) · [E4B](https://huggingface.co/unsloth/gemma-3n-E4B-it) · [E2B](https://huggingface.co/unsloth/gemma-3n-E2B-it) —
  layers, FFN widths, sliding window, per-layer embedding size, total parameters

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

## Week 7 Progress: Gemma 3n

- **Status:** complete — 16:9 master built, frame QC done; GATE P signed off by Ritik B.
- **Video (16:9):** [week7-progress-169.mp4](https://drive.google.com/file/d/1qnJwJuX7-7GkQggGNiNLEkrPqT3gpA0x/view)
- **Playlist / chapter:** Weekly progress updates
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:00.7 (60.69s), 7 beats
- **Resolution:** 3840×2160 (16:9)
- **Beat sheet:** [`beat_sheet-week7-progress.json`](beat_sheet-week7-progress.json)

### What the video covers

The week's progress update (16:9 only): what shipped (the Gemma 3n explainer as two 4K masters with identical
audio, re-cut from the drafted 9-beat teardown to 8 beats on patterns that all have 9:16 twins, with no new scene
code), how the week went (read the docs, both configs and both weight indexes; re-cut; narrate and render at 4K; check
clip lengths, frames and loudness — clean in both orientations on the first pass), what it taught (Google's
"effective" figure is for E2B — 1.91B of over 5B loaded — not E4B, whose weights total 8.39B with 2.35B of per-layer
embeddings), and what is still open (9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`).

### Sources

- This week's explainer: [`beat_sheet.json`](beat_sheet.json) and the Gemma 3n section above
- Google — Gemma 3n model overview · [ai.google.dev/gemma/docs/gemma-3n](https://ai.google.dev/gemma/docs/gemma-3n)
- `gemma-3n-E4B-it` / `E2B-it` `config.json` + safetensors index · [huggingface.co/unsloth/gemma-3n-E4B-it](https://huggingface.co/unsloth/gemma-3n-E4B-it)

### Quality gates

| Gate | 16:9 |
|---|---|
| GATE L — beat-sheet lint | ✅ clean |
| Clip lengths vs measured audio | ✅ 7/7 match |
| GATE V — final frame check | ✅ clean (0 BLOCKER / 0 MAJOR, 14 frames) |
| GATE P — narration | ✅ signed off — Ritik B. |
