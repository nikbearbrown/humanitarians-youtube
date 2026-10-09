# BUILD-PROMPT — documenting-the-system-and-making-the-demo-runnable

The single paste-ready Claude Code prompt that rebuilds this reel end to end, in BOTH
orientations. Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/new_humanitarians/humanitarians-youtube/fellows/om-mali/2026-10-09-Documenting-the-system-and-making-the-demo-runnable

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata.json is generated at build time by querying the live database, reading the generated
   findings file, and running `git show HEAD` against the working tree. Every on-screen number
   is a prop read from it by build_beat_sheet.py. Never type a number into a scene or a beat
   sheet. The injection asserts, and MUST keep asserting:
       documents[]: 6 entries, exactly 3 with existed=false
                    every absent one has lines_before == 0 — an absent file has no "before"
                    nothing shrank; 444 lines from nothing, 104 added
       prior_art[]: 3 rows all at before == 0, all with after > 0
                    EXACTLY 2 of them in documents that EXISTED        <- FRAMING
                    22 citations added, 13 of them in the two published documents
       remark:      1,019 / 4,079 == 0.2498, over 5,178 marks
       layers[]:    3 layers, mutability == [immutable, append-only, rebuildable]
                    the layers' tables account for all 15 tables figdata counts
                    EACH layer's row total == the sum of its OWN tables
                    raw_holdings 5,806 == match_decisions 5,806; 5,806 − 5,479 == 327
       demo:        5 acts, 5 files scanned, 0 write statements

   THE FRAMING ASSERTION IS `len(PUBLISHED_ZEROES) == 2`. w12-priorart.png tabulates THREE
   documents at BEFORE 0, but proposal.md carries existed=false — its zero is an absent file,
   not a document that failed the requirement. The figure's own caption agrees with the reel
   ("in either published document"); its table does not. If that split ever changes the build
   MUST fail rather than ship the wider claim.

   ONE ASSERTION STOPS A FIGURE DRIFTING FROM ITS OWN DETAIL: each layer's row total is
   asserted equal to the sum of that layer's tables, not trusted as a separate number.

   FOUR VALUES ARE NOT IN figdata.json. They come from narration_script.md and the documents,
   are passed as named constants, and each beat that uses one SAYS SO on screen:
       PRIOR_ART_NAMES  Caplight, Gornall & Strebulaev, Agarwal, Chernenko, Kwon   (B03)
       LOAD_BEARING     what the Gornall & Strebulaev citation actually changed    (B04, B09)
       the 8-link chain data_architecture.md's own trace; only the headline is in figdata (B06)
       LM_SITES         exactly two places a language model sits, neither touching a number (B08)

   python3 build_beat_sheet.py --check     # assertions only, writes nothing
   python3 build_beat_sheet.py             # regenerates beat_sheet.json

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 5, 6, 13, 17 and 19 first. Row 5 is load-bearing — it is
     a DERIVATION that contradicts the source figure's table.
   - PEDAGOGY.md must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human what
     they are being asked to sign. Do not sign it. Do not pass --no-gate for a final.
   - CHECKS-REPORT.md must exist before the first compile.
   - THERE IS NO README.md FOR THIS REEL. Weeks 9 and 10 each had one with a figure-to-beat map
     and a known-defects list. Derive the relationships from figdata.json rather than assuming
     a caption is right — that absence is why B03 exists.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then: python3 lock_durations.py beat_sheet.json vertical/beat_sheet.json
   Both cuts share the SAME mp3s. Never regenerate audio for the vertical cut.

3. RENDER — both orientations
   python3 runtime/scripts/remotion_scenes.py <reel>
   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
   Twelve beats each, all Remotion, zero slates. The eight reel-local scenes live in
   runtime/remotion/src/DocumentingTheSystem.tsx, registered in Root.tsx TWICE — 1920x1080 and
   1080x1920 under the <pattern>916 name. --scale=2 gives 3840x2160 and 2160x3840.

   WATCH THE UNKNOWN-PROP WARNING. remotion_scenes.py prints, before rendering:
       [remotion] WARN <beat>: <Pattern> has no prop(s) named ... — zod will DROP them and
       render this beat with that field's DEFAULT text.
   Do not render through it. It stayed silent through every run of this reel, which is what
   correct props look like. A legacy `sparkLine` warning on ClaudeVerdictArtifact is expected.

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
   describes the chart beneath it, cannot tell an empty element from an intentional one, cannot
   tell whose words are on the frame, and CANNOT TELL WHETHER A BAR MEASURES THE THING THE BEAT
   IS ABOUT. It has missed something in eight of the ten episodes in this series.

   Watch specifically:
   - B02's bars are STACKED — pale for what was already there, solid for this week. A single
     bar scaled to total lines gives entity_resolution.md (grew 60 of 1,016) the longest bar on
     a frame about writing from nothing, and gives the three absent documents the shortest.
   - B02 prints the WORDS "did not exist" where an absent file's before-count would go. A 0
     there means "a document with no lines", which is a weaker and different claim.
   - B03's dashed rule is load-bearing. Above it, two real zeroes. Below it, dimmed, the one
     that is not a finding.
   - B06's dots are joined by drawn segments. A bulleted list has no links to break.
   - Portrait B02/B06/B08 were rescaled after the first portrait read. Re-read them if you
     touch any f(landscape, portrait) value.

6. NEVER
   - Never publish. The masters stay in this folder.
   - Never spend. Fellow tier is free end to end; a step asking for a key is a toolkit bug.
   - Never lift the pantry PNGs as media, and never copy them into images/ (compile output).
     w12-demo.png also has an edge-bleed defect of its own — its layer summary runs off the
     right edge. Do not inherit it.
   - Never say three documents failed the prior-art requirement. Two did.
   - Never present 22 citations as a literature review. Exactly one changed a rule.
   - Never present 0 write statements as a proof. It is a static scan of five files.
   - Never drop the run-log limit. The chain is datable because of a log with two rows in it.
   - Never drop B08. The reel ends on its own limits, as every episode in this series does.
```

---

## What a rebuild should produce

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_09_10_2026.mp4` | 3840×2160, 24fps, 212.17s |
| `vertical/documenting-the-system-and-making-the-demo-runnable-916.mp4` | 2160×3840, 24fps, 212.17s |
| `*-slate.mp4` (both) | review cuts with beat IDs + running timecode |
| `_qc/REPORT.md` (both) | 0 BLOCKER, 0 MAJOR |

Twelve beats, zero slates, `$0.00`.
