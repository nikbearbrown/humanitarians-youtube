# BUILD-LOG — knowledge-work-plugins--claude-liam-account-research

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-account-research/beat_sheet.json`,
7 beats, brand `claude-liam`, register `Teardown`, `source_skill` pointing at
a `common-room/skills/account-research/SKILL.md` on Bear's other machine —
not present in this tree). Read the source's own narration text in full
(it already carries the skill's trigger-phrase language verbatim, since B03
quotes it), plus its metadata; there was no SCRIPT.md alongside the source
sheet to cross-check against.

Kept beat count (7) and every fact: `account-research` is a `SKILL.md` file
Claude reads before acting — the file is the program; it fires only on
matching trigger language (`research [company]`, `tell me about [domain]`,
`pull up signals for [account]`, `what's going on with [company]`, or any
account-level question); execution is a linear pipeline (read → execute
each step → return) with no branching unless a step says so; the payoff is
repeatability (same input, same steps, same kind of output, every run); the
limit is exact (anything outside the spec isn't covered). Remapped the
source's B03 Teardown "gets right / bites" framing into a both-directions
mechanism fact (B03: matching triggers run the pipeline; non-matching
requests never start it) with the design-judgment removed, and its BVDT
verdict recap into a single BCRY carry-out sentence per CARRY-OUT LAW.
Added the newcomer wrong-guess move the Teardown source didn't need (Plain
register requires it): that Claude already knows an account's status from
general knowledge, falsified in B01 by the dated-signal case (new hire,
funding round, product launch — nothing dated today is in any training
corpus). New anchor (B02→B03): the literal query `"research Acme Corp"`
walked through READ/EXECUTE/RETURN, run again unchanged, contrasted with a
non-matching question that never enters the pipeline.

B00 WRITER LAW: naive guess "Claude must already **remember** it, right?"
corrected to "check" (the newcomer's default assumption — Claude answers
from memory the way it answers general questions — is exactly what the
reel exists to correct).

**Two defects found and fixed before the cut passed gates — logged
honestly, not rounded up:**

1. **TIMING LAW near-miss.** First B00 narration (31 words) measured only
   8.73s of Kokoro audio. Traced how the pipeline actually times B00:
   `generate_audio_kokoro.py` does not implement `lead_silence_s` at all
   (grepped the script — no match), and `remotion_scenes.py` sizes the
   Remotion composition purely off `actual_duration_s` (`beat.get("actual_duration_s")
   or beat.get("estimated_duration_s")`, no lead-silence addition). So
   `lead_silence_s: 0.8` in the sheet is inert for this Kokoro-only skill —
   the beat's entire typing window IS the measured narration duration, full
   stop. At 8.73s the writer's deterministic timeline (typing three lines,
   the "remember"→"check" reconsideration, its 1000-1500ms pause, the
   retype) was still mid-word ("remember") when the clip ended — confirmed
   by pulling a frame at t=8.65s and seeing the doomed accent-colored
   "remember" frozen, uncorrected. This is the exact pilot failure
   COMPLETION LAW warns about, caught before calling the beat done. Fixed
   by (a) lengthening B00 narration to 35 words (WRITER LAW's ceiling) —
   raised measured audio to 9.69s — and (b) speeding the writer's own
   props (`mistakeRate` 6→4, `hesitateWithin` 3→2, `hesitateBetween` 22→12,
   `charMs` 55→48) since 35 words is the law's hard cap and duration alone
   couldn't close the gap. Re-rendered, re-pulled a late frame (t=9.6s):
   "Claude must already check it, right?" fully typed and settled with
   room to spare. Verified media/B00.mp4 = 9.7s (clears the ≥8s floor) AND
   the correction is visible on screen, not just the numeric floor.
2. **GATE T kerning FAIL, B03.** First `type_check.py` run failed B03: "max
   inter-glyph gap 31px > threshold 13px." Traced the checker's §8.4
   pixel-gap logic (`runtime/scripts/type_check.py` lines ~1891-1958): it
   scans the single densest text row-band per frame and measures column-ink
   gaps, with no notion of separate on-screen groups. B03 places two
   parallel three-station pipelines (matched query, left; non-matching
   query, right) at the same y-height side by side — the checker read the
   empty canvas between the two clusters as one giant "letter gap." Fixed
   in `scenes.py` by vertically staggering the right pipeline's row
   (`UP*0.5` → `UP*0.1`) so the two label rows never share a scanline —
   not a checker change, a scene-authoring fix (never loosened the
   validator). Also removed a redundant small italic caption ("no bracket.
   no match.") that duplicated the beat's own bottom caption, tightening
   B03 per SHOW-DON'T-TELL. Re-rendered B03, re-ran GATE T: PASS, 0 FAILs.

Built via the standard hai-simple pipeline, in the foreground throughout,
per COMPLETION LAW (no background render steps left unattended):

1. `generate_audio_kokoro.py` — 7/7 beats, free, measured durations written
   back (B00 9.69s → 9.7s after prop retune; B01 14.89s; B02 17.77s; B03
   17.92s; BCRY 8.23s; BHTF 16.49s; BOUT 3.33s).
2. `remotion_scenes.py` (foreground; the harness auto-backgrounded the
   >120s call, so it was polled in-turn via its own output file and process
   table rather than left unattended) — B00/BCRY/BHTF/BOUT, all 3840×2160
   with audio.
3. Custom Manim `scenes.py` (`ARB01Scene`/`ARB02Scene`/`ARB03Scene`) via
   `render_scenes.py`, foreground. GATE L checked first
   (`./art scenes "skill folder SKILL.md instructions trigger phrase
   pipeline read execute return"`) — the only hits (`SkillTeardownPipeline`
   and siblings) are Teardown-branded, claude-palette Remotion components;
   not a fit for Plain-register humanitarians-palette body beats, same
   disposition as every other hai-simple reel in this family. Bespoke
   Manim, humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`).
4. `compile.py` (foreground) — 7/7 slots filled, content-check/frame-check/
   lane-check all PASS, GATE AUDIO PASS mean_volume -23.9 dB. THE 4K LAW
   forced the master natively to 3840×2160.
5. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788362972) newer than
   beat_sheet.json mtime (1788362895); h264 3840×2160 + aac streams
   present, duration 89.33s; `ffmpeg -af volumedetect` mean_volume
   **-23.9 dB**, max -2.8 dB.
6. GATE T (`type_check.py`): PASS, 0 FAILs, after the B03 kerning fix above.
7. Gate V: pulled frames at 6s spacing across the full 89.3s runtime (15
   frames) plus two targeted pulls into media/B00.mp4 to verify the writer
   correction, and read all of them directly — B00's naive-question →
   correction, B01's frozen-training-date/live-signals diagram, B02's
   anchor plant (SKILL.md, trigger match, READ/EXECUTE/RETURN lighting),
   B03's anchor payoff (same query rerun, non-matching query staying dark),
   BCRY's carry-out quote card, BHTF's Your Turn composer (mid-type and
   settled), and BOUT's outro/subscribe card all read legibly with safe
   inset respected and no text overlap.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after 1 fix — kerning false-positive from
  side-by-side same-row text clusters, B03)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: duration 89.33s; mp4 mtime newer than beat_sheet.json mtime
- WRITER LAW timing: media/B00.mp4 = 9.7s (≥8s floor) and the correction
  ("remember" → "check") is visible on screen at t≈9.6s, confirmed by frame
  pull, after 1 fix (narration lengthened to 35 words + writer props
  retuned to fit the available window)

Metadata file written: `knowledge-work-plugins--claude-liam-account-research.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `knowledge-work-plugins` matches the map's
`knowledge-work-plugins` prefix directly — plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
