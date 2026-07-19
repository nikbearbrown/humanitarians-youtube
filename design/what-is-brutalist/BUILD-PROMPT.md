You are Claude Code, building ONE video end to end. Work only inside this repo. Run each step,
fix your own errors, and follow the render contract below. Do not ask for confirmation between
steps — this is an unattended build.

SCOPE: work ONLY inside `brutalist-art/`. Do NOT reach outside it (no `../vox/`, no
`../unreal-reels/`, no `~/…`, no `books/…`). Keys are in `brutalist-art/.env`. If you need
something that is not in this folder, do NOT resolve it against a parent repo — write a line
`MISSING: <what> — was at <where, if known> — blocks <beat/step>` to the BUILD-LOG and stop that
thread; the human will vendor it in. First read `EXAMPLES-CAMPAIGN.md` for the campaign rules.

VERIFY every visual fix by extracting a frame and looking — never report a box/layout fixed without confirming the text is inside the border in an actual rendered frame.

LOG EVERYTHING to `youtube/what-is-brutalist/BUILD-LOG.md` (append-only): every command, every
error, every fix (with the file changed), every `MISSING:`, and the final result (beats rendered /
beats left for the human).

REPO: the `brutalist-art` toolkit (you are at its root).
VIDEO FOLDER: `youtube/what-is-brutalist/` — a self-contained reel folder.
SPEC: `youtube/what-is-brutalist/beat_sheet.json` is the heart. Read it first. Also read
`README.md`, `runtime/README.md`, and `runtime/manim/animated_graphics.py` (the shared Manim lib)
before writing anything.

RENDER CONTRACT (apply to every scene):
- Attempt the render. On failure, retry up to FIVE times, fixing the error between attempts.
- If a scene still fails after five tries, LEAVE THAT BEAT UNRENDERED and move on to the next.
  Never stall the whole reel on one scene. A finished pass may contain a few missing beats — that
  is expected; the human reviews the cut and redoes those.
- Palette is `teardown`: flat white #FFFFFF, ink #2A1A0E, one red #C8102E; teal #1F6F5C as the
  single "good/kept" accent. Never more than two accents.

STEP 1 — Write `youtube/what-is-brutalist/scenes.py` (the Manim scenes).
- One Manim `Scene` subclass per GRAPHIC beat with `shot.source == "own"`. From the beat sheet
  those are: B01, B02, B03, B05, B06, B07, B08, B09, B11, B14. The class name is the beat's
  `graphic.manim` value (e.g. `B01_OneClickSlop`).
- Build each scene from that beat's `graphic.production_viz` (`label`, `mechanic`, `colors`). The
  `mechanic` text is the drawing instruction; render it as clean progressive-disclosure line art.
- Resolve the shared library from THIS file's location — the folder is at
  `<repo>/youtube/what-is-brutalist/`, so:
      import sys, pathlib
      sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
      from animated_graphics import *
  Do NOT use any `vox/aspects/...` path — that layout no longer exists.
- Read beat durations from `beat_sheet.json` (`estimated_duration_s`) so each scene fills its beat.
- B07 (`B07_YouAreTheConductor`) is the hero beat — give it the most care: the baton stroke + the
  title "YOU ARE THE CONDUCTOR" in EB Garamond.

STEP 2 — Write the three gate files in the folder (required by `run.sh` GATE F):
- `FACTCHECK.md` — list any on-screen numbers as illustrative. The only figures are the demo
  terminal outputs in B04/B10/B12/B13; label them "illustrative — sample CLI output."
- `SHOTLIST.md` — a one-row-per-beat table (beat id · shot type · source · what it shows).
- `PROMPTS.md` — for any beat needing external media, a beat-prefixed prompt. (This reel has none;
  write "No open media slots — all beats are pipeline-rendered" so the gate passes.)

STEP 3 — Render the Remotion terminal beats: B00, B04, B10, B12, B13, B99.
- `cd runtime/remotion && npm install` (first time only).
- Each of these beats names a scene in `shot.remotion.pattern` that exists in
  `runtime/remotion/src/scenes/` and is registered in `runtime/remotion/src/Root.tsx`:
  BrutalistTerminalOpen (B00), NikBearBrownCodeBlock (B04, B13), NikBearBrownTerminalAsk (B10, B12),
  BrutalistCommentCTA (B99).
- IMPORTANT: the props in the beat sheet express the INTENT but do NOT all match each component's
  zod schema. Open each component, read its `z.object({...})` schema, and for each beat EITHER map
  the beat's intent onto the real props OR extend the component to render what the beat needs
  (e.g. a terminal that shows a `$ command` followed by several output lines — B10/B12 want a
  multi-line output block that `NikBearBrownTerminalAsk` doesn't have yet; add an optional
  `output: z.array(z.string())` prop and render it, rather than dropping the output). Keep the
  teardown palette. Register any new/edited composition in `Root.tsx`.
- Render each beat to `youtube/what-is-brutalist/media/<BID>.mp4`, conforming duration to that
  beat's audio if audio exists (else to `estimated_duration_s`).

STEP 4 — Audio (the master clock).
- If `ELEVENLABS_API_KEY` is set: run `python3 runtime/scripts/generate_audio.py
  youtube/what-is-brutalist` to make one mp3 per beat from `narration_text`, using the voice in
  `ELEVENLABS_VOICE_NIKBEARBROWN` (the beat sheet's `metadata.voice_env`). Then re-render/conform
  every scene to its measured audio length.
- If no key is set: build the SILENT cut (scenes timed to `estimated_duration_s`) and note in the
  final report that narration was skipped.

STEP 5 — Compile the reel.
- Run `bash runtime/scripts/run.sh youtube/what-is-brutalist` (or `./art run
  youtube/what-is-brutalist`). It renders pending Manim scenes from `scenes.py`, slots every beat,
  and assembles the cut. `run.sh` requires `scenes.py` + the three gate files from Steps 1–2 — they
  now exist. (`./art fill-in` is not yet a command; do the steps directly as above.)
- Apply the render contract per scene. Any beat that can't render after 5 tries stays a slate.

STEP 6 — Report.
- Run `python3 runtime/scripts/todo.py youtube/what-is-brutalist` and print the ledger.
- List every beat that ended UNRENDERED or looks rough, with the reason, so the human knows exactly
  which beats to review and redo. Do not claim the video is done if any beat is still a slate —
  report it honestly as "draft, N beats need human review."

Deliverable: `youtube/what-is-brutalist/` containing `scenes.py`, the three gate files, `manim/` +
`media/` renders, `mp3/` (if narrated), the compiled cut, and an up-to-date `STATUS.md`.

FINALLY — emit the refactor report. Append a `## REFACTOR FEEDBACK — what-is-brutalist — <date>`
block (format in EXAMPLES-CAMPAIGN.md) to BOTH `youtube/what-is-brutalist/BUILD-LOG.md` and the
repo-root `CAMPAIGN-FEEDBACK.md`: list MISSING (vendor), FIXED (with commit), DEPS (installs
needed), STILL BLOCKED, and RESULT (beats rendered / left for human). This block is the report the
refactor consumes — make it accurate.
