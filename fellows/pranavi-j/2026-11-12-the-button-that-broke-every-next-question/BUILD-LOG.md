# BUILD-LOG — The Button That Broke Every Next Question

## 2026-11-12 — Research and verification

**Gate P:** Beat sheet approved 2026-11-12. **FACTCHECK:** resolved same day — all claims traced to
the real, current `Regulatory_QA/frontend/src/App.jsx` and `src/components/ChatInterface.jsx`
(read-only, not modified this session), `scripts/regulatory-intel/E1-VERIFICATION.md`,
`/Users/pranavijs/mycroft/logs/RUN_LOG.md`'s 2026-11-12 entry, and this session's own live Node.js
verification harness (`verification/verify_feed_cap.js`, `verification/verify_feed_cap_output.txt`):
the real, current `handleToggle`/`handleSelectAll` and error-reason-extraction logic (confirmed to
match the real source files verbatim, exactly once each) reproduces `E1-VERIFICATION.md`'s own 5
behavioral checks (7 assertions) exactly, including the real captured FastAPI 422 message text. See
`FACTCHECK.md` and `SOURCES.md` for the full claim-by-claim trace. See `FRICTIONAL.md` for the real,
dated build-time snags (including a rewrite of the harness driver after catching that an early draft
re-implemented the selection logic instead of actually running the extracted real source text).

Confirmed via `git -C /Users/pranavijs/mycroft status --short` before and after this project's
research/verification work: identical pre-existing, unrelated diffs both times (two unrelated
`package-lock.json` files, from other, unrelated Project 29 components) plus no changes to
`App.jsx`, `ChatInterface.jsx`, or `logs/RUN_LOG.md` — these were already committed from the real E1
engineering work done before this video session. This session made no changes to the `mycroft` repo.

## 2026-11-12 — Full build (both aspects)

**Audio:** Kokoro `af_bella`, all 9 beats. B01-B08 generated via `generate_audio_kokoro.py`
(measured durations: B01 14.06s, B02 15.34s, B03 28.73s, B04 18.38s, B05 29.59s, B06 29.14s,
B07 13.49s, B08 1.51s). B00 is a real silent mp3 (`ffmpeg anullsrc`, requested 4.05s, measured
4.10s — mp3 frame-boundary rounding, used the real measured value) with `audio_policy: "silence"`
set explicitly per `build_safety.py`'s silent-required-audio gate. Total measured runtime 154.34s
audio.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (Pango/Cairo
small-font-size-artifact workaround), copied from this fellow's closest sibling
(`2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/scenes.py`) for visual consistency.
B02 contrasts the real backend 10-feed cap against Select All's real pre-fix "no cap" code. B03
shows, verbatim, the real pre-fix `handleSelectAll` (no limit), the real backend `max_items=10`
field every selection should respect, and the real pre-fix generic error line — three stacked
panels, since this bug spans two files and two kinds of defect (an unguarded selection path and an
unread validation reason). B04 shows the real diff: `MAX_SELECTABLE_FEEDS = 10` added and both
selection paths capped in `App.jsx`, plus the real detail-extraction block added to
`ChatInterface.jsx`'s catch clause. B05 shows the real 5-check, 7-assertion harness results from
this session's own run, including the real captured 422 message swap (old generic text struck
through in effect by contrast, new real-reason text boxed). B06 shows both honest limits as separate
full-weight cards.

**Timing verification before rendering:** wrote a standalone AST-based checker (parses every
`run_time=`/`self.wait()` literal per `Scene` class and sums it against each beat's measured
`actual_duration_s`, kept in the session scratchpad, not part of this project folder — same checker
pattern this fellow's sibling reels documented building). All 9 landscape scenes AND all 9 vertical
scenes matched their measured durations exactly on the first pass — no arithmetic slip this build.

**GATE A (pre-flight):** all 9 landscape scenes and all 9 vertical scenes individually checked via
`static_scene_check.py --class <Name>` — clean, 0 warn/error on the first pass for every scene, both
aspects.

**GATE B / GATE V (landscape) — real defects found and fixed:**
- First `./art run` pass: GATE B (strict) found 2 real layout warnings, both titles sitting too
  close to the top safe edge on this reel's two tallest-content beats: `B03_TwoBugsOneClick`'s
  title at y=3.45 (half-extent ±3.4) and its closing caption's bottom edge at y=-3.50. Confirmed
  genuine (not false positives) directly from `layout_audit.md`'s own reported bounding boxes.
  Fixed by widening `to_edge()` buffs (title 0.55->0.7, caption 0.5->0.65) rather than shrinking the
  3-panel stack's type/padding that this project's canvas-fill requirement needs to stay large.
  Re-ran `static_scene_check.py --class B03_TwoBugsOneClick` (clean), deleted the stale per-beat
  `.mp4`s, re-rendered.
- Second `./art run` pass (after fixing B03): GATE B found a second, same-shaped real warning on
  `B04_CapAndRealReason`'s title (y=3.50, same top-edge issue — this beat also stacks 2 diff blocks,
  taller than the sibling reel's single-diff B04 that this scene's buff values were copied from).
  Fixed the same way (buff 0.5->0.75). Re-ran `static_scene_check.py --class B04_CapAndRealReason`
  (clean), re-rendered. Third `./art run` pass: GATE B clean on all 9 beats.
- Review-slate GATE V: reported the documented burn-in-timestamp-overlay false positive
  (`frames=18 BLOCKER=18 MAJOR=0`, every frame flagged `edge-bleed`) — not trusted at face value.
  Built the true final master manually (`ffmpeg -f concat -safe 0 -i clips/concat.txt -i
  clips/_work/master.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a
  aac -shortest deliverables/landscape/FeedSelectionCap_SaiPranaviJ.mp4`) and ran
  `final_frame_check.py . --mp4 deliverables/landscape/FeedSelectionCap_SaiPranaviJ.mp4 --lenient`
  from inside the reel folder.
- First true-master GATE V pass: **BLOCKER=0, MAJOR=2** — both `underfill` findings on
  `B05_HarnessTable` (content fills only 38% of the safe area, min 55%). Extracted and visually
  inspected both flagged frames before fixing anything — confirmed a real defect: the block was
  correctly centered but every individual piece (rows, message panel, totals) was sized too
  modestly and too narrow relative to the safe width. Fixed by enlarging every font size and
  widening each panel to `max(content.width + pad, 11.0)`, then added a height-cap guard once the
  enlargement itself pushed the block's top/bottom edges past the safe area on the very next
  render. Re-ran, re-checked: clean.
- Personal verbatim-accuracy re-check (not prompted by any gate): re-read the real `models.py` line
  B03 quotes on screen and found the scene had typed a plausible-looking but not-verbatim
  approximation (`list[int]` instead of the real `List[int]`, an invented `...` instead of the real
  `min_items=1`). The same re-read caught B04's `ChatInterface.jsx` diff silently dropping the real
  `|| JSON.stringify(d)` fallback with no truncation marker. Fixed both to the exact real source
  text (see `FRICTIONAL.md` for the full narrative) — this required re-rendering B03 and B04 a
  second time and rebuilding the true final master a second time.
- Final true-master GATE V re-check (after the B05 underfill fix and both verbatim-accuracy fixes):
  **BLOCKER=0, MAJOR=0**. Landscape master confirmed 3840x2160, 24fps, 154.541667s via `ffprobe`.

**`vertical/scenes.py`:** genuine hand-authored portrait redesign for all 9 beats (rendered at true
2160x3840 / `3840p24` internally), same `T()` helper plus the portrait `config.frame_width` patch
(intended to be copied verbatim from this fellow's sibling reels' documented fix — see the next
entry for how this was initially missed and then corrected). B02's 2-tile row, B03's
code-panel/fields-panel/error-panel stack, and B06's 2-card row each became stacked columns; B05's
row-table became a single compact stacked-rows panel rather than side-by-side tiles, to fit the
same measured beat duration's worth of content inside this frame's narrower safe area.

**`./art vertical`:** scaffolded `vertical/beat_sheet.json`, correctly reusing the hand-authored
`vertical/scenes.py` and the parent's audio (byte-for-byte, via `vertical/mp3/`). The command's own
printed "ONDA CHECK BLOCKED"/"needs native portrait scene916" warnings turned out to be a generic
message `shorts.py` prints for every beat regardless of lane — confirmed harmless by checking the
actual written `vertical/beat_sheet.json` (every beat still `shot.type: GRAPHIC` with the correct
`manim.scene`) before treating it as a real blocker.

**GATE V (vertical, true final master) — a real, severe defect found and fixed across ALL 9
beats:** first true-master GATE V pass: **BLOCKER=0, MAJOR=18** — every single sampled frame across
every beat flagged `underfill` at 5-10% fill (far below the 55% minimum). Extracted and inspected a
real frame (B00's title card) before touching anything: the content was rendering roughly a third
of the real frame width, dead-center, with huge empty margins — the documented signature of a
missing `config.frame_width` portrait patch (manim's CLI derives `frame_width` from the pixel
aspect ratio only once at startup, before the `-r`/`--resolution` flag is applied, so a bare
`-r 2160,3840` render leaves `frame_width` at the 16:9 default even for a portrait render). This
file's own module docstring had already described the sibling reel's fix in prose, but the actual
patch code was never copied in — a real gap between documentation and implementation that no GATE
A/B check catches (GATE A's stub doesn't model frame geometry; GATE B's layout audit measures
positions in Manim's own coordinate space, which was internally self-consistent, just against the
wrong frame width). Fixed by adding the exact patch from the sibling file (copied verbatim) right
after the `manim` import. This required re-rendering all 9 vertical beats from scratch since every
one was affected identically. Re-ran `./art run .../vertical --height 3840`: GATE B clean on all 9
beats (the config patch is also invisible to GATE A/B, so neither flagged the fix either way).
Rebuilt the true final vertical master: **BLOCKER=0, MAJOR=2** — both `underfill` on `B08_BrandOutro`
(53% fill, just under the 55% minimum) — a real, if small and separate, defect, confirmed via frame
extraction (correctly re-timed to the beat's actual 50%/85% sample points, after an initial
personal spot-check at the wrong timestamp caught the Create/FadeIn animation mid-flight and was
discarded as not a real finding). Fixed by enlarging type and spacing. Final true-master GATE V
re-check: **BLOCKER=0, MAJOR=0**. Vertical master confirmed 2160x3840, 24fps, 154.541667s via
`ffprobe` — identical duration to the landscape master (every beat kept, nothing dropped, via
`./art vertical` — no cap, no rewritten outro, no added endcard).

Both final masters were personally re-inspected frame-by-frame (B00's title card, B02's cap-vs-no-
cap tiles, B03's three stacked panels with the real verbatim code, B04's real diff for both files,
B05's re-centered/enlarged harness table with the real message swap, B06's honest-limit cards,
B07's takeaway, and B08's sign-off) directly from the shipped deliverables, in both aspects, before
considering this project done — no text-rendering artifacts, no clipping, no overlap; "Sai Pranavi
J." (never the full surname) and "@HumanitariansAI" confirmed correct everywhere they appear.

**Deliverables:**
- `deliverables/landscape/FeedSelectionCap_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `e1ac65ebcd30895c9f27e536b1c04ebaed76ef8a06b8ad0d2fd9c486c6f9533e`)
- `deliverables/vertical/FeedSelectionCap_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `286c9e636cff0450ac8bcafd9c45a43ea00be587e752a7b8c8f4a0124e425736`)

## Summary — final gate results

| Aspect | Resolution | Duration | GATE V (true final master) |
|---|---|---|---|
| Landscape | 3840x2160 @ 24fps | 154.541667s | 0 BLOCKER, 0 MAJOR |
| Vertical | 2160x3840 @ 24fps | 154.541667s | 0 BLOCKER, 0 MAJOR |

No persistent/unavoidable MAJOR findings remain on either true final master — both are fully
clean. Real defects found and fixed this build: landscape B05 underfill, two verbatim-accuracy
errors (B03's quoted backend field, B04's quoted error-handling diff) caught by a personal re-read
rather than any automated gate, a missing portrait `config.frame_width` patch that affected all 9
vertical beats, and a small B08 vertical underfill — all confirmed genuine via extracted-frame
inspection, full narrative in `FRICTIONAL.md`.

Publishing not authorized. Nothing inside `brutalist/` was modified; nothing inside
`/Users/pranavijs/mycroft` was modified (confirmed via `git status --short` before and after this
session — only pre-existing, unrelated changes from before this session were present both times).
