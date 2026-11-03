# BUILD-LOG — claude-for-legal--claude-liam-ip-clause-review

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-ip-clause-review/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / legal-clinic collection)
about the `ip-clause-review` Anthropic Skill. Rebuilt here per hai-simple:
cold open replaced with `BrutalistHesitantWriter` (trigger word "judging" ->
"checking a list"), narration re-registered to Plain (facts unchanged,
verdict language removed), voice Liam `am_onyx`, close carries the
Humanitarians AI skin (`OutroSeries`). Question, mechanism claims (a Skill
is a folder; SKILL.md holds the instruction set; Claude executes its Steps
linearly), and body argument carried over unchanged from the source; see
SCRIPT.md's beat-count note for the full source-fidelity mapping.

**Source-fidelity note (read before touching this reel again):** the
source's `beat_sheet.json` was a batch build whose narration for the
specific-check beat (source B03/BVDT) carries literal unfilled template
placeholders (`>` marks) — the `ip-clause-review` skill's own SKILL.md
(presumably in a legal-clinic collection not reachable from this machine)
was never actually filled in. Confirmed absent locally: only
`anthropics/claude-for-legal/youtube/claude-liam-ip-clause-review/` exists
for this topic, no source SKILL.md tree. This is NOT a build-halting
blocker per the completion law, because the source establishes real,
generic, true facts about how a Claude skill runs (a folder, one
instruction file, executed step by step) that carry over cleanly. What did
NOT carry over, because it was never actually present in the source: any
specific claim about what `ip-clause-review`'s particular legal checklist
contains. NB03 instead states one concrete, generically true fact about IP
contract drafting — a clause that only licenses rights does not transfer
ownership; only a clause that assigns them does — which is the actual
reason an IP-clause review is a task worth having a skill for, and needs no
invented Claude feature or fabricated checklist item. Documented in
QUESTION.md and SCRIPT.md's beat-count note.

**Six-move / one-flag audits:** see SCRIPT.md. No wrong-guess beat beyond
B00's WRITER LAW correction (source has none of its own to redistribute);
single anchor (the `ip-clause-review` Skill itself, named throughout, never
dropped); both-directions folded into BCRY; zero inference flags (all
mechanism claims are direct, established facts).

**Build steps run, in order:**
1. Audio: `generate_audio_kokoro.py` — 7/7 beats, `mp3/timings.json` written
   (already done on a prior pass within this same invocation before context
   compaction; verified present and consistent with beat_sheet.json on
   resume).
2. GRAPHIC beats (NB01–NB03): rendered via the reel's own `render_scenes.py`
   / `scenes.py` (manim chip-row template, copied from the
   `claude-for-legal--claude-liam-cease-desist` sibling per its header note).
3. REMOTION beats (B00, BCRY, BHTF, BOUT): rendered via
   `runtime/scripts/remotion_scenes.py` — B00 and BOUT were already filled
   from the prior pass; BCRY (`WantQuote`) and BHTF (`ClaudeComposerAsk`)
   rendered this pass.
4. Compile: `runtime/scripts/compile.py` -> `claude-for-legal--claude-liam-
   ip-clause-review.mp4`, 3840x2160, 78.1s. content-check/frame-check/
   lane-check all PASS. GATE AUDIO: PASS, mean_volume -23.9 dB.
5. GATE T (`type_check.py`): first run FAILED — NB01's "FOLDER:
   ip-clause-review" chip label rendered at 11px, under the 20px/1.9%
   floor (too many characters forced a double downscale in the chip-row
   template). Fixed by shortening the label to "ip-clause-review/"
   (matching the sibling `hiring-review` reel's convention of a bare
   folder-name chip with no "FOLDER:" prefix) in both `scenes.py` and
   `beat_sheet.json`'s `production_viz.chips`, re-rendered NB01, and
   RECOMPILED. Second run: GATE T PASS, all checks green.
6. Gate V: pulled frames at fps=2 across the full master (156 frames) plus
   a late B00 frame and the fixed NB01 frame; manually reviewed a spread
   (B00 open + correction, NB01 fixed, NB03, BHTF composer card, BOUT
   outro) — legible, correctly accented (one terracotta moment per beat),
   safe insets, no text overlap.
7. Verified master is newer than beat_sheet.json (mtime 1788102737 vs
   1788102665) and carries audible audio (ffprobe volumedetect:
   mean_volume -23.9 dB, well above the -40 dB floor).

**Result:** `claude-for-legal--claude-liam-ip-clause-review.mp4` — 7/7 beats
filled (B00:VIDEO NB01:MANIM NB02:MANIM NB03:MANIM BCRY:VIDEO BHTF:VIDEO
BOUT:VIDEO), 3840x2160, 78.1s, GATE T PASS, GATE AUDIO PASS, Gate V PASS.
Review cut is DONE. `<slug>.md` YouTube metadata written (Playlist: Claude
Basics, per `hai-simple/loop/playlists.json`'s `hai-simple` -> "Claude
Basics" mapping — `family` "claude-for-legal" has no direct prefix match in
the map).

**Not yet done (Phase 4, next invocation if resumed):** 4K delivery render
and `deliver.py --push` staging were not run this pass — the compiled
master above is already native 3840x2160 (the "4K LAW" forced-upscale in
compile.py's own output), so a separate `-4k.mp4` render step and the
delivery packaging remain open if this reel is picked up again for
delivery.
