# BUILD-PROMPT — The Bottleneck Moved.

Single paste-ready prompt that builds this reel end to end. Run from the toolkit root
(`~/Desktop/brutalist.art-main`). Free path only — Kokoro, Manim, Remotion. Never publishes.

## Prerequisites (verify before pasting)

```bash
./setup && ./art smoke
```

Both must pass. `./setup` green means dependencies check out live; `./art smoke` is the
proof that a video actually renders. This reel needs: ffmpeg, Node ≥ 20, Python 3.10–3.12
(**not 3.14** — `manim<0.19` requires `<3.13`), the Remotion node deps, and the Kokoro
model at `runtime/models/kokoro/`.

---

## The prompt

> Build the reel at
> `~/Desktop/brutalist-reels/youtube/claude-liam-the-bottleneck-moved/` end to end,
> free path only, and do not publish.
>
> Read these first, completely: `skills/make/ai-explainer/SKILL.md` (governs look and
> framing), `skills/make/explainer/SKILL.md` + `MOTION.md` + `REMOTION.md` (governs how
> graphics are made), `skills/make/nopunt/SKILL.md` (the PROOF GATE catalog), and the
> reel's own `beat_sheet.json`, `CHECKS-REPORT.md`, and `FACTCHECK.md`.
>
> **1. Gate check.** Confirm `CHECKS-REPORT.md` shows zero PUNT-flagged beats and a
> passing teaching arc, and that `FACTCHECK.md` exists. Do not proceed past a failure —
> resolve it or log an explicit justification in `BUILD-LOG.md`.
>
> **2. Register the reel-local Remotion scenes.** The five body beats reference the
> generic deck patterns `DivergentFates`, `ScaleComparison`, `AttritionChain`,
> `Threshold`, and `BinaryBranch`, which are registered in
> `runtime/remotion/src/Root.tsx` at 1280×720 with their own color constants. Before
> rendering, add reel-local 1920×1080 registrations retinted to the claude stage —
> cream `#F2F0E9`, ink `#3D3929`, accent `#D97757`, warn `#A44A32` — and add the
> low-opacity `@NikBearBrown` corner bug inside the title-safe inset (LOGO LAW). Position
> everything from the shared `SAFE` constant in `src/tokens/layout.ts`, never by pixel
> nudge. Update each beat's `shot.remotion.pattern` to the new ids. Log the retint as a
> decision in `BUILD-LOG.md`.
>
> **3. Audio — the master clock. Do this before any visual work.**
> ```
> python3 runtime/scripts/generate_audio_kokoro.py ~/Desktop/brutalist-reels/youtube/claude-liam-the-bottleneck-moved
> ```
> Every beat is `am_onyx`. Then stamp the measured `actual_duration_s` back into the beat
> sheet and report the true total runtime. If it lands outside 1:00–3:00, fix it by
> editing narration and regenerating — never by hand-tuning durations.
>
> **4. Render and compile.**
> ```
> python3 runtime/scripts/remotion_scenes.py ~/Desktop/brutalist-reels/youtube/claude-liam-the-bottleneck-moved
> ./art run ~/Desktop/brutalist-reels/youtube/claude-liam-the-bottleneck-moved
> ```
> Render Remotion only through `remotion_scenes.py` — never hand-roll `npx remotion
> render`. `run.sh` carries Gate A (static scene check) and Gate B (pixel layout audit)
> as hard gates; do not set `ART_QC=0`.
>
> **5. VISUAL QC LAW — mandatory, and the mp4 probe does not count.**
> Sample frames at ≥2 fps into `_qc/frames/`, plus each beat at ~15/50/85% of its span,
> then **actually Read the PNGs** and audit the 9-point rubric from
> `CLAUDE-CODE-VISUAL-QC-CHECK.md`: edge bleed, title-safe margins, container overflow,
> collision, offscreen anchors, legibility, brand bug placement, aspect, and CANVAS FILL.
> Pay specific attention to the two risks named in `CHECKS-REPORT.md` § Open items: type
> falling under the legibility floor after the 720p→1080p scale-up, and dead space under
> top-clustered pattern graphics. Log every defect and fix in `_qc/REPORT.md`. Fix root
> causes in scene source and re-render until zero BLOCKER and zero MAJOR remain.
>
> **6. Report, don't ship.**
> ```
> ./art todo  ~/Desktop/brutalist-reels/youtube/claude-liam-the-bottleneck-moved
> ./art final ~/Desktop/brutalist-reels/youtube/claude-liam-the-bottleneck-moved
> ```
> The master stays in the reel folder. Report: true runtime, per-beat status, QC defects
> found and fixed, and anything you could not resolve. Do not upload anything anywhere.

---

## Laws this reel must not break

| Law | Where it binds here |
|---|---|
| COLD OPEN LAW | B00 is `ClaudeComposerAsk` with result lines — the ask lands answered. |
| EXECUTIVE-SUMMARY LAW | B01 is the BLUF: whole idea, one breath, no reveals spent. |
| ILLUSTRATE LAW | UI only at B00, B03, B07, B08, B09. Every other beat illustrates. |
| ASK→RESULT LAW | B03 → B04 is the pair; B03 shows the actual prompt behind B04. |
| SHOW-DON'T-TELL | Every beat carries a `show` block. No beat may become a static slide. |
| HANDOFF LAW | B08's prompt is read aloud verbatim, then graded against a 3-item rubric. |
| OUTRO LAW + OUTRO-LOCK | B09 restates the title, hardcoded `@NikBearBrown`, **no subline**. |
| IN-FOR-BEAR LAW | "this is Liam, in for Bear" in B00; "Liam, in for Bear." in B09. |
| PIXEL-ART LAW | B09 mascot moves by translation and axis-aligned scale only — grep for `rotate`, must be zero. |
| DOUBLE-CHECK LAW | No measured external figure anywhere. See `FACTCHECK.md`. |
| Never publish | There is no publishing machinery here. Don't add any. |
