# BUILD-PROMPT — The Judgment Is the Job.

Single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit root.
Free path only — Kokoro, Remotion, ffmpeg. Never publishes.

## Prerequisites

```bash
./setup && ./art smoke
```

Needs ffmpeg, Node ≥ 20, **Python 3.10–3.12** (not 3.13+ — `manim<0.19` requires `<3.13`),
the Remotion node deps, and the Kokoro model in `runtime/models/kokoro/`.
Manim is NOT required: this reel has zero Manim beats.

On a machine without Homebrew, the working setup is: static ffmpeg/ffprobe in
`~/.local/bin`, the official Node tarball in `~/.local/node`, and a uv-managed Python 3.12
venv — then run every command below with
`PATH="$HOME/.local/brutalist-venv/bin:$HOME/.local/bin:$PATH"`.

---

## The prompt

> Build the reel at
> `~/Desktop/brutalist-reels/youtube/claude-liam-the-judgment-is-the-job/` end to end,
> free path only, and do not publish.
>
> Read completely first: `skills/make/ai-explainer/SKILL.md`,
> `skills/make/explainer/SKILL.md` + `MOTION.md` + `REMOTION.md`,
> `skills/make/nopunt/SKILL.md`, and this reel's `beat_sheet.json`, `CHECKS-REPORT.md`,
> `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`.
>
> **THE ONE CONSTRAINT THAT OVERRIDES CONVENIENCE:** this reel shows no statistic,
> percentage, count, rate, or dated projection anywhere. Comparisons are ordinal or
> described in words. If a component you reach for renders a number, do not use it —
> that is exactly how the previous reel in this series broke. `ScaleComparison`,
> `AttritionChain` and `Threshold` from `deckPatterns` are all disqualified for this
> reason and must not be substituted in.
>
> **1. Gate check.** `CHECKS-REPORT.md` shows zero PUNTs and a passing teaching arc;
> `FACTCHECK.md`, `SHOTLIST.md` and `PROMPTS.md` all exist (GATE F requires all three).
> Re-run the numeral audit over every on-screen string before rendering.
>
> **2. Scenes are already written and registered.** `runtime/remotion/src/scenes/
> JudgmentIsTheJob.tsx` holds `JdgDiverge`, `JdgSplit`, `JdgOptions`, `JdgBranch`,
> `JdgStakes`; shared stage furniture is in `scenes/claudeStage.tsx`; all five are
> registered in `Root.tsx` at 1920×1080 with `durationInFrames` equal to each beat's
> measured Kokoro length × 30fps. Run `npx tsc --noEmit` and expect clean.
>
> **3. Audio — the master clock, before any visual work.**
> ```
> python3 runtime/scripts/generate_audio_kokoro.py <REEL>
> ```
> All beats are `am_onyx`. Stamp measured `actual_duration_s` back into the sheet and
> report true runtime. If it leaves 1:00–3:00, fix it by editing narration and
> regenerating — never by hand-tuning durations. **If any duration changes, update the
> matching `durationInFrames` in `Root.tsx`**, or a progress-mapped animation will be
> trimmed mid-motion.
>
> **4. Render and compile.**
> ```
> python3 runtime/scripts/remotion_scenes.py <REEL>     # --only <BID> --force for one beat
> ./art run <REEL>
> ```
> Render Remotion only through `remotion_scenes.py`. Do not set `ART_QC=0`.
>
> **5. VISUAL QC LAW — the mp4 probe does not count.** Sample ≥2fps plus each beat at
> ~15/50/85% of its span, **Read the PNGs**, and audit the 9-point rubric from
> `CLAUDE-CODE-VISUAL-QC-CHECK.md`. Specifically check the two risks named in
> `CHECKS-REPORT.md` § Carried into visual QC: `JdgOptions` card-label wrapping at 28px,
> and `JdgStakes` row crowding. Log everything in `_qc/`.
>
> **Known false positive — do not chase it.** GATE V reports an `edge-bleed` BLOCKER on
> every frame of every reel on this toolkit. It inspects the `--review` cut and flags that
> cut's own burn-in; `final_frame_check.py`'s `BURN_IN_EXCLUDE = (0.0, 0.94, 0.60, 1.0)`
> masks only the bottom strip while the label sits top-right. Verify the CLEAN master
> instead by running `analyze_frame` on frames from `<slug>.mp4`, and report the real
> numbers.
>
> **6. Report, don't ship.**
> ```
> ./art todo <REEL> && ./art final <REEL>
> ```
> Master stays in the reel folder. Report true runtime, per-beat status, QC defects found
> and fixed, and anything unresolved. Upload nothing.

---

## Laws this reel must not break

| Law | Where it binds |
|---|---|
| COLD OPEN LAW | B00 is `ClaudeComposerAsk` with result lines — the ask lands answered. |
| EXECUTIVE-SUMMARY LAW | B01 is the BLUF: whole idea, one breath, no reveals spent. |
| ILLUSTRATE LAW | UI only at B00, B03, B07, B08, B09. Every other beat illustrates. |
| ASK→RESULT LAW | B03 → B04 is the pair; B03 shows the actual prompt behind B04. |
| SHOW-DON'T-TELL | Every beat carries a `show` block. No beat may become a static slide. |
| HANDOFF LAW | B08's prompt is read aloud verbatim, then graded against a 3-item rubric. |
| OUTRO LAW | B09 restates the title, `@NikBearBrown`, **`subline: ""`** — passing `slug` does nothing and lets Musinique's default subline leak through. |
| IN-FOR-BEAR LAW | "this is Liam, in for Bear" in B00; "Liam, in for Bear." in B09. Wagwan is never Liam's, even though this slug's charsum mod 10 is 0. |
| DOUBLE-CHECK LAW | No statistics. See `FACTCHECK.md`. |
| Never publish | No publishing machinery here. Don't add any. |

## Toolkit gaps that affect this build

- `type_check.py` (GATE T) is not shipped — GATE T cannot run; check type by eye.
- `OUTRO-LOCK.md`, `AUDIT-MODE.md`, `DESIGN-PRINCIPLES.md` are referenced by the skill and
  are not in this tree.
- `ClaudeMascotScene`/`ClaudeMascotGrid` are absent, so the outro's mascot clause cannot be
  satisfied and PIXEL-ART LAW is moot. Logged in the beat's `show` block, never faked.
