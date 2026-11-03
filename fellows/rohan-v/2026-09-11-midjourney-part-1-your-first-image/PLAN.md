# MIDJOURNEY PART 1 — "Your First Image"

**SHIPPED. Runtime 3:24, 3840x2160, 11 beats.** Suno ran 3:57 / 3:09 / 3:29.

Gate L clean - Gate V 0 BLOCKER, 2 MAJOR (the `BOUT` end-card underfill that
all three shipped Suno parts also carry). `check_beats.py` 0 blockers,
0 warnings. Every beat verified 4K and frame-accurate against its own audio.

Every element is in `MIDJOURNEY-UI-SPEC.md`, built by reading all 23 captures
first-hand.

### What visual QC caught that the automated gates did not

Gate V passed every one of these frames. They were found by pulling 4K stills
and crops and looking at them.

| Defect | Beat |
|---|---|
| Hover buttons clipped to "ry Subtle" / "Anima" | B07 |
| Nav labels truncated - in the beat about those labels | B03 |
| An empty bordered card held for 14.5s of a 23s beat | B02 |
| Blurred state indistinguishable from sharp (twice) | B05 |
| Tile read `48% Complete` beside a card reading `15% Complete` | B05 |
| Body text rendering BELOW its own card border | B06 |
| Four cards at 436px holding ~120px of content | B04 |
| One card at 356px holding ~90px of content | B02 |
| A **gear** where the product shows a **sliders** icon | B04 |
| An emoji rendering as a missing-character box at 46px | B04 |

Gate V did catch one thing the eye missed: `edge-bleed` on B03, introduced by
the fix for the truncated labels. Narrowing the rail made the copy rewrap and
the card stack grew past title-safe. The two kinds of checking are complements,
not substitutes.

### Four typed-coordinate bugs, one root cause

Every one was a literal offset that outlived the layout it described - the same
failure as the Suno rail resolving to x=1865. All four are now derived, so the
defect is unrepresentable rather than merely absent:

- `MjRingBox` (new, in the kit) - a ring drawn from its element's own box
- B06's landing line - centred in the gap between window and cards
- B03's section title - built from `MJ_NAV_COUNTS`, not typed
- B04's locator ring - `MjRingBox` instead of `w={0.72 * (CONTENT.w - 176)}`

---

## What this part owes the viewer

A volunteer who has never opened Midjourney should finish this video able to sign
in, find their way around, type a prompt, and understand what comes back. Nothing
more. **No settings, no references, no editing** — those are Parts 2 to 5.

The through-line is **the loop**: one box, four images, pick one. Everything else
in the product is a way of steering that loop, and saying so early stops the tool
feeling like a wall of controls.

---

## Beat table

| Beat | Act | Scene | Est. |
|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | 16s |
| B01 | BLUF — the loop is the whole tool | `MjL1Loop` | 18s |
| B02 | Access — Discord, and the shared account | `MjL1Access` | 17s |
| B03 | The sidebar — eight items, three groups | `MjL1Nav` | 18s |
| B04 | The imagine bar and the header cluster | `MjL1Bar` | 19s |
| B05 | Submit — the three progress states | `MjL1Progress` | 18s |
| B06 | The row of four, and the rail beside it | `MjL1Row` | 19s |
| B07 | Hover — Vary Subtle, Vary Strong, Animate | `MjL1Hover` | 18s |
| BVDT | Verdict — the loop on one card | `ClaudeVerdictArtifact` | 18s |
| BHTF | Recap and the Part 2 tease | `ClaudeComposerAsk` | 17s |
| BOUT | Outro | `ClaudeTitleOutro` | 3s |

**Estimated ~3:01.** Actual comes from Kokoro at audio lock.

Six body beats (B02–B07) plus a BLUF — the design point in
`MIDJOURNEY-SERIES-PLAN.md`.

---

## Scene briefs

**`MjL1Loop`** — no app window. Three cards left to right: a box with a typed
line, four tiles, one tile chosen. The shape of the loop before any chrome. The
one beat in the part that is a diagram rather than a mockup.

**`MjL1Access`** — a Claude-style two-step card (Discord, then midjourney.com),
plus the account chip lifted from the sidebar showing `humanitarians…`.
**Deliberately NOT a recreated sign-in page** — there is no capture of one, and
`VIDEO-PIPELINE.md` section 8 forbids depicting an uncaptured screen.

**`MjL1Nav`** — `MjWindow` with the sidebar carrying the emphasis: four top-level
items, then AESTHETICS with three, then COMMUNITY with one. The rail groups them
and marks which part of the series owns each.

**`MjL1Bar`** — the imagine bar rendered large, with its four affordances ringed
in turn: add-image, the text field, the sliders icon, and the header cluster
(`P`, bolt, search). The search placeholder changes per page — shown, not laboured.

**`MjL1Progress`** — the three states in sequence on the real feed: four grey
tiles badged `Starting…`, then blurred colour badged `15% Complete`, then four
sharp images. Timed to the narration so the states land on the words.

**`MjL1Row`** — the finished row with its right rail: full prompt, reference
thumbnails, and the `stylize 150` / `weird 4` chips. The teaching point is that
every row carries its own recipe.

**`MjL1Hover`** — one tile in hover state: trash top-left, heart top-right,
`Vary Subtle` · `Vary Strong` · `Animate` along the bottom. Three buttons, and
Upscale is deliberately absent — it is not on the hover row.

**Kicker:** every `MjL1*` scene passes
`kicker="LYRICAL LITERACY · MIDJOURNEY TUTORIAL PART 1"`.

---

## The new kit — `midjourneyKit.tsx`

Suno's kit is a dark-product kit. Midjourney is light, so the window is new:

- **`MJ` tokens** — near-white page, white cards, warm hairline borders,
  red-orange accent.
- **`MjWindow`** — sidebar with the two small-caps section labels, the imagine
  bar, the header cluster. Children render in a local coordinate space.
- **`MjTile`** — a feed tile in one of four states: `empty` · `starting` ·
  `blurred` · `done`, with an optional hover overlay.
- **`MjChip`** — the pale grey parameter pill.
- **`MjSeg`** — the segmented control, accent-on-tint when active.

`MjActionRail` (Part 2) and `MjSettingsCards` (Part 3) get built later against
the same spec, so the product cannot drift between parts.

### The Gate V trap, inverted

Suno's problem was dark surfaces at partial alpha turning to grey slabs. **The
Midjourney problem is the opposite: a near-white window on the cream page is
invisible to Gate V**, which counts ink at `INK_DELTA = 28` per channel — and
`#FAF9F5` against a white card is nowhere near that.

So `MjWindow` carries a **2.5px near-black border**, its sidebar sits on a
distinctly darker tint than the page, and every card inside gets a border darker
than `#DDD`. The generated-image tiles are mid-grey to dark and count heavily on
their own, which is why the image-heavy beats are safe; B03 and B04 are the two
that needed the border decision.

Annotation stays on the cream rail via `splitStage()`. **Nothing is drawn over
the window from outside it** — the Suno "red datum line" defect.

---

## Narration rules applied

- Host opens "Hi, I'm Rohaan from Humanitarians AI"; full name spoken **once**,
  in BOUT, as `Rohaan`.
- **The video count is never stated.** "This series", never "the first of five".
- Access stated **once**, mechanically. No pricing, no plan names, no selling.
- **No version number** anywhere. The `Help us improve V8` row is omitted from
  every mockup; the settings panel is not in this part at all.
- Heteronyms avoided in draft: `separate` (rewritten to "independent"), `use`
  as a bare noun, `live`, `read`, `close`, `record`, `present`, `content`.

---

## What this part deliberately does NOT claim

- That the four images are four tries. They are **one job, four results**.
- That `Upscale` is on the hover row. It is **not** — only Vary Subtle, Vary
  Strong and Animate are.
- Anything about the sign-in screen's layout.
- Any number attached to the Aesthetics sliders. The panel shows no readouts;
  the `stylize 150` / `weird 4` chips are shown as *that job's record*, not as a
  recommendation.
