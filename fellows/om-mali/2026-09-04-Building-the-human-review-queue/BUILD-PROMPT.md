# BUILD-PROMPT — building-the-human-review-queue

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-09-04-Building-the-human-review-queue

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata_week6.json is queried from the project's Postgres at build time by
   scripts/make_week6_figures.py and dumped before anything is drawn. Every on-screen number
   is a prop read from it by build_beat_sheet.py. Never type a number into a scene or a beat
   sheet. The injection asserts, and MUST keep asserting:
       holdings == decided == 5806          # nothing dropped, nothing pending
       auto 4537 + human 1269 == 5806
       len(review_groups) == 8, cards == 42 # the collapse IS the beat
       review_rows == 45                    # decisions, each with a name and a reason
       len(xai_spellings) == 24, holdings 278
       duplicate issuer names EXIST in xai_spellings  # so the titles cannot be dropped
       len(split questions) == 3            # NOT four
       perplexity: balance x10, value_usd identical at 4228993.75 (to the cent)
       spacex_same_day: EC and EP on the SAME period_end
       rejected holdings == 28              # the canary
   Three of these exist because the PROSE was wrong until the figures were generated: four
   split questions instead of three, Perplexity's value rounded to the dollar, and the X.AI
   list missing the titles that separate three otherwise-identical rows. Keep every assertion.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 6, 12, 18 and 19 first — the "code rejects a decision
     missing a name or a reason" claim (author-asserted, and the project's central claim), the
     accidental crash test (n=1), the corrected three-not-four split count, and the canary.
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
   runtime/remotion/src/BuildingTheHumanReviewQueue.tsx and are registered in Root.tsx TWICE —
   once at 1920x1080 and once at 1080x1920 under the <pattern>916 name. Same component, same
   props; the component reads its orientation from useVideoConfig(). --scale=2 makes those
   3840x2160 and 2160x3840. Never hand-roll npx remotion render.

   The 9:16 cut is a RE-LAYOUT, not a crop. If a portrait beat looks like a squeezed landscape
   frame, fix the component's f(landscape, portrait) values — do not centre-cut.

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
   it does NOT check text-on-text overlap and cannot tell whether a number on screen is the
   RIGHT number. It has missed something in three of the five episodes in this series.

   Watch specifically:
   - B03's 24-row scroller: the window is 9 rows landscape, 11 portrait. Long HOF CAPITAL /
     MVP OPPORTUNITY strings are ellipsised by design — check they still read.
   - B04 renders 24 + 24 + 1 cells. If they wrap badly in portrait, change the cell size, not
     the count.
   - B06 draws 42 marks twice. Both blocks must show the SAME number; that is the beat.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never say the software decided anything. It routed, grouped and presented. That is the
     README's "one thing not to get wrong on camera" and it is beat B01's entire structure.
   - Never quote the crash as a durability guarantee. One unplanned outage, run by accident.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `building-the-human-review-queue.mp4` | 3840×2160, 24fps, 199.7s |
| `vertical/building-the-human-review-queue-916.mp4` | 2160×3840, 24fps, 199.7s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
