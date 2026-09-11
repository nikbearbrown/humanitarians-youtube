# BUILD-PROMPT — rag-from-first-principles

deep-explainer (~18-20 min) of VIDEO_SCRIPT.md — "RAG From First Principles."
Channel @HumanitariansAI. Persona Liam, in for Ameya. Kokoro am_onyx. 4K. Free pipeline.

25 beats, 12 acts. Bookends: B00 ClaudeComposerAsk; B22 ClaudeVerdictArtifact;
B23 ClaudeComposerAsk (Your turn.); B24 ClaudeTitleOutro. Body: 18 Manim scenes
(scenes.py) + 3 ClaudeCodeBeat (B03 chunk_text, B11 cosine, B12 top-k bug).
VOX quota N/A (measurement film — see BUILD-LOG.md). All numbers real (FACTCHECK.md).

## Rebuild (from this folder, with brutalist.art toolkit on hand)
```
python3 runtime/scripts/generate_audio_kokoro.py <this-reel>            # Kokoro (free)
# set scenes.py TARGET{} to measured mp3/timings.json, then:
# render Manim scenes at 4K (-r 3840,2160) -> manim/<BID>.mp4
# render Remotion beats -> media/<BID>.mp4
python3 runtime/scripts/compile.py <this-reel> --height 2160           # 4K master
python3 runtime/qc/final_frame_check.py <this-reel> --lenient          # QC to 0 BLOCKER
```
Rendered media gitignored; regenerates from beat_sheet.json + scenes.py.
