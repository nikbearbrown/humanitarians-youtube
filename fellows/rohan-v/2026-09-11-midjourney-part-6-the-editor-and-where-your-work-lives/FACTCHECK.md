# MIDJOURNEY PART 6 — fact check

The series finale. Every claim, on screen or in the voice, with its source.

Sources, all read first-hand: `Edit tab.png` (empty state) · `Editor.png`
(Paint, mid-erase) · `editor 2.png` (Move / Resize) · `editor 3.png`
(Smart Select) · `editor 4.png` (Submitting) · `Organize tab.png`.
Recorded element-by-element in `../MIDJOURNEY-UI-SPEC.md` §9 and §10.

**Nothing in this video comes from web research.** The Editor is pure UI; there
is no craft claim to source from documentation.

---

## 1. Claims and sources

### B02 — getting in, and the column

| Claim | Source |
|---|---|
| The sidebar collapses to an icon rail in the Editor | All four editor captures |
| An empty canvas offers `Edit from URL` and `Edit Uploaded Image` | `Edit tab.png`, product labels and the only gradients in the product |
| `Open Editor` is the third route | Part 3's rail (`Image opened.png`) |
| Four tools, then a Layers panel | All four captures. **Layers is not a fifth tool** — it never expands and never takes the accent |
| `Submit Edit` is disabled on an empty canvas | `Edit tab.png` (grey) vs `Editor.png` (dark) |

### B03 — Move / Resize

| Claim | Source |
|---|---|
| `Image Scale`, at 100% | `editor 2.png` — handle at far right |
| `Aspect Ratio`, reading `1 : 1` | Same |
| A grid of presets with `1:1` active and spanning two rows | Same |
| Hovering a preset shows "Set aspect ratio to 1:2" | Same — the tooltip is in the capture |
| The canvas gains square corner handles in this mode | Same |

**"The empty edge is the hole"** is our framing, not a product string. It
follows from what the capture shows — scaling down or reshaping leaves space —
but the *inference* is ours and the narration owns it as such.

### B04 — Paint

| Claim | Source |
|---|---|
| `Erase` and `Restore`, Erase active | `Editor.png` |
| `Brush Size`, `100px`, on a slider | Same |
| **Erasing produces transparency, not paint** | Same — the erased region renders as the transparent checkerboard, on the canvas *and* in the `Layer 1` thumbnail |

That last row is the most important fact in the part, and it is directly
visible rather than inferred.

### B05 — Smart Select

| Claim | Source |
|---|---|
| `Include` and `Exclude`, Include active | `editor 3.png` |
| Clicking drops a small accent `+` marker | Same |
| `Erase Selection` and `Erase Background` | Same |
| Both stay disabled until a selection resolves | Same — they are only ever captured greyed |

### B06 — Submit Edit

| Claim | Source |
|---|---|
| The prompt bar holds a long auto-generated description | `editor 4.png` |
| It describes the whole picture, hole included | Same — the text describes the full composition |
| It ends `--stylize 150 --weird 4` | Same, verbatim |
| A `Submitting…` badge appears on the canvas | Same |
| An edit returns **four** results | Same — four grey placeholders with spinners appear in the filmstrip |
| The tool column and `Download Image` grey out during submit | Same |

**The parameter callback is the strongest cross-reference in the series.**
`--stylize 150 --weird 4` is the same pair of numbers as the `stylize 150` /
`weird 4` chips on the Create rail (Part 1) and the Stylization and Weirdness
dials in the settings panel (Part 4). One job, three surfaces, all captured.
Spoken as **"stylize one fifty, weird four"** because Kokoro mis-reads bare
digits.

### B07 — Organize

| Claim | Source |
|---|---|
| Search placeholder is `Search Prompts` | `Organize tab.png` |
| A dense grid, no right rail, no prompts | Same |
| Grouped by day, with `Today ⊕` / `Yesterday ⊕` | Same |
| The `Filters` panel has **six** groups | Same, counted one per line |
| The first group has no heading | Same |
| `Spotlighted` is one of its options | Same — corroborates `Spotlight Image` in Part 3's options menu |
| `Download Image` from the options menu, or `Export Edit` in the Editor | `options.png` and `Editor.png` |

`MJ_FILTERS.length` is the only place the six lives. `check_beats.py` reads it
out of the scene file and fails the build if the narration disagrees.

---

## 2. Deliberately NOT claimed

| Not claimed | Why |
|---|---|
| What the `sparkle` icon in the `Edit` card does | Its glyph is captured; its function is not. |
| A second layer, or what `+ Add` produces | Only `Layer 1` is ever captured. |
| `Restore` in action | Captured as a button, never as an effect. |
| A **resolved** Smart Select selection | Both Erase buttons are only ever seen disabled. The narration says they wait for a selection — which is what the capture shows — and stops there. |
| The **finished** four results of an edit | The capture stops at `Submitting…`. The video stops there too. |
| Any model version number | Organize's `Version` filter lists them. The group keeps its heading and a muted *"by model"* note; values omitted. Same call as Part 4's `8.2` dropdown and Part 5's `V8 Profiles`. |
| Any price, plan or credit figure | Register rule. |
| A Part 7 | This is the finale. `check_beats.py` fails on any forward tease. |

All eight are enforced by script, not by memory.

---

## 3. Deliberate visual simplifications

| Product | Ours | Why |
|---|---|---|
| The loaded image is a real illustration | A seeded abstract field | REBUILD LAW: no screenshot is composited into any frame. |
| The canvas fills most of its area | Centred, 16:9, with margin | The captures are a 16:9 poster in a taller canvas; keeping the margin is honest to that. |
| The Organize grid is very dense | Five across, rows derived from height | Legibility at 4K. The narration never states a tile count. |

---

## 4. Register compliance

| Rule | Status |
|---|---|
| B00 opens "Hi, I'm Rohaan from Humanitarians AI" | checked by script |
| Full name spoken exactly once, in BOUT | 1 occurrence, checked |
| BHTF closes the series and teases nothing | checked |
| No pricing, no promotion, no series count | checked |
| Every `MjL6*` scene carries the Part 6 kicker | checked |
| No cue resolves past 0.85 of its beat | checked |

**`check_beats.py`: 0 blockers, 0 warnings.**

### Fixes made before audio lock

| Was | Now | Why |
|---|---|---|
| "four **separate** tools" (B01) | "four **different** tools" | adjective /ˈsɛpərət/ vs verb /ˈsɛpəreɪt/ |
| B06's `third` cue at 0.892 | re-anchored to "Hit Submit Edit", now 0.833 | the card had 2.3s to be read |

Rewording B01 **orphaned its cue anchor** — `cues.json` still pointed at "four
separate tools". `sync_cues.py` printed `NOT FOUND` and the anchor was updated.
This is the failure mode `VIDEO-PIPELINE.md` §2 warns about, caught by the tool
built for it.

### A bug in this part's own checker

The first run reported **7 filter groups against a 6-entry array**. Cause was
`kit.count("{heading:")` also matching the `FilterGroup` *type declaration*.
The measurement was fixed rather than the threshold loosened — a checker that
is wrong about a count is worse than no checker, because it teaches you to
ignore it.

---

## 5. Outstanding — needs your ears

1. **`Rohaan`** in BOUT.
2. **"stylize one fifty, weird four"** in B06 — spelled as words on purpose;
   worth confirming it lands as intended.
3. **`Move slash Resize`** in B03 — the product writes `Move / Resize` and the
   narration says "slash" out loud. It is the honest reading of the label, but
   it may sound stilted.
