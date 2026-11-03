# BUILD-LOG — skills--claude-liam-webapp-testing

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-webapp-testing/beat_sheet.json`
(Teardown source examining Anthropic's `webapp-testing` skill, already
fully built, 7 filled beats). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and body argument carried over unchanged: the two-branch
decision tree (static HTML: read the file, script against a `file://` URL;
dynamic webapp: needs a running server); the sub-branches for
server-not-running (`with_server.py --help` first, then start through the
helper) vs. server-already-running (straight to recon); the
reconnaissance-then-action loop (navigate + wait networkidle, screenshot
or inspect, identify selectors from what actually rendered, then act); the
critical rule that inspecting before networkidle shows placeholder
elements, not real content; `with_server.py`'s single-server
(`--server`/`--port`) vs. two-server (`--server` passed twice)
usage; the Playwright pattern (sync_playwright, headless Chromium,
`wait_for_load_state('networkidle')`, close when done, descriptive
selectors over absolute XPath); the three example scripts
(`element_discovery`, `static_html_automation`, `console_logging`); and the
source's own gets-right/bites list (framing, decision tree, networkidle
warning, `with_server.py`, examples ship / no error-recovery guidance,
undescribed examples directory, no sample `--help` output, no auth/session
guidance, no CI/headless notes). The source's Teardown "gets right/bites"
framing was split into this reel's WRONG-GUESS (guess -> break) and
BOTH-DIRECTIONS beats instead of one lumped verdict beat, per Plain
register.

B00 replaced the source's `ClaudeComposerAsk` cold open (already REMOTION,
not a puppet ask — NO-GENAI/NO-PANTRY LAW required no substitution there)
with `BrutalistHesitantWriter`: WRITER LAW correction "loads" -> "settles"
— the newcomer's wrong guess that a page which has loaded is already safe
to test, corrected toward "settles," which previews the reel's central
networkidle insight. B00 audio measured 10.01s (actual_duration_s),
clearing the >=9s TIMING LAW window on the first pass; the "loads" word
verified fully typed in terracotta (doomed) at t=5.0-5.8s, struck and
retyped to "settles?" in ink, settled and legible through clip-end at t=9s
(frame-verified, not assumed).

Source's `WebappTesting*.tsx` components (`Anatomy`, `Patterns`, `Tell`)
were not reused — same seam already logged on the `docx`/`claude-api`/
`mcp-builder` siblings (Claude-fidelity token imports, no ink/accent/bg
props). Built fresh instead as 11 GRAPHIC (Manim) chip-row beats
(NB01-NB11) by copying the `claude-liam-docx` sibling's proven generic
template (`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`) and
swapping in webapp-testing content, carrying the same facts in the
humanitarians palette (#F3EBDD/#2F2A26/#E4572E). One concrete ANCHOR:
the ask "a local React app on port 3000 — click Submit on a login form,
check for a success message" (lifted from the source's own BHTF handoff
line), planted at NB02, paid off at NB09 with the helper starting the
server, Claude waiting for idle, screenshotting, and finding Submit by its
visible text before clicking. Landing at 15 beats total: B00 + 11 GRAPHIC
body + BCRY + BHTF + BOUT (source's 7 beats grew to 15 to give
WRONG-GUESS/BREAK and BOTH-DIRECTIONS their own dedicated beats and to
carry the anchor plant/payoff — see SCRIPT.md's "Beat-count note").

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/webapp-testing/SKILL.md`) could not
be located at that path on this machine — only the built reel folder
exists under `anthropics/skills/youtube/`, not a source
`skills/webapp-testing/` directory. Per the redo contract, facts are
carried over unchanged from the locked source script rather than
re-verified against a live file that could no longer be located.

`generate_audio_kokoro.py` (15 beats, $0.00) clean, first pass.
`render_scenes.py` (11 GRAPHIC beats, foreground) clean, first pass.
`remotion_scenes.py` (B00/BCRY/BHTF/BOUT, foreground, auto-backgrounded by
the harness past its 120s timeout — blocked on it via `TaskOutput(block=
true)` before proceeding, confirmed exit 0) clean, first pass.

**GATE T (type_check.py), real defects found and root-caused, not
papered over:**

Ran `type_check.py` once BEFORE `compile.py` by mistake — it reported 4
bbox-overlap FAILs (NB05, NB08, NB10, NB11), but investigation showed
`beat.build.status` (which the pattern-matching depends on) is only
stamped by `compile.py`, so the exemption-matching logic could not even
run yet on that pass; re-ran after compiling and got the same 4 real
findings against the correctly resolved scene classes. Root-caused each
by reading `type_check.py`'s own `text_run_bboxes()` filter (confirms the
TERRA accent underline is excluded — flat bars with w>h*15 are filtered
before the overlap check ever sees them) and then direct frame pulls +
tight pixel crops at each flagged beat: NB05 ("WAIT-FOR-IDLE" accented
chip), NB08 ("NOT-RAW-XPATH" accented chip), NB11 ("LOGIN-WALLS" accented
chip), and NB10 (the title "WHAT ONE WAIT CATCHES") all render with
completely clean, fully separated glyphs and normal hyphen/word spacing —
the same bold-serif diagonal-letter bounding-box false-positive class
already extensively documented and exempted elsewhere in `type_check.py`
(e.g. `BDNB07Scene`/`BPB03Scene`). Registered `BDNB05Scene`, `BDNB08Scene`,
`BDNB10Scene`, `BDNB11Scene` in `BBOX_OVERLAP_EXEMPT_PATTERNS` with a
verification comment, per established precedent — the content itself was
not touched for these four.

NB10 additionally carried one REAL min-size defect (found on the same
pass): the third chip label "COMMON-FAILURE-STOPPED" (23 chars) autoscaled
to 18px, 2px under the 20px floor. Fixed by shortening to
"COMMON-FAILURE-STOPS" (20 chars, fits the <=22-char/fs=22 tier) in
`scenes.py`, `build_beat_sheet.py`, and `beat_sheet.json`; re-rendered
NB10 only. GATE T: 4 FAILs -> PASS, 0 FAILs (final, after this single
round of fixes — content fix for the real defect, exemption registration
for the four verified false positives).

**Gate V (visual), one real defect found and fixed, not caught by GATE T:**
frame pulls every 8s across the full 151.4s runtime (19 frames) plus
targeted crops surfaced a genuine legibility collision GATE T's checks
don't cover: BHTF's `ClaudeComposerAsk` topic prop
"WEB APPLICATION TESTING · ANTHROPIC SKILL" wrapped to two lines inside
the card, and the wrapped second line ("SKILL") printed with its
descenders nearly touching the "TESTING" segment label directly beneath
it — confirmed by a tight pixel crop, not a false read. Fixed by
shortening the topic to "WEBAPP TESTING · SKILL" (fits one line, matching
the working length used by the `docx` sibling's "DOCX · ANTHROPIC SKILL");
re-rendered BHTF only, re-verified clean by frame pull before recompiling.
No other blockers: every chip label and title legible with normal
word-spacing, safe inset respected, single accent per beat, B00's
"loads"->"settles" correction visible on screen well within the clip,
BCRY/BHTF/BOUT show the correct carry-out line, paste-ready prompt,
@HumanitariansAI handle, and title/subline restate.

Compiled clean on the final `compile.py --force` pass: **15/15 beats real**
(no slate), native 4K (3840×2160), **151.439s** (ffprobe-verified,
independent of compile.py's own summary line), mp4 mtime newer than
beat_sheet.json.

**Gates:**
- content-check: PASS (15 beats, no violations)
- frame-check: PASS (3840×2160, 15 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (independently ffmpeg
  volumedetect-verified), max -2.9 dB
- ffprobe (independent, not compile.py's self-report): video 3840×2160
  h264 @24fps, audio present (aac), duration 151.439s; mp4 mtime newer
  than beat_sheet.json mtime
- Gate V (visual): pulled frames every 8s across the full 151.4s runtime
  (19 frames) plus targeted crops of B00's mid/late correction and the
  BHTF topic-wrap collision (found and fixed, see above). No blockers
  remaining after the fix.
- B00 TIMING LAW: `actual_duration_s` 10.01s (>=9s requirement cleared);
  the "loads"->"settles" correction lands on screen well within the clip.

**Non-blocking warning (compile.py):** motion histogram graphic:11
remotion:4 — graphic at 73%, over the ~40% pantry cap in MOTION.md. This
is structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
REMOTION against an 11-beat GRAPHIC body — the ratio follows beat count,
not a choice made in this build. Same disposition as every sibling in
HAILOOP-LOG.md. Logged per the honesty rule rather than reworking beat
count to dodge the warning.

Playlist resolution: SUBJECT.json's family (`skills`) has no literal
prefix match in `playlists.json` (no key equals or prefixes "skills"), and
the skill-name fallback (`hai-simple` -> "Claude Basics") would misfile
this — the reel's actual subject is an Anthropic Agent Skill's anatomy and
mechanism, a direct content match for the map's `claude-skills`/
`claude-agent-skills`/`claude-plugins` prefixes -> **"Extending Claude —
Skills, Plugins & Connectors."** Same override reasoning already
established by the `docx`, `claude-api`, and `mcp-builder` siblings.
Metadata file written: `skills--claude-liam-webapp-testing.md` (channel
@HumanitariansAI). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
