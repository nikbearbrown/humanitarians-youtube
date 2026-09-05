# FACTCHECK — `yatra-nobody-wrote-this` ("Nobody Wrote This.")

DOUBLE-CHECK LAW. Every figure that reaches the screen is listed here with the
citation it renders with. **No figure in this reel was computed, estimated,
rounded or derived by the build.** All seven data points were supplied verbatim
by the human (2026-09-01) and are rendered as STRINGS, never parsed into the
copy.

## The claim ledger

| # | Claim as narrated / rendered | Citation rendered on screen | Beat |
|---|---|---|---|
| 1 | 41% of long-form LinkedIn posts (250+ words) are fully AI-generated — the highest of any platform studied | Pangram Labs, "AI in Your Feed," July 2026 | B03, B11 |
| 2 | 1 in 4 long-form posts across five major social platforms are fully AI-generated | Pangram Labs, "AI in Your Feed," July 2026 | B05 (baseline marker) |
| 3 | LinkedIn was only about a third of the ~1 million posts scanned, but accounted for nearly 62% of all AI-generated content detected | Pangram Labs, "AI in Your Feed," July 2026 | B06 |
| 4 | Cross-platform: X/Twitter ~25–29%, Medium ~31%, Substack lowest at ~10%, Reddit as low as 4–13% | Pangram Labs, "AI in Your Feed," July 2026 | B05, B09 |
| 5 | Only 4.3% of LinkedIn posts were AI-assisted/mixed — the use is "all-or-nothing" | Pangram Labs / Tech Times | B07, B11 |
| 6 | LinkedIn ships an "Enhance Post" AI-writing tool while also trying to downrank AI-generated content | Pangram Labs, "AI in Your Feed," July 2026 | B08, B11 |
| 7 | The EU AI Act's Article 50 disclosure rules for AI-generated content took effect August 2, 2026 | Tech Times | B10 |

## What is NOT on screen (and why)

These are the invention risks this reel was most exposed to. Each was checked
and refused.

- **The human-written share of LinkedIn posts.** `100 − 41 − 4.3 = 54.7%` is
  arithmetically available and is **never shown**. The human supplied two of the
  three bins; the third is a derivation, and a derivation is an invention under
  the standing instruction ("don't invent any additional numbers beyond what I've
  given you"). `LnkAllOrNothing` renders the third band as an unlabelled
  remainder — the component has no prop that can carry a figure for it.
- **A total post count.** "~1 million posts scanned" is narrated and rendered
  with its stated tilde; it is never sharpened to a specific number.
- **Any engagement, reach, follower or revenue figure.** None was supplied, none
  appears, and no component in `NobodyWroteThis.tsx` accepts one.
- **Any claim about how the detector works internally.** The reel says detection
  is probabilistic (B09) because that is true of classifiers generally; it makes
  no claim about Pangram's accuracy rate, because no accuracy rate was supplied.

## Bar-length discipline (the one place a number is computed)

`LnkLadder` and `LnkDisproportion` draw bars. A bar has to have a length, so the
components take an **explicit `bar` number that is separate from the verbatim
`value` string**. The printed figure is always the human's string; the bar is
only a drawing instruction. The rule used, applied uniformly and recorded here:

| Platform | Rendered verbatim | `bar` | Rule |
|---|---|---|---|
| LinkedIn | `41%` | 41 | single figure → the figure |
| Medium | `~31%` | 31 | single figure → the figure |
| X / Twitter | `25–29%` | 27 | stated range → midpoint |
| Substack | `~10%` | 10 | single figure → the figure |
| Reddit | `4–13%` | 8.5 | stated range → midpoint |

The cross-platform baseline (claim 2) is drawn as a dashed reference line at 25
and labelled `1 in 4 — all five platforms`. The naive parse of `"4–13%"` by the
house `num()` helper used in the older stat components yields **413**, which
would have drawn a bar nine times the width of the track — that is precisely why
this reel does not reuse `SeoCompare` and carries its own ladder component.

For `LnkDisproportion` the two tracks are drawn at `bar: 33` ("about a third",
the human's own words, drawn at a third) and `bar: 62` (nearly 62%). Both print
their verbatim strings.

## Register corrections applied (the DOUBLE-CHECK rewrite)

- The source framing "AI slop is taking over social media" is **not** used. The
  finding is platform-specific and the reel says so: Substack ~10% and Reddit as
  low as 4% are in the same scan, and B09 makes that the falsifier.
- "AI-generated" is not softened to "AI-assisted" anywhere, and the two are kept
  structurally distinct (that distinction is the reel's thesis).
- No model names or version numbers appear — they date the video.
- The reputation argument in B10 is labelled **INTERPRETATION** on screen,
  visually separated from the dated regulatory fact beside it, because it is the
  narrator's judgment and not a sourced finding.

## Sourcing note

Both sources are as supplied by the human and are cited on screen exactly as
given. No independent verification of Pangram Labs' methodology was performed by
this build, and the reel makes no claim about it beyond what B09 states.
