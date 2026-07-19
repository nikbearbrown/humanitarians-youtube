You are Claude Code, building ONE video end to end, unattended. Work only inside this repo. Run each
step, fix your own errors, and follow the render contract. Do not ask for confirmation between steps.

SCOPE: work ONLY inside `brutalist-art/`. Never reach outside it (no `../vox/`, no `../unreal-reels/`,
no `~/…`, no `books/…`). Keys are in `./.env`. If something you need isn't in this folder, write a
`MISSING: <what> — was at <where> — blocks <beat/step>` line to the BUILD-LOG and stop that thread —
the human vendors it in. First read `EXAMPLES-CAMPAIGN.md`, especially the **Standing rules** — this
video IS about what happens when you ignore them, so follow them exactly.

LOG HUMAN FEEDBACK FIRST: any instruction the human gives mid-build → append it verbatim under a
`## HUMAN FEEDBACK — <date>` heading in `BUILD-LOG.md` BEFORE acting on it.

LOG EVERYTHING (append-only) to `youtube/when-cowork-helps-claude-code/BUILD-LOG.md`: every command,
error, fix (with the file changed), MISSING, and the final result.

SOURCE DOC: this video is the spoken form of `docs/cowork-and-claude-code.md`. Read it first.

REPO: the `brutalist-art` toolkit (you are at its root).
VIDEO FOLDER: `youtube/when-cowork-helps-claude-code/` — a self-contained reel folder.
SPEC: its `beat_sheet.json` is the heart. Read it, then `docs/cowork-and-claude-code.md`,
`runtime/README.md`, and `runtime/manim/animated_graphics.py` before writing anything.

RENDER CONTRACT (per scene): attempt; on failure retry ≤5×, fixing the error between tries; if it
still fails, leave that beat a slate and move on — never stall the reel on one scene. Palette is
`teardown`: white #FFFFFF, ink #2A1A0E, one red #C8102E, teal #1F6F5C as the single "good/kept"
accent. Never more than two accents.

STEP 1 — `scenes.py` (Manim). One `Scene` subclass per GRAPHIC beat with `shot.source=="own"`:
B01, B03, B05, B06, B07, B08, B10, B11, B13, B14. Class name = the beat's `graphic.manim`. Build each
from its `graphic.production_viz` (`label`, `mechanic`, `colors`) as clean progressive-disclosure line
art. Resolve the shared lib from this file's location:
    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
    from animated_graphics import *
Read durations from `beat_sheet.json` so each scene fills its beat. Size every bounding box to the
FULL text stack (SurroundingRectangle(VGroup(all lines), buff=…)), never the header alone; verify by
frame. B14 (`B14_TheLesson`) is the HERO — most care; title "A SECOND SET OF EYES" in EB Garamond,
teal accent; it echoes the video-1 conductor beat. B06 also calls back to the conductor — keep it
restrained.

STEP 2 — the three gate files: `FACTCHECK.md` (label the terminal outputs "illustrative — real
transcript, lightly trimmed"; the only figures are "43 processes", "9 beats", "15/15", "4m 47s" —
all real), `SHOTLIST.md` (one row per beat: id · shot type · source · what it shows), `PROMPTS.md`
("No open media slots — all beats are pipeline-rendered").

STEP 3 — Remotion beats: B00, B02, B04, B09, B12, B99.
- `cd runtime/remotion && npm install` (first time only), then back to repo root.
- RENDER WITH THE HELPER, foreground, never by hand:
      python3 runtime/scripts/remotion_scenes.py youtube/when-cowork-helps-claude-code
  (`--force` to re-render, `--only B04` for one). It renders each beat to `media/<BID>.mp4` at
  `--concurrency=1`. NEVER hand-roll `npx remotion render`, NEVER background a render, NEVER poll
  `ps`/`grep` for Chrome. (Yes — this is the exact mistake the video narrates. Don't make it.)
- The beat sheet's `shot.remotion.props` are ALREADY matched to each component's zod schema
  (BrutalistTerminalOpen: command/checklist/topic · NikBearBrownTerminalAsk: command/topic/segment/
  runningText/output · BrutalistCommentCTA: filename/code/variant/topic), all with `topic="A SECOND
  SET OF EYES"`. Don't strip those keys, or the beat will render Root.tsx demo defaults.

STEP 4 — Audio (master clock). If `ELEVENLABS_API_KEY` is set: `python3
runtime/scripts/generate_audio.py youtube/when-cowork-helps-claude-code` using
`ELEVENLABS_VOICE_NIKBEARBROWN`; then conform every scene to its measured audio. Else build the
SILENT cut and say so.

STEP 5 — Compile: `./art run youtube/when-cowork-helps-claude-code`. Apply the render contract.

STEP 6 — VERIFY BY LOOKING (this video's own thesis): after compile, read `qc-sheet.png` and confirm
every beat shows THIS video's content — no `Root.tsx` placeholder (photoelectric/cancer). If any beat
wears another video's text, its props didn't match the schema — fix and re-render with `--force`.

STEP 7 — Report: run `python3 runtime/scripts/todo.py youtube/when-cowork-helps-claude-code`, print
the ledger, and list any beat still a slate or rough. Don't claim done if any beat is a slate.

FINALLY — append a `## REFACTOR FEEDBACK — when-cowork-helps-claude-code — <date>` block (format in
EXAMPLES-CAMPAIGN.md) to BOTH this folder's BUILD-LOG.md and the repo-root CAMPAIGN-FEEDBACK.md.
