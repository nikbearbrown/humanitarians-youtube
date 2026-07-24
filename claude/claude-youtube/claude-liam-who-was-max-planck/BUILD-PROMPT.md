# BUILD-PROMPT — Who was Max Planck? (claude-liam)

Paste-ready prompt for Claude Code. Run from `books/`.
Builds audio → Manim → Remotion → slate cut → final cut. Never publishes.

```
Read books/physics-modern-physics/youtube/claude-liam-who-was-max-planck/beat_sheet.json.
Brand: claude-liam. Voice: Kokoro af_kore. Palette: claude.

Build steps (run from books/):

1. GATE P: narration already approved — proceed.

2. Generate audio (Kokoro af_kore):
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     physics-modern-physics/youtube/claude-liam-who-was-max-planck

3. Render Remotion scenes (ClaudeComposerAsk B00/B03/B08, ClaudeWindow B06, ClaudeTitleOutro B09):
   python3 brutalist-art/runtime/scripts/remotion_scenes.py \
     physics-modern-physics/youtube/claude-liam-who-was-max-planck

4. Run the full machine pass (Manim B02+B04, outro, slate cut, final cut):
   ART_QC=1 bash brutalist-art/runtime/scripts/run.sh \
     physics-modern-physics/youtube/claude-liam-who-was-max-planck

5. Report outputs:
   - Slate cut: physics-modern-physics/youtube/claude-liam-who-was-max-planck/mp4/who-was-max-planck-slate.mp4
   - Final cut: physics-modern-physics/youtube/claude-liam-who-was-max-planck/mp4/who-was-max-planck.mp4

Notes:
- Never publish. Output stays in the reel folder for human review.
- If Manim QC gates (A or B) fail, fix scenes.py and re-run.
- If Remotion render fails, check that brutalist-art/runtime/remotion node_modules exist (npm install in that dir).
- The beat_sheet.json (pipeline-readable) and beat_sheet.claude-liam.json (scaffolding record) are both in the reel folder.
```
