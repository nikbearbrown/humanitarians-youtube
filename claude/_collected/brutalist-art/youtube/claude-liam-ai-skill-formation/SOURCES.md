# SOURCES — claude-liam-ai-skill-formation

## Primary source

**Shen, F. & Tamkin, A. (2026).** "How AI assistance impacts the formation of coding skills."
arXiv:2601.20245. Anthropic.
https://arxiv.org/abs/2601.20245

## Facts used from this source (with location)

| Fact | Source location |
|---|---|
| n = 52 developers | Section 3.1, participant inclusion criteria |
| All Python-experienced | Section 3.1 |
| None had prior Trio async library experience | Section 3.1, task design |
| Randomized assignment to AI-assisted vs. control | Study design (RCT) |
| Post-task quiz on concepts from the coding task | Section 3.2 |
| AI group task time: 23.0 min [20.6, 25.5] | Table 2 |
| Control group task time: 24.7 min [21.7, 27.6] | Table 2 |
| Task time p = 0.391 (not significant) | Table 2 |
| AI group quiz score: 50% [41, 59] | Table 2 (paper: 50.2%, rounded to 50%) |
| Control group quiz score: 67% [59, 72] | Table 2 (paper: 67.1%, rounded to 67%) |
| Quiz score p = 0.010 | Table 2 |
| Cohen's d = 0.738 | Table 2 |
| Biggest quiz gap in debugging competency | Section 4.2 |
| Six qualitative interaction modes identified | Section 4.3 |
| Generation-then-comprehension: n=2, ~24 min, ~86% | Figure 3 data points |
| Hybrid code-explanation: n=3, ~24 min, ~68% | Figure 3 data points |
| Conceptual inquiry: n=7, ~22 min, ~65% | Figure 3 data points |
| AI delegation: n=4, ~19.5 min, ~39% | Figure 3 data points |
| Progressive AI reliance: n=4, ~22 min, ~35% | Figure 3 data points |
| Iterative AI debugging: n=4, ~31 min, ~24% | Figure 3 data points |
| Conceptual inquiry second-fastest mode overall | Figure 3, x-axis |
| Caveats: n=52, short-term quiz, unknown long-term effects | Paper limitations section |
| Study used sidebar assistant, not agentic tool | Study design description |

## Editorial characterizations (not paper claims)

- "Nearly two letter grades" — 17 percentage points on a 100-point scale. Editorial gloss, not in the paper.
- Reference to Claude Code's "Learning" and "Explanatory" output styles — real product features, not from the study. Mentioned as viewer action recommendation only.
- "Getting painfully stuck is part of mastery" — editorial synthesis of the paper's conclusion, not a direct quotation.

## Figure construction notes

All three figures are rebuilt as native Remotion animations in the house design palette (cream #FAF9F5, warm ink #3D3929, terracotta #D97757). No screenshots of Anthropic's figures were used. All numeric values exactly match the paper's Table 2 and Figure 3 data.

- Figure 1 (StudyDesign): 4-stage pipeline; structure from Figure 1 of the paper.
- Figure 2 (TreatmentEffect): point-and-CI chart; values from Table 2.
- Figure 3 (UsageModes): scatter plot; values from Figure 3 of the paper.
