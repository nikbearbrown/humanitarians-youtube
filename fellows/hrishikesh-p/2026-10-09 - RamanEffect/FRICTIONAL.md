# Week 6 Summary: RNN Architecture & Comparative Results for Raman Spectroscopy

## Video Links

- [16:9 video](https://drive.google.com/file/d/1xUevGIxN8gknxQ1OYP6nyflM656rwBsS/view?usp=drive_link)
- [9:16 video](https://drive.google.com/file/d/1PlKiuVd40nQ8oarqcJW-RUDckAGzA0a2/view?usp=drive_link)

In Week 6, we tested the hypothesis that Raman spectra can be modeled as sequential 1D time-series data using Recurrent Neural Networks. By building and training a Bidirectional Long Short-Term Memory network (`RamanLSTM`) across 30 bacterial classes, we uncovered a critical negative result: the RNN achieves only 3.33% test accuracy, perfectly matching random chance (1/30).

Because Raman spectra span 1,000 wavenumbers, vanishing gradients cause catastrophic forgetting of early spectral peaks. This result provides crucial empirical validation for our comparative study:
- Sequential Models (RamanLSTM): 3.33% (fails on L=1000 sequence)
- Deep Spatial Models (ResNet): 67.50% (overfits 1D spectral data)
- Local Spatial Models (Simple CNN): 85.30% (optimally preserves peak geometry)

**Conclusion:** Raman spectra must be computationally modeled as localized spatial structures (1D images), not continuous time-series sequences.

## Chapters
0:00 - Introduction & The Sequential Hypothesis
0:10 - Vanishing Gradients & Catastrophic Forgetting
0:22 - PyTorch RamanLSTM Implementation
0:36 - Experimental Results: Random Guess Baseline
0:53 - 3-Way Architectural Comparison
1:08 - Inductive Bias: Spectra as 1D Images
1:20 - Your Turn to Explore
1:32 - Outro

---
*Created by Hrishikesh for RamanEffect.*

