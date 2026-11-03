# BUILD-LOG — financial-services--claude-liam-ib-check-deck

## 2026-09-01 — review cut, DONE

Picked up an in-progress redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-ib-check-deck/beat_sheet.json`
(Teardown register). On arrival, Phases 0–2 were already complete: QUESTION.md,
CARRY-OUT.md, SCRIPT.md, and a fully-authored `beat_sheet.json` (7 beats) all
existed, along with generated audio (`mp3/*.mp3` + `mp3/timings.json`), the
B00 Remotion cold open (`media/B00.mp4`), and three rendered Manim body beats
(`manim/B01.mp4`, `B02.mp4`, `B03.mp4`). This invocation verified that prior
state, then completed the remaining build.

**Locked facts carried over from the source (QUESTION.md):** a "skill" is a
folder Claude reads before acting; execution is linear (read the file, work
each step in order, return the result); the check itself covers exactly four
things — number consistency across slides, data-narrative alignment, language
polish against IB standards, and visual/formatting QC; only what the
instruction file specifies gets checked.

**Carry-out (CARRY-OUT.md):** "A skill like this doesn't proofread a deck — it
reconciles it: the same four checks, every slide, every run, and nothing
outside that checklist gets caught." Defeats the wrong guess that "checking" a
deck means a spellcheck/read-through for typos.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (`BrutalistHesitantWriter` B00, `WantQuote` BCRY,
`ClaudeComposerAsk` BHTF, `OutroCTA` BOUT) or GRAPHIC/Manim (B01 anatomy, B02
pipeline, B03 four-checks constraint). No beat was ever AI-VIDEO, pantry, or a
human-drop slot.

## What this invocation did

1. **Rendered the remaining Remotion beats.** `remotion_scenes.py` was run
   against the reel; it exceeded the tool's 120s foreground timeout and was
   auto-backgrounded by the harness. Per the ONE-SHOT/COMPLETION LAW, blocked
   on the actual process exit (polled for the pid to clear, read the task
   output) rather than ending the turn assuming it would finish unsupervised.
   Completed clean, exit 0: `BCRY.mp4` and `BHTF.mp4` filled (`B00`/`BOUT`
   were already filled from a prior pass).
2. **Compiled the first cut.** `compile.py` (no `--review`, so the 4K LAW
   forced the master to 3840×2160 directly): 7/7 beats filled, no slates,
   `GATE AUDIO: PASS` at mean_volume −24.0 dB.
3. **Gate V (frame QC).** Pulled frames every 4s across the 81.5s runtime and
   read all of them: legible, on-palette (humanitarians cream/ink/terracotta),
   no text overlap, safe inset respected. Confirmed B00's WRITER LAW
   correction ("spellcheck" → "check") is already resolved on screen well
   before the beat ends (10.43s beat, correction visible by t=4s).
4. **GATE T (`type_check.py`) — caught 2 real defects, both fixed:**
   - B01 and B03 failed §8.4 kerning (max inter-glyph gap 34–38px vs. a
     20–22px threshold) because `scenes.py`'s Manim `Text()` calls used
     `font='Montserrat'`/`'Menlo'` with no EB Garamond anywhere in the file —
     the checker's own suggested fix. Switched all `Text()` calls in
     `B01Scene` and `B03Scene` to `font='EB Garamond'` (left `B02Scene`, which
     was already passing, untouched) and re-rendered both beats.
   - That font swap **introduced a new, genuinely visible defect**: B03's
     title rendered as "EXACTLYFOUR CHECKS." — the space between "EXACTLY"
     and "FOUR" collapsed to zero width in bold EB Garamond at this size (a
     Pango/Manim shaping quirk specific to that word pair; `B01`'s title
     rendered correctly). Caught by direct visual frame inspection at 4K
     resolution, not by GATE T (GATE T's pixel-level kerning check tolerated
     it). Fixed by building the title as three separate `Text()` mobjects
     arranged with an explicit `buff`, which cannot silently collapse the way
     a single string's space glyph can. Re-verified by frame pull: title now
     reads correctly.
   - That fix then tripped GATE T's kerning check again, on an *unrelated*
     element: B03's `DashedLine` divider (`boundary`) — a full-width row of
     evenly spaced dashes reads to the pixel-level letter-run scanner exactly
     like a row of characters with abnormally large inter-letter gaps
     (confirmed by re-running the checker with two different title `buff`
     values and getting an *identical* gap measurement both times — proof the
     flagged region wasn't the title at all). Root-caused by reading the
     checker's own source (`check_kerning_sanity` in `type_check.py`): it
     samples the single densest ink row in the frame and treats it as a text
     line; a full-width dashed rule can out-score real text rows for ink
     density. Fixed the content, not the validator: swapped `DashedLine` for a
     solid, low-opacity `Line` (same visual role as a divider, no periodic
     dash pattern to misread). GATE T went green immediately after.
   - Re-ran `type_check.py` to confirmation: **GATE T: PASS**, 0 FAILs.
5. **Recompiled the final master** after the fixes: 7/7 beats filled, no
   slates, `GATE AUDIO: PASS` at mean_volume −24.0 dB (max −2.9 dB),
   3840×2160, 81.5s.

## Gates

- **GATE L:** all 4 Remotion patterns (`BrutalistHesitantWriter`, `WantQuote`,
  `ClaudeComposerAsk`, `OutroCTA`) were already in the library and had already
  been slated/rendered before this invocation began; no new component
  authoring was needed this pass.
- **GATE T:** FAIL → FAIL (different cause) → **PASS**, per the fix sequence
  above. Final run: 0 pixel-beat FAILs, 0 sweep FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 20–35 words + `lead_silence_s` 0.8 →
  measured `actual_duration_s` **10.43s**, clears the ≥8s/≥9s floor. Frame
  pull at t=4s confirms the "spellcheck"→"check" correction has already
  landed well inside the beat.
- **GATE AUDIO:** PASS, mean_volume **−24.0 dB** (ffmpeg `volumedetect`,
  verified independently of `compile.py`'s own report), max −2.9 dB — well
  above the −40 dB floor.
- **Gate V (frame QC):** pulled frames every 4s across the full 81.5s runtime
  plus targeted zoomed crops of B01's and B03's titles (post-fix) and B03's
  new solid divider. All 7 beats legible, correctly spaced, no overlap, safe
  inset respected.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (7/7 beats, no violations).
- **COMPLETION LAW:** review-cut mp4 mtime (2026-09-01 21:22:35) newer than
  beat_sheet.json mtime (2026-09-01 21:04:04); beat_sheet.json was not touched
  after the compile that produced this review cut — the two GATE T fixes were
  applied to `scenes.py` (content) and resolved by re-rendering the affected
  Manim beats and recompiling, never by editing the beat sheet post-compile.

## Output

`financial-services--claude-liam-ib-check-deck.mp4` — 81.5s, 7/7 beats real
(no slate), 3840×2160 (4K LAW forced the master directly since `compile.py`
was run without `--review`), audible narration throughout (mean_volume
−24.0 dB, ffmpeg-verified). This is the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "financial-services"`
matches no prefix in `playlists.json`'s map; falls to the `hai-simple`
skill-key fallback → "Claude Basics" — same resolution as the
`financial-services--claude-liam-funding-digest`,
`financial-services--claude-liam-fx-carry-trade`, and
`financial-services--claude-liam-gl-recon` siblings already delivered in this
loop.

Metadata file written: `financial-services--claude-liam-ib-check-deck.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct code
link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.
