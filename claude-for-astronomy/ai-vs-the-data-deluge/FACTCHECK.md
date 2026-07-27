# Ep. 01 — AI vs. the Data Deluge — Fact-Check

**Status: All verification done, including the 2026-07-26 second-pass additions (dual-view
architecture). All wording/decision items are resolved — see "Resolved decisions" below.**

Beat numbers below refer to the 18-beat list in `SHOTLIST.md` (revised 2026-07-26, second pass).

| Claim (as used in script) | Beat(s) | Verification | Source | Status |
|---|---|---|---|---|
| Kepler-90i was discovered by a neural network (Shallue & Vanderburg), announced Dec 2017 | 1, 7, 12, 13 | Confirmed. Paper: "Identifying Exoplanets with Deep Learning: A Five-planet Resonant Chain around Kepler-80 and an Eighth Planet around Kepler-90" (Shallue & Vanderburg, 2018/AJ). Christopher Shallue = Google AI engineer; Andrew Vanderburg = astronomer (UT Austin at the time of discovery). | [NASA news release](https://www.nasa.gov/news-release/artificial-intelligence-nasa-data-used-to-discover-eighth-planet-circling-distant-star/); [Smithsonian Magazine](https://www.smithsonianmag.com/science-nature/ai-finds-first-eight-planet-solar-system-besides-ours-180967554/) | ✅ |
| Kepler-90 became the first known system with 8 planets outside our own (tying the solar system's planet count) | 1, 13 | Confirmed — headline claim of the discovery. | [NASA Science](https://science.nasa.gov/universe/exoplanets/discovery-of-eight-planets-makes-alien-system-the-first-to-tie-with-our-solar-system/) | ✅ |
| Network trained on 15,000 human-vetted light curves | 8 | Confirmed. | [Smithsonian Magazine](https://www.smithsonianmag.com/science-nature/ai-finds-first-eight-planet-solar-system-besides-ours-180967554/) | ✅ |
| **NEW** — Network processed each light curve as two separate views: a "global view" (entire folded orbit, 2,001 bins, 8 convolutional layers) and a "local view" (zoomed on the transit, 201 bins, 4 convolutional layers), merged only at a final fully-connected layer | 9, 10, 11 | Confirmed. This is AstroNet's actual documented architecture, not a simplification — the two-column design with these exact bin counts and layer depths is described consistently across the original work and follow-up papers that build on it. | [Classifying Exoplanet Candidates with CNNs (NGTS), arXiv](https://arxiv.org/pdf/1907.11109); [Identifying Exoplanets with Deep Learning II, arXiv](https://arxiv.org/pdf/1903.10507); [Rapid Classification of TESS Candidates with CNNs, arXiv](https://arxiv.org/pdf/1902.08544) | ✅ |
| **NEW** — The global view is what catches an eclipsing binary star (a false-positive source) via a secondary eclipse elsewhere in the orbit; the local view judges the fine shape of the transit itself | 10 | Confirmed — this is the documented *purpose* of the two-view split, not my own inference: "the global view shows the out-of-transit noise as well as any secondary eclipses, while the local primary view draws out the details of the primary transit." | Same sources as above (arXiv 1907.11109, 1903.10507, 1902.08544) | ✅ |
| Kepler-90i had ~1-in-10,000 odds of being a false positive | 12 | Confirmed. | [Smithsonian Magazine](https://www.smithsonianmag.com/science-nature/ai-finds-first-eight-planet-solar-system-besides-ours-180967554/) | ✅ |
| Network correctly distinguished real planets from false positives ~96% of the time | 14 | Confirmed. | [Smithsonian Magazine](https://www.smithsonianmag.com/science-nature/ai-finds-first-eight-planet-solar-system-besides-ours-180967554/) | ✅ |
| Kepler monitored roughly 150,000–200,000 stars simultaneously | 3 | Confirmed range — sources vary (150,000 vs. 190,000+); "up to 200,000" stays inside the reported range. | [PNAS](https://www.pnas.org/doi/10.1073/pnas.1304196111); [Eos.org](https://eos.org/features/kepler-a-giant-leap-for-exoplanet-studies) | ✅ (range, not exact) |
| Kepler recorded brightness at ~30-minute cadence | 3 | Confirmed — 30-minute "long cadence" was the default for the vast majority of targets. | [Kepler & K2 Science Center](https://keplerscience.arc.nasa.gov/k2-observing.html) | ✅ |
| Kepler's primary mission ran ~4 years (2009–2013) | 3 | Confirmed. | [Eos.org](https://eos.org/features/kepler-a-giant-leap-for-exoplanet-studies) | ✅ |
| ~~Earth transiting the Sun would dim it by ~0.01%~~ — **cut from the script 2026-07-26** to make room for the architecture beats | — | No longer used. Was previously verified as a computed estimate; leaving this row for the audit trail only, not because anything was wrong with it. | Computed | N/A — not used |
| Vera Rubin Observatory processes ~10 terabytes of raw images per night | 15 | Confirmed for the Prompt Processing system's raw-image throughput specifically. | [Rubin Prompt Processing System, arXiv](https://arxiv.org/pdf/2603.19541) | ✅ — see "Resolved decisions" for why 10TB over 20TB |
| Rubin generates up to seven million alerts per night | 16 | Confirmed as the figure used in real-time-alert reporting. | [Stanford Report](https://news.stanford.edu/stories/2026/02/rubin-observatory-real-time-alerts-astronomical-events) | ✅ — see "Resolved decisions" for why 7M over 10M |
| Rubin's 10-year survey will total ~60 petabytes | 16 | Confirmed. | [Rubin Observatory news release](https://rubinobservatory.org/news/first-alerts) | ✅ |
| NASA/Ames Kepler-90 artist concept credit line | 13 | Confirmed exact credit: **NASA/Ames Research Center/Wendy Stenzel**, image ID **PIA22193**. | [NASA JPL image page](https://www.jpl.nasa.gov/images/pia22193-kepler-90-system-compared-to-our-solar-system-artists-concept/) | ✅ |
| Rubin Observatory press-image credit line | 15 | Confirmed exact credit: **RubinObs/NOIRLab/SLAC/NSF/DOE/AURA** (this is the full current line — an older/shorter "RubinObs/NSF/AURA" also circulates but the full line is what NOIRLab's own releases use). | [NOIRLab news release](https://noirlab.edu/public/news/noirlab2521/) | ✅ |
| "Zooming into NSF–DOE Rubin's Ocean of Stars" credit + acknowledgements | 17 | Confirmed verbatim by you directly off the NOIRLab page: Credit "NSF–DOE Vera C. Rubin Observatory/NOIRLab/SLAC/AURA"; Acknowledgements "unWISE/NASA/JPL-Caltech/D. Lang/A. Meisner." | [NOIRLab video page](https://noirlab.edu/public/videos/noirlab2616g/) | ✅ |

## Resolved decisions (previously left open — filled in 2026-07-26)

These three were **not** left open because they were unverified — every number was already checked
against a real source. They were left open because they were **judgment calls** (which true number
to lead with, or a rights/licensing risk call), and those were flagged for you rather than decided
silently. Since you asked me to make the call given you don't have astronomy background to weigh
in, here's what I picked and why:

1. **Rubin "10TB vs 20TB/night" → picked 10TB.**
   Both figures are real and both appear in reporting, but they measure different things: 10TB is
   specifically the raw-image throughput of the Prompt Processing pipeline (the system the "AI
   triages it" claim is actually about), sourced straight from the system's own paper. The 20TB
   figure shows up in looser secondary reporting without a clear statement of what's included
   (e.g., calibration data, metadata). Since the script's claim is specifically about the pipeline
   that does the triaging, the number tied directly to that pipeline is the more defensible one to
   put in a video that will get fact-checked by viewers.

2. **Rubin "7M vs 10M alerts/night" → picked "up to seven million."**
   10 million is the system's designed *ceiling* capacity; 7 million is the figure used when
   describing what the real-time alert system is actually reporting. I chose the operational
   number over the theoretical max because a video claim should describe what the system does,
   not what it's rated for — it's the more conservative, harder-to-nitpick choice, and it still
   supports the point (millions per night, no human team could review it).

3. **Shallue/Vanderburg photo rights (beat 7) → resolved by avoiding the question entirely.**
   I couldn't confirm usable image rights for photos of two named private individuals (one at
   Google, one an academic who has since changed institutions), and getting that wrong is a real
   legal/reputational risk, not just a stylistic one. Rather than guess at licensing I can't
   verify, this beat now carries their names as on-screen text with no photo at all (first moved
   off real photos to a generated image on 2026-07-26, then off Higgsfield entirely to a plain
   Remotion name-card once beats 1/2/6/8 were converted to in-house tools — see `SHOTLIST.md`).
   Either way, the underlying fix is the same: the beat no longer depends on a photo whose rights
   couldn't be verified.

**Money status:** none of the above ever concerned spending. The 4 Higgsfield (paid) beats
(1, 2, 6, 8) were approved, then eliminated entirely when those beats moved to Manim/Remotion —
this episode currently has zero paid-generation spend. See `PROMPTS.md` for the record of the
approved-then-unused Higgsfield prompts, and `SHOTLIST.md` for the final shot-type assignments.
