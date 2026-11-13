# STEM Video: What Is an Agent Harness? — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video is about agent harnesses — the real layer of software that turns a language model into something that can actually get work done, reliably, over hundreds of steps.

## B00 — Cold open
A one percent difference on a leaderboard can't tell you whether a model drifts off track after fifty steps. That's the real problem a harness exists to solve.

## B01 — The real computer analogy
Method: think of it like a computer. The model is the CPU — raw processing power. The context window is the RAM — limited, volatile working memory. The agent harness is the operating system — it curates context, handles the boot sequence, provides standard drivers for tool calls. The agent itself is just the application running on top.

## B02 — Harness vs. framework vs. SDK
These three get confused constantly, but they're real, different things. A framework gives you building blocks to assemble an agent's logic. An SDK is a vendor's library for calling one specific model's features. A harness is the full operational wrapper — the thing that runs, constrains, and observes the agent once it's actually built.

## B03 — Why this became real infrastructure, not a nice-to-have
Without a harness, a model in production hits real problems: API timeouts, memory limits, tool calls out of sequence, references to functions that don't exist. A harness turns a powerful but non-deterministic model into something enterprise-ready — governed, observable, and verifiable.

## B04 — The real market signal
This isn't theoretical. Real companies selling domain-specific harness layers — Harvey, Legora, Sierra — each crossed a hundred million dollars in annual recurring revenue in 2026. The control a good harness gives you over how an agent actually runs has become something real businesses will pay real money for.

## B05 — Handoff
Your turn. Before building your next agent, ask what's actually managing its context, its tool-call errors, and its long-running state — if the honest answer is "nothing, the model just handles it," that's the harness you don't have yet.

## B06 — Outro
What Is an Agent Harness? Built with Claude, for Humanitarians AI.
