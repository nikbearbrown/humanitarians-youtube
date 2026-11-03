# BUILD-LOG — behind-the-model--claude-liam-self-check-vs-independent-verification

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-authored Teardown CLI sheet
(`anthropics/youtube/behind-the-model/claude-liam-self-check-vs-independent-verification/beat_sheet.json`,
"Compare Self-Check vs. Independent Verification on an Agent Output with
Claude", brand `cli`, NikBearBrownTerminalAsk/NikBearBrownCodeBlock/FormBCard
beats, `NikBearBrownOpen` cold open, `ClaudeTitleOutro`). Picked up mid-build
this invocation: SCRIPT.md, QUESTION.md, CARRY-OUT.md, beat_sheet.json (10/10
beats authored), mp3 narration (Kokoro, all 10 beats measured), manim/B01-B06
already rendered, and media/B00.mp4 + media/BHTF.mp4 + media/BOUT.mp4 already
rendered from an earlier part of this same session (context had been
summarized) — verified each artifact against beat_sheet.json before reuse
rather than re-deriving from scratch, per the CONTINUE-where-it-stopped rule.

Kept the question and every fact from the source: a five-claim research
summary with one citation per claim, self-checked and returning clean on the
first pass; swapping claim three's citation for a paper that doesn't support
it and rerunning the self-check still returns "verified" (the check reasons
from the same claim it's supposed to be testing, not the paper); opening the
actual paper catches the mismatch immediately; self-check improves output at
the margins but cannot catch systematic errors, so independent verification
is what makes "verified" mean something. **Anchor B01->B06:** the five-claim
table, self-check column, all clean — returns with a human-check column
added, four rows agree, the planted error at claim 3 diverges.

### GATE T — one real defect found and fixed, two false positives registered

On pickup, GATE T failed 3 beats (B01, B03, B06) on `bbox-overlap §8.6b`,
and B01 also failed `min-size §8.1` (an 11px stray blob).

- **Real bug, fixed:** `SCVB01Scene`'s "SELF-CHECK" column header used
  `header.move_to(RIGHT * 1.0 + UP * (rows.get_top()[1] -
  rows[0].get_center()[1] + 0.5))` — after `rows.move_to(LEFT * 4.0)`
  recenters the whole five-row group's bounding box at y=0, that formula no
  longer measures "above row 0"; it landed the header exactly on row 1's
  ("CLAIM 2") y-coordinate, printing "SELF-CHECK" directly on top of its
  "verified" label (confirmed by direct frame pull/crop — the two strings
  were visibly fused). The min-size 11px finding was a byproduct: OCR-style
  blob detection on the fused ink produced a stray fragment below the 20px
  floor. Fixed by replacing the formula with `header.move_to(RIGHT * 1.0);
  header.set_y(rows.get_top()[1] + 0.4)` — unambiguously above the whole
  group regardless of its centering. Re-rendered B01; frame pull confirms
  "SELF-CHECK" now sits cleanly above "CLAIM 1" with no overlap, and the
  min-size finding disappeared as a side effect (it was never a separate
  defect).
- **Verified false positives, registered:** B01's row-card pattern (after
  the header fix) and B06's identical `_claim_rows()` table both still trip
  the box-border-encloses-label detector class (a `RoundedRectangle` chip's
  INK border ring bbox necessarily encloses its own centered "CLAIM N" label
  — same mechanism as `B01Scene`/`B02_FiveProperties`/`IVPB01Scene` and ~25
  other precedents in `type_check.py`). B03's "CLAIM 3" row card is the same
  pattern plus a `CurvedArrow` loop that arcs tangent to, not through, the
  struck "old citation" line — frame-pulled and confirmed no real
  text-on-text or line-on-text overlap in any of the three beats. Registered
  `SCVB01Scene`, `SCVB03Scene`, `SCVB06Scene` in `BBOX_OVERLAP_EXEMPT_PATTERNS`
  in `runtime/scripts/type_check.py`, with a rationale comment, rather than
  loosening the check itself.

GATE T: **PASS, 0 FAILs** after the one real fix + registering the two
already-documented false-positive classes.

### Build sequence

1. Audio (`generate_audio_kokoro.py`) — already complete on pickup, 10/10
   beats measured (B00 10.41s ... BOUT 3.82s, total narration 107.3s).
2. `render_scenes.py` — B01 re-rendered after the header fix; B02-B06
   already rendered and reused as-is.
3. `remotion_scenes.py --only BCRY` — B00/BHTF/BOUT were already rendered
   from earlier in this session; only BCRY was still outstanding (shot
   showed `build.status: "SLATE"`). Rendered in the foreground: `WantQuote ->
   media/BCRY.mp4 (extended to 7.1s)`.
4. `compile.py` (no `--review`) — THE 4K LAW forced the clean master
   natively to 3840x2160. content-check/frame-check/lane-check all PASS,
   GATE AUDIO PASS mean_volume -24.0 dB. All 10 slots filled with real
   media (no slate): B00/BCRY/BHTF/BOUT VIDEO, B01-B06 MANIM.

Gate V: pulled 14 frames across the full 108s master (`fps=1/8`) and read
every one directly — B00 hesitant-writer correction legible, B01 anchor
table clean (header fix confirmed in the compiled master, not just the raw
manim clip), B02-B06 all legible with no overlap, BCRY carry-out card clean,
BHTF Your-Turn composer shows the full paste-ready prompt with the
Humanitarians AI folder label, BOUT outro carries the humanitarians skin
(Subscribe + @HumanitariansAI) correctly. No blockers.

**Gates:**
- content-check: PASS (10 beats, no violations)
- frame-check: PASS (3840x2160, 10 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after 1 real fix + 2 registered false-positive
  exemption classes covering 3 beats)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe independently reverified: 3840x2160 h264, duration 108.36s; mp4
  mtime (2026-09-05 04:43:52) newer than beat_sheet.json mtime (2026-09-05
  04:42:22)

**Non-blocking warning (compile.py):** motion histogram graphic:6 remotion:4
— GRAPHIC at 60%, over the ~40% pantry-cap guideline in MOTION.md.
Structural for this shape: hai-simple's mandated B00 (writer) + BCRY + BHTF
(Your Turn) + BOUT (outro) are REMOTION by skill contract, against 6 GRAPHIC
body beats for this 10-beat reel (B01-B06) — same disposition as every other
`behind-the-model--*` sibling at this beat count.

Metadata file written: `behind-the-model--claude-liam-self-check-vs-independent-verification.md`
(channel @HumanitariansAI, Playlist: **Behind the Model** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`behind-the-model` matches the map's `behind-the-model` prefix directly —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K + deliver.py) in this same invocation.
