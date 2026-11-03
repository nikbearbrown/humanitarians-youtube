# Claude, Cached.

Week 1 STEM video: the KV-cache — why an LLM's text generation "thinks" for
a moment then streams fast. A real systems-level mechanism (prefill vs.
decode), not a UI trick, illustrated with purpose-built Manim diagrams.

| | |
|---|---|
| **Runtime** | 1:35 (94.9s) |
| **Format** | 16:9, 3840×2160 (4K), 24 fps, h264/aac |
| **9:16 cut** | Not yet built (flagged — see BUILD-LOG.md) |
| **Voice** | Kokoro `am_onyx` — local, free, no API |
| **Beats** | 9 · Claude-skin bookends + 5 purpose-built Manim scenes |
| **Presenter** | Sachin Vishaul B |
| **Channel** | @HumanitariansAI (Mycroft) |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd (GATE V: 0 BLOCKER) · solo build, no independent reviewer · not published |

## What this video covers

| Beat | | |
|---|---|---|
| B00 | Cold open | The pause-then-stream feeling, named: the KV-cache |
| B01 | Executive summary | Cache the Key/Value of every past token — never recompute it |
| B02 | Framework | Every token makes a K/V per layer; the past never changes |
| B03 | Worked example (prefill) | The whole prompt's K/V, one parallel pass — the "thinking" pause |
| B04 | Worked example (decode) | One new token, attends to the whole cache — the fast streaming |
| B05 | Falsifiability | The cache grows with every token × layer × head — why long context is expensive |
| B06 | Verdict | Decode is cheap, prefill is not — compute traded for memory |
| B07 | Handoff | Your turn: measure prefill vs. decode latency yourself |
| B08 | Outro | "Claude, Cached." |

## Sourcing

No invented numbers or benchmark figures — every claim is a structural
property of transformer attention (causal masking, K/V dimensionality),
illustrated directly by its own beat's diagram. See `FACTCHECK.md`.
