# BUILD-LOG — installs
# append-only — every command, error, fix, MISSING:, and final result

## Session start: 2026-07-12

---

### SETUP

- Directories created: media/, manim/, mp3/, pantry/, images/
- Read: beat_sheet.json (15 beats: B00–B13, B99)
- Read: docs/Installs.md (source doc)
- Read: runtime/README.md
- Read: runtime/manim/animated_graphics.py (teardown palette, library components)
- Read: runtime/remotion/src/scenes/* (BrutalistTerminalOpen, NikBearBrownCodeBlock, NikBearBrownTerminalAsk, BrutalistCommentCTA schemas)
- Read: runtime/remotion/src/Root.tsx (registered compositions, durationInFrames)
- Env: ELEVENLABS_API_KEY=<set> — narrated cut possible
- Env: ELEVENLABS_VOICE_NIKBEARBROWN=<set>

### BEAT SUMMARY

GRAPHIC/MANIM (9): B01 B03 B04 B06 B07 B09 B10 B11 B12
REMOTION (6): B00 B02 B05 B08 B13 B99

### PROP MAPPING (beat sheet intent → component schema)

- B00 BrutalistTerminalOpen: command ✓, checklist ✓, topic="SET UP ONCE"
- B02 NikBearBrownCodeBlock: code ✓, language="bash" ✓, caption ✓
- B05 NikBearBrownCodeBlock: code ✓, language="bash" ✓, caption ✓
- B08 NikBearBrownTerminalAsk: command ✓, output[] ✓, segment="PYTHON VENV", runningText="checking dependencies…"
- B13 NikBearBrownTerminalAsk: command ✓, output[] ✓, segment="KEY CHECK", runningText="validating keys…"
- B99 BrutalistCommentCTA: title→code (comment lines), handle→code, url→code, variant="A", topic="SET UP ONCE"


## HUMAN FEEDBACK — 2026-07-13

Build the 9:16 Shorts for all four published series videos and STOP FOR HUMAN APPROVAL before any publish.

REELS (in this order): youtube/what-is-brutalist, youtube/installs, youtube/when-cowork-helps-claude-code, youtube/posting-to-youtube

PHASE 1 — BUILD (for each reel):
1. Run ./art shorts <reel> — it checks YouTube's hard 3:00 cap and auto-plans which beats to drop (hook/hero/outro protected). Record each plan in the reel's BUILD-LOG.md. Do not override the plan unless a kept beat is broken.
2. If beats were dropped, shorts.py rewrote the outro to mention the cuts and point to the long. Regenerate ONLY that outro's audio: python3 runtime/scripts/generate_audio.py <reel>/short (it fills the one missing mp3). No other audio is regenerated — every other beat reuses the parent's mp3.
3. Follow shorts.py's per-beat output: GENERATED graphics beats (manim/remotion) are never center-cut — re-lay each kept one out for portrait in <reel>/short/scenes.py and render via the runner on the short/ folder (Remotion only via runtime/scripts/remotion_scenes.py, foreground, props matched to zod schema — rules #3/#4). Captured/user media beats were auto center-cut; leave them (the human replaces bad cuts via pantry/<bid>-916.*).
4. Compile the review cut: python3 runtime/scripts/compile.py <reel>/short --review --height 1920. Verify by LOOKING at the qc-sheet and at actual frames (rule #2): portrait framing correct, no landscape squeeze, outro mentions the cuts, total under 3:00.

PHASE 2 — GATE (all four built): report per short — duration, beats dropped, outro line, qc verdict — and the paths to the four review mp4s. Then STOP. Do not publish. Wait for the human to say "approved" (possibly with per-short corrections; apply them and re-gate).

PHASE 3 — PUBLISH (only after explicit approval).

## SHORTS BUILD — 2026-07-13

### shorts.py plan recorded
**Plan**: drops B09 (21.1s), B01 (18.6s), B03 (17.7s). Outro B99 rewritten.
Real planned duration ~172.6s (under 3:00 cap). Portrait scenes.py written for
B04, B06, B07, B10, B11, B12.

MISSING: ELEVENLABS_API_KEY invalid (HTTP 401) — cannot regenerate outro B99 mp3.
Generating 16s silence placeholder; human must re-run generate_audio.py --only B99.
