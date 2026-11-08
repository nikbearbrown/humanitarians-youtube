# BUILD-PROMPT — reading-debt-announcements-into-cited-facts

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-11-06-Reading-debt-announcements-into-cited-facts

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json transcribes the author's own saved results as published in pantry/*.svg
   (adt-w4-reader, adt-w4-grounding, adt-w4-triage, adt-w4-holdout) and in
   narration_script.md's source table. Every bar's geometry in those SVGs was recomputed as
   a ratio and had to agree with its printed fraction before the value was accepted. Every
   on-screen number is a prop read from figdata.json by build_beat_sheet.py. Never type a
   number into a scene or a beat sheet. The injection asserts, and MUST keep asserting:
       reader:    B2 share > reader share                      <- FRAMING
                  reader share > B1 share   (the check it was set, and passed)
                  B2 got == B2 of == 160    (it read every field right)
                  reader extra > B2 extra > B1 extra           <- THIRD, the reader's cost
                  reader.of != B1.of        (the bars do NOT share a denominator)
                  62 + 4 == 66 instruments, and 62 > 10x4 (mostly easy documents)
       grounding: 227 + 3 + 24 == 254 copies
                  8 + 16 == 24 refused                         <- FOURTH, closes both ways
                  the € is in the passage and the $ is in the copy
       triage:    fresh share < pass line 0.95                 <- SECOND, a FAILED check
                  last week's share >= 0.95 and == 1.0 (a calibration)
                  only 9 positives in the draw
       key:       1 of 5 < 3 of 3
                  4 defects, in 4 DISTINCT companies
       truth:     51 of 51 bonds, 19 of 19 principals

   THE FRAMING ASSERTION IS `B2_SHARE > READER_SHARE`. The week's check, fixed in the design
   in week 1, was that the event reader must beat B1's regex rules. It did. But one model
   call typing every value itself read MORE fields right than the reader. The whole reel is
   built on that gap: the reader can only be sold on provenance, never on accuracy. If the
   reader ever overtook B2 the build MUST fail, because this would be a different episode.

   THREE CLAIMS ARE NOT MEASURED in figdata.json. They are named constants, and each beat
   that uses one SAYS SO on screen:
       GATE_RECORD   the week is DELEGATED, not CLEARED; no person reviewed it  (B00/B08/B09)
       LABELLER      the labels and the truth are a model judgment, not a person's (B04/B08)
       CHECK_ORIGIN  the check and the 95% line were fixed in week 1, before any run (B03/B08)

   NO DEFECT ID IS INVENTED. FRICTIONAL.md gives ids for P41-P46 and gives none for the
   three open reader defects. Do not supply them.

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 27 rows. Read rows 2, 4, 5, 8, 11, 15, 17, 19 and 22 first. Row 2 is the
     framing assertion; rows 4 and 5 are the two numbers most likely to be over-read.
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
   runtime/remotion/src/ReadingIntoCitedFacts.tsx, registered in Root.tsx TWICE — 1920x1080
   and 1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.
   `--only <BID>` re-renders one beat; it takes a single id, not a list.

   That file imports nothing from AiDebtTracker.tsx, GroundingTheDebtTracker.tsx,
   BuildingTheAnswerKey.tsx, BuildingTheTriage.tsx or the week 1-11 reel files, by series
   convention: every earlier signed master stays re-renderable byte-identically.

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
   one word per line, will pass a case-folded proper noun, and will pass a figure stated as
   its own complement.

   Watch specifically:
   - B02's two highlights. `Highlight` marks the first occurrence of its `mark` string; if a
     prop is edited so the mark no longer occurs, the component falls back to plain text and
     the beat loses its entire argument while still rendering a clean-looking frame.
   - B03 is the widest row in the file: name, bar, percentage, fraction, divider, extras
     track, extras count. In portrait the name column stacks ABOVE the track and the value
     columns do not — that is exactly what clipped every figure on week 3's B04.
   - B05's 24 cells must stay countable: 12 per row in landscape, 8 in portrait.
   - B06's dashed pass line sits inside the full 24-of-24 bar. Check it reads at 4K.
   - B08 is the densest beat in the reel. Check the foot of the frame.
   - Portrait beats rescaled after the first portrait read are listed in BUILD-LOG.md.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
   - Never say the reader is more accurate. It beat B1; B2 read every field right.
   - Never show 94% without 100% on the same frame.
   - Never present the three bars as sharing a denominator.
   - Never drop the reader's 29 extras.
   - Never present the fresh triage check as a pass. It failed.
   - Never present 3 of 3, on either the triage set or the answer key, as a measurement.
   - Never say "I labelled". Claude labelled, before any method ran.
   - Never imply a person has reviewed this week. The gate says DELEGATED.
   - Never invent a defect id.
   - Never drop B08. The reel ends on its own limits, as every episode in this series does.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_06_11_2026.mp4` | 3840×2160, 24fps |
| `vertical/reading-debt-announcements-into-cited-facts-916.mp4` | 2160×3840, same length |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
