# BUILD-PROMPT — claude-liam-brand-guidelines

Standalone rebuild prompt. Run from `books/brutalist-art/`.

```text
Build the final cut of the brand-guidelines skill-teardown reel end to end.
Reel folder: ../anthropics/skills/youtube/claude-liam-brand-guidelines/

Steps:
1. Verify PEDAGOGY.md ends "VERDICT: PASS" — stop if not.
2. Generate Kokoro audio (free, no spend approval needed):
   python3 runtime/scripts/generate_audio_kokoro.py ../anthropics/skills/youtube/claude-liam-brand-guidelines/
3. Render all Remotion beats (foreground, --concurrency=1):
   python3 runtime/scripts/remotion_scenes.py ../anthropics/skills/youtube/claude-liam-brand-guidelines/
4. Assemble with compile.py:
   python3 runtime/scripts/compile.py ../anthropics/skills/youtube/claude-liam-brand-guidelines/
5. Visual QC: sample frames at 2fps + each beat at ~15/50/85%:
   ffmpeg -i ../anthropics/skills/youtube/claude-liam-brand-guidelines/mp4/claude-liam-brand-guidelines.mp4 \
     -vf fps=2 ../anthropics/skills/youtube/claude-liam-brand-guidelines/_qc/frames/%05d.png
   Read the PNGs. Check 9-point rubric. Log in _qc/REPORT.md.
6. ffprobe the mp4 — confirm audio present, duration sane (target ~3:00).
7. If QC passes: open the mp4 for human review.
8. Never publish — output stays in the reel folder.

Free pipeline only: Kokoro af_kore, no ElevenLabs, no higgsfield.
```

## Expected output
- `mp4/claude-liam-brand-guidelines.mp4` — ~3:00, 1920×1080, stereo audio
- `mp3/beat-*.mp3` — per-beat Kokoro narration
- `media/B00.mp4` through `media/BOUT.mp4` — per-beat Remotion renders
- `_qc/REPORT.md` — visual QC log
- `_qc/frames/*.png` — QC frame samples
