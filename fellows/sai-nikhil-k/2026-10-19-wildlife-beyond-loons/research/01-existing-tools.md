# Research 1 — existing open wildlife-AI tools (accessed 2026-10-19/20)

Repo facts from `gh api repos/<r>` and `repos/<r>/releases/latest`, run 2026-10-20.
Code licence = GitHub's SPDX detection; weights licence noted separately where it differs.

| tool | repo | code licence | latest release | taxa / input → output |
|---|---|---|---|---|
| MegaDetector | agentmorris/MegaDetector | MIT | v1000.0, 2025-07-23 | camera trap → boxes: animal / person / vehicle (no species) |
| PyTorch-Wildlife (MS AI for Good) | microsoft/CameraTraps → now microsoft/Biodiversity | MIT | pw_v1.3.0, 2026-04-22 | camera trap; hub for MegaDetector, SPARROW, bioacoustics |
| SpeciesNet (Google) | google/cameratrapai | Apache-2.0 | no GitHub release (404) | camera trap → species classification |
| BirdNET-Analyzer | birdnet-team/BirdNET-Analyzer | MIT (code) | v2.4.0, 2025-11-07 | audio → bird species |
| BirdNET-Pi | Nachtzuster/BirdNET-Pi | NOASSERTION | v0.1, 2024-02-10 | audio, Raspberry Pi, realtime |
| Zamba (DrivenData) | drivendataorg/zamba | MIT | v2.7.2, 2026-06-30 | camera-trap video + images → species; distance estimation |
| Wildbook (Wild Me) | WildMeOrg/Wildbook | GPL-2.0 | 10.14, 2026-09-15 | photo → individual ID (web platform, collaborative) |
| HerdNet | Alexandre-Delplanque/HerdNet | MIT | v0.2.1, 2024-03-26 | aerial → points/counts, African mammals |
| AddaxAI (ex-EcoAssist) | PetervanLunteren/AddaxAI | MIT | v7.16.0, 2026-10-15 | camera trap desktop app (Win/mac/Linux) |
| BatDetect2 | macaodha/batdetect2 | NOASSERTION | v1.3.1, 2026-03-25 | ultrasonic audio → bat calls |
| OpenSoundscape | kitzeslab/opensoundscape | MIT | v0.13.2, 2026-06-30 | bioacoustics framework |
| DeepForest | weecology/DeepForest | MIT | v2.1.0, 2026-02-26 | airborne RGB → tree crowns + bird boxes |

## Licence / openness notes (verified below as found)
- **BirdNET:** README §License (gh, 2026-10-20): code MIT; "The models used in this project are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)." Also: "all educational and research purposes are considered non-commercial use". → NC weights; an AGPL app can't relicense them.
- **DeepFaune** (plmlab.math.cnrs.fr/deepfaune/software, README): code CeCILL (GPL-compatible); weights CC BY-NC-SA 4.0; "Commercial use of any element of deepfaune (code or model weights) is forbidden." Contact Vincent Miele.
- **SpeciesNet:** README: MegaDetector detector + EfficientNet V2 M classifier, ">2000 labels", trained on "over 65M images"; weights on Kaggle (kaggle.com/models/google/speciesnet). Runs locally via AddaxAI; cloud via Wildlife Insights, Animl. Repo Apache-2.0.
- **iNaturalist CV model:** no official weights download found; forum answer points to third-party models trained on iNat data. Training code (inatVisionTraining) public; training data available via AWS Open Data. Weights: UNVERIFIED / appear closed. (forum.inaturalist.org/t/computer-vision-model-parameters-available/45408)
- **Merlin:** not checked; treat as closed app (UNVERIFIED).
- **Wild Me / Wildbook:** web platforms per taxon — Flukebook (whales/dolphins; 2024 deck says "50+ species"), Whiskerbook (spotted cats), Sharkbook, GiraffeSpotter, Zebra Wildbook, African Carnivore Wildbook, Seal Wildbook. Collaborative, server-side — not an offline single-user app. (wildme.org/platforms.html)
- **DuckNet** (mkmitchell/DuckNet): "Deep learning-based tool for automated identification of duck species from drone imagery." Licence NOASSERTION, 4 stars, pushed 2026-10-19.
- Aerial waterbirds in the literature: Rice/Houston Audubon detector, 16 Texas colony species (arXiv 2210.04868); Adelaide/MDBA straw-necked ibis colony counter (2022); Audubon "SeeBird" suite — licences/offline status UNVERIFIED.

## GAPS (synthesis, not a source claim)
1. **Camera traps are solved-ish** — MegaDetector (MIT) + SpeciesNet (Apache) + AddaxAI desktop GUI already run offline. Building another is not a gap.
2. **Bird audio is covered but NC** — BirdNET weights are CC BY-NC-SA; a permissive alternative is a gap, but it's audio, not Gavia's photo shape.
3. **Single-species photo/drone detectors with a review-first offline desktop app** — research code exists (DuckNet, Rice waterbirds, MDBA ibis) but no installable app like Gavia. This is Gavia's niche, open for other species.
4. **Individual ID offline** — Wildbook is server-side; nothing installable for a single field team.
5. **Aerial counts outside African mammals** — HerdNet covers African herds; seals/colonies/nests have papers, not tools (to confirm in research 2).
