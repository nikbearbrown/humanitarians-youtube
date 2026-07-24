# BUILD-PROMPT — Claude, Configured (`claude-liam-installing-plugins`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-installing-plugins/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered,
   greeting "Bonjour, Kore", Kore signs in) → body → ClaudeVerdictArtifact
   ("Let's recap with Claude.", 0.5s lead) → ClaudeComposerAsk "Your turn."
   (prompt read aloud + discussed) → ClaudeTitleOutro (title re-read, "Kore, in for Humanitarians AI.").

2. LANE-MIX LINT. Run the beat-mix histogram over the 28 body beats. Expect
   VOX 6 (21%), MANIM 7 (25%), REMOTION 9 (32%), CARD 6 (21%) — all inside band.
   Confirm no lane runs >2 consecutive except vox run R1 (B10→B11). If the lint
   disagrees, fix the plan, not the label.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro af_kore, free. No ElevenLabs.

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/af_kore).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B04, B08, B10,
   B11, B17, B21), first run python3 runtime/scripts/pantry_search.py on its
   pantry_note terms against svg/svg/images/. Copy real matches into pantry/
   pre-checked; write SHOPPING.md from the LOCKED durations for the rest. All six
   are Tier 1 illustrative (no rights escalation, no real people). B10→B11 is a
   vox run — source both stills as one continuous camera move (studio → clients).

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; author the B10→B11 handoff continuity.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample ≥2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757): accumulate_install_steps, divergence_generic_vs_yours,
loop_ask_answer_calibrate, divergence_generic_vs_tuned, threshold_public_vs_connected,
toggle_disable_preserved, scale_active_vs_shelved. Remotion: ChipGrid (B03, B12),
SourceFlow (B16), code-block (Onda, B22), plus the illustration scenes named in the
sheet (plugin-library-grid, config-to-conversation, customize-qa,
self-contained-vs-connected, plugin-updates). Retint deck patterns to the claude
stage (cream #F2F0E9, ink #3D3929, accent #D97757) and log the retint.

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P. Never hardcode plugin counts, prices, or platform lists.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it.
- The ILLUSTRATE LAW is tight here: the Claude UI appears ONLY at B00, the H01
  handoff, V01 verdict, and O01 outro. The customize "conversation" beats (B06, B09)
  illustrate the exchange abstractly — they are NOT the Claude composer chrome.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all
  reels in chapter order with one paste.
