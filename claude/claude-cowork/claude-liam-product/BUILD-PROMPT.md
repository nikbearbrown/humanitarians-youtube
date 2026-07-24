# BUILD-PROMPT — Claude, Shipping (`claude-liam-product`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-product/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered) →
   body → ClaudeVerdictArtifact → ClaudeComposerAsk "Your turn." → ClaudeTitleOutro.

2. LANE-MIX LINT. Run the beat-mix histogram. Target: VOX 6 (20%), MANIM 8 (27%),
   REMOTION 9 (30%), CARD 7 (23%) across 30 body beats — all in band, REMOTION the
   plurality. Confirm no lane runs 3+ consecutive (the only 2-in-a-row VOX pair is
   the intended R1 run, B14→B15). If the lint drifts, fix the plan, not the label.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro am_onyx, free. No ElevenLabs. B00 opens "Annyeong — this is Liam, in for
   Bear."; the outro signs off "Liam, in for Bear." (IN-FOR-BEAR LAW).

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/am_onyx).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B02, B08, B14,
   B15, B18, B23), first run python3 runtime/scripts/pantry_search.py on its
   pantry_note terms against svg/svg/images/. Copy real matches into pantry/
   pre-checked; write SHOPPING.md from the LOCKED durations for the rest. All six
   are Tier 1 illustrative (no rights escalation, no real people, no real product
   UI/branding). B14→B15 is vox_run R1 — its two stills share room grammar and the
   authored handoff (camera 1.6 → 2.1 push into one recurring note).

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; B23 gets the terracotta ring drawn on
   at previz; B15 gets the ring on the recurring note.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample ≥2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757): divergence_interesting_vs_right, branch_want_to_stories,
accumulate_story_by_story, scale_ideas_vs_hours, rank_feedback_frequency_severity,
compare_loudest_vs_common, transform_builder_to_user, converge_rank_then_human.
Remotion: ChipGrid, SourceFlow, PredictCard, code-block (Onda), plus the two
illustration scenes named in the sheet (structured-thinking-partner,
decision-doc-tradeoffs). Retint deck patterns to the claude stage (cream #F2F0E9,
ink #3D3929, accent #D97757) and log the retint.

DATABLE STRIP (DOUBLE-CHECK LAW, sharpened): never put a plugin count, a price, a
PM-tool roster, or an analytics-vendor list on screen. Analytics tools (Mixpanel /
PostHog / Amplitude) may appear as at most ONE fleeting spoken aside, never a beat
subject; build-vs-buy stays generic ("an outside service"). See SOURCES.md.

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it. The authoring
  sandbox has no Remotion/Manim/Kokoro belt; do not attempt to render here.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all
  reels in chapter order with one paste.
