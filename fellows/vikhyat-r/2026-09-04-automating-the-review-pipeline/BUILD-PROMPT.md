# BUILD-PROMPT — Automating the YouTube Review Pipeline

**By Vikhyat Raghumanda · @HumanitariansAI · ~4 min · 16:9**

---

## Where do I put this?

Three different files do three different jobs. This confuses everyone once.

| File | What it is | Who reads it |
|---|---|---|
| `beat_sheet.json` | **The actual script.** Every beat: narration, on-screen action, which component renders it. | The tool. This is what Brutalist reads. |
| `BUILD-PROMPT.md` | **The instruction to rebuild.** This file. | Claude Code — you paste the block below. |
| `FACTCHECK.md` / `SHOTLIST.md` / `PROMPTS.md` | The paperwork the build gate requires. | The gate, and you. |

**To build it:** open Claude Code with the toolkit folder as the working
directory and paste the block below. You do not "open" Brutalist like an app —
it is a set of command-line tools plus skills an agent follows.

**To just render what already exists:**

```bash
./art run  <path-to-this-folder>     # draft cut, runs the quality gates
./art final <path-to-this-folder>    # clean 4K master
```

On Windows neither of those works as shipped — see WINDOWS NOTES below.

---

## Paste this into Claude Code

```
Build the @HumanitariansAI pitch reel "Automating the YouTube Review Pipeline"
by Vikhyat Raghumanda. It argues what part of the fellow-video review loop can
be automated, and is itself the proof the author can operate Brutalist.

Ground truth, read first:
1. <reel>/beat_sheet.json — the master. 12 beats, narration final, every beat
   carries a `show` block. Do not rewrite narration without re-running FACTCHECK.
2. <reel>/FACTCHECK.md — every claim with its verdict and source. THREE claims
   were cut as FALSE; do not reinstate them. B05 is the only unproven claim and
   is deliberately hedged — do not strengthen its wording.
3. <reel>/SHOTLIST.md — which components exist vs. which were built for this reel.
4. runtime/remotion/src/scenes/HaiReviewPipeline.tsx — the 8 reel-local
   components (B02-B09), humanitarians palette, progress-based animation.
5. skills/make/ai-explainer/SKILL.md — the chassis laws.

Hard constraints:
- CHANNEL IS @HumanitariansAI. ClaudeComposerAsk's `folderLabel` prop DEFAULTS TO
  @NikBearBrown — it must stay explicitly set on B00 and B10, or this video ships
  the exact defect beat B07 proposes to detect.
- The outro is OutroSeries, NEVER ClaudeTitleOutro (locked to @NikBearBrown).
- Author every composition at 1920x1080. remotion_scenes.py hardcodes --scale=2,
  so 1920x1080 renders as true 3840x2160. Never author at 1280x720.
- Audio is the clock. Regenerate audio and recompile; never hand-tune timing.

Steps:
1. Audio: python runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro af_bella, free and local. Writes mp3/ + timings.json and stamps
   actual_duration_s back into the beat sheet.
2. Set each reel-local composition's durationInFrames in Root.tsx to its beat's
   exact frame count (duration * 30). The components animate on progress, so they
   then fill the beat with no slow-motion and no centre-cut.
3. Render each beat to media/<BID>.mp4 at --scale=2 --image-format=png --crf=16.
   Where a composition is LONGER than its beat, render frames 0..N-1 (keeps the
   opening). Where SHORTER, render full then freeze-hold with ffmpeg tpad.
4. Compile: python runtime/scripts/compile.py <reel> --review --height 2160
   then without --review for the clean master.
5. QC by LOOKING at frames, not the probe. Sample every beat, check for clipped
   text, overlap, and anything outside the 5% title-safe inset.
6. Report and STOP. Never publish.
```

---

## What the video says (the four stages)

1. **Check the file before uploading.** Dimensions are in the file; reading them
   takes a second. Brutalist's own docs already specify this check — nobody wrote
   the code.
2. **Sort the Drive folder.** Pass one way, fail the other, with an actionable
   note. Nothing deleted.
3. **Stop it happening.** Put the check inside the tool so it refuses to finish a
   video that would fail. Fellows only send finished files, so the "measures 4K
   but is soft" case can only be caught on their machine — which is why this
   stage exists.
4. **Upload and review.** Blocked on two steps only the organisation can take.

---

## WINDOWS NOTES (this reel was built on Windows 11)

Two genuine portability bugs in the toolkit, neither affecting macOS or Linux:

1. **`runtime/scripts/todo.py`** calls `write_text()` with no encoding, so Windows
   uses cp1252 and crashes on the emoji in STATUS.md.
   Workaround: `set PYTHONUTF8=1`. Real fix: `write_text(..., encoding="utf-8")`.

2. **`runtime/scripts/remotion_scenes.py:88`** runs `subprocess.run(["npx", ...])`.
   On Windows npx is `npx.cmd`, which CreateProcess will not resolve, so it dies
   with `WinError 2`. Workaround: drive `npx remotion render` directly.
   Real fix: `shutil.which("npx")`.

Also: `python3` on Windows is a Microsoft Store stub. The real interpreter is
`python`. Every toolkit script shells out to `python3`, and `./art` is bash-only.

`./setup --install` cannot install ffmpeg or Node — it only checks for them.
On Windows: `winget install OpenJS.NodeJS.LTS` and `winget install Gyan.FFmpeg`.

---

## Verification

- `ffprobe` the master: must read 3840x2160. **Verified on B00 — the --scale=2
  path produces genuine 4K, measured not assumed.**
- The video must pass its own B07 check: the outro is the HAI outro and no beat
  shows @NikBearBrown.
- Every claim on screen traces to a row in FACTCHECK.md.
