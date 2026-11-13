# BUILD-PROMPT — Where You Cut The Page.

Paste-ready Claude Code prompt that builds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root —
this reel lives in the book, not the toolkit (CLAUDE.md rule 3). The book root
is `D:\ai1-cli-main` (the book's canonical repo, per `metadata.yaml`).

```
Reel: D:\ai1-cli-main\youtube\2026-08-26-claude-rag-chunking

0. Windows note — set UTF-8 for EVERY python step below:
   export PYTHONUTF8=1
   Without it, build_scene_index.py fails reading Root.tsx and compile.py's
   status-line arrow crashes a cp1252 console. This is environmental, not a
   reel defect.

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.

2. Audio (only if narration changed — it is the master clock):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   Add --only <BEAT_ID> to regenerate a single beat after a narration edit.
   NEVER hand-edit actual_duration_s. Regenerate and recompile instead.
   B01 is load-bearing here: the EXECUTIVE-SUMMARY LAW floor is a 9s audio
   window plus lead_silence_s 0.8, or the hesitant writer's correction does
   not land before the cut. Current: 11.01s.

2b. *** IF AUDIO CHANGED ON B02-B06 OR B08, RE-SYNC `beatSeconds` ***
   Those six beats pass their measured duration to their component as a
   `beatSeconds` prop, and the component stages every reveal as a fraction of
   it. This is NOT redundant with actual_duration_s — it is necessary, because
   remotion_scenes.py renders each composition at its REGISTERED length
   (900f / 30s) and then truncates the clip with `ffmpeg -t`. Keying stages to
   useVideoConfig().durationInFrames would therefore schedule late reveals
   past the truncation point, where they are cut off and never seen.

   A stale beatSeconds fails SILENTLY — the mp4 probe is clean, the duration
   is right, and a reveal simply never lands. Re-sync it:

     python - <<'PY'
     import json
     p = r'<REEL>\beat_sheet.json'
     d = json.load(open(p, encoding='utf-8'))
     CHUNK = {'ChunkWholeDocVector','ChunkSizeTradeoff','ChunkOverlapGuard',
              'ChunkThreeStrips','ChunkSeparatorLadder','ChunkThreeWays'}
     for b in d['beats']:
         rem = b['shot']['remotion']
         if rem['pattern'] in CHUNK:
             rem['props']['beatSeconds'] = b['actual_duration_s']
     json.dump(d, open(p,'w',encoding='utf-8'), indent=1, ensure_ascii=False)
     PY

   Then re-render those beats with --force and re-check in step 5 that the
   LAST staged reveal of each is on screen before its cut.

3. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   Add --force to re-render after a component edit; --only <BEAT_ID> for one.

   Bespoke components for this reel (one file each, in
   runtime/remotion/src/scenes/, registered in runtime/remotion/src/Root.tsx
   at BOTH 16:9 and 916):
     ChunkWholeDocVector   (B02)   ChunkThreeStrips     (B05)
     ChunkSizeTradeoff     (B03)   ChunkSeparatorLadder (B06)
     ChunkOverlapGuard     (B04)   ChunkThreeWays       (B08)
   Shared layout primitive (NOT a registered composition):
     ChunkChrome.tsx — useBeatClock (stages keyed to the beat's own measured
     audio), Bars, Panel, PanelTitle, PanelNote, useFigureWidth.
   All six render inside Chapter 3's EmbedChrome FigureFrame, so Ch.3 and Ch.4
   cut together as one series. Do not fork that chrome.

   Reused unmodified (props only): ClaudeComposerAsk (B00, BHTF),
   BrutalistHesitantWriter (B01), ProblemPredictCard (B07),
   ClaudeVerdictArtifact (BVDT), TitleOutroChannel (BOUT).

   BOUT must stay TitleOutroChannel. Do NOT swap it to ClaudeTitleOutro:
   that card is locked to claude-liam-* slugs (OUTRO-LOCK.md §Scope), its
   handle is hardcoded to @NikBearBrown with no prop, and it never renders a
   subline — which would silently drop the author signature.

   After ANY new component: python runtime/scripts/build_scene_index.py
   (or ./art scene-index) — an unindexed component cannot be found again.

   No Manim / scenes.py in this build. This book's ai-explainer reels are
   pure-Remotion by convention, which also sidesteps the missing LaTeX
   (LaTeX blocks only Manim EQUATION beats — nothing here needs one).

4. Assemble at 4K:
   python runtime/scripts/compile.py <REEL> --height 2160
   Explicit --height 2160 — compile.py's bare default is NOT 4K.
   (./art final <REEL> also defaults to 2160 and writes the clean master to
   $ART_OUT / renders/ instead of beside the reel — RENDER-TARGETS.md §2.)

5. Visual QC — MANDATORY, never skip. An ffprobe duration/frame check is a
   FILE check and never counts as QC (VISUAL QC LAW):
   ffmpeg -i <REEL>/claude-rag-chunking.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Actually READ the PNGs and audit the 9-point rubric. Watch especially:
     B03, B04, B08 — text-heavy multi-panel cards: check overflow and wrap
     B05 — three strips side by side: check panel gaps and that the fixed-count
           cut still visibly severs a text row (that severing IS the argument)
     B06 — ladder: check the arrows sit between rungs, not on them
     B01 — confirm the correction is fully on screen BEFORE the cut
   Log defects and fixes in _qc/REPORT.md. Fix ROOT CAUSES in the component
   source and re-render (--force) until zero BLOCKER and zero MAJOR.

6. Confirm resolution:
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
     -of csv=p=0 <REEL>/claude-rag-chunking.mp4     → must read 3840,2160

7. Never publish. The master is written for human review; nothing here uploads.
```

## What's already done (as of this build)

- `beat_sheet.json` — authored; 12 beats; audio generated (Kokoro `am_onyx`,
  free, $0.00); all beats rendered and compiled at 4K.
- `PEDAGOGY.md` (VERDICT: PASS) / `SOURCES.md` / `CHECKS-REPORT.md` /
  `_qc/REPORT.md` — all written.
- Six new Remotion components + `ChunkChrome.tsx`, registered in `Root.tsx` at
  both aspects, typechecked clean, and added to `scenes.json` via
  `./art scene-index`.
- GATE L: six library searches run before authoring, six genuine misses, all
  logged to `TEMPLATE-MISSES.md`. Nothing slated.

## If re-running after a content edit

- Edit `narration_text` → step 2 with `--only <ID>` → step 3 with `--force`
  for that beat → step 4 with `--force` → step 5 again. Never fix timing by
  hand; regenerate audio and recompile.
- **4K is a hard requirement for this reel** per the original build request:
  step 4 must pass `--height 2160` and step 6 must confirm `3840,2160`. Do not
  ship a 1080p draft as the master.
- If you add a chunk SIZE or an overlap PERCENTAGE anywhere on screen, stop —
  that is a DOUBLE-CHECK LAW violation for this chapter, not a helpful detail.
  The chapter explicitly refuses to name one. See SOURCES.md §Corrections.

## Deriving the 9:16 Short

All six bespoke components register a `916` twin and re-band (stack) rather
than crop, so the short does not need new work:

```
python runtime/scripts/shorts.py <REEL>
python runtime/scripts/compile.py <REEL>/short --height 1920
```
