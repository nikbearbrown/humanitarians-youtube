# BUILD-PROMPT — From Annotated Data to Training a Computer Vision Model (Episode 4)

Paste this into Claude Code from the repo root.

```
Create an ai-explainer reel in videos/loon-model-training/ using the scaffold in beat_sheet.json, matching the register and schema of videos/loon-metadata-pipeline and videos/loon-annotation-tool.

Goals:
1. Keep the reel in the Claude Swara / Pragmatist register (voice af_bella).
2. Use only the registered Remotion compositions: ClaudeComposerAsk, ClaudeScienceLayerStack, ClaudeScienceSourceFlow, ClaudeScienceChipGrid, BinaryBranch, ClaudeVerdictArtifact, and ClaudeTitleOutro.
3. Keep the one illustrative number ("Loon, 92% confidence") clearly labeled as illustrative; invent no others.
4. Leave the pedagogy gate unsigned until a human reviewer signs it.

Steps:
1. Review the scaffold in videos/loon-model-training/beat_sheet.json.
2. Sign GATE P in videos/loon-model-training/PEDAGOGY.md (a human reviewer only).
3. Generate narration audio with python3 runtime/scripts/generate_audio_kokoro.py videos/loon-model-training/.
4. Render the beats with python3 runtime/scripts/remotion_scenes.py videos/loon-model-training/.
5. Compile the 16:9 4K master with python3 runtime/scripts/compile.py videos/loon-model-training/ --height 2160 (and --review first for QC).
6. Derive the 9:16 short with python3 runtime/scripts/shorts.py videos/loon-model-training/, then compile it at true vertical 4K with python3 runtime/scripts/compile.py videos/loon-model-training/short --height 3840 (2160 width x 3840 height — NOT --height 2160, which under-renders portrait 4K).
```
