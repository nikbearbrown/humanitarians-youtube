# BUILD-LOG — financial-services--claude-liam-fsi-strip-profile

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-fsi-strip-profile/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `fsi-strip-profile`
Skill — an `investment-banking` vertical-plugin Skill, financial-services
family — already fully built; no SCRIPT.md existed for the source, so its
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Unlike the `comps-analysis` redo (whose source Skill file no longer
resolves on this machine), `strip-profile/SKILL.md` **was found and read in
full** at
`/Users/nik/Documents/Cowork/anthropics/financial-services/plugins/vertical-plugins/investment-banking/skills/strip-profile/SKILL.md`.
The source's own narration for B00/B03/BVDT/BHTF carried the same unfilled
batch-template placeholder (`│`) as several other redos in this family
(confirmed via the source dir's `PEDAGOGY.md`, which logs only "Batch
build — skill teardown format"), but because the real file was available
this time, the gap was filled with the file's own specific, verified
mechanism rather than a generic placeholder-substitute: the Workflow
section's scope question before research (§1: "Only after user confirms,
proceed to research"), the one-slide-at-a-time build with mandatory user
approval (§3: "You MUST create ONE slide at a time and get user approval
before proceeding to the next slide"), and the mandatory image-render-and-
inspect step before every approval (§3.2–3.3: "MANDATORY: Convert to image
for review" / "MANDATORY VISUAL REVIEW: Text overlap check... Text cutoff
check... Chart boundary check... Quadrant integrity").

Question, facts, and body argument carried over from the source's shape;
register re-registered Teardown → Plain (verdict/strengths-gaps framing
dropped, mechanism facts kept). B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "trust" → "check" —
the newcomer's wrong guess that Claude just trusts the slide it generated,
corrected toward the actual mechanism: it renders the slide to a picture
and checks it first). Source's BVDT verdict facts were merged into the
single BCRY carry-out sentence per CARRY-OUT LAW. BHTF's prompt uses Nike
as the worked example — not invented, but the Skill's own named reference
(`examples/Nike_Strip_Profile_Example.pptx`, cited in its "Visual
Reference" section). Close re-skinned to @HumanitariansAI (`OutroSeries`).
Full six-move / one-flag / beat-count audit in SCRIPT.md.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). Kept the same 7-beat shape: B00 carries the wrong-guess pedagogy
per WRITER LAW instead of a dedicated beat; B01→NB01 kept as anatomy;
B02→NB02 upgraded from the source's generic "reads steps in order" framing
to the file's actual first pipeline step (ask scope, wait for yes, then
research) — a strengthening, not a contradiction; B03+BVDT→NB03+BCRY carry
the file's actual design tell (render-to-image-and-inspect loop) instead of
the unrecoverable Teardown gets-it-right/bites-you framing. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`financial-services--claude-liam-comps-analysis` sibling, adapted with
fsi-strip-profile-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`). B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground;
the run exceeded the tool's 120s timeout and was moved to background by the
harness automatically — blocked on it via `TaskOutput` before proceeding,
per the COMPLETION LAW's foreground-render rule); NB01–NB03 rendered via
`render_scenes.py` (foreground, completed within the timeout).

**Two real defects found and fixed this build, both caught by direct frame
inspection rather than trusting a script's own success message:**

1. **B00 TIMING LAW defect.** First attempt (69-char on-screen text against
   a 9.34s narration) did not finish typing before the clip ended — frame
   pull at t=9.1s showed `"the slide it buil|"`, missing `"t?"`. Root cause:
   `remotion_scenes.py` sizes B00's render duration directly from
   `actual_duration_s` (the narration audio length) — `lead_silence_s` is
   **not** added to the render duration by this script, contrary to what
   the SKILL.md's TIMING LAW framing implies. Fixed by shortening the
   on-screen text (69 → 46 chars: "Does Claude trust the strip profile it
   builds?") rather than inflating narration length further, keeping the
   same typing-speed parameters proven on the `comps-analysis` /
   `agent-development` siblings (42ms/char, 8% hesitateBetween, 4%
   mistakeRate). Re-verified by frame pull: full corrected question settled
   by t≈8.7s, clip ends at 9.03s.

   **A second, independent bug surfaced while fixing the first:**
   `remotion_scenes.py`'s own `extend_clip_to_duration()` step printed
   `"ok: ... (extended to 9.0s)"` but the installed `media/B00.mp4` was
   actually the raw, un-trimmed 20.2s composition render (ffprobe measured
   20.245s against a stamped `actual_duration_s` of 9.02). The function
   does not check its own `ffmpeg` subprocess's exit code before reporting
   success, so a failed trim/pad silently leaves the untouched raw render
   in place. Root-caused by re-running the identical `tpad=stop_mode=clone`
   + `-t` ffmpeg command by hand (exit 0, confirmed 9.033s output) and
   installing that file in place of the raw render. **MISSING:** this
   script gap (silent-failure success message) is a toolkit defect, not
   something this reel's build can fix — logged here rather than patched,
   per the skill's file-ownership boundary.

2. **Chip label word-space collapse (Manim/Pango bug), broader than the
   documented single-word-first case.** GATE T's first pass failed on
   NB03 min-size (an 18px run under the 20px floor from an over-long chip
   label), fixed by shortening labels — which then exposed a second,
   purely visual defect GATE T's automated checks do not catch: multiple
   chip labels rendered with their inter-word space fully collapsed —
   `"render image"`→`"renderimage"`, `"check overlap"`→`"checkoverlap"`,
   `"ask you first"`→`"askyou first"`, `"wait for yes"`→`"waitforyes"` —
   caught only by reading actual compiled frames (Gate V), not by
   type_check.py, which passed clean throughout. Isolated with a series of
   throwaway Manim test renders (`/tmp/spacetest/test*.py`, outside the
   reel) rather than guessing: confirmed the collapse is real (not a
   preview artifact) and word-pair-specific — `"then research"`,
   `"check the picture"`, `"look at it"`, `"picture check"`, `"spot
   overlap"`, `"scope first"` all render with normal spacing at identical
   font/size, while `"ask you"`, `"wait for"`, `"render image"`, `"check
   overlap"`, `"ask first"`, `"render it"`, `"check it"` collapse. A
   further isolated test at BOLD weight (matching the actual accented-chip
   styling) found an *additional*, narrower trigger: `"your yes"` and
   `"your approval"` collapse under BOLD specifically (`"you approve"` and
   `"the approval"` at the same weight do not) — a defect invisible in the
   first isolated test, which used NORMAL weight. Root-cause fix: reworded
   rather than patched around, per the `comps-analysis` sibling's precedent
   — final chips: NB02 `["scope first", "you approve", "then research"]`
   (accent=1), NB03 `["picture check", "spot overlap", "the approval"]`
   (accent=2), all confirmed clean by both the isolated test renders and a
   full frame-pull re-check of the actual compiled beats after
   re-rendering. `beat_sheet.json`'s `graphic.production_viz.chips` and
   `scenes.py`'s `BEAT_CONTENT` were kept in sync at each edit;
   `build_beat_sheet.py` updated to match for reproducibility.

Compiled three times total (initial, then after each of the two fixes
above):

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Final result: `financial-services--claude-liam-fsi-strip-profile.mp4`, 7/7
beats filled real (no slate), 78.2s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the min-size fix above; the word-space
  collapse defect is NOT caught by this automated gate — see Gate V)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 78.18s; mp4
  mtime (1788303522) newer than beat_sheet.json mtime (1788303401)
- Gate V (visual): pulled frames across the full runtime after each fix
  (B00 at t≈2/4.3/8.7s for the WRITER LAW correction; NB01 anatomy chips;
  NB02/NB03 chips post-respace-fix; BCRY carry-out quote + sparkline; BHTF
  correct topic/title/@HumanitariansAI handle and legible paste-ready Nike
  prompt; BOUT correct eyebrow "FSI-STRIP-PROFILE · @HumanitariansAI" and
  title restate). Both defects above found and fixed here; no remaining
  blockers on the final pass.
- B00 TIMING LAW: `actual_duration_s` 9.02s (≥8s requirement met, and the
  render itself is 9.033s after the trim fix); the "trust" → "check"
  correction is fully settled and legible by t≈8.7s, well before clip end.

Metadata file written: `financial-services--claude-liam-fsi-strip-profile.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`financial-services`) matches no
map prefix, so per the fallback rule the skill value `hai-simple` was
matched against the map instead, hitting the `"hai-simple"` key directly →
"Claude Basics". Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
