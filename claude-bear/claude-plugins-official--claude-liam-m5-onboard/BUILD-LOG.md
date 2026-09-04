# BUILD-LOG — claude-plugins-official--claude-liam-m5-onboard

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-m5-onboard/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the `m5-onboard` Claude Code
plugin-dev Skill: M5Stack ESP32 cold-start provisioning — detect, identify,
flash UIFlow 2.0, install a MicroPython app bundle — already fully built;
no SCRIPT.md, source `beats[*].narration_text` served as the locked
script). Built entirely fresh this invocation — only SUBJECT.json existed
on pickup.

Question, facts, and body argument carried over unchanged: one orchestrator
(`onboard.py --apps buddy`) runs four stages — Detect (enumerates USB ports,
port name differs by OS, confirms the chip), Identify (hardware-signature
guess, but final variant choice is always explicit, never guessed — two
boards share the same USB VID and guessing wrong boot-loops the device),
Flash (writes UIFlow 2.0, 460800 baud UART / 115200 no-stub native USB),
Install (uploads .py files, reboots via machine.reset); the run takes 2-3
minutes so it goes in the background with output streamed to a log (a
silent terminal for 3 minutes looks like a crash); and on native-USB
boards, entering flashing mode has no software path — the source states
plainly there is no DTR/RTS or esptool-flag substitute, so the script waits
for a physical button dance (hold BtnG0, tap RST while still holding,
hold one more second, release). B00 replaced the source's `ClaudeComposerAsk`
typed-ask cold open with `BrutalistHesitantWriter` (WRITER LAW: "zero" →
"one" — the newcomer's wrong guess that automating detect/identify/flash/
install into one command means zero manual exceptions, corrected toward
the actual mechanism: exactly one stage still needs a human hand). Register
re-registered Teardown → Plain: the source's B05 "gets it right / where it
bites" list (5 strengths, 4 gotchas: variant question easy to miss, NVS
set_str/set_blob boot-loop bug buried in gotchas, BLE OSError -519 opaque,
Linux dialout group / Windows Store Python PATH buried in platform notes)
and BVDT's verdict recap were both dropped as their own beats — NB03
instead generalizes the button-dance mechanism itself (the DTR/RTS
contrast the source states directly inside B02's prose: "reboots via
machine.reset rather than DTR/RTS, which is a no-op on native USB") into a
both-directions payoff, since that's the single fact a general audience
without hands-on ESP32/NVS debugging experience can actually use, versus
the harness-internals gotcha list which assumes that experience. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01
kept as one beat; B02's four patterns (variant ambiguity, background+log,
button dance, install-only mode) split across NB02 (first three, ending on
the button dance as the planted anchor) and NB03 (the DTR/RTS contrast
generalized into the both-directions payoff; install-only mode dropped as a
secondary CLI detail not needed for the carry-out); B05+BVDT folded into
BCRY; BHTF kept as the your-turn handoff, rewritten to a prompt runnable by
any viewer today (ask Claude to name the physical step before running
anything) rather than the source's five-point hardware-test checklist,
which assumes the viewer already owns a Cardputer-Adv; BOUT kept. Full audit
in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`M5OnboardAnatomy` / `M5OnboardDesign` / `M5OnboardTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01-NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`), copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling and
adapted with m5-onboard-specific labels.

**B00 TIMING LAW — one real defect caught and fixed, not a QC-sampling
trap.** First render used a MULTI-WORD trigger ("No human steps" →
"One button dance"). Frame pulls at t=9.5s, t=10.3s, and t=10.7s (the
clip's near-final and last frames) all showed the uncorrected naive text
"Flash my board with one script. No human steps, right?" still on screen,
never corrected. Root-caused by reading `BrutalistHesitantWriter.tsx`'s
`buildActs()`: trigger matching is `triggers.indexOf(core.toLowerCase())`
where `core` is a single whitespace-tokenized, punctuation-stripped word —
a multi-word trigger phrase can never equal any single token's core, so the
special replacement branch never fires and the writer just types the full
naive text verbatim with ordinary typo/hesitation jitter, holding it
uncorrected for the rest of the clip. Fixed by redesigning the on-screen
text around a single-word trigger: "Flash my board / with one script — /
zero / exception?" with `triggerWords: "zero"`, `replacementWords: "one"`
— narration also rewritten to match ("zero exceptions" → "the one
exception"). Regenerated B00's audio only (10.62s) and re-rendered B00 only
(media/B00.mp4; other beats' stamps unaffected). Reverified by frame pull:
"zero" sits doomed in terracotta at t≈3.8s, the full corrected question
"Flash my board with one script — one exception?" is settled and legible
by t≈5s, and holds to the end of the 10.6s clip (well past the ≥8s TIMING
LAW floor).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 regenerated once after the text fix via `--only B00`);
NB01-NB03 rendered via `render_scenes.py` (manim, foreground, first pass
clean); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground;
both the full-sheet run and the B00-only re-render exceeded the tool's 120s
timeout and were moved to background by the harness automatically —
blocked on each via `TaskOutput` before proceeding, per the COMPLETION
LAW's foreground-render rule, never treating a backgrounded render as
"handled" without waiting on it). `type_check.py` ran clean first pass:
GATE T PASS, 0 FAILs, 7/7 beats checked (the §8.10 SKIP lines are the
advisory redundancy check, no exit effect). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-m5-onboard.mp4`, 7/7 beats
filled real (no slate), 142.5s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect)
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 142.5s; mp4
  mtime newer than beat_sheet.json mtime
- Gate V (visual): pulled frames across the full runtime (t=15/25/45/60/
  75/90/105/118/130/138s) plus targeted B00 checks (t≈3.8s "zero" doomed
  in terracotta, t≈5-10.6s settled+correct). NB01 (detect→identify→flash→
  install, flash accented), NB02 (same USB ID / background+log / button
  dance, button dance accented), NB03 (native USB / button dance / USB
  bridge / software reset, software reset accented) all legible, correct
  humanitarians palette, one accent moment each, no overlap or truncation.
  BCRY carry-out + sparkline read clean. BHTF shows correct topic/title/
  @HumanitariansAI handle with the paste-ready prompt legible (mid-typing
  animation frame, expected). BOUT (OutroSeries): correct eyebrow
  "M5-ONBOARD · @HumanitariansAI", correct title restate, crimson
  underline, no truncation. No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.6s (≥8s requirement met); "zero" →
  "one" correction lands on screen by t≈5s and the full corrected question
  stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-m5-onboard.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors"; more specific than the `hai-simple` skill-key
default ("Claude Basics"). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
