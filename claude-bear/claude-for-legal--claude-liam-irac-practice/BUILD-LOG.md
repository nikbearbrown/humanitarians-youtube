# BUILD-LOG — claude-for-legal--claude-liam-irac-practice

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-irac-practice/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / legal-clinic collection)
about the `irac-practice` Anthropic Skill. Rebuilt here per hai-simple:
cold open replaced with `BrutalistHesitantWriter` (trigger word "answer" ->
"steps"), narration re-registered to Plain (facts unchanged, verdict
language removed), voice Liam `am_onyx`, close carries the Humanitarians AI
skin (`OutroSeries`). Question, mechanism claims (a Skill is a folder;
SKILL.md holds the instruction set; Claude executes its Steps linearly),
and body argument carried over unchanged from the source; see SCRIPT.md's
beat-count note for the full source-fidelity mapping.

**Source-fidelity note (read before touching this reel again):** the
source's `beat_sheet.json` was a batch build whose narration for the
specific-check beat (source B03/BVDT) carries literal unfilled template
placeholders (`>` marks) — the `irac-practice` skill's own SKILL.md
(referenced at `/Users/bear/Documents/CoWork/bear-textbooks/books/
anthropics/claude-for-legal/law-student/skills/irac-practice/SKILL.md`)
is not reachable from this machine — confirmed absent: only
`anthropics/claude-for-legal/youtube/claude-liam-irac-practice/` exists
locally for this topic, no source SKILL.md tree. This is NOT a
build-halting blocker per the completion law, because the source
establishes real, generic, true facts about how a Claude skill runs (a
folder, one instruction file, executed step by step) that carry over
cleanly. What did NOT carry over, because it was never actually present in
the source: any specific claim about what `irac-practice`'s particular
drilling script or hypo bank contains. NB03 instead states one concrete,
well-established, generically true fact about IRAC method itself — stating
the right Conclusion without showing the Application earns no credit,
because the Application is where the Rule actually meets the facts — which
is the actual reason IRAC practice is a task worth having a skill for, and
needs no invented Claude feature or fabricated checklist item. Documented
in QUESTION.md and SCRIPT.md's beat-count note. This is the same resolution
pattern used one build earlier in this loop for the identical placeholder
problem in `claude-for-legal--claude-liam-ip-clause-review`.

**Six-move / one-flag audits:** see SCRIPT.md. No wrong-guess beat beyond
B00's WRITER LAW correction (source has none of its own to redistribute);
single anchor (the `irac-practice` Skill itself, named throughout, never
dropped); both-directions folded into BCRY; zero inference flags (all
mechanism claims are direct, established facts).

**Build steps run, in order:**
1. Audio: `generate_audio_kokoro.py` — 7/7 beats generated (mean voice
   `am_onyx`), `actual_duration_s` written back into beat_sheet.json. B00's
   audio measured 9.92s; with `lead_silence_s: 0.8` the WRITER LAW's >=9s
   typing window is satisfied (~10.7s total).
2. GRAPHIC beats (NB01-NB03): rendered via the reel's own `render_scenes.py`
   / `scenes.py` (manim chip-row template, copied from the
   `claude-for-legal--claude-liam-ip-clause-review` sibling per its header
   note, same family/template).
3. REMOTION beats (B00, BCRY, BHTF, BOUT): rendered via
   `runtime/scripts/remotion_scenes.py` in the foreground (the render
   exceeded the tool's 120s timeout and was auto-moved to a background
   task by the harness; per the one-shot invocation warning, the turn was
   NOT ended to await a notification — instead blocked synchronously in
   the foreground on the task's output file until completion, confirmed
   exit code 0, all 4 beats: B00/BCRY/BHTF/BOUT `ok`).
4. Compile: `runtime/scripts/compile.py` -> `claude-for-legal--claude-liam-
   irac-practice.mp4`, 3840x2160, 74.1s. content-check/frame-check/
   lane-check all PASS. GATE AUDIO: PASS, mean_volume -24.0 dB.
5. GATE T (`type_check.py`): first run FAILED — 2 findings. (a) NB02
   bbox-overlap: two glyph blobs in the title "POSE, WAIT, CHECK"
   overlapped (a font-rendering artifacts specific to that letter
   cluster, reproduced only in the full composited beat frame, not an
   isolated title-only render — confirmed by directly calling
   `type_check.py`'s own `check_bbox_overlap`/`labeled_blobs` against
   extracted frames). (b) NB03 min-size: the "NO REASONING SHOWN" chip
   label was squeezed to a 0.75x scale-down to fit the fixed chip width,
   landing its rendered height at 19px, 1px under the 20px floor. Fixed
   by rewording the NB02 title to "POSE, PAUSE, CHECK" (removes the
   overlapping letter cluster) and shortening the over-squeezed chip
   labels ("WAIT FOR YOUR ANSWER" -> "PAUSE FOR ANSWER" in NB02, "NO
   REASONING SHOWN" -> "NO REASONING" in NB03) in `scenes.py`,
   `build_beat_sheet.py`, and `beat_sheet.json`'s `production_viz`
   fields (patched in place, not regenerated, to preserve the
   already-measured audio/render stamps). Verified each fix directly
   against `type_check.py`'s real check functions on the re-rendered
   clips before recompiling. Re-rendered NB02/NB03, RECOMPILED. Second
   run: GATE T PASS, all checks green (see TYPECHECK.md).
6. Gate V: pulled frames at fps=2 across the full master (148 frames);
   manually reviewed a spread (B00 open + correction landing on screen,
   NB01, NB02 fixed, NB03 fixed, BCRY, BHTF composer card, BOUT outro) —
   legible, correctly accented (one terracotta moment per beat), safe
   insets, no text overlap.
7. Verified master is newer than beat_sheet.json (mtime 1788104540 vs
   1788104470) and carries audible audio (ffprobe volumedetect:
   mean_volume -24.0 dB, well above the -40 dB floor).

**Result:** `claude-for-legal--claude-liam-irac-practice.mp4` — 7/7 beats
filled (B00:VIDEO NB01:MANIM NB02:MANIM NB03:MANIM BCRY:VIDEO BHTF:VIDEO
BOUT:VIDEO), 3840x2160, 74.1s, GATE T PASS, GATE AUDIO PASS, Gate V PASS.
Review cut is DONE. `<slug>.md` YouTube metadata written (Playlist: Claude
Basics, per `hai-simple/loop/playlists.json`'s `hai-simple` -> "Claude
Basics" mapping — `family` "claude-for-legal" has no direct prefix match in
the map).
