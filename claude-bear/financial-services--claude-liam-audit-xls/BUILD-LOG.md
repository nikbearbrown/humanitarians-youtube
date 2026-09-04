# BUILD-LOG — financial-services--claude-liam-audit-xls

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-audit-xls/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `audit-xls` skill (not an unfilled
placeholder shell) — see QUESTION.md. Facts preserved: it audits a
spreadsheet for formula accuracy, errors, and common mistakes; scopes to
a selected range, a single sheet, or the entire model (including BS
balance, cash tie-out, and logic sanity checks); checks BS balance first
because everything downstream is suspect if it's off; triggers on
phrases like "audit this sheet" / "check my formulas" / "model won't
balance". The `source_skill` path it names does not exist on this
machine (different machine's home directory), but no reconstruction was
needed.

**The call:** register re-registered Teardown → Plain. Source's B03
framed the BS-balance-first ordering as "the interesting constraint... a
deliberate trade-off" — Teardown design judgment — removed; Plain states
only the mechanism (checks balance first, because downstream becomes
suspect if it's off) and its two failure directions, never a verdict on
the ordering choice itself. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` per WRITER LAW: "fix" → "audit"
— the newcomer's actual wrong guess that asking Claude to look at a
broken spreadsheet means asking it to repair it, corrected to: it audits
and reports, it doesn't rewrite. Added a wrong-guess beat (B01: "finds
the errors and fixes them" vs. audits-and-reports, falsified by
"check the sheet again after — the formula is untouched") and an anchor
(B02 → B03: a balance sheet off by a fixed amount traveling scope-set →
checked-first → mismatch-found → cited/reported, then stopping, paid off
into "balanced is not error-free" / "suspect is not wrong") per this
factory's PHASE 1 structure requirement — the source's Teardown shape
(anatomy / pipeline / design-tell / verdict) carried neither. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept
the source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No
source beat was AI-VIDEO, pantry, or a human-drop slot — every source
beat was already REMOTION, so NO-GENAI/NO-PANTRY LAW required no beat
replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 9.30s (clear of the ≥9s TIMING LAW
   floor, though tighter margin than the `accrual-schedule` sibling's
   10.35s) on the first narration draft (29 words + `lead_silence_s:
   0.8`). Durations: B00 9.30s, B01 20.71s, B02 16.94s, B03 22.38s, BCRY
   10.86s, BHTF 17.28s, BOUT 4.52s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `AXLB01Scene` /
   `AXLB02Scene` / `AXLB03Scene`, reusing the `accrual-schedule` sibling's
   already-worked-around card pattern from the start — TEAL borders, not
   INK; fade-out/fade-in token transitions, never a continuous slide;
   traveling token held clear of every card, off in open ground) and
   `render_scenes.py`; rendered B01–B03 clean on the first pass — no
   repeat of that sibling's four-attempt bbox-overlap hunt.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the
   foreground, per the ONE-SHOT/COMPLETION LAW (no background render left
   unsupervised). All four rendered clean on the first pass.
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K LAW
   forces a clean non-review master to 4K), mean_volume -24.2 dB (GATE
   AUDIO pass on the first compile).
5. GATE T (`type_check.py`) → PASS, clean, zero FAILs, first attempt —
   the TEAL-border / fade-not-slide pattern carried over from the
   `accrual-schedule` sibling avoided that reel's four-round bbox-overlap
   failure hunt entirely.
6. Gate V (visual, manual): pulled 26 frames every 4s across the full
   103.0s runtime and read every one directly. B00's correction ("fix" →
   "audit") lands legibly on the final frame; B01's struck "FIX IT" hand
   and lit "AUDIT REPORT" card read cleanly, including the "checked again
   — cell unchanged" / "the report changed, not the spreadsheet" pair;
   B02's four-stop anchor (with the traveling "BS OFF BY $1,200" token
   beside each card) is legible at every step; B03's anchor-return and
   both-directions split ("balanced is not error-free" / "suspect is not
   wrong", including the strike-through on "ERROR-FREE?") read cleanly;
   BCRY's carry-out quote, BHTF's Your Turn composer card, and BOUT's
   title outro all render legibly with no overlap, no clipping, no
   contrast issues. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.2 dB**, max -2.9 dB. Master mtime
   (07:00:46) is newer than beat_sheet.json mtime (06:59:10).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family
(`financial-services--claude-liam-accrual-schedule`,
`financial-services--claude-liam-ai-readiness`, `claude-for-legal--claude-liam-handbook-updates`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), first pass
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 103.0s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a
defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your
Turn) + BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC
body beats for this 7-beat reel — same disposition as every other short
hai-simple reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same
resolution as the `accrual-schedule` and `ai-readiness` sibling reels in
this same family.

Metadata file written:
`financial-services--claude-liam-audit-xls.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-audit-xls.mp4 \
   financial-services--claude-liam-audit-xls-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-audit-xls/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-audit-xls/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `08b3ab60`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
