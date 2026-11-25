# Can You Trust Your AI? How We Test Large Language Models

**Author:** Yeshwanth Balaji · **Channel:** @HumanitariansAI · **Built:** 2026-11-20
**Voice:** Kokoro `am_onyx` (local AI voice) narrating as Yeshwanth Balaji. It is not a recording of me.
**Based on:** Nik Bear Brown, "Enhancing Trust in LLMs: Algorithms for Comparing and Interpreting LLMs", arXiv 2406.01943 (June 2024).

Videos (Google Drive): [AI topic videos](https://drive.google.com/drive/folders/1XhU4MUKToZgao9dtdw6Yh1uxFcJD63n1?usp=sharing)

---

## Subject

A 4:43 explainer for students and early-career engineers who use AI tools every day but have never thought about how they are evaluated. It follows the supplied script's six sections and covers its four learning goals:

1. **Why trust is a real problem.** Hallucination (confident answers that aren't true), bias learned from data, and the black box.
2. **How models are evaluated and compared.** Metrics scored against reference answers, benchmarks (the same test for every model), A/B tests, bias tests, and looking inside the model (embeddings, explanations).
3. **Why human evaluation still matters.** Scores miss tone, context and subtle errors; the survey calls human evaluation "indispensable".
4. **A trust checklist.** Can I verify it? Does rewording change it? Does the reasoning hold? Are the stakes high enough to need a person?

**Takeaway for the viewer:** don't just ask whether an answer sounds right. Ask how you'd know.

## Beats

| Beat | What it shows |
|---|---|
| B00 | Cold open: a Claude composer asks how researchers decide whether a model can be trusted (answer labelled illustrative) |
| B01 | The hesitant writer types "Trusting an AI is a feeling" and corrects it to "is something you measure" |
| B02 | **Required visual:** a confident wrong answer (water boils at 100 °C on Everest) with a red HALLUCINATION stamp, then the true value (about 70 °C) |
| B03 | **Required visual:** three icons: hallucination, bias, black box; "confidence isn't evidence" |
| B04 | **Required visual:** the evaluation toolbox: metrics, benchmarks, A/B tests, bias tests, interpretability, human review |
| B05 | Metrics, with a real calculation: the wrong answer scores 0.87 on word overlap, and a right answer in other words scores 0.25 |
| B06 | Benchmarks and A/B testing side by side; the survey's warning about over-optimizing for a benchmark |
| B07 | A bias test: the same request with one name swapped, the two answers compared (labelled illustrative) |
| B08 | **Required visual:** a real embedding space: 16 words from a small open model, in four clusters; "kitten" lands next to "cat" |
| B09 | Explanations: the faulty reasoning step flagged, black box → glass box, and the survey's caution that attention isn't proof |
| B10 | What scores catch vs what people catch |
| B11 | **Required visual:** the four-point trust checklist |
| B12 | **Required visual:** credit card for Nik Bear Brown, arXiv 2406.01943; the paper is a survey and the examples are ours |
| B13 | Recap: trust is measured, not felt |
| B14 | Your Turn: a prompt that runs the checklist on an AI answer of your own, read aloud and discussed |
| B15 | Title-restate outro with the Humanitarians AI wordmark |

Full narration with measured durations: `script.md`.

## Deliverables

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 beat sheet, the primary source of the film |
| `beat_sheet_vertical.json` | The 9:16 beat sheet: every beat on its native portrait composition, not a crop |
| `make_sheet.py`, `make_vertical.py`, `make_docs.py` | Build the sheets (narration, props, cues on the spoken words; portrait wording) and the shot list, prompts and script |
| `script.md` | Full narration, every beat, with measured durations |
| `evidence/` | The real computations shown on screen, with their scripts: `overlap.py` (ROUGE-1 scores), `embed.py` (embeddings and similarities), `boiling.py` (the Everest boiling point) |
| `src/TrustLLM.tsx` | The nine new Remotion scenes, each with its own 16:9 and 9:16 layout |
| `src/BackgroundAgents.tsx`, `src/Root.tsx.patch` | The checklist, sort and outro scenes reused from the previous film, and the registration of all scenes in the toolkit's `Root.tsx` |
| `FACTCHECK.md`, `SOURCES.md` | Every claim with its source, and the changes made to the supplied script |
| `CHECKS-REPORT.md`, `BUILD-LOG.md`, `SHOTLIST.md`, `PROMPTS.md`, `BUILD-PROMPT.md` | Teaching-arc checks, decisions and deviations, shot list, on-screen prompts, the build commands |
| `TYPECHECK.md`, `TYPECHECK-vertical.md`, `qc/` | The text-size and visual check reports for both masters |

The videos are delivered through Google Drive, not this folder: this folder is text only.

| Video | Size | Duration | SHA-256 |
|---|---|---|---|
| `llm-trust_yeshwanth_16x9.mp4` | 3840×2160 | 283.2 s | `1d3deec0e2361f30510e7f916b1af185bfc5f99e1f9a66968095615eba30d56f` |
| `llm-trust_yeshwanth_9x16.mp4` | 2160×3840 | 283.2 s | `5604372600f59d5a60ff3eaad57cd94c996c1dfda0576d532bff67c2faa6d473` |

## Build notes

- **Toolkit and cost.** Built with the `brutalist.art` toolkit (`ai-explainer` skill) at commit `3a6d397`. Kokoro TTS, Remotion and the embedding model all ran locally and free. No paid API was called and nothing was published.
- **Both ratios are rendered natively** at 4K. The new scenes switch to a phone layout with larger type and less on screen at once. A few portrait cards use shorter wording (the checklist details, the honesty labels) or fuller wording (the recap); the 16:9 cut and the narration keep the full script.
- **New toolkit scenes.** `./art scenes` found no parametric match for these visuals, so nine scenes were added in `src/TrustLLM.tsx`:
  - `TrustHallucination`
  - `TrustThreeProblems`
  - `TrustToolbox`
  - `TrustOverlap`
  - `TrustBenchAB`
  - `TrustCounterfactual`
  - `TrustEmbedding`
  - `TrustReasoning`
  - `TrustCredit`

  Reproducing the render needs `TrustLLM.tsx`, `BackgroundAgents.tsx` and `Root.tsx.patch` applied to the toolkit.
- **Channel.** On @HumanitariansAI, with the Humanitarians AI wordmark as the corner mark and the series label "Irreducibly Human". No person is drawn anywhere in the film.
- **Pronunciation.** The voice says the name Yesh-wunth ba-LAA-jee through a pronunciation lexicon in the beat sheet.
- **Remotion** is 4.0.535 while 4.0.545 is current; I did not upgrade it for this build.

## Honesty notes

- **Two beats are real computations.**
  - B05's scores come from `evidence/overlap.py`, which computes the ROUGE-1 F1 score.
  - B08's points come from `evidence/embed.py`, which runs `all-MiniLM-L6-v2` locally and projects its 384 dimensions to 2 with PCA. I compared four word sets and chose the one that separates most clearly in 2-D, as BUILD-LOG.md records. The positions are not edited.
- **Four beats are illustrative, and the screen says so:** the wrong Everest answer (B02), the benchmark bars and A/B votes (B06), the two reference letters (B07) and the reasoning steps (B09).
- **Two corrections against the paper.** I read the paper in full.
  - It does not mention A/B testing. The toolbox footnote says A/B testing is industry practice.
  - Its fairness section has no name-swap test. The swap is credited to its counterfactual section (§21).
- **The paper is a survey.** It reports no experiments of its own, and the credit beat says so.
- **On-screen quotes are verbatim** from the paper (§5, §13, §20), each cited by section.
- **No figures** about real models: no model names, versions, scores, prices or usage statistics are claimed.
