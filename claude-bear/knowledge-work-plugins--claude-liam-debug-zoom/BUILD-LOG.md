# BUILD-LOG — knowledge-work-plugins--claude-liam-debug-zoom

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-debug-zoom/
beat_sheet.json`, 7 beats, partner-built `debug-zoom` skill for Zoom
integrations, brand `claude-liam`, `@NikBearBrown`). SUBJECT.json's
`source_sheet`/`source_dir` pointed at the source reel correctly (unlike
some sibling redos, this one resolved locally without a path substitution).
The source reel's own `source_skill` field points at a partner-built
`SKILL.md` under `.../knowledge-work-plugins/partner-built/zoom-plugin/
skills/debug-zoom/` that lives only on Bear's other machine — not locally
readable — so this redo relied on the source reel's own narration (B00
carries the skill's full, un-truncated stated job) as the record of the
skill's content. Noted in QUESTION.md: three of the source's later beats
(B03, BVDT, BHTF) truncate that same sentence mid-word — an interpolation
bug in the source, not a fact carried forward here.

Kept beat count (7) and every fact from the source: a skill is a folder
Claude reads before acting; `debug-zoom` is one file, `SKILL.md`, plain
language, no hidden logic; its stated job is to isolate the failure point in
a broken Zoom integration and route to the right reference, scoped to auth,
API, webhook, SDK, or MCP behavior; the pipeline is linear — read the file,
execute each step in order, return the result, no branching unless a step
says so; the output is a ranked hypothesis list plus verification steps,
not an automatic fix; same input -> same output every run, inside the five
named categories, and outside them the file has nothing to say. Remapped the
source's B03/BVDT Teardown "gets right / where it bites" framing into B03's
both-directions beat (holds inside the five categories; flips outside them —
same facts, no verdict), and its BVDT verdict into a single BCRY carry-out
sentence per CARRY-OUT LAW.

**Invented, and flagged as invented (QUESTION.md, CARRY-OUT.md, SCRIPT.md):**
the anchor's concrete worked example — a Zoom webhook that stops delivering
events, ranked as signing secret -> timestamp tolerance -> endpoint URL, each
with a verification step. The source never gives a worked example past its
own generic folder/file/pipeline description, so this redo built one from
the skill's own named failure categories to make "ranked hypothesis list
plus verification steps" visualizable, and narration never asserts this
specific order as a quote from the file.

B00 WRITER LAW: naive guess "fix" -> corrected to "diagnose" (the newcomer's
default read of "debug" is "repair"; the skill's actual output is a ranked
list to check, not a repair). 32-word narration + `lead_silence_s: 0.8`,
measured 10.71s (clears the TIMING LAW >=9s window). First render of B00
was killed mid-write by a 2-minute Bash timeout and left a truncated/corrupt
mp4 (`moov atom not found` on ffprobe) that `remotion_scenes.py` had already
marked "filled" — caught this before compiling by probing the file, deleted
it, and re-rendered in the foreground with no timeout cap. Verified on a
frame pulled at 9.5s that the writer's final text reads "...just diagnose
it?" in full — correction confirmed on screen well before the beat ends.

Anchor B02->B03: THE ANCHOR (a silent Zoom webhook; three ranked rows —
signing secret, timestamp tolerance, endpoint URL — typing in one at a time)
returns identically at B03, each row gaining a teal verification checkmark,
then two outside-scope failures (billing glitch, UI bug) fade in struck
through beneath a "nothing to say" label. Same object, same treatment, per
ANCHOR LAW.

**Gate V defect found and fixed before sign-off:** first Gate V frame pull
found BHTF's grey topic line ("DEBUG-ZOOM · ANTHROPIC SKILL · YOUR TURN")
wrapping to two lines and visually colliding with the dark serif "Your Turn"
title directly beneath it — a text-overlap defect, not a rendering glitch.
Root cause: an unnecessary " · YOUR TURN" suffix on the topic prop that the
template reel (`claude-code--claude-liam-plugin-structure`) omits when
`segment` already reads "Your Turn". Fixed by shortening `topic` to
"DEBUG-ZOOM · ANTHROPIC SKILL" (matching the main-title topic, template
convention), deleted the stale `media/BHTF.mp4`, re-rendered BHTF alone, and
recompiled — confirmed clean on a second frame pull (single-line topic, no
overlap with "Your Turn").

Full build sequence, all in the foreground per COMPLETION LAW (no
backgrounded render steps):

1. `generate_audio_kokoro.py` — 7/7 beats, cost $0.00, measured durations
   written back (B00 10.71s, B01 18.2s, B02 19.35s, B03 18.75s, BCRY 7.21s,
   BHTF 16.51s, BOUT 3.07s).
2. `render_scenes.py` (bespoke Manim, this reel's own `scenes.py`) — 3/3
   GRAPHIC beats (B01, B02, B03) rendered clean, first pass.
3. `remotion_scenes.py` — 4/4 REMOTION beats (B00, BCRY, BHTF, BOUT); B00
   needed one re-render after the timeout-truncation catch above; BHTF
   needed one re-render after the Gate V topic-overlap fix.
4. `compile.py` — 7/7 slots filled (B00/BCRY/BHTF/BOUT VIDEO, B01/B02/B03
   MANIM), content-check/frame-check/lane-check all PASS, GATE AUDIO PASS
   mean_volume -24.0 dB. THE 4K LAW forced the clean master natively to
   3840x2160 (no `--review` flag used). Manim clips were time-stretched to
   fill their measured audio durations (B01 ~2.06x, B02 ~2.20x, B03
   ~2.17x); spot-checked in the Gate V frame pull, no visible artifacting
   (static-camera Manim compositions, no fast motion to stretch).
5. GATE T (`type_check.py`): **PASS, 0 FAILs, first pass** — all 7 beats
   §8.10 SKIP (no kerning issues flagged).
6. Gate V: pulled 12 frames at 8s spacing across the full 94.8s runtime and
   read all of them directly, plus two targeted pulls (B00 late-frame
   correction check; BHTF re-check after the topic-overlap fix). B00's
   writer-open correction, B01's one-file/five-category anchor setup, B02's
   pipeline strip + THE ANCHOR planting (ranked rows typing in), B03's
   anchor payoff (checkmarks + struck-through outside-scope cards), BCRY's
   carry-out quote card, BHTF's Your Turn composer card (post-fix), and
   BOUT's outro/subscribe card all read legibly with safe inset respected
   and no text overlap. One defect found and fixed (topic-overlap, above);
   no other defects.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, first pass)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: h264 3840x2160 24fps + aac 48kHz mono; duration 94.82s; mp4 mtime
  (1788454435) newer than beat_sheet.json mtime (1788454381) — independently
  reverified after the final compile, not trusted from compile.py's own report

Metadata file written: `knowledge-work-plugins--claude-liam-debug-zoom.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's own family `knowledge-work-plugins` matches the map's
`knowledge-work-plugins` prefix directly — plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
