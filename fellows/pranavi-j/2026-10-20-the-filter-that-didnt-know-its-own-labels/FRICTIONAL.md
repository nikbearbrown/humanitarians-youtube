# Frictional log — The Filter That Didn't Know Its Own Labels

Written contemporaneously during this build (per this fellow's `research-plan.md` commitment for
this period), not reconstructed afterward. Entries are dated to when they actually happened.

## 2026-10-21 — Building the live verification harness

- Importing the real `app.routers.feeds` module (to mount it post-fix, unmodified, in a
  `TestClient`) transitively imports `app.crud` -> `app.database` -> `app.config.get_settings()`,
  which is a `pydantic-settings` `BaseSettings` that requires `database_url` with no default —
  raised `ValidationError: database_url Field required` on bare import, even though no DB
  connection is ever attempted (the CRUD call is mocked). Fixed by setting a syntactically-valid
  but inert `DATABASE_URL` env var (`postgresql://test:test@localhost:5432/test_db_not_used`)
  before the import; confirmed no actual network/DB call occurs by patching
  `FeedCRUD.list_feeds` with `unittest.mock.patch` before any request is sent.
- First harness run failed with `pydantic_core.ValidationError: 1 validation error for
  FeedListResponse: filters_applied Field required` — the real `FeedListResponse` model (in
  `models.py`) requires a `filters_applied` field the mock dict didn't include. Not a bug in the
  real code — my own mock response was incomplete. Added `"filters_applied": {}` to
  `MOCK_RESULT` and re-ran; both the post-fix and reconstructed pre-fix paths then returned clean,
  real status codes (200 and 422 respectively), confirmed in
  `verification/verify_source_feed_output.txt`.
- Decided NOT to `git checkout` the parent commit of `565e84e` to get the real pre-fix file (that
  would touch the working tree of a repo under explicit no-push/no-modify instructions). Instead
  reconstructed the exact pre-fix endpoint signature as a separate router mounted in its own
  isolated `FastAPI()` app, keeping the real post-fix `app.routers.feeds` import completely
  untouched for the other half of the comparison. Cross-checked the reconstruction's field-by-field
  signature directly against `git show 565e84e`'s diff context (not from memory) before trusting it
  as a faithful "before" baseline.

## 2026-10-21 — Audio-first build (Kokoro)

- `./art keys`/`generate_audio_kokoro.py --list-voices` refused immediately: the toolkit's
  `runtime/models/kokoro/` only had `voices-v1.0.bin` (28MB) on disk, not the actual
  `kokoro-v1.0.onnx` model (~325MB) — a prior session must have fetched the voice bank but not the
  model weights. Downloaded it directly from the documented release URL
  (`github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx`,
  confirmed the same source cited in `generate_audio_kokoro.py`'s own docstring) — no
  toolkit/script change needed, this was a one-time local setup gap, not a toolkit bug.

## 2026-10-21 — Authoring scenes.py (landscape): caught my own timing arithmetic slip

- While hand-deriving each scene's final `self.wait()` remainder against its measured Kokoro
  duration, wrote a small standalone checker (parses every `run_time=`/`self.wait()` literal per
  `Scene` class and sums it against `beat_sheet.json`'s `actual_duration_s`) before rendering
  anything, rather than trusting the by-hand arithmetic in the inline comments. First run flagged
  `B05_TestClientTable` as 1.5s too long (28.62s vs the measured 27.12s) — the inline comment had
  summed the beat's "plays" total without the opening title card's own `Write()`/`wait()` pair
  (0.5s play + 1.0s wait = exactly the 1.5s discrepancy). Fixed by correcting the final
  `self.wait()` from 18.42 to 16.92 and re-running the checker: all 9 scenes now sum exactly to
  their measured audio length. Same category of mistake this fellow's sibling reel's BUILD-LOG
  documented catching by hand after a render came back 1s long — catching it here before the first
  render avoided the wasted render cycle entirely.

## 2026-10-21 — Manim render / compile

- First `./art run . --height 2160` pass: GATE A clean on all 9 scenes (checked individually with
  `static_scene_check.py --class <Name>` before the full run, as well as inside the run itself).
  GATE B (`manim_layout_audit.py`, post-render pixel audit) flagged one real warning:
  `B04_TwoLineDiff`'s closing caption ("The database column was always just a string
  underneath.") landed with its real bottom edge at y=-3.45, just outside the documented
  +/-3.4 safe-area half-height — genuine overflow, not a false positive (the caption's own
  `to_edge(DOWN, buff=0.55)` left too little clearance once the actual rendered glyph height was
  measured). `ART_STRICT=1` (the default) correctly refused to slot the clip. Fixed by widening
  the bottom buffer to 0.75. Deleted the stale `manim/B04.mp4`, `media/videos/scenes/2160p24/B04_TwoLineDiff.mp4`
  and the per-beat partial-movie-file cache under `media/videos/scenes/2160p24/partial_movie_files/B04_TwoLineDiff/`
  before re-rendering, per this toolkit's known stale-cache gotcha (it does not detect
  `scenes.py` source edits on its own) — confirmed the regenerated clip's mtime postdated the
  `scenes.py` edit before trusting it.
- Full `./art run` pass (all 9 beats compiled, slate built, GATE V run on the review slate):
  `[gate-v] frames=18 BLOCKER=18 MAJOR=0` — every single sampled frame across every beat, including
  the simplest title card (B00), flagged identically: `edge-bleed — content crosses the
  title-safe right/top edge`. Did not take this at face value — extracted a real frame directly
  from the review slate (`_qc/slate_frame_check.png`, B00 at t=2s) and visually confirmed the real
  scene content (title + border frame) sits comfortably inside the card's own bordered frame,
  nowhere near the top-right corner; the actual top-right corner holds the slate's own burned-in
  per-beat timestamp overlay (`00:00:02.000`), which `final_frame_check.py`'s `BURN_IN_EXCLUDE`
  mask does not cover (it only blanks the bottom-left beat-label strip). This is the same review-
  slate false positive this fellow's sibling reels' BUILD-LOG already documented — proceeding to
  `./art final` for the true candidate (no slate chrome), per the toolkit's own design.
- `./art final` itself then refused outright (no `--lenient` escape hatch on its embedded check,
  as documented): `compile.py` ran `final_frame_check.py` against its own temp candidate and
  exited non-zero before ever writing a deliverable. Used the documented manual-master workaround:
  built the true final directly from the already-verified `clips/concat.txt` + `clips/_work/master.wav`
  via `ffmpeg -f concat ... -c:v libx264 -crf 16 ... -c:a aac -shortest`, then ran
  `final_frame_check.py . --mp4 deliverables/landscape/SourceFeedDynamicLabels_SaiPranaviJ.mp4
  --lenient` directly from inside the reel folder (the true candidate, not the `-slate.mp4`).
  Result: `BLOCKER=0 MAJOR=2`, both `low-contrast`: B07's bottom statement line used
  `PALETTE["gold"]` text directly on the cream page background (no ink panel behind it, unlike
  every other gold-text beat in this file) — real luminance separation 0.29 against the checker's
  0.3 floor, not a false positive. This file's own `PALETTE` dict already comments
  `"gold": ... # fill only — never text color`, which this one beat violated by following the
  sibling reel's B07 too literally. Fixed in both `scenes.py` and `vertical/scenes.py` by
  switching that line's color to `crimson` (already proven legible as text on `"bg"` elsewhere in
  both files, e.g. B03/B04's captions).
- Vertical GATE B flagged the same systemic issue twice more as `./art run vertical` progressed
  beat by beat: `B04_TwoLineDiff`'s 2-line title (`title.to_edge(UP, buff=0.5)`) and then, after
  that fix, `B05_TestClientTable`'s 2-line title (same `buff=0.5` default) each landed their real
  top edge at y=3.5, just past the +/-1.95 x / +/-3.4 y safe area — the exact same overflow already
  fixed on B03's title. Rather than fix these one at a time per re-render (each cycle costs a full
  Manim render + GATE B pass), widened `B05`'s title buff to 0.68 in the same edit and left a note
  that this is a systemic pattern (any 2-line `title.to_edge(UP)` in this file needs buff >= 0.68,
  not 0.5) — confirmed by `grep -n "to_edge(UP"` across the file that B06's title (single line, not
  two) was the only remaining `buff=0.5` instance, left as-is since a single short line has real
  headroom the 2-line titles don't.
  (Correction logged a few minutes later: that assumption was wrong — `B06_HonestLimits`'s
  single-line title at `buff=0.5` hit the exact same real overflow, `WARN outside safe area:
  box=[-1.26, 3.26, 1.26, 3.5]`. Fixed the same way, `buff=0.5 -> 0.68`. In hindsight this is a
  systemic property of this portrait frame's actual safe-area geometry at this font scale, not a
  per-beat coincidence — worth treating `buff=0.68` as this file's floor for any `title.to_edge(UP)`
  from the start of the next build, rather than re-discovering it beat by beat.)
- Rebuilt the landscape master a second time after the B07 contrast fix (same manual-master
  workaround as before: `ffmpeg -f concat ... clips/concat.txt ... -shortest`). First
  `final_frame_check.py --lenient` attempt against the freshly-overwritten file failed with
  `moov atom not found` / `Invalid data found when processing input` — not a real defect: the
  `ffmpeg` encode (auto-backgrounded past the 120s foreground timeout) was still mid-write when the
  check ran against it. Waited for the actual background-command-completed notification (not a
  fixed sleep) before re-probing the file; the second attempt read a complete, valid MP4 and GATE V
  passed clean.
- Built the true final vertical master the same way (`ffmpeg -f concat ... vertical/clips/concat.txt
  ... vertical/clips/_work/master.wav ...`) and ran `final_frame_check.py vertical --mp4
  deliverables/vertical/SourceFeedDynamicLabels_SaiPranaviJ.mp4 --lenient`: `BLOCKER=0 MAJOR=2`,
  both `underfill` on `B01_ExecSummary` — real content covering only 52% of the safe area (min
  55%), genuine underfill from tight inter-group spacing (the badge/name/role header, the summary
  paragraph, and the top/bottom rules were packed at `buff=0.4` with only `buff=0.1` inside the
  summary itself), not a false positive. Fixed by widening the summary's internal buff to 0.18 and
  the top-level `arrange(DOWN, buff=...)` from 0.4 to 0.7 — no text changed, only spacing.
- Re-ran `./art run vertical` once more with the B01 fix; all 9 beats slotted, GATE B clean (0
  errors, 0 warnings). Rebuilt the true final vertical master and re-ran
  `final_frame_check.py vertical --lenient`: `BLOCKER=0 MAJOR=0`. Both true final masters are now
  clean. Wrote `.verified.json` sidecars (SHA-256 + duration + GATE V result) next to both
  deliverables, then personally extracted and visually inspected spot-check frames from both
  shipped MP4s (not the slate, not an intermediate render) — B03's enum/code panels and
  highlighted template literal, B05's TestClient table, B06's honest-limits cards, B07's
  re-colored takeaway line past its fade-in, and B01/B08 in the vertical master — before
  considering this build done. No further defects found.

## Closing note

Every entry above is real and dated to when it happened during this single build session
(2026-10-20 research/verification, 2026-10-21 audio + render + compile). Nothing here was
back-filled after the fact.
