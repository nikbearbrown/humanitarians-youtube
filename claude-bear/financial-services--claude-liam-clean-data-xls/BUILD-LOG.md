# BUILD-LOG — financial-services--claude-liam-clean-data-xls

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-clean-data-xls/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `clean-data-xls` skill (not an unfilled
placeholder shell) — see QUESTION.md. Facts preserved: the skill cleans up
messy spreadsheet data by trimming whitespace, fixing inconsistent casing,
converting numbers stored as text into real numbers, standardizing dates,
removing duplicate rows, and flagging columns that mix types — nothing
beyond that six-item list; used when data is messy, inconsistent, or needs
prep before analysis. The `source_skill` path it names does not exist on
this machine (different machine's home directory), but no reconstruction
was needed.

**The call:** register re-registered Teardown → Plain. Source's B03 framed
"what it gets right: repeatable results / what it bites: anything outside
the spec" as a design-tell verdict — Teardown language — removed; Plain
states only the mechanism (the six fixed operations) and its two failure
directions as properties of the practice, never a verdict on the skill's
design. B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW: "judgment" → "a checklist" — the
naive assumption that cleaning messy data takes Claude's own judgment
about what looks wrong, corrected to: it runs a fixed list of six
operations. Added a wrong-guess beat (B01: judgment vs. the six-step
checklist, falsified by "a column mixing two currencies under one symbol
isn't on the checklist, so it passes through unchanged") and an anchor
(B02 → B03: one Revenue column carrying " 1,200 " / "1300" / "N/A" /
" 1,400.00 " traveling raw → trimmed → converted → flagged, then stopping,
waiting) per this factory's PHASE 1 structure requirement — the source's
Teardown shape (anatomy / pipeline / design-tell / verdict) carried
neither. Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Kept the source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF,
BOUT). No source beat was AI-VIDEO, pantry, or a human-drop slot — every
source beat was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no beat replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 9.96s (clear of the ≥9s TIMING LAW floor)
   on the first narration draft (30 words + `lead_silence_s: 0.8`).
   Durations: B00 9.96s, B01 29.18s, B02 25.86s, B03 28.44s, BCRY 12.82s,
   BHTF 19.50s, BOUT 4.74s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CDXB01Scene` /
   `CDXB02Scene` / `CDXB03Scene`, reusing the `ai-readiness` sibling's
   worked-around card-border pattern — TEAL borders, not INK, and the
   traveling token fading beside each card rather than sliding through
   it, plus off-card overflow lines) and `render_scenes.py`; rendered
   B01, B02, B03 clean on the first pass.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The shell moved
   it to a background task past the 120s inline timeout; blocked on it
   with `TaskOutput` rather than ending the turn — no unsupervised
   background render was left running, per the ONE-SHOT/COMPLETION LAW.
   All four rendered clean on the first pass. B00 verified ≥8s (9.966s)
   and the "judgment" → "a checklist" correction confirmed legible on a
   frame at t=9.3s, well inside the clip.
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K LAW),
   mean_volume -24.0 dB — but flagged B03 with a non-fatal WARNING:
   "clip 9.4s slowed 3.0x into 28.4s beat — extreme slow-mo." Fixed at the
   root rather than accepted: lengthened B03's Manim scene wait times
   (four `self.wait()` calls extended, adding ~5.1s) to bring the clip to
   14.5s, dropping the stretch ratio to 1.96x. Re-rendered B03, recompiled
   → clean, no warning.
5. GATE T (`type_check.py`) → first pass **FAIL** (1 FAIL): B03's mini
   summary row (`TRIMMED`/`CONVERTED`/`FLAGGED`, font_size 15) shrinks
   further under the beat's `row.animate.scale(0.6)` transition and
   renders below the 20px legibility floor (measured 12px). Fixed by
   bumping those three labels to font_size 32 with `_fit_text` capping
   width at 2.85 (card width 3.0), so the post-scale render clears the
   floor. Re-rendered B03, recompiled, GATE T → **PASS**, 0 FAILs.
6. Gate V (visual, manual): pulled 26 frames every 5s across the full
   131.5s runtime and read every one directly. B00's correction
   ("judgment" → "a checklist") lands legibly; B01's struck judgment box
   and lit six-step checklist card read cleanly, including the off-card
   "two currencies, one symbol" line; B02's four-stop anchor (with the
   fading "REVENUE COLUMN" token beside each card) is legible at every
   step; B03's anchor-return and both-directions split ("converted
   cleanly is not correct" / "flagged is not broken") read cleanly,
   including the strike-through on "CORRECT?" and the now-legible mini
   summary row; BCRY's carry-out quote, BHTF's Your Turn composer card,
   and BOUT's title outro all render legibly with no overlap, no
   clipping, no contrast issues. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.0 dB**, max -2.9 dB. Master mtime
   (10:16:04) is newer than beat_sheet.json mtime (10:08:40).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
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
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 131.5s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py), resolved:** first compile pass
flagged B03 as extreme slow-mo (3.0x stretch); fixed at the root by
lengthening the Manim scene rather than accepting the stretch — see step
4. Second compile: clean, no warning.

**Non-blocking warning (compile.py), structural:** motion histogram
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

Metadata file written: `financial-services--claude-liam-clean-data-xls.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.

```
cp financial-services--claude-liam-clean-data-xls.mp4 \
   financial-services--claude-liam-clean-data-xls-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-clean-data-xls/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-clean-data-xls/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `52d0dc8c`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
