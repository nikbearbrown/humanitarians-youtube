# SHOTLIST — The All-Clear That Wasn't All There

## ~1:47 (107.537s) measured total · 9 beats · all Manim, no pantry/toolkit assets

Durations below are the real Kokoro-measured `actual_duration_s` values from
`beat_sheet.json` (B00 is the fixed 4.049s silent-track target; B01-B08 are
measured `af_bella` narration lengths via `generate_audio_kokoro.py` +
ffprobe). `scenes.py` is authored and each scene's `self.wait()` budget is
tuned to these exact numbers — see that file's per-scene comments.

| Beat | Act | Lane | Medium | Scene class | Measured Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | `B00_TitleCard` | 4.05s | Silent title card, `audio_policy: "silence"`, real silent mp3 via ffmpeg anullsrc |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | `B01_ExecSummary` | 14.23s | Fellow name/role badge + spoken one-line thesis summary, streamed with narration |
| B02 | HOOK | manim | GRAPHIC | `B02_AllClearHook` | 9.74s | The shipped "All Clear!" email header + "No new high-priority regulatory items detected" message, recreated verbatim, with a foreshadow highlight |
| B03 | SETUP | manim | GRAPHIC | `B03_FourCardGrid` | 14.02s | Real shipped 4-card "Monitored Sources" grid: SEC Press Releases, Federal Register, FINRA Enforcement, CFTC Regulations |
| B04 | DISCOVERY | manim | GRAPHIC | `B04_FiveRealFeeds` | 11.66s | 4 shown source names next to the workflow's real 5 RSS-feed node names, missing 5th (Investment Advisor Rules) highlighted gold |
| B05 | FIX | manim | GRAPHIC | `B05_BeforeAfterFix` | 16.51s | Before (4 cards) / after (5 cards) both visible, new card highlighted, conformance-check confirmation |
| B06 | ASIDE | manim | GRAPHIC | `B06_StaleNoteClosed` | 20.26s | Stale `FINDINGS.md` note, two-item checklist checked off, stamped "ALREADY FIXED — confirmed 2026-09-29" |
| B07 | TAKEAWAY | manim | GRAPHIC | `B07_Statement` | 12.00s | 3-line statement card, dark background |
| B08 | SIGN-OFF | manim | GRAPHIC | `B08_BrandOutro` | 5.06s | @HumanitariansAI, in for Sai Pranavi J. — short beat, single combined reveal |

## Emoji-glyph substitution (found and fixed this build, before rendering the real beats)

The source material (`B5-VERIFICATION.md`) writes each card label with a leading
emoji glyph (e.g. "\U0001F4F0 SEC Press Releases"). A direct pre-build test —
`Text("\U0001F4F0 SEC Press Releases", ...)` rendered through this
environment's Manim/Pango/Cairo text-to-SVG-path pipeline — logged
`Unsupported element type: <class 'svgelements.svgelements.Image'>` and the
glyph rendered as **blank space**, not a visible tofu box, not a crash: a real,
silent legibility defect that no automated gate catches (the surrounding text
still passes). Every card badge in B03/B04/B05 substitutes a small drawn
circle + short mono abbreviation (SEC / FED / FIN / CFTC / IAR) for the
dropped emoji; the verbatim text label itself (e.g. "SEC Press Releases") is
unchanged. See `scenes.py`'s module docstring and `BUILD-LOG.md`.

## Side-by-side / two-column legibility check

B04 uses a two-column layout (SHOWN ON THE CARD vs. REAL WORKFLOW FEED NODES)
with a vertical divider positioned from the two columns' own measured bounds,
not a guessed constant. B05 stacks BEFORE (4 cards) above AFTER (5 cards)
rather than side-by-side, so both full grids are legible together without a
divider crossing either row. Both were spot-checked by extracting real
rendered frames after the first `./art run` pass — see `BUILD-LOG.md` for the
frame-by-frame findings.

## QC plan

- Pre-flight (before first render): GATE A/W static scene check
  (`runtime/scripts/build_safety.py` invoked via `./art run`) — catches
  shape-distinctness and margin/off-frame issues before spending a render.
- Post-render: GATE V `final_frame_check.py --lenient` on the true clean
  master (never a `-slate.mp4` watermarked review cut), plus manual frame
  extraction via ffmpeg at multiple timestamps per beat — especially B03,
  B04 and B05's card grids — looked at directly, not inferred from the
  BLOCKER/MAJOR count alone.
