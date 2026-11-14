# JEPA Explained: Latent World Models

This architecture teardown compares **JEPA (Joint-Embedding Predictive
Architecture)** with vision-language models (VLMs) such as `CLIP` and `LLaVA`,
and pixel-reconstruction models such as `MAE` and `VideoMAE`.

## Why JEPA?

- **Pixel reconstruction:** `MAE`, `VideoMAE`, and autoregressive tokenizers
  spend capacity predicting unpredictable detail such as textures, lighting,
  and sensor noise.
- **Language alignment:** `CLIP`, `LLaVA`, and other contrastive VLMs compress
  3D geometry, occlusion, and temporal physics into short text descriptions.
- **JEPA:** `I-JEPA` and `V-JEPA` predict masked target representations in
  latent space instead of pixels or tokens. This avoids a pixel decoder,
  contrastive negative pairs, and hand-crafted view augmentations.

## Architectural differences

| Model family | Prediction space | Main limitation |
| --- | --- | --- |
| `MAE` / `VideoMAE` | Pixels | Models high-entropy visual detail |
| `LLaVA` / autoregressive VLMs | Text tokens | Loses physical detail not expressed in language |
| `I-JEPA` / `V-JEPA` | Abstract latent representations | Requires asymmetric training to avoid collapse |

JEPA uses a context encoder for visible patches, an EMA target encoder for
masked patches, and a narrow predictor conditioned on mask positions:

$$
\mathcal{L}_{\mathrm{JEPA}} =
\frac{1}{M}\sum_{j=1}^{M}
\left\|g_\phi(s_x,z_j)-\operatorname{sg}(s_{y_j})\right\|_2^2
$$

Stop-gradient targets, EMA weights, layer normalization, and semantic
multi-block masking prevent both branches from collapsing to the same constant
embedding.

## Headline results

- **ImageNet-1K:** `I-JEPA` ViT-H/14 reaches **79.3%** linear-probe accuracy
  (`81.1%` at 448px), versus **77.2%** for `MAE`, with less than 1,200 GPU
  hours.
- **Low-shot learning:** With 1% of ImageNet-1K labels, ViT-H/14 reaches
  **73.3%**, versus **67.0%** for `MAE` and **63.3%** for `data2vec`.
- **3D geometry:** On CLEVR depth prediction, `I-JEPA` scores **72.4%**,
  compared with **62.3%** for `DINO` and **62.8%** for `iBOT`.
- **Video dynamics:** `V-JEPA` ViT-H/16 reaches **71.4%** on
  Something-Something-v2, versus **35.8%** for OpenCLIP and **65.5%** for
  VideoMAE-L. It also reaches **82.1%** on Kinetics-400.

## Video links

- [16:9 video](https://drive.google.com/file/d/1KHqXXd_NWYdyKv5M6wlIne93B7nCBzjb/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1BP96FAxCyYqGO2cVel5huAODRSPpo4IM/view?usp=sharing)

## References

- Yann LeCun, *A Path Towards Autonomous Machine Intelligence* (2022)
- Mahmoud Assran et al., *Self-Supervised Learning from Images with a
  Joint-Embedding Predictive Architecture*, CVPR 2023
  ([arXiv:2301.08243](https://arxiv.org/abs/2301.08243))
- Adrien Bardes et al., *Revisiting Feature Prediction for Learning Visual
  Representations from Video* (2024)
  ([arXiv:2404.08471](https://arxiv.org/abs/2404.08471))
- [I-JEPA code and weights](https://github.com/facebookresearch/ijepa) ·
  [V-JEPA code and weights](https://github.com/facebookresearch/jepa)

*Created by Hrishikesh for RamanEffect.*  
*Tags: #JEPA #IJEPA #VJEPA #WorldModels #VisionLanguageModels #VLM #YannLeCun
#MetaAI #DeepLearning #ComputerVision #SelfSupervisedLearning #RamanEffect*
