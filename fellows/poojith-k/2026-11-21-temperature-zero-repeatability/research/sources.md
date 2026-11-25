# Research and claim ledger

Checked 2026-11-21. Primary sources govern the script. The source-location line numbers below refer to the retrieved page text and are supplemented by headings and paragraph openings for independent lookup.

## Sources

- S1 · [Horace He with Thinking Machines Lab, Defeating Nondeterminism in LLM Inference, September 10, 2025](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
- S2 · [Thinking Machines Lab, batch_invariant_ops companion library](https://github.com/thinking-machines-lab/batch_invariant_ops)
- S3 · [David Goldberg, What Every Computer Scientist Should Know About Floating-Point Arithmetic, March 1991, authorized edited reprint](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
- S4 · [PyTorch Reproducibility documentation, version 2.15](https://docs.pytorch.org/docs/2.15/notes/randomness.html)

## Short exact excerpts

| Source | Exact excerpt | Exact location |
| --- | --- | --- |
| S1 | “highest probability token” | Introduction, temperature-zero footnote, retrieved line 25. |
| S1 | “CPUs or TPUs” | Batch invariance and “determinism”, paragraph beginning “In other words”, retrieved line 150. |
| S1 | “all of our 1000 completions are identical.” | Experiments → How nondeterministic are completions?, final paragraph, retrieved line 231. |
| S2 | “an example of achieving deterministic vLLM inference.” | README, opening paragraph under Batch Invariant Ops, retrieved line 182. |
| S3 | “must often be rounded” | Rounding Error, second sentence after the opening paragraph, retrieved line 38. |
| S3 | “the associative laws of algebra do not necessarily hold” | Systems Aspects → Languages and Compilers → Ambiguity, paragraph beginning “Another grey area”, retrieved line 708. |
| S4 | “Completely reproducible results are not guaranteed across PyTorch releases, individual commits, or different platforms.” | Reproducibility, opening paragraph, retrieved line 416. |
| S4 | “throw an error” | Avoiding nondeterministic algorithms, opening paragraph, retrieved line 456. |

Total direct quotation stays below 25 words per source. The following rows paraphrase the evidence and separate editorial inference from reported experiments.

## Claim map

| ID | Claim and beats | Evidence location and scope |
| --- | --- | --- |
| C0 | Presenter identity, exact introduction, AI disclosure and sign-off, B00/B07/B99. | Presenter brief. Production description refers to the approved planned Kokoro narration. |
| C1 | Greedy decoding selects the top token and removes the sampling draw, B01. | S1 Introduction, temperature-zero footnote, line 25. A token is described in ordinary language as a piece of text. The claim concerns this decoding choice. |
| C2 | Arithmetic uses finite precision and rounds. Regrouping an addition can change its answer, B02. | S3 Rounding Error, opening paragraphs, lines 37–38, and Languages and Compilers → Ambiguity, line 708. Goldberg gives an explicit reordered-sum example. |
| C3 | A small score perturbation can switch a near-tie. A changed token can alter later output, B02. | Mathematical consequence of greedy selection in C1 applied to C2. S1 Experiments → How nondeterministic are completions?, lines 229–231, supplies an observed output divergence. “Can” expresses possibility. No claim that every later token must change. |
| C4 | A server batches requests. Batch size can change the arithmetic path. Changing load makes the effective batch vary for a caller, B03. | S1 Batch invariance and “determinism”, paragraphs beginning “To explain batch invariance” and “However, when a non-batch-invariant kernel”, lines 127–150. |
| C5 | A kernel may repeat for fixed inputs yet vary with the batch. CPU and TPU endpoints can share this source of variation. GPU concurrency alone does not explain it, B04. | S1 same section, lines 127, 145–150. Why don't kernels always add numbers in the same order? and When are atomic adds needed?, lines 103–119. Scope is the mechanism described, not a claim that all kernels or stacks behave identically. |
| C6 | Batch-invariant kernels preserve the relevant arithmetic as batching changes. The authors obtained identical completions in a test, B05. | S1 How do we make kernels batch-invariant? → RMSNorm, line 166, and Batch-invariant attention, lines 201–221. Experiments → How nondeterministic are completions?, lines 229–231. S2 README Overview and Deterministic Inference in vLLM, lines 180–185 and 237–239, and the supplied example. |
| C7 | The demonstration took longer. An attention optimization reduced that overhead and still trailed the default in that test, B05. | S1 Experiments → Performance, lines 234–243. This is an implementation-specific timing comparison, not a universal penalty for deterministic inference. |
| C8 | PyTorch can choose deterministic algorithms or raise an error where a required alternative is absent, B06. | S4 Avoiding nondeterministic algorithms, opening paragraph, lines 454–466. |
| C9 | PyTorch gives no complete cross-release or cross-platform reproducibility guarantee, including CPU versus GPU, B06. | S4 Reproducibility, opening paragraph, line 416. |
| C10 | Keep the system configuration controlled. Repeat tests when repeatability is uncertain and report observed variation, B07. | Editorial evaluation practice drawn from C1–C9. The script states a practical response, not a measured scientific result. |

## Experiment identity and scope

S1's completions experiment uses exactly `Qwen/Qwen3-235B-A22B-Instruct-2507`, non-thinking mode, one thousand completions of one thousand tokens from the Feynman prompt. It reports eighty unique outputs with the original setup and one unique output with its batch-invariant kernels. S1 does not specify a GPU model for this completion experiment.

S1's separate performance test uses Qwen-3-8B on one GPU with one thousand requests and output lengths from ninety to one hundred ten tokens. The table reports 26 seconds for default vLLM, 55 seconds for the unoptimized deterministic implementation and 42 seconds with improved attention. The GPU model is not named in that table. These model identities and workloads must stay separate.

S2's example uses `Qwen/Qwen3-8B`, one thousand requests and at most one hundred generated tokens, with temperature zero. Its README reports eighteen unique samples before the integration and one afterward. This is separate from S1's larger-model completion experiment. Code paths and the example service address are excluded from this episode.

The episode uses the qualitative findings, with no model-size or benchmark-number headline. No hardware model is inferred from instruction-set examples elsewhere in S1.

## Changes from the supplied outline

1. Changed “top word” to “top token”, and defined a token as a piece of text.
2. Replaced “any variation has to come from the arithmetic” with a whole-system account. Greedy decoding removes its random draw. It does not hold model weights, software, hardware or every other input fixed.
3. Replaced “everything after it changes” with “later text can diverge”. A score flip changes the next context without guaranteeing that every subsequent token differs.
4. Presented batching as an important mechanism demonstrated by the authors. The script distinguishes a kernel repeating at one fixed batch from its output changing across batch shapes.
5. Named CPU and TPU servers as the other processor settings mentioned in S1. No inference that all nondeterminism is due to GPUs or racing threads.
6. Kept the deterministic completion demonstration separate from the smaller-model performance workload. Omitted hardware-model guesses and numerical benchmark headlines.
7. Described optimization as reducing the measured overhead while remaining slower in that test. No promise of zero overhead or universal cost.
8. Added the documented scope of PyTorch determinism controls and the distinction between choosing an algorithm and guaranteeing an entire application.
9. Kept the closing repeat-testing guidance as editorial advice for uncertain repeatability. The takeaway states both token choice and consistent computation.
