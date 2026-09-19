# BUILD-PROMPT — measuring-how-private-marks-move-and-propagate

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-09-18-Measuring-how-private-marks-move-and-propagate

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata_week8.json is queried from the marks panel at build time by
   scripts/make_week8_figures.py and dumped before anything is drawn. Every on-screen number is
   a prop read from it by build_beat_sheet.py. Never type a number into a scene or beat sheet.
   The injection asserts, and MUST keep asserting:
       guards.marks == 5479; unadjudicated_splits == 0; incomplete_runs == 0
       steps 4079 + first_observation 1099 == marks 5178 == 5479 − change_blocked 301
       remark.overall: unchanged 1019 / steps 4079 == 0.2498, and moved + unchanged == steps
       ALL THREE widenings < 0.30 AND monotonically increasing
       by_company: 10 rows whose steps sum to 4079; floor 0.0%, ceiling X.AI 48.5%
       same_date_stats: groups 130, median 0.1082, multi_level 92 == len(transition)
       steady 38 + transition 92 == 130; p90 == 0.405 (measured, not a round number)
       window: 11 rows, 8 distinct managers, 2 period ends, 140.9676 → 261.5705
       window levels: >= 2 clusters, and the LAST holds more marks than the first
       propagation: 37 events, median 30, max 92, 15 at zero days
       AND: (small events at zero days) / 28  >  (big events at zero days) / 9

   THE WIDENING ASSERTION IS THE LOAD-BEARING ONE. B02's whole claim is that 25% is a result
   rather than a threshold choice. If a future data change pushed any widened definition into
   the plan's 30–40% band, the build MUST fail rather than ship a quieter version of that beat.

   THE LAST ASSERTION protects a deleted claim. The figure once said "the biggest events are
   the fastest"; the data says the smaller ones reach the same period end more often. Keep it.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 6, 9, 18 and 20 first. Row 6 is the only load-bearing
     value that is a prior rather than a measurement.
   - PEDAGOGY.md must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human what
     they are being asked to sign. Do not sign it. Do not pass --no-gate for a final.
   - CHECKS-REPORT.md must exist before the first compile.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then: python3 lock_durations.py beat_sheet.json vertical/beat_sheet.json
   Both cuts share the SAME mp3s. Never regenerate audio for the vertical cut.

3. RENDER — both orientations
   python3 runtime/scripts/remotion_scenes.py <reel>
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/MarksMoveAndPropagate.tsx, registered in Root.tsx TWICE — 1920x1080 and
   1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.

   NOTE: remotion_scenes.py loads the beat sheet at the START of a run and rewrites it at the
   END. Any edit during a long render is silently lost. Re-run build_beat_sheet.py and
   lock_durations.py afterwards if you touched it — both are idempotent.

4. COMPILE
   ./art run   <reel>                          # slate cut, 16:9
   ./art final <reel>                          # clean master, 3840x2160
   ./art final <reel>/vertical --height 3840   # clean master, 2160x3840
   The vertical sheet carries "aspect_ratio": "9:16"; --height 2160 there would give 1215 wide.

5. VERIFY BY LOOKING
   python3 runtime/qc/final_frame_check.py <reel>
   python3 runtime/qc/final_frame_check.py <reel>/vertical
   Then READ the PNGs in _qc/ yourself. The gate checks edge bleed, canvas fill and contrast —
   it does NOT check overlap, cannot tell whether a number is the RIGHT number, and cannot tell
   whether a source line cites a file containing the claim. It has missed something in five of
   the seven episodes in this series.

   Watch specifically:
   - B05 is the collision-prone beat. Four managers price at $259.1364 on the same date, so
     their dots and labels land on the same y. The component FANS dots that share a y and
     pushes labels down to a minimum gap with a leader line. If you change the plot height or
     the label size, re-read that frame before shipping.
   - B03 draws the panel-wide rate as a rule ACROSS the bars. The bar sits in a fixed-width
     track and the pct/steps labels sit after it — that is what keeps the rule off the labels.
     Do not let the labels flow from the bar's own width again.
   - B04 and B06 share the DotField primitive on purpose. B06's argument is the stack at zero;
     if it stops reading as a stack, change the dot size, not the axis.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never say "disagreement" where the measurement supports "different prices on the same
     date". B05 exists because that distinction is the README's own warning.
   - Never present a propagation lag as diligence. The reporting calendar sets the floor.
   - Never drop the "what none of this shows" block. These are fund marks, not transactions.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `measuring-how-private-marks-move-and-propagate.mp4` | 3840×2160, 24fps, 225.5s |
| `vertical/measuring-how-private-marks-move-and-propagate-916.mp4` | 2160×3840, 24fps, 225.5s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
