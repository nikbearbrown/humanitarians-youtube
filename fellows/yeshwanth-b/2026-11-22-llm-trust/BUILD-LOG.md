# BUILD-LOG — claude-hai-llm-trust

Decisions and deviations, newest last.

- **Skill and channel.** `ai-explainer` on the `claude-hai` channel, the same as the Background AI Agents film (2026-11-10), at Yeshwanth's standing request. The narrator persona is Yeshwanth Balaji ("Ciao, this is Yeshwanth Balaji"; greeting "Ciao, Yeshwanth", a new language for the batch). The voice is the local AI voice Kokoro `am_onyx` at speed 0.95; it is not a recording of Yeshwanth. The name is pronounced through the sheet's `pronounce` lexicon (Yesh-wunth ba-LAA-jee). Chips and corner marks read @HumanitariansAI; the kicker is the channel's fixed "Irreducibly Human" (`runtime/qc/brand_labels.json`).
- **No Professor Bear portrait.** No beat needs a person, and none is drawn. This follows Yeshwanth's earlier request.
- **Library first.** `./art scenes` found no parametric match for the stamp, three-problem, toolbox, overlap-score, benchmark/A-B, counterfactual, embedding-map, reasoning and credit beats, so nine scenes were added in `runtime/remotion/src/scenes/TrustLLM.tsx` and registered in both ratios. `AgentChecklist`, `AgentFitSort` and `ChannelTitleOutro` from the previous film were reused. `./art scene-index` was run.
- **Paper check.** A full read of arXiv 2406.01943 found that A/B testing is not in the paper and that its fairness section has no name-swap test. Both ideas stay in the film with honest credit (see SOURCES.md).
- **Executable evidence.**
  - `evidence/overlap.py` computes ROUGE-1 for the two Everest answers: wrong 0.87, right 0.25.
  - `evidence/embed.py` runs all-MiniLM-L6-v2 locally. Four candidate word sets were compared by 2-D silhouette (0.62, 0.68, 0.65, 0.70). The first set tried (with vehicles) put animals and vehicles on top of each other in 2-D. The film uses the clearest set (animals, fruit, sports, music; silhouette 0.70). The points are the real PCA projection; only label placement (left/right/above/below) was chosen, so labels don't collide.
  - `evidence/boiling.py` checks the hook's physics: 71.9 °C at summit pressure, said as "about 70".
- **Spoken "A/B".** Kokoro read "A B testing" as "uh B"; the narration text says "A-B testing" (phonemes ˈeɪbˈiː). Screens show "A/B".
- **First frame review (16:9).** The stamp covered the answer text, so it moved below the text. The embedding labels hid "cat" under "kitten" and stacked football on soccer, fixed with label sides. Several beats left too much empty canvas (FILL-THE-CANVAS), so the hallucination, three-problem, benchmark, reasoning and credit beats were scaled up. The overlap beat's quote card sat under the corner mark and was narrowed. Seven beats were re-rendered.
- **Remotion** is 4.0.535 while 4.0.545 is current; not upgraded for this build (an upgrade means re-rendering and re-gating the reels still shipped).
- **GATE T, first pass: FAIL** (16:9: 4 beats; 9:16: 8 beats). The checker measures each word's ink height, so lowercase-only words ("as", "for", "air") are judged by their x-height. Fixes, made in scene source, not the checker:
  - Every Trust scene got a dedicated phone layout (serif 92, sans 72, mono 70 on the 1080×1920 canvas), with less on screen at once. In portrait the embedding map labels clusters, not all 16 words; the overlap beat drops the reference row; the reasoning beat shows the survey quote after the glass-box moment instead of beside it. Portrait honesty labels are short ("Illustrative", "Real model, run locally").
  - 16:9: counterfactual and reasoning text enlarged; the benchmark bars returned to 24 px, since the 34 px terracotta bar was read as accent text (contrast); the embedding note was cut to 12 words (no-wordy-card).
- **GATE T, later passes.** Some portrait shapes were read as text runs: the benchmark bars (raised to 52 px), the embedding dots (larger radius) and strikethrough lines, which cut glyphs into fragments. Faulty reasoning steps are now marked ✕ in red instead of struck through. GATE T then passed in both ratios.
- **Gate V on 9:16:** one BLOCKER and three MAJOR defects.
  - B07: the ✓/✕ marks sat on the right safe edge; the rows are now inset.
  - B05: half the frame was empty before the second card's cue; both cards now show dimmed from the start.
  - B13: the shared `ClaudeVerdictArtifact916` card sets small type and underfilled the frame. The toolkit component was not changed. The portrait recap uses fuller wording of the same four points, plus the closing line (`make_vertical.py`); the 16:9 recap keeps its short lines.
