# BUILD-PROMPT — RLHF: How Chatbots Learned to Help

Paste into Claude Code at the toolkit root:

> Rebuild youtube/brutalist/claude-hai-rlhf as a review cut in 16:9 and 9:16. Re-run `.venv/bin/python youtube/brutalist/claude-hai-rlhf/evidence/rlhf_toy.py` and confirm the on-screen numbers (defaults in runtime/remotion/src/RLHF.tsx) still match. Narration lives in `evidence/build_sheets.py` (writes both sheets). If narration changed: regenerate those beats with `generate_audio_kokoro.py <reel> --speed 1.25 --only <ids>` (B00/B10 at 1.2), delete their `mp3/_raw/` copies, then `python3 <reel>/evidence/balance_audio.py` (trims tails so frames sum to 1440, copies mp3/ to vertical/). Render with `python3 runtime/scripts/remotion_scenes.py <reel>[/vertical] --force`, compile with `./art run <reel>` and `./art run <reel>/vertical --height 3840`, sample frames into `_qc/`, read them, fix any BLOCKER/MAJOR and log it in `_qc/REPORT.md`. Never publish.
