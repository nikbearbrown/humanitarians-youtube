# VISUAL QC REPORT — Episode 3, "Tools: Giving a Model Hands"

VISUAL QC LAW. Contact sheet plus per-beat frames at 95 % of span for every beat carrying
dense text or a staged reveal, read as PNGs. Frames in `_qc/frames/`.

## Defects found and fixed

### D1 — B02 · word-orphaning in two feed labels · **MINOR** · FIXED

Two of the three feed labels overran the destination card's line width and wrapped, dropping
a single word onto its own line:

```
✓ description — your docstring,
verbatim
✓ parameter schema — from your type
hints
```

The orphans (`verbatim`, `hints`) sit at the same indent as the checked items, so they read
as two extra list entries — the beat appeared to name *five* things crossing the wire on a
beat whose entire point is that there are **three**. A wrap defect that changed the meaning.

*Fix:* shortened the labels to fit one line each — `description — your docstring` and
`schema — from your type hints`. Both terms are spoken in full in the narration, so nothing
is lost. Verified in `_qc/frames/B02_fixed.png`: three clean rows, no orphans.

### D2 — B07 · card over-wide for its content · **MINOR** · FIXED

The card was authored at `width: 1700, fontSize: 22` to guarantee the 80-character alignment
rows would not wrap. They didn't — but the longest row only occupied ~1100 px, leaving a
dead band of roughly 600 px inside the card's right edge, with the type smaller than it
needed to be. Undersized type plus accidental empty space is exactly what FILL-THE-CANVAS /
TYPESIZE LAW targets.

*Fix:* `width: 1440, fontSize: 26`. Recomputed the longest line first
(80 chars × ~0.6 em × 26 px ≈ 1248 px, plus 80 px padding = 1328 px, inside 1440) so the fix
could not reintroduce a wrap. Verified in `_qc/frames/B07_fixed.png`: larger type, no wrap,
alignment columns intact, card sized to its content.

## Checked and passed

| Beat | Finding |
|---|---|
| B03 | The episode's key frame, and it holds. `wire_view()` output legible at `fontSize: 24`; the description's wrapped continuation lines indent correctly under the label; `(292 chars total)` visible; `not sent — the function body` lands last and alone. Good vertical fill. |
| B05 | All 14 lines of `to_schema()` legible with no horizontal clipping — including the longest, the `"properties"` comprehension. Verified the rendered code matches `inspect.getsource()` output, and counted the lines on the frame to confirm the narration's "fourteen". |
| B07 | Alignment columns hold after the resize; `function bodies identical: True` — the control for the episode's central claim — is clearly readable. |
| B08 | All four chips land by 95 %. The contact sheet's single mid-beat frame showed three; sampling artefact, not truncation. Same false alarm as Episode 1's B08 — worth remembering that the contact sheet samples one frame per beat and will routinely catch grids mid-reveal. |
| B02 | Arc completes to "The model"; settle line `It reads the label.` renders in terracotta. |
| B06 / B09 | Three layers each, terracotta accent on the third, captions anchoring the bottom. |
| BVDT | Five verdict lines inside the card, no overflow. |
| B00 / BHTF | Composer legible; typing confined to these two beats per HANDOFF LAW. |
| BOUT | Title, handle, subline inside the title-safe inset; "Episode 3 of 10" present. |

## Rubric audit (9 points)

| Point | Result |
|---|---|
| Edge bleed / clipping | PASS. |
| Title-safe margins | PASS — widest element is B03 at 1620 px, inside the 1728 px safe span. |
| Container overflow | PASS — B03's 8 lines, B05's 14 code lines and B07's alignment rows all sit inside their containers without wrapping. Checked specifically because all three are monospaced and pre-formatted, where a wrap destroys meaning rather than just looking untidy. |
| Collision | PASS. |
| Offscreen anchors | PASS. |
| Legibility | PASS after D1/D2. |
| Brand bug | `@HumanitariansAI` chip on B00/BHTF, full handle on BOUT — consistent with Episodes 1–2. |
| Aspect | PASS — 16:9 throughout. |
| Canvas fill | PASS after D2. B01/B04 act cards keep deliberate negative space (10–13 s breathing beats). B05's code panel has room below 14 lines — the `ClaudeCodeBeat` panel is a fixed-height terminal frame; accepted as the component's house look, as in Episodes 1–2. |

## Accepted, not fixed

- **`lane histogram: remotion 13/13 (100 %)` warning** — as in Episodes 1–2. The ~40 % cap
  is `deep-explainer` pantry/vox doctrine; this is an `ai-explainer` reel with no pantry
  stills. Nine *distinct* patterns across 13 beats here, the widest spread in the series, so
  the wallpaper risk the cap guards against does not apply.
- **Two `ClaudeWindow` beats (B03, B07)** — separated by three beats, both playing the same
  deliberate role: real printed output of the file that ships with the episode. A rhyme, not
  wallpaper.

## Process note

Both prior episodes' traps were avoided this time by building them into the process rather
than remembering them:

- **The auto-numbering trap** (Ep 1 D1/D2, Ep 2 D1) — B03 and B07 were authored with
  `numbered: false` from the start, so no numbered payload or trace ever rendered.
- **The clobber trap** (Ep 2) — the beat-sheet patch waited for `remotion_scenes.py` to print
  `done`, not for the last `media/*.mp4` to appear, and the JSON was **read back** after
  writing to confirm the patch survived. It did, first time.
- **Transcription drift** — B05's `code` prop was generated by
  `inspect.getsource(tools.to_schema)` at authoring time rather than copied by hand, so the
  beat cannot silently diverge from the file. Worth doing for every future code beat.

## Verdict

> **Zero BLOCKER, zero MAJOR.** 2 MINOR defects found, 2 fixed, 2 beats re-rendered
> (B02, B07). Build is clear for the clean master.
>
> Cleanest QC pass of the series so far — the two carried-forward traps produced no defects.
