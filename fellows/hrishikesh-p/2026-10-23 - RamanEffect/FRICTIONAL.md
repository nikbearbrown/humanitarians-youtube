[Week 8 commit](https://github.com/hspgit/RAMAN-Effect/commit/23883ad3b3bc587d719f898efbe74101bef97bb0)

# Week 8: Empiric Antibiotic Groupings and Clinical Accuracy

This week examined how raw Raman spectra can support empiric treatment decisions using the bacterial spectroscopy study **"Rapid identification of pathogenic bacteria using Raman spectroscopy and deep learning"** (Ho et al., *Nature Communications*, 2019).

The evaluation remapped 30 reference isolates into 8 treatment groups and tested 3,000 unseen spectra. This reframes clinically benign within-treatment-group confusion separately from true prescribing errors: over 80% of isolate-level mistakes received the same treatment recommendation.

## Results

| Model | Isolate accuracy | Treatment-group accuracy | Gain |
| --- | ---: | ---: | ---: |
| Legacy CNN | 82.23% (2,467/3,000) | 96.53% (2,896/3,000) | +14.30% |
| ResNet (`Raman1DCNN`) | 80.00% (2,400/3,000) | 94.80% (2,844/3,000) | +14.80% |

- **Clinical error analysis:** 429 of 533 Legacy CNN isolate errors (80.5%) stayed within the same treatment group; 104 were cross-treatment errors (3.47% of all spectra).
- **Best group results:** Daptomycin reached 100.00% accuracy and Caspofungin 99.50%. Legacy CNN also outperformed ResNet on TZP (96.00% vs. 88.00%) and Penicillin (95.86% vs. 91.29%).
- **Decision support:** A direct 8-class head with 10,000 Monte Carlo majority votes over 10 spectra simulates a treatment recommendation in under one hour, compared with 24–72 hours for culture.

## Treatment Groups

`ATCC_GROUPINGS` maps the 30 isolates to these 8 empiric treatment classes:

| Group | Treatment | Main organisms | Spectra |
| ---: | --- | --- | ---: |
| 0 | Meropenem | Enteric Gram-negative rods | 800 |
| 1 | Ciprofloxacin | *Salmonella enterica* | 100 |
| 2 | TZP | *Pseudomonas aeruginosa* | 200 |
| 3 | Vancomycin | Staphylococci, including MSSA and MRSA | 700 |
| 4 | Ceftriaxone | *Streptococcus pneumoniae* | 200 |
| 5 | Penicillin | Streptococci and *E. faecalis* | 700 |
| 6 | Daptomycin | *Enterococcus faecium* / VRE | 100 |
| 7 | Caspofungin | *Candida albicans* and *C. glabrata* | 200 |

## Video Chapters

`0:00` Sepsis and the clinical accuracy dilemma · `0:17` Isolate versus clinical accuracy · `0:33` Treatment mapping · `0:49` Results · `1:03` Evaluation architecture · `1:18` Model comparison · `1:34` Raman peak preservation · `1:47` Ten-spectra voting · `2:02` Monte Carlo voting · `2:14` Benchmarking · `2:29` Outro

## Evidence

- **Paper:** Ho et al., *Rapid identification of pathogenic bacteria using Raman spectroscopy and deep learning*, *Nature Communications* (2019).
- **Code:** `src/engine.py`, including `ATCC_GROUPINGS` and post-hoc treatment mapping.
- **Automation:** Managed and verified with Swamp (`@hspsat/brutalist-reel`).
- **Videos:** [16:9](https://drive.google.com/file/d/1ZEEaDkIRnRjdvGCCnVK9SCFeP7F39OVC/view?usp=drive_link) · [9:16](https://drive.google.com/file/d/1cfbvhZzKi9g0oPb6D0GtltLuKUWPqcNK/view?usp=drive_link)

*Created by Hrishikesh for RamanEffect.*

*Tags: #RamanSpectroscopy #DeepLearning #ClinicalAI #Antibiotics #Sepsis #MachineLearning #RamanEffect #Bioinformatics*