# BUILD-LOG — knowledge-work-plugins--claude-liam-contract-review

## 2026-09-03 — hai-simple redo, DELIVERED

**Mode:** redo. Source: `anthropics/knowledge-work-plugins/youtube/claude-liam-contract-review/beat_sheet.json`
(Teardown skill-teardown format, examining a contract-review skill's anatomy).
Source's own `beats[*].narration_text` for B00/B03/BVDT/BHTF carried unfilled
`>` placeholder markers (the worked example — which contract, which clause —
was never written in; `PEDAGOGY.md` records only `VERDICT: PASS / Batch
build`, and the source SKILL.md path is not present on this machine). The
source's non-placeholder argument stayed intact and locked: a skill is a
folder Claude reads before acting; the pipeline is read → execute steps in
order → return result, linear; the design trade is a fixed checklist bought
for repeatable results, at the cost of anything outside the spec. This redo
keeps that argument word-for-word in substance and supplies one concrete,
generic, true worked example (a freelance contract's termination clause) to
fill the placeholder gap, per hai-simple PHASE 1's "when in doubt, describe
behavior generically." Logged in `QUESTION.md`.

**Picked up mid-build.** On invocation, the reel already had `beat_sheet.json`
(13 beats), `SCRIPT.md`, `CARRY-OUT.md`, `QUESTION.md`, `scenes.py`,
`render_scenes.py` written, audio fully generated (`mp3/*.mp3` +
`timings.json`, `actual_duration_s` written back for all 13 beats), all 9
Manim GRAPHIC beats rendered (`manim/NB01-09.mp4`), and 2 of 4 Remotion beats
already rendered (`media/B00.mp4`, `media/BCRY.mp4`). No `BUILD-LOG.md` yet —
this entry is the first. Verified the existing artifacts rather than
rebuilding: `ffprobe` confirmed B00.mp4 carries video+audio, 10.5s (clears
the ≥9s WRITER LAW/TIMING LAW floor).

**Beat shape (13 beats, matches the `claude-liam-simple-*` series lineage):**
B00 writer (`BrutalistHesitantWriter`, "lawyer"→"checklist") + NB01-NB09
GRAPHIC body (chip-row Manim template, generic and reused across all 9: 1
stakes, 2 wrong guess, 3 mechanism ×3, 2/3 checklist-not-judgment, 4 anchor
planted [NB06: freelance contract → termination clause → flagged], 3
mechanism-the-limit, 4 anchor payoff [NB08: same contract, same flag, not a
verdict] / 5 direction A, 5 direction B) + BCRY carry-out (`WantQuote`) +
BHTF your-turn handoff (`ClaudeComposerAsk`) + BOUT outro (`OutroCTA`, HAI
skin). All 13 beats REMOTION or GRAPHIC — no `ai-video-prompt`, no pantry,
no human-drop slot anywhere (NO-GENAI/NO-PANTRY LAW clean by construction;
nothing needed swapping).

**Completed this invocation:**
- Rendered the 2 remaining Remotion beats (`BHTF`, `BOUT`) via
  `remotion_scenes.py` — first invocation exceeded the tool's 120s timeout
  and was moved to background by the harness; blocked on it via
  `TaskOutput(block=true)` before proceeding, per the one-shot COMPLETION
  LAW's foreground-render rule. Exit 0, both beats `ok`.
- Compiled via `compile.py`: 13/13 slots filled (no slate), native 4K
  (3840×2160, compile.py's 4K LAW forces this for any non-`--review`
  compile), GATE AUDIO PASS (mean_volume −23.9 dB, max −2.9 dB).
- **GATE T FAILED on first pass**: `NB02` bbox-overlap §8.6b — the bold,
  accented third chip "LAWYER'S CALL" rendered with its two words'
  bounding boxes overlapping 11% (visually, "LAWYER'S" and "CALL" crowded
  into what read as one merged word). Tried renaming to "LAWYER DECIDES"
  (still two words) — same crowding recurred on the new word pair,
  confirming this is a bold-weight + multi-word EB Garamond spacing defect
  in this Manim/font environment, not specific to the apostrophe. Fixed by
  switching to a single word, "JUDGMENT" — matches the established safe
  pattern (every other bold accented chip in this sheet, e.g. "FLAGGED",
  "REPEATABLE", is single-word and passed clean) and strengthens the later
  payoff, since NB05 already contrasts "CHECKLIST, NOT JUDGMENT,
  REPEATABLE." Re-rendered NB02 only, recompiled, re-ran `type_check.py`:
  **GATE T PASS, 0 FAILs.**
- Gate V: pulled 13 frames across the full 105.0s runtime (one per beat,
  plus a late B00 pull at t=9.5s). All legible, safe inset, single accent
  moment per beat, no overlap, correct `@HumanitariansAI` folder label on
  BHTF/BOUT, humanitarians palette throughout. B00's correction ("lawyer"
  struck, "checklist" landed) fully resolved and holding by the sampled
  frame. Anchor pair (NB06→NB08) visually consistent: "FREELANCE CONTRACT"
  chip returns identically.
- Re-verified independently: `ffprobe` 3840×2160, one video + one audio
  stream, 105.017667s; `ffmpeg volumedetect` mean_volume −23.9 dB, max
  −2.9 dB (well above the −40 dB audibility floor); mp4 mtime newer than
  `beat_sheet.json`.
- Master born natively 3840×2160 via `compile.py`'s 4K LAW — no separate
  4K re-render needed. Copied to `knowledge-work-plugins--claude-liam-contract-review-4k.mp4`
  (deliver.py's preferred filename) rather than re-rendering, since the
  content is already true 4K.
- Wrote `knowledge-work-plugins--claude-liam-contract-review.md` (YouTube
  metadata): playlist resolved from `playlists.json` — family
  `knowledge-work-plugins` matches the map directly (no `_default`
  fallback needed) → **"Extending Claude — Skills, Plugins & Connectors"**
  (already stamped in `beat_sheet.json.metadata.playlist` from the prior
  invocation; confirmed correct against the current map). Description
  carries the direct code link and a "Deliberately not claimed" section
  documenting the source placeholder gap (same disclosure pattern as the
  `claude-for-legal--claude-liam-nda-review` sibling).
- Ran `deliver.py --push`: staged `DELIVERY/knowledge-work-plugins--claude-liam-contract-review/`
  (4K master + description) and committed+pushed
  `claude-bear/knowledge-work-plugins--claude-liam-contract-review/` to
  humanitarians-youtube.

**Status: DONE.** `knowledge-work-plugins--claude-liam-contract-review.mp4`
exists, is newer than `beat_sheet.json`, is 3840×2160, carries audible audio
(−23.9 dB mean), passes GATE T (0 FAILs) and Gate V (0 blockers on frame
sweep). 4K deliverable produced and both delivery targets packaged.
