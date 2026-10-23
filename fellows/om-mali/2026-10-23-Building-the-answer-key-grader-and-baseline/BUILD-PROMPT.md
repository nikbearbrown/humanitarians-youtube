# BUILD-PROMPT — building-the-answer-key-grader-and-baseline

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-10-23-Building-the-answer-key-grader-and-baseline

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json transcribes the author's own saved results as published in pantry/*.svg
   (adt-w2-answerkey, adt-w2-handcheck, adt-w2-headroom) and in narration_script.md's source
   table. Every bar's geometry in those SVGs was recomputed as a ratio and had to agree with
   its printed fraction before the value was accepted. Every on-screen number is a prop read
   from figdata.json by build_beat_sheet.py. Never type a number into a scene or a beat sheet.
   The injection asserts, and MUST keep asserting:
       answer key:  900 + 41 + 152 == 1,093 reports        <- B01 draws ONE partitioned bar
                    bond-by-bond is a MAJORITY             <- the narration says "most"
                    25 + 75 == 100 companies
       grader:      4 bond fields, 3 scoring modes
       handcheck:   held-out share < after-fixes share     <- FRAMING
                    first-pass share < after-fixes share
                    exactly 5 bugs; same 10 reports before and after; held-out set is smaller
       baseline:    recall > 0.90 AND new bonds caught == 0 AND exact/quarters < 0.5
                                                           <- SECOND ARGUMENT
                    recall_lo < recall < recall_hi
       headroom:    36 - 4 == 32 searchable new bonds
                    16 - 9 - 1 == 6 early repayments
                    announced > baseline caught            <- B06 draws the DISTANCE
       clock:       43 < 495

   THE FRAMING ASSERTION IS `HELD_OUT_SHARE < AFTER_SHARE`. B04's whole claim is that 10 of 10
   is a CALIBRATION — the same ten reports found the five grader bugs, so the grader cannot
   help but agree with them afterwards — and that 2 of 3 on untouched reports is the
   measurement. If those scores ever became equal the beat would be drawing a distinction that
   no longer exists, and the build MUST fail rather than advertise a perfect score.

   THE SECOND ARGUMENT is B05: a flattering number that hides a zero. If recall ever stopped
   being high, or the zero stopped being zero, that beat is a different beat.

   THREE VALUES ARE NOT IN figdata.json's measured block. They are named constants, and each
   beat that uses one SAYS SO on screen:
       AGENT_STATE    the agent is NOT built; this week built what will grade it  (B00/B02/B08)
       TZ_INFERENCE   "most likely a time-zone change" — EDGAR published no note  (B07/B08)
       HELD_OUT_MISS  the one miss is a company's own tagging errors              (B04/B08)

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 5, 8, 9, 12, 14 and 17 first. Row 12 is the framing
     assertion; row 5 is the one the whole reel can get wrong by implication.
   - PEDAGOGY.md must carry a signed verdict line. If it says PENDING, STOP and tell the human
     what they are being asked to sign. Do not sign it. Do not pass --no-gate.
     NEVER write the signed-verdict phrase anywhere else in that file — not in a placeholder,
     not in an instruction, not in a quotation. Until 2026-10-18 the audio gate searched the
     whole file for the substring and a PENDING template opened it; the gate now matches a
     verdict LINE, but a document that argues with its own gate is still a bad document.
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
   runtime/remotion/src/BuildingTheAnswerKey.tsx, registered in Root.tsx TWICE — 1920x1080 and
   1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.

   That file imports nothing from AiDebtTracker.tsx, GroundingTheDebtTracker.tsx or the week
   1-11 reel files, by series convention: every earlier signed master stays re-renderable
   byte-identically.

   WATCH THE UNKNOWN-PROP WARNING. remotion_scenes.py prints, before rendering:
       [remotion] WARN <beat>: <Pattern> has no prop(s) named ... — zod will DROP them and
       render this beat with that field's DEFAULT text.
   Do not render through it. ClaudeVerdictArtifact's props are artifactTitle /
   artifactHeading / artifactLines, and ClaudeTitleOutro's is subline — not title / heading /
   lines / subtitle.

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
   cannot tell whose words are on the frame, cannot tell whether a bar measures the thing the
   beat is about, and does not check that money figures carry a currency symbol.

   Watch specifically:
   - B05 IS SUPPOSED TO BE MOSTLY EMPTY. The outlined, labelled track with nothing in it is
     the argument. If a fill check complains, read the frame; the fix is never to put a bar
     in it, and never to delete the outline either — an absent bar reads as a render fault.
   - B04's dashed rule is load-bearing: above it the reports that FOUND the fixes, below it
     the ones picked first and graded once. Do not merge the three bars into one group.
   - B06 draws a SPAN between two readings on one axis. Two ordinary bars would show two
     quantities and lose the beat.
   - B01's segment labels live in the legend, not in the bar. A segment 41 of 1,093 wide
     cannot hold a label.
   - Portrait beats rescaled after the first portrait read are listed in BUILD-LOG.md.
     Re-read them if you touch any f(landscape, portrait) value.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never say the agent exists. Week 2 built the things that will judge it.
   - Never present 10 of 10 as an accuracy score. It is a calibration; the measurement is 2 of 3.
   - Never lead B05 with 90.7%. The zero is the finding; the recall is what hides it.
   - Never say "30 of 36". The searchable denominator is 32, and the 4 are on the frame.
   - Never state the timestamp cause as fact. EDGAR published no note.
   - Never drop B08. The reel ends on its own limits, as every episode in this series does.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_23_10_2026.mp4` | 3840×2160, 24fps |
| `vertical/building-the-answer-key-grader-and-baseline-916.mp4` | 2160×3840, same length |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
