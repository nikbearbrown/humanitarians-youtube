# Frictional log — The Dashboard That Disagreed With Its Own Alerts

Written contemporaneously during this build, not reconstructed afterward. Entries are dated to
when they actually happened (same session, 2026-11-03).

## 2026-11-03 — Building the live verification harness

- The real bug and fix are in a raw SQL string inside a Python function
  (`Regulatory_QA/backend/app/crud.py`'s `FeedCRUD.get_stats()`), not JS inside an n8n workflow
  like last week's C3 report — so this harness could be plain Python, no `node:vm` needed.
- First tried to connect directly to the real, live `mycroft_intelligence` Postgres DB the same
  way the real backend does (`from app.database import get_db, get_cursor`), to query it fresh
  rather than reconstruct a synthetic table. Hit the same category of friction the 2026-10-20
  report's FastAPI harness documented: `app.config.Settings` is a `pydantic_settings.BaseSettings`
  that requires `database_url` from a `.env` file, and this shell has no working `DATABASE_URL`/
  `.env` loaded for that backend — `Settings()` raised `pydantic_core.ValidationError: database_url
  Field required`. Did not try to read or reconstruct the real `.env` contents (out of scope and
  unnecessary — the real counts are already independently documented in `D1-VERIFICATION.md` and
  `RUN_LOG.md`'s 2026-11-03 entry from this week's own live-DB run). Pivoted to the same
  discipline last week's Node harness used for a different bug: extract the REAL current SQL
  string from the real file on disk, confirm it matches verbatim exactly once, reconstruct the
  pre-fix SQL by undoing the exact documented diff, and run both against a dataset built to match
  the documented aggregate distribution exactly — not a live second query, and said so plainly in
  the harness's own docstring and in `FACTCHECK.md` #4, rather than overclaiming a fresh DB hit.
- Used `sqlite3` (Python stdlib) instead of a mocked Postgres connection — confirmed first that
  `sqlite3`'s bundled engine (3.51.2 on this machine) supports the same `COUNT(*) FILTER (WHERE
  ...)` aggregate syntax Postgres uses, so the real SQL strings could be run completely unmodified
  (only the `WHERE created_at >= NOW() - INTERVAL '7 days'` windowing clause is stripped for the
  unwindowed comparison, matching exactly what `D1-VERIFICATION.md` itself did and documented).
- Solving for a synthetic 411-row dataset that reproduces the documented 4-tier distribution
  (old: Critical 32/High 139/Medium 240/Low 0; new: Critical 33/High 98/Medium 280/Low 0; 62/411
  disagreements) is a small transportation/assignment problem — worked it by hand (shown in the
  harness's own module docstring and inline comments) before writing the row list, rather than
  guessing values and hoping they summed correctly.
- First run of the harness failed one assertion: `old High inflation == 30%` — had written the
  denominator as the NEW (true) count (`41/98 = 41.8%`) instead of the OLD (reported) count
  (`41/139 = 29.5%`, which `D1-VERIFICATION.md` rounds to "30% inflated"). Fixed the assertion to
  divide by `pre["high"]` (the old, reported total) and widened the check to a small tolerance band
  (29–30%) rather than a single rounded integer, since `D1-VERIFICATION.md`'s own "30%" is itself a
  rounding of 29.5%, not an exact figure. Re-ran: all 13 assertions pass.
- Confirmed via `git -C /Users/pranavijs/mycroft status --short` before and after writing/running
  the harness: identical set of pre-existing, unrelated changes both times (`logs/RUN_LOG.md`,
  two unrelated `package-lock.json` files, `crud.py` itself — all from the real D1 engineering work
  already done before this video session, not from this session's own read-only harness) plus the
  untracked `D1-VERIFICATION.md`. This session made no changes to the `mycroft` repo.

## 2026-11-03 — Audio-first build (Kokoro)

- `generate_audio_kokoro.py` ran clean on the first attempt (voice model already present from this
  fellow's prior episodes' setup). Measured durations came in noticeably shorter than the draft
  beat sheet's pre-audio estimates for several beats (e.g. B01 estimated 18s, measured 14.28s; B03
  estimated 27s, measured 24.12s) — kept the real measured numbers as the timing target throughout,
  per the audio-first rule, rather than padding scenes to hit the original estimate.
- B00's silent track: `ffmpeg -f lavfi -i anullsrc ... -t 4.05` measured 4.104s on `ffprobe` (mp3
  frame-boundary rounding, same effect this fellow's prior reports documented), not exactly 4.05 —
  used the real measured value (4.10, rounded) as B00's `actual_duration_s`/timing target.
- Total measured audio across all 9 beats: 144.78s (B00 4.10 + B01 14.28 + B02 17.95 + B03 24.12 +
  B04 17.88 + B05 24.55 + B06 29.11 + B07 11.28 + B08 1.51) — shorter than the draft ~160s target,
  kept as-is rather than artificially padded, since duration is an output of the real narration,
  never a target to hit by stretching silence.

## 2026-11-03 — Authoring scenes.py (landscape + vertical)

- Wrote a standalone timing checker (AST-parses every `run_time=`/`self.wait()` literal per `Scene`
  class and sums it against `beat_sheet.json`'s measured `actual_duration_s`, kept in the session
  scratchpad, not part of this project folder — same checker pattern this fellow's sibling reels
  documented building) BEFORE rendering anything. Landscape `scenes.py` matched every beat's
  measured duration to the millisecond on the first pass. The first vertical `vertical/scenes.py`
  draft had one real arithmetic slip: `B05_HarnessTable`'s explicit play/wait literals summed to
  24.85s against a measured 24.55s target (off by 0.3s) — traced to the vertical redesign having a
  different number of `self.play()` calls than the landscape version (one extra `Create()` for the
  per-row crimson box plus a differently-grouped FadeIn for the last two tiles) without re-summing
  the final `self.wait()` remainder. Fixed by reducing the final wait from 16.95 to 16.65; re-ran
  the checker — exact match (24.549999... vs. 24.55, within float rounding).
- Applied every systemic portrait fix this fellow's prior reports' vertical builds already
  documented (the buff=0.68 safe-area floor for 2-line `title.to_edge(UP)`, `next_to(panel, DOWN,
  ...)` instead of an independent `to_edge(DOWN)` for any caption following a variable-height panel
  stack, the B03 panel-stack height cap of 4.3, and generous internal buffs/enlarged type for
  canvas-fill) proactively from the first draft, rather than waiting for GATE B/V to re-discover
  them on this reel's own content.
- `static_scene_check.py --class <Name>` ran clean (0 warn/error) on all 9 landscape scenes and all
  9 vertical scenes on the first pass — no GATE A defects this build.

## 2026-11-03 — Manim render / compile (landscape)

- `./art run` (landscape, native 4K/2160-height default): GATE A clean on all 9 scenes going in,
  GATE B (`manim_layout_audit.py`) clean on all 9 scenes on the first full pass. Review-slate GATE V
  reported the documented burn-in false positive (`frames=18 BLOCKER=18 MAJOR=0`, every frame
  flagged `edge-bleed`) — not trusted at face value; built the true final master manually
  (`ffmpeg -f concat -safe 0 -i clips/concat.txt -i clips/_work/master.wav -map 0:v -map 1:a -c:v
  libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a aac -shortest
  deliverables/landscape/DashboardSeverityDrift_SaiPranaviJ.mp4`) and ran
  `final_frame_check.py . --mp4 deliverables/landscape/DashboardSeverityDrift_SaiPranaviJ.mp4
  --lenient` from inside the reel folder.
- First true-master GATE V pass: **BLOCKER=0, MAJOR=2** — both `underfill` findings on
  `B05_HarnessTable` (`content fills only 50% of the safe area (min 55%)`, sampled at both the 50%
  and 85% marks of that beat). Extracted and visually inspected both flagged frames
  (`ffmpeg -ss <t> -i <mp4> -frames:v 1 ...`) before fixing anything — confirmed a real defect, not
  a false positive: B05's title was pinned to the top edge (`to_edge(UP, buff=0.6)`) and every
  element below it was chained off that anchor via `next_to()`, so the whole block (title, 4 tier
  tiles, totals, 2 captions) clustered in the top ~45% of the frame with the entire bottom half
  empty. Fixed by enlarging the tiles/type (head 18pt->22pt, values 26pt->32pt, tile padding
  0.6->0.9) and, more importantly, restructuring the scene to build title/tiles/totals/captions
  as one `VGroup(...).arrange(DOWN, buff=0.7).move_to(ORIGIN)` — vertically CENTERED as a block,
  rather than top-anchored — same canvas-fill principle documented in sibling reels but applied via
  centering here instead of just enlarging content. Also applied the identical centering fix
  preemptively to `vertical/scenes.py`'s own B05 (same top-anchored risk, smaller safe area) before
  ever rendering it, rather than waiting to rediscover the same defect on the second aspect.
- Re-ran `./art run` (B05 only; deleted the stale `manim/B05.mp4`/`clips/B05.mp4`/media cache
  first) — GATE B clean. Rebuilt the true final master, re-ran `final_frame_check.py --lenient`:
  **BLOCKER=0, MAJOR=0** on the underfill issue, but a SECOND, independent real defect turned up on
  personal frame inspection (not caught by the automated gate, which only checks fill/overlap/edge-
  bleed, not text-highlight correctness) — see next entry.
- Personally extracting and inspecting a `B03_OneQueryOneColumn` frame (not prompted by any gate —
  routine spot-check before trusting the master) revealed the crimson highlight box around
  "urgency_score" was landing 1-2 characters late, boxing "rgency_score >=" instead of
  "urgency_score". Root cause: this scene highlights a substring by slicing the `Text` mobject
  directly (`line[start:end]`, using the plain python string's character offsets) — but Manim's
  `Text` only gives a glyph submobject to NON-whitespace characters; the two spaces before
  "urgency_score" in `"FILTER (WHERE urgency_score ..."` are never in `self.submobjects`, so a
  python-string-index slice silently drifts by the number of preceding spaces. This went unnoticed
  through GATE A/B/V because none of those gates check whether a highlighted substring is the
  CORRECT substring, only layout/overlap/fill — a real gap in the automated QC this build actually
  hit, worth flagging for future reels doing the same kind of inline substring highlight.
  - First fix attempt: manually split each line into separate prefix/needle/suffix `Text()` pieces
    arranged with `buff=0`, each colored independently. This fixed the highlight boundary (verified
    by a second rendered-frame inspection) but introduced a NEW, different real defect: Manim's
    `Text` trims each piece's own leading/trailing whitespace from its layout box, so three `Text()`
    objects packed at `buff=0` lose the actual space character entirely — the rendered line read
    "FILTER (WHEREurgency_score>= 8) as" with no gaps around the highlighted word. Caught by a third
    rendered-frame inspection before considering this attempt done.
  - Second fix attempt: Manim's `Text` exposes a `.chars` property specifically built to restore
    whitespace-inclusive indexing (`self.chars[start:end]` lines up with plain string offsets,
    unlike `self[start:end]`) — confirmed correct via a standalone script against real Manim
    (`t.chars[i:j]` returned exactly the 13-character "urgency_score" span, correctly positioned,
    both before and after the same `.scale()` call `T()` applies). This was the technically correct
    fix for real Manim, but running `static_scene_check.py --class B03_OneQueryOneColumn` (this
    toolkit's render-free GATE A pre-flight, which fakes `sys.modules["manim"]` with a lightweight
    stub so it can run without a working Manim/pangocairo install) immediately hard-failed:
    `TypeError: 'function' object is not subscriptable`. Traced the root cause by reading the
    stub's `_Mob.__getattr__` (`static_scene_check.py`): any attribute the stub doesn't explicitly
    implement — including `.chars` — resolves to a generic no-op callable, so `line.chars[i:j]`
    tried to subscript a function object. Since GATE A is wired as a hard blocking gate in
    `run.sh` (`rc >= 2` → `exit 2`, "nothing rendered"), this fix was a non-starter for this
    toolkit regardless of its correctness under real Manim.
  - Third, final fix: Manim's `Text(..., t2c={needle: color})` constructor parameter colors a named
    substring using Manim's own internal (correct) index resolution — no manual slicing at all.
    Confirmed correct against real Manim first (a standalone script showed exactly 13 consecutive
    submobjects recolored crimson, matching "urgency_score" exactly) and confirmed GATE-A-safe
    second (the `static_scene_check.py` stub accepts and silently ignores unrecognized kwargs like
    `t2c`, so it neither crashes nor needs to understand it). Since there is no cheap way to get a
    handle on just the `t2c`-colored span for boxing without `.chars`, redesigned the emphasis box
    to wrap the WHOLE line (both relevant FILTER lines), not just the substring within it — a
    deliberate, documented scope change from the original design, not a workaround that hides the
    defect. Re-rendered B03 a second time (GATE A/B clean), rebuilt the true final master, re-ran
    `final_frame_check.py --lenient`: **BLOCKER=0, MAJOR=0**. Personally re-extracted and inspected
    the B03 frame a fourth time — "urgency_score" now colored crimson with no collapsed spacing, and
    boxed cleanly within its own full line.
- Final true-master GATE V re-check (after both the B05 underfill fix and the B03 three-attempt
  highlight fix): **BLOCKER=0, MAJOR=0**. Landscape master confirmed 3840x2160, 24fps, 144.958333s
  via `ffprobe`.

## 2026-11-03 — Manim render / compile (vertical)

- `./art vertical` scaffolded `vertical/beat_sheet.json`, correctly picking up the hand-authored
  `vertical/scenes.py` already written (same scene class names as the landscape parent, `shot.manim`
  pointing at it, not rewired to a `shot.remotion.pattern` 916 composition) — no Remotion re-render
  step needed. The command's own printed "ONDA CHECK BLOCKED"/"needs native portrait scene916"
  warnings turned out to be a generic message `shorts.py` prints for every beat regardless of lane;
  confirmed harmless by checking the actual written `vertical/beat_sheet.json` (every beat still
  `shot.type: GRAPHIC` with the correct `manim.scene`) before treating it as a real blocker.
- First `./art run vertical --height 3840` pass: GATE B failed outright (not just a warning) on
  `B02_DashboardVsEmailHook` — 2 real WARNs: the title's real top edge at y=3.48 and the zinger's
  real bottom edge at y=-3.48, both just outside the +/-3.4 safe half-height, once the whole
  title+tiles+zinger block was centered at `buff=0.7`. Confirmed genuine (not a false positive) by
  reading the reported bounding boxes directly against the documented safe half-extents. Fixed by
  tightening the top-level arrange buff from 0.7 to 0.55 (saves 0.3 units of total block height
  across the two gaps) rather than shrinking the tiles/type that this project's canvas-fill
  requirement needs to stay large — re-ran `static_scene_check.py --class B02_DashboardVsEmailHook`
  (clean) before re-rendering just that one beat.
- Re-ran `./art run vertical`: GATE B clean, all 9 beats slotted at true 3840p24 (confirmed via the
  manim render log's own `3840p24` output-folder naming). Review-slate GATE V again reported the
  same known burn-in false positive (`BLOCKER=18 MAJOR=0`) — not trusted at face value, same as the
  landscape pass.
- Proactively applying the landscape B05 fix (vertical-centered block instead of top-anchored) to
  `vertical/scenes.py`'s own B05 BEFORE this first render meant B05 needed no second round-trip
  here — confirmed clean on the very first vertical GATE B/V pass for that beat.

Built the true final vertical master the same way as the landscape master
(`ffmpeg -f concat -safe 0 -i vertical/clips/concat.txt -i vertical/clips/_work/master.wav -map 0:v
-map 1:a -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a aac -shortest
deliverables/vertical/DashboardSeverityDrift_SaiPranaviJ.mp4`) and ran
`final_frame_check.py vertical --mp4 deliverables/vertical/DashboardSeverityDrift_SaiPranaviJ.mp4
--lenient`: **BLOCKER=0, MAJOR=0** — clean on the first true-master pass, no further fixes needed
for vertical (the B02 safe-area fix and the proactive B05 centering fix applied before ever
rendering this aspect meant no second round-trip was needed here, unlike the landscape pass's two
real bugs). Confirmed via `ffprobe`: 2160x3840, 24fps, 144.958333s — identical duration to the
landscape master (every beat kept, nothing dropped, via `./art vertical` — no cap, no rewritten
outro, no added endcard). Wrote `.verified.json` sidecars (SHA-256 + duration + GATE V result) next
to both deliverables, then personally extracted and visually inspected spot-check frames from both
shipped MP4s (not the slate, not an intermediate render) — B00's title card, B02's dashboard-vs-
email tiles, B03's SQL highlight (now correctly bounding "urgency_score" with real spacing intact),
B05's redesigned harness table, B06's honest-limit cards, and B08's sign-off (correct
"@HumanitariansAI" and "Sai Pranavi J." attribution) — in both the landscape and vertical masters,
before considering this project done. No further defects found.

## Closing note

Every entry above is real and dated to when it happened during this single build session
(2026-11-03: research/verification, audio generation, scene authoring, render/compile for both
aspects, and three real bugs found and fixed via GATE B/V and personal frame inspection — the B05
underfill, the vertical B02 safe-area overflow, and the B03 highlight-indexing defect, the last of
which took three attempts to fix correctly within this toolkit's constraints). Nothing here was
back-filled after the fact.
