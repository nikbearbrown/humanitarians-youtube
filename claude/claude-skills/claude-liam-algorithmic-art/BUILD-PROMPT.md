# BUILD-PROMPT — claude-liam-algorithmic-art

Paste this prompt into Claude Code from the `books/` working directory to rebuild
the "Claude, Seeded." reel end-to-end.

---

Build the 16:9 claude-explainer video **"Claude, Seeded."** — a Teardown-register
explainer about Anthropic's algorithmic-art skill, narrated by Kore (in for Humanitarians AI),
Kokoro af_kore voice, @HumanitariansAI channel.

Reel folder: `brutalist-art/youtube/claude-liam-algorithmic-art/`

The beat_sheet.json, audio (mp3/), and SOURCES.md already exist. Do NOT
re-generate audio. Re-render all Remotion scenes, then compile the final cut.

**Step 1 — Type-check Remotion project**
```
cd brutalist-art/runtime/remotion && npx tsc --noEmit
```
Fix any errors before proceeding.

**Step 2 — Re-render all 12 Remotion beats**
```
RIFF_PROJECT=youtube/claude-liam-algorithmic-art \
  python3 runtime/scripts/remotion_scenes.py \
  youtube/claude-liam-algorithmic-art --force
```
Run foreground, `--concurrency=1` is the default. All 12 beats are Remotion.

**Step 3 — Compile the final master at 1080p/30fps**
```
python3 runtime/scripts/compile.py \
  youtube/claude-liam-algorithmic-art \
  --height 1080 --fps 30 --force
```
Output: `youtube/claude-liam-algorithmic-art/claude-liam-algorithmic-art.mp4`

**Step 4 — Verify**
```
ffprobe -v quiet -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate,nb_frames \
  -of csv=p=0 \
  youtube/claude-liam-algorithmic-art/claude-liam-algorithmic-art.mp4
```
Expected: `1920,1080,30/1,~9143`

**Step 5 — Visual QC**
```
mkdir -p youtube/claude-liam-algorithmic-art/_qc/frames
ffmpeg -i youtube/claude-liam-algorithmic-art/claude-liam-algorithmic-art.mp4 \
  -vf fps=2 \
  youtube/claude-liam-algorithmic-art/_qc/frames/%05d.png -y
```
Read sample frames. Check 8-point rubric: edge bleed, title-safe margins,
container overflow, element collision, offscreen anchors, legibility, brand palette,
aspect ratio. Log defects and fixes in `_qc/REPORT.md`.

---

## Remotion scenes (all registered in Root.tsx)

| Beat | Pattern | Notes |
|------|---------|-------|
| B00 | ClaudeComposerAsk | Cold open — IN-FOR-BEAR LAW |
| B01 | AlgArtPipeline | Three-node pipeline diagram |
| B02 | AlgArtOrganicTurbulence | Live flow field, seed=42 |
| B03 | AlgArtMovementGallery | Four-vignette gallery, SECTION_LEN=210 |
| B04 | AlgArtHiddenSeed | φ annotation ring, seed=256 |
| B05 | ClaudeCodeBeat | Art Blocks seed pattern code block |
| B06 | AlgArtSeedGrid | 3×3 seed grid, highlightSeed=3 |
| B07 | AlgArtFixedVariable | Artifact viewer mock |
| B08 | AlgArtQualityDial | Quality phrases with tick counters |
| BVDT | ClaudeVerdictArtifact | Verdict — 4 numbered points |
| BHTF | ClaudeComposerAsk | Your turn — prompt read aloud |
| BOUT | ClaudeTitleOutro | "Claude, Seeded." + @HumanitariansAI |

## Known issues / watch for

- **Wrap artifacts**: AlgArtOrganicTurbulence, AlgArtMovementGallery (FieldDynamics),
  AlgArtSeedGrid (TileViz), and AlgArtFixedVariable (SystemA) all use toroidal
  particle trails. The path builder must break the SVG path (M instead of L) when
  consecutive points jump >W/2 or >H/2. This is implemented — verify it stays intact.
- **Resolution**: Always compile with `--height 1080 --fps 30`. The default (720p/24fps)
  will produce a downscaled output.
- **BVDT slow rate**: ClaudeVerdictArtifact composition is 360 frames (12s at 30fps)
  but BVDT audio is 35.7s — compile.py slows it 2.96×. The card is static text so
  the slowdown is invisible. To fix permanently: increase BVDT durationInFrames to
  1080 in Root.tsx and re-render.

## Free pipeline — no paid spend

Kokoro af_kore (local, free). No ElevenLabs. No higgsfield. No publishing.
