# BUILD-PROMPT — running-full-episodes-from-filings-to-ledger

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-11-13-Running-full-episodes-from-filings-to-ledger

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json transcribes the author's own saved results as published in pantry/*.svg
   (adt-w5-graph, adt-w5-episodes, adt-w5-additions, adt-w5-fresh) and in
   narration_script.md's source table and notes. Every bar's geometry in those SVGs was
   recomputed as a ratio and had to agree with its printed fraction before the value was
   accepted. Every on-screen number is a prop read from figdata.json by
   build_beat_sheet.py. Never type a number into a scene or a beat sheet. The injection
   asserts, and MUST keep asserting:
       episodes:  recall tracker > recall B0                  <- FRAMING, half one
                  precision tracker < precision B0            <- FRAMING, half two
                  45 quarters, both sides from the SAME opening ledger
       new bonds: B0 caught == 0                              <- SECOND
                  0 < tracker caught < issued  (30 of 34, not all of them)
       additions: 40 real + 26 wrong == 66, five segments, summing both ways  <- THIRD
                  3 kinds carry ids (P56-P58); the 2 misreads carry NONE
       timing:    first-run precision < fixed-run precision   <- FOURTH
                  fixed-run precision IS the precision every other beat quotes
       fresh:     triage 15/15 >= 0.95 AND last week's 8/9 < 0.95   <- FIFTH
                  B2 share > reader share > B1 share (96% / 91% / 74%)
                  key agreed < gradable < drawn  (3 < 4 < 5)
       graph:     174 read + 71 reused == 245 kept; 95 of 95 episodes ran

   THE FRAMING ASSERTION IS A TRADE, HELD IN BOTH DIRECTIONS. Recall must rise against the
   do-nothing baseline AND precision must fall. The whole reel is built on the exchange:
   reading the filings is the only way to see a new bond, and a system that adds things
   will add some wrong ones. If either half ever stopped being true the build MUST fail,
   because this would be a different episode.

   THREE CLAIMS ARE NOT MEASURED in figdata.json. They are named constants, and each beat
   that uses one SAYS SO on screen:
       GATE_RECORD    the week is DELEGATED, not CLEARED; no person reviewed it (B00/B08/B09)
       LABELLER       the labels, truth and the diagnosis of the 26 are a model judgment
                      (B05/B08)
       ORACLE_START   every quarter began from the answer key's ledger, deliberately
                      (B02/B03/B08)

   NO DEFECT ID IS INVENTED. FRICTIONAL.md gives P53-P58, P44, P47 and P48, and gives none
   for the two plain misreads among the 26 additions. Do not supply them.

   NEVER SAY THE TRACKER READS THE OPENING LEDGER. It was borrowed from the answer key;
   reading it is week 6. narration_script.md says this explicitly.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 29 rows. Read rows 3, 4, 5, 7, 9, 12, 14, 18, 21 and 25 first. Row 4 is
     the framing assertion; rows 5 and 12 are the two claims most likely to be over-read.
   - PEDAGOGY.md must carry a signed verdict line. If it says PENDING, STOP and tell the human
     what they are being asked to sign. Do not sign it. Do not pass --no-gate.
     NEVER write the signed-verdict phrase anywhere else in that file — not in a placeholder,
     not in an instruction, not in a quotation. The audio gate matches a verdict LINE, but a
     document that argues with its own gate is still a bad document.
   - CHECKS-REPORT.md must exist before the first compile.
   - Do NOT touch README.md or FRICTIONAL.md. Both are the author's, written before this
     build, and the figure-to-beat map lives in BUILD-LOG.md instead.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then: python3 lock_durations.py beat_sheet.json
         python3 make_vertical.py          # rewires to 916 AND copies the same mp3s across
   Both cuts share the SAME mp3s. Never regenerate audio for the vertical cut.

   make_vertical.py matches the REGISTRATION TUPLE SHAPE in Root.tsx, not a naming
   convention. Do not "simplify" that regex back to a `W<digits>` pattern.

3. RENDER — both orientations
   python3 runtime/scripts/remotion_scenes.py <reel>
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/RunningFullEpisodes.tsx, registered in Root.tsx TWICE — 1920x1080
   and 1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.
   `--only <BID>` re-renders one beat; it takes a single id, not a list.

   The composition ids are W5Graph, W5Engine, W5Versus, W5NewBonds, W5Added, W5Timing,
   W5Fresh and W5Limits. They deliberately avoid W5Bluf / W5Setup / W5Scoreboard /
   W5InventedFact / W5Substring / W5CodeAlone / W5Confidence / W5Veto — the Private AI
   Valuation series already owns those ids and a collision is silent.

   That file imports nothing from AiDebtTracker.tsx, GroundingTheDebtTracker.tsx,
   BuildingTheAnswerKey.tsx, BuildingTheTriage.tsx, ReadingIntoCitedFacts.tsx or the
   week 1-11 reel files, by series convention: every earlier signed master stays
   re-renderable byte-identically.

   WATCH THE UNKNOWN-PROP WARNING. remotion_scenes.py prints, before rendering:
       [remotion] WARN <beat>: <Pattern> has no prop(s) named ... — zod will DROP them and
       render this beat with that field's DEFAULT text.
   Do not render through it. ClaudeVerdictArtifact's props are artifactTitle /
   artifactHeading / artifactLines, and ClaudeTitleOutro's is subline.

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

   Then READ the PNGs yourself, sampling each beat at ~0.95 of its own duration — footnotes
   and source lines enter at 0.80-0.90 and a frame sampled at 0.80 looks half empty when it
   is not. The gate checks edge bleed, canvas fill and contrast. It does NOT check overlap,
   cannot tell whether a number is the RIGHT number, cannot tell whether a source line cites
   a file containing the claim, cannot tell whether a caption describes the chart beneath it,
   cannot tell an empty element from an intentional one, cannot tell whose words are on the
   frame, cannot tell whether a bar measures the thing the beat is about, does not check that
   money figures carry a currency symbol, will pass a text box sized to two pixels that wraps
   one word per line, will pass a case-folded proper noun, will pass a figure stated as its
   own complement, will pass a divider rule with nothing under it, will pass a column header
   aligned to the wrong column, and will pass a frame that claims more than the data logs.

   Watch specifically:
   - B05's band has FIVE segments and the smallest is 2 of 66 — about 19px in landscape.
     Check the "4" and the "2" beneath it do not collide, and that the unnamed segment reads
     as a segment and not as a seam. Check the "26 not in the report" bracket label, which is
     wider than the bracket it sits under.
   - B04's grid is 17 per row in landscape and 9 in portrait, so 9:16 ends on a ragged row of
     7. Check it still reads as thirty-four.
   - B06's dashed boundary is derived from the SECOND band's span, so the rule and the end of
     the fixed window are the same instant by construction. Check they line up at 4K, and
     check the long right-hand axis label does not meet the boundary label in portrait.
   - B07 is the densest beat in the reel: five bars, a line label and three multi-line
     qualifiers. Check the foot of the frame.
   - B01's five-node column and B04's four-row cell grid are NEW shapes in portrait.
   - Portrait beats rescaled after the first portrait read are listed in BUILD-LOG.md.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never show the recall rise without the precision fall on the same frame.
   - Never say the tracker reads its own opening ledger. It was borrowed from the answer key.
   - Never present the 30 of 34 without the 26 wrong additions that follow it.
   - Never present the diagnosis of the 26 as a measurement. Claude read them, after scoring.
   - Never quote only the fixed run's precision. Both runs are reported, 89.2% and 90.2%.
   - Never present triage's 15 of 15 without last week's 8 of 9 failure on the same frame.
   - Never say the reader is more accurate. A single model call read 96% against its 91%.
   - Never present 3 of 4 as 3 of 5, or drop the ungradable report from the denominator.
   - Never imply a person has reviewed this week. The gate says DELEGATED.
   - Never invent a defect id.
   - Never drop B08. The reel ends on its own limits, as every episode in this series does.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_13_11_2026.mp4` | 3840×2160, 24fps |
| `vertical/running-full-episodes-from-filings-to-ledger-916.mp4` | 2160×3840, same length |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
