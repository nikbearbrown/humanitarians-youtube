# BUILD-PROMPT — National Loon Center Weekly Update (Week 10)

Paste this into Claude Code from the repo root.

```
Create a weekly-progress ai-explainer reel in weekly_updates/09-05/ using the scaffold in beat_sheet.json and the repo guidance in WEEKLY-VIDEO-GUIDE.md, HOW-TO.md, and README.md.

Goals:
1. Keep the reel in the Claude Swara / Teardown register.
2. Preserve the 8-beat weekly-progress spine.
3. Use only the registered Remotion compositions: ClaudeComposerAsk, ClaudeScienceLayerStack, ClaudeScienceSourceFlow, ClaudeScienceChipGrid, BinaryBranch, ClaudeVerdictArtifact, and ClaudeTitleOutro.
4. Keep the narration qualitative and avoid invented numbers.
5. Leave the pedagogy gate unsigned until a human reviewer signs it.

Steps:
1. Review the scaffold in weekly_updates/09-05/beat_sheet.json.
2. Sign GATE P in weekly_updates/09-05/PEDAGOGY.md (a human reviewer only).
3. Generate narration audio with python3 runtime/scripts/generate_audio_kokoro.py weekly_updates/09-05/.
4. Render the beats with python3 runtime/scripts/remotion_scenes.py weekly_updates/09-05/.
5. Compile the 16:9 4K master with python3 runtime/scripts/compile.py weekly_updates/09-05/ --height 2160 (and --review first for QC).
6. Derive the 9:16 short with python3 runtime/scripts/shorts.py weekly_updates/09-05/, then compile it at true vertical 4K with python3 runtime/scripts/compile.py weekly_updates/09-05/short --height 3840 (2160 width x 3840 height — NOT --height 2160, which under-renders portrait 4K).
```
