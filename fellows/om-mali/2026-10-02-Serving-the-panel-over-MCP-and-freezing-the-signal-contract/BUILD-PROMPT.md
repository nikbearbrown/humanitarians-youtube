# BUILD-PROMPT — serving-the-panel-over-mcp-and-freezing-the-signal-contract

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-10-02-Serving-the-panel-over-MCP-and-freezing-the-signal-contract

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json is queried from the live database and the live signal at figure-build time by
   scripts/make_week1011_figures.py. signal_example.json is a real emitted signal and is READ
   DIRECTLY by build_beat_sheet.py — B05's key list is the file's own key list, not a copy.
   Never type a number into a scene or a beat sheet. The injection asserts, and MUST keep
   asserting:
       six tools; rows_returned <= rows_total for all of them
       get_marks: 2,151 rows, 50 returned == limits.default_limit
                  575,299 chars -> 17,976, a 96.9% cut
       COSTLIER == 5 and CHEAPER == 1, and the one that saves IS get_marks   <- FRAMING
       0.18 < overhead_lo < overhead_hi < 0.50   (B03 shows "+19% to +49%")
       exactly one tool paged (get_marks); exactly one returned zero rows (list_unresolved)
       limits.max_response_chars == 48000, and the bounded page is UNDER it
       schema_version "1.0" in BOTH figdata and the emitted file
       top_level_keys == len(signal_example.json keys) == 9
       forbidden_fields == 10, and NONE of them appears in the emitted file
       not_supported == len(suppressed) == len(file's not_supported) == 4
       list_companies rows_total 11 − signal.companies 10 == 1
       guards[] has 3 rows, all caught, incl. the invented-ranking draft found BY ITS TEXT
       commentary_words == 388

   THE FRAMING ASSERTION IS `COSTLIER == 5`. B03's whole claim is that the bounding envelope is
   not free. If a future measurement made bounding a pure win, the build MUST fail rather than
   ship a beat whose arithmetic still holds while its framing has gone stale.

   ONE ASSERTION CHECKS THE ARTIFACT, NOT THE FIGURE: the ten refused field names are asserted
   ABSENT from signal_example.json, so B05's frame carries the result of a check rather than a
   restatement of a claim. Keep it that way.

   THREE VALUES ARE NOT IN figdata.json. They come from README.md and narration_script.md, are
   passed as named constants, and each beat that uses one SAYS SO on screen:
       FOURTH_GUARD  the length check — figdata has THREE guards and w11-guards.png is
                     titled "Three guards"; the script says four. The fourth postdates the
                     figure, which is why B07 draws it below a dashed rule.
       LATE_MISSES   the empty note accepted as a success; the spelled-out number
       SETUP_BUGS    the three client-side registration defects
   Never move one of these into a string, and never let a beat cite figdata.json for it.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 6, 12, 15 and 18 first. Row 12 is load-bearing — the
     figure says three guards and the reel says four.
   - PEDAGOGY.md must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human what
     they are being asked to sign. Do not sign it. Do not pass --no-gate for a final.
   - CHECKS-REPORT.md must exist before the first compile.
   - Six FACTCHECK rows (2, 3, 9, 14, 15, 17) were verified against the LIVE MCP server. If the
     server is running, re-verify them; if it is not, they fall back to REPRODUCIBLE.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then: python3 lock_durations.py beat_sheet.json vertical/beat_sheet.json
   Both cuts share the SAME mp3s. Never regenerate audio for the vertical cut.

3. RENDER — both orientations
   python3 runtime/scripts/remotion_scenes.py <reel>
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/ServingThePanelOverMcp.tsx, registered in Root.tsx TWICE — 1920x1080
   and 1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.

   WATCH THE UNKNOWN-PROP WARNING. remotion_scenes.py now prints, before rendering:
       [remotion] WARN <beat>: <Pattern> has no prop(s) named ... — zod will DROP them and
       render this beat with that field's DEFAULT text.
   Do not render through it. This exact failure put another project's copy on B09 and B11 of a
   4K review cut: ClaudeVerdictArtifact wants artifactTitle/artifactHeading/artifactLines, and
   ClaudeTitleOutro wants `subline`, not `subtitle`. A legacy `sparkLine` warning on
   ClaudeVerdictArtifact is expected and harmless — weeks 1-9 all pass it.

   NOTE: remotion_scenes.py loads the beat sheet at the START of a run and rewrites it at the
   END. Any edit during a long render is silently lost. Re-run build_beat_sheet.py and
   lock_durations.py afterwards if you touched it — both are idempotent.

4. COMPILE
   ./art run   <reel>                          # slate cut + clean master, 3840x2160
   ./art run   <reel>/vertical --height 3840   # slate cut + clean master, 2160x3840
   The vertical sheet carries "aspect_ratio": "9:16"; --height 2160 there would give 1215 wide.

5. VERIFY BY LOOKING
   python3 runtime/qc/final_frame_check.py <reel> --mp4 <the exact master you are shipping>
   python3 runtime/qc/final_frame_check.py <reel>/vertical --mp4 <the 916 master>
   PASS --mp4 EXPLICITLY. With two cuts in a folder the gate picks the first non-slate match,
   which is not necessarily the file you are delivering.

   Then READ the PNGs in _qc/ yourself. The gate checks edge bleed, canvas fill and contrast —
   it does NOT check overlap, cannot tell whether a number is the RIGHT number, cannot tell
   whether a source line cites a file containing the claim, cannot tell whether a caption
   describes the chart beneath it, cannot tell an empty element from an intentional one, and
   CANNOT TELL WHOSE WORDS ARE ON THE FRAME. It has missed something in seven of the nine
   episodes in this series.

   Watch specifically:
   - B02's figures sit BELOW the bar, never beside it. Beside the full-width bar they run off
     the right edge of the safe area.
   - B02's token figure carries ONE DECIMAL. 575,299/4 rounds to "144k" at whole thousands,
     and the narration says "a hundred and forty three thousand".
   - B03's before/after column is EXACT below 100k. "2k -> 3k" beside "+34%" implies +50%.
   - B03's saving row is pinned to full width and the frame says so. A 97% saving and a 49%
     cost cannot share a linear scale without the costs vanishing.
   - Portrait B02/B03/B07 were rescaled after the first portrait read. Re-read them if you
     touch any f(landscape, portrait) value.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never present bounding as a pure win. It costs on five of the six tools.
   - Never call the server's read-only surface a limitation. A resolution decision needs a
     named human; that is the reason, not a consequence.
   - Never drop B06. Two of this reel's own numbers disagree, and a viewer who notices and is
     not told would be right to distrust the rest.
   - Never show four guards of equal provenance. The fourth postdates its own figure.
   - Never drop the "what none of this shows" block: no company valuation, not timely, and the
     model's prose is labelled output rather than a verified claim.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_02_10_2026.mp4` | 3840×2160, 24fps, 211.96s |
| `vertical/serving-the-panel-over-mcp-and-freezing-the-signal-contract-916.mp4` | 2160×3840, 24fps, 211.96s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
