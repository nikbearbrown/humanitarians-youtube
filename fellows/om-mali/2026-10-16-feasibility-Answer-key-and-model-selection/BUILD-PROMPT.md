# BUILD-PROMPT — grounding-an-ai-debt-tracker-in-real-sec-filings

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-10-16-feasibility-Answer-key-and-model-selection

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json transcribes the author's own saved results, as published in pantry/*.svg
   (adt-w0-borrowing, adt-w0-feasibility, adt-w1-levels, adt-w1-bakeoff) and in
   narration_script.md's source table. Every on-screen number is a prop read from it by
   build_beat_sheet.py. Never type a number into a scene or a beat sheet. The injection
   asserts, and MUST keep asserting:
       issuance:   121 / 28 rounds to the stored 4.3x — the multiple is DERIVED, never stated
       levels[]:   3 levels summing to universe.ai == 25          <- a partition that leaks
                                                                     is not a partition
                   bond-by-bond 15 < assumed 21                   <- FRAMING
                   gate: 14 qualified + 1 on the tie == 15
       cases:      95 + 400 == 495, and the held-back set is the LARGER one
       matching:   594/636 == 0.934 > line 0.90
                   all_quarters_share 0.85 < 0.934                <- the caveat only means
                                                                     something while this holds
       spike:      56/64 == 0.875 > 0.80 ; 21/46 > 0.30 ; raw 33 > conservative 21
       bakeoff:    one denominator (143) for all three models
                   the WINNER IS THE SMALLEST and beats both outright     <- SECOND ARGUMENT
                   all three clear the 0.85 line (that is why ONE rule is drawn, not three)
                   0.95 before corrections < 0.99 after

   THE FRAMING ASSERTION IS `MEASURED_BY_BOND < ASSUMED`. B05's whole claim is "fifteen, not
   twenty-one". 21 counted companies whose instruments carried a tag; 15 measures how much of
   each company's debt its report actually itemises. If a data change ever made those equal,
   the beat would be arguing about nothing and the build MUST fail rather than ship it.

   FIVE VALUES ARE NOT IN figdata.json. They come from narration_script.md and the project
   documents, are passed as named constants, and each beat that uses one SAYS SO on screen:
       MYCROFT_RECIPES  ~99 recipes, none on debt or credit                       (B01)
       PIPELINE         the four designed stages — DESIGN.md, not a measurement   (B02)
       PIT_SERVER       what the point-in-time server refuses, and that it exists (B03)
       COARSE_EXAMPLES  Microsoft's 13 batches, Oracle's partial 10-Qs            (B05)

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 4, 7, 9, 12, 15 and 18 first. Row 15 is the framing
     assertion; row 4 is the one the whole reel can get wrong by implication.
   - PEDAGOGY.md must carry "VERDICT: PASS" ON ITS OWN LINE. If it says PENDING, STOP and
     tell the human what they are being asked to sign. Do not sign it. Do not pass --no-gate.
     NEVER write the phrase "VERDICT: PASS" anywhere else in that file — not in a placeholder,
     not in an instruction, not in a quotation. Until 2026-10-18 the gate searched the whole
     file for the substring and this reel's own PENDING template opened it. The gate now
     matches a line, but a document that argues with its own gate is still a bad document.
   - CHECKS-REPORT.md must exist before the first compile.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then: python3 lock_durations.py beat_sheet.json
         python3 make_vertical.py          # rewires to 916 AND copies the same mp3s across
   Both cuts share the SAME mp3s. Never regenerate audio for the vertical cut.

   make_vertical.py matches the REGISTRATION TUPLE SHAPE in Root.tsx, not a naming
   convention. Two earlier versions hardcoded `W<digits>` ids and refused whole reels whose
   916 compositions were present. Do not "simplify" that regex back.

3. RENDER — both orientations
   python3 runtime/scripts/remotion_scenes.py <reel>
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/GroundingTheDebtTracker.tsx, registered in Root.tsx TWICE —
   1920x1080 and 1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and
   2160x3840.

   That file imports nothing from AiDebtTracker.tsx or the week 1-11 reel files, by series
   convention: every earlier signed master stays re-renderable byte-identically.

   WATCH THE UNKNOWN-PROP WARNING. remotion_scenes.py prints, before rendering:
       [remotion] WARN <beat>: <Pattern> has no prop(s) named ... — zod will DROP them and
       render this beat with that field's DEFAULT text.
   Do not render through it. A legacy `sparkLine` warning on ClaudeVerdictArtifact is
   expected. ClaudeVerdictArtifact's props are artifactTitle / artifactHeading /
   artifactLines, and ClaudeTitleOutro's is subline — not title / heading / lines / subtitle.

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

   Then READ the PNGs in _qc/ yourself. The gate checks edge bleed, canvas fill and contrast.
   It does NOT check overlap, cannot tell whether a number is the RIGHT number, cannot tell
   whether a source line cites a file containing the claim, cannot tell whether a caption
   describes the chart beneath it, cannot tell an empty element from an intentional one,
   cannot tell whose words are on the frame, and cannot tell whether a bar measures the thing
   the beat is about. It has missed something in eight of the twelve episodes to date.

   Watch specifically:
   - B01's value sits BESIDE its bar and needs its OWN fixed column. Reserving only the label
     width bled "$121bn" past the title-safe right edge the first time this figure was built.
   - B05 is ONE row of 25, partitioned, with the assumed 21 drawn as an outline OVER it. If
     anyone turns it back into three bars, the beat becomes a comparison of 15 against 4
     against 6, which is not what it is about.
   - B07's pass line is ONE rule drawn through all three tracks. Check at 4K that the three
     segments align and that it is not read as a bar edge.
   - Portrait beats rescaled after the first portrait read are listed in BUILD-LOG.md.
     Re-read them if you touch any f(landscape, portrait) value.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never say the agent exists. Week 1 built the ground under it, not the agent.
   - Never round 87.5% to "nearly ninety". On the wider denominator it is 76.7%, under the line.
   - Never say carry-forward is wrong "half the time" without the 21-of-46 fraction beside it.
   - Never give 93.4% without "from one report to the next" and the 85% across all quarters.
   - Never present the bake-off as a benchmark. 29 documents, one plain prompt, six corrections.
   - Never drop B08. The reel ends on its own limits, as every episode in this series does.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_16_10_2026.mp4` | 3840×2160, 24fps, 213.74s |
| `vertical/grounding-an-ai-debt-tracker-in-real-sec-filings-916.mp4` | 2160×3840, 24fps, 213.74s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
