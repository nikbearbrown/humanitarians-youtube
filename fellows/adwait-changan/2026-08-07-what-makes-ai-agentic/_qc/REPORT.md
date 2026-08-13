# VISUAL QC REPORT — Episode 1, "What Makes an AI Agentic"

VISUAL QC LAW. The mp4 probe is a file check and does not count as QC. This pass sampled
the contact sheet plus per-beat frames at 50 %, 88 % and (where a settle animation was in
question) 98 % of each beat's span, and **read the PNGs**.

Frames in `_qc/frames/`. Contact sheet: `../qc-sheet.png`.

## Defects found and fixed

### D1 — B03 · double numbering · **BLOCKER** · FIXED

`ClaudeWindow` numbers `artifactLines` itself (`{i + 1}.`, hardcoded). The beat sheet also
carried manual `"1. "`, `"2. "`, `"3. "` prefixes, so the frame rendered
**"1.  1. Search an airline site…"**. Visible, embarrassing, and would have shipped.

*Root cause:* authored against an assumed contract instead of the component source.
*Fix:* stripped the manual prefixes from `beat_sheet.json`. Verified in
`_qc/frames/FIX_2026-08-07_B03.png` — single numbering.

### D2 — B03 · honesty disclosure rendered as a plan step · **MAJOR** · FIXED

The line "Nothing was searched. Nothing was booked…" was a fourth `artifactLine`, so it
rendered as **"4."** — reading as a fourth thing the chatbot planned to do, which inverts
its meaning. The disclosure required by FACTCHECK row 3 was actively undermined by its own
placement.

*Fix:* the artifact now carries the three plan steps only; the disclosure moved to the
spark line beneath the card, "**Nothing was actually booked.**", where it reads as the
episode's judgement rather than as part of the plan. FACTCHECK row 3 updated to match.

### D3 — B03 · canvas underfill · **MAJOR** · FIXED (component root cause)

The card rendered 1100 px wide on a 1920 stage — 57 % of the width, ~35 % of the height,
with the type at 19 px. Fails FILL-THE-CANVAS / TYPESIZE LAW: the graphic could have been
halved and still fit with room to spare.

*Root cause:* `runtime/remotion/src/scenes/ClaudeWindow.tsx` **declares `width`, `height`
and `fontSize` in its zod schema but never reads them** — the JSX hardcodes `width: 1100`,
`fontSize: 19/32/26/20`. The props were dead. This is a component bug, not a beat-sheet
mistake, and it silently affects every reel that has ever tried to set them.

*Fix (toolkit edit, backwards compatible):* wired the declared props through —
`cardW = width ?? 1100`, `fs = fontSize ?? 19`, with the heading, title bar and spark line
deriving from `fs` at their existing ratios (×1.68, ×1.05, ×1.37). Defaults are unchanged,
so no existing reel re-renders differently. B03 now passes `width: 1560, fontSize: 27`.

### D4 — B09 · underfill + fails to show what the voice enumerates · **MAJOR** · FIXED

`MedhavyConceptCard` rendered a small centred card (~31 % of frame height) whose body was a
single run-on paragraph. The narration explicitly says *"Three conditions"* and then lists
them — so the screen was telling, not showing, on the beat that carries the episode's
practical takeaway. `MedhavyConceptCard` has no width/fontSize props to fix it with.

*Fix:* swapped the pattern to `ClaudeScienceLayerStack`, three layers, one per spoken
condition, terracotta accent on the third ("You can check the result") which is the one the
narration singles out. Caption carries the "you have a rumour" line. Narration unchanged, so
no audio was regenerated. Verified in `_qc/frames/FIX_2026-08-07_B09.png`.

## Checked and passed

| Beat | Finding |
|---|---|
| B02 | The reference for canvas fill in this reel — three layers spanning the frame, accent on `Return`, caption anchoring the bottom. |
| B05 | At 88 % the settle line is mid-fade; at 98 % "Now it can act." is fully rendered in terracotta. Correct animation, not a defect — first read was a sampling artefact. |
| B06 | Code legible at full size, comments intact, no horizontal clipping of the longest line. |
| B08 | All six chips land by 88 % (the contact sheet's single mid-beat frame showed five — sampling, not truncation). "Failure that reports success" holds last, as authored. |
| BVDT | Five verdict lines, all inside the card, no overflow. |
| B00 / BHTF | Composer type legible; the two typing beats are the only two, per HANDOFF LAW. |
| BOUT | Title, handle and subline all inside the title-safe inset. |

## Rubric audit (9 points)

| Point | Result |
|---|---|
| Edge bleed / clipping | PASS — nothing crosses the frame edge on any sampled frame. |
| Title-safe margins | PASS — widest element after the fix is B03 at 1560 px, inside the 1728 px safe span. |
| Container overflow | PASS — no text escapes its card; B03's longest line wraps inside the widened card. |
| Collision | PASS. |
| Offscreen anchors | PASS. |
| Legibility | PASS after D3/D4 — B03 body type 19 → 27 px, B09 now stack-scale. |
| Brand bug | Channel identity carried by the `@HumanitariansAI` chip on B00/BHTF and the full handle on BOUT. No separate corner bug exists in this toolkit's Claude patterns; consistent with the previously shipped reel. |
| Aspect | PASS — 16:9 throughout; `ClaudeScience*` patterns author at 1280×720 and scale cleanly. |
| Canvas fill | PASS after D3/D4. Act cards B01/B04 keep generous negative space — accepted as deliberate (they are 12–13 s breathing beats between acts, and the law permits negative space as a design choice), not as accidental dead space under undersized content. |

## Accepted, not fixed

- **`lane histogram: remotion 13/13 (100 %)` warning.** `compile.py` warns above a ~40 %
  single-language cap. That cap is `deep-explainer` doctrine for pantry/vox quota; this is
  an `ai-explainer` reel with no pantry stills and no Manim installed, and every beat is a
  distinct Remotion pattern rather than repeated wallpaper. Same disposition as the
  previously shipped fellow reel.
- **Three `ClaudeScienceLayerStack` beats (B02, B07, B09).** Non-consecutive, and each
  carries a genuinely different three-item enumeration. ILLUSTRATE LAW's smell is two
  *consecutive* beats sharing a scheme; that does not occur. Verified programmatically —
  no two adjacent beats use the same pattern.

## Verdict

> **Zero BLOCKER, zero MAJOR remaining.** 4 defects found, 4 fixed, 3 beats re-rendered
> (B03, B09 in this episode; the component fix also corrected Episode 2's B03).
> Build is clear for the clean master.
