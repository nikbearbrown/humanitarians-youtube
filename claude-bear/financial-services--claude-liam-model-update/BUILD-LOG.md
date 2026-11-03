# BUILD-LOG — financial-services--claude-liam-model-update

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-model-update/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `model-update`
Claude Skill, from the `financial-services` book's `earnings-reviewer`
plugin — already fully built, no SCRIPT.md; source `beats[*].narration_text`
served as the locked script — same defect class as the
`financial-services--claude-liam-kyc-rules` sibling: source's own SKILL.md
not present on this machine). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so;
`model-update`'s specific job is to update financial models with new
data — quarterly earnings, management guidance, macro changes, or revised
assumptions — adjusting estimates, recalculating valuation, and flagging
material changes; same input produces the same output every run; the
skill only handles what its file specifies. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "smarter" -> "new numbers" — the newcomer's wrong guess that
a Claude reel titled "model update" means Anthropic shipped a new Claude,
corrected toward the actual mechanism: the skill refreshes a financial
model with new data, it does not change Claude). Register re-registered
Teardown -> Plain: the source's B03 "gets it right: repeatable results /
what it bites: anything outside the spec" framing and BVDT's verdict facts
("same input, same output, every run"; "know the limit: only what the file
says") were merged into a single NB03 mechanism-and-boundary beat, per the
NO JUDGMENT register check and CARRY-OUT LAW. BHTF's prompt was adapted,
not copied verbatim: the source asked the viewer to "read the model-update
skill," which requires a plugin install a general viewer won't have, so
this redo substitutes an equivalent, actually paste-ready prompt exercising
the same work-out-then-flag-then-wait habit without depending on any
specific Skill file. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01->NB01, B02->NB02 kept as one beat each; B03's Teardown framing and
BVDT's verdict facts compressed into the single NB03 (mechanism-and-
boundary fact, no separate verdict artifact); BHTF kept (prompt adapted,
see above); BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01-NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`financial-services--claude-liam-kyc-rules` sibling, adapted with
model-update-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the
`financial-services--claude-liam-kyc-rules` sibling's proven working
configuration. `actual_duration_s` (narration) 11.41s + `lead_silence_s`
1.0 gave the writer a 12.41s window; rendered clip extended to 11.4s,
comfortably clearing the >=8s TIMING LAW floor. Verified by frame pulls at
t=2.0s ("Does a model" mid-type), t=4.5s ("...Claude just got" mid-type),
t=5.5s-6.0s ("smarter" fully typed and doomed in terracotta), t=7.0s
(mid-correction, "new" retyping underway), t=8.0s and t=11.0s (full
corrected question "Does a model update mean Claude just got new numbers?"
settled and legible, holding to the end of the clip) — correction lands
and settles well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01-NB03 rendered via `render_scenes.py`
(foreground); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` — the
invocation exceeded the tool's 120s foreground timeout and was
auto-backgrounded by the harness; blocked on it via `TaskOutput`
(block=true) before proceeding, per the COMPLETION LAW's foreground-render
rule, and confirmed exit code 0 with all four beats reporting `ok` before
moving on.

**GATE T (type_check.py) first pass: FAIL, 2 defects (NB02 + NB03,
min-size §8.1), root-caused by direct pixel inspection rather than
guessed at:** extracted the checker's own mid-clip sample frames (t=dur*0.5
of each raw manim/NBxx.mp4) and ran its exact
`visible_text_mask`/`labeled_blobs`/`blob_bboxes`/`text_run_bboxes`
pipeline directly (numpy) to rank every detected text-run bbox by height.
In both beats the smallest run (19px < floor 20px) localized to the same
substring: the word "new" in the first chip ("new data in" / "new data")
was segmented by the connected-component labeler into "n" + "ew", and the
isolated "ew" run — lowercase, x-height-only, no ascender/descender — read
at 19px even though the full word "new" is legible at normal size. Same
defect class as the `kyc-rules` sibling's "reviewed by staff" dotted-i
failure: a connected-component segmentation artifact, not an actual
legibility defect. **Fixed at the root:** renamed both chips from
"new data in"/"new data" to "data arrives" — same meaning, no isolated
x-height-only run. Re-verified directly against the checker's pipeline
before re-running the full checker: both beats' smallest run rose clear of
the floor. `type_check.py` went FAIL->**PASS, 0 FAILs** on the full re-run
(re-rendered NB02/NB03 via `render_scenes.py`, recompiled with `--force`).

Result: `financial-services--claude-liam-model-update.mp4`, 7/7 beats
filled real (no slate), 99.1s, 3840x2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect,
  independently re-verified), max -2.9 dB
- ffprobe: video 3840x2160 h264, audio (aac) present, duration 99.08s; mp4
  mtime (1788330636) newer than beat_sheet.json mtime (1788330494)
- Gate V (visual): pulled frames at t=3/8/15/25/35/45/55/65/69/75/85/92/97s
  across the full runtime plus the targeted B00 correction-timing checks
  above. B00 (writer, correction visible and settled, "@HumanitariansAI"
  overlay present per hai's channel-title law), NB01/NB02/NB03 (all chips
  legible post-fix, arrows and captions clean, no overlap), BCRY (carry-out
  quote + sparkline "Current. Never decided." read clean), BHTF (correct
  topic "MODEL-UPDATE · FINANCIAL MODEL REFRESH SKILL", correct title "It
  Updates the Model. Not Itself.", @HumanitariansAI folder label,
  paste-ready prompt legible), BOUT (OutroSeries: "MODEL-UPDATE ·
  @HumanitariansAI" eyebrow, correct title restate, crimson underline, no
  truncation). No blockers.

Metadata file written: `financial-services--claude-liam-model-update.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`financial-services`) matches no
specific vertical prefix in the map (no `finance-`/`financial-` entry
exists), so resolution falls through in map order to the `hai-simple` key
itself (present in the map precisely as this general fallback), which
resolves to "Claude Basics" — reached before `_default` ("Claude Across
the Curriculum") is ever considered, matching the disposition of the
`financial-services--claude-liam-kyc-rules` sibling exactly. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
