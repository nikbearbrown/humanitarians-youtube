You are Claude Code, building ONE video end to end. Work only inside this repo. Run each step,
fix your own errors, and follow the render contract below. Do not ask for confirmation between
steps — this is an unattended build.

SCOPE: work ONLY inside `brutalist-art/`. Do NOT reach outside it (no `../vox/`, no
`../unreal-reels/`, no `~/…`, no `books/…`). Keys are in `brutalist-art/.env`. If you need
something that is not in this folder, do NOT resolve it against a parent repo — write a line
`MISSING: <what> — was at <where, if known> — blocks <beat/step>` to the BUILD-LOG and stop that
thread; the human will vendor it in. First read `EXAMPLES-CAMPAIGN.md` for the campaign rules.

LOG HUMAN FEEDBACK FIRST: if the human gives feedback during the build, append it verbatim under a
`## HUMAN FEEDBACK` heading in `BUILD-LOG.md` BEFORE you act on it.

VERIFY every visual fix by extracting a frame and looking — never report a box/layout fixed without
confirming the text is inside the border in an actual rendered frame.

LOG EVERYTHING to `youtube/installs/BUILD-LOG.md` (append-only): every command, every error, every
fix (with the file changed), every `MISSING:`, and the final result (beats rendered / beats left
for the human).

SOURCE DOC: this video is the spoken form of `docs/Installs.md`. Read it — the narration is already
written in the beat sheet, but the doc is the ground truth for anything you need to expand.

REPO: the `brutalist-art` toolkit (you are at its root).
VIDEO FOLDER: `youtube/installs/` — a self-contained reel folder.
SPEC: `youtube/installs/beat_sheet.json` is the heart. Read it first. Also read `docs/Installs.md`,
`runtime/README.md`, and `runtime/manim/animated_graphics.py` (the shared Manim lib) before writing
anything.

RENDER CONTRACT (apply to every scene):
- Attempt the render. On failure, retry up to FIVE times, fixing the error between attempts.
- If a scene still fails after five tries, LEAVE THAT BEAT UNRENDERED and move on to the next.
  Never stall the whole reel on one scene. A finished pass may contain a few missing beats — that
  is expected; the human reviews the cut and redoes those.
- Palette is `teardown`: flat white #FFFFFF, ink #2A1A0E, one red #C8102E; teal #1F6F5C as the
  single "good/kept" accent. Never more than two accents.

STEP 1 — Write `youtube/installs/scenes.py` (the Manim scenes).
- One Manim `Scene` subclass per GRAPHIC beat with `shot.source == "own"`. From the beat sheet
  those are: B01, B03, B04, B06, B07, B09, B10, B11, B12. The class name is the beat's
  `graphic.manim` value (e.g. `B01_OneFileEverything`).
- Build each scene from that beat's `graphic.production_viz` (`label`, `mechanic`, `colors`). The
  `mechanic` text is the drawing instruction; render it as clean progressive-disclosure line art.
- Resolve the shared library from THIS file's location:
      import sys, pathlib
      sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
      from animated_graphics import *
  Do NOT use any `vox/aspects/...` path — that layout no longer exists.
- Read beat durations from `beat_sheet.json` (`estimated_duration_s`) so each scene fills its beat.
- B11 (`B11_CloneYourVoice`) is the HERO beat — give it the most care: the "30 min ONCE vs 30 min
  EVERY session" split-scale, title "CLONE YOUR VOICE" in EB Garamond, teal on the "once" side.
- Boxes must fit their text: size any bounding box to the FULL text stack it contains
  (SurroundingRectangle(VGroup(all lines), buff=…)), never to the header alone. Verify by frame.

STEP 2 — Write the three gate files in the folder (required by `run.sh` GATE F):
- `FACTCHECK.md` — the only on-screen figures are the demo terminal outputs (B08/B13) and the
  "~30 minutes" claim; label the terminal outputs "illustrative — sample CLI output" and the 30-min
  figure as an estimate.
- `SHOTLIST.md` — a one-row-per-beat table (beat id · shot type · source · what it shows).
- `PROMPTS.md` — for any beat needing external media, a beat-prefixed prompt. This reel has none;
  write "No open media slots — all beats are pipeline-rendered" so the gate passes.

STEP 3 — Render the Remotion beats: B00, B02, B05, B08, B13, B99.
- `cd runtime/remotion && npm install` (first time only), then `cd` back to the repo root.
- Render with the HELPER, never by hand:
      python3 runtime/scripts/remotion_scenes.py youtube/installs        # (--force to re-render, --only B08 for one)
  It renders each slate beat to `media/<BID>.mp4` in the FOREGROUND at `--concurrency=1` and stamps
  provenance. NEVER hand-roll `npx remotion render`, NEVER background a render, NEVER poll `ps`/`grep`.
- BEFORE rendering, make each beat's `shot.remotion.props` match the component's real zod schema —
  any key that doesn't match is ignored and the composition renders its `Root.tsx` demo defaults
  (cancer-biology / photoelectric-effect). The real prop names:
    - BrutalistTerminalOpen (B00): `command`, `checklist`, `topic`
    - NikBearBrownCodeBlock (B02, B05): `filename`, `segment`, `topic`, `code`, `language?`, `caption?`
    - NikBearBrownTerminalAsk (B08, B13): `command`, `topic`, `segment`, `runningText`, `output?`
    - BrutalistCommentCTA (B99): `filename`, `code`, `variant`, `topic`
  Set `topic` to "SET UP ONCE" on all six so none inherit another video's topic.
- The compiler conforms each clip to the beat's audio by CENTER-CUT; the fixed composition durations
  are long, so terminal beats get trimmed head+tail. After compile, check `qc-sheet.png` that the
  type-on reveal survived; if a beat's head is cut, lower its composition `durationInFrames`.

STEP 4 — Audio (the master clock).
- If `ELEVENLABS_API_KEY` is set: run `python3 runtime/scripts/generate_audio.py youtube/installs`
  to make one mp3 per beat from `narration_text`, using `ELEVENLABS_VOICE_NIKBEARBROWN` (the beat
  sheet's `metadata.voice_env`). Then re-render/conform every scene to its measured audio length.
- If no key is set: build the SILENT cut (scenes timed to `estimated_duration_s`) and note in the
  final report that narration was skipped.

STEP 5 — Compile the reel.
- Run `./art run youtube/installs` (wraps `runtime/scripts/run.sh`). It renders pending Manim scenes
  from `scenes.py`, slots every beat, and assembles the cut. Apply the render contract per scene.

STEP 6 — Report.
- Run `python3 runtime/scripts/todo.py youtube/installs` and print the ledger. Every beat should
  report `pipeline` (zero human beats — this explainer is fully machine-buildable, same as video 1).
- List every beat that ended UNRENDERED or looks rough, with the reason. Do not claim the video is
  done if any beat is still a slate — report it honestly as "draft, N beats need human review."

Deliverable: `youtube/installs/` containing `scenes.py`, the three gate files, `manim/` + `media/`
renders, `mp3/` (if narrated), the compiled cut, and an up-to-date `STATUS.md`.

FINALLY — emit the refactor report. Append a `## REFACTOR FEEDBACK — installs — <date>` block
(format in EXAMPLES-CAMPAIGN.md) to BOTH `youtube/installs/BUILD-LOG.md` and the repo-root
`CAMPAIGN-FEEDBACK.md`: MISSING (vendor), FIXED (with commit), DEPS (installs needed), STILL
BLOCKED, and RESULT (beats rendered / left for human).
