
## Week 2 — Research Framework and Technical Methodology

### Overview

This week, I focused on turning the initial literature review into a structured computational research problem. The work involved defining the research question, exploring suitable learning algorithms, and establishing criteria for evaluating whether immune-related patterns could remain consistent across different autoimmune diseases.

### Work Completed

### Research Question Development

Defined the initial research question:

**Can computational models identify shared immune dysfunctions and underlying mechanisms across RA, PsA, and SLE, and where do those models disagree?**

The objective was to go beyond identifying individual disease-associated patterns and investigate whether computational methods could capture similarities across multiple conditions.

### Technical Approach Exploration

- Investigated invariant representation learning as a potential approach to identifying patterns that remain stable across different datasets.
- Considered methods for separating shared immune-related variation from disease-specific and dataset-specific variation.
- Explored perturbation-based validation as a possible future direction for evaluating biological hypotheses.
- Considered reinforcement learning environments and simulation-based experimentation as potential longer-term research applications.

These methods were explored as research directions rather than presented as completed implementations.

### Evaluation Strategy

Established preliminary evaluation criteria focusing on:

- Reproducibility of identified patterns across independent datasets.
- Cross-disease consistency and model generalization.
- Sensitivity to differences in sample sizes and measurement technologies.
- Robustness to potential confounding factors.

### Findings and Outcomes

Developed a clearer technical research framework for ImmuneUnite.

The research indicated that identifying similar patterns across diseases is only the first step. Establishing whether those patterns are reliable requires additional validation and careful consideration of differences between datasets.

The availability of suitable data emerged as a major factor in determining which modeling approaches would be feasible.

### Hours Breakdown

| Research Activity | Estimated Hours |
|---|---:|
| Research question refinement and technical planning | 6 |
| Investigating computational approaches | 8 |
| Evaluation strategy and documentation | 8 |
| Weekly team meeting and preparation | 2 |
| **Total Estimated Workload** | **24** |

### Supporting Evidence

- [Week 2 — Research Progress Log](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/ImmuneUnite/lab-work-progress.md#week-2--research-question-and-technical-approach)
- [Week 2 — Progress Video](https://drive.google.com/drive/folders/16X-QPVS652EmjbDTiqbxRTN9EndfUhWa)

### Challenges

- Determining whether the available public datasets could support cross-disease modeling.
- Distinguishing biological similarities from technical variation.
- Establishing realistic validation requirements before selecting more complex learning algorithms.
