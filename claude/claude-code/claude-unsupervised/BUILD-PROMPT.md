# BUILD-PROMPT — claude-unsupervised

Paste into Claude Code from books/:

```
Build the claude-unsupervised reel end to end and produce brutalist-art/youtube/claude-unsupervised/media/final-cut.mp4 in my ElevenLabs voice.

Ground truth, read first: (1) brutalist-art/youtube/claude-unsupervised/beat_sheet.json — THE MASTER: B00 ASK (ClaudeComposerAsk cold open, greeting "Merhaba, Bear") · B01 THE FLAG (Onda code-block on claude-window blank view — the dark glass block is NEVER re-skinned) · B02–B06 one lesson per beat (ClaudeUsageBeat: composer view + sparkLine + accumulating callouts, command pre-typed) · B07 VERDICT (artifact view, the seatbelt rules) · B08 HANDOFF (composer, greeting 'Your turn.', paste-ready prompt, type-on) · B09 ClaudeTitleOutro restating "Claude, unsupervised." (2) remotion-src/Unsupervised.tsx beside it — the working composition. (3) brutalist-art/CLAUDE-BRAND.md — the laws.

Execute: 1. GATE P: verify PEDAGOGY.md contains "VERDICT: PASS" (it does; never bypass). 2. From brutalist-art/: python3 runtime/scripts/generate_audio.py youtube/claude-unsupervised/ (ELEVENLABS_VOICE_NIKBEARBROWN from .env). 3. ffprobe each mp3 → actual_duration_s into beat_sheet.json. 4. Host in brutalist-art/skills/make/component-showcase/remotion; copy remotion-src/* into src/; rewire imports (claude-window, claude-callout, code-block from vox/remotion/_bench/onda/registry/components/; ClaudeComposerAsk + tokens/claude from brutalist-art/runtime/remotion/src/); DELETE the Caption component (previz-only). 5. Conform: regenerate unsup_timing.json from real mp3s — frames = ceil((duration + 0.4) * 30) — copy mp3s to public/mp3/ and update timing audio paths from "mp3-unsup/..." to "mp3/...". 6. Render at --scale=1.5 (authored 1280x720 → 1920x1080) to media/final-cut.mp4. 7. QC: audio stream present, duration = frames/30 ±0.2s; stills of B00, B01, B04, B07, B08 — spark lines beside the asterisk, code block legible, arrows on targets, outro restates the title. 8. Never publish. Report durations, runtime, QC, path.
```
