# SOURCES — Ground Truth First

Weekly progress reel · loon detector · week of 2026-08-28.

## External links

| Source | How it is used | Verified |
|---|---|---|
| — | This reel cites no external source. | n/a |

Nothing external is quoted, linked or shown. Every claim in this reel is a
first-person report of the author's own week, supplied by the author on
2026-08-28, plus one photograph he took and annotated himself.

## On-screen assets

| Asset | Origin | Note |
|---|---|---|
| `images/B03-source.png` | Author's own annotation screenshot, `Screenshot 2026-08-28 at 00.34.19.png`, 2354x1320 | Two loons on open water with two hand-drawn bounding boxes. Staged into the reel per rule 4 (videos travel with their book). |
| `media/B03.png` | Composed from the above by `make_plates.py` | 3840x2160, full uncropped frame matted on the deck ground. |
| `pantry/B03-916.png` | Composed from the above by `make_plates.py` | 2160x3840, a 1180px-wide crop centred on the boxes — deliberately NOT `shorts.py`'s centre cut. |

## Honesty log

**The only figure in this reel is 10%, and it is project-wide.** The author's
raw words were "I am currently at 10% of the total repo," which is ambiguous —
it could have meant 10% of the images annotated, 10% of the footage processed,
or 10% of the overall project. He was asked directly and answered: **the whole
project**. So B04 and B05 say "about ten percent of the project" and nothing
else. The reel never says ten percent of the images, of the footage, or of the
annotation.

**No architecture is named.** The author said he is writing a guideline document
on "the architecture of the loon detection model" by "gathering the latest
research and best practices" — he did not say which architectures it surveys or
which one he is leaning toward. So B02 is built around the *act* of choosing and
recording it, and names no model, backbone, framework or paper. Putting a
plausible-sounding name on screen here would have been the easiest and worst
invention available. **If you want a named architecture on screen, supply it and
B02 gets rebuilt.**

**"Two instances boxed by hand" is a count of one frame.** The B03 plate caption
and narration describe only what is visible in that single screenshot. It is not
a dataset total, and no dataset total is asserted anywhere in this reel — no
image counts, no class counts, no annotation counts, no accuracy or mAP.

**B04 is an argument, not a report.** The claim that a labelling standard is far
cheaper to fix at 10% than at 80% is editorial judgment the voice is making. The
author did not describe making that decision. It is framed throughout as
reasoning ("that's exactly the moment that matters"), never as a completed
action, and the verdict card does not list it among the week's deliverables.

**"Three repositories."** The author said both footage repos and the git coding
repo are initialized. The reel counts that as three — two footage, one code. If
the two footage repos are in fact one repo with two remotes, or if there are
more than two, B00/B01/B05 need a correction before render.

## Not yet verified

- Nothing in this reel depends on an unverified external claim.
- The one item to re-check before signing GATE P is the repository count above.
