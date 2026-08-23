# BUILD-PROMPT — Loops That Know When to Stop.

Paste into Claude Code, run from the `brutalist.art` toolkit root
(`/Users/muskankhandelwal/Documents/brutalist.art`). Free/local pipeline —
Kokoro voice, no API keys.

```
Build the ai-explainer reel "Loops That Know When to Stop." (loop engineering).

REEL: /Users/muskankhandelwal/Documents/humanitarians-youtube/fellows/Muskan-k/2026-08-09-loop-engineering

Ground truth, read first:
1. <REEL>/beat_sheet.json — the master. Narration is GATE P for this text only.
2. <REEL>/PEDAGOGY.md — GATE P (must read "VERDICT: PASS" before audio).
3. skills/make/ai-explainer/SKILL.md + CLAUDE-BRAND.md — the laws (ILLUSTRATE LAW,
   SHOW-DON'T-TELL, DOUBLE-CHECK, VISUAL QC). Per-video override: narrator = Muskan,
   handle @NikBearBrown, banner "Loop Engineering", voice af_bella (Bella).

Steps:
1. Audio (the clock):
   python3 runtime/scripts/generate_audio_kokoro.py <REEL>
   (Kokoro af_bella. Writes actual_duration_s + audio_file back into beat_sheet.json.)
2. Fill the 6 body beats B01–B06 (currently slates). For each, EITHER:
   - drop a still  <REEL>/media/B0N.png (≥1920×1080, animated by shot.motion), OR
   - drop a clip   <REEL>/media/B0N.mp4, OR
   - write a reel-local Manim scene in scenes.py named B0N_Name(Scene), OR
   - register a reel-local Remotion comp wrapping LayerStack/ChipGrid with the beat props.
   Bookends B00/B07/B08/B09 render from registered Claude Remotion comps automatically.
3. Compile + QC:
   ./art run <REEL>                 # previz; add --height 1080 for a fast pass
   Verify by LOOKING at _qc/ frames + qc-sheet.png (VISUAL QC LAW), not the mp4 probe alone.
   Fix scene sources until zero BLOCKER / zero MAJOR defects.
4. Master (only when no slates remain):
   ./art final <REEL>               # clean cut → loop-engineering-cut.mp4 (4K)
5. Report and STOP. Never publish — the master stays in the reel folder.
```

## Status
- GATE P: PENDING (sign in PEDAGOGY.md after narration review).
- Audio: generated (Kokoro af_bella). Bookends render; B01–B06 are slates to fill.
- Rendered media (*.mp3 / *.mp4) is git-ignored — rebuilds from this paperwork for $0.00.
