# BUILD-LOG — healthcare--claude-liam-fraud-detection

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-fraud-detection/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `fraud-detection`
Claude Skill, from the `healthcare` book's plugin set — already fully
built, no SCRIPT.md; source `beats[*].narration_text` served as the locked
script, per its own REBUILD-LOG.md/AUDIT.md, which document the source's
own truncation-artifact repairs). Built entirely fresh this invocation —
only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, this one containing eight files
(ARCHITECTURE.html, claims-schema.sql, LOAD-CLAIMS.md, package.json,
PROPOSE-DETECTORS.md, README.md, REFERENCE-DATA.md, SKILL.md); the
skill's job is to screen a Medicare/Medicaid claims corpus for fraud,
waste, and abuse and produce ranked, fully-cited investigation referrals
for an SIU / program-integrity team; used when asked to run a fraud
sweep, screen claims for FWA, find billing anomalies, or generate
investigation referrals over a claims dataset; the pipeline relays one
output — a ranked list of referrals, each carrying the provider's NPI, the
suspected scheme, the dollar exposure, and a confidence score; same input
produces the same output every run; the skill only handles what its file
specifies, and it does not decide whether fraud occurred — that call
stays with the SIU / program-integrity team. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "convict" → "flag" — the newcomer's wrong guess that Claude
renders a legal-style fraud determination, corrected toward the actual
mechanism: the skill only flags and ranks candidate claims and hands the
investigation to a person). Register re-registered Teardown → Plain: the
source's B03 "gets it right: repeatable results / what it bites: anything
outside the spec" framing was restated in NB03 as a plain
mechanism-and-boundary fact (what the skill screens/ranks/cites, and what
it declines to decide), per the NO JUDGMENT register check. BVDT's verdict
facts (same input → same output every run; limited to what the file
specifies) were merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW. BHTF's
prompt was adapted, not copied verbatim: the source asked the viewer to
"read the fraud-detection skill," which requires a plugin install a
general viewer won't have, so this redo substitutes an equivalent,
actually paste-ready prompt exercising the same screen-then-hand-off habit
without depending on any specific Skill file. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02 kept as one beat each; B03's Teardown framing
compressed into NB03 (a plain mechanism-and-boundary fact); BVDT folded
into BCRY; BHTF kept (prompt adapted, see above); BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`financial-services--claude-liam-kyc-rules` sibling, adapted with
fraud-detection-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the
`financial-services--claude-liam-kyc-rules` sibling's proven working
configuration. `actual_duration_s` (narration) 10.65s + `lead_silence_s`
1.0 gave the writer an 11.65s window; rendered clip extended to 10.7s,
comfortably clearing the ≥8s TIMING LAW floor. Verified by frame pulls at
t=2.0s ("convict" doomed in terracotta, mid-type), t=4.5s (mid-correction,
"flag / fraudule[nt]" typing), and t=10.3s (full corrected question "Does
Claude flag fraudulent claims?" settled and legible, holding to the end of
the clip) — correction lands and settles well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground, exit 0, all 3 ok); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` — the invocation exceeded the tool's 120s timeout and
was moved to background by the harness automatically; blocked on it via
`TaskOutput` (block=true) before proceeding, per the COMPLETION LAW's
foreground-render rule, and confirmed exit code 0 with all four beats
reporting `ok` before moving on.

`type_check.py` (GATE T): **PASS, 0 FAILs on the first pass** — no fixes
needed. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `healthcare--claude-liam-fraud-detection.mp4`, 7/7 beats filled
real (no slate), 90.0s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 90.0s; mp4
  mtime (1788345772) newer than beat_sheet.json mtime (1788345652)
- Gate V (visual): pulled frames at t=5/15/25/30/42/55/65/78/88s across
  the full runtime, one per beat, plus the targeted B00 correction-timing
  checks above. B00 (writer, correction visible and settled, correct
  final question, "@HumanitariansAI" overlay present per hai's
  channel-title law), NB01/NB02/NB03 (all chips legible, arrows and
  captions clean, no overlap or truncation), BCRY (carry-out quote +
  sparkline "Ranks. Never convicts." read clean), BHTF (correct topic
  "FRAUD-DETECTION · MEDICARE/MEDICAID CLAIMS SCREENING SKILL", correct
  title "It Flags and Ranks. It Never Convicts.", @HumanitariansAI folder
  label, paste-ready prompt legible), BOUT (OutroSeries: "FRAUD-DETECTION
  · @HumanitariansAI" eyebrow, correct title restate, crimson underline,
  no truncation). No blockers.

Metadata file written: `healthcare--claude-liam-fraud-detection.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`healthcare`) matches no specific
vertical prefix in the map (no `healthcare-` entry exists), so resolution
falls through in map order to the `hai-simple` key itself (present in the
map precisely as this general fallback), which resolves to "Claude Basics"
— reached before `_default` ("Claude Across the Curriculum") is ever
considered, matching the disposition of every other `healthcare--*`
sibling already built in this loop. Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
