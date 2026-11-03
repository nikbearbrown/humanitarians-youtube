# Maitri Pasale. — Humanitarians AI Fellow

- **Role:** AI Software Engineer
- **Project:** RL_Environment — Pi agent memory, then Policy Decompilation for Optimus
- **Repository:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/maitri-p
- **GitHub:** [@maitripasale](https://github.com/maitripasale)
- **Supervisors:** Dev Shah, Dhruv Patel, Shilpa V G
- **Agreement period:** 11 Sep — 31 Oct 2026

## Research question

Can an AI agent carry **lessons from earlier sessions** into new ones, and does
that memory make it work better in a way that is *measured* rather than assumed?

Pi starts every session from zero. This project gives it an external memory of
lessons saved from practice runs, then compares fresh runs with and without
those lessons on questions it has never seen. In Week 5 the work moved to a new
track: Policy Decompilation, turning a small trained model's choices into
readable rules.

## Project work

| Week | Work | Result | Evidence | Log |
|---|---|---|---|---|
| [21–27 Sep](./2026-09-21-pi-week1-onboarding/) | How Pi works | Mapped Pi's prompt → tool → result loop and where memory could fit; added a Jupyter tool so Pi can run Python. | [drive](https://drive.google.com/drive/folders/1mainiFrl4-LOSw0kgNHxgwPRx3mCKdC_) · [code](https://github.com/maitripasale/pi-memory-search/blob/main/extensions/jupyter-repl.ts) | [log](./2026-09-21-pi-week1-onboarding/FRICTIONAL.md) |
| [28 Sep – 4 Oct](./2026-10-03-pi-agent-memory/) | Memory systems | Scoped two memory types — procedural (how to do it) and metacognitive (what went wrong) — and how to evaluate them. | [drive](https://drive.google.com/drive/folders/18lEGqobYIRiYHgXF4oMB68NmZFddJH3V) · [code](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/memory.py) | [log](./2026-10-03-pi-agent-memory/FRICTIONAL.md) |
| [5–11 Oct](./2026-10-09-pi-memory-pilot/) | Memory pilot | 3 practice → 6 unseen questions, four conditions. All answers correct; mean tool calls 6.00 / 4.33 / 5.00 / 6.83. Fixed a scoring bug across all conditions. | [drive](https://drive.google.com/drive/folders/1OIblBvPv67TWI_ix_2MRl98TlqTI9bzN) · [report](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/MULTIHOP_EXPERIMENT.md) | [log](./2026-10-09-pi-memory-pilot/FRICTIONAL.md) |
| [12–18 Oct](./2026-10-23-pi-memory-task-review/) | Task-level review | One hard task (12 calls, 2 errors → 3 calls with memory) drove most of the gain. Retrieving a lesson at the right time matters as much as storing it. | [drive](https://drive.google.com/drive/folders/1UO2dYgzjzEDvV-CASwsnMpC9BqfFAqqt) · [analysis](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/WEEK3_ANALYSIS.md) | [log](./2026-10-23-pi-memory-task-review/FRICTIONAL.md) |
| [19–25 Oct](./2026-10-23-policy-decompilation-scope/) | Policy Decompilation scope | Chose first measures: action agreement, task performance, rule simplicity. Scoping only — no model trained yet. | [drive](https://drive.google.com/drive/folders/1pJitpxHlOK22vwyq9DDNVPpdGVnMnJp3) | [log](./2026-10-23-policy-decompilation-scope/FRICTIONAL.md) |

**One repetition per condition** — the pilot numbers are early signals, not a proven improvement.

## STEM Topics

| Week | Topic | Evidence | Log |
|---|---|---|---|
| [21–27 Sep](./2026-10-23-noise-cancelling-headphones/) | Noise cancellation | [drive](https://drive.google.com/drive/folders/1mainiFrl4-LOSw0kgNHxgwPRx3mCKdC_) | [log](./2026-10-23-noise-cancelling-headphones/FRICTIONAL.md) |
| [28 Sep – 4 Oct](./2026-10-02-agents-use-tools/) | How agents use tools | [drive](https://drive.google.com/drive/folders/18lEGqobYIRiYHgXF4oMB68NmZFddJH3V) | [log](./2026-10-02-agents-use-tools/FRICTIONAL.md) |
| [5–11 Oct](./2026-10-23-dynamodb-hot-partition/) | DynamoDB hot partitions | [drive](https://drive.google.com/drive/folders/1OIblBvPv67TWI_ix_2MRl98TlqTI9bzN) | [log](./2026-10-23-dynamodb-hot-partition/FRICTIONAL.md) |
| [12–18 Oct](./2026-10-23-lambda-cold-start/) | AWS Lambda cold starts | [drive](https://drive.google.com/drive/folders/1UO2dYgzjzEDvV-CASwsnMpC9BqfFAqqt) | [log](./2026-10-23-lambda-cold-start/FRICTIONAL.md) |
| [19–25 Oct](./2026-10-23-gps-how-it-works/) | How GPS works | [drive](https://drive.google.com/drive/folders/1pJitpxHlOK22vwyq9DDNVPpdGVnMnJp3) | [log](./2026-10-23-gps-how-it-works/FRICTIONAL.md) |

## Next steps

- Set up a small, reproducible Policy Decompilation baseline — a trained model on CartPole.
- Record the model's decisions across states and extract a first set of readable rules.
- Compare the rules with the model on action agreement, task performance and simplicity; document where they fail.
- Use the findings to define what this can explain about model behavior before applying it to Optimus.

## Hours and renewal

- [Weekly hours](HOURS.md)
- [Renewal request](./renewal-requests/2026-10-23-renewal-request.md)
