# BUILD-LOG — financial-services--claude-liam-deal-tracker

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/financial-services/youtube/claude-liam-deal-tracker/beat_sheet.json`,
7 beats, investment-banking vertical plugin's `deal-tracker` Anthropic
skill, brand `claude-liam`, `@NikBearBrown`). The source's `source_skill`
pointed at Bear's other machine (`/Users/bear/Documents/CoWork/...`); no
local copy of the skill's actual SKILL.md exists in this tree, so the
source `beat_sheet.json` narration (the fully locked script) served as the
complete fact source — it already states the skill's job description,
triggers, pipeline mechanism, and design-tell verbatim.

Kept beat count (7) and every fact: deal-tracker's job, verbatim from the
source — "track multiple live deals with milestones, deadlines, action
items, and status updates; maintain a deal pipeline view; surface upcoming
deadlines and overdue items"; the six exact trigger phrases ("deal
tracker", "deal status", "where are we on", "process update", "deal
pipeline", "weekly deal review"); the Steps section runs linearly, no
branching unless a step says so; same input → same output every run; the
limit is symmetric — anything outside the written spec isn't handled.
Remapped the source's B03/BVDT Teardown "gets right / bites" framing into
this reel's B03 both-directions beat (reliable inside the spec, unhandled
outside it — same facts, no verdict), and its BVDT verdict recap into a
single BCRY carry-out sentence per CARRY-OUT LAW. Anchor B02→B03: invented
a concrete "ACME · Series C" deal card (not in the source, which never
gives a worked example) to make the reliable/unhandled split visualizable —
planted with the card moving through three steps and an OVERDUE flag
lighting up on step three (within spec), paid off with the same card asked
something the six trigger phrases never cover and staying inert (outside
spec, no fallback, no guess).

B00 WRITER LAW: naive guess "smart" (assistant that already knows the
pipeline) → corrected to "scripted" (the actual misconception — deal-tracker
doesn't reason about deals, it executes a written spec); 30-word narration +
`lead_silence_s: 0.8`, measured 9.77s (clears the TIMING LAW ≥9s window).
Verified on frame pulls at 6s and 12s that the correction ("smart" →
"scripted") lands well before the beat ends and the final question ("so
what does it actually do?") is fully typed and readable.

Built from scratch this invocation — no prior artifacts found in the reel
dir (only SUBJECT.json existed at start):

1. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json, scenes.py
   (3 custom Manim scenes: `DTB01Scene`, `DTB02Scene`, `DTB03Scene`),
   render_scenes.py — following the beat-for-beat pattern of the prior
   `claude-code--claude-liam-plugin-structure` redo (same source shape:
   7-beat skill-teardown sheet, all-REMOTION source beats, no AI-video/
   pantry substitution needed beyond the WRITER LAW swap).
2. `generate_audio_kokoro.py` — 7/7 beats, am_onyx, $0.00. B00 9.77s, B01
   13.72s, B02 11.46s, B03 13.99s, BCRY 6.81s, BHTF 20.59s, BOUT 3.07s.
3. `render_scenes.py` (Manim, foreground) — B01/B02/B03 rendered clean.
4. `remotion_scenes.py` (foreground) — first invocation hit the 2-minute
   tool timeout after B00 finished; re-ran in the foreground with a longer
   timeout per the ONE-SHOT/no-background-render rule, which completed
   BCRY, BHTF, BOUT (`extended to Ns` — Remotion clips stretched to match
   measured audio).
5. `compile.py` — 7/7 slots filled, content-check/frame-check/lane-check
   PASS, GATE AUDIO PASS mean_volume -24.0 dB. THE 4K LAW forced the clean
   master natively to 3840×2160 (no `--review` flag used).
6. Gate V (first pass): pulled 13 frames at 6s spacing plus one at 78s.
   Found a real overlap defect in B03 — the "draft the counterparty's
   redline" request bubble collided with the step-box row above it,
   clipping "step 1" and "step 3" text. Fixed by repositioning the steps
   row higher (UP*2.1) and the deal card / bubble lower with a computed
   gap (bubble at UP*0.1, deal at DOWN*1.9) so no two elements' bounding
   boxes overlap. Re-rendered B03, recompiled — confirmed clean on a
   frame pull.
7. GATE T (`type_check.py`): first pass **FAIL** — 2 pixel beats, B02 and
   B03 had caption text at 15-16px, under the 20px (1.9% of 1080p) floor
   (the deal card's "Term sheet — due Fri" line at font_size 16, the
   OVERDUE flag and request-bubble text at font_size 18). Bumped all four
   to font_size 22 (matching B01's already-passing size) and widened the
   deal/flag/bubble cards to avoid new overflow from the larger text.
   Re-rendered B02/B03, recompiled, reran GATE T: **PASS, 0 FAILs**.
8. Gate V (second pass): pulled fresh frames of B02 (32s) and B03 (46s) —
   both read cleanly at the new sizes, no overflow, no overlap.
9. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788289339) newer than
   beat_sheet.json mtime (1788288897); h264 3840×2160 + aac streams
   present, duration 80.42s; `ffmpeg -af volumedetect` mean_volume
   **-24.0 dB**, max -2.9 dB — independently confirms GATE AUDIO.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, second pass — fixed 2 pixel-floor beats)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: duration 80.42s; mp4 mtime newer than beat_sheet.json mtime
- Gate V: two passes, one real defect found and fixed (B03 bbox overlap),
  clean on the second pass across all 7 beats

Metadata file written: `financial-services--claude-liam-deal-tracker.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`financial-services` matches no prefix in the map, so per the fallback
rule the `hai-simple` skill name itself was matched against the map, which
does contain a `hai-simple` key → `Claude Basics` — plus the direct code
link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
