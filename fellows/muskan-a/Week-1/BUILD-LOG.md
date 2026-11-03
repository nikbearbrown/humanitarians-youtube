# BUILD-LOG — humanitarians-ai-week1-diagnostic-audit

## 2026-08-31 — authored (Claude, built against the brutalist.art-main toolkit)

- HUMAN NOTE (logged first): Muskan Agrawal supplied a full video brief
  ("Week 1 Video Brief: Diagnostic Audit and Typography Foundations") with
  a 7-scene script, 6 screenshots, a visual-direction note (brutalist: black
  type on white ground, one maroon accent, hard crops, hard cuts, sub-bass
  hits instead of music, no gradients/shadows/rounded corners), and a
  review checklist (4K source + 4K post-upload, both 16:9 and 9:16, an
  intro line in a fixed format, a real viewer takeaway).
- ADDITIONAL INSTRUCTION: prepend a 2-line presenter intro — "Hi, I am
  Muskan Agrawal, and this video is [a summary of the topic]" — before the
  brief's own Scene 1. Added as B00; wrote original 2-sentence copy rather
  than reusing Scene 1's opening line verbatim, since that line ("Before
  touching a single pixel...") is the brief's actual Scene 1 script and
  reusing it in the intro would have doubled it.

## KEY DECISION — why this reel is 100% Manim, not Remotion/pantry

The toolkit ships three named builder skills (ai-explainer, cli-explainer,
deep-explainer), each of which assumes Claude-branded bookend components
(ClaudeComposerAsk, ClaudeVerdictArtifact, etc.) that don't fit a
project-status video with no "ask Claude" framing. More importantly: the
brief's red-box/arrow/circle annotations over real screenshots map to what
this toolkit calls the Remotion "annotation plane" — and
`skills/make/explainer/REMOTION.md`, as shipped in this checkout, opens
with: **"spec (v1, not yet built)."** I confirmed this by checking
`runtime/remotion/src/scenes/` for the track components the spec describes
(Highlight.tsx, Ring.tsx, Push.tsx, etc.) — none exist.

Rather than write a beat_sheet.json against a feature that won't actually
render, I used the toolkit's own documented fallback: `run.sh` itself says,
verbatim, "Write REEL_DIR/scenes.py (one Scene per GRAPHIC/CARD/DOCUMENT
beat)" when a reel needs custom visuals it can't already find in the
library. So:
- All 14 beats are `shot.type: GRAPHIC`, `engine: manim`, each pointing at
  a real Scene class in `scenes.py`.
- Manim's `ImageMobject` displays the real screenshots full-frame; Manim's
  `Rectangle`/`Ellipse`/`Arrow` draw the red annotations directly on top —
  full creative control, zero dependency on an unbuilt Remotion plane.
- This also sidesteps the `pantry.py`/STILL Ken-Burns pathway entirely
  (screenshots live in `assets/`, loaded directly by `scenes.py`, not in
  `pantry/`) — there was no reason to route through two systems when one
  does the whole job reliably.
- `run.sh` renders Manim scenes natively at 3840×2160, 24fps
  (`manim -qk --fps 24 -r 3840,2160`) — confirmed by reading the script
  directly — so no manual 4K configuration was needed in scenes.py.

## Palette — measured, not guessed

The brief says "stick to the site's own palette." Rather than approximate a
generic "brutalist maroon," I sampled the actual accent color from
`01_hero_section.jpg`'s Donate/YouTube buttons using PIL:

```python
from PIL import Image
im = Image.open('01_hero_section.jpg').convert('RGB')
# sampled 3 points across the Donate button face
# → (96,18,11), (101,19,11), (108,23,18) → averaged to #64140E
```

Used `#64140E` (MAROON), `#FFFFFF` (PAPER), `#111111` (INK, near-black —
the site's body text isn't pure #000) throughout `scenes.py`, replacing the
toolkit's default "claude" cream/terracotta preset entirely.

## Annotation coordinates — measured, not eyeballed

For B03 (red box on About Us / Contact Us, arrow at Donate) and B09 (red
circle on the video embed), I located the actual UI elements
programmatically rather than guessing pixel positions:

```python
import numpy as np
from PIL import Image
im = Image.open('01_hero_section.jpg').convert('RGB')
arr = np.array(im)
target = np.array([100, 20, 14])                    # the measured maroon
mask = np.linalg.norm(arr.astype(int) - target, axis=2) < 40
ys, xs = np.where(mask)                              # then bbox per region
```

This found: About Us/Contact Us at normalized x∈[0.073,0.261]
y∈[0.762,0.812]; the Donate button at x∈[0.811,0.888] y∈[0.016,0.065].
For the video embed (B09), used a brightness threshold (`gray < 60`) since
the embed is a large near-black block, not a maroon one: x∈[0.300,0.927]
y∈[0.219,0.799]. All four numbers are recorded in SHOTLIST.md next to the
beat that uses them, so they can be re-measured or adjusted independently
of the code.

**One exception:** B06's footer crop (the Projects column) was estimated
from the column's visual ORDER, not color/brightness-thresholded, since
there's no distinguishing color to detect. Flagged in SHOTLIST.md as the
one crop to double-check on the first local previz.

## Runtime check against the brief's 3–4 minute target

Summed each beat's narration word count ÷ 2.3 words/sec (≈138 wpm, Kokoro's
approximate reading pace) + 1.2s settle time per beat → 223.5s = 3:43.5.
Within the brief's stated 3–4 minute runtime target. Real duration will be
whatever Kokoro's actual synthesis measures — these are planning estimates,
not the master clock (the audio is, per the toolkit's own audio-first
design).

## Two screenshots not used in this cut

`04_irreducibly_human.jpg` and `05_mission_cta_spotify.jpg` were the
brief's own stated "reserve" material for B-roll / extra runtime. The
script's 14 beats already land at 3:44 without them, so they weren't
needed. They're still copied into `assets/` in case a future edit wants
them (e.g. if the real Kokoro audio runs shorter than estimated and the
piece needs another beat to hit 3 minutes).

## What's NOT done yet (needs you, not more scripting)

- **Sign FACTCHECK.md.** Two rows describe your project's internal
  history (original brief = full rebuild; the pivot) that no screenshot
  can confirm — only your own project records can. Three checkboxes are
  open there.
- **Render locally.** I have no Manim/Kokoro/ffmpeg in this sandbox (by
  design — you confirmed everything's installed on your machine). See the
  chat response for the exact commands.
- **qc-sequence.png** — genuinely can't be produced without a real render;
  `compile.py` builds it from actual rendered mid-frames.
- **Double-check B06's footer crop** on the first previz (see SHOTLIST.md).

## Gate status
- [ ] GATE F (FACTCHECK.md) — DRAFT, not yet signed (3 open items, listed above)
- [x] GATE — palette/coordinates verified by direct pixel measurement (this log)
- [ ] GATE A / GATE W (static + WCAG/margin pre-flight) — untested; these run
      automatically inside `./art run` on your machine (Manim isn't
      installed in the sandbox that built this)
- [ ] Local render, 4K master, 9:16 short — not yet run (needs your machine)
