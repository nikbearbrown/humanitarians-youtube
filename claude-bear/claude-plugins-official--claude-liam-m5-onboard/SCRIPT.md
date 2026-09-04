# SCRIPT.md — The One Step No Script Can Skip. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-m5-onboard` (Teardown, walks the `m5-onboard` Claude
Code plugin-dev Skill: M5Stack ESP32 cold-start provisioning — detect,
identify, flash UIFlow 2.0, install a MicroPython app bundle) — question,
facts, and body argument carried over; narration re-registered to Plain
(explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed one script could flash this board with zero hands-on steps.
It can't — one button dance still has to happen by hand. So: flash my board
with one script. One button dance, right?

*(Text typed on screen: "Flash my board / with one script. / No human
steps, / right?" — trigger words "No human steps" correct to "One button
dance", landing on: "Flash my board with one script. One button dance,
right?" `lead_silence_s: 0.8` gives the typing its window; TIMING LAW
requires `media/B00.mp4` ≥ 8s and the correction visibly landed — verify by
frame pull after render.)*

## Body — the four stages, the one physical step, and when it isn't needed

**NB01 — One command, four stages** (source B01, anatomy)
The whole workflow runs through one command: onboard.py --apps buddy.
Underneath, that's four stages. Detect finds the board over USB — the port
name differs by system, usbmodem on macOS, ttyACM or ttyUSB on Linux, COM on
Windows — then confirms the actual chip. Identify checks hardware
signatures for a likely firmware match, but the final choice is always
stated explicitly, never guessed. Flash writes the firmware itself. Install
copies the real program files onto the board and restarts it. Two smaller
tools exist for narrower jobs: pushing just the app bundle to a board
that's already flashed, or running a hardware check afterward.

**NB02 — The button dance** (source B02, design — anchor planted)
Three things matter once you're actually running this. First: two boards
share the exact same USB signature, so the script can't tell them apart on
its own — guess the variant wrong and the device boot-loops. Second: a full
run takes two to three minutes, so it goes in the background with its
output streamed to a log file; a silent terminal for three minutes looks
exactly like a crash. Third, the flash step itself: on boards that connect
over native USB, there's no software line the script can pulse to reset the
chip into flashing mode — so it's a physical dance. Hold one button, tap
reset while still holding it, hold one more second, then let go. The script
waits for a person to actually do that.

**NB03 — Native USB vs. bridge** (source B02's DTR/RTS detail, generalized —
anchor paid off, both directions)
That physical step isn't universal. It's needed only because native-USB
boards have no control line the script can pulse to force a reset — the
standard software trick, toggling two control lines, is simply a no-op
there. Boards that connect through a separate USB-to-serial bridge chip skip
the button dance entirely: that same software trick works normally, and the
whole flash step runs through without anyone touching the board. Same
script, same command — which path it takes depends entirely on which USB
hardware happens to be inside.

## Close

**BCRY — carry-out**
One script can detect, identify, flash, and install this board — every
stage but one. The button press stays a human's job. No flag replaces a
thumb.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm using the m5-onboard skill to set up
a new M5Stack board. Before you run anything, tell me exactly which stage
needs me to physically touch the device, and what that button sequence
actually is. Then watch: does Claude name the button dance before it
starts, or does it just launch the script and wait?

**BOUT — outro**
The One Step No Script Can Skip. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an automation question — does "one script" mean zero hands-on steps? |
| Wrong guess | B00 (WRITER LAW) | "No human steps" corrects to "One button dance" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the four-stage pipeline behind one command; the three patterns that actually matter once running it, ending on the physical button-dance mechanism itself |
| Anchor | the button dance, planted at B00 and NB02, paid off at NB03 | NB03 returns to the same physical action to show the boundary condition that makes it apply — the anchor is recognizable as the same object both times (hold-tap-hold-release) |
| Both directions | NB03 | states both directions concretely: native-USB boards need the button dance because the software reset is a no-op there; USB-bridge boards get the same software reset working normally, so no button dance is needed |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the source Skill's build documents (the four-stage orchestrator, the
shared-USB-signature variant ambiguity, the background+log run pattern, the
native-USB button-dance requirement, and the DTR/RTS software-reset contrast
the source itself states when describing the install-stage reboot: "reboots
via machine.reset rather than DTR/RTS, which is a no-op on native USB" —
implying DTR/RTS is the real, working software reset on non-native-USB
boards). Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy / design)
+ B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01 kept as one beat; B02's four patterns
(variant, background+log, button dance, install-only mode) are split across
NB02 (the first three, ending on the button dance as the anchor) and NB03
(the DTR/RTS contrast the source itself states inside B02's prose,
generalized into the both-directions payoff — install-only mode is dropped
as a secondary CLI detail, not a fact the carry-out needs); B05's long
"gets it right / where it bites" list (five things praised, four gotchas
named: variant question easy to miss, NVS set_str/set_blob boot-loop bug
buried in gotchas, BLE OSError -519 opaque, Linux dialout group and Windows
Store Python PATH buried in platform notes) and BVDT's verdict recap are
both dropped from their own beats — the single most generally teachable,
already-anchored fact (the button dance's boundary condition) is kept as
NB03 instead of the harness-internals gotcha list, which assumes hands-on
ESP32/NVS debugging experience simple/hai-simple's general audience doesn't
have; Teardown framing ("gets it right," "where it bites," the verdict
recap) is stripped entirely, per the NO JUDGMENT register check; BHTF kept
as the your-turn handoff, rewritten to a prompt any viewer can paste today
without owning the specific hardware (ask Claude to name the physical step
before running anything) rather than the source's five-point hardware-test
checklist, which assumes the viewer already owns a Cardputer-Adv; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`M5OnboardAnatomy` / `M5OnboardDesign` / `M5OnboardTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
