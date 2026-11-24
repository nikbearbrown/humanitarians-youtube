
## Week 4 — Machine Learning Implementation and Statistical Validation

### Overview

This week focused on developing and evaluating the first machine learning baseline for ImmuneUnite, investigating shared and disease-specific immune patterns across RA, PsA, and SLE.

### Key Contributions and Outcomes

- **Data Processing and Analysis:** Prepared gene-expression datasets and conducted statistical comparisons to investigate disease-associated patterns across RA, PsA, and SLE.
- **Machine Learning Development:** Implemented an L2-regularized logistic regression baseline using immune-related gene-module scores.
- **Model Evaluation:** Evaluated within-cohort performance, statistical significance, and cross-disease generalization through permutation testing and sensitivity analysis.
- **Research Findings:** Achieved AUROC scores of 0.71 for RA, 0.52 for PsA, and 0.80 for SLE. Identified candidate shared associations, while cross-disease transfer showed no statistically significant generalization.
- **Optimus AI-Assisted Research:** Used Optimus AI to support technical research, explore modeling approaches, and review evaluation challenges.
- **Future Research Exploration:** Investigated potential applications of reinforcement learning environments and AI-supported autoimmune disease education.


### Hours Breakdown

| Activity | Hours |
|---|---:|
| Data preparation and statistical analysis | 7 |
| Machine learning baseline implementation | 8 |
| Model evaluation and validation | 9 |
| Research documentation and further exploration | 4 |
| Weekly team meeting preparation | 2 |
| **Total** | **30** |


### Supporting Evidence

- [Week 4 — Research Progress Log](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/ImmuneUnite/lab-work-progress.md)
- [Milestone 1 — Implementation Commit](https://github.com/Nenyax-AI/team-work/commit/fda487e)
- [Machine Learning Baseline Code](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/ImmuneUnite/models/milestone1/03_baseline_models.py)
- [Baseline Evaluation Results](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/ImmuneUnite/models/milestone1/results/baseline_results.csv)
- [Cross-Disease Transfer Results](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/ImmuneUnite/models/milestone1/results/transfer_two_sided.csv)
- [Week 4 — Progress Video](https://drive.google.com/drive/folders/1DTkCh6odPrf35cVPCxtu6sZan5bqCFSZ)

### Challenges

- **Cross-Disease Generalization:** Model performance did not transfer reliably between diseases, indicating limitations in the current baseline.
- **Confounding Factors:** Treatment-related effects in the RA dataset and differences in blood-cell composition complicated biological interpretation.
- **Dataset Constraints:** Small PsA cohort size and differences in measurement technologies limited statistical confidence and comparability.
