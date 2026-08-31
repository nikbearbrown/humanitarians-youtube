# BUILD-PROMPT — measuring-a-local-llm-against-the-matcher

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/humanitarians-youtube/fellows/om-mali/2026-08-28-Measuring-a-local-LLM-against-the-matcher

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata_week5.json is generated from the run's cached model replies by
   scripts/make_week5_figures.py in the project repo. Every on-screen number is a prop read
   from it by build_beat_sheet.py. Never type a number into a scene or a beat sheet.
   The injection asserts, and MUST keep asserting:
       run.parameter_size == "8.0B"          # the claim is an 8B model
       throughput.calls_measured == 322 and errors == 0
       prompt_example.candidates == 11       # 7 universe + 4 watchlist, NOT 7
       micro fp: matcher 1 -> band 196
       band_changes: promotions == broke == 14, fixed == 1
       confidence.at_full == 315 and disagrees_at_95_plus == 12
       len(veto_rows) == 4 and exactly one vetoed
   Two of these exist because the PROSE was wrong until a generated figure disagreed with it
   (confidence was 315, not 308; candidates were 11, not 7). Keep every assertion.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 3, 9, 13 and 18 first — the 11 candidates, the
     micro-vs-macro record count, the ONE rebuttal that rests on author knowledge rather than
     an artifact (B04's parent-company claim), and the 12-of-15 confidence finding.
   - PEDAGOGY.md must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human what
     they are being asked to sign. Do not sign it. Do not pass --no-gate for a final.
   - CHECKS-REPORT.md must exist before the first compile.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then: python3 lock_durations.py beat_sheet.json vertical/beat_sheet.json
   which writes each measured actual_duration_s into shot.remotion.props.durationInSeconds.
   Both cuts share the SAME mp3s. Never regenerate audio for the vertical cut.

3. RENDER — both orientations
   python3 runtime/scripts/remotion_scenes.py <reel>
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/MeasuringLocalLlm.tsx and are registered in Root.tsx TWICE — once at
   1920x1080 and once at 1080x1920 under the <pattern>916 name. Same component, same props;
   the component reads its orientation from useVideoConfig(). --scale=2 makes those 3840x2160
   and 2160x3840. Never hand-roll npx remotion render.

   The 9:16 cut is a RE-LAYOUT, not a crop. If a portrait beat looks like a squeezed landscape
   frame, fix the component's f(landscape, portrait) values — do not centre-cut.

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
   it does NOT check text-on-text overlap, and has missed a collision in two of the four
   episodes in this series. Frames are the evidence; a clean report is not.

   Watch specifically:
   - B06's twelve character slots must not wrap in portrait (12 slots x 62px + gaps < 972).
   - B08's holding names are already shortened at the exposure clause; if you re-lengthen them
     they will cross the right title-safe edge, which is the exact BLOCKER week 4 hit.
   - B07's 322-dot grid is 26 columns landscape, 16 portrait. If it overflows, change the
     column count, not the dot size.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never quote the hardest-cases 100%. It is true and misleading at once; FACTCHECK.md
     explains why, and it stays off screen.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `measuring-a-local-llm-against-the-matcher.mp4` | 3840×2160, 24fps, 215.5s |
| `vertical/measuring-a-local-llm-against-the-matcher.mp4` | 2160×3840, 24fps, 215.5s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
