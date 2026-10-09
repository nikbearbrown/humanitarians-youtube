# PEDAGOGY — Small Enough to Stay Offline

Reel `weekly_updates/2026-10-09-small-enough-to-stay-offline/` · slug `claude-sai-small-enough-to-stay-offline`
· host Sai (Kokoro `am_onyx`) · `@HumanitariansAI` · Computational Skepticism weekly.
Subject: **Sai's research week on a local AI assistant for Gavia** — no release.

Intake (2026-10-09, Sai's words): "In this week I am looking at the potential of using
AI agents in Gavia. Most of this week is research. I am focusing on local LLM models to
keep the app offline. Most of my research was on what parameter model is best for most
of the desktops and also all OS envs. What kind of inferences can we use. What are the
potential applications of these agents? I am talking chatbot, inhouse IT support, help
with app navigation things like that. All the conclusions should be backed by research
going on in local LLMs." He asked for a new folder for it. From Claude's proposals he
chose the ONE idea ("size to the smallest machine") and the title, and asked to **drop**
the B00 line about last week's survey plan (2026-10-09).

## The ONE idea

**Offline means the assistant runs on the user's own computer, so size it for the
small one.** Some new laptops still ship with 8 GB (MacBook Neo, 2026; the best-selling
Core Ultra 5 PC it is measured against). A ~4B model at 4–5 bits is 2.65 GB and writes
39 tokens/s on an M2 Pro's GPU, 23 on its CPU alone. llama.cpp runs it in-process on
all three of Gavia's systems. And its job is Gavia's own actions plus a way to say no —
not driving the screen, and not answering what Gavia's Help doesn't cover.

Two honest edges the reel keeps in view:

- **Everything was timed on one laptop** (M2 Pro, 16 GB, 200 GB/s). The arithmetic
  (B02) is what generalises; the table (B04) is one machine. No speed is claimed for
  any other computer.
- **20 requests is a demo, not a benchmark.** The 20/20 on B06 shows the shape the
  research predicts (TinyAgent, Octopus); it does not prove the assistant is ready.
  The 0.8B's 16/20 under the same rule is kept on screen to say so.

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Can Gavia have an assistant and stay offline? "This is Sai, and this week was research." The ask: which computer, which model, which engine, which job? |
| B01 | THE MACHINES | `ClaudeScienceChipGrid` | 16 GB is the AI-PC floor (Copilot+, MacBook Air 2024) but 8 GB is back (MacBook Neo 2026 and its PC comparison). Gavia ships for three systems. |
| B02 | THE ARITHMETIC | `TypesetMath` | M = N·b/8; r ≤ B/M; 200 GB/s ÷ 2.65 GB ≈ 75.5 tokens/s, worked on the real Qwen3.5 4B file. |
| B03 | THE BITS | `BinaryBranch` | Same memory: bigger at 4 bits beats smaller at 16 (Dettmers & Zettlemoyer); below 4 it breaks (Huang et al.: 6.5 → 8.2 → 210). Apple ~3B @ 3.7 bpw; Gemini Nano 1.8B/3.25B @ 4-bit. |
| B04 | THE RUN | `ExecutedData` | Measured: 4B 38.8 / 9B 25.4 tokens/s on the GPU; 23.3 / 8.3 on the CPU alone. |
| B05 | THE ENGINE | `DivergentFates` | ONNX Runtime GenAI (the engine Gavia ships; no official Rust API, its one community binding has 140 downloads) vs llama.cpp in-process (Metal/Vulkan/CUDA/CPU; community binding `llama-cpp-2`, 1.5M downloads; enforced Gavia's schema 40/40). Web view: no WebGPU on Linux; Ollama: a second install. |
| B06 | THE BUTTONS | `BinaryBranch` | Pixels vs the app's own actions: ≤9B best 46% on OSWorld (people 72%); TinyAgent 1.1B 80% vs GPT-4-Turbo 79%; here, 4B held to Gavia's list: 20/20. Ghost: 0.8B 16/20. |
| B07 | HELP AND IT | `DivergentFates` | Chat help and IT support = answering from what is written down. Retrieval helps (Lewis 2020); abstaining is rare (FaithEval: Llama 3.1 8B 38%); the support-desk gain (+15%, QJE) had a person fixing. |
| B08 | VERDICT | `ClaudeVerdictArtifact` | One page, four bare sentences. |
| B09 | HANDOFF | `ClaudeComposerAsk` (`greeting: "Your turn."`) | Start from your users' smallest machine. Read aloud and discussed. |
| B10 | OUTRO | `LogoOutro` | "Small enough to stay offline. Sai." (6 words, inside the 4 s card) |

## ILLUSTRATE LAW check

- Claude UI only at B00, B08, B09. ✔
- Every body beat illustrates (grid, equation, fork, measured rows, two split paths). ✔
- No two consecutive body beats share a pattern: ChipGrid · TypesetMath · BinaryBranch ·
  ExecutedData · DivergentFates · BinaryBranch · DivergentFates (asserted by
  `build_beats.py --check`). ✔
- SHOW-DON'T-TELL: every beat has an ordered `show` block in `beat_sheet.json`. ✔
- MATH + EVIDENCE: B02's algebra is worked on the model file's own numbers
  (`evidence/model_facts.out`); B04 is a run made for this video (`evidence/local_bench.out`). ✔
- No positional references in narration ("the top row"): one mp3 serves both aspects. ✔

## 9:16 constraint

`shorts.py --vertical` builds the same film. Every pattern has a registered `*916`
sibling in `Root.tsx`: ClaudeComposerAsk916, ClaudeScienceChipGrid916, TypesetMath916,
BinaryBranch916, ExecutedData916, DivergentFates916, ClaudeVerdictArtifact916,
LogoOutro916. No user media, so nothing needs a hand-made pantry plate.

## Evidence and honesty

Every number on screen was re-measured or re-read at its source for this video
(details in FACTCHECK.md, disagreements in SOURCES.md):

- `local_bench.out` — Qwen3.5 0.8B / 4B / 9B in Ollama 0.30.10 on this M2 Pro: decode
  and prompt speed on GPU and CPU, plus 20 Gavia requests with native tool calling.
- `llamacpp_constrained.out` — the same 20 requests through llama.cpp's own server with
  Gavia's action list enforced as a grammar, and llama-bench as a speed cross-check.
- `grammar_probe.out` — why the Ollama "format" run is not used: the schema was not
  enforced (asked for a poem with the schema attached, both models wrote a poem).
- `model_facts.out` — parameter counts, file sizes and bits per weight.
- `osworld_check.out` — the OSWorld-Verified results file.
- `sources_check.out` — every paper and vendor figure, re-read at the source.
- `ollama_toolcall_failure.out` — the 0.8B's malformed tool calls and the stalls after.
- `crates_check.out` — the Rust bindings' versions and download counts (crates.io).

Corrections against the research passes:

- One research pass gave "AutoGLM-OS-9B 48.03%" as the best small OSWorld model; it is
  not in the verified results file. The reel uses EvoCUA-8B, **46.06%**.
- The support-desk study is quoted from the published QJE version (5,172 agents, +15%),
  not the 2023 NBER draft (5,179 agents, +14%).
- Phi Silica's "3.3B" is press coverage only; the reel does not use it.
- Neither engine publishes its own Rust binding: `llama-cpp-2` (utilityai) and
  `onnx-genai` (justinchuby) are both community crates. The draft card said ORT was
  "Rust only through third parties" as if llama.cpp were not; B05 now compares the two
  bindings by the same measure (downloads, crates.io, 2026-10-09).

Measurement notes the reel does not hide:

- The 9B's CPU runs were unstable (4.7, 8.3, 15.9 tokens/s); B04 says so.
- Ollama's prompt-reading speeds come from a 244-token prompt and differ from
  llama-bench's 512-token figures; the reel shows no prompt speed, only "CPUs read slowly".
- In Ollama's native mode the 0.8B wrote a malformed tool call; Ollama answered HTTP 500
  and its runner then stopped answering until restarted, every time. Not on screen — it is
  a bug in one Ollama build — but it is why the reel recommends an enforced list.

**Continuity with last week's reel** (2026-10-02, B06): it ended "there is no whole
folder yet, no single total of loons, and no CSV. Those are next on the roadmap." The
draft B00 said the week went to research instead; **Sai asked for that line to be
dropped** (2026-10-09). B00 now says only "this week was research" — true, and it
contradicts nothing last week said.

**Not claimed:** speed on any machine but this one; that the assistant exists (it does
not — this is research); adoption or download figures; that a small model can fix a
computer (no study found one doing end-user IT support).

## Attribution

The research and the week are Sai's. Claude ran the research passes, the benchmarks and
the source checks for this video at his request. The only commit in the Gavia repo since
2026-10-02 is a Dependabot bump (`3099d47`, unmerged branch), so no collaborator work is
narrated.

## Attribution override

Hosted by Sai in his own name (B00 "This is Sai", B10 "Sai."), voice Kokoro `am_onyx`,
handle `@HumanitariansAI`. The guide's IN-FOR-BEAR LAW is deliberately suspended for this
series (`metadata.greeting_note`).

## Expected build noise (not bugs)

- `./art run` SKIN LINT asks for `ClaudeTitleOutro` — wrong for this channel; `LogoOutro`
  is deliberate.
- GATE V `underfill` on B08/B10 (centred cards); B10 declares `qc.sparse`.
- The portrait slate reports edge-bleed on every frame (its own burn-in); the verdict
  that counts is `./art final`'s gate on the clean candidate.

## Portrait-only edits (in `vertical/beat_sheet.json`, not the parent)

**One** (2026-10-09 frame review): B03 `data.question` →
`"Same memory: bigger at 4 bits, or smaller at 16?"`. The parent's 68-character question
wraps to three lines in `BinaryBranch916`'s fixed-height card and the third line sits on
the border. Re-render with `remotion_scenes.py vertical --force --only B03`. Re-apply after
every `shorts.py --vertical`.

## Review checklist (Sai)

- [x] The ONE idea and the title are yours (chosen 2026-10-09).
- [x] Left out at your request: last week's survey plan (B00).
- [ ] Nothing else here should be left out of a public video.
- [ ] The conclusions (4B at 4–5 bits; llama.cpp; actions + "none") match your reading.

## Narration

<!-- NARRATION:BEGIN (generated by fill_narration.py — do not edit by hand) -->

### B00 · ASK — `ClaudeComposerAsk` · 16.5s measured (58 words)

> Can Gavia have an assistant you can ask for help, without breaking its promise
> to stay offline? This is Sai, and this week was research. Offline means the
> model runs on your own computer. Which computer, though? Which model fits it,
> what runs that model on Mac, Windows and Linux, and what should it be allowed
> to do?

### B01 · THE MACHINES — `ClaudeScienceChipGrid` · 20.6s measured (66 words)

> Start with the machines. Microsoft's AI PCs need sixteen gigabytes, and in
> twenty twenty-four Apple moved the MacBook Air to sixteen. But eight has not
> gone away: Apple's cheapest laptop this year has eight, and so does the best-
> selling PC laptop it is measured against. Gavia ships for all three systems,
> so the assistant has to fit in eight gigabytes, beside everything else that is
> open.

### B02 · THE ARITHMETIC — `TypesetMath` · 21.2s measured (69 words)

> Two lines of arithmetic decide most of this. The weights take parameters times
> bits per weight, over eight, in bytes. Writing each token reads every weight
> once, so speed is capped by memory bandwidth over that size. Here: four point
> two billion parameters at about five bits is two point six five gigabytes, and
> two hundred gigabytes a second over that is a ceiling near seventy-five tokens
> a second.

### B03 · THE BITS — `BinaryBranch` · 25.8s measured (82 words)

> Why five bits, not sixteen? In the same memory, a bigger model at four bits
> beats a smaller one at full precision: over thirty-five thousand experiments,
> Dettmers and Zettlemoyer found four bits almost universally optimal. Below
> four, it breaks. For Llama three's eight-billion model, perplexity, where
> lower is better, goes from six point five at four bits to eight point two at
> three, and two hundred and ten at two. Apple and Google chose about three
> billion parameters, at about four bits.

### B04 · THE RUN — `ExecutedData` · 19.5s measured (62 words)

> Then I timed two sizes of Kwen three point five on this laptop. On the
> graphics chip, the four-billion writes thirty-nine tokens a second, the nine-
> billion twenty-five. On the CPU alone, twenty-three and eight. So the four-
> billion on a plain CPU keeps pace with the nine-billion on a GPU. And the
> nine-billion's CPU runs swung from five to sixteen, run to run.

### B05 · THE ENGINE — `DivergentFates` · 22.6s measured (83 words)

> What runs it? The obvious answer is the engine Gavia already ships, Onix
> Runtime, with its add-on for language models. But Gavia is Rust, and that add-
> on's only Rust binding has a hundred and forty downloads. A model in the web
> view fails on Linux, whose web view has no WebGPU yet. Ollama is a second app
> to install. Llama dot C P P's Rust binding has one and a half million, and it
> runs on Metal, Vulkan, CUDA or a plain CPU.

### B06 · THE BUTTONS — `BinaryBranch` · 22.9s measured (77 words)

> So what should it do? Not drive the screen by its pixels: the best model under
> ten billion parameters finishes forty-six percent of desktop tasks, where
> people finished seventy-two. Given an app's own actions, though, a one point
> one billion model matched GPT-4 Turbo. So I gave Kwen Gavia's: its pages, its
> themes, its update switch, plus eight requests it can't do. Held to that list
> by llama dot C P P, the four-billion got all twenty.

### B07 · HELP AND IT — `DivergentFates` · 19.6s measured (66 words)

> Chat help and IT support are one problem: answering from what is written down.
> Retrieve the right page first, and answers get more factual. The danger is the
> page without the answer. In FaithEval, an eight-billion Llama said so only
> thirty-eight percent of the time. And in a study of over five thousand support
> agents, the fifteen percent gain came with a person doing the fixing.

### B08 · VERDICT — `ClaudeVerdictArtifact` · 17.5s measured (62 words)

> So: one page. Offline means the assistant runs on the user's own computer, and
> some new ones still have eight gigabytes. A four-billion model at four to five
> bits fits, and is fast enough. Llama dot C P P runs it on all three systems.
> And it should press Gavia's own buttons, answer from Gavia's Help, and say so
> when it can't.

### B09 · HANDOFF — `ClaudeComposerAsk` · 15.6s measured (58 words)

> Your turn. Building an assistant into an app that has to stay offline? Paste
> this. Start from your users' smallest machine, not yours. Ask what fits there
> at four bits, and how fast it reads a page with no graphics chip. Then list
> your app's own actions, and give the model a way to say none of them.

### B10 · OUTRO — `LogoOutro` · 2.8s measured (6 words)

> Small enough to stay offline. Sai.

**Total: 689 words** → 204.7s measured (3:24). No 180s cap applies to the --vertical cut; audio remains the master clock.

<!-- NARRATION:END -->

VERDICT: __________ — reviewer: ___ date: ___
