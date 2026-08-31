# BUILD-PROMPT — rag-reranking

RAG-series episode on reranking (~4 min). Channel @HumanitariansAI. Persona Liam,
in for Ameya. Kokoro `am_onyx`. 4K. Free pipeline.

11 beats. Bookends: B00 ClaudeComposerAsk; B08 ClaudeVerdictArtifact; B09
ClaudeComposerAsk (Your turn.); B10 ClaudeTitleOutro. One ClaudeCodeBeat (B05,
verbatim `rerank.py`). Body: 6 Manim scenes (scenes.py).

## Rebuild
```
python3 runtime/scripts/generate_audio_kokoro.py <reel>
# set scenes.py TARGET{} from measured durations, render Manim 4K -> manim/<BID>.mp4
python3 runtime/scripts/remotion_scenes.py <reel>   # -> media/<BID>.mp4
python3 runtime/scripts/compile.py <reel> --height 2160
python3 runtime/qc/final_frame_check.py <reel> --lenient
```
