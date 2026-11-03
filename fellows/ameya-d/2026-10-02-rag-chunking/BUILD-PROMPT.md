# BUILD-PROMPT - rag-chunking

RAG-series deep-explainer (~4-5 min) from fin-disclosure-rag VIDEO_SCRIPT.md.
Channel @HumanitariansAI. Liam, in for Ameya. Kokoro am_onyx. 4K.

12 beats: Claude bookends (B00 ComposerAsk; B07 CodeBeat; B09 VerdictArtifact; B10 ComposerAsk; B11 TitleOutro) + 7 Manim body scenes.

## Rebuild
```
python3 runtime/scripts/generate_audio_kokoro.py <reel>
# set scenes.py TARGET to measured durations; render Manim 4K to manim/<BID>.mp4; render Remotion to media/<BID>.mp4
python3 runtime/scripts/compile.py <reel> --height 2160   # writes brutalist.art/renders/<slug>.mp4
python3 runtime/qc/final_frame_check.py <reel> --lenient
```
