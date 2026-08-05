# BUILD-LOG — Nine Months at the Data Ceiling

Built 2026-08-04. Toolkit: `nikbearbrown/brutalist.art`, Fellow Tier. Cost $0.00.

## Environment

| | |
|---|---|
| Host | Arch Linux, kernel 7.1.3 |
| Python | **3.11 via conda env `brutalist`** — system Python 3.14 has no wheels for `manim<0.19` or `kokoro-onnx` |
| Node | v26.4.0 |
| ffmpeg | system, libx264 |
| LaTeX / dvisvgm | **absent** — Manim equation beats unavailable; reel authored to not require them |
| Kokoro model | ~340 MB, downloaded by `./setup --install` (not in the git repo) |

`./setup` readiness after install: audio, captions, Manim beats, Remotion,
slates/previz, fonts all READY. Manim *equation* beats blocked (LaTeX).

## Sequence

```
./setup --install
python3 runtime/scripts/generate_audio_kokoro.py <reel>    # 12 beats, af_bella
./art run   <reel>                                          # review cut
./art final <reel>                                          # clean master
```

## Measured audio (the master clock)

| Beat | s | Beat | s |
|---|---|---|---|
| B00 | 19.48 | B06 | 27.03 |
| B01 | 21.80 | B07 | 28.10 |
| B02 | 23.06 | B08 | 24.13 |
| B03 | 21.87 | B09 | 22.91 |
| B04 | 26.65 | B_CLI | 23.02 |
| B05 | 15.08 | B_OUTRO | 7.15 |

**Total 260.28s (4m20s).** Word-rate estimation at 155 wpm predicted 4m08s —
Kokoro paces ~5% slower than that. Estimates were re-synced from measured audio;
timing was never adjusted by hand.

## Output

- Master: 3840×2160, h264/aac, 260.28s, 9.5 MB, 12/12 slots filled, zero slates
- Scenes used: `ClaudeComposerAsk` (×2), `SlateCard` (×9), `BarChart` (×1),
  `OutroSeries` (×1) — all stock registered compositions, no custom TSX

## Failures and overrides

**1. Concurrent compiles — self-inflicted, resolved.** A second `./art run` was
started while the first was still rendering. It deleted the first run's
`media/_ext_B_CLI.mp4` temp, producing a `FileNotFoundError` in
`remotion_scenes.extend_clip_to_duration`, and the ffmpeg concat then died
half-written (output had no `moov` atom). No rendered beat was lost; re-running
the assembly against the intact `media/` resolved it. **Do not run two compiles
against one reel concurrently.**

**2. `./art run` output looks dead when piped.** The command's stdout piped
through `tail` buffers the entire stream until the pipeline closes, so a healthy
20-minute render appears to produce no output. Redirect to a file instead.

**3. GATE V failed — 24 blockers — overridden after verification.** Every sampled
frame reported `edge-bleed` at the title-safe right/top edge, including the
plain centred-text outro. That uniformity was the tell: the defect is the review
cut's own burn-ins — the timecode `drawtext` at `x=w-text_w-16:y=16` and the
bottom-left beat label — both of which sit hard against the frame edge and
**do not exist in the clean master**. Confirmed by extracting a frame from the
master and inspecting it directly before accepting the override. The gate is
evaluating the review artifact, not the deliverable.

**4. Motion-mix warning — accepted, documented.** `illustrate` carries 10/12
beats (83%) against the ~40% cap in `MOTION.md`. Consequence of using only stock
scenes. Legible but static; converting the excess requires per-beat custom
Remotion scenes. Recorded as known debt rather than silently ignored.

## Documentation discrepancies encountered

- `skills/make/hai/SKILL.md` specifies voice `af_kore`; `runtime/scripts/brand_variant.py`
  writes `af_bella`. The script is authoritative — `af_bella` used.
- `HOW-TO.md` says the Kokoro model ships inside the toolkit; it does not, and
  `./setup --install` downloads it.
- `HOW-TO.md` says `./art final` writes `<slug>-cut.mp4`; it writes `<slug>.mp4`.
- `HOW-TO.md` presents three builder skills flatly; `CLAUDE.md` tiers them, and
  `cli-explainer` / `deep-explainer` / `nbb` are ADVANCED (Bear only). Fellow Tier
  is `fellows`, `ai-explainer`, `hai`, `your-turn`, `duration-planner`. This reel
  uses the `ai-explainer` chassis on the `hai` brand, which is in tier.

## Gates

| Gate | State |
|---|---|
| GATE P (narration) | **signed** 2026-08-04 — see `PEDAGOGY.md` |
| GATE L (beat-mix lint) | clean |
| GATE V (visual QC) | failed on review cut; overridden after master-frame verification (see above) |
| Publishing | not authorized — master held locally |
