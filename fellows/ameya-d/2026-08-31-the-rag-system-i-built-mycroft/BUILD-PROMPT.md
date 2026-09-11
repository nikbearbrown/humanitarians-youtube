# BUILD-PROMPT — mycroft-rag-walkthrough

Weekly WORK video: a measured walkthrough of the `fin-disclosure-rag` system
(~5 min). Channel @HumanitariansAI. Persona Liam, in for Ameya. Kokoro `am_onyx`.
4K. Free pipeline.

12 beats. Bookends: B00 ClaudeComposerAsk; B09 ClaudeVerdictArtifact; B10
ClaudeComposerAsk (Your turn.); B11 ClaudeTitleOutro. One ClaudeCodeBeat (B07,
verbatim `hybrid.py` RRF). Body: 7 Manim scenes (scenes.py).

## Rebuild
```
python3 runtime/scripts/generate_audio_kokoro.py <reel>
# set scenes.py TARGET{} from measured durations, render Manim 4K -> manim/<BID>.mp4
python3 runtime/scripts/remotion_scenes.py <reel>   # -> media/<BID>.mp4
python3 runtime/scripts/compile.py <reel> --height 2160
python3 runtime/qc/final_frame_check.py <reel> --lenient
```
