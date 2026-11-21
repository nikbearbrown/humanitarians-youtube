# BUILD-PROMPT — reading-the-opening-ledger-instead-of-borrowing-it

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-11-20-Reading-the-opening-ledger-instead-of-borrowing-it

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json transcribes the author's own saved results as published in pantry/*.svg
   (adt-w6-merge, adt-w6-opening, adt-w6-gap, adt-w6-catch) and in narration_script.md's
   source table and notes. Every bar's geometry in those SVGs was recomputed as a ratio and
   had to agree with its printed fraction before the value was accepted. Every on-screen
   number is a prop read from figdata.json by build_beat_sheet.py. Never type a number into
   a scene or a beat sheet. The injection asserts, and MUST keep asserting:
       gap:      oracle recall > B0 recall                      <- FRAMING, half one
                 agent recall <= B0 recall                      <- FRAMING, half two
                 oracle recall > agent recall  (the cost is a fall)
                 agent precision > B0 precision AND > oracle precision   <- SECOND
       merge:    26 -> 3 wrong additions; precision after > before
                 0 < (precision after - B0) <= 0.01             <- THIRD, "level" not "better"
                 21+25+4 != 26   (actions, NOT a breakdown of the 26)
       score:    model recall > rules recall, model precision > rules precision
                 (model recall gain) > (model precision gain)   <- FOURTH
                 graded_on 43 < reports_read 94
       variance: run1 count != run2 count                       <- FIFTH
       catch:    caught < missed (17 < 33); settled < questions; no graded bond changed
       limits:   total debt agent 26 < oracle 44 < 79

   THE FRAMING ASSERTION HAS TWO HALVES AND BOTH MUST HOLD. Week 5 reported +7.0 points of
   recall over doing nothing. That number depended on every quarter being handed an opening
   ledger copied from the answer key. Reading its own start, the agent lands at 90.1%
   against B0's 90.9% — LEVEL, not ahead. If agent start ever pulled ahead of B0 on recall
   the build MUST fail, because B00 and B05 would be announcing a cost that did not land.

   THREE CLAIMS ARE NOT MEASURED in figdata.json. They are named constants, and each beat
   that uses one SAYS SO on screen:
       GATE_RECORD   the week is DELEGATED, not CLEARED; no person reviewed it (B00/B08/B09)
       JUDGMENTS     which rows are instruments is qwen3:4b's judgment, not a person's
                     (B08); the hand-check transcriptions are a model's reading
       ORACLE_WAS    the borrowed start was a deliberate ablation (A4), not an oversight
                     (B02)

   NO DEFECT ID IS INVENTED. FRICTIONAL.md gives P56-P61, P47, P49, P53, P54, P59 and P60.
   The three wrong additions that remain are NOT yet diagnosed and carry no id.

   ONE CONFLICT IS UNRESOLVED ON PURPOSE. FRICTIONAL.md breaks the 21 settled questions
   down as 19+2; description.txt as 17+2+2. Both total 21. NO breakdown is drawn on any
   frame — only the 21, that most were bonds the ledger already held, and that no graded
   bond changed. FACTCHECK row 22. Do not guess a split.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 31 rows. Read rows 3, 4, 5, 8, 10, 12, 14, 17, 20 and 22 first. Row 14 is
     the framing assertion; row 22 is the conflict that needs the author.
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
   python3 runtime/scripts/remotion_scenes.py <reel> --force
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical --force

   PASS --force AFTER ANY SCENE EDIT. remotion_scenes.py SKIPS any beat whose
   media/<BID>.mp4 already exists and prints `[remotion] B01: filled already (skip)`. In
   week 5 two full re-render-and-recompile cycles were no-ops for exactly this reason, and
   GATE V re-graded the untouched video and reported it clean. Check the log says `ok:` and
   not `skip` before believing any gate result.

   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/ReadingTheOpeningLedger.tsx, registered in Root.tsx TWICE —
   1920x1080 and 1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and
   2160x3840. `--only <BID>` re-renders one beat; it takes a single id, not a list.

   The composition ids are W6Merge, W6Opening, W6Score, W6Variance, W6Gap, W6Where, W6Catch
   and W6Limits. They deliberately avoid W6Bluf / W6Collapse / W6Crash / W6Durability /
   W6Funnel / W6Key / W6Split / W6ThreeCauses — the Private AI Valuation series already owns
   those ids and a collision is silent.

   That file imports nothing from the weeks 0-5 reel files, by series convention: every
   earlier signed master stays re-renderable byte-identically.

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
   aligned to the wrong column, will pass a frame that claims more than the data logs, will
   pass a limit whose sentence has lost its subject, and will pass a beat that was never
   re-rendered at all.

   Watch specifically:
   - B05 is the densest layout in the reel and its whole argument is two bars ending at the
     same x. Agent 90.1% and B0 90.9% differ by ~8px on a 1000px track. Check they read as
     level and that B0 is very slightly the longer of the two, which is the truth. READ THIS
     FRAME IN 9:16 FIRST — it is the most likely to overrun its portrait column.
   - B07 draws 86 cells. Check no row is ragged in a way that makes a count look approximate.
   - B01's smaller bar is 3 of 26 — about 11% of the track. Check it is a bar, not a seam.
   - B03 prints a gap figure under each pair; the precision one is +0.9 points (~9px). Check
     it cannot be read as labelling the wrong pair.
   - B06's accented rule block must not read as a fifth company.
   - B08 carries five claim/limit pairs, the gate and three next steps. Check the foot.
   - Portrait beats rescaled after the first portrait read are listed in BUILD-LOG.md.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never show the recall fall without the precision rise on the same frame.
   - Never let 93.3% against B0's 92.8% read as "better". It is level.
   - Never quote the reader's 89.7% / 98.8% against 94 reports. They are graded on 43.
   - Never drop the run-to-run variance. 36 bonds then 22, same report.
   - Never present Core Scientific's refusal as a miss. The point-in-time rule withheld it.
   - Never say the investigators fixed something. They changed no graded bond.
   - Never imply a person has reviewed this week. The gate says DELEGATED.
   - Never invent a defect id, and never guess the split of the 21 settled questions.
   - Never drop B08. The reel ends on its own limits, as every episode in this series does.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_20_11_2026.mp4` | 3840×2160, 24fps |
| `vertical/reading-the-opening-ledger-instead-of-borrowing-it-916.mp4` | 2160×3840, same length |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
