# BUILD-LOG — knowledge-work-plugins--claude-liam-draft-offer

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-draft-offer/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`draft-offer` Anthropic skill — an HR offer-letter generator). This
invocation started from a bare reel dir (only `SUBJECT.json` present) and
built end to end in one pass.

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source graded the skill via a "design tell" beat framed as
"the Teardown moment" ("what it gets right… what it bites") and closed with
a "Verdict" card; this redo states the three-part boundary as fact (no
grading language) and folds the verdict into a `WantQuote` carry-out beat.
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "letter" -> "package" — the newcomer
assumption that drafting an offer means just the congratulatory letter,
corrected to the full comp package). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. BHTF's prompt was rewritten clean —
the source's handoff string was truncated/garbled ("I want to draft an
offer letter with comp details and terms. use when a candidat.") and
referenced a skill file the general viewer won't have installed; this
version asks Claude directly to draft a comp package, letter, and
negotiation notes for a concrete hypothetical hire, no plugin dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot. The source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so no beat needed substitution beyond the WRITER LAW
and channel-skin row the skill already requires.

## Built end to end this invocation

1. Read the contract skills (`hai-simple/SKILL.md`, `simple/SKILL.md`), the
   source sheet + no local SKILL.md for `draft-offer` existed on this
   machine, so the source beat_sheet.json's narration served as the locked
   fact set (skill = folder with one SKILL.md; linear pipeline read ->
   execute -> return; exactly three things covered once a candidate is
   ready — comp package, letter text, negotiation guidance for the hiring
   manager; boundary = only what the file specifies). Also read the closest
   prior art directly: `knowledge-work-plugins--claude-liam-brief` (same
   source repo, same skill-teardown shape, already fully built and
   delivered) — used as the structural and stylistic template beat-for-beat
   in place of re-deriving conventions from the longer `claude-liam-simple-
   delve` six-move template, since the source's shape (anatomy -> pipeline
   -> constraint -> verdict, 7 beats) matches `brief`'s shape exactly.
2. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (7 beats:
   B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out,
   BHTF your turn, BOUT outro) and scenes.py/render_scenes.py for B01-B03.
3. Audio: `generate_audio_kokoro.py`, free, `am_onyx` — measured durations
   B00 11.2s, B01 15.06s, B02 9.34s, B03 16.98s, BCRY 10.94s, BHTF 17.45s,
   BOUT 3.93s. Updated scenes.py wait-times to match measured durations,
   then rendered B01-B03 via `render_scenes.py` (foreground) — 3/3 clean.
4. Rendered the 4 REMOTION beats via `remotion_scenes.py` in the
   foreground; the harness moved it to a tracked background task past its
   inline timeout, so per the COMPLETION LAW blocked on it directly via
   `TaskOutput(block=true)` until the completion notification confirmed
   exit code 0 — 4/4 rendered clean, B00 extended to 11.2s with the
   "letter" -> "package" correction landing well inside the >=8s TIMING LAW
   floor.
5. `compile.py` — first pass, 7/7 real (no slate), master
   `knowledge-work-plugins--claude-liam-draft-offer.mp4`, born natively at
   3840x2160 (4K LAW), 85.9s, mean_volume -24.1 dB. content-check,
   frame-check, and lane-check all PASS on the first pass.
6. GATE T (`type_check.py`): PASS, 0 FAILs, no fix iterations needed.
7. Gate V: pulled a frame from every beat and read it directly. B00's
   correction is legible at t=8s (final on-screen question: "Can Claude
   just write the offer package for a hire?"). B01-B03 anatomy/pipeline/
   constraint graphics are clean, correct contrast, no overlap. BCRY and
   BHTF cards are legible with correct @HumanitariansAI branding and the
   correct topic kicker ("DRAFT-OFFER · ANTHROPIC SKILL", single line, no
   wrap — checked directly against the `brief` sibling's logged BHTF
   kicker-wrap defect and confirmed this reel's shorter topic string does
   not reproduce it). Two pre-existing cosmetic quirks noted, not fixed,
   both already present unfixed on the shipped `brief` sibling with
   byte-for-byte identical code: (a) B03's Manim footer
   ("...same three parts back.") renders with the last word visually
   squeezed against "parts" — confirmed by direct frame comparison against
   `brief`'s shipped B03 ("...same three modes back." has the identical
   squeeze) — a Pango/Manim kerning artifact in that specific `Text(...)`
   call, not something this build introduced; (b) `OutroCTA` renders on
   flat white rather than the humanitarians cream ground, same
   shared-component note already logged unfixed across this factory.
8. Final master verified directly: 3840x2160, 85.92s, mean_volume -24.1 dB
   (max -2.8 dB), mtime newer than beat_sheet.json (18:49 vs 18:46) — the
   COMPLETION LAW conditions are all met.

## Gates

- **TIMING LAW (B00):** narration 31 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **11.2s**, clears the >=8s floor.
  Correction ("letter" -> "package") visible on-screen by t=8s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS, 0 FAILs, first run.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly. No new
  defects; two pre-existing shared-component cosmetic quirks noted (see
  above), consistent with the shipped `brief` sibling.
- **GATE AUDIO:** PASS, mean_volume **-24.1 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at 3840x2160
via `compile.py`'s 4K LAW, so no separate 4K re-render was needed — copied
directly to `knowledge-work-plugins--claude-liam-draft-offer-4k.mp4`.
