# SHOTLIST — weekly-recap
# Typed work order per beat. cli-explainer story spine, rendered via the
# run.sh/compile.py pipeline (vox_run.sh/vox_compile.py/type_check.py do
# not exist in this toolkit install — see beat_sheet.json metadata.note).
# Content corrected per a revised kickoff prompt — see metadata.note for
# the full disclosure; this file reflects only the current, shipping cut.

## OPEN — INTRO (B00)

B00 · ClaudeComposerAsk (Remotion)
  action: render -> media/B00.mp4
  props: greeting="Hi,", command="claude \"help me build a real log of what
         I actually did this week\"", output=[3 lines]
  show: composer types -> running indicator -> output lands. Narration opens
        with the host's self-introduction ("Hi, I'm Agrima...") directly in
        B00, per cli-explainer's own reference-example convention.
  status: RENDERABLE

## PROBLEM (B01)

B01 · Manim B01_NotAHighlightReel (scenes.py)
  action: render -> manim/B01.mp4
  show: typographic reveal — "Not a highlight reel." + subline, no composer
  status: RENDERABLE

## CLI LOOP — cycle 1 (B02-B04)

B02 · ClaudeComposerAsk (Remotion) — the ask
  action: render -> media/B02.mp4
  props: greeting="The ask,", command=weekly_recap_v1.py request (article,
         video, Suffolk talk)
  status: RENDERABLE

B03 · ClaudeCodeBeat (Remotion) — the real v1 code
  action: render -> media/B03.mp4
  props: title="weekly_recap_v1.py", code=trimmed real source,
         sparkLine="One list, three lines."
  status: RENDERABLE

B04 · Manim B04_FlatWeek (scenes.py) — the real v1 output, visualized
  action: render -> manim/B04.mp4
  show: three same-weight cards — article/research card, video-production
        icon card (16:9 + 9:16), Suffolk University talk card — no visual
        distinction between what's done and what's just started
  status: RENDERABLE

## CLI LOOP — cycle 2, the required revision (B05-B07)

B05 · ClaudeComposerAsk (Remotion) — the change
  action: render -> media/B05.mp4
  props: greeting="The change,", command=weekly_recap_v2.py revision request
  status: RENDERABLE

B06 · ClaudeCodeBeat (Remotion) — the real v2 code
  action: render -> media/B06.mp4
  props: title="weekly_recap_v2.py", code=trimmed real source,
         sparkLine="Two lists, one honest week."
  status: RENDERABLE

B07 · Manim B07_SplitWeek (scenes.py) — the real v2 output, visualized
  action: render -> manim/B07.mp4
  show: the same three cards, now regrouped under two headers — DONE THIS
        WEEK (checkmark green, article + video cards) and STARTING NEXT
        WEEK (terracotta, Suffolk University card) — a vertical divider
        between the two groups; the visible improvement the revision made
  status: RENDERABLE

## CLOSE (B08-B10)

B08 · Manim B08_TheLesson (scenes.py)
  action: render -> manim/B08.mp4
  show: three-line typographic beat — the lesson (done vs next is the whole
        difference, not a formatting detail)
  status: RENDERABLE

B09 · ClaudeComposerAsk (Remotion) — HANDOFF LAW
  action: render -> media/B09.mp4
  props: greeting="Your turn.", command=(viewer prompt, read + discussed
         in narration)
  status: RENDERABLE

B10 · ClaudeTitleOutro (Remotion)
  action: render -> media/B10.mp4
  props: title="This Week: What Shipped, What's Next.",
         handle="@HumanitariansAI", subline="logged, not hyped"
  status: RENDERABLE

## Notes

- No pantry / archival stills used in this reel — every visual is either a
  Claude-skin Remotion composer/code/outro beat or a from-scratch Manim
  scene (scenes.py). No open pantry slots, no SHOPPING.md.
- weekly_recap_v1.py and weekly_recap_v2.py are real, runnable Python
  scripts in this reel folder — both were actually executed to capture the
  CODE/OUTPUT beats' real source and output (THE ACTUAL-CODE LAW). See
  FACTCHECK.md for the captured terminal transcripts.
- Target duration: 1-3 minutes per explicit user request (a range, not an
  exact target) — confirmed only once Kokoro audio is generated and
  measured (audio-first principle).
- `@HumanitariansAI` matches the branding precedent set on this user's other
  reels in this book; af_bella (Bella) voice per explicit request for a
  woman's voice — the only female voice this toolkit ships (see
  beat_sheet.json metadata.note).
- Content correction: this cut replaces the original build's fashion-
  sustainability framing wholesale with the corrected kickoff's three items
  (article/research, video production, Suffolk University talk) — see
  beat_sheet.json metadata.note for the full disclosure.
