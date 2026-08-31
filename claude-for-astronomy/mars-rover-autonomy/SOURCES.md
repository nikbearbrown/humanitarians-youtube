# SOURCES — *Nobody Is Coming to Approve It.*

Ep. 06 · AI in Astronomy & Space Science

## Primary and institutional sources

| Short cite | Full source |
|---|---|
| NASA JPL 2023 (autonomy) | *Autonomous Systems Help NASA's Perseverance Do More Science on Mars* — [jpl.nasa.gov](https://www.jpl.nasa.gov/news/autonomous-systems-help-nasas-perseverance-do-more-science-on-mars/) · [nasa.gov mirror](https://www.nasa.gov/missions/mars-2020-perseverance/perseverance-rover/autonomous-systems-help-nasas-perseverance-do-more-science-on-mars-2/). Source of Snowdrift Peak (1,706 ft straight / 2,490 ft driven / six autonomous drive sols / ~12 sols faster than Curiosity), the 2,296.2 ft longest drive without human review, the 1,140.7 ft single-day drive record, the Sojourner/MER/MSL autonomy progression, and the "two computer brains working together" description. |
| IEEE Spectrum 2024 | *Mars Rover Perseverance Sets Autonomous Driving Record* — [spectrum.ieee.org](https://spectrum.ieee.org/perseverance-mars-rover-autonomous-driving). Source of the ~1,700 evaluated paths, the ~6 m planning horizon, the travel-time-plus-roughness cost, the ACE clearance check applied only to top-ranked candidates, Curiosity at ~6.2% autonomous versus Perseverance at ~90% by sol 1,312, and 95% during the 24-sol delta campaign. |
| Rankin et al. 2023 | *Autonomous robotics is driving Perseverance rover's progress on Mars*, **Science Robotics** — [doi:10.1126/scirobotics.adi3099](https://www.science.org/doi/10.1126/scirobotics.adi3099) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37494463/). The peer-reviewed overview behind the AutoNav/ENav operational figures. |
| Francis et al. 2017 | *AEGIS autonomous targeting for ChemCam on Mars Science Laboratory: deployment and results of initial science team use*, **Science Robotics** — [doi:10.1126/scirobotics.aan4582](https://www.science.org/doi/10.1126/scirobotics.aan4582). The primary AEGIS paper; source of the target-selection success figures. |
| Francis et al. 2020 (iSAIRAS) | *Results from the First Four Years of AEGIS Autonomous Targeting on MSL* — [hou.usra.edu](https://www.hou.usra.edu/meetings/isairas2020fullpapers/pdf/5017.pdf). |
| Francis et al. 2024 (iSAIRAS) | *AEGIS on M2020* — [ai.jpl.nasa.gov](https://ai.jpl.nasa.gov/public/documents/papers/francis-isairas-2024.pdf). |
| NASA Mars 2020 status 446 | *SuperCam Gains New Artificial Intelligence Capabilities with AEGIS Upgrade* — [science.nasa.gov](https://science.nasa.gov/blog/supercam-gains-new-artificial-intelligence-capabilities-with-aegis-upgrade/) · [mars.nasa.gov](https://mars.nasa.gov/mars2020/mission/status/446/supercam-gains-new-artificial-intelligence-capabilities-with-aegis-upgrade/). Source of AEGIS-Lite first use on 18 May 2022 (sol 442), AEGIS-Heavy the week of 2 Feb 2023 (sol 697), and the LIBS/VISIR and five-target details. |
| Planetary Society | *Automating Science on Mars* — [planetary.org](https://www.planetary.org/articles/0313-automating-science-on-mars). Source of the Rockster description (edge detection, edge-segment grouping, morphological operations), the measured properties (brightness, shape, stereo range), and the "scene profile" framing. |
| ESA Mars Express | *Time delay between Mars and Earth* — [blogs.esa.int](https://blogs.esa.int/mex/2012/08/05/time-delay-between-mars-and-earth/). Source of the one-way light-time range. |
| JPL Robotics — M2020 mobility | [www-robotics.jpl.nasa.gov](https://www-robotics.jpl.nasa.gov/what-we-do/flight-projects/mars-2020-rover/m2020mobility/). Source of the stereo-to-cost-map pipeline description. |
| Mars 2020 landing press kit | [jpl.nasa.gov](https://www.jpl.nasa.gov/news/press_kits/mars_2020/landing/mission/spacecraft/perseverance_rover/). Source of the Vision Compute Element description (cited, deliberately not named on screen — see FACTCHECK). |

Verified but deliberately unused: the 331.74 m single-sol autonomous drive of
3 April 2023, the 347.7 m single-day drive record, the iMac G3 processor
comparison, and the ChemCam 256→327 collections figure. See `FACTCHECK.md`
§ "Verified, then deliberately NOT used".

## Reel provenance

| Item | Value |
|---|---|
| Brief | `E:/NEU/Jobs/Humanitarians_AI/weekly_stem_videos/ideas.md` → Astronomy, topic **06** ("Mars rover autonomy") |
| Series | AI in Astronomy & Space Science, **Ep. 06** |
| Sibling episodes | `ai-vs-the-data-deluge` (01) · `exoplanet-hunting` (02) · `gravitational-wave-detection` (03) · `galaxy-classification` (04) · `fast-radio-bursts` (05) |
| Fact-check date | 2026-08-28, during this build |
| Toolkit | `brutalist.art` · skill `ai-explainer` · channel `claude-hai` |
| Slug | `mars-rover-autonomy` — matches the folder |
| Deliverables | 16:9 at 3840×2160 **and** 9:16 at 2160×3840, both full length, same beats |

## Generated imagery — provenance and seeds

Every plate is **synthetic**, produced by `assets/gen_mars.py` from a seeded
procedural height field: fractal value noise for the ground, irregular embossed
caps for rocks, Lambertian shading with a marched **cast-shadow** pass under a
low sun, rendered monochrome. Navcam and Hazcam are genuinely greyscale
instruments, so a mono plate is the honest depiction rather than a stylisation.
Nothing was downloaded, licensed, or traced from a NASA image. Re-running the
script reproduces every PNG byte-for-byte.

| Asset | Recipe | Seed |
|---|---|---|
| `navcam.png` | forward-looking terrain, 34 rocks, low sun | 101 |
| `navcam_far.png` | the stereo partner / a sparser field | 104 |
| `costmap.png` | the same terrain reduced to a 40-px cell grid scored on step height + slope; cells under the traversable floor stay page-white | 101 |
| `pathfan.png` | the cost map with 96 drawn candidate arcs over a ~6 m horizon; feasible = no cell above the clearance limit; the winner is the feasible arc that reaches furthest forward | 101 (+7 for the fan) |
| `rockfield.png` | a closer scene, 13 rocks, larger | 202 |
| `rockfield_edges.png` | six closed contours, one per well-separated rock | 202 (+3) |
| `rockfield_ranked.png` | the same contours scored on size, brightness and range; the winner in terracotta | 202 (+3) |
| `route.png` | top-down boulder field: the straight line, and the bowed route actually driven | 303 |

**The fan draws 96 arcs, not 1,700.** ENav's real figure is ~1,700 per planning
step; a plate that drew 1,700 arcs is a solid hairball with nothing legible in
it. The plate draws a legible subset and the beat states the real number on
screen. The *scoring* is not a stand-in: a path is feasible if no cell it
crosses exceeds the clearance limit, and the winner is the feasible path that
gets furthest forward — which is the actual shape of the decision, and it is why
the rejected arcs are allowed to run straight through obstacles.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is latency, not volume.** `ideas.md` says Ep. 01 exists so later
   episodes need not re-argue the data-deluge premise. This episode's premise is
   the opposite kind of problem, and B01 says so out loud so the pivot is not
   accidental.
2. **The design tell is that "interesting" is a document.** Framed at B08 as the
   honest engineering answer, not as the failure, so it does not land as Ep. 03's
   out-of-distribution punchline or Ep. 04's crowd-ceiling punchline a second time.
3. **The limits are new to the series.** Ep. 05's limit was irreversibility; this
   one's are the price of caution (metres) and the latency of *correction* (sols).
4. **Two derived numbers are labelled as derived on screen** (239 m of detour;
   255 sols), and both of their inputs are shown so the viewer can check the
   subtraction.
5. **Two figures in B09 come from different evaluations** and the citation line
   says so rather than implying a single head-to-head table.
6. **No invented numbers, and no NASA imagery.**

## Not used

- No archival or licensed imagery. No AI-generated stills. No stock. No screen
  recordings. No NASA photograph reproduced, redrawn, or traced.
