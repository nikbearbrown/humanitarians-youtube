# QUESTION

**You have three Claude models that can all do your task — Opus, Sonnet, Haiku
— at three different prices and three different accuracies. How do you know
which one to actually use, without running (and paying for) all three on real
traffic first?**

Redo source: `anthropics/cwc-workshops/youtube/rightmodel-pareto-frontier`
(Teardown register, Code with Claude 2026 Workshop cut on model selection via
the pareto frontier). Facts carried over unchanged from the source's own
worked example — a customer-support classification task: Opus 98% accuracy /
$0.08 per call, Sonnet 90% / $0.04, Haiku 82% / $0.01 — and the per-million-
token cost table (Opus $15/$75, Sonnet $3/$15, Haiku $0.25/$1.25 in/out). The
source's own narration already flags these as illustrative and relative
("check current pricing before you build"); this redo keeps that same caveat
rather than presenting the numbers as live pricing.

Name: General viewer (not attributed).
Channel: @HumanitariansAI — Claude Basics series.
