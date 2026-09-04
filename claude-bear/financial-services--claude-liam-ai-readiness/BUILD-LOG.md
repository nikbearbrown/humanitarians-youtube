# BUILD-LOG — financial-services--claude-liam-ai-readiness

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-ai-readiness/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `ai-readiness` skill (not an unfilled
placeholder shell) — see QUESTION.md. Facts preserved: the skill scans
the portfolio for the highest-leverage AI opportunities and ranks where
to deploy operating-partner time; it ingests quarterly updates and
financials across multiple portfolio companies, identifies quick wins at
each, and stacks them into a single ranked action list; used during
quarterly portfolio reviews, annual planning, or when deciding which
companies get AI investment first. The `source_skill` path it names does
not exist on this machine (different machine's home directory), but no
reconstruction was needed.

**The call:** register re-registered Teardown → Plain. Source's B03
framed "what it gets right / where it bites" as a design-tell verdict —
Teardown language — removed; Plain states only the mechanism (ingest,
identify, rank) and its two failure directions as properties of the
practice, never a verdict on the skill's design. B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
per WRITER LAW: "judgment" → "the update" — the naive assumption that
ranking AI-readiness takes Claude's own judgment about the companies,
corrected to: it works from what's in the update. Added a wrong-guess
beat (B01: judgment vs. ingest/identify/rank, falsified by "a company
whose update never mentions an AI opportunity gets nothing ranked") and
an anchor (B02 → B03: one portfolio company's Q3 update traveling
identified → quick wins found → scored → ranked, then stopping, waiting)
per this factory's PHASE 1 structure requirement — the source's Teardown
shape (anatomy / pipeline / design-tell / verdict) carried neither. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept
the source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No
source beat was AI-VIDEO, pantry, or a human-drop slot — every source
beat was already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no beat replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 11.16s (clear of the ≥9s TIMING LAW
   floor) on the first narration draft (34 words + `lead_silence_s: 0.8`).
   Durations: B00 11.16s, B01 22.19s, B02 20.97s, B03 26.45s, BCRY 13.01s,
   BHTF 20.69s, BOUT 5.01s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `AIRB01Scene` /
   `AIRB02Scene` / `AIRB03Scene`, reusing the `accrual-schedule` sibling's
   worked-around card-border pattern — TEAL borders, not INK, and the
   traveling token fading beside each card rather than sliding through
   it, plus off-card overflow lines — since that sibling had already hit
   and fixed the exact GATE T false-positive this layout risks) and
   `render_scenes.py`; rendered B01, B02, B03 clean on the first pass.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The shell moved
   it to a background task past the 120s inline timeout; blocked on it
   with `TaskOutput` rather than ending the turn — no unsupervised
   background render was left running, per the ONE-SHOT/COMPLETION LAW.
   All four rendered clean on the first pass.
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K LAW),
   mean_volume -24.0 dB (GATE AUDIO pass on the first compile).
5. GATE T (`type_check.py`) → PASS, first pass, 0 FAILs. No repeat of the
   `accrual-schedule` sibling's card-border/bbox-overlap failure mode —
   avoided by reusing its worked-around scene pattern from the start
   (see step 2).
6. Gate V (visual, manual): pulled 20 frames every 6s across the full
   120.5s runtime and read every one directly. B00's correction
   ("judgment" → "the update") lands legibly; B01's struck judgment box
   and lit ingest/identify/rank card read cleanly, including the
   off-card "no mention in update" line; B02's four-stop anchor (with
   the fading "PORTCO A · Q3 UPDATE" token beside each card) is legible
   at every step, including the mid-transition shrink frame; B03's
   anchor-return and both-directions split ("scored well is not best
   overall" / "ranked low is not no opportunity") read cleanly, including
   the strike-through on "BEST OVERALL?"; BCRY's carry-out quote, BHTF's
   Your Turn composer card, and BOUT's title outro all render legibly
   with no overlap, no clipping, no contrast issues. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.0 dB**, max -2.9 dB. Master mtime is newer
   than beat_sheet.json mtime.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`financial-services--claude-liam-accrual-schedule`,
`financial-services--claude-liam-3-statement-model`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), first pass
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 120.48s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a
defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your
Turn) + BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC
body beats for this 7-beat reel — same disposition as every other short
hai-simple reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the
map's documented fallback ("match SUBJECT.json's family, or the
hai-simple prefix"), fell through to matching the skill name itself:
`hai-simple` is a literal key in the map, resolving to **Claude Basics**
— same resolution as the `accrual-schedule` and `3-statement-model`
sibling reels in this same family.

Metadata file written:
`financial-services--claude-liam-ai-readiness.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-ai-readiness.mp4 \
   financial-services--claude-liam-ai-readiness-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-ai-readiness/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-ai-readiness/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `faa4eb98`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
