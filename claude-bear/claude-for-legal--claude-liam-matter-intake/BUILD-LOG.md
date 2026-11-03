# BUILD-LOG — claude-for-legal--claude-liam-matter-intake

## 2026-08-30 — review cut, DONE

This invocation picked up a reel already partially built by an earlier,
unlogged attempt: `beat_sheet.json`, `SCRIPT.md`, `CARRY-OUT.md`,
`QUESTION.md`, all 11 beats' Kokoro audio (`mp3/`, `timings.json`), all 7
GRAPHIC beats rendered (`manim/B01.mp4`-`B07.mp4`), and 2 of 4 REMOTION
beats rendered (`media/B00.mp4`, `media/BCRY.mp4`) already existed on disk
with no `BUILD-LOG.md` to explain the state. Per the COMPLETION LAW, verified
each artifact rather than trusting it, and continued from where the prior
attempt stopped rather than rebuilding from scratch.

**Redo-mode build** (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-matter-intake/beat_sheet.json`.
Register re-registered Teardown -> Plain; B00 is `BrutalistHesitantWriter`
(WRITER LAW) in place of the source's `ClaudeComposerAsk`; close carries the
Humanitarians AI skin. Source's nine intake categories, two output files
(`matter.md`/`history.md`), and `_log.yaml` row are carried verbatim from the
source's own narration (see `QUESTION.md`).

**Completed this invocation:**

1. Rendered the two missing REMOTION beats (`BHTF`, `BOUT`) via
   `remotion_scenes.py` in the foreground.
2. First `compile.py` pass -> 11/11 real (no slate), 3840×2160 (4K LAW),
   mean_volume -24.1 dB.

**Gate V (visual) — found and fixed one real defect in B00:**

Pulled frames across the full runtime and read them directly. B00
(`BrutalistHesitantWriter`) never reached its own question: the props
authored by the prior attempt — a 4-line, two-sentence text ("Claude decides
which matters to take on with matter-intake. What is a skill?") with
`mistakeRate:5 hesitateWithin:2 hesitateBetween:12 charMs:46 jitter:26` and a
"decides"->"logs" correction — hand-computed against the component's own
deterministic timeline builder (`BrutalistHesitantWriter.tsx`:
`buildActs`/`buildTimeline`) come out to roughly **11.4s of expected typing**
against the beat's **10.11s** audio-driven window. The render confirmed it:
pulled frames at t=8-10.8s and the typing stopped at "...with matter-intake."
— the fourth line, "What is a skill?", never appeared. The beat cut to B01
before landing on a question at all, which fails the WRITER LAW ("end ON the
question") independent of the timing defect.

Cross-checked the math against a shipped sibling
(`claude-for-legal--claude-liam-ai-inventory`, `actual_duration_s` 9.94s):
the same hand-computation against its props (42 chars, single 3-line
question, "policy"->"inventory") comes out to ~8.96s — under budget with
~1s margin, consistent with it having shipped correctly.

**Fix:** rewrote B00's on-screen text only (narration/audio/duration
untouched) to match the proven pattern — a single 3-line question with the
correction inline, ending on "?": "Does matter-intake / decide which
matters / to take on?", trigger "decide"->"log" (base-verb forms so
"Does...decide"/"Does...log" stay grammatical). Hand-computed expected
typing time for the new props: ~8.24s, leaving ~1.9s margin. Re-rendered B00
with `--force`, recompiled. Verified: `media/B00.mp4` extended to 10.1s (the
full window, as expected), and frame pulls at t=3s/5.5s/9.0s/9.8s confirm the
correction lands by ~5.5s and the beat completes at "Does matter-intake log
which matters to take on?" with the cursor after the closing "?" — the
question, in full, on screen. Updated `SCRIPT.md`'s B00 visual-description
cell and `CARRY-OUT.md`'s wrong-guess description to match (narration text
itself unchanged).

**GATE T (`type_check.py`) — found and fixed three real defects:**

First pass: FAIL (3 pixel beats — B01, B03, B06), all "min-size §8.1:
smallest text run 15px < floor 20px", B03/B06 additionally "bbox-overlap
§8.6b" at 100%. Root-caused via `scenes.py`'s shared `_chip()` renderer: its
length-tiered font size (`26 if len<=14 else 22 if len<=22 else 17`) dropped
to 17pt for labels over 22 characters — B03/B06's anchor chips
("Identification · Conflicts · Source", etc.) at that size rendered the
middot "·" small enough to survive `type_check.py`'s fragment filter as its
own isolated ~15px connected-component blob, nested inside the chip
border's bbox (same documented false-positive class as the `SPCB04Scene`
exemption already in `type_check.py` — a real, if small, rendering defect,
not a checker bug). No exemption mechanism exists for §8.1 (only §8.6b has
`BBOX_OVERLAP_EXEMPT_PATTERNS`), so fixed at the content level:

- Raised the >22-char font-size tier 17->21 and loosened the chip's
  width/height fit caps (0.86->0.92, 0.7->0.8) so the larger font isn't
  immediately re-clamped back down. Re-rendered B01/B03/B06, recompiled,
  re-ran GATE T: B03/B06 now pass (151px, both checks green); B01 still
  failed at the same 15px, unchanged.
- B01's failure turned out to be a different mechanism: its first chip
  ("CLAUDE HAS A MATTER-INTAKE SKILL", 32 chars, n=2 row) was wide enough at
  the new fs=21 to still hit the width cap and get scaled back down by
  Manim's `set_width()`, shrinking its hyphen glyph under the floor
  regardless of nominal font size. `render_chip_row`'s chip width formula
  (`min(3.4, (12.4-(n-1)*gap)/n)`) capped every row's chip width at 3.4
  units even when fewer chips left much more of the 12.4-unit budget unused
  (n=2 computes 5.9, still capped to 3.4). Raised the cap 3.4->5.0 so 2-chip
  rows actually use the available width. Re-rendered B01, recompiled,
  re-ran GATE T: **PASS, 0 FAILs.**

Verified by frame pull after each fix (not just re-running the checker):
B01/B03/B06 all read cleanly at native size, wider chips, visible margin,
no text-on-text overlap, safe inset intact.

**Gates (final state):**
- content-check: PASS (11 beats, no violations)
- frame-check: PASS (3840×2160, 11 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: **PASS (0 FAILs)**
- Gate V: PASS after fixing the B00 timing/WRITER-LAW defect above; all 11
  beats read legibly, safe inset, no overlap
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 126.781s, video 3840×2160 h264 + aac audio; mp4 mtime
  (1788124715) newer than beat_sheet.json mtime (1788123912)

**Non-blocking warning (compile.py):** motion histogram graphic:7
remotion:4 — graphic at 63%, over the ~40% pantry-cap guidance. Structural:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 7 GRAPHIC body beats for
this 11-beat reel (the source sheet's own beat count, preserved per the
redo-mode LOCKED SCRIPT contract) — same disposition as other longer
hai-simple redos in this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Falls through to
the skill name itself: `hai-simple` is a literal key in the map, resolving
to **Claude Basics** (already stamped in `beat_sheet.json`'s metadata by the
prior attempt; confirmed correct against the map file, not just reused
blind).

Metadata file written: `claude-for-legal--claude-liam-matter-intake.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct code
link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.

```
cp claude-for-legal--claude-liam-matter-intake.mp4 \
   claude-for-legal--claude-liam-matter-intake-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/claude-for-legal--claude-liam-matter-intake/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-matter-intake/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `70a6d18`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
