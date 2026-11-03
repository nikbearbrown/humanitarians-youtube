# Frictional log — The Correction That Never Reached The Email

Written contemporaneously during this build, not reconstructed afterward. Entries are dated to
when they actually happened (same session, 2026-10-27).

## 2026-10-27 — Building the live verification harness

- The real bug and fix are in `jsCode` inside an n8n workflow JSON
  (`scripts/regulatory-intel/workflow.dev.json`), not a Python/FastAPI endpoint like this fellow's
  2026-10-20 report — so the harness needed to be Node.js, not Python. Wrote
  `verification/verify_effective_severity.mjs`: reads the real file with `fs.readFileSync` (no
  write, confirmed read-only), extracts the real `Generate Email` node's `jsCode` directly from the
  parsed JSON, and runs it inside a sandboxed `node:vm` context with `$("High Priority Filter")`
  shimmed to return a synthetic 3-item batch.
- Decided NOT to hand-retype a "pre-fix" reconstruction from memory (risk of silently drifting from
  the real diff). Instead, built it by string-substituting the real post-fix block back to the
  original two-line form, and added a hard check — `occurrences !== 1` throws — so the harness
  refuses to run at all if the real file's current code doesn't match the expected post-fix shape
  exactly once. This also doubles as a canary: if the fix is ever reverted or refactored, this
  harness fails loudly instead of silently reporting stale results.
- First run succeeded on the first try (no `DATABASE_URL`/settings import chain to fight, unlike
  the 2026-10-20 report's FastAPI harness — a plain Node `vm.Script` over an extracted code string
  has no framework-level import side effects to work around).
- Cross-checked this session's own harness output
  (`critical_count: 2, high_count: 1` pre-fix; `critical_count: 1, high_count: 2` post-fix) against
  `C3-VERIFICATION.md`'s independently-reported table from earlier the same day — both match
  exactly, corroborating both this session's harness and the original investigation.
- Confirmed via `git -C /Users/pranavijs/mycroft status --short` before and after writing/running
  the harness: only pre-existing, unrelated `package-lock.json` changes present both times — this
  session made no changes to the `mycroft` repo.

## 2026-10-27 — Audio-first build (Kokoro)

- `generate_audio_kokoro.py` ran clean on the first attempt (voice model already present from this
  fellow's prior episode's setup) — no repeat of the missing-`kokoro-v1.0.onnx` gap documented in
  the 2026-10-20 report's `FRICTIONAL.md`.
- B00's silent track: `ffmpeg -f lavfi -i anullsrc ... -t 4.05` actually measured 4.104s on
  `ffprobe` (mp3 frame-boundary rounding, same category of effect documented in sibling reels), not
  exactly 4.05 — used the real measured value (4.10, rounded) as B00's `actual_duration_s`/timing
  target rather than the requested target, per the audio-first rule (measure, don't assume).

## 2026-10-27 — Authoring scenes.py (landscape)

- Wrote a standalone timing checker (parses every `run_time=`/`self.wait()` literal per `Scene`
  class via regex and sums it against `beat_sheet.json`'s `actual_duration_s`, kept in the session
  scratchpad, not part of this project folder) BEFORE rendering anything, modeled directly on the
  2026-10-20 report's documented timing-slip catch. First pass on all 9 scenes already matched
  every beat's measured duration to the millisecond — no arithmetic slip this time, but ran the
  checker anyway rather than trusting hand-summed inline comments, per that sibling report's own
  documented lesson.
- `static_scene_check.py --class B04_EffectiveImpactDiff` failed on the first pass:
  `AttributeError: property 'width' of 'Line' object has no setter` — the original B04 draft built
  each strike-through `Line` BEFORE the whole-diff-block `fit()` call, then tried to rescale each
  `Line`'s `.width` directly afterward to match its (now-scaled) parent text line. Manim's `Line`
  exposes `.width` as a read-only property computed from its endpoints — there is no setter. Fixed
  by grouping each strike `Line` together with its corresponding minus-text line into a shared
  `VGroup` BEFORE the block-level `fit()` call, so the strike scales and repositions automatically
  as part of the group (not as a manual post-hoc adjustment) — confirmed clean on the next
  `static_scene_check.py` pass.
- B04's real diff contains one genuinely long real source line (the `effectiveImpact()` ternary's
  condition, ~100 characters as it's actually formatted in `workflow.dev.json`). Rather than risk
  misquoting it by hand-wrapping mid-expression, used the file's real existing line breaks (the
  real source is already multi-line) and `fit()`-scaled the whole diff block as one unit to this
  reel's width budget, keeping every line's relative size consistent — documented in
  `scenes.py`'s own module docstring and `SHOTLIST.md`.

## 2026-10-27 — Manim render / compile (landscape)

- `./art run` (landscape, `--height 2160`): GATE A clean on all 9 scenes going in. GATE B
  (`manim_layout_audit.py`, post-render pixel audit) flagged one real warning on the first pass:
  `B05_HarnessTable`'s scenario label (`item-1\nconfirmed, recategorized`) landed with its real
  left edge at x=-6.35, just outside the documented +/-6.3 safe-area half-width — genuine overflow
  from the 3-row-card group (3 cards @4.3 width + 2 gaps @0.35 = 13.6, against a 12.6-wide safe
  area), not a false positive. `ART_STRICT=1` correctly refused to slot the clip. Fixed by
  `fit()`-scaling the whole `rows` VGroup to a 12.2 width budget as one block before positioning
  (same pattern already used for B04's diff), deleted the stale
  `media/videos/scenes/2160p24/B05_HarnessTable.mp4` and its `partial_movie_files` cache per this
  toolkit's documented stale-cache gotcha, and re-ran — clean on the next pass.
- Full `./art run` pass (all 9 beats compiled, review slate built): `[gate-v] frames=18 BLOCKER=18
  MAJOR=0` — every sampled frame, including the simplest title card (B00), flagged identically as
  `edge-bleed`. Did not take this at face value — extracted a real frame directly from the review
  slate (B00 at t=2s) and visually confirmed the real scene content (title + border frame) sits
  comfortably inside its own bordered frame; the actual top-right corner holds only the slate's own
  burned-in `00:00:02.000` timestamp overlay, which `final_frame_check.py`'s `BURN_IN_EXCLUDE` mask
  doesn't cover. Same review-slate false positive this fellow's sibling reels already documented.
  Built the true final master manually (`ffmpeg -f concat -safe 0 -i clips/concat.txt -i
  clips/_work/master.wav -map 0:v -map 1:a -c:v libx264 -preset fast -crf 16 -pix_fmt yuv420p -c:a
  aac -shortest`) and ran `final_frame_check.py . --mp4
  deliverables/landscape/EffectiveSeverity_SaiPranaviJ.mp4 --lenient` from inside the reel folder:
  **BLOCKER=0, MAJOR=0** — clean on the first true-master pass, no further fixes needed for
  landscape.

## 2026-10-27 — Manim render / compile (vertical)

- `./art vertical` scaffolded `vertical/beat_sheet.json`, correctly picking up the hand-authored
  `vertical/scenes.py` already written (same scene class names as the landscape parent) — no
  Remotion re-render step needed, since every beat here is a Manim GRAPHIC beat, not a
  `shot.remotion.pattern` one.
- First `./art run vertical --height 3840` pass: GATE B failed outright (not just a warning) on
  `B03_FieldWrittenFieldIgnored` — one real ERROR (`text-on-text (overlap 14%)`: the closing
  caption crossing the code panel's own last line) and 2 real WARNings (title's real top edge at
  y=3.5 against the +/-3.4 safe half-height; caption's real bottom edge at y=-3.5). All three traced
  to the same root cause: the fields/code panel stack was never height-capped, so on this
  particular beat's real content it grew tall enough to push the independently-positioned closing
  caption off the bottom safe edge and into the code panel itself. Fixed by (1) bumping this file's
  title buff from 0.5 to 0.68 — the same portrait safe-area floor for any 2-line
  `title.to_edge(UP)` already documented in this fellow's sibling reels' vertical builds — (2)
  capping the panel stack's height (`scale_to_fit_height(3.5)`), and (3) switching the caption from
  an independent `to_edge(DOWN)` to `next_to(panels, DOWN, buff=0.35)`, which structurally
  guarantees no overlap regardless of the stack's exact rendered size, rather than two
  independently-placed blocks that can collide. Preemptively applied the same buff=0.68 fix to
  `B04`'s title/caption and `B05`'s/`B06`'s titles in the same edit pass (all were still at the old
  0.45/0.5 default), rather than re-discovering the identical systemic issue beat by beat across
  separate render cycles.
- Re-ran `./art run vertical`: GATE B clean, all 9 beats slotted. Review-slate GATE V again
  reported the same known burn-in false positive (`BLOCKER=18 MAJOR=0`). Built the true final
  vertical master manually and ran `final_frame_check.py vertical --mp4
  deliverables/vertical/EffectiveSeverity_SaiPranaviJ.mp4 --lenient`: **BLOCKER=0, MAJOR=6** — real
  `underfill` findings this time, not false positives: `B02_IgnoredCorrectionHook` (51% of the safe
  area, min 55%), `B03_FieldWrittenFieldIgnored` (50% — ironically, the same beat just fixed for
  overlap, now too conservatively capped), `B08_BrandOutro` (45%). Fixed by widening internal
  buffs/padding and enlarging type in all three scenes (B02's tile heading/value buffs and panel
  padding, B03's panel-stack height cap raised from 3.5 to 4.3 — confirmed there was still clear
  room below it for the caption via the `next_to()` positioning from the previous fix — B08's
  handle/line/tagline font sizes and top-level arrange buff from 0.45 to 0.85), per this project's
  canvas-fill requirement, rather than padding with an invisible spacer. Re-ran `./art run
  vertical`: GATE B clean (0 errors, 0 warnings). Rebuilt the true final vertical master and
  re-ran `final_frame_check.py vertical --lenient`: **BLOCKER=0, MAJOR=0.** Both true final masters
  are now clean. Wrote `.verified.json` sidecars (SHA-256 + duration + GATE V result) next to both
  deliverables, then personally extracted and visually inspected spot-check frames from both
  shipped MP4s (not the slate, not an intermediate render) — B02's LLM-correction/email-shows
  tiles, B03's fields/code panels with the `impact_level` boxes, B05's harness table with the
  gold-boxed recategorized row, B07's takeaway, and B08's sign-off (correct "@HumanitariansAI" and
  "Sai Pranavi J." attribution) in the vertical master — before considering this project done. No
  further defects found.

## Closing note

Every entry above is real and dated to when it happened during this single build session
(2026-10-27: research/verification, audio generation, scene authoring, render/compile for both
aspects). Nothing here was back-filled after the fact.
