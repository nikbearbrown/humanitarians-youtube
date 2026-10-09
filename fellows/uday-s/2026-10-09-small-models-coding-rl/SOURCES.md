# SOURCES - One Model, Three Numbers

Two primary sources. No aggregator page, vendor roundup or newsletter summary
was used for any figure on screen.

| On screen | Beat | Source |
|---|---|---|
| 42.2 pass@1 on SWE-bench Verified | B01, B04, B05, B06, B07 | DeepSWE-Preview release (Agentica / Together AI) |
| 57.9 Best@8 | B04 | same |
| 59.0 Best@16, verifier-selected | B01, B04, B06, B07, B08 | same |
| 71.0 Pass@16, oracle upper bound | B01, B04 | same |
| Qwen3-32B base, RL only, modified GRPO | B03 | same |
| 4,500 tasks from an R2E-Gym subset | B03 | same |
| benchmark repositories filtered out of training | B03 | same (sympy named as the example) |
| 64 x H100, six days | B03 | same |
| R2E-Gym scaffold, 64k context, 100 steps | B05 | same |
| Devstral-Small 24B at 46.6, OpenHands | B05, B06 | same - the release's comparison table |
| Skywork-SWE 32B at 47.0 (Best@8) and R2EGym-Agent 32B at 34.4 | B06 | same table |
| SWE-Agent-LM-32B at 40.2 pass@1 | B06, B07 | SWE-smith abstract (and the DeepSWE table agrees) |
| SWE-smith: 50k instances, 128 GitHub repositories | B07 | SWE-smith abstract |

## Reference links

- DeepSWE-Preview release - https://www.together.ai/blog/deepswe
- DeepSWE-Preview model card - https://huggingface.co/agentica-org/DeepSWE-Preview
- SWE-smith (Yang et al.) - https://arxiv.org/abs/2504.21798

## Why the aggregators were refused

The first search for this topic returned a dozen pages of the form "best open
models for coding agents in 2026". Several quoted scores with no scaffold, and
at least two quoted a best-of-N figure beside another model's single-attempt
figure without saying so. That is precisely the failure this reel is about, so
using one as a source would have been self-refuting. Every number here was
re-read from the release or the paper.

This is the same discipline that caught a wrong figure in the previous STEM reel
on HOPE, where a search summary had slid one row of a results table.

## The one internal inconsistency

The DeepSWE release prints the hybrid test-time-scaling score as 59% in its
table and figures and 59.2% in its conclusion. The reel uses 59.0 - the table
figure - because the table is where the scaffold and setting columns live. The
difference changes nothing and is recorded in FACTCHECK.md rather than hidden.

## Claims NOT sourced here, and therefore not made

- Nothing about closed models - none are compared.
- Nothing about dollar cost, latency or tokens per second; the sources do not
  provide comparable figures, so "16x inference" is a count of trajectories and
  is labelled as such.
- Nothing about which model a viewer should use.
