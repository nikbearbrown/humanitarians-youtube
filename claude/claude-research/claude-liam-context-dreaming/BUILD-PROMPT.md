# BUILD PROMPT — claude-liam-context-dreaming ("Claude, Dreaming.")

Paste-ready end-to-end build prompt. All commands run from `books/brutalist/`
(reels live in the toolkit's own `youtube/`). The reel folder is
`youtube/claude-liam-context-dreaming/`. NEVER publish — the master stays in
the reel folder; going public is a human Studio flip.

---

Build the deep-explainer reel at `youtube/claude-liam-context-dreaming/`
end to end. Follow the deep-explainer skill and its parents (ai-explainer
house laws, your-turn closing standard). This is a talk-analysis episode of
Lamis Mukta's AI Native DevCon 2026 talk — SOURCE.md in the folder is the
only verification authority.

1. GATE CHECK (stop if any gate is unsigned)
   - Confirm PEDAGOGY.md is human-signed (it ships as PENDING HUMAN REVIEW —
     do not proceed past planning while it is pending).
   - Confirm FACTCHECK.md stands: every on-screen quote must match SOURCE.md
     character-for-character; results claims keep their speaker-reported
     framing and tags.
   - GATE P: render the animated narration slate (show events at estimated
     timing, never a page of text) and get the human signature BEFORE any
     audio generation.
   - Hard rules that bind this episode: no imagery of Lamis Mukta (Tier 3);
     no product names or CTAs in narration; all vox stills Tier 1 generic,
     source "ai"; one terracotta accent per beat; logo bug @NikBearBrown
     lower-right every beat.

2. AUDIO (Kokoro only — Onyx)
   - `python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-context-dreaming`
   - Voice: am_onyx. B42 keeps its 0.5 s lead silence.
   - Audio lock: measured per-beat mp3 durations become the clock; run the
     align step so the word clock exists (reveals land ON the spoken word —
     B03 underline on "multiplying", B20 "optimistic locking" label, B33
     RAD/DEG draw-on, B43 margin checks).

3. GATE D2 — SHOPPING.md (only now — after audio lock, never before)
   - Write SHOPPING.md from the locked durations: one entry per missing
     pantry asset, tier-tagged, each motion asset stating minimum duration
     and asking for MORE than needed (conform trims, never stretches).
   - Six plates cover the eight vox beats (see BUILD-LOG MISSING lines):
     R1 plate serves B09+B10; R2 plate serves B30+B31; singles for B12, B16,
     B28, B33. All Tier 1, generate or stock; B33 needs clean margin space
     for the draw-on annotation.

4. GATE D1 — SLATE PREVIZ (the first compile is always full-length)
   - `./art run youtube/claude-liam-context-dreaming`
   - Vox slots render as slates (beat id + narration line + terracotta
     pipeline pointer); Manim/Remotion beats render for real; audio is real.
   - Present it AS a previz for pacing review while stills are sourced.
     Never present a previz as a finished cut.

5. PANTRY FILL
   - Human drops the six plates into `pantry/`; intake treats (desaturate
     ~80%, contrast ~1.15, cream stage, grain, warm-ink vignette), renames to
     beat ids, sets shot.focus. Vox-run handoff frames must reproduce the
     serialized camera/object values in the beat sheet (R1 on B09, R2 on
     B30). Rerun `./art run` — only changed slots recompile.
   - The review cut does not proceed with unresolved SHOPPING.md entries
     unless the human explicitly says "ship with slates".

6. VISUAL QC (frame-level, per VISUAL QC LAW — the mp4 probe never counts)
   - `ffmpeg -i [review.mp4] -vf fps=2 _qc/frames/%05d.png` plus each beat at
     ~15/50/85% of its span; READ the PNGs; audit the 9-point rubric
     (edge bleed, title-safe, overflow, collision, offscreen anchors,
     legibility, brand bug, aspect, CANVAS FILL). Log defects and fixes in
     `_qc/REPORT.md`; fix root causes in scene source; re-render to zero
     BLOCKER/MAJOR.
   - Episode-specific checks: every on-screen quote verbatim against
     SOURCE.md with its small citation; the speaker-reported tag legible on
     B24 and B40; the B41 credit card complete (name, role, title, event,
     URL); no frame anywhere depicts the speaker.

7. FINAL
   - `./art final youtube/claude-liam-context-dreaming`
   - Deliverables stay in the reel folder: the master mp4, the slate cut,
     `_qc/REPORT.md`, updated BUILD-LOG.md with gate signatures.
   - DO NOT publish, upload, or flip anything public.

Metadata for the eventual (human) upload, drawn from beat_sheet.json:
title "Claude, Dreaming." · playlist "Talks, Torn Down" · description credits
the talk (Lamis Mukta, Anthropic Applied AI — "Learning while you sleep:
Beyond memory to dreaming", AI Native DevCon London, June 2026,
https://www.youtube.com/watch?v=tTcxVv8HHNw).
