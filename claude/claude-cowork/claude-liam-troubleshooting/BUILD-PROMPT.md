# BUILD-PROMPT — Claude, Unstuck (`claude-liam-troubleshooting`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-troubleshooting/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered,
   greeting "Salaam, Liam", Liam signs in "Salaam — this is Liam, in for Bear.") →
   body → ClaudeVerdictArtifact ("Let's recap with Claude." + 0.5s lead) →
   ClaudeComposerAsk "Your turn." → ClaudeTitleOutro (sign-off "Claude, Unstuck.
   Liam, in for Bear.").

2. LANE-MIX LINT. Run the beat-mix histogram. It should read VOX 5 (25%), MANIM 5
   (25%), REMOTION 6 (30%), CARD 4 (20%) over 20 body beats — all in band. If your
   linter disagrees, report it; do not pad the reel to hit a longer runtime. This is
   a short chapter (~520 words) and a ~4:00 reel is correct.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro am_onyx, free. No ElevenLabs.

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/am_onyx).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B05, B11, B12,
   B15, B16), first run python3 runtime/scripts/pantry_search.py on its pantry_note
   terms against svg/svg/images/. Copy real matches into pantry/ pre-checked; write
   SHOPPING.md from the LOCKED durations for the rest. All five are Tier 1
   illustrative (no rights escalation, no real people, no product UI). B15→B16 is
   vox_run R1 — the two stills must share scene grammar so the descent reads as one
   continuous move; ask for MORE duration than the beats need so conform trims.

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; hold the R1 handoff camera values.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample ≥2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757 accent) — MANIM is MOVING DATA every time: surface_vs_bedrock
(layers: interface shifts, concept line holds), threshold_generic_vs_context (meter
jumps a threshold), scope_reduces_latency (query set shrinks, latency bar falls),
four_step_loop (accumulate with a resolved counter), interface_dates_concept_holds
(timeline: interface labels churn, concept line flat). Remotion: ChipGrid, SourceFlow,
code-block (Onda) for the slash-commands, plus the illustration scenes named in the
sheet (failure-to-abandonment, reopen-reload, plugins-panel-toggle). Retint deck
patterns to the claude stage (cream #F2F0E9, ink #3D3929, accent #D97757) and log the
retint.

DATABLE-STRIP IS THIS EPISODE'S SUBJECT. Never hardcode plugin counts, prices, or
platform lists. Keep the official channels named as durable institutions (Anthropic
blog, Claude release notes, the plugin directory, per-plugin GitHub docs) but never
pin a URL, version, or "as of [month]." Act IV's whole job is: the interface dates,
the concept persists, verify current specifics against the live docs.

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it. Nothing here was
  rendered; there is no audio, no media, no compiled previz yet.
- **Short-chapter discipline.** Duration is an OUTPUT. This is the book's shortest
  chapter; the reel is deliberately ~4:00 at 20 body beats. Do not add acts or beats
  to "match" the longer reels in the batch.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all
  reels in chapter order with one paste.
