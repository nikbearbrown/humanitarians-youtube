# BUILD-LOG — behind-the-model--claude-liam-material-plan-change

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown sheet
(`anthropics/youtube/behind-the-model/claude-liam-material-plan-change/beat_sheet.json`,
9 beats + 3 unused BOOKEND placeholders, brand `claude-liam`, `@NikBearBrown`,
2 of 9 real beats filled — B01/B02/B03/B04 carried fully-written Teardown
narration, B05 was a short handoff line). Built entirely fresh this
invocation (only SUBJECT.json present on pickup).

Kept the question and every fact: agents adapt constantly (tool fails, file
missing, format unexpected) and adaptation itself is normal, not an error;
three small-feeling changes (extra file read, shared-folder output, library
install) are each a real scope expansion; the material-plan-change rule has
three triggers — different tool, new data, higher risk — and on any trigger
the agent stops before proceeding, not after; reporting a change after the
fact is an audit log, asking before it is supervision, only supervision can
still change what happens. Compressed the source's B01(adapt)/B02(small
changes) into B01's anchor-planting beat, B03(the rule)/B04(verdict) into
B03/B04's break+mechanism beats, and added a wrong-guess beat (B02: report
afterward is enough — falsified by the anchor's own case) and a
both-directions beat (B05: stopping for every small in-scope adaptation
defeats itself) per this factory's PHASE 1 six-move spine, since the
source's Teardown shape carried neither explicitly.

**Anchor B01→B06:** a five-step approved plan (pull invoices, merge, reformat,
save, post to drive), step three flagged with a format mismatch. Planted
with no split drawn; returns at B06 split into a before-path (paused, control
returned) and an after-path (already done, only reported).

B00 WRITER LAW: naive framing "when should it tell me **after** it changes
something?" corrected to "**before**" (the source's own before/after
distinction — reporting after vs. asking before). 33-word narration +
`lead_silence_s: 0.8`, measured 10.37s (clears the ≥9s TIMING LAW window
with margin); frame-verified at t=9s/t=10s that the full corrected question
("...before it changes something?") is legible well before the beat ends.

Build sequence:
1. `generate_audio_kokoro.py` — 10/10 beats, first pass, no retries
   (B00 10.37s, B01 19.52s, B02 6.93s, B03 16.04s, B04 12.20s, B05 11.99s,
   B06 14.89s, BCRY 9.54s, BHTF 19.33s, BOUT 4.89s).
2. `render_scenes.py` — 6 Manim GRAPHIC beats (B01–B06), clean first pass.
3. `remotion_scenes.py` — 4 REMOTION beats (B00/BCRY/BHTF/BOUT); auto-
   backgrounded past the tool's 120s foreground timeout, blocked on
   explicitly via `TaskOutput` per the ONE-SHOT/COMPLETION LAW rather than
   ending the turn — exit 0, all 4 confirmed rendered (`B00: extended to
   10.4s`).
4. `compile.py --height 2160` (no `--review`) — THE 4K LAW forced the clean
   master natively to 3840×2160. content-check/frame-check/lane-check all
   PASS, GATE AUDIO PASS mean_volume -23.9 dB.

**GATE T required two fix passes**, both against real defects plus three
verified false positives of already-documented classes:

- Real fixes: B05's leftmost "retry" card sat 8px outside the 90% title-safe
  box (manual `shift()` arithmetic didn't recenter correctly) — replaced with
  `.arrange(RIGHT, buff=0.35).move_to(...)` for guaranteed centering. B06's
  "PAUSED"/"DONE" badges and "BEFORE —"/"AFTER —" labels were sized at
  16px and then further scaled 0.46× (effective ~7px, both a min-size FAIL
  and a contrast-local FAIL from anti-aliased blending against their own
  card border) — rebuilt the badges as standalone elements at font_size 22
  (not nested inside the scaled-down plan-card group), and bumped the plan
  card's own step-list text via a new `step_font_size` param (40 pre-scale,
  ~22px effective after the 0.55× card scale) so every B06 text run clears
  the 20px floor with margin.
- Verified false positives (frame-pulled directly, not patched around):
  B02 kerning — the "TASK DONE" gate box → Arrow() → "REPORT" card sit at
  one y-band, so the checker's row-based kerning analysis reads the
  box-to-box arrow-shaft gap as one 349px inter-glyph gap; same mechanism as
  the `BDNB01Scene`/`BDNB05Scene`/`BDNB10Scene` precedents. B03/B05
  bbox-overlap — the "REPORTED" stamp (B03) and the "retry"/"read file" row
  cards (B05) are each a `SurroundingRectangle`/`RoundedRectangle` border
  whose bbox necessarily encloses its own centered label; same class as
  `IVPB01Scene`/`B03_HookMechanism` and ~20 other precedents. Registered
  `MPCB02Scene` in `KERNING_EXEMPT_PATTERNS` and `MPCB03Scene`/`MPCB05Scene`
  in `BBOX_OVERLAP_EXEMPT_PATTERNS` in `runtime/scripts/type_check.py`, each
  with a rationale comment and the exact frame timestamps read. GATE T:
  **PASS, 0 FAILs** after both passes.

Gate V: pulled the full contact sheet (`qc-sheet.png`) plus targeted frame
pulls for every beat that had a finding (B00 correction at t=9s/10s, B02 at
t=3s, B03 at t=6s/15s, B05 at t=9s, B06 before/after both v1 and v2) — all
legible, no overlap, safe inset respected, anchor pair (the five-step plan
card) visually identical at B01 and B06, Humanitarians AI skin correct
throughout (@HumanitariansAI, humanitarians palette, Fable 5 composer,
subscribe CTA).

**Gates:**
- content-check: PASS (10 beats, no violations)
- frame-check: PASS (3840×2160, 10 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after 2 fix passes — 2 real layout fixes + 3
  registered false-positive exemptions)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe independently reverified: 3840×2160, h264 + aac, duration
  126.703s; mp4 mtime (1788594526) newer than beat_sheet.json mtime
  (1788593746)

**Non-blocking warning (compile.py):** motion histogram graphic:6 remotion:4
— GRAPHIC at 60%, over the ~40% pantry-cap guideline in MOTION.md.
Structural for this shape: hai-simple's mandated B00 (writer) + BCRY + BHTF
(Your Turn) + BOUT (outro) are REMOTION by skill contract, against 6 GRAPHIC
body beats for this 10-beat reel (B01–B06) — same disposition as most
`behind-the-model--*` siblings at this beat count.

Metadata file written: `behind-the-model--claude-liam-material-plan-change.md`
(channel @HumanitariansAI, Playlist: **Behind the Model** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`behind-the-model` matches the map's `behind-the-model` prefix directly —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-05 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.

```
cp behind-the-model--claude-liam-material-plan-change.mp4 \
   behind-the-model--claude-liam-material-plan-change-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
