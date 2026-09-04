# BUILD-LOG — cwc-workshops--claude-liam-forecasting

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-forecasting/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `forecasting`
cwc-workshops Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script, cross-checked
against the skill's own SKILL.md, present unchanged at
`/Users/nik/Documents/Cowork/anthropics/cwc-workshops/agent-decomposition/.claude/skills/forecasting/SKILL.md`
even though the source reel's own `source_skill` metadata field points at
a Bear-machine path that does not exist here — same defect class as other
`cwc-workshops--*` siblings, resolved the identical way: the skill content
itself is present, unchanged, at the Cowork-mirrored path). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it acts, containing two scripts
(`rolling_mean.py` for a single SKU, `batch_days_of_cover.py` for ranking
many at once) plus SKILL.md; forecasting has two paths gated by four flags
(horizon, `is_seasonal`, `promo_next_month`, a mentioned trend break) —
clear of all four routes to Path A (compute it yourself, a rolling mean,
one script call), any one flipped routes to Path B (delegate to a
forecaster subagent, because it needs the full 90-day sales history in its
own context window rather than crowding out the main conversation); and
the confidence threshold downstream — below 0.6, escalate rather than
auto-order — plus the fact that `forecast_qty` is a computed output of the
rolling mean or the subagent's model, not a predicted fact about next
month. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open
with `BrutalistHesitantWriter` (WRITER LAW: "always" → "sometimes" — the
newcomer's wrong guess that Claude always delegates forecasting to a
subagent, corrected toward the actual mechanism: delegation is
flag-gated, not automatic). Register re-registered Teardown → Plain: the
source's B03 design-tell text (which had been corrupted by truncation in
the source per its own AUDIT.md — "compute it y", card body cut at
"promos,") and BVDT's verdict were merged into a single NB03, keeping the
two facts a general audience needs and can act on (the confidence
threshold; what the returned number actually is) and dropping the
Claude-harness-internals aside about `callable_agents` being a
research-preview feature with an inline fallback, which assumes a
technical audience this series doesn't target — not a verdict on the
skill's quality. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B03+BVDT compressed into NB03 (the two
facts a general viewer needs and can act on); BHTF kept as the your-turn
handoff, rewritten as a fully self-contained prompt — the source's version
named "the forecasting skill" by file, which only works if the viewer has
that exact SKILL.md installed; this redo's prompt instead states the
scenario directly (a promo next month, a 30-day horizon) so it is runnable
in any Claude conversation today, no skill install required, while still
testing the same reasoning (horizon + promo routes to delegation; promo
uplift uncertainty routes to a low confidence score and an escalate, not
auto-order); BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with forecasting-specific labels.

**B00 TIMING LAW:** narration 24 words + `lead_silence_s` 0.9, audio
measured 9.24s (clears the ≥9s TIMING LAW floor; media/B00.mp4 rendered to
9.27s, well past the ≥8s media-file floor). Frame-verified: "always" sits
doomed in terracotta at t≈3s, corrects to "sometimes" by t≈5s, and the
full corrected question — "Does Claude sometimes spawn a subagent to
forecast?" — is settled and legible for the remainder of the 9.27s clip.

**Foreground-render discipline (COMPLETION LAW):** the first
`remotion_scenes.py` invocation exceeded the tool's 120s foreground
timeout and was killed mid-run by the harness before completing — it had
partially rendered B00 and BCRY to `media/` with stale/corrupt extended
durations (a leftover `_ext_BCRY.mp4` temp file from the aborted ffmpeg
step caused a `FileNotFoundError` on the next invocation). Rather than
treat either partial file as "handled," both `media/B00.mp4` and
`media/BCRY.mp4` were deleted and `remotion_scenes.py` was re-run to
completion in the foreground with an explicit 590s tool timeout, producing
clean B00 (9.27s), BCRY (10.83s), and BOUT (3.4s) renders; BHTF had
completed correctly during the first attempt and was left in place
(verified by ffprobe before reuse, per the reuse-and-continue rule for
prior-attempt artifacts).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); NB01–NB03 rendered via `render_scenes.py` (foreground, Manim);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground). First
`type_check.py` pass was **FAIL, 2 defects**, fixed at the root:

- **min-size §8.1, NB01** — smallest text run 17px, under the 20px floor.
  The chip label `"batch_days_of_cover.py"` (22 chars) forced the
  width-based scale-to-fit path to shrink further than its nominal
  font-size tier; `"rolling_mean.py"` (15 chars) was the second offender
  once the first was fixed. Both real filenames were replaced with
  parallel generic labels — `"single script"` / `"batch script"` — short
  enough to stay in the top font-size tier without any width-forced
  scale-down; the exact filenames remain in the spoken narration
  unchanged, so no fact was lost, only the on-screen chip text was
  shortened.
- **min-size §8.1, NB02** — smallest text run 18px, under the 20px floor.
  The accented (bold) chip `"Path B: subagent"` (16 chars) hit the same
  bold+borderline-length interaction documented in the
  `claude-plugins-official--claude-liam-access` / `-agent-development`
  siblings' own NB0x fixes. Shortened chips to `"Path A"` / `"Path B"`
  (each ≤ 7 chars) and moved the subagent/context-window detail into the
  caption (`"Path B gets its own context window"`), which is plain (not
  bold) weight and unaffected by the same failure mode.

Both fixes re-rendered only the affected beat (`NB01`/`NB02` individually,
via `render_scenes.py`'s skip-if-exists behavior after deleting just the
stale file), and `beat_sheet.json`'s `graphic.production_viz` fields were
synced to the fixed chip/caption text directly (not via a full sheet
regeneration, which would have discarded the already-measured audio
durations and B00/BCRY/BHTF/BOUT render stamps), per COMPLETION LAW.
`type_check.py` went 2→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `cwc-workshops--claude-liam-forecasting.mp4`, 7/7 beats filled real
(no slate), 123.9s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 123.9s; mp4
  mtime (1788237258) newer than beat_sheet.json mtime (1788237103)
- Gate V (visual): pulled frames every ~8s across the full runtime plus a
  targeted late-clip pull for B00 (correction legible, holds to end of
  9.27s clip) and BOUT (t≈121s, past the last 8s-grid sample) — all 7
  beats legible, correctly inset, no text overlap. NB01/NB02 re-checked
  post-fix: "single script" / "batch script" / "SKILL.md" and "4 flags" /
  "Path A" / "Path B" all read clean and parallel-sized. BHTF: correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible.
  BOUT (OutroSeries): correct eyebrow "FORECASTING · @HumanitariansAI",
  correct title restate "Flags Decide The Path.", crimson underline, no
  truncation. No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.24s / rendered clip 9.27s (both
  ≥ the ≥9s/≥8s floors); the "always" → "sometimes" correction lands on
  screen by t≈5s and the full corrected question stays legible for the
  remainder of the clip.

Metadata file written: `cwc-workshops--claude-liam-forecasting.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`cwc-workshops`) matches no
prefix in the map's family column; per the redo instruction to also check
the `hai-simple` skill-key prefix, `"hai-simple"` is itself a map key
resolving to `"Claude Basics"` — the same fallback documented in the
`cwc-workshops--claude-liam-eval-audit-and-sweep` sibling built earlier
today, so this is a real, more-specific-than-`_default` match, not the
last-resort default. Direct code link per DELIVERY CONTRACT format
included. Chapters computed from `actual_duration_s` cumulative offsets
(B00 0:00, NB01 0:09, NB02 0:28, NB03 1:02, BCRY 1:29, BHTF 1:40, BOUT
1:59).

**Status: review cut DONE.** Passed every Phase-3 gate.
