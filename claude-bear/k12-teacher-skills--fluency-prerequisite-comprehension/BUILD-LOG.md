# BUILD-LOG.md — k12-teacher-skills--fluency-prerequisite-comprehension

## 2026-09-02 — Phase 0-3, review cut

Redo-mode reel (SUBJECT.json `mode: "redo"`), source
`anthropics/k12-teacher-skills/youtube/fluency-prerequisite-comprehension`
(8 beats: B00 ClaudeComposerAsk cold open + B01/B02/B02a/B02b body +
B03 verdict + B04 handoff + B05 outro). Read the source beat_sheet.json and
its SOURCES.md completely before writing. Built fresh from scratch (target
dir held only SUBJECT.json): QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (8 beats, same shape as source: B00 hesitant-writer +
NB01-NB04 body + BCRY + BHTF + BOUT), scenes.py/render_scenes.py (the
generic Manim "chip row" template, copied verbatim from the
`k12-teacher-skills--cra-progression-scaffold` sibling built earlier the
same day, itself copied from `k12-lesson-differentiation`).

**Body mapping (1:1 with source, per redo's beat-count law):**
NB01=B01 (the conserved working-memory bar, low-fluency 78/22 vs
high-fluency 12/88 split — THE ANCHOR, ONE FLAG on the illustrative
percentages), NB02=B02 (immediate bridge vs real fluency intervention),
NB03=B02a (five-role AI-substitution ledger, compressed to the
listener-vs-reader BOTH-DIRECTIONS pair), NB04=B02b (the cold-read check —
ANCHOR PAYOFF, ties back to "the split" from NB01). B03's two verdict facts
folded into the single BCRY carry-out sentence per CARRY-OUT LAW; B04's
bracketed handoff prompt kept nearly verbatim (already paste-ready). Source
was already all-Remotion (no ai-video-prompt/pantry beats to replace beyond
B00, which hai-simple replaces by mandate anyway); source's
`K12Fig04WorkingMemory`/`K12Fig11SubLedger`/`K12Fig12ColdReadTest` have no
ink/accent/bg props and can't move to the humanitarians palette, so NB01-
NB04 are built fresh as GRAPHIC (Manim) on the same channel-skin precedent
as both `k12-teacher-skills` siblings built this week.

**B00 GATE V FINDING — TIMING LAW failure on first render, caught by frame
pulls, fixed by shortening text (not narration):** First B00 text ("I've
scaffolded everything I can think of, and they still can't comprehend. Need
another scaffold?", 101 chars) never reached the trigger word within the
beat's 9.88s duration — confirmed by pulling frames every 0.5s across the
full clip; the last frame was still mid-sentence at "comprehend." with the
correction never having started. Root cause: `lead_silence_s` is authored
per WRITER LAW convention (as the `cra-progression-scaffold` sibling also
does) but grepping compile.py confirms it is NOT wired in there at all —
only `tail_silence_s` is handled. The real on-screen typing budget is
exactly `actual_duration_s` (narration length alone), not
narration-plus-lead-silence, which the SKILL.md's "≥9s window" language
does not make obvious. Two iterations to fix: shortened first to a 59-char
text (still ran out — reached only "another flue" by the last frame) then
to "Nothing's helped.\nNeed another scaffold?" (41 chars, 2 lines instead of
4, matching the working `cra-progression-scaffold` sibling's char/line
budget). Re-rendered B00 alone (`--only B00 --force`) after each edit;
final frame-pull sequence (0.25s spacing) confirms the trigger word
("scaffold", in terracotta) appears by ~5.25s and the full correction
("Need another fluency check?") settles by ~7.25s, comfortably inside the
9.9s beat with margin — matching the sibling's confirmed-working pattern.
Both `remotion_scenes.py` invocations exceeded the tool's 120s foreground
timeout and were auto-backgrounded; blocked on each via TaskOutput to real
completion (exit 0) before proceeding, per the ONE-SHOT/COMPLETION LAW —
never treated an auto-backgrounded render as done without checking its
actual exit.

**Audio:** all 8 beats generated in one pass (`generate_audio_kokoro.py`,
`am_onyx`); B00 measured 9.88s (clears the ≥8s floor after the text fix).

**Manim (NB01-NB04):** rendered clean on first pass via `render_scenes.py`.

**GATE T (type_check.py): PASS, 0 FAILs, first pass** — no defects to fix
(unlike the same-day `cra-progression-scaffold` sibling, which needed three
chip-label/eyebrow-separator fixes; this reel's chip labels and the BOUT
eyebrow's " — " em-dash separator were written correctly from the start,
copying the sibling's already-fixed conventions rather than its originals).

**Compile:** `compile.py` -> exceeded 120s foreground timeout, auto-
backgrounded, blocked to completion (exit 0) ->
`k12-teacher-skills--fluency-prerequisite-comprehension.mp4`, 139.0s, native
3840x2160 (every beat source was already 4K/1080p-native; no upscale
needed). `content-check`/`frame-check`/`lane-check` all PASS, 8/8 beats
filled. One advisory (non-blocking) WARNING: Remotion carries 4/8 beats
(50%), over the ~40% pantry-cap guideline — structural, not a defect: this
skill's 4 fixed bookend beats (B00 writer, BCRY, BHTF, BOUT) plus this
source's 4-body-beat shape puts every 8-beat hai-simple redo of this family
at exactly 50%.

**Gate V (visual):** pulled frames every 6s across the full 139s runtime
(23 frames) plus targeted pulls at B00's correction point and BOUT's last
3s, and read every one. B00's correction ("scaffold" -> "fluency check")
lands well before the beat ends (see GATE V FINDING above). NB01-NB04 chip
rows read clean and parallel-sized, one terracotta accent/strike moment
each, no overlap. BCRY/BHTF/BOUT (Remotion) show the correct carry-out
quote, the full paste-ready bracketed prompt with `@HumanitariansAI`
explicit, and the outro title/eyebrow with no truncation. No blockers.

**Audio presence:** `ffmpeg -af volumedetect` on the master -> mean_volume
-24.1 dB, max_volume -2.8 dB (well above the -40 dB floor).

Metadata file written: `k12-teacher-skills--fluency-prerequisite-
comprehension.md` (channel @HumanitariansAI, **Playlist: Claude Basics**).
Per `playlists.json`, SUBJECT.json's family (`k12-teacher-skills`) matches
no map prefix; falls through to the `hai-simple` skill-key match (->
"Claude Basics"), consistent with both `k12-teacher-skills` siblings built
this week. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, delivery

Master was already born native 3840x2160 (compile.py's 4K LAW), so
`k12-teacher-skills--fluency-prerequisite-comprehension-4k.mp4` was copied
directly from the review master with no re-render needed (same as the
`cra-progression-scaffold` sibling). Ran
`deliver.py <reel_dir> --push`: staged `DELIVERY/k12-teacher-skills--
fluency-prerequisite-comprehension/` (4K mp4 + description) for the Drive
sync, and copied text artifacts (README.md=description, beat_sheet.json,
SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md) into
`humanitarians-youtube/claude-bear/k12-teacher-skills--fluency-prerequisite-
comprehension/`, committed, and pushed (no mp3/mp4 entered the repo copy).

**Status: DELIVERED.**
