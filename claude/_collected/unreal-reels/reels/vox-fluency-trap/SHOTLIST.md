# SHOTLIST — vox-fluency-trap

**Why the Group That Learned Less Was Sure It Learned More** · 16:9 · ~113s est. (13 beats)
Accents: dusty blue `#5B7B9C` = checking / hand-coders · terracotta `#D35F43` = delegation / AI group · gold `#F5D061` = editor's pen (one voice per graphic).
Facts to verify before ship: 67% vs 50% (17 pts), interrogation 65–86%, delegation 24–39% — Shen & Tamkin, Anthropic, Feb 2026, arXiv:2601.20245.

Shot-type histogram: CARD 2 · STILL 1 · FOOTAGE 1 · DOCUMENT 1 · GRAPHIC 5 · COMPOSITE 3 — max consecutive same-type: 2 (B09–B10 GRAPHIC/COMPOSITE-manim). Lint: pass.

---

## B01 — CARD (title) · own · ~10.0s
Cue: "Two groups of engineers… feeling smarter."
Copy: **Why the group that learned less was sure it learned more** / sub: *the fluency trap*
Design system only. No media slot.

## B02 — STILL · archive · kenburns · ~7.7s
Cue: "A research lab took a group of junior engineers…"
Slot: `media/B02.png` + `media/B02.source.txt` (required — archive slot)
Archive queries:
- https://www.loc.gov/free-to-use/?q=computer+programmers+office
- https://catalog.archives.gov/search?q=computer%20programmers%20office%20photograph
- https://commons.wikimedia.org/w/index.php?search=programmers+computer+lab+historic+photograph&title=Special:MediaSearch&type=image
Fallback t2i prompt: archival photograph of young software engineers at computer workstations in an office, 1980s-90s print reproduction, desaturated on aged newsprint *(if used, source flips to `ai` → STAND-IN X until replaced)*

## B03 — GRAPHIC · own · manim · ~9.2s
Cue: "Half got an AI assistant. Half had to write every line by hand."
Manim: `IsotypeSplitGroups` — one square grid divides into terracotta (AI) and blue (hand) halves on "Half". No headcount shown (card exclusion: no n=52).

## B04 — FOOTAGE · ai · ~7.3s
Cue: "The AI group finished clean."
Seed still: `media/B04.png` → i2v to `media/B04.mp4`
t2i prompt: computer screen with tidy commented Python code and a passing test indicator, flat print reproduction on aged newsprint, desaturated editorial collage
i2v prompt: code lines type themselves rapidly and settle, a small check mark stamps in the corner, subtle paper-plane parallax, no camera move (key action in first 60%)

## B05 — DOCUMENT · own · highlight · ~8.5s
Cue: "Then the twist. Everyone took the same quiz…"
Quote plate: "**Do you understand what the code does?**" — attribution: *14-question comprehension quiz*. Gold highlighter sweeps "understand" timed to the word.

## B06 — GRAPHIC · own · manim · ~9.2s
Cue: "The hand-coders averaged sixty-seven percent…"
Manim: `BarCompare` — blue 67 vs terracotta 50, count-up; gap bracket "17 points" lands on "Seventeen".
viz.note: verify 67/50.

## B07 — COMPOSITE · ai · hold · ~8.5s
Cue: "…the AI group felt fine."
Plate: `media/B07.png` — reuse/re-crop of B04 still, pinned smaller like a clipping.
Annotation (assembly plane): hand-drawn terracotta ring around the check mark, timed to "fine".

## B08 — GRAPHIC · own · manim · ~8.8s
Cue: "…understanding doesn't form while the code gets typed."
Manim: `CheckLoopCycle` — blue cycle read → test → question → break → fix draws stage-by-stage timed to the spoken verbs; a small grey "typing" node sits outside the loop.

## B09 — GRAPHIC · own · manim · ~9.2s
Cue: "The engineers who interrogated the model…"
Manim: `RangeBars` (1 of 2) — blue range bar 65–86 rises. viz.note: verify 65–86.

## B10 — COMPOSITE · own · manim · ~7.3s
Cue: "The engineers who delegated…"
Manim: `RangeBars` (2 of 2) — terracotta range bar 24–39 drops in beside blue.
Annotation: gold highlighter bar sweeps the gap between ranges on "Opposite". viz.note: verify 24–39.

## B11 — GRAPHIC · own · manim · ~8.8s
Cue: "Every clean artifact you can't explain is a small loan…"
Manim: `DebtLedgerStack` — 6 clean-artifact cards stamp onto a pile one per phrase; unscaled terracotta ledger meter ticks up with each. Metaphor beat, no numbers.

## B12 — COMPOSITE · ai · hold · ~8.5s
Cue: "…until the system breaks… The loan comes due."
Plate: `media/B12.png`
t2i prompt: computer screen filled with a stack-trace error page, harsh and dense, printed reproduction desaturated on aged newsprint, editorial collage
Annotation (assembly plane): B11's debt meter persists; terracotta "DUE" stamp lands on "due".

## B13 — CARD (endcard) · own · ~10.0s
Cue: "The machine is a better typist than you will ever be…"
Copy: **Let it type. Keep the checking.** / sub: *from The Reallocation Engine, chapter 1*

---

## Slot inventory (human work order)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` + `B02.source.txt` | archival office/programmers photo | LOC / NARA / Commons links above |
| `media/B04.png` → `media/B04.mp4` | clean-code still → i2v clip | t2i + i2v prompts above |
| `media/B07.png` | clipping-crop of B04 still | derive locally, no spend |
| `media/B12.png` | error-page still | t2i prompt above |

Everything else is CARD / DOCUMENT / GRAPHIC — Manim + design system, no media generation, no credits.
