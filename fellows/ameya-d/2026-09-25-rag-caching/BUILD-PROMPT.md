# BUILD-PROMPT — rag-caching

RAG-series deep-explainer (~4-5 min) extending the fin-disclosure-rag project.
Channel @HumanitariansAI. Persona Liam, in for Ameya. Kokoro am_onyx. 4K. Free pipeline.

12 beats: Claude bookends (B00 ClaudeComposerAsk; B07 ClaudeCodeBeat; B09 ClaudeVerdictArtifact; B10 ClaudeComposerAsk 'Your turn.'; B11 ClaudeTitleOutro) + 7 Manim body scenes.

## Rebuild
```
python3 runtime/scripts/generate_audio_kokoro.py <reel>
# set scenes.py TARGET{} to measured durations, render Manim 4K -> manim/<BID>.mp4,
# render Remotion bookends -> media/<BID>.mp4
python3 runtime/scripts/compile.py <reel> --height 2160   # writes to brutalist.art/renders/<slug>.mp4
python3 runtime/qc/final_frame_check.py <reel> --lenient
```
