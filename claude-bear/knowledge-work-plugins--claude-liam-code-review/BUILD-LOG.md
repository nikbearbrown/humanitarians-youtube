# BUILD-LOG — knowledge-work-plugins--claude-liam-code-review

## 2026-09-02/03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-code-review/beat_sheet.json`,
16 beats, teardown of Anthropic's `code-review` skill, brand `claude-liam`).
Read the source sheet in full. Kept the question, beat count, and every
fact: `code-review` is a skill (a folder Claude reads before it acts,
containing one file, `SKILL.md`); it names exactly three check categories
(security, performance, correctness) and its own trigger (a PR link, a
diff, or "review this before I merge"); it runs fixed linear steps (read
diff, check each category, return findings); the anchor is an N+1 loop
(`orders/repository.py`, `db.query` inside a `for` loop) planted at S05 and
paid off identically at S09 (same `GitHubCodeDiff` beat, same file, same
diff, caption changed from "hold on to this" to "flagged"). Re-registered
narration from Teardown to Plain (facts unchanged, no design verdict) and
carried the Humanitarians AI skin (Liam `am_onyx`, `OutroSeries`/`OutroCTA`).
No source beat was AI-video, pantry, or human-drop — the source was already
Remotion end to end, so every beat carried over as Remotion with no
NO-GENAI/NO-PANTRY substitution needed.

Picked up a prior session's near-complete artifacts on this invocation
(SCRIPT.md, beat_sheet.json, Kokoro audio for all 16 beats already measured
into `actual_duration_s`, B00 already rendered) and continued rather than
rebuilding, per COMPLETION LAW.

1. **GATE T (type_check.py), first pass: FAIL** — 5 `no-wordy-card §8.5`
   violations (S01, S02, S03, S07, S11 `body` props over the 12-word
   pull-quote limit at 19/17/19/13/21 words). Fixed by shortening each
   `body` string to a label-length line (narration_text left untouched —
   only the on-screen card text changed). Re-ran: **GATE T: PASS**, 0 FAILs.
2. Rendered the 15 remaining Remotion beats via `remotion_scenes.py` in the
   foreground (B00 was already filled, skipped). Exceeded the tool's 600s
   timeout mid-run and was moved to background by the harness; per this
   skill's ONE-SHOT warning, blocked on it with `TaskOutput` (not a
   fire-and-forget) until it returned exit 0 rather than ending the turn —
   confirmed via polling that the render kept advancing (13/16 media files
   present partway through) before it completed clean: all 15 beats `ok`,
   no failures.
3. `compile.py` — 16/16 slots filled (all VIDEO), content-check/frame-check/
   lane-check all PASS, GATE AUDIO PASS mean_volume -23.9 dB. THE 4K LAW
   forced the clean master natively to 3840x2160 (no `--review` flag used).
4. Independently reverified rather than trusting compile.py's own report:
   `ffprobe` — 3840x2160, 109.04s, h264+aac; master mtime (00:25:19) newer
   than beat_sheet.json mtime (00:23:28); `ffmpeg -af volumedetect` —
   mean_volume **-23.9 dB**, max -3.1 dB, independently confirming GATE
   AUDIO well above the -40 dB floor.
5. Gate V: pulled 10 frames at 6s spacing across the 109s runtime and read
   all of them directly — B00's writer-open correction ("everything" ->
   "some things", the naive framing visibly struck and replaced by t=6s,
   well inside the beat's 9.94s window), the wrong-guess/break-it pair
   (S02/S03), the SKILL.md anatomy card (S04), the anchor plant and payoff
   (S05/S09 — identical `GitHubCodeDiff` treatment, caption changed from
   "hold on to this" to "flagged, same loop, same day"), the trigger-cue
   card (S07), the both-directions pair (S10/S11), the carry-out quote
   (BCRY), the Your Turn composer card (BHTF), and the outro title card
   (BOUT1) with the Humanitarians AI skin. All legible, safe inset
   respected, no text overlap. No defects found — no fixes needed this
   pass.

**Gates:**
- content-check: PASS (16 beats, no violations)
- frame-check: PASS (3840x2160, 16 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after de-wordifying 5 body props)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.1 dB
- ffprobe: duration 109.04s, 3840x2160; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warnings (compile.py, both expected for this skill):**
- SKIN LINT flagged B00 (`BrutalistHesitantWriter` vs ai-explainer's
  `ClaudeComposerAsk`) and BOUT2 (`OutroCTA` vs `ClaudeTitleOutro`) as
  palette mismatches. Both are the hai-simple skill's deliberate
  COLD OPEN LAW / OUTRO LAW overrides, not defects.
- Motion histogram: remotion 16/16 (100%), over the generic ~40% pantry
  cap. Structural, not a defect: this redo's source was already all-Remotion
  and NO-GENAI/NO-PANTRY LAW requires every beat be Remotion or Graphic —
  there was no pantry/Manim material to substitute in without inventing
  content not in the source.

Metadata file written:
`knowledge-work-plugins--claude-liam-code-review.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
family `knowledge-work-plugins` matches the map's `knowledge-work-plugins`
prefix directly — plus the direct code link per the DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-03 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects, then packaged
to both delivery targets.
