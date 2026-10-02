# BUILD-PROMPT — joining-filed-rounds-to-fund-entry-dates

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-09-25-Joining-filed-rounds-to-fund-entry-dates

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata_week9.json is queried from the project database at build time by
   scripts/make_week9_figures.py and dumped before anything is drawn. Every on-screen number is
   a prop read from it by build_beat_sheet.py. Never type a number into a scene or beat sheet.
   The injection asserts, and MUST keep asserting:
       form_d: quarters_scanned == 49, rows == 706
       by_class: pooled 595 + candidate 111 == 706, and 595/706 == 0.8428
       pooled_rows > candidate_rows * 5          <- the FRAMING assertion, see below
       lots 249, position_cost 227, fund_cost 22, and 227 + 22 == 249
       exactly ONE filer has fund_cost > 0 and position_cost == 0
       entry_vs_mark: 7 rows, of which exactly 3 have first_entry < first_mark
       earliest first_entry == "2015-01-20"
       corroboration: dates_in_window 18, hits["0"] 10, and the 18 pairs[] rows
         contain exactly 10 with gap_days == 0
       the Databricks row: gap_days 0, registrants 5   (asserted by company+date, not index)
       dates_outside_window sums to 12, and 10 / (18 + 12) == 0.3333
       exposure: 90 rows, 30 managers, 10 companies

   THE FRAMING ASSERTION IS THE LOAD-BEARING ONE. B02's whole claim is that a name scan is
   overwhelmingly wrong, and B03 derives the join key from that. If a future data change made
   feeders merely a plurality, the build MUST fail rather than ship a beat whose framing had
   quietly gone stale.

   THREE VALUES ARE NOT IN figdata_week9.json. They come from narration_script.md and the
   filings behind it, are passed as named constants at the top of build_beat_sheet.py, and each
   beat that uses one SAYS SO in its on-screen source line:
       XAI_COLLISION   the 2014 filer that normalises to the same string as X.AI   (B03)
       LAYOUT_COUNT    four tables, one with no table, a sixth that needed no code (B04)
       DBX_ROUND_USD   the $400M Databricks reported selling in October 2019       (B07)
   Never move one of these into a string, and never let a beat cite figdata_week9.json for it.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 6, 9, 14 and 19 first. Row 6 is load-bearing — it is the
     evidence that no better string normalisation would have fixed the join.
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
   runtime/remotion/src/JoiningFiledRounds.tsx, registered in Root.tsx TWICE — 1920x1080 and
   1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.

   NOTE: remotion_scenes.py loads the beat sheet at the START of a run and rewrites it at the
   END. Any edit during a long render is silently lost. Re-run build_beat_sheet.py and
   lock_durations.py afterwards if you touched it — both are idempotent.

   NEVER name a scene prop `key`. React strips a prop called `key` before it reaches the
   component, so W9Bluf's join-key chip rendered as an empty outline with no error anywhere —
   not from tsc, not from the schema, not from GATE V. The prop is `joinKey`.

4. COMPILE
   ./art run   <reel>                          # slate cut, 16:9
   ./art final <reel>                          # clean master, 3840x2160
   ./art final <reel>/vertical --height 3840   # clean master, 2160x3840
   The vertical sheet carries "aspect_ratio": "9:16"; --height 2160 there would give 1215 wide.

5. VERIFY BY LOOKING
   python3 runtime/qc/final_frame_check.py <reel>
   python3 runtime/qc/final_frame_check.py <reel>/vertical
   Then READ the PNGs in _qc/ yourself. The gate checks edge bleed, canvas fill and contrast —
   it does NOT check overlap, cannot tell whether a number is the RIGHT number, cannot tell
   whether a source line cites a file containing the claim, and cannot tell whether a caption
   describes the chart beneath it. It has missed something in six of the eight episodes so far.

   Watch specifically:
   - B06 is the collision-prone beat, and it exists in this form because of a collision. The
     source figure truncated manager names into the next column — "Robinhood Ventures Fund" ran
     into "Databricks". The auditor does NOT catch that, because the two are separate text
     elements sharing a baseline rather than overlapping boxes. Read the frame.
   - B05 places seven companies on a shared calendar axis with two dated points each. Labels
     collide when two companies share a year. Re-read it if you touch the plot height.
   - B02 and B04 both draw bars and must not read as the same slide. B02 is ONE bar splitting;
     B04 is ten filers ranked. If B04 starts reading as a proportion, change its ordering cue,
     not its colour.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never call the 84% a data-quality note. It is the reason the join key is what it is.
   - Never say the corroboration shows funds participated in those rounds. It is agreement
     between two filings that do not cite each other, and B07 states the competing reading.
   - Never drop B08. The reel restating its own headline as 33% is the point of the episode.
   - Never let "227 with a cost" stand alone. The other 22 are one filer's, at fund level.
   - Never say all seven companies reach back before the panel. Three do; B05 says why.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `joining-filed-rounds-to-fund-entry-dates.mp4` | 3840×2160, 24fps, 217.45s |
| `vertical/joining-filed-rounds-to-fund-entry-dates-916.mp4` | 2160×3840, 24fps, 217.45s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
