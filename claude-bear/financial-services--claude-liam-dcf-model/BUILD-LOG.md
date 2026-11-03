# BUILD-LOG — financial-services--claude-liam-dcf-model

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-dcf-model/beat_sheet.json`,
following the sibling `financial-services--claude-liam-3-statement-model`
redo (built the same day) as the structural template.

**Source-gap finding:** the source sheet is NOT a placeholder shell — its
narration already states the `dcf-model` skill's real facts: it builds a
real DCF model for equity valuation, retrieves financial data from SEC
filings and analyst reports, builds cash flow projections with WACC
calculations, performs sensitivity analysis, and outputs a professional
Excel model with an executive summary; triggered when a user needs to
value a company using DCF methodology or requests intrinsic-value
analysis with growth projections and terminal-value calculations. No
reconstruction needed.

**The call:** register re-registered Teardown -> Plain. Source's B03
"what it gets right / what it bites" design-tell verdict removed; Plain
keeps only the mechanism (assumptions run through a fixed formula) and its
two failure directions (a number that swings a lot isn't broken; a number
that holds steady isn't proven right). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER
LAW: "judgment" -> "the formula" — the naive assumption that a DCF number
reflects Claude's own judgment about the company, corrected to: it is
Claude running a formula over assumptions it was given. Added a
wrong-guess beat (B01: analyst judgment vs. formula-fed assumptions,
falsified by "feed it a different assumption and the valuation moves
without protest") and an anchor (B02 -> B03: the discount-rate/WACC dial
driving a single valuation readout, planted then paid off as a
sensitivity grid) per this factory's PHASE 1 structure requirement — the
source's Teardown shape (anatomy/pipeline/design-tell/verdict) carried
neither. Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Kept the source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF,
BOUT) per the redo contract.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.92s (clear of the >=9s/>=8s TIMING LAW
   floor) on the first narration draft (34 words + `lead_silence_s: 0.8`).
   Durations: B00 10.92s, B01 21.16s, B02 13.97s, B03 22.25s, BCRY 10.84s,
   BHTF 20.71s, BOUT 4.39s (+1.0s tail).
2. Verified B00's correction on frame pulls at t=6.5s/9.5s: "judgment"
   still mid-typing (accent color) at 6.5s, fully backspaced and replaced
   with "the formula?" by 9.5s, legible with margin before the 10.9s
   cutoff. TIMING LAW satisfied on the first pass.
3. Wrote `scenes.py` (3 Manim scenes, reel-unique names `DCFB01Scene` /
   `DCFB02Scene` / `DCFB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   — the shell moved it to a background task past the 120s inline
   timeout; blocked on it with `TaskOutput` rather than ending the turn,
   per this skill's no-orphaned-render rule. All four rendered clean.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (4K LAW),
   mean_volume -24.1 dB.
6. GATE T (`type_check.py`) FAILED on the first pass: 1 bbox-overlap
   (§8.6b) in B02. Root-caused, not patched around: the dial card's INK
   border outline (a hollow rounded-rectangle ring) was itself qualifying
   as a pseudo "text-run" blob under the checker's shape heuristics
   (width/height ratio >= 1.5, fill-ratio >= 4% of its own bounding box),
   so its bounding box — which necessarily spans the whole card —
   registered as "overlapping" the real label text sitting inside it.
   Confirmed by direct comparison against the sibling reel's identical
   `_card()` helper: the sibling's cards use `border_width=2` on
   near-square proportions (fill ratio ~3.8%, under the checker's 4%
   floor); mine used `border_width=2.5` on a much more elongated 3.2x1.1
   card (fill ratio ~5.15%, over the floor). Fixed the actual content,
   not the validator: widened the dial card to 3.6x1.3 and dropped
   `border_width` to 1.5 (fill ratio ~2.6-2.9% verified across all 88
   sampled frames of the re-rendered clip, comfortable margin under the
   4% floor — the first `border_width=2` attempt only got to ~3.9-4.1%,
   too close to the cutoff and still intermittently FAILed on some
   frames' compression noise). Also lowered the B02 cash-flow-bar
   baseline/heights so the tallest (terminal-value) bar's top edge
   cleared "THE ANCHOR" label text with margin — an earlier visual
   inspection (before the bbox-overlap numeric root-cause was found)
   caught the bar visibly overlapping that label at some frames.
   Re-rendered B02, recompiled: GATE T -> PASS, 0 FAILs, second pass.
7. Gate V (visual, manual): pulled frames every 4s across the full 105.2s
   runtime (27 frames) and read every one directly. Found ONE real defect
   GATE T's automated checks did not catch: in B03, the "cash flows" and
   "terminal value" bar labels (both wider than the 0.5-unit bars they
   sat under, with only `buff=0.5` between the two bars) printed directly
   on top of each other into one fused, illegible run at the beat's final
   frames. Fixed by widening the gap between the two bars (`buff=0.5` ->
   `1.6`) and width-capping both labels with `_fit_text(..., 1.3)` so
   neither can overflow its column regardless of text length. Re-rendered
   B03, recompiled, re-verified across all 88 sampled frames of the new
   clip (0 bbox-overlap FAILs) and re-pulled the Gate V frame at the
   defect's timestamp: labels now sit cleanly apart with margin. Re-ran
   GATE T after this fix -> still PASS. No other defects found across
   B00/B01/B02/BCRY/BHTF/BOUT on the full 27-frame sweep.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master -> mean_volume **-24.1 dB**, max -3.0 dB. Master mtime
   (1788282064) is newer than beat_sheet.json mtime (1788280929).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (B02 fix above)
- Gate V: PASS, second pass (B03 fix above) — no defects remain
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: duration 105.25s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — same structural disposition as every other hai-simple reel in
this family (B00 writer + BCRY + BHTF + BOUT mandated REMOTION against 3
GRAPHIC body beats).

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback, fell through to matching the skill name itself:
`hai-simple` is a literal key in the map, resolving to **Claude Basics** —
same resolution as the `3-statement-model` sibling reel.

Metadata file written: `financial-services--claude-liam-dcf-model.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the two fix
passes above). Proceeding to Phase 4 (4K render + deliver.py) in this same
invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-dcf-model.mp4 \
   financial-services--claude-liam-dcf-model-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-dcf-model/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-dcf-model/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `bcd2348e`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
