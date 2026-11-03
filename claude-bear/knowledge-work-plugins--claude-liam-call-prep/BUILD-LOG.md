# BUILD LOG — hai-simple/knowledge-work-plugins--claude-liam-call-prep

Redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-call-prep` (Teardown
register, 7-beat skill-teardown of an Anthropic skill named `call-prep`) as `hai-simple`
(Plain register, Humanitarians AI skin). Source folder untouched.

## Source defect found on read

The source's narration truncates its own quoted trigger-phrase list mid-sentence in
three of its seven beats — B03, BVDT, and BHTF all cut off right after "Triggers on
'prep me for my call ." instead of finishing the phrase. This is the same batch
template-truncation bug already logged on this family's `customize` sibling in
`claude-for-legal`, but milder here: the source's own B00 carries the complete,
untruncated sentence — "Triggers on 'prep me for my call with [company]', 'prepare for
a meeting with [company]', 'what should I know before talking to [company]', or any
call preparation request." Nothing had to be invented; the complete phrase list was
recovered from B00 and used wherever the truncated copies appear. Full detail in
`QUESTION.md`.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Source's B03 opened with "Here is the Teardown
  moment" and B03/BVDT carried "what it gets right / what it bites" and "Verdict"
  framing; this build's B03 states the same scope without ruling on the skill's
  design, and BCRY carries the fact as a plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer
  types the newcomer's wrong-guess word "JOIN" (implying Claude sits in on or makes
  the call), hesitates, corrects to "prep" → lands "Does Claude prep me before the
  call?". The correction is picked up directly by B03's stated scope (Claude prepares
  the brief, never participates in the call) and by BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  source's single `BOUT` (`ClaudeTitleOutro`) split into hai-simple's fixed two-part
  Humanitarians AI outro (`OutroSeries` + `OutroCTA`) — 7 → 8 beats total, same
  restructuring precedent as every other hai-simple redo in this family (e.g.
  `claude-for-legal--claude-liam-customize`).
- **Facts/argument:** unchanged and generalized — the skill's anatomy (SKILL.md +
  references folder), its pipeline (Steps section, linear execution), and its scope
  (prepares one call from Common Room signals, triggered on specific phrases, nothing
  outside that) are reworded only for register. The source's truncated trigger-phrase
  quote is completed from its own B00, never guessed at.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is a new, complete first-person Claude prompt
  ("Read the call-prep skill in this folder, tell me exactly which signals it will pull
  and from where, then prep me for a call with a company I name") — the source's own
  handoff was truncated mid-sentence around its own cut-off quote.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over
the ~40% pantry cap) is expected and accepted for the same reason every prior
all-REMOTION sibling logged it: this reel is a file/pipeline/scope explainer, not a
worked-example narrative, and has no illustrative-figure beats to draw as Manim.

## Gates

- **TYPECHECK / GATE T:** PASS, 0 FAILs, first pass (all 8 beats §8.10 SKIP — no
  truncation issues in this build's own strings).
- **TIMING LAW (B00):** narration 33 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.2s**, clears the ≥8s/≥9s-window floor. Frame pull at t≈8s
  (of 10.2s) confirms the full corrected question "Does Claude prep me before the
  call?" on screen with the correction already landed and the cursor still blinking.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB floor), max
  -2.9 dB. Verified independently via `ffprobe`/`ffmpeg volumedetect` on the compiled
  master, not just the compile-step log.
- **Gate V (frame QC):** sampled one frame per beat (B00 late, B01, B02, B03, BCRY,
  BHTF, BOUT, BCTA) at full 3840×2160 resolution and read each: all legible, correctly
  kerned, no text overlap, safe inset respected, `@HumanitariansAI` handle correct
  throughout.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations).

## Output

`knowledge-work-plugins--claude-liam-call-prep.mp4` — 73.7s, 8/8 beats real (no
slates), native 3840×2160 (compile.py's 4K LAW forces this even without `--review`,
since all beats are Remotion rendered natively at 4K), audible narration throughout
(mean_volume -23.9 dB, independently verified). This is the review cut AND satisfies
the 4K master requirement in the same file (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, audible audio verified via ffprobe independently of compile.py's own
GATE AUDIO report).

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "knowledge-work-plugins"` matches the `knowledge-work-plugins` prefix in
`playlists.json`'s map directly (no fallback needed).

## Phase 4 (4K + delivery)

- **4K master:** the Phase-3 compile already wrote the master natively at 3840×2160
  (see Output above). Copied it to
  `knowledge-work-plugins--claude-liam-call-prep-4k.mp4` so `deliver.py`'s
  `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/knowledge-work-plugins--claude-liam-call-prep/` (4K master + description,
  syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-call-prep/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md
  + QUESTION.md — no media).

**Status: DELIVERED.**
