# BUILD-PROMPT — National Loon Center Weekly Update (Week 9)

Paste this into Claude Code from the repo root.

```
Create a weekly-progress ai-explainer reel in weekly_updates/08-28/ using the scaffold in beat_sheet.json and the repo guidance in WEEKLY-VIDEO-GUIDE.md, HOW-TO.md, and README.md.

Goals:
1. Keep the reel in the Claude Swara / Teardown register.
2. Preserve the 8-beat weekly-progress spine.
3. Use only the registered Remotion compositions: ClaudeComposerAsk, ClaudeScienceLayerStack, ClaudeScienceSourceFlow, ClaudeScienceChipGrid, BinaryBranch, ClaudeVerdictArtifact, and ClaudeTitleOutro.
4. Keep the narration qualitative and avoid invented numbers.
5. Leave the pedagogy gate unsigned until a human reviewer signs it.

Steps:
1. Review the scaffold in weekly_updates/08-28/beat_sheet.json.
2. Sign GATE P in weekly_updates/08-28/PEDAGOGY.md (a human reviewer only).
3. Generate narration audio with python3 runtime/scripts/generate_audio_kokoro.py weekly_updates/08-28/.
4. Render the beats with python3 runtime/scripts/remotion_scenes.py weekly_updates/08-28/.
5. Compile the 16:9 master with ./art run weekly_updates/08-28/.
6. Derive the 9:16 short with ./art shorts weekly_updates/08-28/, then compile it per its printed instructions.
```
