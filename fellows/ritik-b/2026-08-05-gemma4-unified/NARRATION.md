# NARRATION — Gemma 4, Unified?

The spoken script, with **measured** audio durations (Kokoro `am_onyx`).
Durations are ground truth — they are the reel's master clock.

- Beats: 12 · spoken words: 546
- **Runtime: 3m 01.8s** · 3840×2160 @ 24fps
- Channel handle on screen: `@HumanitariansAI` · presenter: Ritik

⚑ = this beat SPEAKS a different line than the one typed on screen.

---

## B00 · ASK ⚑
`ClaudeComposerAsk` · 35 words · **10.84s**

> Google shipped a model that reasons about images and sound with almost no perception hardware in front of it. I want to know what got deleted, and whether anybody proved it was a good idea.

*Typed on screen, not spoken:*

> Gemma 4 twelve B ships a unified, encoder-free multimodal architecture: a thirty-five million parameter matmul where a five hundred and fifty million parameter vision encoder used to be, and no audio encoder at all. Can you help me (1) pin down exactly what was deleted and what replaced it, (2) check whether the technical report actually shows encoder-free matching encoder-based at the SAME parameter count, and (3) separate this kind of convergence from the generator-discriminator unification thread it keeps getting confused with?

## B01 · SUMMARY
`GemmaExecSummary` · 68 words · **19.43s**

> Hi, I'm Ritik, and this video is about one line in Google's Gemma 4 technical report. In June, Google shipped a Gemma 4 that deletes the parts which let a model see and hear. I'll show you what was removed, what replaced it, what the benchmarks actually say, and the experiment the report never runs. If you build multimodal systems, that last one is the part that matters.

## B02 · EXHIBIT
`GemmaEncoderStack` · 54 words · **17.32s**

> Until this spring, you built a multimodal model out of three specialists. A vision transformer to see. A Conformer to hear. A tokenizer for text. Each trained separately, frozen, then bolted onto the front of a language model that does the thinking. Gemma 4 shipped in April with four models built exactly that way.

## B03 · MECHANISM
`GemmaEncoderStack` · 48 words · **17.56s**

> Two months later, Google shipped a fifth model and deleted the eyes. Gemma 4 twelve B takes raw forty-eight by forty-eight pixel patches, and replaces a five hundred and fifty million parameter vision encoder with one matrix multiply. Thirty-five million parameters. Ninety-four percent of the seeing apparatus, gone.

## B04 · MECHANISM
`GemmaEncoderStack` · 42 words · **15.17s**

> Audio went further. Not shrunk. Removed. Raw sixteen kilohertz sound, sliced into forty millisecond frames, projected straight into the space the word embeddings live in. No audio encoder at all. And Google's stated reason is not accuracy. It is latency and memory.

## B05 · PREDICT
`PredictCard` · 22 words · **7.62s**

> Commit before the scores. You just deleted the purpose-built perception hardware out of a perception model. Did it get worse at perceiving?

## B06 · EVIDENCE
`GemmaScoreboard` · 61 words · **19.99s**

> Both. On M M M U Pro the encoder-free twelve B scores sixty-nine point one, against seventy-three point eight for the twenty-six B and seventy-six point nine for the thirty-one B. It loses. But on speech recognition its word error rate is zero point zero six seven, against zero point zero seven five and zero point zero nine zero. It wins.

## B07 · TWIST
`GemmaScoreboard` · 61 words · **20.12s**

> Both of those readings are junk. Sixty-nine against seventy-six is not encoders versus no encoders. It is twelve billion parameters against thirty-one billion. And on audio, it is twelve billion against four point five. Every comparison moves two variables at once. Go looking in the report for the experiment that holds size fixed and toggles the encoder. It is not there.

## B08 · VERDICT
`ClaudeVerdictArtifact` · 52 words · **16.98s**

> So the verdict has three lines. The deletion is real. The efficiency win is real: one stack, trainable end to end, no encode-then-reason hop. And parity with encoders is unproven. Google's own wording is that it performs near the larger twenty-six B at under half the memory. Near. At a different size.

## B09 · REFRAME
`GemmaConvergenceThread` · 68 words · **25.02s**

> One more thing, because these two get conflated constantly. That was encoder convergence, perception folding into the decoder. It is not generators and discriminators collapsing into one architecture. Gemma 4 emits only text. There is no image head. The models that genuinely unify making and judging are Chameleon, Emu three, Show-oh, Transfusion, Janus, and BAGEL. The idea underneath them is the Platonic Representation Hypothesis, and it is contested.

## B10 · HANDOFF ⚑
`ClaudeComposerAsk` · 29 words · **8.32s**

> Your turn. Take the Gemma four technical report and find the ablation I just said was missing. If you find it, I am wrong, and I want to know.

*Typed on screen, not spoken:*

> Your turn. Take the Gemma four technical report and go find the ablation I just told you was missing. If you find it, I am wrong, and I want to know.

## B11 · OUTRO ⚑
`ClaudeTitleOutro` · 6 words · **3.43s**

> Gemma four, unified. Humanitarians A I.

*Typed on screen, not spoken:*

> Gemma 4, Unified?
