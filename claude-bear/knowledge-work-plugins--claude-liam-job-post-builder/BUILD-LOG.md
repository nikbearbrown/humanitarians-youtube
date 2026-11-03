# BUILD-LOG — knowledge-work-plugins--claude-liam-job-post-builder

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-job-post-builder/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`job-post-builder` Anthropic skill). This invocation started from a bare
reel dir (only `SUBJECT.json` present) and built end to end in one pass.

**Facts sourced from the real SKILL.md, not the source's placeholder
narration.** The source's own beats left their content as unfilled ">"
tokens (e.g. B03: "Claude's job: >. What it gets right... What it bites:
anything outside the spec.") — a batch-authoring defect, not filled-in
content to preserve. Located the actual skill at
`/Users/nik/Documents/Cowork/anthropics/knowledge-work-plugins/small-business/skills/job-post-builder/SKILL.md`
and read it completely: builds a hiring packet (job post, interview guide +
scoring rubric, offer letter) from a hiring brief via a 6-phase pipeline
(gather context → research comparable posts → write job post → draft
interview guide → assemble offer letter → optionally route to DocuSign via
Claude in Chrome), with three explicit hard approval gates — never send the
DocuSign envelope without review, never send the Gmail fallback without
approval, never publish the job post (produce the `.docx` only) — and an
explicit non-goal ("Does NOT screen or rank applicants"). These are the
facts kept unchanged; the redo's wrong-guess/carry-out axis (does it also
hit send once it's driving the browser?) is built from the skill's own
approval-gate section, the single richest and most surprising real fact
available, in place of re-deriving generic "skill = folder" filler.

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source graded the skill via a "design tell" beat framed as
"the Teardown moment" and closed with a "Verdict" card; this redo states the
three-stop boundary as fact (no grading language) and folds the verdict into
a `WantQuote` carry-out beat. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "sends" -> "drafts" —
the newcomer assumption that once Claude is far enough in to be driving
DocuSign, it will finish the job and send the offer itself, corrected to it
stopping at a draft). Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot. The source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`),
so no beat needed substitution beyond the WRITER LAW and channel-skin row the
skill already requires. `SkillTeardownAnatomy`/`Pipeline`/`Mechanism` hardcode
Claude-palette tokens with no humanitarians override props, so B01-B03 were
rebuilt as GRAPHIC (Manim) scenes carrying the same teaching content in the
humanitarians palette — following the exact precedent set by the
`knowledge-work-plugins--claude-liam-draft-offer` sibling (same source shape,
built the day before this invocation), used directly as the structural and
Manim-code template rather than re-deriving conventions from scratch.

## Built end to end this invocation

1. Read the contract skills (`hai-simple/SKILL.md`, `simple/SKILL.md`), the
   source sheet, and the real `job-post-builder` SKILL.md (found under
   `~/Documents/Cowork/anthropics/knowledge-work-plugins/...` — the source
   reel dir only had the rendered `beat_sheet.json` and a stub
   `PEDAGOGY.md`). Also read the closest prior art directly:
   `knowledge-work-plugins--claude-liam-draft-offer` (same source repo, same
   skill-teardown shape, already fully built and delivered) — used as the
   structural and Manim-code template beat-for-beat.
2. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (7 beats: B00
   writer, B01 anatomy, B02 mechanism [6-step pipeline], B03 constraint
   [three hard stops], BCRY carry-out, BHTF your turn, BOUT outro) and
   scenes.py/render_scenes.py for B01-B03 (B02 expanded to a two-row,
   six-card layout to carry the skill's actual 6-phase pipeline, versus the
   sibling's 3-card version).
3. Audio: `generate_audio_kokoro.py`, free, `am_onyx` — measured durations
   B00 10.41s, B01 15.27s, B02 15.98s, B03 15.02s, BCRY 9.79s, BHTF 15.38s,
   BOUT 4.10s. Updated scenes.py wait-times to match measured durations, then
   rendered B01-B03 via `render_scenes.py` (foreground) — 3/3 clean.
4. Rendered the 4 REMOTION beats via `remotion_scenes.py`; the harness moved
   it to a tracked background task past its inline timeout, so per the
   COMPLETION LAW blocked on it directly via `TaskOutput(block=true)` until
   the completion notification confirmed exit code 0 — 4/4 rendered clean,
   B00 extended to 10.4s with the "sends" -> "drafts" correction landing well
   inside the >=9s TIMING LAW floor.
5. `compile.py` — first pass, 7/7 real (no slate), master
   `knowledge-work-plugins--claude-liam-job-post-builder.mp4`, born natively
   at 3840x2160 (4K LAW), 87.0s, mean_volume -24.0 dB. content-check,
   frame-check, and lane-check all PASS on the first pass.
6. GATE T (`type_check.py`): PASS, 0 FAILs, no fix iterations needed (7 beats
   checked across min-size, overflow, contrast, contrast-local, bbox-overlap,
   card-clip, kerning — all 0 FAILs).
7. Gate V: pulled frames at 19 timestamps spanning every beat, read each
   directly. B00's correction is legible by t=6s ("drafts" already typed) and
   the full corrected question ("Claude builds the hiring packet, then
   drafts the offer once it's ready?") is complete and legible by t=9.5s of
   the 10.4s beat. B01's folder/SKILL.md/references layout is clean and
   correct (the folder-outline/SKILL.md-box visual crossing is the same
   established look as the shipped `draft-offer` sibling's B01, and
   bbox-overlap §8.6b passed programmatically on all 7 beats). B02's six-card
   two-row pipeline reads correctly with the wrap arrow (row 1 → row 2) clear.
   B03's three-stop list and boundary caption are legible with correct
   contrast. BCRY and BHTF are centered/legible with correct
   `@HumanitariansAI` branding (folderLabel override confirmed working — not
   the `ClaudeComposerAsk` Root.tsx default `@NikBearBrown`) and BHTF's
   single-line topic kicker does not wrap. One pre-existing cosmetic quirk
   noted, not fixed: `OutroCTA` renders on flat white rather than the
   humanitarians cream ground — same shared-component note already logged
   unfixed on the `draft-offer` sibling with byte-for-byte identical code.
8. Final master verified directly: 3840x2160, h264/aac streams present,
   mean_volume **-24.0 dB** (max -3.0 dB, ffmpeg `volumedetect`), mtime
   (01:30:17) newer than beat_sheet.json (01:29:00) — the COMPLETION LAW
   conditions are all met.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.41s**, clears the >=9s floor. Correction
  ("sends" -> "drafts") visible on-screen by t=6s, full question complete by
  t=9.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS, 0 FAILs, first run.
- **Gate V (frame QC):** full beat sweep across 19 frames, all 7 beats read
  directly. No new defects; one pre-existing shared-component cosmetic quirk
  noted (OutroCTA background), consistent with the shipped `draft-offer`
  sibling.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at 3840x2160
via `compile.py`'s 4K LAW, so no separate 4K re-render was needed — copied
directly to `knowledge-work-plugins--claude-liam-job-post-builder-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-job-post-builder/` (4K master +
description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-job-post-builder/` (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md,
QUESTION.md — no media) to `humanitarians-youtube`. `HAILOOP-LOG.md` updated
with the matching entry.

**Status: DELIVERED.**
