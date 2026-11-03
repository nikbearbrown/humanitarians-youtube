# BUILD LOG — hai-simple/knowledge-work-plugins--claude-liam-enrich-lead

Redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-enrich-lead` (Teardown
register, 7-beat skill-teardown of an Anthropic skill named `enrich-lead`) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched.

## Source is intact

Unlike this batch's `crm-maintenance`/`crm-cleanup` siblings (whose `>`-prefixed
skill-description placeholder was truncated or empty), this source carries the full
sentence in every beat: "Instant lead enrichment. Drop a name, company, LinkedIn URL, or
email and get the full contact card with email, phone, title, company intel, and next
actions." Nothing to recover; full detail in `QUESTION.md`.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Source's "Teardown moment," "what it gets right / what
  it bites," and verdict framing dropped; B03 states the mechanism and scope and stops.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer
  types the newcomer's wrong-guess word "PROFILE" (implying enrich-lead needs a
  near-complete profile in hand already), hesitates, corrects to "name" → lands "Enrich-lead
  needs a full name to start. Right?". The wrong guess is the inverse of the source's own
  spec line ("name, company, LinkedIn URL, **or** email" — any one suffices).
- **Beat count:** kept the source's shape in substance (B00 → B01 anatomy → B02 pipeline →
  B03 mechanism → BCRY carry-out → BHTF handoff → BOUT outro), source's single outro split
  into hai-simple's fixed two-part Humanitarians AI outro (`OutroSeries` + `OutroCTA`) — 8
  beats total, same precedent as this family's other redos (`crm-maintenance`,
  `redshift-api`).
- **Facts/argument:** unchanged — anatomy (one file, `SKILL.md`), pipeline (Steps section,
  linear execution), the job (name/company/LinkedIn URL/email → contact card with email,
  phone, title, company intel, next actions), and the scope guarantee (same input, same
  output; silent outside the file) all carried over from the source's own intact text.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new and complete (the source's own handoff was
  visibly truncated: "drop a name, company, linkedin url, or email and get th."). Rewritten
  as "I have a lead — just a first name, nothing else. Read the enrich-lead skill in this
  folder and walk me through exactly which steps you'll run, in order, before you actually
  run them."

## NO-GENAI / NO-PANTRY LAW

Every beat is REMOTION (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `WantQuote`, `ClaudeComposerAsk`,
`OutroSeries`, `OutroCTA`) — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over the
~40% pantry cap) is expected and accepted for the same reason every prior all-REMOTION
sibling in this family logged it: this reel is a file/pipeline/scope explainer, not a
worked-example narrative, and has no illustrative-figure beats to draw as Manim/GRAPHIC.

## Defect found and fixed before compile

First-pass B00 used `triggerWords: "LINKEDIN"` against typed text "a LINKEDIN profile to
start" — the component matches and swaps exactly one token, so the corrected sentence read
"a name profile to start," which is not standard English and did not match the planned
narration ("Enrich-lead needs a name to start"). Caught on frame inspection at t=8.5s of
the first B00 render. Fixed by rewriting the typed text to "a full PROFILE" with
`triggerWords: "PROFILE" -> "name"`, so the single-token swap produces a clean, correct
sentence: "Enrich-lead needs a full name to start. Right?" Regenerated B00's audio (10.18s,
narration text updated to match), re-rendered B00 with `--force`, recompiled. Frame-checked
again at t=9.0s of the fixed render: the correction is fully landed, cursor resting after
"R" of "Right?", no leftover fragment from the naive framing.

**Harness note:** `remotion_scenes.py` on this reel (8 beats, one of them the
heavier-weight `ClaudeComposerAsk` composition) consistently exceeded the tool's 120s
foreground window. Per the one-shot COMPLETION LAW's foreground-render rule, backgrounded
renders were never treated as done on backgrounding — blocked synchronously on the task
(`TaskOutput`, `block=true`) until each exited, and separately re-ran the failed BHTF beat
directly via `npx remotion render` with a longer foreground budget after confirming the
first "FAIL" was a mid-render kill (truncated stderr showing only the harmless Remotion
package-version-mismatch banner, no real error) rather than a genuine renderer defect.

## Gates

- **GATE T:** PASS, 0 FAILs, all 8 beats (first pass).
- **TIMING LAW (B00):** narration 33 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.18s**, clear of the ≥8s/≥9s-window floor. Frame pull at t=9.0s
  (of 10.18s) confirms the corrected question "Enrich-lead needs a full name to start.
  Right?" fully on screen, correction already landed, cursor at the end.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB floor), max
  -2.9 dB — verified independently via `ffmpeg volumedetect` on the compiled master.
- **Gate V (frame QC):** sampled frames across B00 (early + late, both the defective and
  fixed renders), B01, B02, B03, BCRY, BHTF, BOUT, BCTA at full 3840×2160: all legible,
  correctly kerned, no text overlap, safe inset respected, `@HumanitariansAI` handle
  correct throughout, HAI outro skin correct (`OutroSeries` title restate + `OutroCTA`
  subscribe/handle). **Noted, not a defect introduced here:** `OutroCTA`/`OutroSeries`
  render on a flat-white ground rather than the humanitarians cream (`#F3EBDD`) — same
  shared-component behavior already logged unremarked in sibling hai-simple reels
  (`crm-maintenance`, `redshift-api`); out of this reel's scope to fix.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` (8/8 beats, no
  violations).
- **ffprobe:** video 3840×2160 h264, audio aac present; duration 83.0s; mp4 mtime newer
  than beat_sheet.json mtime.

## Output

`knowledge-work-plugins--claude-liam-enrich-lead.mp4` — 83.0s, 8/8 beats real (no slates),
native 3840×2160 (compile.py's 4K LAW forces this even without `--review`, since all beats
are Remotion-rendered natively at 4K), audible narration throughout (mean_volume -23.9 dB,
independently verified, mp4 newer than beat_sheet.json). COMPLETION LAW satisfied.

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "knowledge-work-plugins"` matches the `knowledge-work-plugins` prefix in
`playlists.json`'s map directly (no fallback needed).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K render +
deliver.py) in this same invocation.

## Phase 4 (4K + delivery)

- **4K master:** the Phase-3 compile already wrote the master natively at 3840×2160
  (all-Remotion reel). Copied it to
  `knowledge-work-plugins--claude-liam-enrich-lead-4k.mp4` so `deliver.py`'s
  `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/knowledge-work-plugins--claude-liam-enrich-lead/` (4K master + description,
  syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-enrich-lead/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md +
  QUESTION.md — no media): commit `18b26228`, pushed clean (`git status --short` empty
  after).

**Status: DELIVERED.**
