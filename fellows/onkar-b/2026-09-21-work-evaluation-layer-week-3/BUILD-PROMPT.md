# BUILD-PROMPT.md — hai-liam-evaluation-layer

Paste-ready prompt that rebuilds this reel end to end, beat sheet → verified 4K
masters in both aspects. Deterministic and free: Kokoro + Remotion, no key, no
paid call, never publishes. Run from the toolkit root (`brutalist.art/`).

---

```
Rebuild the reel at ../brutalist-reels/youtube/hai-liam-evaluation-layer
("Finding Is Not Grading." — Week 3: Evaluation Layer & n8n Integration,
Provenance Gatekeeper Development Log, @HumanitariansAI, Liam / Kokoro am_onyx).

Read completely first: skills/make/ai-explainer/SKILL.md, RENDER-TARGETS.md,
OUTRO-LOCK.md, and this reel's BUILD-LOG.md — it records eight deliberate
deviations from the source script. Keep every one.

1. GATE CHECK.
   Paperwork present and non-empty: FACTCHECK.md, SHOTLIST.md, PROMPTS.md,
   CHECKS-REPORT.md, SOURCES.md.
   python3 runtime/qc/beat_lint.py <REEL>/beat_sheet.json     # must be clean:
        the claude-hai channel has a LOCKED kicker ("Irreducibly Human") in
        runtime/qc/brand_labels.json — metadata.topic must equal it, and the
        episode subject lives in the per-beat segment titles.
   python3 runtime/scripts/build_safety.py <REEL>             # must PASS
   Confirm every pattern and its portrait twin are renderable:
     ./art scenes --check GatekeeperTaxonomy        (and GatekeeperTaxonomy916)
     ./art scenes --check GatekeeperVerifyLoop      (and ...916)
     ./art scenes --check GatekeeperDirectionalBlindspot (and ...916)
     ./art scenes --check GatekeeperScoreboard      (and ...916)
     ./art scenes --check HaiTitleOutro             (and HaiTitleOutro916)
     plus ClaudeComposerAsk and BrutalistHesitantWriter.
   A missing 916 blocks the vertical cut — register it, never centre-crop.

2. AUDIO IS THE CLOCK.
     python3 runtime/scripts/generate_audio_kokoro.py <REEL>
   Expect 9 beats, am_onyx, ~163s total, $0.00. Never hand-edit a duration; if
   a beat runs long, change its words and regenerate. Watch two registrations
   in particular: GatekeeperVerifyLoop is 540 frames (18s), so B04's narration
   must stay under it or the clip freeze-holds; ClaudeComposerAsk is 900 frames
   (30s) and frame-absolute, so a longer B07 simply holds its end state.

3. RENDER AT 4K.
     ART_CONCURRENCY=3 python3 runtime/scripts/remotion_scenes.py <REEL>
   (--scale=2, PNG frames, crf 16. Add --force --only <BID> to redo one beat.)
   Measured on the build machine: ~146 ms/frame at concurrency 3; 4 is no
   faster (memory-bound at 8 GB). Plug the laptop in first — on battery under
   the Balanced power scheme the same render is 2.5x slower.

4. COMPILE THE REVIEW CUT.
     ./art run <REEL>
   No Manim beats, so the Manim stage skips and no scenes.py is needed here.

5. VISUAL QC LAW — not optional. The mp4 probe is a file check, not QC.
     ffmpeg -i <REEL>/hai-liam-evaluation-layer-slate.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   plus each beat at ~15/50/85% of its span. READ the PNGs and audit the
   9-point rubric: edge bleed, title-safe margins, container overflow,
   collision, offscreen anchors, legibility, brand-bug placement, aspect, and
   CANVAS FILL. Log defects and fixes in _qc/REPORT.md. Fix root causes in the
   component source and re-render until zero BLOCKER and zero MAJOR.
   Check specifically: B01's correction ("verifies" → "locates") must be fully
   on screen and holding BEFORE the cut, and no similarity figure may appear
   anywhere in B05 (see SOURCES.md correction 2).

6. CLEAN MASTER (4K landscape):
     ./art final <REEL>           # --out DIR, else $ART_OUT, else renders/

7. VERTICAL COMPANION (its own beat sheet, never a crop):
     ./art vertical <REEL>
   Then render the portrait beats and QC the vertical frames separately —
   portrait type sizes and safe margins are a different layout, not a scale.

Report: measured runtime, per-beat durations, QC defects found and fixed, and
where both masters landed. Do not publish; this toolkit has no upload path.
```

---

## Expected output

| Artifact | Path |
|---|---|
| Review cut (beat labels + timecode) | `hai-liam-evaluation-layer-slate.mp4` |
| Clean 4K landscape master | `$ART_OUT` / `brutalist.art/renders/hai-liam-evaluation-layer.mp4` |
| Vertical companion | `vertical/` |
| Per-beat clips | `clips/`, `media/` |
| Narration + timings | `mp3/`, `mp3/timings.json` |
| QC evidence | `_qc/REPORT.md`, `_qc/frames/`, `_qc/contact_sheet.png` |
