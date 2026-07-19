# PROMPTS — posting-to-youtube

No open media slots — all beats are pipeline-rendered.

Every beat is `shot.source == "own"` and falls into one of two categories:
- **GRAPHIC**: rendered by Manim from `scenes.py` → `manim/<BID>.mp4`
- **REMOTION**: rendered by `runtime/scripts/remotion_scenes.py` → `media/<BID>.mp4`

There are no `historical-image`, `ai-video-prompt`, or `user-capture` beats.
No human-supplied assets required.
