# BUILD-PROMPT — Why MCP Exists

Paste into Claude Code at the toolkit root:

> Rebuild youtube/brutalist/claude-hai-mcp-protocol as a review cut in 16:9 and 9:16. Regenerate audio only if narration changed (`.venv/bin/python runtime/scripts/generate_audio_kokoro.py <reel>`), set each beat's `durationSeconds` to its `actual_duration_s`, render with `python3 runtime/scripts/remotion_scenes.py <reel> --force`, compile with `./art run <reel>`, then `./art vertical <reel>`, render the vertical sheet, and compile it with `--height 3840`. Sample frames into `_qc/`, read them, fix any BLOCKER/MAJOR, and log it in `_qc/REPORT.md`. Never publish.
