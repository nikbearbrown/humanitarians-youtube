# SOURCES — humanitarians-ai-week2-typography-hero-concepting

Every on-screen number in this reel is listed here with how it was obtained.
Nothing in this video is an estimate presented as a measurement.

## Primary source

**https://humanitarians.ai** — homepage, inspected live on 2026-09-04 in a
browser at an emulated 1503×812 viewport (chosen to match the exact pixel
dimensions of the Week 1 screenshots, so figures are directly comparable).

Two independent measurement channels were used:

1. **Live DOM** — JavaScript run in the page: `getComputedStyle` for every
   text-bearing element, `getBoundingClientRect` for geometry, canvas
   `measureText` for character widths, and a walk of `<header>` / `<footer>`
   for link inventories.
2. **Screenshot pixels** — PIL + numpy + `scipy.ndimage` against the Week 1
   assets: connected-component labelling on a maroon mask
   (`r>85 & r<190 & g<75 & b<75 & r>g*1.8`) for the buttons, a brightness
   threshold (`gray<60`) for the video block, and ink-column profiling
   (`gray<150`, summed down the column axis) for the footer columns.

Where both channels measured the same thing they agree: the hero media-to-
message area ratio comes out 1.91× from the DOM and 2.10× from the pixels
(the DOM measures the `<iframe>` element, the pixels measure the rendered
dark block including its player chrome). **The reel quotes 2.10×**, the
pixel figure, because the pixels are what the viewer sees on screen.

## Claim-by-claim

| Beat | On-screen claim | Source | Value |
|---|---|---|---|
| B03 | 7 nav destinations; 4 section links + 2 buttons | DOM `<header>` anchor walk | logo, AI+1, Fellows, Projects, Videos, Youtube, Donate (+ theme toggle, not a destination) |
| B03 | "No About. No Contact." | DOM: neither string appears in the header | absent from nav; present in hero + footer only |
| B04 | Orientation missing / promotion duplicated | DOM: YouTube appears 4× and Donate 3× page-wide | counted |
| B05 | 6 columns, 33 links, 39 anchors | DOM `<footer>` walk | Company 5, Programs 3, Platform 4, Resources 6, Projects 11, Legal 4 = 33; +logo +5 inline = 39 |
| B06 | Projects column = 11 links | DOM | All Projects, AI Skunkworks, 80 Days to Stay, Dewey, Irreducibly Human, Lyrical Literacy, Madison, Medhavy, Musinique, Mycroft, Popper |
| B06 | 6 bare proper nouns | DOM, judgement applied to the list above | Dewey, Madison, Medhavy, Musinique, Mycroft, Popper |
| B07 | "All Projects" and "Musinique" each listed twice | DOM | All Projects: Company + Projects. Musinique: Resources + Projects |
| B08 | 19 distinct text styles | DOM: unique (tag, size, weight, family, transform, tracking) tuples over visible text | 19 |
| B08 | 8 font sizes | DOM | 60, 48, 36, 24, 20, 18, 16, 14 px |
| B08 | 1 type family | DOM `fontFamily` | Inter throughout |
| B08 | bold at 6 of 8 sizes | DOM: weight 700 observed at 60, 48, 36, 24, 20, 18 px | 6 |
| B10 | 84 characters per line | canvas `measureText` ÷ element width, longest body paragraph | 84 (a second long paragraph measures 78; card body 70–74) |
| B10 | 45–75 comfortable | typographic convention, not a site measurement | stated as the target band |
| B11 | #7D7D7D measures 4.12:1 | WCAG 2.x relative-luminance formula, computed | 4.12:1 — below the 4.5:1 AA threshold for normal text |
| B11 | 64 elements, 52 at body size | DOM: leaf elements with `color: rgb(125,125,125)` | 64 total; by size 16px×52, 14px×9, 20px×2, 18px×1 |
| B11 | #767676 measures 4.54:1 | computed; #767676 is the lightest neutral grey that clears 4.5:1 on white | 4.54:1 |
| B12 | 4 maroon buttons above the fold, same fill, same height | pixel components + DOM | all `rgb(122,0,0)`, all 40 px tall, all within the first 812 px |
| B13 | video = 2.10× the message area | pixel measurement | 840×471 = 395,640 px² vs 390×484 = 188,760 px² |
| B13 | message = 26% of the frame | pixel measurement | 390 / 1503 = 25.9% |

## Note on the accent colour

The live site's CSS accent measures **rgb(122, 0, 0) = #7A0000** (11.49:1 on
white). Week 1's palette used **#64140E**, sampled from JPEG-compressed
screenshot pixels of the Donate button face. #64140E is therefore slightly off
the true token — but it is the colour already published in Week 1, and the
brief locks one visual system across all four videos, so the series keeps
#64140E. The true value is recorded here so a future design hand-off uses the
right number.

## Not verifiable from public sources

The following come from the project's own internal record and cannot be
confirmed against the site — they are the presenter's own account of her work
and are carried on her authority:

- that Week 2's work order was scope reassessment → typography → hero → nav → footer
- that the hero concepts described in B14 are the ones actually explored
- that the four-step scale in B09 is the proposal on the table

These are marked in FACTCHECK.md and need her sign-off before publication.
