# SHOTLIST — Week 6 Progress

Typed work order. Eight beats, **no open media slots**. Two are registered Remotion compositions; six are Manim
scenes in `scenes.py`. Narration is `SCRIPT.md` verbatim: B00 is section 1, B01-B06 are sections 2-7, BOUT is
section 8. Same structure and style as the Week 3 progress video.

**Status: audio approved; both review cuts are being built with every gate on. `./art final` waits for your OK.**

## Rules for every visual

- Simple illustrative graphics only. No photos or recordings of you, no person icons, no real company, product or
  tool logos. **No Google, reCAPTCHA or Cloudflare logos and no screenshots of real challenge pages:** a CAPTCHA is a
  plain drawn grid of squares; Claude Code is a generic drawn terminal. Nothing on screen is data.
- **Fill the frame (Gate V):** content covers at least 55% of the safe area at 50% and at 85% of every beat. Each scene lays out
  its cast early and scales it up to fill the stage.
- **Portrait (9:16):** native layouts, not a crop (`vertical/scenes.py` is `scenes.py` with `PORTRAIT = True`). Text is at
  least 72 px at 2160x3840 (the scene scan flags anything under 30 pt, about 88 px of ink) and sits above 86% of the frame
  height; the bottom 14% stays empty. Casts stack in one column, and crowded scenes are split into more phases.
- **Gate T:** no thin tick marks or outlines near text. The dial ticks are pale, drawn on a soft tint, and kept away from every
  label; cards that hold text use a soft border; ticks on the lists are thick.
- Palette `humanitarians`: ink `#2F2A26`, crimson `#E4572E` (problem or changed, one accent per beat), teal `#1F4E5F`
  (done), slate `#29335C` (structure), ground `#F3EBDD`. Gold and sage are fills only, never text.
- BOUT is the only beat marked `sparse_by_design` (same reason as your other progress videos). No other exemptions.
- No dates on screen or in files you write.

## Library check

`./art scenes` was searched first for the cold open and outro (composer, logo outro); the checks for the body scenes follow Week 3.

| Need | Result |
|---|---|
| Cold open | **Hit:** `ClaudeComposerAsk`, `ClaudeComposerAsk916` |
| Outro | **Hit:** `LogoOutro`, `LogoOutro916` |
| Grid of squares, paper pages, terminal, landscape and vertical frames, dial, numbered list, claim-to-source rows, cursor path | Custom Manim (no library match for these notes-style cards) |

## Beats

| Beat | Act | Lane | Asset | What the viewer sees | Length (s) |
|---|---|---|---|---|---|
| B00 | INTRO | remotion | `ClaudeComposerAsk` | Claude composer: "Hi, Keya", the ask types in, three result lines | 11.24 |
| B01 | THIS WEEK'S VIDEO | manim | `B01_ThisWeeksVideo` | Title of the explainer (text only); a drawn grid of squares "CAPTCHAs on websites"; two drawn papers "two research studies"; a drawn terminal "Claude Code"; the three small with a star "all new for me" | 12.63 |
| B02 | FILM AS CODE, DEEPER | manim | `B02_FilmAsCodeDeeper` | Angle brackets to a film frame; a wide and a tall frame "landscape" "vertical"; "narration: the same", "checks: not the same"; "text size" with "41 px" for landscape and "72 px" for vertical | 16.90 |
| B03 | NOTHING UNCHECKED | manim | `B03_NothingUnchecked` | claim to source with a tick ("my rule"); five rows turn crimson ("five things to fix", "lines that said more than the sources did"), the last turns slate ("one source that couldn't be opened"); slots fill teal ("pointed to a source"); rows ticked ("easy to fix") | 18.26 |
| B04 | SHAPES THAT LOOK LIKE TEXT | manim | `B04_ShapesLikeText` | A page of lines "the text-size check"; a dial on a crimson tint "tick marks on a dial", "read as tiny letters"; the same dial on a teal tint with paler ticks and a tick, "a paler colour", "no words changed" | 10.86 |
| B05 | ONE SENTENCE, FOUR NUMBERS | manim | `B05_FourNumbers` | A numbered card of four ragged bars (crimson, "one sentence, four numbers", "it read oddly"); then four full bars each ticked, "four complete thoughts" | 9.09 |
| B06 | THE TAKEAWAY | manim | `B06_Takeaway` | A cursor path watched by an eye ("more and more websites check how I behave"); a check box pointing at what it measures; a video frame ticked; claim to source ticked; a frame with an eye "a second look" | 12.76 |
| BOUT | OUTRO | remotion | `LogoOutro` | Humanitarians AI mark and `@HumanitariansAI` handle | 4.18 |

Lengths are the measured narration (total 95.92 s).

## Portrait notes

- 9:16 stacks pairs vertically (claim above source, dial above its page) and splits B01, B02 and B04 into more phases so each fills the stage.
- Text sizes were checked at 9:16 with the scene scan: nothing under 30 pt, nothing below the 86% line.
- 9:16 outro keeps the `@HumanitariansAI` line, which the toolkit places below 86% of the frame height (as in your Week 3 video).

## Cue times

Scene cues come from word timings measured on the generated audio (faster-whisper). If any beat's audio is regenerated,
re-measure and update the `go()` times in `scenes.py`, then re-copy to `vertical/scenes.py`.

## Listen for

- "Keya" (custom pronunciation), "CAPTCHAs" (no plural "s"?), "Brutalist", "Claude Code", "forty-one" and "seventy-two".
