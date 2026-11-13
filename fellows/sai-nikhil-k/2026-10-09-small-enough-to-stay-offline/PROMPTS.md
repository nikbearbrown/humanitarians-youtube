# PROMPTS — Small Enough to Stay Offline

**There are no open generation slots in this reel.** All eleven beats are registered
Remotion compositions. No image model, no stock, no paid call. A Fellow Tier build end
to end.

## B00 — the on-screen typed ask

> Gavia promises to work offline. If I add an AI assistant, which model will my users' computers actually run, what runs it on Mac, Windows and Linux, and what should it be allowed to do?

## B09 — the handoff prompt (typed on screen and discussed in narration)

> My app has to work offline on Mac, Windows and Linux. Before I add an AI assistant: what is the smallest machine my users have, which model fits it at 4 bits next to my app, how fast does it read a page on the CPU alone — and which of my app's own actions may it call, with 'none' as an allowed answer?

## The executed scripts

| Script | Produces | Deps |
|---|---|---|
| `evidence/local_bench.py` | `local_bench.out`, `.json` → B04, B08; native tool-call results (FACTCHECK) | Ollama 0.30.10 with `qwen3.5:0.8b`, `:4b`, `:9b`; stdlib Python |
| `evidence/llamacpp_constrained.py` | `llamacpp_constrained.out`, `.json` → B05, B06, B08 | Homebrew llama.cpp 0.4.0 (build 10809): `llama-server`, `llama-bench`; the Ollama blobs |
| `evidence/grammar_probe.py` | `grammar_probe.out` (why Ollama's `format` run is not used) | Ollama |
| `evidence/model_facts.py` | `model_facts.out` → B02 | Ollama |
| `evidence/crates_check.py` | `crates_check.out` → B05 | network (crates.io API) |
| `curl` + openpyxl on the OSWorld-Verified results file | `osworld_check.out` → B06 | network |
| fetch / PyMuPDF on the papers and vendor pages | `sources_check.out` → B01, B03, B06, B07 | network |
