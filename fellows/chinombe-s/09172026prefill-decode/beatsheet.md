# Beat Sheet — Prefill vs. Decode

**Channel:** claude-hai · **Persona:** Simba · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer · **Aspect:** 16:9 (3840×2160) · **Total runtime:** 4:02 (242.05s, Kokoro ground truth)

| Beat | Act | Timestamp | Duration | Pattern | Note |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 21.48s | `ClaudeComposerAsk` | Cold open — the two-jobs question |
| B01 | SUMMARY | 0:21 | 15.07s | `ClaudeStatement` | BLUF — prefill vs. decode in one line |
| B02 | STRUCTURE | 0:36 | 22.03s | `ParallelPass` **(new)** | Fan-in/fan-out diagram — one parallel pass over all prompt tokens |
| B03 | REASONING | 0:58 | 30.60s | `FactStack` | Why the bottleneck flips — arithmetic intensity |
| B04 | STRUCTURE | 1:29 | 23.06s | `AutoregressiveLoop` **(new)** | Loop-back diagram — decode's one-token-at-a-time cycle, growing KV cache |
| B05 | RESULTS | 1:52 | 19.08s | `DataTable` | TTFT vs. TPOT — what gets measured |
| B06 | REASONING | 2:11 | 22.61s | `FactStack` | What goes wrong sharing one GPU |
| B07 | FINDINGS | 2:33 | 24.05s | `FindingPair` | Fix one — chunked prefill (Sarathi-Serve, OSDI 2024) |
| B08 | FINDINGS | 2:57 | 23.86s | `FindingPair` | Fix two — disaggregated serving (DistServe, OSDI 2024) |
| B09 | SUMMARY | 3:21 | 24.41s | `ClaudeVerdictArtifact` | Verdict — two jobs, two bottlenecks, two fixes |
| B10 | NEXT STEPS | 3:46 | 11.62s | `ClaudeComposerAsk` | Your Turn — which clock is stuck |
| B11 | OUTRO | 3:57 | 4.18s | `ClaudeTitleOutro` | Sign-off |

## GATE L — component search log

Re-run explicitly for this build after the first draft leaned on reused text-card components (`TwoWayCompare` for B02, `RouterFlow` for B04) that were accurate but not actual diagrams. Searched the shared library for: (1) anything drawing fan-in from N inputs into one block and fan-out to M outputs — nothing found (`RouterFlow` is single-path-plus-one-branch, `PageTable` is 1:1 reordering, `SharedBlocks` fans out only, never in); (2) anything drawing a feedback/loop-back arrow — nothing found (every existing motion pattern is forward-only). Authored two new components to fill both gaps:

- **`ParallelPass`** (B02) — N input token boxes converge via SVG lines into one wide central "pass" block, which fans back out into the KV-cache/first-token outputs. Built for prefill's actual shape: many-in, one-simultaneous-compute, few-out.
- **`AutoregressiveLoop`** (B04) — three boxes (in → pass → out) in a row, connected by straight arrows, with a curved SVG path looping from the last box back to the first (dash-offset draw-in animation), plus a growing row of KV-cache blocks underneath, newest block always highlighted. Built for decode's actual shape: a closed loop, one cycle per output token.

Both passed `tsc --noEmit` clean, both required a second pass to satisfy FILL-THE-CANVAS (rescaled vertical proportions — see process notes), both confirmed correct in isolated QC stills and in the fully compiled master.

## Sources
- Agrawal et al., "Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve," OSDI 2024. [arXiv:2403.02310](https://arxiv.org/abs/2403.02310)
- Zhong et al., "DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving," OSDI 2024. [arXiv:2401.09670](https://arxiv.org/abs/2401.09670)
