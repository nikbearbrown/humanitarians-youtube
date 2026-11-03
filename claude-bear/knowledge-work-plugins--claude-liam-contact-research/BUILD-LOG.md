# BUILD-LOG — knowledge-work-plugins--claude-liam-contact-research

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-contact-research/beat_sheet.json`,
7 beats, brand `claude-liam`, register `Teardown`, `source_skill` pointing at
a `common-room/skills/contact-research/SKILL.md` on Bear's other machine —
not present in this tree). Read the source's own narration text in full
(it already carries the skill's trigger-phrase language verbatim, since B03
quotes it), plus its metadata; there was no SCRIPT.md alongside the source
sheet to cross-check against. Used the same-family, same-shape
`knowledge-work-plugins--claude-liam-account-research` sibling (built
2026-09-02, already DELIVERED) as the exact structural precedent — its
source was the same kind of `common-room/skills/<x>/SKILL.md` teardown,
also not present locally, and its beat_sheet/SCRIPT/CARRY-OUT conventions
were copied directly.

Kept beat count (7) and every fact: `contact-research` is a `SKILL.md` file
Claude reads before acting — the file is the program; it fires only on
matching trigger language (`who is [name]`, `look up [email]`, `research
[contact]`, `is [name] a warm lead`, or any contact-level question);
execution is a linear pipeline (read → execute each step → return) with no
branching unless a step says so; the payoff is repeatability (same input,
same steps, same kind of output, every run); the limit is exact (anything
outside the spec isn't covered). Remapped the source's B03 Teardown
"interesting constraint" / "gets right vs. bites" framing into a
both-directions mechanism fact (B03: matching triggers run the pipeline;
non-matching requests never start it) with the design judgment removed, and
its BVDT verdict recap into a single BCRY carry-out sentence per CARRY-OUT
LAW. Added the newcomer wrong-guess move the Teardown source didn't need
(Plain register requires it): that Claude already knows a specific person
the way it knows general facts, falsified in B01 by the dated-signal case
(a recent reply, a meeting booked, a title change — nothing dated today is
in any training corpus). New anchor (B02→B03): the literal query `"who is
Jane Doe at Acme"` walked through READ/EXECUTE/RETURN, run again unchanged,
contrasted with a non-matching open-ended question that never enters the
pipeline.

B00 WRITER LAW: naive guess "Claude must already **know**, right?" corrected
to "look them up" (the newcomer's default assumption — Claude answers
people-questions from memory the way it answers general questions — is
exactly what the reel exists to correct).

**One defect found and fixed before the cut passed gates — logged
honestly, not rounded up:**

1. **Gate V frame-read caught a Manim/Pango text-rendering bug, not
   flagged by any automated check.** B01's signal card labelled "recent
   reply" rendered with the space between the two words collapsed to zero
   width — the frame read as "recentreply", one fused word, while the two
   sibling cards on the same beat ("meeting booked", "title change")
   rendered their spaces normally. This is a font/kerning quirk on that
   specific letter pair (…t | r…) in Manim's `Text` + Pango backend, not a
   scene-authoring mistake (same `Text(name, font=SANS, ...)` call as the
   other two cards) and not something `type_check.py`'s GATE T caught,
   since the space is present in the string — only a pixel-level glyph
   collision, invisible to a text-content check. Caught only because
   COMPLETION LAW's Gate V frame-pull is a *read*, not a checklist tick.
   Fixed by rewording the card to "reply received" (same fact — a contact
   engagement signal dated today — different letters, avoiding the
   collision), re-rendering only `manim/B01.mp4`, and recompiling. Re-pulled
   the frame: "reply received" renders with a normal visible space.
   Updated the corresponding `new_visual_element`/`mechanic` prose in
   `beat_sheet.json` to match the actual rendered label.

Also fixed pre-emptively (not a gate failure, a self-caught wording issue
before compiling): B00's naive-writer text originally read "Claude must
already know them, right?" with `triggerWords: "know"` / `replacementWords:
"look up"`, which typed out as the grammatically awkward "look up them,
right?" Changed the base text to "...know, right?" (dropping "them" before
the trigger word) and the replacement to "look them up", so the corrected
line reads naturally: "Claude must already look them up, right?" Re-rendered
B00, re-verified the correction is legible at t≈9.3s.

Built via the standard hai-simple pipeline, in the foreground throughout,
per COMPLETION LAW (no background render steps left unattended):

1. `generate_audio_kokoro.py` — 7/7 beats, free, measured durations written
   back (B00 9.73s; B01 16.90s; B02 19.35s; B03 19.18s; BCRY 8.60s; BHTF
   17.11s; BOUT 3.43s).
2. `remotion_scenes.py` (foreground; the first call exceeded the harness's
   default 120s timeout mid-run but had already completed B00/BCRY/BOUT
   before being cut off — confirmed by checking `media/` on disk rather
   than trusting the truncated log — then a second foreground call with an
   explicit longer timeout picked up the remainder) — B00/BCRY/BHTF/BOUT,
   all 3840×2160 with audio. B00 re-rendered once more after the wording
   fix above (`--only B00 --force`).
3. Custom Manim `scenes.py` (`CRB01Scene`/`CRB02Scene`/`CRB03Scene`) via
   `render_scenes.py`, foreground. GATE L checked first (`./art scenes
   "skill folder SKILL.md instructions trigger phrase pipeline read execute
   return"`) — the only hits (`SkillTeardownPipeline` and siblings) are
   Teardown-branded, claude-palette Remotion components; not a fit for
   Plain-register humanitarians-palette body beats, same disposition as
   every other hai-simple reel in this family. Bespoke Manim, humanitarians
   palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). B01 re-rendered once
   after the "recent reply" → "reply received" fix.
4. `compile.py` (foreground, run twice — once before and once after the
   B01 fix) — 7/7 slots filled, content-check/frame-check/lane-check all
   PASS, GATE AUDIO PASS mean_volume -24.0 dB. THE 4K LAW forced the master
   natively to 3840×2160.
5. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788425245) newer than
   beat_sheet.json mtime (1788425176); h264 3840×2160 + aac streams
   present, duration 95.30s; `ffmpeg -af volumedetect` mean_volume
   **-24.0 dB**, max -3.0 dB.
6. GATE T (`type_check.py`): PASS, 0 FAILs (run after the B01 re-render).
7. Gate V: pulled frames at 6s spacing across the full 95.3s runtime (16
   frames) plus two targeted pulls into media/B00.mp4 to verify the writer
   correction, and read all of them directly — B00's naive-question →
   correction, B01's frozen-training-date/live-signals diagram (post-fix,
   "reply received" legible), B02's anchor plant (SKILL.md, trigger match,
   READ/EXECUTE/RETURN lighting), B03's anchor payoff (same query rerun,
   non-matching query staying dark), BCRY's carry-out quote card, BHTF's
   Your Turn composer (mid-type and settled), and BOUT's outro/subscribe
   card all read legibly with safe inset respected and no text overlap.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 95.30s; mp4 mtime newer than beat_sheet.json mtime
- WRITER LAW timing: media/B00.mp4 = 9.7s (≥8s floor) and the correction
  ("know" → "look them up") is visible on screen at t≈9.3s, confirmed by
  frame pull
- Gate V: 16-frame read across full runtime, 0 legibility/overlap defects
  after the B01 text-collision fix

Metadata file written: `knowledge-work-plugins--claude-liam-contact-research.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `knowledge-work-plugins` matches the map's
`knowledge-work-plugins` prefix directly — plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
