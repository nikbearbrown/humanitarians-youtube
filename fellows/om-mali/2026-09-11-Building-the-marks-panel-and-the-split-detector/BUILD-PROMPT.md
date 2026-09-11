# BUILD-PROMPT — building-the-marks-panel-and-the-split-detector

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-09-11-Building-the-marks-panel-and-the-split-detector

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata_week7.json is queried from the marks panel at build time by
   scripts/make_week7_figures.py and dumped before anything is drawn. Every on-screen number is
   a prop read from it by build_beat_sheet.py. Never type a number into a scene or beat sheet.
   The injection asserts, and MUST keep asserting:
       5806 - 28 - 72 == 5706 == coverage.lines_in_marks   # performed on screen at B02
       totals.marks == 5479
       blocks[] sums to totals.blocked == 301
       exactly ONE block reason is the confirmed split, holding 7 marks
       priced + unpriceable(294) == marks       # the 7 split marks are priced but held out
       tolerance == 0.01                        # RELATIVE, the rule that ships
       all 7 quarantine rows adjudicated, every note carries the reviewer's name
       3 distinct companies; BOTH verdicts present (split and not_a_split)
       the COM row: ratio 11.9300, factor 10.0000, and they DIFFER
       perplexity: shares x10, value_usd identical at "13488132.50" and still carrying decimals
       anthropic: ONE share count across 13 rows, and the step REVERSES next quarter
       spacex: constant shares, value exactly doubled
       checks: 7 total, 6 True, 0 False, 1 None — counted, never typed
       agreement.families == 10 == sum(clusters)

   THE ONE NUMBER NOT IN figdata: the OLD detector window, ±0.02. figdata carries only the rule
   that ships. The old value comes from narration_script.md / plan.md and is passed as the
   named constant OLD_WINDOW. B04's on-screen source line SAYS SO. Do not silently cite
   figdata for it, and do not delete the attribution — FACTCHECK row 9 is the whole point.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 9, 12, 18 and 20 first.
   - PEDAGOGY.md must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human what
     they are being asked to sign. Do not sign it. Do not pass --no-gate for a final.
   - CHECKS-REPORT.md must exist before the first compile.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then: python3 lock_durations.py beat_sheet.json vertical/beat_sheet.json
   which measures the mp3s with ffprobe and writes durationInSeconds into both sheets.
   Both cuts share the SAME mp3s. Never regenerate audio for the vertical cut.

3. RENDER — both orientations
   python3 runtime/scripts/remotion_scenes.py <reel>
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/MarksPanelAndSplitDetector.tsx and are registered in Root.tsx TWICE —
   once at 1920x1080 and once at 1080x1920 under the <pattern>916 name. Same component, same
   props; the component reads its orientation from useVideoConfig(). --scale=2 makes those
   3840x2160 and 2160x3840. Never hand-roll npx remotion render.

   NOTE: remotion_scenes.py loads the beat sheet at the START of a run and rewrites it at the
   END. Any edit to the sheet during a long render is silently lost. Re-run build_beat_sheet.py
   and lock_durations.py afterwards if you touched it — both are idempotent.

4. COMPILE
   ./art run   <reel>                          # slate cut, 16:9
   ./art final <reel>                          # clean master, 3840x2160
   ./art final <reel>/vertical --height 3840   # clean master, 2160x3840
   The vertical sheet carries "aspect_ratio": "9:16", which is what makes compile.py compute
   width 2160 from height 3840. Passing --height 2160 there would produce a 1215-wide file.

5. VERIFY BY LOOKING
   python3 runtime/qc/final_frame_check.py <reel>
   python3 runtime/qc/final_frame_check.py <reel>/vertical
   Then READ the PNGs in _qc/ yourself. The gate checks edge bleed, canvas fill and contrast —
   it does NOT check overlap, cannot tell whether a number on screen is the RIGHT number, and
   cannot tell whether a source line cites a file containing the claim. It has missed something
   in four of the six episodes in this series.

   Watch specifically:
   - B02 and B08 are the two densest frames. If the FootNote rule is drawn across the text
     above it, the column is over-full — remove a restated number, do not shrink the type.
   - B04's number line: the 11.93 mark MUST sit visibly outside the grey ±0.02 box. If it does
     not, the axis half-width (HALF = 0.25) has been changed and the beat no longer argues.
   - B03 and B05 are two DIFFERENT Perplexity securities (ARK common vs T. Rowe preferred).
     Both name their class on screen. Do not "simplify" that away.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never say the detector was broken. Too narrow. That is the README's own phrasing.
   - Never say the splits are adjusted. Detected, quarantined, decided. Week 8 divides.
   - Never use red as a warning colour. DESIGN.md: red is the primary series. In B07 it marks
     the CORRECT divisor, which is README correction 3 and the point of the figure.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `building-the-marks-panel-and-the-split-detector.mp4` | 3840×2160, 24fps, 214.9s |
| `vertical/building-the-marks-panel-and-the-split-detector-916.mp4` | 2160×3840, 24fps, 214.9s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
