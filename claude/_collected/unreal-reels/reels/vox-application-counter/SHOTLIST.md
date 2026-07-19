# SHOTLIST — vox-application-counter

**Why the Application Counter Is Lying to You** · 16:9 · ~94s est. (11 beats)
Accents: terracotta `#D35F43` = the counter / cold channel · dusty blue `#5B7B9C` = connections / return · gold `#F5D061` = editor's pen (once per graphic).
Two-number cap (card exclusion): only **~0.2%** (B06) and **54%** (B07) appear on screen. Both inherit the chapter's [verify] flags — see FACTCHECK.md.

Shot-type histogram: CARD 2 · STILL 1 · FOOTAGE 1 · DOCUMENT 1 · GRAPHIC 5 · COMPOSITE 1 — max consecutive same-type: 2 (B05–B06). Lint: pass.

---

## B01 — CARD (title) · own · ~8.4s
Cue: "The most disciplined job search in the room…"
Copy: **Why the application counter is lying to you** / sub: *the reallocation principle*

## B02 — STILL · ai · kenburns · ~9.6s  ← MEDIA SLOT
Cue: "Eight a.m. Coffee. Seventeen open tabs…"
Slot: `media/B02.png`
t2i prompt: overhead photograph of a cluttered desk with a laptop showing many browser tabs and a color-coded spreadsheet, cooling cup of coffee, morning light, desaturated print reproduction on aged newsprint, editorial collage
Synthetic — disclosure line in credits.

## B03 — GRAPHIC · own · manim · ~9.2s
Cue: "And the counter is the trap."
Manim: `CounterTicks` — mono odometer digits tick 28 → 41 in terracotta, submission stamps land beneath. Dressing, not a data claim: no axis, no chart.

## B04 — FOOTAGE · ai · ~6.4s  ← MEDIA SLOT
Cue: "…the machine underneath, quietly deleting most of what it's fed."
Seed still: `media/B04.png` → i2v to `media/B04.mp4`
t2i prompt: editorial paper-collage illustration of documents feeding into a slot in a large flat machine, shredded paper strips below, cream and charcoal palette, desaturated print on aged newsprint, flat graphic style
i2v prompt: pages slide steadily into the machine's slot while thin paper strips drift down beneath it, slow constant motion, no camera move, flat collage plane (key action in first 60%)

## B05 — GRAPHIC · own · manim · ~10.4s
Cue: "Some postings were never real jobs…"
Manim: `SilentDeletions` — application grid; three named strike-waves: *never real* / *no sponsorship* / *auto-rejected*. NO percentages (two-number cap).

## B06 — GRAPHIC · own · manim · ~6.0s — **number 1 of 2**
Cue: "Cold applications convert at roughly zero point two percent…"
Manim: `OneInFiveHundred` — 500 pale squares count up, exactly ONE fills ink. The arithmetic is drawn: 0.2% × 500 = 1.

## B07 — DOCUMENT · own · highlight · ~8.0s — **number 2 of 2**
Cue: "Meanwhile, about fifty-four percent of hires…"
54% set enormous, claim beneath, gold sweep on "personal connections."

## B08 — GRAPHIC · own · manim · ~10.4s
Cue: "…the good channel pays back on a delay."
Manim: `TwoClocks` — terracotta timeline sprouts instant ticks; blue timeline stays quiet, then lands conversation → referral → offer. No time units.

## B09 — COMPOSITE · own · manim · ~10.4s
Cue: "Your instincts read the silence as failure…"
Manim: `InstinctRing` — counter redrawn small, hour-blocks drift to it, HandRing (terracotta) lands on "loudest." One ring only.

## B10 — GRAPHIC · own · manim · ~7.2s
Cue: "The fix is not more effort. It's reallocation…"
Manim: `Reallocate` — 8 identical hour-blocks migrate terracotta column → blue column. Conservation rule: same count before and after.

## B11 — CARD (endcard) · own · ~8.0s
Cue: "The counter will keep offering you its number…"
Copy: **Spend effort where the return is — not where the feedback is.** / sub: *from The Reallocation Engine — chapter 2*

---

## Slot inventory (fill later, any order; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | overhead desk still | t2i prompt above (ai — disclosure) |
| `media/B04.png` → `media/B04.mp4` | shredder still → clip | t2i + i2v prompts above (ai — disclosure) |

Everything else is CARD / DOCUMENT / GRAPHIC — no media generation needed for the slate cut.
