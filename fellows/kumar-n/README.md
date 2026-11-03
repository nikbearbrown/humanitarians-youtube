# Kumar N. — Humanitarians AI Fellow

| | |
|---|---|
| **Name** | Kumar Karthik Ankasandra Naveen |
| **Role** | AI/ML Engineer |
| **Project** | The RAMAN Effect — *Machine Learning for Surface-Enhanced Raman Spectroscopy: From Preprocessing to Deployment* (Paper 2 of 3) |
| **Supervisor** | Edward Olano |
| **Co-author** | Kunal |
| **GitHub** | [@kumarkarthik23](https://github.com/kumarkarthik23) |
| **Paper draft** | [Google Doc](https://docs.google.com/document/d/1yMAE0CghIcEXnI67sW6jCQ1tVSY3qqnLF1kgoWTtlKo/edit) |
| **Agreements** | 19 June – 31 July 2026 (previous) · 1 August – 31 October 2026 (current) |

## Overview

This folder documents my work on Paper 2 of the RAMAN Effect series, a review
of machine learning methods for surface-enhanced Raman spectroscopy (SERS).

The paper's first draft was AI-generated. It covered every relevant method but
only defined each one, and several of its references either did not exist or
did not support the claims attached to them. The work recorded here rebuilds
the paper section by section. Every claim is checked against its source,
unsupported figures are removed or properly sourced, and every section is
rewritten to answer the three questions set out in the team's guidelines:
what has been done, why it works or fails, and what the evidence supports
recommending.

**Research question.** Can a review of machine learning for SERS separate
what the literature has demonstrated from what it only claims, and state
clearly which methods are ready for deployment and which are not?

## Contents

Each work folder contains its own `FRICTIONAL.md`, alongside the video
source files and, for Section 4, a fact-check and a record of AI use.

| Type | Folder | Subject |
|---|---|---|
| Project update | `08312026-5weeks-update/` | Sections 2.4–2.6 and 3.3–3.5 |
| Project update | `09132026-2weeks-update/` | Section 4.2 |
| Project update | `09272026_ProjectUpdate/` | Section 4.4 |
| Project update | `10102026_ProjectUpdate/` | Section 4.5 |
| Project update | `10182026_ProjectUpdate/` | Section 4.6 |
| STEM topic | `08312026-sers-ai-topic/` | SERS |
| STEM topic | `09132026-sers-ml-ai-topic/` | SERS and machine learning |
| STEM topic | `09272026_SERS_Hotspots/` | SERS hot spots |
| STEM topic | `10102026_SERS_Quantitative/` | Quantitative SERS |
| STEM topic | `10182026_SERS_GoldVsSilver/` | Gold vs. silver substrates |
| Previous agreement | `07312026-the-tier-that-grades-papers/` | The paper's three-tier validation framework |

## 1. Project Work

Sections were divided at random between my co-author Kunal and me. Each
section followed a two-week cycle: one week of research and reference
verification, followed by one week of rewriting.

| Period | Sections | Key results | Video | Folder | Log |
|---|---|---|---|---|---|
| 2–29 Aug | 2.4–2.6, 3.3–3.5 | Unsourced 10–30 point performance-gap figure removed; PCA data-leakage rule added; mismatched summary-table citation removed; PLSR citation gap closed | [watch](https://drive.google.com/file/d/19nsmO86GMq5KFVTzu0dVtudDOF0Gy6Nx/view?usp=share_link) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/08312026-5weeks-update) | [log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/08312026-5weeks-update/FRICTIONAL.md) |
| 30 Aug – 12 Sep | 4.2 Transformer architectures | Closing recommendation added; Wang et al.'s 100% figure scoped to its test conditions; transformer–CNN comparison gap closed with a peer-reviewed benchmark | [watch](https://drive.google.com/file/d/1kEl2exl4Ir8VLZ_uphFgBxbwqUb0xIfP/view?usp=share_link) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/09132026-2weeks-update) | [log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/09132026-2weeks-update/FRICTIONAL.md) |
| 13–26 Sep | 4.4 Hybrid and multi-task architectures | Uncited "often helps" claim replaced with a leakage-audited comparison; two-model default established; U-55 author attribution corrected | [watch](https://drive.google.com/file/d/1PrcdTqEzoUHAYqTdwhzb7Wx5dqrQTFne/view?usp=share_link) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/09272026_ProjectUpdate) | [log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/09272026_ProjectUpdate/FRICTIONAL.md) |
| 27 Sep – 10 Oct | 4.5 Training with limited data | Strategy matched to the bottleneck (spectra vs. labels); uncited gap claim replaced with SMAE and SemiRaman results, scoped to conventional Raman | [watch](https://drive.google.com/file/d/1IC8uWNKcDZ4Jg6oQ6XFIkkvC-ZqOvPHy/view?usp=share_link) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/10102026_ProjectUpdate) | [log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/10102026_ProjectUpdate/FRICTIONAL.md) |
| 11–24 Oct | 4.6 Deployment considerations | Compression reframed with an expected accuracy cost; interpretability updated with CRIME and GRASS; generalization claim corrected following early SERS cross-device work | [watch](https://drive.google.com/file/d/1Y8sDrNScZtMCfVsPoFP1K1vd1Iab8vYz/view?usp=share_link) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/10182026_ProjectUpdate) | [log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/10182026_ProjectUpdate/FRICTIONAL.md) |

**Finding across Section 4.** In Sections 4.2, 4.4, 4.5 and 4.6, the
strongest available evidence came from conventional Raman spectroscopy or
from outside spectroscopy altogether. Each revision states that scope beside
the result rather than presenting it as SERS evidence, which identifies the
missing SERS-specific studies as open research gaps.

## 2. STEM Topics

One explainer topic was produced per two-week period. Research and topic
selection were my own; beat sheets and scene files were produced with Claude
from my material.

| Period | Topic | Video | Folder |
|---|---|---|---|
| 16–29 Aug | SERS | [watch](https://drive.google.com/file/d/180PHlgNXd90HQq9GJuo-wJcf8qXuWlKy/view?usp=sharing) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/08312026-sers-ai-topic) |
| 30 Aug – 12 Sep | SERS and machine learning | [watch](https://drive.google.com/file/d/1nbLBLm234VWkuisV_x03jWOTD3TinQv8/view?usp=sharing) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/09132026-sers-ml-ai-topic) |
| 13–26 Sep | SERS hot spots | [watch](https://drive.google.com/file/d/10A_QiL5l9JpY2qAMQzCPBMKTcZWNeg5q/view?usp=sharing) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/09272026_SERS_Hotspots) |
| 27 Sep – 10 Oct | Quantitative SERS | [watch](https://drive.google.com/file/d/1pRcUTaUBYhUdcPrXyAtZbyAL4MVrQjoW/view?usp=sharing) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/10102026_SERS_Quantitative) |
| 11–24 Oct | Gold vs. silver substrates | [watch](https://drive.google.com/file/d/1D0d2GzZ723jzOL4jCZhWTYuTfFDFoOGl/view?usp=sharing) | [open](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/10182026_SERS_GoldVsSilver) |

## 3. Previous Agreement

*The Tier That Grades the Papers* (`07312026-the-tier-that-grades-papers/`)
was produced on 31 July 2026, at the close of the previous agreement. It
explains the paper's three-tier validation framework, places published
studies within it, and describes how the problems in the first draft were
identified. It is not counted in the current period's hours.

## 4. Use of AI

- **Paper:** the first draft was AI-generated. During the rewrite, AI was
  used mainly to locate relevant papers. I read each paper myself, used AI to
  test whether my reading was sound, and rewrote each section against the
  team's guidelines.
- **Videos:** beat sheets, scene files and fact-checks were written by Claude
  from information I provided, and reviewed by me.
- **Documentation:** the frictional logs were drafted with Claude from my
  materials, and reviewed and corrected by me.

## 5. Next Steps

Renewal is requested from 1 November 2026. The full plan is set out in
[RENEWAL.md](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/RENEWAL.md).

| Dates | Stage |
|---|---|
| 1–14 Nov | Section 5, Continuous Monitoring Systems: research, then rewrite |
| 15–28 Nov | Section 6, Conclusion: rewrite to reflect the revised sections |
| 29 Nov – 5 Dec | Reference audit: verify every citation and author list against its source and DOI |
| 6–12 Dec | Convert the paper to LaTeX in Overleaf; number citations; add figures |
| 31 Dec | Submit the full draft to Professor Brown |

## 6. Frictional Logs

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.

The logs for the current agreement period were written after the work, from the
videos, fact-checks and paper drafts, and each is labelled as backfilled.

## 7. Hours and Renewal

- [Hours report](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/HOURS.md)
- [Renewal request](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/kumar-n/RENEWAL.md)
