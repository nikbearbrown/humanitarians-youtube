# BUILD-LOG — claude-plugins-official--claude-liam-cardputer-buddy

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-cardputer-buddy/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `cardputer-buddy`
Claude Code plugin skill — the iterate-after-provisioning dev loop for the
M5Stack Cardputer, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the
Cardputer runs MicroPython on a /flash/ filesystem; main.py is the launcher
and scans /flash/apps/ at boot, listing every .py file as a menu entry with
no registration code; the payload has three zones (launcher, shared buddy
libraries, apps folder); hello_cardputer.py is the canonical template
(keyboard polling, font rendering, exit convention); four dev-loop scripts
each own one job — install_apps.py (full directory sync), push.py (named
subset, faster for single-file edits), tail_serial.py (serial log stream),
repl_run.py (one-shot REPL expression); PORT comes from the provisioning
step's detect.py output; and the concrete overlap between install_apps.py
and push.py — both can push a single changed file, but only push.py is
built for that job, and the distinction is easy to get wrong. B00 replaced
the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "reinstall" → "push" — the
newcomer's wrong guess that any change means the full-sync tool, corrected
toward the actual mechanism: push.py exists for exactly a single-file
change). Register re-registered Teardown→Plain: the source's B05 "gets it
right / where it bites" list (4 items each) was compressed to the single
most teachable, general-audience fact (the install_apps.py/push.py
overlap) rather than kept as a full strengths/gaps inventory — the
technical-audience gaps in the source (BLE protocol undocumented, PORT
rediscovery when detect.py hasn't been re-run, hello_cardputer.py's exact
function signatures) were dropped as assuming a technical audience
simple/hai-simple doesn't target, not as a verdict on the skill's quality.
BVDT's verdict facts were merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's four-item strengths/gaps list
compressed into NB03 (the one fact a general viewer needs and can act on);
BVDT folded into BCRY; BHTF kept, with the source's already-generic,
already-runnable prompt ("Add a timer app to the Cardputer that counts
down from 60 seconds and returns to the launcher when done") and its four
watch points carried over unchanged; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`CardputerBuddyLayout` / `CardputerBuddyScripts` / `CardputerBuddyTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-access` sibling, adapted with
cardputer-buddy-specific labels.

B00 TIMING LAW: verified `media/B00.mp4` at 10.57s (≥8s floor). Frame
pulls confirmed "reinstall" sits doomed in terracotta at t≈7s ("do I
rein|") and the corrected "do I push it?" is fully settled by t≈8s,
holding legible for the remaining ~2.5s of the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground; the run exceeded the tool's 120s timeout and was moved to
background by the harness automatically — blocked on it via `TaskOutput`
before proceeding, per the COMPLETION LAW's foreground-render rule);
NB01–NB03 rendered via `render_scenes.py`. First `type_check.py` pass was
**FAIL, 2 defects**, fixed at the root:

- **min-size §8.1, NB01** — smallest text run 17px < floor 20px, traced to
  the third chip label `"hello_cardputer.py"` (19 chars, tier-22 font size)
  needing heavy scale-down to fit the 3.2-unit chip width. Fixed by
  shortening the chip label to `"template.py"` (11 chars, tier-26 font
  size, far less scaling needed) — the filename is unchanged in narration
  and caption, only the chip label was generalized.
- **min-size §8.1, NB03** — smallest text run 13px < floor 20px, traced to
  the third chip label `"same file, different cost"` (26 chars, tier-18
  font size). First fix attempt shortened it to `"different cost"` (14
  chars, tier-26) and re-rendered — but a frame-pull spot-check (not part
  of `type_check.py`'s automated scan) caught a **second, separate defect**
  the pixel-floor check doesn't detect: the two words rendered as
  `"differentcost"` with no visible space, a content-legibility bug in the
  shared chip template specific to **bold+accented chips carrying more
  than one word** — confirmed by comparing against NB01/NB02, where every
  accented chip label (`"main.py"`, `"push.py"`) is a single word and
  renders correctly spaced. Root-caused to bold-weight Text rendering at
  extreme scale-down effectively collapsing space-glyph width for this
  font/weight combination, not to the min-size floor itself. Fixed by
  switching the label to the single word `"slower"` (6 chars) — re-verified
  by direct frame extraction (not just the automated gate) that the label
  renders as one clean word with correct kerning.

Both fixes were applied in `scenes.py`'s `BEAT_CONTENT` (the single source
of truth for chip labels) and mirrored into `beat_sheet.json`'s
`graphic.production_viz.chips` for NB01/NB03 directly (not via a full
`build_beat_sheet.py` re-run, which would have discarded the already-
measured audio durations and render stamps) before each recompile, per
COMPLETION LAW. `type_check.py` went 2→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-cardputer-buddy.mp4`, 7/7
beats filled real (no slate), 153.8s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 153.8s; mp4
  mtime (2026-08-30T22:44:29) newer than beat_sheet.json mtime
  (2026-08-30T22:42:00)
- Gate V (visual): pulled frames every 12s across the full runtime plus
  targeted checks of B00 (t≈7s "rein" doomed in terracotta, t≈8s settled
  to "push it?", held to the end of the 10.6s clip), NB01–NB03 (all chips
  legible and correctly spaced post-fix, including the twice-recompiled
  NB03), BCRY (carry-out sentence + sparkline read clean), BHTF (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible),
  and BOUT (OutroSeries: correct eyebrow "CARDPUTER BUDDY ·
  @HUMANITARIANSAI", correct title restate "Push The One File.", crimson
  underline, no truncation — a mid-fade frame at t=150s briefly appeared
  near-blank on a coarse 12s sampling grid, confirmed by finer sampling to
  be an ordinary opacity fade-in, not a dropped frame). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.57s (≥8s requirement met); the
  "reinstall" → "push" correction lands on screen by t≈8s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-cardputer-buddy.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match, not an exact-key match —
`"claude-plugins-official".startswith("claude-plugins")`), which resolves
to "Extending Claude — Skills, Plugins & Connectors"; this is a more
specific match than falling through to the `hai-simple` skill-key default
("Claude Basics"), consistent with the `claude-plugins-official--claude-
liam-access` and `claude-plugins-official--claude-liam-agent-development`
siblings built in this same family. Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-30 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-plugins-official--claude-liam-cardputer-buddy-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-cardputer-buddy/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-cardputer-buddy/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`1b6c46d2`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
