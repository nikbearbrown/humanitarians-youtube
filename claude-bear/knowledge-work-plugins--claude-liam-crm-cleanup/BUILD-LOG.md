# BUILD LOG — hai-simple/knowledge-work-plugins--claude-liam-crm-cleanup

Redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-crm-cleanup` (Teardown
register, 7-beat skill-teardown of an Anthropic skill named `crm-cleanup`) as `hai-simple`
(Plain register, Humanitarians AI skin). Source folder untouched.

## Source defect found on read

The source's narration truncates its own skill-description sentence mid-quote in three of
its seven beats. B00 carries the complete, untruncated version — "Scans HubSpot for stale
deals, duplicate contacts, and missing fields, then fixes what the owner approves. Accepts
optional scope argument for deals, contacts, or all." — but B03 cuts it to "...then fixes
what the owner app.", `BVDT` cuts it to "...then fixe.", and `BHTF` cuts it to "...missing
fields,." right before the clause finishes. This is the same batch template-truncation bug
already logged on this family's `call-prep` sibling. Nothing had to be invented; the
complete sentence was recovered directly from B00 and used wherever the truncated copies
appear. Full detail in `QUESTION.md`.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Source's B03 opened with "Here is the Teardown moment"
  and B03/BVDT carried "what it gets right / what it bites" and "Verdict" framing; this
  build's B03 states the same scope without ruling on the skill's design, and BCRY carries
  the fact as a plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "FIX" (implying Claude fixes the CRM on its own
  judgment), hesitates, corrects to "scan" → lands "Does Claude scan my CRM by itself?".
  The correction is picked up directly by B03's stated scope (Claude scans for exactly
  three named things and only fixes what the owner approves) and by BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  source's single `BOUT` (`ClaudeTitleOutro`) split into hai-simple's fixed two-part
  Humanitarians AI outro (`OutroSeries` + `OutroCTA`) — 7 → 8 beats total, same
  restructuring precedent as every other hai-simple redo in this family (e.g.
  `knowledge-work-plugins--claude-liam-call-prep`).
- **Facts/argument:** unchanged and generalized — the skill's anatomy (one SKILL.md file,
  no other items listed in the source), its pipeline (Steps section, linear execution),
  and its scope (scans HubSpot for three named things, fixes only what the owner approves,
  optional scope argument for deals/contacts/all) are reworded only for register. The
  source's truncated description is completed from its own B00, never guessed at.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is a new, complete first-person Claude prompt ("Read
  the crm-cleanup skill in this folder, tell me exactly which stale deals, duplicate
  contacts, and missing fields you'd flag in HubSpot, and wait for my approval on each
  one") — the source's own handoff was truncated mid-sentence around its own cut-off quote.

## Self-caught wording defect (fixed before delivery)

First draft of the carry-out line read "It scans for exactly what the file names, and
fixes only what you approve" — a genuine ambiguity ("names" read as a noun, not the
intended verb "specifies"), caught on Gate V frame review of the compiled BCRY beat.
Fixed in `beat_sheet.json` (BCRY `narration_text`, `quote`, `sparkLine`), `CARRY-OUT.md`,
`QUESTION.md`, and `SCRIPT.md` to "the file specifies" throughout; BCRY's audio (Kokoro,
`--only BCRY`) and Remotion render (`--only BCRY --force`) were regenerated and the master
recompiled (`--force`). Re-verified: frame pull at t=58s of the recompiled master reads
"It scans for exactly what the file specifies, and fixes only what you approve." cleanly.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components (substituting
`WantQuote` for the carry-out, per this family's precedent) rather than converting to
Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a human-drop slot.
`compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over the ~40% pantry cap)
is expected and accepted for the same reason every prior all-REMOTION sibling logged it:
this reel is a file/pipeline/scope explainer, not a worked-example narrative, and has no
illustrative-figure beats to draw as Manim.

## Gates

- **TYPECHECK / GATE T:** PASS, 0 FAILs, first pass (all 8 beats §8.10 SKIP — no
  truncation issues in this build's own strings).
- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **13.29s**, well clear of the ≥8s/≥9s-window floor. Frame pull at
  t=8s (of 13.29s) confirms the full corrected question "Does Claude scan my CRM by
  itself?" on screen with the correction already landed.
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB floor), max
  -2.9 dB. Verified independently via `ffprobe`/`ffmpeg volumedetect` on the compiled
  master both before and after the BCRY wording fix and recompile.
- **Gate V (frame QC):** sampled one frame per beat (B00 early + late, B01, B02, B03,
  BCRY, BHTF, BOUT, BCTA) at full 3840×2160 resolution and read each: all legible,
  correctly kerned, no text overlap, safe inset respected, `@HumanitariansAI` handle
  correct on the first beat only. Caught and fixed the BCRY wording defect above during
  this pass.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations), on both the initial compile and the post-fix recompile.

## Output

`knowledge-work-plugins--claude-liam-crm-cleanup.mp4` — 81.7s, 8/8 beats real (no
slates), native 3840×2160 (compile.py's 4K LAW forces this even without `--review`, since
all beats are Remotion rendered natively at 4K), audible narration throughout (mean_volume
-23.8 dB, independently verified). This is the review cut AND satisfies the 4K master
requirement in the same file (COMPLETION LAW satisfied: newer than `beat_sheet.json`,
audible audio verified via ffprobe independently of compile.py's own GATE AUDIO report).

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "knowledge-work-plugins"` matches the `knowledge-work-plugins` prefix in
`playlists.json`'s map directly (no fallback needed).

## Phase 4 (4K + delivery)

- **4K master:** the Phase-3 compile already wrote the master natively at 3840×2160 (see
  Output above). Copied it to
  `knowledge-work-plugins--claude-liam-crm-cleanup-4k.mp4` so `deliver.py`'s
  `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/knowledge-work-plugins--claude-liam-crm-cleanup/` (4K master + description,
  syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-crm-cleanup/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md +
  QUESTION.md — no media).

**Status: DELIVERED.**
