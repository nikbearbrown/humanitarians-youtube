# BUILD-PROMPT — Quantization: Big AI on a Laptop

Paste into Claude Code at the toolkit root:

> Rebuild youtube/brutalist/claude-hai-quantization as a review cut in 16:9 and 9:16. Re-run `.venv/bin/python youtube/brutalist/claude-hai-quantization/evidence/quant_toy.py` and confirm the on-screen numbers still match. Regenerate audio only if narration changed (`generate_audio_kokoro.py <reel> --speed 1.2`, then rebalance trailing silence so the per-beat ceil(duration × 24) sums to 1440; copy mp3/ into vertical/mp3/), set each beat's `durationSeconds` to its `actual_duration_s`, render both sheets with `python3 runtime/scripts/remotion_scenes.py <reel>[/vertical] --force`, compile with `./art run <reel>` and `./art run <reel>/vertical --height 3840`, sample frames into `_qc/`, read them, fix any BLOCKER/MAJOR and log it in `_qc/REPORT.md`. Never publish.
