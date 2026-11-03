# Simbaremuteuro Chinombe — Humanitarians AI Fellow

- **Role:** AI engineer
- **Project:** Mycroft — Adaptive Model Routing
- **Repository:** https://github.com/nikbearbrown/mycroft
- **Branch:** `chinombesimbaremuteuro/adaptive-model-routing`
- **Group / supervisor:** Mycroft / Shradha Katte
- **Agreement period:** 21 Aug — 30 Sep

## Research question

Can an AI system route each request to the **cheapest model that still answers
it correctly**, and can that saving be *measured* rather than assumed?

Mycroft currently picks models four incompatible ways, hardcoded across its
scripts. This project builds one gateway every request passes through, records
what each request actually cost and how good the answer was, and then decides
against thresholds fixed in advance whether adaptive routing is worth shipping.

## Project work

| Week | Work | Result | Evidence | Log |
|---|---|---|---|---|
| [24–28 Aug](./08282026-mycroft-logbook/) | Request logbook | Append-only record of every model call. Separates a logical request from its physical attempts | [video](https://www.youtube.com/watch?v=nC1xKKoPuUE) · [drive](https://drive.google.com/drive/folders/1H2fjjURBSxWyUZ5dBAkl9Ced5ANGVGSJ) · [commit `b46d48e`](https://github.com/nikbearbrown/mycroft/commit/b46d48e14ad2da14c507af6a59e85cd40cd4cae8) | [log](./08282026-mycroft-logbook/FRICTIONAL.md) |
| [31 Aug – 4 Sep](./09032026mycroft-gateway/) | Model connection | One client for three model tiers | - · [drive](https://drive.google.com/drive/folders/1pHXg01GKXl1-iEPKqCr3O4BUJwsPSCBk?usp=sharing) · [commit `f8c80ee`](https://github.com/nikbearbrown/mycroft/commit/f8c80ee081c0cf1411b0dcc0592a06ec4d79a384) | [log](./09032026mycroft-gateway/FRICTIONAL.md) |
| [7–11 Sep](./09102026mycroft-router/) | Policy, router, test set | Six task types locked to evidence in the repo; rules router; 24 fixtures hand-labelled before any model ran, then frozen by SHA-256. | [video](https://www.youtube.com/watch?v=MiWZyDMCR50) · [drive](https://drive.google.com/drive/folders/1xOoXuHBwvOA8mb8O3YAUd3hiCSPezVJB) · [commit `68bbeb5`](https://github.com/nikbearbrown/mycroft/commit/68bbeb5d1ee5b7e53bd283d17dc516024a2b5589) | [log](./09102026mycroft-router/FRICTIONAL.md) |
| [14–18 Sep](./09172026mycroft-retry/) | Retry and first full run | One retry on a stronger model, never a chain. | [video](https://www.youtube.com/watch?v=VndHWZ2dPFI&t=10s) · [drive](https://drive.google.com/drive/folders/1OopER7YqxoKf_w_qwXM98Jh9C2Yxwm6l?usp=sharing) · [commit `d235542`](https://github.com/nikbearbrown/mycroft/commit/d2355422cf45a7951881cc4547a2b90a5e266678) | [log](./09172026mycroft-retry/FRICTIONAL.md) |
| [21–25 Sep](./09242026mycroft-Measure-quality/) | Quality judging | A stronger model compares two answers, each pair judged twice with the answers swapped. | - · [drive](https://drive.google.com/drive/folders/1qJOzaQNE3GbWStgf9_dqkrWMGw8rJnQ6?usp=sharing) · [commit `2a002da`](https://github.com/nikbearbrown/mycroft/commit/2a002da9e20c6887e1cac7dbbeb45ba93cd16152) | [log](./09242026mycroft-Measure-quality/FRICTIONAL.md) |

**Tests:** 168 passing, no runtime dependencies.
**Every cost figure above traces to a logged row**, not an estimate — see
`logs/gateway/runs/` and `scripts/gateway/bench/results/` in the Mycroft repo.

## STEM Topics

Research and diagrams mine; beat sheet and production by Claude from them.

| Week | Topic | Evidence | Log |
|---|---|---|---|
| [24–28 Aug](./08282026-whatismcp/) | What is MCP | [video](https://www.youtube.com/watch?v=a1tiMgiQDfg) · [drive](https://drive.google.com/drive/folders/1BS4mqXHacyxOIfFH9vQwKDVt2q36ZS23?usp=sharing) | [log](./08282026-whatismcp/FRICTIONAL.md) |
| [31 Aug – 4 Sep](./09032026how-kv-cache-works/) | How KV cache works | - · [drive](https://drive.google.com/drive/folders/1-H-vE7c3x-pJmIU_Jw5rjhPBydSJfA8q) | [log](./09032026how-kv-cache-works/FRICTIONAL.md) |
| [7–11 Sep](./09102026paged-attention/) | PagedAttention | [video](https://www.youtube.com/watch?v=0rRC3kx5Jd8) · [drive](https://drive.google.com/drive/folders/1CY_suzRRK4f05C5OeNKXm-5Bw6Ynhv1H?usp=sharing) | [log](./09102026paged-attention/FRICTIONAL.md) |
| [14–18 Sep](./09172026prefill-decode/) | Prefill vs decode | [video](https://www.youtube.com/watch?v=G-BSNylji68) · [drive](https://drive.google.com/drive/folders/1dNRtEobtVoOo96AsAAauUyMaR99WWjsT?usp=sharing) | [log](./09172026prefill-decode/FRICTIONAL.md) |
| [21–25 Sep](./09242026jev-speed/) | Why Jev is fast | - · [drive](https://drive.google.com/drive/folders/1LYJr3yRnV_77b5HQTvbN21b-z5r7EJEB?usp=sharing) | [log](./09242026jev-speed/FRICTIONAL.md) |

## Next steps

- **Sprint 6 (28 Sep – 2 Oct):** hand-score 30 answer pairs blind and measure how
  often the automatic judge agrees. Until that number exists, no judged quality
  figure is quotable.
- **Sprint 7 (5–9 Oct):** baseline — every fixture on all three tiers, several
  runs each, since verdicts change between runs.
- **Sprint 8 (12–16 Oct):** the break-even router, and the ship / don't-ship
  decision against thresholds set in August: ≥20% cheaper at equal quality, ≤20%
  slower.
- **Sprint 9 (19–23 Oct):** package whichever version won, plus reliability
  testing and documentation.

## Hours and renewal

- [Weekly hours](HOURS.md)
- [Renewal request](RENEWAL.md)