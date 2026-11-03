# BUILD-LOG — claude-plugins-official--claude-liam-plugin-structure

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/claude-plugins-official/youtube/claude-liam-plugin-structure/beat_sheet.json`,
7 beats, `claude-plugins-official` plugin-dev `plugin-structure` skill, brand
`claude-liam`, `@NikBearBrown`). Read the source sheet in full (no separate
SCRIPT.md existed for it — narration lived only in the beat sheet).

A near-identical redo of the same underlying `plugin-structure` SKILL.md
already exists on the channel under a different family
(`hai-simple/claude-code--claude-liam-plugin-structure`, sourced from
`anthropics/claude-code`'s own copy of the skill) — that reel anchors on the
`SKILL.md`-exact-filename rule. To give this reel its own throughline rather
than re-running the same anchor under a different slug, this build foregrounds
a different fact this source gives equal billing to its own three "critical
rules": the `${CLAUDE_PLUGIN_ROOT}` portable-path rule. Kept beat count (7)
and the source's core facts: the manifest `plugin.json` lives inside
`.claude-plugin/` and needs exactly one field, `name` (kebab-case); every
other component — `commands/`, `agents/`, `skills/`, `hooks/`, an MCP server
file — lives at the plugin's own root; auto-discovery needs no registration
step; and every intra-plugin path reference (hook command, MCP server
argument, script reference) must be written through `${CLAUDE_PLUGIN_ROOT}`,
never hardcoded, because plugins install to different locations depending on
install method, OS, and user preference. Remapped the source's B05 Teardown
"gets right / where it bites" framing into B03's both-directions beat (a
path routed through the variable survives any install; a hand-written path
works only on the machine that wrote it and breaks silently elsewhere — same
facts, no verdict), and its BVDT verdict into a single BCRY carry-out
sentence per CARRY-OUT LAW. Anchor B02→B03: a hook command field written two
ways (hardcoded vs. `$CLAUDE_PLUGIN_ROOT`), planted with the hardcoded path
struck through and the variable typing in, paid off with the same field
installed on a second machine — the variable version checks green and runs,
the hardcoded version fades with "no error. no warning. just doesn't run."
The manifest/component placement split and the `SKILL.md`-exact-filename
requirement both remain in the body (B01) as supporting facts, not dropped.

B00 WRITER LAW: naive guess "fixed" address → corrected to "portable" (the
newcomer's default move once a hook needs to find a file inside its own
plugin is to just write the path that works right now, on the machine in
front of them); 35-word narration + `lead_silence_s: 0.8`, measured 20.24s
raw (clears the TIMING LAW ≥9s window with wide margin); verified on a late
frame (t=18s of the raw 20.2s clip) that the writer's text reads "a hook's
path to its own plugin's script — should it be a portable address?" —
correction confirmed on screen. Re-verified after compile's audio-driven
center-cut (20.2s→11.5s, skip 4.4s head/tail): pulled a frame at t=10.5s of
the compiled `clips/B00.mp4` and confirmed the correction still lands inside
the conformed clip — the center-cut trims from both ends symmetrically, so a
correction landing in the back third of a much-longer raw clip is not
automatically safe; this reel's timing gave enough margin.

Built fresh in this invocation — no prior artifacts existed beyond
SUBJECT.json:

1. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (7 beats),
   scenes.py (3 Manim scenes: PLRB01Scene/PLRB02Scene/PLRB03Scene),
   render_scenes.py. Confirmed all 4 Remotion patterns used
   (BrutalistHesitantWriter, WantQuote, ClaudeComposerAsk, OutroCTA) are
   RENDERABLE via `./art scenes --check` (Gate L).
2. GATE T (type_check.py) on the empty sheet: PASS, 0 FAILs (all beats
   §8.10 SKIP — no kerning content pre-render).
3. `generate_audio_kokoro.py` — 7/7 beats, am_onyx, $0.00, durations written
   back (B00 11.48s, B01 21.23s, B02 21.03s, B03 19.86s, BCRY 8.77s, BHTF
   19.24s, BOUT 3.90s).
4. `render_scenes.py` (Manim, foreground) — 3/3 GRAPHIC beats rendered.
5. `remotion_scenes.py --only <beat>` (foreground, one beat per invocation
   after the unscoped run timed out mid-B01 render at the harness's 2-minute
   default) — 4/4 REMOTION beats rendered: B00, BCRY, BHTF (needed the
   extended 480s timeout), BOUT.
6. `compile.py` — 7/7 slots filled, content-check/frame-check/lane-check
   PASS, GATE AUDIO PASS mean_volume -24.1 dB. THE 4K LAW forced the master
   natively to 3840×2160.
7. GATE T on the compiled cut: **FAIL, 1 beat** — B03 smallest text run
   19px < floor 20px (font_size=17/18 two-line hardcoded-path labels).
   Bumped every sub-20 font_size in scenes.py to 20+, re-rendered B03,
   recompiled: **still FAIL, same 19px**, unchanged — traced by pulling the
   checker's own mid-clip sample frame (`ffmpeg -ss <clip_duration*0.5>`)
   rather than guessing from the raw Manim output: the actual small run was
   B03's untouched italic `subtitle` text (font_size=20, "installed on:
   teammate's laptop..."), not the hardcoded-path labels I'd been bumping.
   Bumped subtitle to font_size=26 (plus var_txt/hard_txt to 26 and the two
   italic "note" captions in B01/B03 to 32 for margin), re-rendered,
   recompiled: **GATE T PASS**, 0 FAILs.
8. Independently reverified with ffprobe/ffmpeg: master mtime (1788170627)
   newer than beat_sheet.json mtime (1788169631); h264 3840×2160 stream
   present, duration 106.52s; `ffmpeg -af volumedetect` mean_volume
   **-24.1 dB**, max -2.8 dB — independently confirms GATE AUDIO.
9. Gate V: pulled 13 frames at 8s spacing across the full 106.5s runtime
   plus a dedicated outro frame, and read all of them directly — B00's
   writer-open correction, B01's manifest/root-folders diagram with the
   hardcoded-path typing demo, B02's anchor plant (hardcoded path struck
   through, `$CLAUDE_PLUGIN_ROOT/scripts/check.sh` typing in, "resolves to
   wherever THIS install landed" badge), B03's anchor payoff (second
   machine, variable version checked green, hardcoded version faded with
   "no error. no warning. just doesn't run."), BCRY's carry-out quote card,
   BHTF's Your Turn composer card (mid-type and final), and BOUT's
   outro/subscribe card all read legibly with safe inset respected and no
   text overlap. Humanitarians palette (cream #F3EBDD / ink #2F2A26 /
   terracotta #E4572E / teal #1F4E5F) applied consistently. No defects found.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after 2 font-size correction passes)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: duration 106.52s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking note (compile.py):** motion histogram remotion:4 graphic:3 —
same disposition as every other 7-beat hai-simple reel in this format (B00
writer + BCRY + BHTF Your Turn + BOUT outro are REMOTION by skill contract
against 3 GRAPHIC body beats). B01/B02/B03 Manim clips were time-stretched
by compile.py to fill their measured audio durations (B01 9.0s→21.2s at
2.37x, B02 9.2s→21.0s at 2.28x, B03 6.9s→19.9s at 2.89x); spot-checked in
the Gate V frame pull, no visible artifacting (static-camera compositions).

Metadata file written: `claude-plugins-official--claude-liam-plugin-structure.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `claude-plugins-official` matches the map's
`claude-plugins` prefix — plus the direct code link per the DELIVERY
CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
