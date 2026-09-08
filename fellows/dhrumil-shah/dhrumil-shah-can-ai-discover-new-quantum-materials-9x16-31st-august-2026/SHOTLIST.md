# SHOTLIST — 9:16 vertical cut

Every shot is generated in-composition on a 2160 × 3840 canvas. There is no
camera, no stock footage, no AI-generated clip, and no captured screenshot.

The usable content column is **1920 px** (2160 minus a 120 px margin each
side). Every layout below is designed against that number.

| # | Time | Shot | Motion | Portrait legibility contract |
|---|---|---|---|---|
| 01 | 00:00 | Title, accent answer card, five-token **vertical** pipeline | staggered spring reveal, down-arrow connectors | Each token is full safe-width, so no title is compressed; the final token is accent |
| 02a | 00:12 | Headline, Tc definition card, 860 px measured Tc scatter | chart points reveal progressively | High-pressure values live in a callout; `YBCO 92K` is left-anchored clear of the BSCCO point |
| 02b | 00:26 | Five CLAIM cards in a **3 + 2 grid** | staggered, 14-frame offsets | 624 px columns; I and M accent from first appearance and sit together on the second row |
| 03a | 00:35 | Full bibliographic citation, full width | spring reveal | Author, year, title, journal, volume, pages all on screen |
| 03b | 00:35 | 2 × 2 stat grid beneath the citation | staggered | 948 px cells; the zero-structure-inputs stat is accent |
| 03c | 00:48 | Feature chips card, then NOT-IN-THE-TABLE card, **stacked** | chips stagger, exclusions reflow as a wrapping row | The exclusion card is accent — it is the point of the scene |
| 04a | 01:00 | ±9.5 K at 200 px, full width | spring reveal | The metric appears with its model and split, never bare |
| 04b | 01:00 | Three supporting cards **stacked** beneath | staggered | Each is full width; no card is narrowed to fit a second column |
| 04c | 01:10 | Interpolation reframe card | fade and rise | Accent, full width, one sentence |
| 05a | 01:15 | Five funnel rows: label column + proportional block | staggered, 26-frame offsets | Label is never inside a bar, so it cannot overflow one; note sits beneath the label |
| 05b | 01:28 | ILLUSTRATIVE SCHEMATIC disclosure | fade and rise | Accent card, held to end of scene |
| 06 | 01:34 | Inside/outside distribution **stacked**, then two dated cards **stacked** | staggered | Outside card is accent; both dates on screen |
| 07a | 01:51 | Five-link confirmation chain, **vertical** with down-arrows | staggered with connectors | Only the first link is accent — the link AI touches |
| 07b | 02:04 | Boundary labels above and below a full-width rule, then the Meissner rule card | fade and rise | States that zero resistance alone is insufficient |
| 08 | 02:10 | **LK-99 stacked**: claimed above (02:10), replication below (02:22) | both held to 02:33 | **Both panels on screen together for 11.2 s** — the axis rotated, the simultaneity did not |
| 09 | 02:33 | CLAIM rubric scored, five rows | staggered rows | Justification moved beneath each axis name so verdict chips keep full width |
| 10a | 02:46 | Five-row viewer scaffold and decision rule | staggered rows | Prompt beneath each axis name; I and M markers accent |
| 10b | 02:57 | Title close and disclaimer, centred | cross-fade | Disclaimer is a held card, not a flash |

## Persistent elements

- Presenter name upper-left at 80 px; film title beneath it at 120 px in
  ghost weight; scene number `NN / 10` upper-right.
- Scene label under the header, monospace, letterspaced.
- A `SOURCE` plate spanning the **full safe width** at the bottom of every
  scene, at 27 px with a 1.32 line-height so long citations wrap to two lines
  rather than clipping. This is the main source-tag difference from the 16:9
  cut, where the plate is a single line at 36 px.

## Safe area

`{left: 120, right: 120, top: 170, bottom: 170}`. No element is clipped or
placed outside this box in any frame sampled in `_qc/final/`.
