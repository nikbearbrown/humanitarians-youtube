# CNN vs. ResNet: 1D Spectral Architecture Teardown

## LegacyCNN vs. Raman1DCNN

In this architectural teardown, we compare and contrast plain Convolutional Neural Networks (**`LegacyCNN`**) against Residual Networks (**`Raman1DCNN` / 1D-ResNet**), examining how layer topology, identity shortcut connections, pooling operators, and receptive field scaling govern representation learning on 1,000-point vibrational Raman spectra.

While conventional deep learning intuition suggests that deeper networks with more parameters always learn superior representations, 1D spectral data exposes a sharp tension between **model capacity** and **spatial inductive bias**. By inspecting the exact PyTorch implementations (`legacy_baseline/model.py` and `src/model.py`) alongside evaluations across preprocessed, augmented, and raw spectra ($N = 3,000$), we show why residual skip connections are essential for deep optimization—and why a shallow 6-layer convolutional bottleneck outperforms a 25-layer ResNet on raw bacterial Raman peaks.

## Video Links

- [16:9 video](https://drive.google.com/file/d/1ZKckHZmxm6UxpkTayt2t3gr6t7ZN2UjD/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/10tM5jfvwokSynajs2lVfM1YthImbrA86/view?usp=sharing)
