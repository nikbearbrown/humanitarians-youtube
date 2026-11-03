# BUILD-LOG — financial-services--claude-liam-initiating-coverage

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-initiating-coverage/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `initiating-coverage` skill (not an
unfilled placeholder shell) — see QUESTION.md. Facts preserved: the skill
creates equity research initiation reports through a five-task workflow —
(1) company research, (2) financial modeling, (3) valuation analysis, (4)
chart generation, (5) final report assembly — executed individually with
verified prerequisites; tasks 3–5 depend on earlier tasks; deliverables
are markdown docs, Excel models, charts, or DOCX reports. The
`source_skill` path it names does not exist on this machine (different
machine's home directory, same situation as the `clean-data-xls` sibling
redo), but no reconstruction was needed.

**The call:** register re-registered Teardown → Plain. Source's B03
framed "what it gets right: repeatable results / what it bites: anything
outside the spec" as a design-tell verdict — Teardown language — removed;
Plain states only the mechanism (five ordered, dependency-gated tasks)
and its two failure directions as properties of the practice, never a
verdict on the skill's design. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` per WRITER LAW: "instantly" →
"five ordered tasks" — the naive assumption that asking for coverage
produces the whole report in one pass, corrected to: it runs a fixed
five-task pipeline with dependencies. Added a wrong-guess beat (B01: one
continuous pass vs. the five-task ordered chain, falsified by "jump
straight to valuation before a financial model exists — task three's
prerequisite isn't there, so it can't run") and an anchor (B02 → B03: one
ticker's coverage package moving through RESEARCH → MODEL → VALUATION →
CHARTS → REPORT, then resting at REPORT and splitting into the two
both-directions cautions) per this factory's PHASE 1 structure
requirement — the source's Teardown shape (anatomy / pipeline /
design-tell / verdict) carried neither. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Kept the source's 7-beat count
(B00, B01, B02, B03, BCRY, BHTF, BOUT). No source beat was AI-VIDEO,
pantry, or a human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 11.5s (clear of the ≥9s TIMING LAW floor)
   on the first narration draft (33 words + `lead_silence_s: 0.8`).
   Durations: B00 11.5s, B01 28.35s, B02 26.56s, B03 29.61s, BCRY 16.58s,
   BHTF 18.86s, BOUT 4.76s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `ICB01Scene` /
   `ICB02Scene` / `ICB03Scene`, reusing the `clean-data-xls` sibling's
   worked-around card-border pattern — TEAL borders, not INK, and the
   traveling token fading beside each card rather than sliding through
   it, plus off-card overflow lines) and `render_scenes.py`; rendered
   B01, B02, B03 clean on the first pass.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The shell moved
   it to a background task past the 120s inline timeout; blocked on it
   with `TaskOutput` rather than ending the turn — no unsupervised
   background render was left running, per the ONE-SHOT/COMPLETION LAW.
   All four rendered clean on the first pass. B00 verified ≥8s (11.5s)
   and the "instantly" → "five ordered tasks" correction confirmed
   legible on a frame at t=9.5s, well inside the clip.
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K LAW),
   mean_volume -24.1 dB, no slow-mo warnings (B01 2.44x, B02 2.33x, B03
   2.04x — all under the 3.0x flag threshold).
5. GATE T (`type_check.py`) → first pass **FAIL** (1 FAIL): B03's mini
   summary row (`RESEARCH`/`MODEL`/`VALUATION`/`CHARTS`/`REPORT`,
   font_size 15) shrinks further under the beat's `row.animate.scale(0.55)`
   transition and renders below the 20px legibility floor (measured
   11px) — same defect class as the `clean-data-xls` sibling. Fixed by
   bumping those five labels to font_size 34 with `_fit_text` capping
   width at 2.5 (card width 2.6). Re-rendered B03, recompiled, GATE T →
   **PASS**, 0 FAILs.
6. Gate V (visual, manual): pulled 17 frames every 8s across the full
   137.2s runtime, plus one frame at t=9.5s for the B00 correction, and
   read every one directly. B00's correction ("instantly" → "five
   ordered tasks") lands legibly; B01's struck one-pass card and lit
   five-task chain read cleanly, including the off-card "valuation
   before a model exists — can't run" line; B02's five-card anchor (with
   the fading "TICKER PACKAGE" token beside each card) is legible at
   every step; B03's anchor-return and both-directions split ("ran is
   not sound" / "blocked is not bad") read cleanly, including the
   strike-through on "SOUND?" and the now-legible mini summary row;
   BCRY's carry-out quote, BHTF's Your Turn composer card, and BOUT's
   title outro all render legibly with no overlap, no clipping, no
   contrast issues. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.1 dB**, max -2.8 dB. Master mtime
   (23:01:51) is newer than beat_sheet.json mtime (22:54:59).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`financial-services--claude-liam-clean-data-xls`,
`financial-services--claude-liam-accrual-schedule`,
`financial-services--claude-liam-ai-readiness`,
`financial-services--claude-liam-3-statement-model`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (first pass caught 1 real min-size
  defect in B03, fixed and re-verified — see step 5)
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 137.2s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking observation (compile.py):** motion histogram
remotion:4 graphic:3 — remotion at more than half of beats. Structural,
not a defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF
(Your Turn) + BOUT (outro) all REMOTION by skill contract, against 3
GRAPHIC body beats for this 7-beat reel — same disposition as every other
short hai-simple reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as every other `financial-services--*` sibling reel in this log.

Metadata file written: `financial-services--claude-liam-initiating-coverage.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
