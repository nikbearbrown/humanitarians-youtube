# BUILD-LOG — knowledge-work-plugins--claude-liam-forecast

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-forecast/beat_sheet.json`
— a Teardown skill-teardown sheet for the Anthropic `forecast` sales skill
(weighted forecast, best/likely/worst, commit vs. upside, gap analysis).
The source's `metadata.source_skill` points at a Bear-machine path,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-
plugins/sales/skills/forecast/SKILL.md`, absent on this machine — same
defect class as other siblings in this family. The skill content itself is
present, unchanged, at the Cowork mirror:
`/Users/nik/Documents/Cowork/anthropics/knowledge-work-plugins/sales/skills/
forecast/SKILL.md`. Facts were re-grounded directly against that file
(stage default-probability table, Commit/Upside split, risk-flag categories,
gap analysis, the CRM-connected "supercharged" mode, and the Acme Corp /
TechStart / BigCo sample-deals block used as this reel's worked example).

**Beat count:** source is 7 beats (B00 composer-ask + B01 anatomy + B02
pipeline + B03 design tell + BVDT verdict + BHTF handoff + BOUT outro).
hai-simple's mandatory six-move spine (stakes, wrong guess, mechanism, one
flag, an anchor genuinely *planted and paid off as a pair*, both directions,
carry-out) needed room the source's 3-beat body didn't have, so the body
expanded from 3 beats to 5: NB01 (source B01+B02 merged into one mechanism
beat — the stage-weighted arithmetic) then NB02–NB05, newly authored to
carry a concrete anchor (the SKILL.md's own "Acme Corp" sample deal, planted
sitting in Commit at NB02, returned at NB04 flagged for a no-activity
re-engage) and both failure directions stated as an explicit pair (NB04:
a Commit deal can still slip; NB05: a Discovery-stage 20% deal can still
land). BVDT's Teardown verdict framing is dropped entirely; its two true
facts (same input -> same output; the output is bounded by what the
SKILL.md specifies) survive redistributed into NB01's exact arithmetic and
BCRY's carry-out ("never which deals... will actually close"). Total:
B00 + NB01-NB05 + BCRY + BHTF + BOUT = 9 beats.

**B00 WRITER LAW:** naive assumption that "forecast" means Claude predicts
which deals will actually close, corrected to "weighs" — the wrong-guess
pedagogy this reel exists to defeat (probability vs. certainty), broken
concretely at NB04/NB05 (a Commit deal can still slip; a low-odds deal can
still land). Typed text: "Does Claude / predict / which deals / will
close?", trigger "predict" -> "weigh". Narration 29 words + `lead_silence_s`
0.9 -> measured 9.37s (clears the >=9s TIMING LAW floor). Verified by frame
pull at 0.5s spacing across the full clip: "predict" typed and shown in
terracotta by t~1s, backspaced by t~3s, retyped as "weigh" and the rest of
the question completed by t~6s, held to the end of the 9.37s clip with
margin to spare.

**Body beats:** all 5 built as Manim GRAPHIC scenes via the proven generic
"chip row" renderer in `scenes.py` (title + up to 5 labeled chips, optional
arrows, optional terracotta accent/strike, caption) — copied verbatim from
the `cwc-workshops--claude-liam-forecasting` / `claude-plugins-official--
claude-liam-agent-development` siblings, not hand-tuned per beat. Anchor
pair: NB02 plants "Acme Corp / 80% odds / Commit"; NB04 returns "Acme Corp /
no activity / re-engage" — same deal, same chip-row composition, confidence
turning out not to be a guarantee. One flag: NB03 (CRM-connected reels swap
the generic default stage-probability table for the team's own historical
win rates — everything upstream of that is a stated assumption). Both
directions: NB04 (Commit can still slip) / NB05 (a low-odds deal can still
land, and the gap analysis is a number, not a list of names). Close: BCRY
`WantQuote` (carry-out), BHTF `ClaudeComposerAsk` (explicit
`folderLabel: "@HumanitariansAI"` per the known ClaudeComposerAsk-defaults-
to-@NikBearBrown bug documented on prior sibling builds — confirmed correct
in the rendered frame), BOUT `OutroSeries` (@HumanitariansAI).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (9 beats), `scenes.py` (generic chip-row Manim generator +
5-beat content table), `render_scenes.py`. Ran `generate_audio_kokoro.py`
(9/9 beats, am_onyx, $0.00) in the foreground — measured durations became
the clock. Rendered 5 Manim beats via `render_scenes.py` (foreground, all
5 succeeded first pass) and 4 Remotion beats via `remotion_scenes.py`; the
Remotion step exceeded the shell's 120s default and was auto-moved to
background by the harness mid-render — per this invocation's one-shot rule
(no later turn exists to receive that notification), blocked in-turn
polling the actual OS process (the node `remotion_scenes.py` PID, then the
compositor-darwin-x64/ffmpeg encoder PID for each beat) until exit code 0,
verifying all four `media/*.mp4` files existed before proceeding. Same
one-shot polling discipline applied to `compile.py`, which also exceeded
120s and was moved to background — blocked on its PID until it exited 0.
No orphaned renders.

**GATE T (type_check.py):** PASS, 0 FAILs on the first pass — no fixes
needed.

Compiled with `compile.py`: 9/9 beats real (no slate), master born natively
4K (3840x2160, `compile.py`'s 4K LAW), 118.9s. `content-check`/`frame-check`/
`lane-check` all PASS. Non-blocking warning: motion histogram `graphic:5
remotion:4` (55%, over the ~40% pantry cap) — logged as structural, not a
defect: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION
against 5 Manim body beats for a 9-beat reel, same disposition as every
sibling in this family.

**Gate V:** pulled frames at 8s spacing across the full 118.9s runtime (15
frames) plus a finer 0.5s-spaced sweep of B00 alone to verify the writer
correction; read every one directly. All 9 beats legible, correctly inset,
no text overlap, no truncation. NB01-NB05 chip rows all read clean at their
intended font tier (chip labels kept <=14 chars to stay in the top tier).
BHTF shows the correct topic/title/@HumanitariansAI handle and the full
paste-ready pipeline prompt. BOUT (OutroSeries) shows "FORECAST ·
@HUMANITARIANSAI" eyebrow and "Weighed, Not Predicted." title with the
crimson underline, no truncation. No remaining blockers.

**Audio:** ffprobe confirms an AAC stream present alongside 3840x2160 h264
video; master mtime (22:09:39) newer than beat_sheet.json mtime (22:07:15).
Independent `ffmpeg -af volumedetect` (not just compile.py's own GATE AUDIO
line): mean_volume **-23.9 dB**, max -2.9 dB — comfortably above the -40 dB
floor.

Metadata file written: `knowledge-work-plugins--claude-liam-forecast.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Playlist note: `SUBJECT.json`'s `family` is
`"knowledge-work-plugins"`, which has a direct, exact-match entry in
`skills/make/hai-simple/loop/playlists.json`'s map (not the `hai-simple`
fallback or `_default`). Per the DELIVERY CONTRACT format, the description
also carries the direct code link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
