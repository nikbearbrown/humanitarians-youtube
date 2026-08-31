# FACTCHECK — *Nobody Is Coming to Approve It.*

Ep. 06 · AI in Astronomy & Space Science · checked 2026-08-28 against the
sources listed in `SOURCES.md`. Every number that reaches the screen or the
narration is in this table.

| # | Claim (beat) | Verdict | Source | Note |
|---|---|---|---|---|
| 1 | One-way light time Mars↔Earth is 3–22 minutes (B00, B03, B11) | **VERIFIED** | ESA Mars Express; standard range from ~4 light-min at closest approach to ~22 at superior conjunction | The narration says "between three and twenty-two", which brackets the usual quoted range without pretending to a precision the geometry does not have |
| 2 | A round trip can reach ~44 minutes (B03, B00 props) | **VERIFIED** | Same | Simple doubling, stated as such on screen |
| 3 | Rovers are not joysticked; a command block is uplinked per sol before the rover wakes (B02, B03) | **VERIFIED** | MER/MSL operations practice, described in the light-time and operations sources | Framed as the operating model, not as a hard rule for every command type |
| 4 | Navcams are a stereo pair; disparity gives a height map, reduced to a per-cell traversability cost (B04) | **VERIFIED** | JPL Robotics M2020 mobility; ENav/GESTALT descriptions | The reel calls the cell value "how much the ground steps and tilts", which is step height + slope — the two standard terms |
| 5 | ENav evaluates ~1,700 candidate paths (B05, B11) | **VERIFIED** | IEEE Spectrum on Perseverance autonomous driving, citing the ENav design | Scoped in narration to "Perseverance's navigation software" |
| 6 | Planning horizon ~6 m ahead (B05, B11) | **VERIFIED** | Same | "usually reaching around six metres ahead" |
| 7 | Paths are scored on travel time and terrain roughness (B05) | **VERIFIED** | Same | |
| 8 | A clearance check (ACE) runs on only the top-ranked handful (B05) | **VERIFIED** | Same | The reel says "a proper clearance check on only the handful still standing" and does not name ACE on screen, to keep the beat readable |
| 9 | A second computer lets it process images while driving ("thinking while driving") (B05) | **VERIFIED** | JPL/NASA Perseverance autonomy article ("two computer brains working together", dedicated image-processing computer); VCE described in the M2020 landing press kit | The reel does not name the VCE on screen |
| 10 | AEGIS finds edges and groups them into closed outlines (B06) | **VERIFIED** | Planetary Society on AEGIS/Rockster: "edge-detection, edge-segment grouping and morphological operations" | Rockster is named in SOURCES, not on screen |
| 11 | Each outline is measured on brightness, shape, and range from stereo (B06) | **VERIFIED** | Same | The reel shows SIZE, BRIGHTNESS, RANGE |
| 12 | Candidates are ranked against a science-team "scene profile" (B06, B08) | **VERIFIED** | Same | "an adjustable framework called a scene profile" |
| 13 | The top target is shot with a laser (SuperCam/ChemCam LIBS) (B06) | **VERIFIED** | NASA SuperCam/AEGIS blog; AEGIS ChemCam literature | |
| 14 | Snowdrift Peak: ~520 m straight line, 759 m driven, 6 autonomous drive sols (B07, B10, B11) | **VERIFIED** | NASA JPL, *Autonomous Systems Help NASA's Perseverance Do More Science on Mars* (1,706 ft / 2,490 ft / six sols) | Feet converted; the reel rounds to whole metres |
| 15 | NASA estimates Curiosity would have taken ~12 sols longer (B07) | **VERIFIED** | Same | Attributed on screen and in narration as NASA's estimate |
| 16 | Curiosity drove ~6.2% of its distance autonomously (B09) | **VERIFIED** | IEEE Spectrum | |
| 17 | Perseverance ~90% autonomous as of sol 1,312 (B00 props, B09) | **VERIFIED** | IEEE Spectrum | The sol condition is on screen in B09's citation |
| 18 | Longest drive with no human review: 699.9 m (B09, B00 props) | **VERIFIED** | NASA JPL article (2,296.2 ft) | Narration says "almost seven hundred metres" |
| 19 | AEGIS selected the intended target material >93% of the time (B09) | **VERIFIED** | AEGIS performance evaluation on Curiosity ChemCam data (Francis et al., *Science Robotics* 2017 and follow-on results) | Condition stated on screen: Curiosity, ChemCam |
| 20 | Pointing without onboard intelligent targeting hit desirable material ~20% of the time (B09) | **VERIFIED — different evaluation** | AEGIS results reporting the >86%-vs-20% comparison | **Flagged in PEDAGOGY §2.** The two figures in B09 come from the same body of AEGIS work but not from a single head-to-head table; the on-screen citation says "two evaluations" |
| 21 | AEGIS first used on Perseverance 18 May 2022, sol 442 (B10, B11) | **VERIFIED** | NASA Mars 2020 status, *SuperCam Gains New Artificial Intelligence Capabilities with AEGIS Upgrade* | |
| 22 | AEGIS-Heavy deployed week of 2 Feb 2023, sol 697 (B10, B11) | **VERIFIED** | Same | |
| 23 | 255 sols between them (B10, B11) | **DERIVED** | 697 − 442 | Both sols are on screen so the viewer can do the subtraction |
| 24 | 239 m of the Snowdrift crossing was detour (B10) | **DERIVED** | 759 − 520 | **Flagged in PEDAGOGY §3.** Stated as "spent going around things", not as a published figure |

## Verified, then deliberately NOT used

- **Sojourner stopped every 13 cm; Spirit/Opportunity managed 0.5 m** (NASA).
  A lovely progression, but B05 is already the densest beat and the history does
  not change the argument.
- **The 331.74 m single-sol autonomous drive of 3 April 2023** (IEEE Spectrum)
  and **the 347.7 m single-day drive record** (NASA). Both are real, they are
  different metrics from different articles, and putting them beside the 699.9 m
  figure invites the viewer to try to reconcile three records. Only the 699.9 m
  "no human review" figure survives, because it is the one that is actually
  about autonomy rather than about speed.
- **"An iMac G3"** as the processor comparison (IEEE Spectrum). Funny, accurate,
  and it would pull the beat toward a hardware joke and away from the decision.
- **The ChemCam yield increase from 256 to 327 collections.** The number is
  reported but the period it covers is not stated unambiguously in the sources I
  could reach, so it is out. Ep. 05 set the precedent: a derived figure whose
  units cannot be checked comes out entirely rather than being patched.
- **The Xilinx Virtex-5QV and the Vision Compute Element by name.** True, cited
  in SOURCES, and too much apparatus for a beat whose point is "it looks while
  it drives".

## Imagery

**No NASA image is used anywhere in this reel.** Every terrain plate, cost map,
contour overlay and route map is generated by `assets/gen_mars.py` from a seeded
procedural height field. Beats that could be mistaken for showing a real camera
frame carry an on-screen SYNTHETIC caption; the route map carries SCHEMATIC.
Seeds are in `SOURCES.md`.

## DOUBLE-CHECK LAW — the fact-check of the fact-check

- **The strongest temptation in this topic was to call the rover "curious".** It
  is not. B08 exists specifically to say so, and the word "interesting" is in
  quotes-by-implication every time it appears.
- **The second temptation was to make the light-time number scarier than it is.**
  22 minutes is the far end, not the typical case. B03 gives the range.
- **The third was to let the Snowdrift detour read as a failure.** It is not —
  the crossing was 12 sols faster than the alternative. B07 lands the win before
  B10 prices it.
