# BUILD-PROMPT — building-the-filing-timeline-triage-and-document-server

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-10-30-Building-the-filing-timeline-triage-and-document-server

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json transcribes the author's own saved results as published in pantry/*.svg
   (adt-w3-holdout, adt-w3-funnel, adt-w3-triage, adt-w3-docs) and in narration_script.md's
   source table. Every bar's geometry in those SVGs was recomputed as a ratio and had to agree
   with its printed fraction before the value was accepted. Every on-screen number is a prop
   read from figdata.json by build_beat_sheet.py. Never type a number into a scene or a beat
   sheet. The injection asserts, and MUST keep asserting:
       handcheck:  fresh share < last-week share               <- FRAMING
                   gradable 3 + not-gradable 2 == drawn 5
                   1 agreement + 2 defects == the 3 gradable reports
       timeline:   469 + 94 + 30 == 593 filings
       funnel:     394 + 199 == 593   (every filing is decided somewhere)
                   163 + 21 == 184    (what is kept is what each decider kept)
                   rules share between 0.64 and 0.69 — the narration says "two thirds"
       check:      recall == 1.0 AND recall >= pass line 0.95  <- SECOND ARGUMENT
                   precision < recall, event type < precision
                   precision denominator - recall numerator == 2 named false alarms
                                                              <- THIRD, ties frame to maths
                   22 of 22 carry-over; 24 positives inside a 50-filing sample
       wrong:      3 failures, every one of them with a consequence
       quotes:     8 not verbatim of 21 checked

   THE FRAMING ASSERTION IS `FRESH_SHARE < LAST_WEEK_SHARE`. B01's claim is that 3 of 3 is a
   calibration on the reports last week's fixes were made against, and that 1 of 3 on reports
   drawn fresh and graded once is the measurement. If the fresh score ever caught up, the beat
   would be drawing a distinction that no longer exists and the build MUST fail.

   THREE CLAIMS ARE NOT MEASURED in figdata.json. They are named constants, and each beat
   that uses one SAYS SO on screen:
       AGENT_STATE   the agent still cannot read a filing into facts   (B00/B04/B08)
       LABELLER      the 50 labels are Claude's judgment, not a person's (B05/B08)
       OWN_MISTAKE   one transcription error in the author's hand-check (B02)

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 21 rows. Read rows 3, 5, 9, 12, 13, 16 and 19 first. Row 3 is the framing
     assertion; row 13 is the number most likely to be over-read.
   - PEDAGOGY.md must carry a signed verdict line. If it says PENDING, STOP and tell the human
     what they are being asked to sign. Do not sign it. Do not pass --no-gate.
     NEVER write the signed-verdict phrase anywhere else in that file — not in a placeholder,
     not in an instruction, not in a quotation. The audio gate matches a verdict LINE, but a
     document that argues with its own gate is still a bad document.
   - CHECKS-REPORT.md must exist before the first compile.

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
   runtime/remotion/src/BuildingTheTriage.tsx, registered in Root.tsx TWICE — 1920x1080 and
   1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.

   That file imports nothing from AiDebtTracker.tsx, GroundingTheDebtTracker.tsx,
   BuildingTheAnswerKey.tsx or the week 1-11 reel files, by series convention: every earlier
   signed master stays re-renderable byte-identically.

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

   Then READ the PNGs in _qc/ yourself. The gate checks edge bleed, canvas fill and contrast.
   It does NOT check overlap, cannot tell whether a number is the RIGHT number, cannot tell
   whether a source line cites a file containing the claim, cannot tell whether a caption
   describes the chart beneath it, cannot tell an empty element from an intentional one,
   cannot tell whose words are on the frame, cannot tell whether a bar measures the thing the
   beat is about, does not check that money figures carry a currency symbol, and will pass a
   text box sized to two pixels that wraps one word per line.

   Watch specifically:
   - B01's dashed tail is EXCLUDED, not empty. It must never read as an unfilled part of the
     score: dashed border, no fill, labelled +2, with "1 of 3" beside it.
   - B04 keeps the full 593 outline on EVERY row. Four free-standing bars would claim four
     populations instead of one being narrowed.
   - B05's pass line is one rule through all four tracks, and on the recall bar it sits
     INSIDE the fill. Check at 4K that it does not read as a seam.
   - B03's ticks stand for filings; the real count is printed beside the band. Never label
     the ticks.
   - B07's hit card holds a real quoted sentence. Check it wraps rather than clipping.
   - Portrait beats rescaled after the first portrait read are listed in BUILD-LOG.md.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never say the agent reads filings. It finds them and makes them citable.
   - Never present 3 of 3 as a measurement, or 1 of 5 as the fresh score.
   - Never present 24 of 24 as accuracy. It is recall, on 24 positives in a 50-filing sample.
   - Never say "I labelled". Claude labelled, before triage ran.
   - Never say the model "made up" a quote. Not verbatim is not the same as invented.
   - Never drop B08. The reel ends on its own limits, as every episode in this series does.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_30_10_2026.mp4` | 3840×2160, 24fps |
| `vertical/building-the-filing-timeline-triage-and-document-server-916.mp4` | 2160×3840, same length |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
