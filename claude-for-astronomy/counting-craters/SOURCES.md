# SOURCES — Ep. 18, *counting-craters*

Register: Pragmatist. Audience: STUDENTS. Spine: when to use AI and when not.
Every source below was read for its claims and **rewritten**, never parroted —
DOUBLE-CHECK LAW. Corrections applied during fact-checking are logged at the
bottom.

---

## Primary — the counting half

**Robbins, S. J., & Hynek, B. M. (2012).** *A new global database of Mars
impact craters ≥1 km: 1. Database creation, properties, and parameters.*
Journal of Geophysical Research 117, E05004. doi:10.1029/2011JE003966
→ 384,343 craters, statistically complete to D ≥ 1 km. Built by hand. Used in
B04 as the scale of what humans actually did.

**Robbins, S. J., et al. (2014).** *The variability of crater identification
among expert and community crater analysts.* Icarus 234, 109–131.
doi:10.1016/j.icarus.2014.02.022 · arXiv:1404.1334
→ Expert-to-expert differences up to ~±45%, depending on diameter, counts per
bin and terrain; volunteers ~2× the dispersion of experts; artifacts near the
minimum diameter, with caution urged for craters ≤10 px. Used in B05 and on
the B11 artifact. **This is the paper that makes automation an argument about
consistency rather than speed.**

**Silburt, A., Ali-Dib, M., Zhu, C., Jackson, A., Valencia, D., Kissin, Y.,
Tamayo, D., & Menou, K. (2019).** *Lunar crater identification via deep
learning.* Icarus 317, 27–38. arXiv:1803.02192
→ UNet on LRO DEM data. 92% recall post-processing; **57% ± 20% raw CNN
recall** (83% ± 16% for craters < 15 px radius); ~42% of extracted craters new;
~11% false-positive rate among new detections, estimated from inspecting 361.
Used in B06 — including the raw number, on screen.

**Benedix, G. K., et al. (2020).** *Deriving surface ages on Mars using
automated crater counting.* Earth and Space Science 7, e2019EA001005.
doi:10.1029/2019EA001005
→ YOLO-based crater detection on THEMIS imagery, trained on 7,048 manually
identified craters; 91% positive identification at D ≥ 1 km; motivates
automation by the tens-of-millions population between 10 m and 1 km. Used in
B04 (the scale argument) and B06 (the training-set bar).

## Primary — the dating half

**Neukum, G. (1983).** Habilitation thesis; restated in **Neukum, G., Ivanov,
B. A., & Hartmann, W. K. (2001).** *Cratering records in the inner Solar
System in relation to the lunar reference system.* Space Science Reviews 96,
55–86. Coefficient form as used here from **Neukum et al., LPSC XXXIII (2002),
abstract 1263.**
→ `N(1) = 5.44e-14 (exp(6.93 T) - 1) + 8.38e-4 T`. The curve in B02, B07, B08
and every derived number in this episode.

**Li, Q.-L., et al. (2021).** *Two-billion-year-old volcanism on the Moon from
Chang'e-5 basalts.* Nature 600, 54–58. doi:10.1038/s41586-021-04100-2
→ Pb–Pb age **2,030 ± 4 Ma** on basalt clasts; described by the authors as
residing "squarely in the centre of this large gap" and providing "a pivotal
calibration point for crater-counting chronology in the inner Solar System."
Used in B09 and B10.

**Qiao, L., et al. (2021).** *Cratering records in the Chang'e-5 mare unit:
filling the "age gap" of the lunar crater chronology and preparation for its
recalibration.* Geophysical Research Letters 48, e2021GL095132.
doi:10.1029/2021GL095132
→ Crater counts give the unit ~**1.3–2.7 Ga** across several chronology
models, inside the ~1–3 Ga gap between existing calibration points. Used in
B10 as the counted window.

**Yue, Z., et al. (2022).** *Updated lunar cratering chronology model with the
radiometric age of Chang'e-5 samples.* Nature Astronomy 6, 541–545.
doi:10.1038/s41550-022-01604-3
→ Refit using the 2.030 ± 0.004 Ga anchor; ages older than Neukum for most of
lunar history, **maximum difference 0.24 Gyr at 2.55 Ga**. Used in B10 as the
episode's own counter-evidence.

**Hiesinger, H., et al. (2023).** *Cratering history and lunar chronology.*
Reviews in Mineralogy & Geochemistry 89, 401–451.
→ The calibration sites (Apollo 11, 12, 14, 15, 16, 17; Luna 16, 24) and their
correlation with radiometric ages; sparse coverage for 1–3 Ga. Background for
the structure of `anchors.png`.

**Stöffler, D., & Ryder, G. (2001).** *Stratigraphy and isotope ages of lunar
geologic units.* Space Science Reviews 96, 9–54.
→ The conventional radiometric ages used to place the anchor dots. Placement
is illustrative — see FACTCHECK F9.

## Consulted, used for scoping only

**Robbins, S. J., & Hynek, B. M. (2014)** — describes the 2012 database as
~640,000 craters total, ~385,000 forming the complete D ≥ 1 km census.
Consulted to keep F2 from quoting the wrong figure.

**Fairweather, J. H., et al. (2023)** — comparison of automated Mars crater
catalogues (Benedix 2020 vs Lee & Hogan 2021). arXiv:2308.14650. Consulted to
confirm that automated catalogues differ from each other, which is why B06's
claim is about perception scaling, not about a detector being "right".

**Giannakis, I., et al. (2023)** — zero-shot crater detection with Segment
Anything. arXiv:2304.07764. Detection only, no age estimation. Consulted when
checking whether anyone regresses surface age directly from imagery.

**Chen, Y., et al. (2020)** — lunar crater identification and age estimation
from Chang'E data by deep and transfer learning. Consulted as the closest
counter-example to this episode's thesis; it treats crater *degradation-stage*
age as a classification target and does not move the chronology curve. Scoped
explicitly in FACTCHECK "Claims deliberately NOT made".

**Jia, Y., et al. (2024)** — recalibration of the lunar chronology for spatial
cratering-rate variability. Icarus. Notes that all calibration points except
Chang'e-5 sit very close to the equator. Consulted; not used on screen,
because it adds a second complication the runtime cannot carry honestly.

---

## Corrections applied during fact-checking

1. **"92% recall" was nearly shipped alone.** The raw per-CNN recall is 57% ±
   20%; the 92% is post-processing. B06 now shows both, with 57% ghosted
   beneath. A headline recall quoted without its post-processing qualifier
   would have been exactly the kind of claim this channel exists to puncture.
2. **The Mars catalogue count was nearly quoted as ~635,000.** That is the
   press release's rounded total including sub-kilometre craters. The paper's
   own complete-census figure is 384,343, and the screen labels it "D ≥ 1 km".
3. **The ±45% was nearly attributed to the simulation.** `spread.png`'s
   analysts are synthetic. The figure is cited from Robbins et al. (2014) and
   placed on screen as a citation; `gen_craters.py` asserts nothing about the
   analyst model.
4. **`cost.png` originally taught the opposite of its beat.** Drawn on an
   absolute time axis the two age windows are only 1.6× apart and read as
   "about the same". A second panel was added showing each window against its
   own age. See FACTCHECK F7.
5. **`pile.png` originally read as a linear axis**, making the automation gap
   look like ~4× instead of ~78×. Decade rails were added and the beat now
   states the axis is log.
6. **"Reinforcement learning" was never introduced.** `ideas.md`'s topic line
   for Ep. 17 mentioned RL; topic 18 does not, and no source here uses it.
   Nothing in this episode claims a learned policy anywhere.
7. **The anchor ages are illustrative and now say so.** Sources differ on
   which sites count as independent anchors, so the episode shows the shape
   (cluster / gap / cluster) and never a tally.

## Determinism

`assets/gen_craters.py` is seeded (`1801`–`1804`) and asserts nine claims
before writing. Same seeds → identical plates every render. No network access,
no paid API, no key. Total spend for this episode: **$0.00.**
