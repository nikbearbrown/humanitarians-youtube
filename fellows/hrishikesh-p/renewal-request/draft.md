
# Fellowship Renewal Request

**Request:** Please renew my fellowship from **October 1, 2026** through **October 31, 2026**. My current agreement ends **September 30, 2026**. This summary covers the reporting period **August 22, 2026 to October 30, 2026**.

## Completed

- **Established the Raman spectroscopy project context.** Defined the Raman Effect and Raman spectroscopy, documented the use of AI/ML in Raman spectroscopy, and reviewed previous project work. Evidence: [Week 1 frictional log](../2026-09-04%20-%20RamanEffect/FRICTIONAL.md), including the linked 16:9 and 9:16 videos and task materials.
- **Built initial classification models.** Created and trained a baseline CNN and a ResNet, then explored data augmentation techniques. Evidence: [Week 2 frictional log](../2026-09-12%20-%20RamanEffect/FRICTIONAL.md), with links to both videos and the related Git commits.
- **Compared model approaches and investigated Raman-specific methods.** Tested 1D CNN, ResNet, and Transformer architectures for bacterial Raman spectra classification; reviewed RamanSPy preprocessing; and studied a GNN approach for SERS. Evidence: [Week 3 frictional log](../2026-09-18%20-%20RamanEffect/FRICTIONAL.md), [Week 4 frictional log](../2026-09-25%20-%20RamanEffect/FRICTIONAL.md), and the [GNN Raman spectroscopy paper](https://www.researchgate.net/publication/404553159_Graph_Neural_Network_in_Raman_Spectroscopy_to_Leverage_the_Performance_and_Interpretability_of_the_Classification).
- **Studied clinical Raman spectroscopy and transfer learning.** Reviewed a 1D ResNet approach for identifying bacterial isolates, antibiotic treatment groups, and MRSA versus MSSA, including transfer learning that reached 99.0% accuracy with limited patient data. Evidence: [Week 5 frictional log](../2026-10-02%20-%20RamanEffect/FRICTIONAL.md), the [Nature paper](https://www.nature.com/articles/s41467-019-12898-9), and the linked videos.
- **Evaluated sequential versus spatial models.** Tested a bidirectional LSTM on 1,000-wavenumber Raman spectra and documented its 3.33% test accuracy at random-chance level, then compared it with ResNet and Simple CNN results. Evidence: [Week 6 frictional log](../2026-10-09%20-%20RamanEffect/FRICTIONAL.md) and the linked videos.
- **Analyzed agent-scale software infrastructure.** Reviewed Anthropic's migration from Git to Scion and Antique, including changesets, recursive derived data, content-addressed checkout architecture, source-control benchmarks, and the use of Claude in development. Evidence: [Week 7 frictional log](../2026-10-16%20-%20RamanEffect/FRICTIONAL.md) and the linked videos.
- **Evaluated clinical treatment-group classification.** Mapped 30 bacterial reference isolates into 8 empiric treatment groups, compared CNN and ResNet accuracy on 3,000 Raman spectra, and analyzed clinically benign versus cross-treatment errors. Evidence: [Week 8 frictional log](../2026-10-23%20-%20RamanEffect/FRICTIONAL.md), [Week 8 commit](https://github.com/hspgit/RAMAN-Effect/commit/23883ad3b3bc587d719f898efbe74101bef97bb0), and the linked videos.
- **Analyzed CNN and ResNet architectures for Raman spectra.** Compared a shallow 6-stage CNN with a 25-layer 1D ResNet, documenting the effects of residual connections, pooling, receptive fields, parameter capacity, and overfitting on raw and processed bacterial Raman spectra. Evidence: [Week 9 frictional log](../2026-10-30%20-%20RamanEffect/FRICTIONAL.md), [Week 9 fact-check](../2026-10-30%20-%20RamanEffect/FACTCHECK.md), and the linked videos.

## Hours Status

20 hours recorded for each documented week, for a total of **180 hours across nine documented weeks**.

## Degree Relevance and Supervision

This work directly supports my Master of Science in Computer Science (MSCS) degree through applied machine learning, deep learning, data augmentation, signal classification, scientific computing, and research communication. **Project supervisor:** Edward M. Olano.

## Authorization

F1 - OPT

## Next Period

Proposed deliverable: document a reproducible comparison of the CNN, ResNet, Transformer, preprocessing, and data-augmentation approaches, and write sections for the research paper by **October 31, 2026**.

## Outstanding Issues

- None

## Weekly Evidence Index

| Week / dates | Actual hours | Video links | Log and work evidence |
| --- | ---: | --- | --- |
| Week 1: September 4, 2026 | 20 | [16:9](https://drive.google.com/file/d/1r-kp4AmVq7jagd_hE_RYkS_MG-ncFryT/view?usp=drive_link) · [9:16](https://drive.google.com/file/d/1FkoclIif7jndW5vlq19XgV2acuOrKKxB/view?usp=drive_link) | [Dated log](../2026-09-04%20-%20RamanEffect/FRICTIONAL.md) · [Week 1 commit](https://github.com/hspgit/RAMAN-Effect/commit/a6fde58dcda69f8289689b4902ddc6fcd310a1c6) |
| Week 2: September 12, 2026 | 20 | [9:16](https://drive.google.com/file/d/165BQpd0I57LtkrU-O201GBXlG02lgXDD/view?usp=drive_link) · [16:9](https://drive.google.com/file/d/10yeSZjYiqBUnXhloul43senjBD6UcY2k/view?usp=drive_link) | [Dated log](../2026-09-12%20-%20RamanEffect/FRICTIONAL.md) · [Week 2 commit](https://github.com/hspgit/RAMAN-Effect/commit/4f19d70d1eccfcc99bb7c2f04c1c101e4f7553a4) |
| Week 3: September 18, 2026 | 20 | [9:16](https://drive.google.com/file/d/1mddrZIQlIJbJlc0UilCHjJCPs7mcKVbQ/view?usp=drive_link) · [16:9](https://drive.google.com/file/d/11U7lbnUZMGASTv3i7q85IiV51brc7Ke1/view?usp=drive_link) | [Dated log](../2026-09-18%20-%20RamanEffect/FRICTIONAL.md) · [Week 3 commit](https://github.com/hspgit/RAMAN-Effect/commit/084e4b3736d5f81af5fcfa71f13036ef9ca261ba) |
| Week 4: September 25, 2026 | 20 | [Preprocessing video](https://drive.google.com/drive/folders/1Ykhbt4J7RBEY2AsfH2TOdTMzykfHOOu0?usp=drive_link) · [GNN video](https://drive.google.com/drive/folders/1AoB0THXTlO-7Ki7lNtHKoEXm5sZHfqq?usp=drive_link) | [Dated log](../2026-09-25%20-%20RamanEffect/FRICTIONAL.md) · [GNN paper](https://www.researchgate.net/publication/404553159_Graph_Neural_Network_in_Raman_Spectroscopy_to_Leverage_the_Performance_and_Interpretability_of_the_Classification) |
| Week 5: October 2, 2026 | 20 | [16:9](https://drive.google.com/file/d/1wbHRC--hcMLumE4XGLJZSv4KMJ8mZ01s/view?usp=drive_link) · [9:16](https://drive.google.com/file/d/1ql_IYbLr-fX-8Fi8Kog37vFWks64ELmH/view?usp=drive_link) | [Dated log](../2026-10-02%20-%20RamanEffect/FRICTIONAL.md) · [Nature paper](https://www.nature.com/articles/s41467-019-12898-9) · No Git commit; paper review only |
| Week 6: October 9, 2026 | 20 | [16:9](https://drive.google.com/file/d/1xUevGIxN8gknxQ1OYP6nyflM656rwBsS/view?usp=drive_link) · [9:16](https://drive.google.com/file/d/1PlKiuVd40nQ8oarqcJW-RUDckAGzA0a2/view?usp=drive_link) | [Dated log](../2026-10-09%20-%20RamanEffect/FRICTIONAL.md) · [Week 6 commit](https://github.com/hspgit/RAMAN-Effect/commit/faf0410d432ec99f702ceb5c23d591017ad6cc65) |
| Week 7: October 16, 2026 | 20 | [16:9](https://drive.google.com/file/d/1xz1x9fcxEY6vCJDcc-OE6IVJkftIRW4m/view?usp=sharing) · [9:16](https://drive.google.com/file/d/14iKqr9zQUYYMyc6btWhrs1l7shz42fl4/view?usp=drive_link) | [Dated log](../2026-10-16%20-%20RamanEffect/FRICTIONAL.md) · Source-control and agent-scale infrastructure review |
| Week 8: October 23, 2026 | 20 | [16:9](https://drive.google.com/file/d/1ZEEaDkIRnRjdvGCCnVK9SCFeP7F39OVC/view?usp=drive_link) · [9:16](https://drive.google.com/file/d/1cfbvhZzKi9g0oPb6D0GtltLuKUWPqcNK/view?usp=drive_link) | [Dated log](../2026-10-23%20-%20RamanEffect/FRICTIONAL.md) · [Week 8 commit](https://github.com/hspgit/RAMAN-Effect/commit/23883ad3b3bc587d719f898efbe74101bef97bb0) |
| Week 9: October 30, 2026 | 20 | [16:9](https://drive.google.com/file/d/1ZKckHZmxm6UxpkTayt2t3gr6t7ZN2UjD/view?usp=sharing) · [9:16](https://drive.google.com/file/d/10tM5jfvwokSynajs2lVfM1YthImbrA86/view?usp=sharing) | [Dated log](../2026-10-30%20-%20RamanEffect/FRICTIONAL.md) · [Fact-check](../2026-10-30%20-%20RamanEffect/FACTCHECK.md) |
