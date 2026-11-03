# BUILD-LOG — knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-meeting-sdk-app/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic
`build-zoom-meeting-sdk-app` Claude Skill, from the `knowledge-work-plugins`
book's Zoom partner-built plugin — already fully built, no SCRIPT.md;
source's own SKILL.md path (`/Users/bear/Documents/CoWork/bear-textbooks/...`)
not present on this machine, so source `beats[*].narration_text` served as
the locked script — same defect class as several `financial-services--*`
siblings). Built entirely fresh this invocation — only SUBJECT.json existed
on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, containing a RUNBOOK.md and a
SKILL.md plus one platform folder each for android/electron/ios/linux/
macos/react-native (8 files total per source B01); the instructions run as
steps, in order — read the file, execute each step, return the result —
linear, no branching unless a step says so; `build-zoom-meeting-sdk-app`'s
specific job is a reference for Zoom's Meeting SDK, used only after
routing to a meeting-embed workflow, for real meeting joins,
platform-specific SDK behavior, auth/join flows, waiting-room issues, or
meeting-bot patterns; it gets repeatable results right and bites on
anything outside the spec; same input produces the same output every run;
the skill only handles what its file specifies. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "design" → "follow steps for" — the newcomer's wrong guess
that Claude improvises the whole Zoom integration itself, corrected toward
the actual mechanism: it follows one file's steps for a build already
routed to it). Register re-registered Teardown → Plain: the source's B03
"gets it right: repeatable results / what it bites: anything outside the
spec" framing was restated in NB03 as a plain mechanism-and-boundary fact
(what the skill supplies — platform rules, once routed — and what it
declines to decide — the platform, or whether to embed at all), per the NO
JUDGMENT register check. BVDT's verdict facts (same input → same output
every run; limited to what the file specifies) were merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW. BHTF's prompt was adapted, not copied verbatim:
the source asked the viewer to "read the build-zoom-meeting-sdk-app
skill," which requires a plugin install a general viewer won't have, so
this redo substitutes an equivalent, actually paste-ready prompt
exercising the same decide-then-follow-the-rules habit without depending
on any specific Skill file. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02 kept as one beat each; B03's Teardown framing compressed
into NB03 (a plain mechanism-and-boundary fact); BVDT folded into BCRY;
BHTF kept (prompt adapted, see above); BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`financial-services--claude-liam-kyc-rules` sibling, adapted with
build-zoom-meeting-sdk-app-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate)
reused directly from the `financial-services--claude-liam-kyc-rules`
sibling's proven working configuration; the multi-word replacement
("design" → "follow steps for") followed the `financial-services--
claude-liam-macro-rates-monitor` sibling's precedent of putting the
trigger word alone on its own line so the longer replacement has room
(fontSize 64, matching that sibling). `actual_duration_s` (narration)
10.03s + `lead_silence_s` 1.0 gave the writer an 11.0s window; rendered
clip landed at 10.0s, comfortably clearing the ≥9s TIMING LAW floor.
Verified by frame pulls at t=2.0s ("design" doomed in terracotta,
mid-type), t=4.5s (mid-correction, "a whole Zoo[b]" typing toward "Zoom"),
and t=9.8s (full corrected question "Does Claude follow steps for a whole
Zoom meeting app?" settled and legible, holding to the end of the clip) —
correction lands and settles well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground, all 3 first pass). B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py`: the first invocation was wrapped in a manual `timeout
115` that killed B00's render mid-flight (SIGTERM, not a real renderer
failure — BCRY/BHTF/BOUT all completed clean in that same run); re-ran B00
alone (`--only B00 --force`) without an artificial wrapper timeout and it
completed clean on the retry.

**GATE T (type_check.py) first pass: FAIL, 1 defect (NB02, kerning §8.4),
root-caused via direct pixel inspection of the checker's own sample frame
rather than guessed at:** the checker flagged a 130px "inter-glyph gap" at
43.3× the expected advance. Direct frame pull at the checker's exact
sample point (t=6.46s, mid-clip) and a numpy re-run of its own row-ink/
run-detection pipeline localized the peak-ink row to y=512 — the chip-label
row itself, spanning all three chips ("read SKILL.md" / "run each step" /
"return result") plus the connecting arrows. Real letter-run gaps inside
the chip text measured 2–24px (normal); the 4 large gaps (100, 120, 119,
130px) landed exactly at the arrow-shaft positions between chips — the
same box-to-box arrow-shaft mechanism already documented in
`type_check.py`'s `KERNING_EXEMPT_PATTERNS` for `BGB02Scene`/`BNB02Scene`
(chip-row templates elsewhere in the toolkit). Direct visual read of the
frame confirms all three chip labels are correctly kerned and fully
legible — this is the same verified false-positive class, not a Pango
shaping bug. **Fixed by adding `BZNB02Scene` to `KERNING_EXEMPT_PATTERNS`**
in `runtime/scripts/type_check.py` (shared script — this is the
established, documented mechanism the toolkit already uses for this exact
defect class, not a loosened check: dozens of prior per-reel scene-name
entries already exist in that list for verified counter-space/arrow-gap
false positives).

Separately, a genuine Gate V legibility defect was caught by direct frame
inspection (not by GATE T, which doesn't check this): NB01's third chip
("6 platforms") rendered with the space between the digit and the word
visually collapsed to zero, reading as "6platforms." **Fixed at the
root** by spelling the numeral out ("six platforms", matching the spoken
narration "Six platforms, one shared reference") — re-rendered, and the
word-space, while still tighter than the other two-word chips, is clearly
legible as two words on re-inspection. NB01 re-rendered, master
recompiled, GATE T re-run clean.

`type_check.py` went FAIL→**PASS, 0 FAILs** on the full re-run (after both
fixes). Compiled via:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app.mp4`,
7/7 beats filled real (no slate), 101.0s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 100.98s;
  mp4 mtime (1788378948) newer than beat_sheet.json mtime (1788378838)
- Gate V (visual): pulled frames at t=5/15/25/35/45/55/65/75/85/95/98s
  across the full runtime plus the targeted B00 correction-timing checks
  above, and a re-check of the NB01 fix. B00 (writer, correction visible
  and settled, "@HumanitariansAI" overlay present per hai's channel-title
  law), NB01 (RUNBOOK.md / SKILL.md / six platforms chips all legible
  post-fix, arrows and caption clean), NB02/NB03 (chips legible, no
  overlap), BCRY (carry-out quote + sparkline "Supplies rules. Never
  decides." read clean), BHTF (correct topic "BUILD-ZOOM-MEETING-SDK-APP ·
  ZOOM MEETING SDK SKILL", correct title, @HumanitariansAI folder label,
  paste-ready prompt legible), BOUT (OutroSeries: "BUILD-ZOOM-MEETING-
  SDK-APP · @HumanitariansAI" eyebrow, correct title restate, crimson
  underline, no truncation). No remaining blockers.

Metadata file written:
`knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches that exact map key directly. Direct
code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to
`knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged
`DELIVERY/knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `eb078bb1`,
pushed clean (no rebase conflicts, branch up to date with origin/main).

**Status: DELIVERED.**
