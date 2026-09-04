# BUILD-LOG — cwc-workshops--agent-decomposition-skills-vs-tools

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/agent-decomposition-skills-vs-tools/beat_sheet.json`
(Teardown register, Code with Claude 2026 Workshop W5). Picked up mid-build:
SUBJECT.json, QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (15
beats fully authored), TYPECHECK.md (GATE T PASS), all mp3 narration, and
manim/B01–B11.mp4 already existed on pickup; media/B00.mp4 and
media/BCRY.mp4 existed, media/BHTF.mp4 and media/BOUT.mp4 did not. No prior
BUILD-LOG.md — this is the first log entry.

Question/facts/case unchanged from the source: a 402-line prompt with 12
tools ran a daily low-stock sweep in 102 tool calls / 488 seconds; splitting
the same knowledge across three levers (tools = stateless calls, skills =
loaded on demand, subagents = own context window) gets the same task done
in 3 scripts / ~100 seconds, same correctness. B00 replaced the source's
puppet-style open with `BrutalistHesitantWriter` (WRITER LAW: "more" ->
"fewer" — the newcomer's guess that a slow agent needs more tools/context/
instructions, corrected toward: cutting the prompt is what makes it
faster). Register re-registered Teardown->Plain: the source's implicit
endorsement of the three-lever split as good engineering was dropped from
BCRY, which states the fact (load only what's needed, when it's needed) and
stops. One flag (S08) kept exactly: the 5x/100s numbers are one team's
measurement on one workflow. Both-directions (S10/S11) and the anchor
plant/payoff (S03/S09) carried over unchanged. Close carries the
Humanitarians AI skin per hai-simple SKILL.md.

No source beat was ai-video-prompt, pantry, or a human-drop slot — every
body beat (B01-B11) is GRAPHIC via the shared Manim scenes.py/
render_scenes.py pipeline; B00/BCRY/BHTF/BOUT are REMOTION. NO-GENAI/
NO-PANTRY LAW required no substitution.

**Work done this invocation:**

1. Rendered the two missing REMOTION beats: `BHTF` (ClaudeComposerAsk,
   17.7s) and `BOUT`. First `remotion_scenes.py <REEL>` (no `--only`) call
   timed out at the tool's 3-minute limit mid-render; re-ran targeted
   (`--only BHTF`) with a longer foreground timeout and it completed
   cleanly — no process was ever backgrounded or left orphaned by this
   invocation (a `ps` check found long-running orphaned chrome-headless-
   shell processes elsewhere on the machine, ~2 days old, unrelated to this
   reel or this run — left alone).
2. First compile (`compile.py`, 15/15 filled, GATE AUDIO PASS -24.0 dB,
   3840x2160 native) — content-check/frame-check/lane-check all PASS.
3. **Gate V caught one real defect.** BOUT used `ClaudeTitleOutro`, which
   is HARDCODED to `@NikBearBrown` and always renders the Claude mascot
   (see `ClaudeTitleOutro.tsx`'s own doc comment: "for claude-liam /
   @NikBearBrown reels ONLY... Other channels (HAI, Medhavy, Musinique) use
   their own outro components — never this one"). The beat sheet's
   `handle`/`subline` props were silently ignored by the locked component,
   so the rendered frame read "@NikBearBrown" plus the Claude mascot glyph
   under a HAI-branded video — a Claude-wash of the outro, which
   hai-simple's SKILL.md explicitly refuses ("HAI keeps its own skin").
   Confirmed against a finished sibling in this exact skill
   (`claude-plugins-official--claude-liam-agent-development`, BOUT beat)
   that the house pattern for hai-simple's single-beat close is
   `OutroSeries` with `eyebrow`/`line` props, not `ClaudeTitleOutro`. Fixed
   `beat_sheet.json`'s BOUT beat to `OutroSeries` (`eyebrow: "AGENT
   DECOMPOSITION · @HumanitariansAI"`, `line`: the title restated),
   re-rendered BOUT only, recompiled. Reverified by frame pull: eyebrow and
   title-restate legible, crimson underline present, no Claude branding.
4. All other beats read clean on Gate V frame pulls at ~6s intervals across
   the full runtime (B00 correction visible and held, B03/B09 anchor card
   pair consistent, B05 three-lever labels legible, B07 boundary-crossing
   diagram clean, B08 flag pill + hedge caption legible, B10/B11 mirrored
   construction clean, BCRY carry-out + sparkline clean, BHTF prompt card
   legible with correct @HumanitariansAI handle). No blockers.

Compiled: `cwc-workshops--agent-decomposition-skills-vs-tools.mp4`, 15/15
beats filled real (no slate), 164.7s, 3840x2160 (native 4K — compile.py's
4K LAW forced it directly; no separate low-res review pass was needed).

**Gates:**
- content-check: PASS (15 beats, no violations)
- frame-check: PASS (3840x2160, 15 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs (see TYPECHECK.md, run on pickup)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio (aac, 48kHz) present, duration
  164.6s; mp4 mtime (1788229806) newer than beat_sheet.json mtime
  (1788229727)
- Gate V (visual): pulled frames at 6s intervals across the full runtime
  plus a targeted re-check of the fixed BOUT beat. No blockers after the
  outro fix.
- Advisory: compile.py flagged `graphic` motion share at 73% (11/15 beats),
  over the ~40% pantry-cap guideness in MOTION.md — inherited from the
  source's beat structure (11 GRAPHIC body beats is the source's own
  shape); not treated as a blocker since it mirrors the locked
  redo-contract beat count, logged here per honesty rules rather than
  silently overridden.

Metadata file written: `cwc-workshops--agent-decomposition-skills-vs-tools.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). SUBJECT.json's
family (`cwc-workshops`) has no entry in `playlists.json`; falling through
to the `hai-simple` skill-key entry resolves to "Claude Basics" per the
map's documented fallback order. Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
