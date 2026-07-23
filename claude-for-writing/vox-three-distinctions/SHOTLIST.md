# SHOTLIST — vox-three-distinctions
**Three Questions That Catch Broken Causal Arguments**
Writing Guide · Chapter 13 (cause-and-effect distinctions only)

---

## Header checks

### Shot-type histogram

| Type | Beats | % |
|---|---|---|
| CARD | B01, B03, B05, B07, B09, B11, B17, B18 | 8 (44%) |
| GRAPHIC | B04, B06, B08, B10, B13, B14, B15, B16 | 8 (44%) |
| STILL | B02, B12 | 2 (11%) |

No type exceeds 44%. No more than 2 consecutive same-type beats:
- B07 (CARD) → B08 (GRAPHIC) → B09 (CARD) → B10 (GRAPHIC) → B11 (CARD) — alternating, fine.
- B17 (CARD) → B18 (CARD) — 2 consecutive CARD, at act boundary (PRACTICE → RECAP), acceptable.

### Rhythm check: ✓ PASS

### Act map

| Beat | Act |
|---|---|
| B01–B02 | COLD OPEN |
| B03 | THE QUESTION |
| B04–B05 | THE PROBLEM |
| B06–B11 | THE MECHANISM (3 distinction pairs) |
| B12–B13 | THE IMPLICATION |
| B14–B15 | THE EXAMPLE (16:9 only) |
| B16–B17 | THE PRACTICE |
| B18 | RECAP |

### Color law
CRIMSON = the collapsed/wrong reading (bad reasoning — the mistake)
TEAL = the correct distinction / diagnostic pass (good reasoning — the fix)
GOLD = highlighter fill only, once per graphic, never text
SLATE = structural scaffolding (chain nodes, neutral containers)
Never swap mid-film.

### Exclusion confirmations
- NO Toulmin model: confirmed absent from all beats and narration
- NO analogy strategy: confirmed absent
- NO classification/comparison/problem-solution/definition: confirmed absent
- ONLY causal reasoning: confirmed — 3 distinctions only

### Estimated runtime
18 beats × avg 11.2s ≈ ~201s ≈ 3:21 — within the 3–5 min band. ✓

### Media economy
2 STILL beats across ~3:21 = 1 per 101s ≈ roughly 1 per 90s. ✓

---

## Per-slot sections (fill-in beats only)

---

### B02 — STILL · ai — the newspaper / phone-ban story

**Beat:** B02 · COLD OPEN · kenburns · focus [0.5, 0.4]

**What the beat needs:** a newspaper front page, desaturated editorial treatment, with a headline style that reads like a correlation-as-cause story about phones and teen outcomes. Evokes the "public discourse" framing of the cold open.

**Archive search links:**
- Wikimedia: [https://commons.wikimedia.org/w/index.php?search=newspaper+front+page&title=Special:MediaSearch](https://commons.wikimedia.org/w/index.php?search=newspaper+front+page&title=Special:MediaSearch)
- The Guardian archive shots, CC licensed: broad broadsheet photography
- Note: real newspaper front pages showing phone-ban stories may exist via wire services but carry non-CC licenses — use a generative approach.

**Provenance notes:** generative (ai); requires sidecar stub at `media/B02.source.txt`.

```
B02, newspaper broadsheet front page with bold headline about smartphone phone ban and student test performance, printed newspaper format, black and white headline typography, editorial newsprint photography, desaturated flat treatment, slight angle on wooden desk, academic aesthetic, high contrast print, no people visible
```

---

### B12 — STILL · ai — corroded pipeline / Refugio implication beat

**Beat:** B12 · THE IMPLICATION · kenburns · focus [0.5, 0.5]

**What the beat needs:** a close-up of a corroded industrial pipeline section, evoking the Refugio oil spill context (aging infrastructure, regulatory failure). Editorial flat-print treatment.

**Archive search links:**
- Wikimedia Commons – Refugio oil spill: [https://commons.wikimedia.org/w/index.php?search=refugio+oil+spill&title=Special:MediaSearch&type=image](https://commons.wikimedia.org/w/index.php?search=refugio+oil+spill&title=Special:MediaSearch&type=image)
- NOAA OR&R (Office of Response and Restoration) archives: public domain government photos
- USFWS Flickr (CC): search "oil spill pipeline" — may include Refugio or comparable spills
- Provenance note: if a real Refugio archival photo is found with CC/PD license, prefer that over ai — mark source as `archive` and fill `media/B12.source.txt` with URL + license.

**If no suitable archive found — generative prompt:**
```
B12, close-up photograph of a corroded steel industrial oil pipeline section, visible rust and surface corrosion, outdoor setting near coastal terrain, slightly overcast light, desaturated editorial newsprint treatment, flat print reproduction, no text, no people, no branding, industrial infrastructure detail
```

---

## Non-fill beats (own-Manim, no slot to fill)

B01, B03, B04, B05, B06, B07, B08, B09, B10, B11, B13, B14, B15, B16, B17, B18 — all rendered by `vox_scenes.py`. No media intake needed.
