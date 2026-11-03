# Renewal request — Simbaremuteuro Chinombe

- **Current agreement:** 21 Aug — 30 Sep
- **Requested period:** 1 Oct — 30 Nov

- **Project:** Mycroft — Adaptive Model Routing & Inference Gateway
- **Repository:** https://github.com/nikbearbrown/mycroft
- **Branch:** `chinombesimbaremuteuro/adaptive-model-routing`

## What the current period produced

Five sprints of a measurement-first routing gateway. All evidence is in the
repository above, and every figure below traces to a logged row rather than an
estimate.

- An append-only logbook where every model call's cost, latency, tier and
  routing reason are recorded before the caller gets its answer  168 tests, no
  runtime dependencies.
- Six task types locked to evidence already in the repository, a rules router,
  and 24 fixtures hand-labelled and frozen before any model was run on them.
- A live sweep of the whole fixture set: 24 requests, 8% escalation, 0% failure,
  $0.00250, p50 393 ms. Escalated requests were 8% of requests and 23% of spend.
- A pairwise quality judge that runs every comparison twice with the answers
  swapped, so position bias appears as a recorded disagreement instead of a
  result. It established that judging a pair costs 2.4x producing it, which is
  why it stays out of the request path.
- Five STEM explainers on inference economics, three published/uploaded to youtube so far.

### Evidence

| Sprint | Commit | Drive | Video | Log |
|---|---|---|---|---|
| 1 — request logbook | [`b46d48e`](https://github.com/nikbearbrown/mycroft/commit/b46d48e14ad2da14c507af6a59e85cd40cd4cae8) | [folder](https://drive.google.com/drive/folders/1H2fjjURBSxWyUZ5dBAkl9Ced5ANGVGSJ) | [watch](https://www.youtube.com/watch?v=nC1xKKoPuUE) | [log](./08282026-mycroft-logbook/FRICTIONAL.md) |
| 2 — model connection | [`f8c80ee`](https://github.com/nikbearbrown/mycroft/commit/f8c80ee081c0cf1411b0dcc0592a06ec4d79a384) | [folder](https://drive.google.com/drive/folders/1pHXg01GKXl1-iEPKqCr3O4BUJwsPSCBk?usp=sharing) | not uploaded | [log](./09032026mycroft-gateway/FRICTIONAL.md) |
| 3 — policy, router, fixtures | [`68bbeb5`](https://github.com/nikbearbrown/mycroft/commit/68bbeb5d1ee5b7e53bd283d17dc516024a2b5589) | [folder](https://drive.google.com/drive/folders/1xOoXuHBwvOA8mb8O3YAUd3hiCSPezVJB) | [watch](https://www.youtube.com/watch?v=MiWZyDMCR50) | [log](./09102026mycroft-router/FRICTIONAL.md) |
| 4 — retry and first run | [`d235542`](https://github.com/nikbearbrown/mycroft/commit/d2355422cf45a7951881cc4547a2b90a5e266678) | [folder](https://drive.google.com/drive/folders/1OopER7YqxoKf_w_qwXM98Jh9C2Yxwm6l?usp=sharing) | [watch](https://www.youtube.com/watch?v=VndHWZ2dPFI) | [log](./09172026mycroft-retry/FRICTIONAL.md) |
| 5 — quality judging | [`2a002da`](https://github.com/nikbearbrown/mycroft/commit/2a002da9e20c6887e1cac7dbbeb45ba93cd16152) | [folder](https://drive.google.com/drive/folders/1qJOzaQNE3GbWStgf9_dqkrWMGw8rJnQ6?usp=sharing) | not yet recorded | [log](./09242026mycroft-Measure-quality/FRICTIONAL.md) |

## Stem Topics

| Week | Topic | Video | Drive | Log |
|---|---|---|---|---|
| [24–28 Aug](./08282026-whatismcp/) | What is MCP | [video](https://www.youtube.com/watch?v=a1tiMgiQDfg) | [drive](https://drive.google.com/drive/folders/1BS4mqXHacyxOIfFH9vQwKDVt2q36ZS23?usp=sharing) | [log](./08282026-whatismcp/FRICTIONAL.md) |
| [31 Aug – 4 Sep](./09032026how-kv-cache-works/) | How KV cache works | - | [drive](https://drive.google.com/drive/folders/1-H-vE7c3x-pJmIU_Jw5rjhPBydSJfA8q) | [log](./09032026how-kv-cache-works/FRICTIONAL.md) |
| [7–11 Sep](./09102026paged-attention/) | PagedAttention | [video](https://www.youtube.com/watch?v=0rRC3kx5Jd8) | [drive](https://drive.google.com/drive/folders/1xOoXuHBwvOA8mb8O3YAUd3hiCSPezVJB?usp=sharing) | [log](./09102026paged-attention/FRICTIONAL.md) |
| [14–18 Sep](./09172026prefill-decode/) | Prefill vs decode | [video](https://www.youtube.com/watch?v=G-BSNylji68&t=3s) | [drive](https://drive.google.com/drive/folders/1dNRtEobtVoOo96AsAAauUyMaR99WWjsT?usp=sharing) | [log](./09172026prefill-decode/FRICTIONAL.md) |
| [21–25 Sep](./09242026jev-speed/) | Why Jev is fast | - | [drive](https://drive.google.com/drive/folders/1LYJr3yRnV_77b5HQTvbN21b-z5r7EJEB?usp=sharing) | [log](./09242026jev-speed/FRICTIONAL.md) |

Weekly hours: [HOURS.md](HOURS.md). Weekly Frictional logs: one per work folder,
listed in [README.md](README.md).

## Plan for the requested period

Sprints 6–9, in order, each gating the next:

1. **Measure the scorer** (28 Sep – 2 Oct). Hand-score 30 answer pairs blind;
   report agreement per task type. If agreement is poor, report that quality
   cannot be measured reliably for that task rather than tuning the judge until
   it agrees.
2. **Baseline** (5–9 Oct). Every fixture on all three tiers, repeated runs, cost
   reported as a spread rather than a single figure.
3. **Decision** (12–16 Oct). Implement the break-even rule and decide against
   thresholds fixed in August: >20% cheaper at equal quality, <20% slower.
   "Don't ship" is an acceptable outcome and will be published as one.
4. **Build the chosen option** (19–23 Oct). Package it as a service other Mycroft
   projects can call or a rules table they can copy, with reliability testing and
   documentation for both audiences.
5. **Future Work** (from 26 Oct). Choose the next topic, propose and carry it out.

Reporting continues as it has: a dated Frictional log per work folder, weekly
hours, and a RUN_LOG entry plus findings in the project repository.

## Open items I am carrying

- Jev-speed upload
- The Sprint 5 RUN_LOG entry