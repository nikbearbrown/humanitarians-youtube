# BUILD-PROMPT — rag-answers-that-matter

Field-guide explainer (~6-7 min) from the user's AI/RAG/LLM reference doc.
Channel @HumanitariansAI. Persona Liam, in for Ameya. Kokoro am_onyx. 4K. Free pipeline.

14 beats. Bookends: B00 ClaudeComposerAsk; B11 ClaudeVerdictArtifact; B12
ClaudeComposerAsk (Your turn.); B13 ClaudeTitleOutro. Body: 10 Manim scenes (scenes.py).

## Rebuild
```
python3 runtime/scripts/generate_audio_kokoro.py <reel>
# set scenes.py TARGET{} to mp3/timings.json, render Manim 4K -> manim/<BID>.mp4,
# render Remotion -> media/<BID>.mp4
python3 runtime/scripts/compile.py <reel> --height 2160
python3 runtime/qc/final_frame_check.py <reel> --lenient
```
