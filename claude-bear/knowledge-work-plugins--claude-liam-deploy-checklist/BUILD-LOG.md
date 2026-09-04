# BUILD-LOG — knowledge-work-plugins--claude-liam-deploy-checklist

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-deploy-checklist/beat_sheet.json`,
7 beats, teardown of Anthropic's `deploy-checklist` skill, brand
`claude-liam`, all-Remotion: `ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`).
Read the source sheet in full (no source `SKILL.md` file exists on this
machine — the source's `metadata.source_skill` path points at
`/Users/bear/...`, unreachable here — so every fact was taken from the
source beat_sheet's own narration_text, which already states the skill's
full description verbatim). Kept the question and every fact:
`deploy-checklist` is a skill (a folder Claude reads before it acts,
containing one file, `SKILL.md`); it triggers on "about to ship a release,
deploying a change with database migrations or feature flags, verifying CI
status and approvals before going to production, or documenting rollback
triggers ahead of time"; it runs fixed linear steps (read, execute each
step, return output); the source's own design-tell/verdict beats already
named the "repeatable results" / "only what the file says" shape this reel
reframes as both-directions.

Expanded the source's compressed 7-beat teardown into the full 16-beat
hai-simple spine (stakes / wrong guess+break-it / mechanism / anchor
planted+payoff / both directions / carry-out / your-turn / outro), matching
this same family's prior `knowledge-work-plugins--claude-liam-code-review`
build: reused `SkillTeardownMechanism`/`SkillTeardownAnatomy`/
`SkillTeardownPipeline` (already-Remotion source patterns, re-registered
Teardown → Plain, judgment language removed) plus `GitHubCodeDiff` for a
new anchor (a live database migration, invented to serve the anchor beat —
not present in the source, which had no anchor device) and
`Opus5ChecklistCard` for the three named check items. No source beat was
AI-video, pantry, or human-drop — the source was already Remotion end to
end, so every beat carried over as Remotion with no NO-GENAI/NO-PANTRY
substitution needed. B00 replaced with `BrutalistHesitantWriter`
(WRITER LAW); outro replaced with `OutroSeries`/`OutroCTA` (Humanitarians
AI skin, Liam `am_onyx`).

Wrote `SCRIPT.md` and `beat_sheet.json` fresh this invocation (no prior
partial artifacts existed — directory held only `SUBJECT.json`).

1. **Audio (generate_audio_kokoro.py):** 16/16 beats generated, `am_onyx`,
   $0.00. B00's first pass measured 8.83s from a 30-word narration — under
   the TIMING LAW's effective floor. Lengthened the narration to 34 words
   and regenerated B00 alone: 9.92s.
2. **GATE T (type_check.py): PASS**, 0 FAILs on first run (5 `body` props
   kept ≤8 words each from the start, learning from this family's
   code-review build's GATE T failure). One advisory-only §8.10 redundancy
   flag on S06 (narration recites the checklist card) — non-blocking, same
   shape as the source's own checklist beat.
3. Rendered all 16 Remotion beats via `remotion_scenes.py` in the
   foreground. Exceeded the tool's 120s timeout and was moved to background
   by the harness twice; per this skill's ONE-SHOT warning, blocked on both
   with `TaskOutput` (not fire-and-forget) until each returned exit 0.
   First pass: 15/16 ok, S04 (`SkillTeardownAnatomy`) FAILed on a Remotion
   package-version mismatch (`@remotion/*` packages resolving to mixed
   versions in node_modules) — re-ran `--only S04 --force` alone and it
   rendered clean on retry (transient resolution issue, not a props defect).
4. **Gate V catch — B00 correction never landed:** first `compile.py` pass
   produced a technically-passing master (all gates green), but reading
   frames near the end of B00 (9.3s / 9.6s / 9.8s / 9.9s) showed the
   trigger word "judgment" fully typed and held in accent color, never
   deleted/replaced with "checklist" — the correction was cut off, not
   missing. Root cause, traced through
   `runtime/scripts/remotion_scenes.py`'s `extend_clip_to_duration`: it uses
   `ffmpeg -t <duration_s>`, which *truncates* a Remotion render longer than
   the beat's audio duration (it only pads via `tpad` when the render is
   *shorter*). `BrutalistHesitantWriter`'s fixed 606-frame (20.2s)
   composition, with my original text placing the trigger word
   ("judgment") in the *last* line, meant the correction's char-by-char
   delete/retype cycle fell right at ~9.9s — past the 9.92s audio-driven
   cutoff, so it got truncated mid-correction. This is exactly the pilot
   failure the skill's TIMING LAW names, just reached by a different path
   (trigger-word position, not narration length). Fixed by moving the
   trigger word earlier in the on-screen text (line 1 of 4, ~31% through
   the token sequence, matching the code-review sibling's proportion)
   instead of lengthening narration further. Re-rendered B00 alone,
   re-checked frames at t=7s in both the raw beat clip and the final
   compiled master: "judgment" → "checklist" completes cleanly by ~7s,
   comfortably inside the 9.9s window, leaving 3s to type the remaining
   question. Recompiled (fast — only B00's clip changed).
5. `compile.py` — 16/16 slots filled (all VIDEO), content-check/frame-check/
   lane-check all PASS, GATE AUDIO PASS mean_volume -23.9 dB. THE 4K LAW
   forced the clean master natively to 3840x2160.
6. Independently reverified rather than trusting compile.py's own report:
   `ffprobe` — 3840x2160, 118.70s, h264+aac; master mtime (14:12:05) newer
   than beat_sheet.json mtime (14:10:40); `ffmpeg -af volumedetect` —
   mean_volume **-23.9 dB**, max -3.0 dB, confirming GATE AUDIO well above
   the -40 dB floor.
7. Gate V (full pass, on the corrected master): pulled frames across the
   full 118.7s runtime and read all of them — B00's writer-open correction
   confirmed landing at t=7s inside the 9.9s window; the wrong-guess/
   break-it pair (S02/S03); the SKILL.md anatomy card (S04); the anchor
   plant and payoff (S05/S09 — identical `GitHubCodeDiff` migration,
   caption changed from "hold on to this" to "flagged, same file, same
   day"); the checklist-items card (S06); the trigger-cue card (S07); the
   pipeline card (S08); the both-directions pair (S10/S11); the carry-out
   quote (BCRY); the Your Turn composer card (BHTF); both outro cards
   (BOUT1/BOUT2) with the Humanitarians AI skin. All legible, safe inset
   respected, no text overlap. One defect found and fixed (B00, above); no
   further defects on the recheck.

**Gates:**
- content-check: PASS (16 beats, no violations)
- frame-check: PASS (3840x2160, 16 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 118.70s, 3840x2160; mp4 mtime newer than beat_sheet.json mtime
- Gate V: PASS after one fix (B00 correction timing — see step 4)

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
`knowledge-work-plugins--claude-liam-deploy-checklist.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
family `knowledge-work-plugins` matches the map's `knowledge-work-plugins`
prefix directly — plus the direct code link per the DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
